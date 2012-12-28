__author__ = 'Benno'
import re
from abc import ABCMeta, abstractmethod
from dateutil import parser
import datetime
from django.utils.timezone import utc


class Command(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def model_dict(self):
        """
        Return a dict of kwargs for inserting into database
        """
        return

    def clean_xml(self, xml):  # Remove useless namespace defaults from the XML
        xml = re.sub('xmlns=".+" (?=xmlns)', "", xml)
        xml = re.sub('i:', "", xml)
        return xml

    def parse_value(self, value):
        parsed = None

        if isinstance(value, float):
            parsed = float(value)
        if isinstance(value, int):
            parsed = int(value)
        if isinstance(value, datetime):
            parsed = parser.parse(value).replace(tzinfo=utc)
        if isinstance(value, str):
            parsed = value

        return parsed
