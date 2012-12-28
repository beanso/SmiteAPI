#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import md5
from datetime import datetime, timedelta
import urllib2
import xml.etree.ElementTree as ET
import requests
from configobj import ConfigObj
from Database import Database

__author__ = 'Benno'


class SmiteAPI:

    config = ConfigObj('config.ini')
    API_DEVID = config['devid']
    API_AUTHKEY = config['authkey']
    API_URL = config['apiurl']
    SESSION_INFO_FILE = 'session.txt'
    NAMESPACE = '{http://schemas.datacontract.org/2004/07/SmiteApi}'
    SESSION_DURATION = 15
    SESSION_INFO = {'key': None, 'timestamp': None}

    def get_md5_hash(self, value):
        m = md5()
        m.update(value)
        return m.hexdigest()

    def get_timestamp(self):
        return datetime.utcnow().strftime('%Y%m%d%H%M%S')

    def xml_to_datetime(self, value):
        return datetime.strptime(value, '%m/%d/%Y %I:%M:%S %p')

    def generate_signature(self, method):
        combined = self.API_DEVID + method + self.API_AUTHKEY \
            + self.get_timestamp()
        combinedmd5 = self.get_md5_hash(combined)
        return combinedmd5

    def create_session(self):
        url_segments = [self.API_URL, 'createsessionxml', self.API_DEVID,
                        self.generate_signature('createsession'),
                        self.get_timestamp()]
        url = '/'.join(url_segments)
        response = requests.get(url).text.encode('utf-8')
        root = ET.fromstring(response)
        if root.find(self.NAMESPACE + 'ret_msg').text == 'Approved':
            key = root.find(self.NAMESPACE + 'session_id').text
            timestamp = self.xml_to_datetime(root.find(self.NAMESPACE
                    + 'timestamp').text)
            return [timestamp, key]

    def get_session(self):
        db = Database()
        session = db.get_session()
        self.log(session['timestamp'])
        sess_datetime = session['timestamp']
        if session['timestamp'] is None or datetime.utcnow() \
            - sess_datetime > timedelta(minutes=14):
            sessionlist = self.create_session()
            db.update_session(*sessionlist)
            session = db.get_session()
            self.log('needs new ' + session['key'] + ' expires: '
                     + str(session['timestamp'] + timedelta(0, 0, 0, 0,
                     15)))
            return session['key']
        else:
            self.log('old ' + session['key'] + ' expires: '
                     + str(session['timestamp']
                     + timedelta(minutes=15)))
            return session['key']

    def web_request(self, method, args):
        url_segments = [
            self.API_URL,
            method + "json",
            self.API_DEVID,
            self.generate_signature(method),
            self.get_session(),
            self.get_timestamp(),
            ]
        if args is not None:
            url_segments = url_segments + args
        the_url = '/'.join(url_segments)
        self.log(the_url)
        response = None
        try:
            response = requests.get(the_url.encode('utf-8'))
        except urllib2.HTTPError:
            self.log('Error with requesting, trying again...')
            return self.web_request(method, args)
        return response.text.encode('utf-8')

    # Lang -> 1 - english, 2 - french

    def get_items(self, lang='1'):
        return self.web_request('getitems', [lang])

    def get_player(self, name):
        return self.web_request('getplayer', [name])

    def get_match_details(self, mapid):
        return self.web_request('getmatchdetails', [mapid])

    def get_match_history(self, name):
        return self.web_request('getmatchhistory', [name])

    def get_queue_stats(self, name, queue):
        return self.web_request('getqueuestats', [name, queue])

    def get_data_used(self):
        return self.web_request('getdataused', None)

    def get_top_ranked(self):
        return self.web_request('gettopranked', None)

    def ping(self):
        params = [self.API_URL, 'ping']
        url = '/'.join(params)
        time = datetime.now()
        urllib2.urlopen(url).read()
        time2 = datetime.now()
        delta = time2 - time

        return delta

    def data_usage(self):
        resp = self.get_data_used()
        resp_tree = ET.fromstring(resp)
        resp_tree = resp_tree[0]
        usage = {
            'active_sessions': resp_tree.find(self.NAMESPACE
                    + 'Active_Sessions').text,
            'concurrent_sessions': resp_tree.find(self.NAMESPACE
                    + 'Concurrent_Sessions').text,
            'request_limit_daily': resp_tree.find(self.NAMESPACE
                    + 'Request_Limit_Daily').text,
            'session_limit_daily': resp_tree.find(self.NAMESPACE
                    + 'Session_Cap').text,
            'session_time_limit': resp_tree.find(self.NAMESPACE
                    + 'Session_Time_Limit').text,
            'total_requests_today': resp_tree.find(self.NAMESPACE
                    + 'Total_Requests_Today').text,
            'total_sessions_today': resp_tree.find(self.NAMESPACE
                    + 'Total_Sessions_Today').text,
            }
        return usage

    def log(self, text):

        # print text

        return




# for p in models.Player.objects.all():
#    hist = s.get_match_history(p.name)
#    games = etree.XML(hist).findall(".//{*}playerMatchHistory")
#
#    for one in games:
#        matchsum = MatchSummary(etree.tostring(one))
#        models.MatchSummary.objects.create(player_id=p.id, **matchsum.model_dict())
#

# root = etree.XML(d)
# names = root.findall(".//{*}name")
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# from Smitedb import models
# import time
# players = models.Player.objects.all()
# for player in players:
#    d = s.get_player(player.name)
#    try:
#        p = Player(d)
#    except:
#        continue
#    updated_player = models.Player(id=player.id, **p.dict)
#    updated_player.save()
#    time.sleep(1)

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# from Smitedb import models
#
# for item in i.items:
#    models.Item.objects.create(name=item.name, description=item.description, secondary_description=item.second_description, item_id=item.item_id)
#

# root = etree.fromstring(d)
# descriptionroot = root.findall(s.NAMESPACE + "ItemDescriptionRoot")
# names = []
# for i in descriptionroot:
#    thename = i.find(s.NAMESPACE + "DeviceName")
#    names.append(thename)
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# from Smitedb import models
#
#
# for name in names:
#    models.Item.objects.create(name=name.text)
