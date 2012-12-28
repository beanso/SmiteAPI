__author__ = 'Benno'
from lxml import objectify, etree
from item import Item
import simplejson as json


class ItemList:

    items = []

    def __init__(self, str):
        obj = json.loads(str)

        for root in obj:
            item = Item(json.dumps(root))
            self.items.append(item)

        for item in self.items:
            print item.name

    def update(self):
        return
