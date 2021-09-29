"""a wikidot spell scraper"""

import requests
import time
import json
import os
from bs4 import BeautifulSoup

WIKIDOT = "http://dnd5e.wikidot.com"
SPELLS  = WIKIDOT + "/spells"
SPELL_FILE = os.path.join(os.path.dirname(__file__), "../../data/spells.json")

def get_spell_links(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = [l.find('a')['href'] for l in soup.find_all('tr') if l.find('a') is not None]
    links = [WIKIDOT + href for href in rows]
    return links

def get_spell_data(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')

    spell = {}
    spell['title'] = soup.find(class_='page-title').text
    data = [d.text for d in soup.find(id="page-content").find_all(['p', 'li'])]
    # for dd in data:
    #     print(dd)

    spell['source']      = data[0][8:]
    if not data[0].startswith("Source: "):
        spell['source'] = ""
        data.insert(0, "")
    spell['type']        = data[1]
    l = data[1].split()
    if 'level' in l[0]:
        spell['level']       = l[0]
        spell['school']      = l[1]
    else:
        spell['level']       = l[1]
        spell['school']      = l[0]
    info        = data[2].split("\n")
    spell['cast_time']   = info[0][14:]
    spell['range']        = info[1][7:]
    spell['components']  = info[2][12:]
    spell['duration']    = info[3][10:]
    spell['spell_lists'] = data.pop()[13:].split(", ")
    spell['description'] = data[3:]
    spell['link']        = link
    return spell

def update_spell_db(new_spell_list):
    with open(SPELL_FILE, "w+") as spell_file:
        spell_file.write(json.dumps(new_spell_list))

def reload_spell_db():
    tmp_spells = []
    counter = 1
    for link in get_spell_links(SPELLS):
        print(f"\rloading from {link}...                             ", end="")
        try:
            sp = get_spell_data(link)
            sp["id"] = counter
        except Exception as e:
            print(f"\n{link} failed to download!")
            print(e)
        else:
            tmp_spells.append(sp)
        counter += 1
        time.sleep(0.05)

    print("loaded all spells!                                        ")
    with open(SPELL_FILE, "w+") as spell_file:
        spell_file.write(json.dumps(tmp_spells))

def load_spell_db():
    if not os.path.exists(SPELL_FILE):
        return []
    with open(SPELL_FILE) as spell_file:
        return json.loads(spell_file.read())

def find_spells(attr, value):
    return [x for x in spell_list if x[attr] == value]

def find_spell(attr, value):
    try:
        return next(x for x in spell_list if x[attr] == value)
    except StopIteration:
        return None

spell_list = load_spell_db()