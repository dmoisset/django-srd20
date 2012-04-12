#!/usr/bin/env python
# encoding: utf-8

import sys, os
import json 
import csv
import re
from pyquery import PyQuery as Q
import lxml.etree


CRMAP = {
    '1/2': 0,
    '1/3': -1,
    '1/4': -2,
    '1/6': -3,
    '1/8': -4,
    
}

ALIGNMENTS = set(['LG', 'NG', 'CG', 'LN', 'N', 'CN', 'LE', 'NE', 'CE'])
SIZES = set(['Diminutive', 'Fine', 'Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan', 'Colossal'])
TYPES = set([
    'aberration', 'animal', 'construct', 'dragon', 'fey', 'humanoid',
    'magical beast', 'monstrous humanoid', 'ooze', 'outsider', 'plant',
    'undead', 'vermin'])

def pqiter(pq):
    """
    Iterator on a PyQuery object that produces PyQuery objects, instead
    of plain XML elements
    """
    index = 0
    while index < len(pq):
        yield pq.eq(index)
        index += 1

def normalize_attribute(attr):
    """
    Normalizes the name of an attribute which is seplled ins lightly different
    ways in paizo HTMLs
    """
    if attr.find('a'):
        attr = attr.find('a').html() # Remove links
    else:
        attr = attr.html()
    attr = attr.strip()

    translation_map = {
        'Atk': 'Base Atk',
        'Attacks': 'Special Attacks',
        'Bloodline Spell-Like Ability': 'Spell-Like Abilities',
        'Defensive Ability': 'Defensive Abilities',
        'Language': 'Languages',
        'Racial Modifier': 'Racial Modifiers',
        'Special Attack': 'Special Attacks',
        'Spell-Lilke Abilities': 'Spell-Like Abilities',
        'Special Qualities': 'SQ',
    }

    if attr in translation_map:
        attr = translation_map[attr]
    assert attr in (
        'AC', 'Aura', 'Base', 'Base Atk', 'Cha', 'CMB', 'CMD', 'Con',
        'Defensive Abilities', 'Dex', 'DR', 'Environment', 'Feats', 'Gear',
        'hp', 'Fort', 'Immune', 'Init', 'Int', 'Languages', 'Melee',
        'Opposition Schools', 'Organization', 'Racial Modifiers', 'Ranged',
        'Reach', 'Ref', 'Resist', 'Skills', 'Senses', 'Sorcerer Spells Known',
        'Space', 'Special', 'Special Attacks', 'Speed', 'Spell-Like Abilities',
        'Spells Known', 'Spells Prepared', 'SQ', 'SR', 'Str', 'Treasure',
        'Weaknesses', 'Will', 'Wis'
    )
    return attr.lower()

# Iterate over input files
result = []
abilities = []

xpline = re.compile("XP [0-9,]*")
maxl=0
for filename in sys.argv[1:]:
    monster_html = Q(filename=filename, parser='html')
    monsters = monster_html("#body .monster-header")

    for m in pqiter(monsters):
        slug = m.attr('id')
#        fn = os.path.basename(filename)

        title = m[0].text_content().strip()

        attributes = {}
        description = ''
        p = m.next('p')

        if p.attr('class') != 'flavor-text':
            sys.stderr.write("%s: No flavor-text after <h1>. Skipping\n" % slug)
            continue

        has_type_line = False

        # Get fields
        while p.attr('class'):
            eclass = p.attr('class')
            etext = p[0].text_content()
            if eclass == 'flavor-text':
                flavor_text = etext
            elif eclass == 'stat-block-title':
                _, cr = etext.split('CR')
                cr = cr.strip()
                if cr in CRMAP:
                    cr = CRMAP[cr]
                else:
                    cr = int(cr)
            elif eclass == 'stat-block-xp' or xpline.match(etext.strip()):
                _, xp = etext.split('XP')
                xp = int(xp.replace(',','').strip())
            elif eclass == 'stat-block-breaker':
                # Collect special abilities
                if etext.lower() == "special abilities":
                    p = p.next('p')
                    while p.attr('class') in ('stat-block-1', 'stat-block-2'):
                        abilities.append(lxml.etree.tostring(p[0]))
                        p = p.next('p')                        
            elif eclass == 'stat-block-1':
                
                attrname = p.children('b')
                
                if not has_type_line and len(attrname)==0: # No bold items, line is probably alignment/size/type/subtypes
                    text = p[0].text_content()
                    if '(' in text and ')' in text:
                        # subtypes
                        l, m = text.split('(', 1)
                        m, r = m.split(')', 1)
                        attributes['subtypes'] = m
                        text = (l+r).strip()
                        has_type_line = True
                    
                    if text.split()[-1].isdigit():
                        # Class + level
                        items = text.split()
                        attributes['class_level'] = ' '.join(items[-2:])
                        text = ' '.join(items[:-2])
                        if text.lower().endswith(title.lower()): # Repeated name
                            text = text[:-len(title)].strip()
                        
                    if text.lower().startswith('any alignment'):
                        text = text[len('Any alignment'):].strip()
                        attributes['alignment'] = 'Any'
                        has_type_line = True
                    items = map(str.strip, text.split(None, 2))
                    if items and items[0] in ALIGNMENTS:
                        attributes['alignment'] = items[0]
                        has_type_line = True
                        del items[0]
                    if items and items[0] in SIZES:
                        attributes['size'] = items[0]
                        has_type_line = True
                        del items[0]
                    if items and items[0].lower() in TYPES:
                        attributes['type'] = items[0].lower()
                        has_type_line = True
                        
                        del items[0]
                    if items:
                        attributes['other_type'] = ' '.join(items)
                
                for a in pqiter(attrname):
                    label = normalize_attribute(a)
                    if label=='base': continue # skip the <b>Base</b> <b>Atk</b> everywhere
                    if label=='special': continue # skip the <b>Special</b> <b>Attacks</b> everywhere
                    # Get the rest until the next <b>
                    elem = a[0]
                    value = elem.tail or ''
                    while elem.getnext() is not None and elem.getnext().tag != 'b':
                        elem = elem.getnext()
                        value += lxml.etree.tostring(elem)
                    value = value.strip()
                    if value.endswith(';'):
                        value = value[:-1]
                    attributes[label] = value
                    if label in ('treasure'): maxl = max(maxl, len(value))

            elif eclass == 'stat-block-2':
                # Continues the last item
                attributes[label] += lxml.etree.tostring(p[0])
            else:
                sys.stderr.write("%s: Paragraph with class %s unparsed\n" % (slug, p.attr('class')))
                
            p = p.next('p')

        # The rest is description
        while p:
            description += p.outerHtml()
            p = p.next('p')
            
        # Reference
        reference = '/'.join(filename.split('/')[-3:-1])

        try: flavor_text
        except NameError: sys.stderr.write("%s: No flavor text\n" % slug)

        result.append({
            "model": "srd20.monster",
            "pk": len(result),
            "fields": {
                "name": title,
                "altname": slug,
                "flavor_text": flavor_text,
                "cr": cr,
                "xp": xp,
#                "school": attributes.get("school", ""),
#                "subschool": attributes.get("subschool", ""),
#                "descriptor": attributes.get("descriptor", ""),
#                "level": attributes.get("level", ""),
#                "components": attributes.get("components", ""),
#                "casting_time": attributes.get("casting time", ""),
#                "range": attributes.get("range", ""),
#                "target": attributes.get("target", ""),
#                "area": attributes.get("area", ""),
#                "effect": attributes.get("effect", ""),
#                "duration": attributes.get("duration", ""),
#                "saving_throw": attributes.get("saving throw", ""),
#                "spell_resistance": attributes.get("spell resistance", ""),
#                "reference": reference,
#                
                "description": description,
#                "short_description": descriptions.get(slug, '')
            }
        })
        del cr, xp, slug, title, attributes, description, flavor_text

#print json.dumps(result, ensure_ascii=False, indent=4).encode('utf-8')
print maxl
