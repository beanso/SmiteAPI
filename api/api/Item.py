__author__ = 'Benno'
from lxml import etree, objectify
from API import SmiteAPI
import simplejson


class Item:

    name = None
    description = None
    secondary_description = None
    stats = None  # menuitems
    itemid = None
    price = None

    def __init__(self, str):
        obj = simplejson.loads(str)

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
