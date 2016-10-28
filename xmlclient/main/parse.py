import xml.etree.ElementTree as ET
import os
import requests
from .models import Pl1516


baseUrl = 'http://dgriff67.pythonanywhere.com/api/Pl1516/?format=xml'
data_dict = dict()

def parse_load(venue, team):
    url = baseUrl+'&'+venue+'team='+team
    resp = requests.get(url)
    msg = resp.content
    tree = ET.fromstring(msg)
    for objects in tree.findall('objects'):
        for object in objects:
            for child in object:
                data_dict.update({child.tag : child.text})
            m = Pl1516(**data_dict)
            m.save()

def parse_load_all():
    teams = ['Arsenal','Aston Villa', 'Bournemouth', 'Chelsea', 'Crystal Palace', 'Everton', 'Leicester',
             'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Norwich', 'Southampton', 'Stoke', 'Sunderland',
             'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham']
    for team in teams:
        url = baseUrl+'&hometeam='+team
        resp = requests.get(url)
        msg = resp.content
        tree = ET.fromstring(msg)
        for objects in tree.findall('objects'):
            for object in objects:
                for child in object:
                    data_dict.update({child.tag : child.text})
                m = Pl1516(**data_dict)
                m.save()

