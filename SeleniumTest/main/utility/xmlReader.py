import xml.etree.ElementTree as ET
from pathlib import Path


class XmlReader():
    def __init__(self):
        self.path = str(Path(__file__).parent.parent.parent) + "/testresources/Testxml.xml"

    def get_value(self, VariableName):
        tree = ET.parse(self.path)
        root = tree.getroot()

        for variable in root.findall('Variable'):
            if variable.find('Name').text == VariableName:
                # print(variable.find('Value').text)
                return variable.find('Value').text

# X1= XmlReader()
# X1.getValue('Password')
