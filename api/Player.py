__author__ = 'Benno'

from dateutil import parser
from lxml import etree, objectify
from django.utils.timezone import utc
import re

class Player:
    created = None
    last_login = None
    leaves = None #int
    level = None #int
    losses = None #int
    wins = None #int
    name = None
    rank_confidence = None #int
    rank_stat = None #float

    dict = {}

    def __init__(self, xml_string):
        xml_string = re.sub('xmlns=".+" (?=xmlns)', "", xml_string) # Replace namespace
        tree = objectify.fromstring(xml_string)
        tree = tree.player
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