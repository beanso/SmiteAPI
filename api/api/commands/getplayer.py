__author__ = 'Benno'

from dateutil import parser
from lxml import etree, objectify
from django.utils.timezone import utc
import re
from Smite.api.commands.command import Command


class GetPlayer(Command):
    data = {}

    def __init__(self, xml_string):
        xml_string = self.clean_xml(xml_string)
        tree = objectify.fromstring(xml_string)
        tree = tree.player
        for child in tree.iterchildren():
            self.data[child.tag.lower()] = self.parse_value(child.text)
#        root = ET.fromstring(xml)
#        player_root = root[0]
#        ns = "{http://schemas.datacontract.org/2004/07/SmiteApi}"

        self.created = parser.parse(tree.Created_Datetime.text).replace(tzinfo=utc)
        self.last_login = parser.parse(tree.Last_Login_Datetime.text).replace(tzinfo=utc)
        self.leaves = int(tree.Leaves)
        self.level = int(tree.Level)
        self.losses = int(tree.Losses)
        self.wins = int(tree.Wins)
        self.name = tree.Name
        self.rank_confidence = float(tree.Rank_Confidence)
        self.rank_stat = float(tree.Rank_Stat)
        self.dict = {
            "created": self.created,
            "last_login": self.last_login,
            "leaves": self.leaves,
            "level": self.level,
            "losses": self.losses,
            "wins": self.wins,
            "name": self.name,
            "rank_confidence": self.rank_confidence,
            "rank_stat": self.rank_stat
        }

    def model_dict(self):
        return self.dict

    def get_created(self):
        return self.data['created_datetime']

    def get_last_login(self):
        return self.data['last_login_datetime']

    def get_leaves(self):
        return self.data['leaves']

    def get_level(self):
        return self.data['level']

    def get_losses(self):
        return self.data['losses']

    def get_wins(self):
        return self.data['wins']

    def get_name(self):
        return self.data['name']

    def get_rank_confidence(self):
        return self.data['rank_confidence']

    def get_rank_stat(self):
        return self.data['rank_stat']
