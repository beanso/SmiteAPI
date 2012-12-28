__author__ = 'Benno'

from API import SmiteAPI
from dateutil import parser
from lxml import etree, objectify
from django.utils.timezone import utc

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from Smitedb import models
from Player import Player
from MatchSummary import MatchSummary
import time
import urllib2

class Global():
    pass

g = Global()
g.s = SmiteAPI()
g.sleep = .5

def get_top_200():
    xml_string = g.s.get_top_ranked()
    xml_string = xml_string.replace('xmlns="http://schemas.datacontract.org/2004/07/SmiteApi"', "")
    #print xml_string
    tree = objectify.fromstring(xml_string)
    for player in tree.iterchildren():
        name = player.name.text.encode("utf-8")
        created = parser.parse(player.Created_datetime.text).replace(tzinfo=utc)
        if (not models.Player.objects.filter(name=name).exists()
            and models.Player.objects.filter(created=created).exists()): # Name changed.
                old = models.Player.objects.get(created=created)
                print "Changed {0}'s name to {1}".format(old.name, name)
                old.name = name
                old.save()
        else: # Add new player
            player, created = models.Player.objects.get_or_create(name=name)
            if created:
                print "Added new player: {0}".format(name)


def update_players():
    for player in models.Player.objects.all():
        d = g.s.get_player(player.name)
        try:
            p = Player(d)
        except:
            player.delete()
            print "Deleted %s from top 200 (wtb ID)" % player.name
            continue
        updated_player = models.Player(id=player.id, **p.dict)
        updated_player.save()
        print "Updated %s" % updated_player.name
        time.sleep(g.sleep)
    return

def update_match_histories():
    total = 0
    for player in models.Player.objects.all():
        hist = g.s.get_match_history(player.name)
        hist_xml = etree.XML(hist)
        num = 0

        for match in hist_xml.findall(".//{*}playerMatchHistory"):
            match_sum = MatchSummary(etree.tostring(match))
            m, created = models.MatchSummary.objects.get_or_create(player_id=player.id, **match_sum.model_dict())
            if created:
                num += 1
                total += 1

        print "Added {0} new matches for {1}".format(str(num), player.name)
        time.sleep(g.sleep)

    print "Added {0} new matches".format(str(total))
    return

#get_top_200()
#update_players()
#update_match_histories()
import simplejson
obj = simplejson.loads(g.s.get_items())
print g.s.get_items()