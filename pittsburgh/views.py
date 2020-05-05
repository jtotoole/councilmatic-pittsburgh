from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django.urls import reverse

from datetime import date, timedelta, datetime

from pittsburgh.models import PittsburghBill, PittsburghEvent, PittsburghPerson
from councilmatic_core.views import *

from haystack.query import SearchQuerySet

from django.db.models import DateTimeField
from django.db.models.functions import Cast
from councilmatic.settings_jurisdiction import MANUAL_HEADSHOTS, CONTACT_INFO


class PittsburghIndexView(IndexView):
    template_name = 'pittsburgh/index.html'
    bill_model = PittsburghBill
    event_model = PittsburghEvent

    def last_meeting(self):
        return PittsburghEvent.most_recent_past_city_council_meeting()


class PittsburghAboutView(AboutView):
    template_name = 'pittsburgh/about.html'


class PittsburghEventsView(EventsView):
    template_name = 'pittsburgh/events.html'
    event_model = PittsburghEvent


class PittsburghEventDetailView(DetailView):
    template_name = 'pittsburgh/event.html'
    model = PittsburghEvent

    def get_context_data(self, **kwargs):
        context = super(PittsburghEventDetailView, self).get_context_data(**kwargs)
        event = context['event']


class PittsburghCouncilMembersView(CouncilMembersView):
    template_name = 'pittsburgh/council-members.html'
    person_model = PittsburghPerson

    def get_context_data(self, **kwargs):
        context = super(PittsburghCouncilMembersView, self).get_context_data(**kwargs)

        posts = context['posts']

        for post in posts:
            if post.current_member.person.slug in MANUAL_HEADSHOTS:
                post.current_member.person.headshot = '/static/images/' + \
                                                          MANUAL_HEADSHOTS[post.current_member.person.slug]['image']

        return context


class PittsburghPersonDetailView(PersonDetailView):
    template_name = 'pittsburgh/person.html'
    person_model = PittsburghPerson

    def get_context_data(self, **kwargs):
        context = super(PittsburghPersonDetailView, self).get_context_data(**kwargs)

        person = context['person']

        if person.latest_council_membership:
            context['tenure_start'] = person.latest_council_membership.start_date_dt.strftime("%B %d, %Y")

        context['chair_positions'] = person.chair_role_memberships

        if person.slug in CONTACT_INFO:
            context['phone'] = CONTACT_INFO[person.slug]['phone']
            context['website'] = CONTACT_INFO[person.slug]['website']
            context['email'] = CONTACT_INFO[person.slug]['email']
            context['twitter_handle'] = CONTACT_INFO[person.slug]['twitter']['handle']
            context['twitter_url'] = CONTACT_INFO[person.slug]['twitter']['url']

        if person.slug in MANUAL_HEADSHOTS:
            person.headshot = 'images/' + MANUAL_HEADSHOTS[person.slug]['image']

        context['feedback_url'] = 'https://pittsburghpa.gov/council/d{}-feedback'.format(person.current_council_seat.
                                                                                         split(' ')[1])
        return context


class PittsburghCouncilmaticFacetedSearchView(CouncilmaticFacetedSearchView):

    def build_form(self, form_kwargs=None):
        form = super(CouncilmaticFacetedSearchView, self).build_form(form_kwargs=form_kwargs)

        # For faceted search functionality.
        if form_kwargs is None:
            form_kwargs = {}

        form_kwargs['selected_facets'] = self.request.GET.getlist("selected_facets")

        # For remaining search functionality.
        data = None
        kwargs = {
            'load_all': self.load_all,
        }

        sqs = SearchQuerySet().facet('bill_type') \
            .facet('sponsorships', sort='index') \
            .facet('controlling_body') \
            .facet('inferred_status') \
            .facet('topics') \
            .facet('legislative_session') \
            .highlight()

        if form_kwargs:
            kwargs.update(form_kwargs)

        dataDict = {}
        if len(self.request.GET):
            data = self.request.GET
            dataDict = dict(data)

        if self.searchqueryset is not None:
            kwargs['searchqueryset'] = sqs

            if dataDict.get('sort_by'):
                for el in dataDict['sort_by']:
                    if el == 'date':
                        if dataDict.get('order_by') == ['asc']:
                            kwargs['searchqueryset'] = sqs.order_by('last_action_date')
                        else:
                            kwargs['searchqueryset'] = sqs.order_by('-last_action_date')
                    if el == 'title':
                        if dataDict.get('order_by') == ['desc']:
                            kwargs['searchqueryset'] = sqs.order_by('-sort_name')
                        else:
                            kwargs['searchqueryset'] = sqs.order_by('sort_name')
                    if el == 'relevance':
                        kwargs['searchqueryset'] = sqs

            elif dataDict.get('q'):
                kwargs['searchqueryset'] = sqs
            else:
                kwargs['searchqueryset'] = sqs.order_by('-last_action_date')

        return self.form_class(data, **kwargs)
