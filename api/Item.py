__author__ = 'Benno'
from lxml import etree, objectify
from API import SmiteAPI

class Item:

    name = None
    description = None
    secondary_description = None
    stats = None #menuitems
    itemid = None
    price = None


    def __init__(self, xml_string):
        xml_string = xml_string.replace('xmlns="http://schemas.datacontract.org/2004/07/SmiteApi"', "")
        tree = objectify.fromstring(xml_string)

        self.name = tree.DeviceName
        self.description = tree.ItemDescription.Description
        self.secondary_description = tree.ItemDescription.SecondaryDescription
        self.itemid = tree.ItemId
        self.price = tree.Price

        self.stats = []
        for item in tree.ItemDescription.Menuitems.iterchildren():
            dict = {}
            dict["description"] = item.Description
            dict["value"] = item.Value
            self.stats.append(dict)



