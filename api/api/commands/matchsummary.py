__author__ = 'Benno'
from lxml import etree, objectify
from dateutil.parser import parse
from django.utils.timezone import utc
from Smite.api.commands.command import Command

class MatchSummary(Command):
    data = None

    def __init__(self, xml):
        xml = self.clean_xml(xml)
        root = objectify.fromstring(xml)
        self.data = {}
        for child in root.iter():
            self.data[child.tag.lower()] = child.text


    def model_dict(self):
        return self.data

    def get_gold(self):
        return self.data["gold"]

    def get_deaths(self):
        return self.data["deaths"]

    def get_item_5(self):
        return self.data["item_5"]

    def get_queue(self):
        return self.data["queue"]

    def get_god(self):
        return self.data["god"]

    def get_damage(self):
        return self.data["damage"]

    def get_damage_taken(self):
        return self.data["damage_taken"]

    def get_active_3(self):
        return self.data["active_3"]

    def get_active_2(self):
        return self.data["active_2"]

    def get_active_1(self):
        return self.data["active_1"]

    def get_ret_msg(self):
        return self.data["ret_msg"]

    def get_match(self):
        return self.data["match"]

    def get_kills(self):
        return self.data["kills"]

    def get_playername(self):
        return self.data["playername"]

    def get_match_time(self):
        return self.data["match_time"]

    def get_win_status(self):
        return self.data["win_status"]

    def get_creeps(self):
        return self.data["creeps"]

    def get_level(self):
        return self.data["level"]

    def get_item_6(self):
        return self.data["item_6"]

    def get_item_4(self):
        return self.data["item_4"]

    def get_assists(self):
        return self.data["assists"]

    def get_item_2(self):
        return self.data["item_2"]

    def get_item_3(self):
        return self.data["item_3"]

    def get_item_1(self):
        return self.data["item_1"]

    def get_minutes(self):
        return self.data["minutes"]
