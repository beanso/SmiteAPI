__author__ = 'Benno'
import command

class GetTopRanked(command.Command):

    def __init__(self, xml_string):
        xml_string = self.clean_xml(xml_string)
