__author__ = 'Benno'
from lxml import etree, objectify
from dateutil.parser import parse
from django.utils.timezone import utc

class MatchSummary:
    data = None

    Active_1 = None
    Active_2 = None
    Active_3 = None
    Assists = None
    Creeps = None
    Damage = None
    Damage_Taken = None
    Deaths = None
    God = None
    Gold = None
    Item_1 = None
    Item_2 = None
    Item_3 = None
    Item_4 = None
    Item_5 = None
    Item_6 = None
    Kills = None
    Level = None
    Match = None
    Match_Time = None
    Minutes = None
    Queue = None
    Win_Status = None
    playerName = None

    def __init__(self, xml):
        root = objectify.fromstring(xml)
        self.data = {}
        for child in root.iter():
            self.data[child.tag.lower()] = child.text

        print self.data

        # self.Active_1 = root.find(".//{*}Active_1").text
        # self.Active_2 = root.find(".//{*}Active_2").text
        # self.Active_3 = root.find(".//{*}Active_3").text
        # self.Item_1 = root.find(".//{*}Item_1").text
        # self.Item_2 = root.find(".//{*}Item_2").text
        # self.Item_3 = root.find(".//{*}Item_3").text
        # self.Item_4 = root.find(".//{*}Item_4").text
        # self.Item_5 = root.find(".//{*}Item_5").text
        # self.Item_6 = root.find(".//{*}Item_6").text
        # self.Kills = int(root.find(".//{*}Kills").text)
        # self.Deaths = int(root.find(".//{*}Deaths").text)
        # self.Assists = int(root.find(".//{*}Assists").text)
        # self.Creeps = int(root.find(".//{*}Creeps").text)
        # self.Damage = int(root.find(".//{*}Damage").text)
        # self.Damage_Taken = int(root.find(".//{*}Damage_Taken").text)
        # self.Gold = int(root.find(".//{*}Gold").text)
        # self.Level = int(root.find(".//{*}Level").text)
        # self.Minutes = int(root.find(".//{*}Minutes").text)
        # self.Match_Time = parse(root.find(".//{*}Match_Time").text).replace(tzinfo=utc)
        # self.God = root.find(".//{*}God").text
        # self.Queue = root.find(".//{*}Queue").text
        # self.Win_Status = root.find(".//{*}Win_Status").text
        # self.Match = root.find(".//{*}Match").text

    def model_dict(self):
        dict = {}
        dict["active_1"] = self.Active_1
        dict["active_2"] = self.Active_2
        dict["active_3"] = self.Active_3
        dict["item_1"] = self.Item_1
        dict["item_2"] = self.Item_2
        dict["item_3"] = self.Item_3
        dict["item_4"] = self.Item_4
        dict["item_5"] = self.Item_5
        dict["item_6"] = self.Item_6
        dict["kills"] = self.Kills
        dict["deaths"] = self.Deaths
        dict["assists"] = self.Assists
        dict["gold"] = self.Gold
        dict["level"] = self.Level
        dict["match"] = self.Match
        dict["match_time"] = self.Match_Time
        dict["minutes"] = self.Minutes
        dict["queue"] = self.Queue
        dict["win_status"] = self.Win_Status
        dict["god"] = self.God

        return self.data
