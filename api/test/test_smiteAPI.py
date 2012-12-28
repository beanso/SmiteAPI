import unittest
from Smite.api.API import SmiteAPI

__author__ = 'Benno'


class TestSmiteAPI(unittest.TestCase):
    s = None

    def setUp(self):
        self.s = SmiteAPI()
        return

    def test_get_items(self):
        self.fail()

    def test_get_player(self):
        xml =\
        """
        <playerMatchHistory>
            <Active_1/>
            <Active_2/>
            <Active_3/>
            <Assists>0</Assists>
            <Creeps>318</Creeps>
            <Damage>16189</Damage>
            <Damage_Taken>25343</Damage_Taken>
            <Deaths>6</Deaths>
            <God>He_Bo</God>
            <Gold>15524</Gold>
            <Item_1>Spear of the Magus</Item_1>
            <Item_2>Boots of the Magi</Item_2>
            <Item_3>Gem of Isolation</Item_3>
            <Item_4>Rod of Tahuti</Item_4>
            <Item_5>Void Stone</Item_5>
            <Item_6>Obsidian Shard</Item_6>
            <Kills>4</Kills>
            <Level>20</Level>
            <Match>6396885</Match>
            <Match_Time>12/9/2012 4:43:43 PM</Match_Time>
            <Minutes>37</Minutes>
            <Queue>Joust</Queue>
            <Win_Status>Loss</Win_Status>
            <playerName>RGLassiz</playerName>
            <ret_msg i:nil="true"/>
        </playerMatchHistory>
        """
        from Smite.api.commands.matchsummary import MatchSummary

        p = MatchSummary(xml)
        for key in p.model_dict().keys():
            print key
        self.assertEquals(p.get_playername(), "RGLassiz")

    def test_get_match_details(self):
        from Smite.api.commands.getmatchdetails import GetMatchDetails

        xml = """
            <root>
            <Assists>14</Assists>
            <Damage_Bot>27257</Damage_Bot> = damage to minions/npcs
            <Damage_Done_Magical>1527</Damage_Done_Magical>
            <Damage_Done_Physical>64489</Damage_Done_Physical>
            <Damage_Player>38759</Damage_Player>
            <Damage_Taken>29345</Damage_Taken>
            <Deaths>8</Deaths>
            <Entry_Datetime>11/28/2012 1:44:21 AM</Entry_Datetime>
            <Final_Match_Level>20</Final_Match_Level>
            <Gold_Earned>17575</Gold_Earned>
            <Gold_Per_Minute>925</Gold_Per_Minute>
            <Item_Active_1>Sprint</Item_Active_1>
            <Item_Active_2>Aegis Amulet</Item_Active_2>
            <Item_Active_3/>
            <Item_Purch_1>Warrior Tabi</Item_Purch_1>
            <Item_Purch_2>The Executioner</Item_Purch_2>
            <Item_Purch_3>Deathbringer</Item_Purch_3>
            <Item_Purch_4>Qin's Blades</Item_Purch_4>
            <Item_Purch_5>Voidblade</Item_Purch_5>
            <Item_Purch_6>Titan's Bane</Item_Purch_6>
            <Kills_Bot>51</Kills_Bot> = minion kills
            <Kills_Player>18</Kills_Player>
            <Match>6090445</Match> = mapid
            <Minutes>19</Minutes>
            <Reference_Name>Loki</Reference_Name> = god name
            <Win_Status>Winner</Win_Status>
            <name>Arena</name>
            <playerName>smellsgood</playerName>
            <ret_msg i:nil="true"/>
            </root>
        """

        md = GetMatchDetails(xml)
        self.assertEqual(md.get_match(), "6090445")

    def test_get_match_history(self):
        self.fail()

    def test_get_queue_stats(self):
        self.fail()

    def test_get_data_used(self):
        self.fail()

    def test_get_top_ranked(self):
        self.fail()

    def test_ping(self):
        self.fail()

    def test_data_usage(self):
        self.fail()

    def test_log(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()

