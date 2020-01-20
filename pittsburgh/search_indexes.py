from councilmatic_core.haystack_indexes import BillIndex
from haystack import indexes
from .models import PittsburghBill
from datetime import datetime
from django.conf import settings
import pytz

app_timezone = pytz.timezone(settings.TIME_ZONE)


class PittsburghBillIndex(BillIndex, indexes.Indexable):
    topics = indexes.MultiValueField(faceted=True)

    def get_model(self):
        return PittsburghBill

    def prepare(self, obj):
        data = super(PittsburghBillIndex, self).prepare(obj)

        boost = 0
        if obj.last_action_date:
            now = app_timezone.localize(datetime.now())

            # obj.last_action_date can be in the future
            weeks_passed = (now - obj.last_action_date).days / 7 + 1
            boost = 1 + 1.0 / max(weeks_passed, 1)

        data['boost'] = boost

        return data

    def prepare_topics(self, obj):
        return obj.topics

    def prepare_last_action_date(self, obj):
        app_timezone = pytz.timezone(settings.TIME_ZONE)

        if not obj.last_action_date:
            index_actions = [a.date for a in obj.actions.all()]

            if index_actions:
                index_actions = max(index_actions)

            return index_actions

        return obj.last_action_date
