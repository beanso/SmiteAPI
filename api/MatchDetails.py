__author__ = 'Benno'
from dateutil import parser
import pprint
import xml.etree.ElementTree as ET

class MatchDetails:

    data = {}

    def __init__(self, xml):
        root = ET.fromstring(xml)
        ns = "{http://schemas.datacontract.org/2004/07/SmiteApi}"
        for match_details in root.findall(ns+"playerMatchDetails"):
            single_data = {}
            for elem in list(match_details):
                single_data[elem.tag.replace(ns, "")] = elem.text

            self.data[single_data["playerName"]] = single_data
        print self.data["Beanso"]

    def get_players(self):
        players = []
        for name in self.data:
            players.append(name)
        return players

    def get_player_details(self, name):
        return
