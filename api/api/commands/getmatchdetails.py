__author__ = 'Benno'
from dateutil import parser
import pprint
import xml.etree.ElementTree as ET
from Smite.api.commands.command import Command
from lxml import etree, objectify

class GetMatchDetails(Command):

    data = {}

    def __init__(self, xml):
        xml = self.clean_xml(xml)

        root = objectify.fromstring(xml)
        self.data = {}
        for child in root.iter():
            self.data[child.tag.lower()] = child.text

    def get_players(self):
        players = []
        for name in self.data:
            players.append(name)
        return players

    def model_dict(self):
        return self.data

    def get_deaths(self):
        return self.data["deaths"]

    def get_final_match_level(self):
        return self.data["final_match_level"]

    def get_damage_done_physical(self):
        return self.data["damage_done_physical"]

    def get_gold_per_minute(self):
        return self.data["gold_per_minute"]

    def get_gold_earned(self):
        return self.data["gold_earned"]

    def get_item_purch_5(self):
        return self.data["item_purch_5"]

    def get_item_purch_4(self):
        return self.data["item_purch_4"]

    def get_item_purch_6(self):
        return self.data["item_purch_6"]

    def get_item_purch_1(self):
        return self.data["item_purch_1"]

    def get_item_purch_3(self):
        return self.data["item_purch_3"]

    def get_item_purch_2(self):
        return self.data["item_purch_2"]

    def get_match(self):
        return self.data["match"]

    def get_playername(self):
        return self.data["playername"]

    def get_reference_name(self):
        return self.data["reference_name"]

    def get_damage_player(self):
        return self.data["damage_player"]

    def get_kills_bot(self):
        return self.data["kills_bot"]

    def get_damage_taken(self):
        return self.data["damage_taken"]

    def get_assists(self):
        return self.data["assists"]

    def get_entry_datetime(self):
        return self.data["entry_datetime"]

    def get_win_status(self):
        return self.data["win_status"]

    def get_name(self):
        return self.data["name"]

    def get_damage_done_magical(self):
        return self.data["damage_done_magical"]

    def get_minutes(self):
        return self.data["minutes"]

    def get_damage_bot(self):
        return self.data["damage_bot"]

    def get_item_active_2(self):
        return self.data["item_active_2"]

    def get_item_active_3(self):
        return self.data["item_active_3"]

    def get_item_active_1(self):
        return self.data["item_active_1"]

    def get_kills_player(self):
        return self.data["kills_player"]
    
