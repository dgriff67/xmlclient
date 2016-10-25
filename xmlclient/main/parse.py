import xml.etree.ElementTree as ET
import os
import requests
from .models import Pl1516


baseUrl = 'http://dgriff67.pythonanywhere.com/api/Pl1516/?format=xml&hometeam='
data_dict = dict()

def parse_load(hometeam):
    url = baseUrl+hometeam
    resp = requests.get(url)
    msg = resp.content
    tree = ET.fromstring(msg)
    for objects in tree.findall('objects'):
        for object in objects:
            for child in object:
                data_dict.update({child.tag : child.text})
            m = Pl1516(**data_dict)
            m.save()

