#!/usr/bin/env python
# encoding: utf-8

import sys, os
import json 
import csv
import re
from decimal import Decimal

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
SIZES = ['Fine', 'Diminutive', 'Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan', 'Colossal']
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
        'Arcane School Spell-Like Abilities': 'Spell-Like Abilities',
        'Atk': 'Base Atk',
        'Attacks': 'Special Attacks',
        'Bloodline Spell-Like Ability': 'Spell-Like Abilities',
        'Cleric Spells Prepared': 'Spells Prepared',
        'Conjurer Spells Prepared': 'Spells Prepared',
        'Defensive Ability': 'Defensive Abilities',
        'Domain Spell-Like Abilities': 'Spell-Like Abilities', 
        'Ifrit Spell-Like Abilities': 'Spell-Like Abilities',
        'Language': 'Languages',
        'Racial Modifier': 'Racial Modifiers',
        'Ranger Spells Prepared': 'Spells Prepared',
        'Sorcerer Spell-Like Abilities': 'Spells Prepared',
        'Special Attack': 'Special Attacks',
        'Spell-like Abilities': 'Spell-Like Abilities',
        'Spell-Like Ability': 'Spell-Like Abilities',
        'Spell-Lilke Abilities': 'Spell-Like Abilities',
        'Special Qualities': 'SQ',
        'Weakness': 'Weaknesses',
        'Witch Spells Prepared': 'Spells Prepared',
    }

    if attr in translation_map:
        attr = translation_map[attr]
    assert attr in (
        'AC', 'Aura', 'Base', 'Base Atk', 'Bloodline', 'Cha', 'CMB', 'CMD', 'Con',
        'Defensive Abilities', 'D', 'Dex', 'DR', 'Domains', 'Environment', 'Feats', 'Gear',
        'hp', 'Fort', 'Immune', 'Init', 'Int', 'Languages', 'Melee',
        'Opposition Schools', 'Organization', 'Racial Modifiers', 'Ranged',
        'Reach', 'Ref', 'Resist', 'Skills', 'Senses', 'Sorcerer Spells Known',
        'Space', 'Special', 'Special Attacks', 'Speed', 'Spell-Like Abilities',
        'Spells Known', 'Spells Prepared', 'SQ', 'SR', 'Str', 'Treasure',
        'Weaknesses', 'Will', 'Wis'
    ), "Unkown attribute '%s'" % attr
    return attr.lower()

# Iterate over input files
result = []
abilities = []

xpline = re.compile("XP [0-9,]*")
for filename in sys.argv[1:]:
    monster_html = Q(filename=filename, parser='html')
    monsters = monster_html("#body .monster-header")

    # sys.stderr.write(" *** %s \n" % filename)

    for m in pqiter(monsters):
        slug = m.attr('id').replace(',','')
#        fn = os.path.basename(filename)

        title = m[0].text_content().strip()

        attributes = {}
        description = ''
        p = m.next('p')

        if p.attr('class') != 'flavor-text':
            sys.stderr.write("%s: No flavor-text after <h1>. " % slug)
            
            if p.next('p').hasClass('stat-block-title'):
                sys.stderr.write("Assuming following <p> as flavor-text.\n")
                flavor_text = p[0].text_content()
                p = p.next()
            else:
                sys.stderr.write("Skipping\n")
                continue

        has_type_line = False

        # sys.stderr.write(" *** %s \n" % slug)

        # Get fields
        while p.attr('class'):
            eclass = p.attr('class')
            # remove irrelevant classes
            class_list = eclass.split()
            if 'para-style-override' in class_list: class_list.remove('para-style-override')
            eclass = ' '.join(class_list)
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
                xp = int(xp.replace(',','').replace('each','').strip())
            elif eclass == 'stat-block-breaker':
                # Collect special abilities
                if etext.lower().startswith("special abilities"):
                    p = p.next('p')
                    while p.hasClass('stat-block-1') or p.hasClass('stat-block-2') or p.hasClass('stat-block-indent'):
                        abilities.append(lxml.etree.tostring(p[0]))
                        p = p.next('p')
                    # Leave p right at the last paragraph processed
                    p = p.prev('p')
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
                    if value.endswith(';') or value.endswith(','):
                        value = value[:-1]
                    attributes[label] = value

            elif eclass in ('stat-block-2', 'stat-block-indent'):
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
                "alignment": attributes['alignment'],
                "size": SIZES.index(attributes['size']) - 4,
                "type": attributes['type'],
                "subtypes": attributes.get("subtypes", ""),
                "other_type": attributes.get("other_type", ""),
                "class_level": attributes.get("class_level", ""),
                "initiative": int(attributes["init"].replace(u"–", "")),
                "senses": attributes["senses"],
                "aura": attributes.get("aura", ""),
                
                "armor_class": attributes['ac'],
                "hit_points": attributes['hp'],
                "fortitude_save": attributes['fort'],
                "reflex_save": attributes['ref'],
                "will_save": attributes['will'],
                "defensive_abilities": attributes.get('defensive abilities', ""),
                "damage_reduction_amount": int(attributes.get('dr', "0/").split('/')[0]),
                "damage_reduction_condition": attributes.get('dr', "0/").split('/',1)[1],
                "immunities": attributes.get('immune', ""),
                "resistance": attributes.get('resist', ""),
                "spell_resistance": int(attributes.get('sr', "0")),
                "weaknesses": attributes.get('weaknesses', ""),
                
                "speed": attributes.get('speed', ""),
                "melee": attributes.get('melee', ""),
                "ranged": attributes.get('ranged', ""),
                "space": attributes.get('space', u"5").replace(' ft.', '').replace(" ft", "").replace(' feet', '').replace("-1/2", ".5").replace(u"–1/2", ".5"),
                "reach": attributes.get('reach', ""),
                "special_attacks": attributes.get('special attacks', ""),
                "spell_like_abilities": attributes.get('spell-like abilities', ""),
                "spells_known": attributes.get('spells known', ""),
                "sorcerer_spells_known": attributes.get('sorcerer spells known', ""),
                "spells_prepared": attributes.get('spells prepared', ""),
                "opposition_schools": attributes.get('opposition schools', ""),
                # TODO: domains/bloodline!

                "strength": int(attributes['str'].replace(u"—", "0")),
                "dexterity": int(attributes['dex']),
                "constitution": int(attributes['con'].replace(u"—", "0")),
                "intelligence": int(attributes['int'].replace(u"—", "0")),
                "wisdom": int(attributes['wis']),
                "charisma": int(attributes['cha']),
                "base_attack_bonus": int(attributes['base atk']),
                "combat_maneuver_bonus": attributes['cmb'],
                "combat_maneuver_defense": attributes['cmd'],
                "feats": attributes.get('feats', ''),
                "skills": attributes.get('skills', ''),
                "racial_modifiers": attributes.get('racial modifiers', ''),
                "languages": attributes.get('languages', ''),
                "special_qualities": attributes.get('sq', ''),
                "gear": attributes.get('gear', ''),
                "environment": attributes['environment'],
                "organization": attributes['organization'],
                "treasure": attributes.get('treasure', ''),
                "abilities": attributes.get('abilities', ''),
                "description": attributes.get('description', ''),

                "reference": reference,
                
                "description": description,
            }
        })
        del cr, xp, slug, title, attributes, description, flavor_text

print json.dumps(result, ensure_ascii=False, indent=4).encode('utf-8')
