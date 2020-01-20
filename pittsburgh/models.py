from django.conf import settings
from django.db import models
from django.utils.html import mark_safe
from councilmatic_core.models import Bill, Event, Person
from councilmatic.settings_jurisdiction import MANUAL_HEADSHOTS
from datetime import datetime
import pytz
import re
from urllib.parse import quote

app_timezone = pytz.timezone(settings.TIME_ZONE)

class PittsburghBill(Bill):

    class Meta:
        proxy = True
        app_label = 'pittsburgh'


class PittsburghEvent(Event):

    class Meta:
        proxy = True
        app_label = 'pittsburgh'


class PittsburghPerson(Person):
    def get_headshot(self):
        if self.slug in MANUAL_HEADSHOTS:
            self.headshot.url = 'images/' + MANUAL_HEADSHOTS[self.slug]['image']