__author__ = 'Benno'
from lxml import objectify, etree
from Item import Item

class ItemList:

    items = []

    def __init__(self, xml_string):
        xml_string = xml_string.replace('xmlns="http://schemas.datacontract.org/2004/07/SmiteApi"', "")
        tree = objectify.fromstring(xml_string)

        for item_root in tree.iterchildren():
            item = Item(etree.tostring(item_root))
            self.items.append(item)

        for item in self.items:
            print item.name

    def update(self):
        import os
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
        from Smitedb import models
        from API import SmiteAPI

        s = SmiteAPI()
        list_string =