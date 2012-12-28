__author__ = "Benno Tremback"

from API import SmiteAPI
import simplejson as json
from datetime import datetime
import pytz
from dateutil import parser
from abc import ABCMeta, abstractmethod


class G:
    pass

G.s = SmiteAPI()


class ApiObject(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def model_dict(self):
        """
        Return a dict of kwargs for inserting into database
        """
        return

    def parse_value(self, value):
        parsed = None

        if isinstance(value, float):
            parsed = float(value)
        if isinstance(value, int):
            parsed = int(value)
        if isinstance(value, datetime):
            parsed = parser.parse(value).replace(tzinfo=pytz.utc)
        if isinstance(value, str):
            parsed = value

        return parsed


class Item:

    name = None
    description = None
    secondary_description = None
    stats = None  # menuitems
    itemid = None
    price = None

    def __init__(self, str):
        obj = json.loads(str)

        self.name = obj["DeviceName"]
        self.description = obj["ItemDescription"]["Description"]
        self.secondary_description = obj["ItemDescription"]["SecondaryDescription"]
        self.itemid = obj["ItemId"]
        self.price = obj["Price"]

        self.stats = []
        for item in obj["ItemDescription"]["Menuitems"]:
            dict = {}
            dict["description"] = item["Description"]
            dict["value"] = item["Value"]
            self.stats.append(dict)


class GetItems():
    items = []

    def __init__(self, lang='1'):
        response = G.s.get_items(lang)
        obj = json.loads(response)

        for root in obj:
            item = Item(json.dumps(root))
            self.items.append(item)

        for item in self.items:
            print item.name


class GetMatchDetails():
    data = {}

    def __init__(self, mapid):
        response = G.s.get_match_details(mapid)
        obj = json.loads(response)

        for tag, value in obj[0].iteritems():
            self.data[tag] = value


class MatchSummary(ApiObject):
    data = None

    def __init__(self, json_str):
        root = json.loads(json_str)

        for key, value in root.iteritems():
            self.data[key.lower()] = value
