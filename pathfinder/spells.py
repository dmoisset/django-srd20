#!/usr/bin/env python
# encoding: utf-8

import sys, os
import json 
from pyquery import PyQuery as Q
import lxml.etree

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
        'Targets': 'Target',
        'Component': 'Components',
        'Target or Area': 'Target',
        'Target or Targets': 'Target',
        'Save': 'Saving Throw',
        'Saving': 'Saving Throw',
        'Saving throw': 'Saving Throw',
        'Casting': 'Casting Time',
        'Casting time': 'Casting Time',
        'SR':  'Spell Resistance',
        'Target, Effect, or Area': 'Area',
        'Target, Effect, Area': 'Effect',
        'Target/Effect': 'Effect',
        'Area or Target': 'Area',
    }
    if attr in translation_map:
        attr = translation_map[attr]
    assert attr in ('School', 'Level', 'Components', 'Casting Time', 'Range',
         'Effect', 'Duration', 'Saving Throw', 'Spell Resistance',
         'Target', 'Area', 'Preparation Time'
     )
    return attr.lower()

# Iterate over input files
result = []
for filename in sys.argv[1:]:
    spell_html = Q(filename=filename, parser='html')
    spells = spell_html("#body .stat-block-title")

    for s in pqiter(spells):
        slug = s.attr('id')
        fn = os.path.basename(filename)

        if fn == 'icyPrison.html':
            # This file has wrong formatting. skip
            sys.stderr.write(u"Skipping file %s, known bad formatting\n" % fn)
            break

        if slug is None:
            if fn in ('fogCloud.html', 'symbolOfStrife.html'):
                # the id is missing. autocomplete
                basename = os.path.splitext(fn)[0]
                for c in 'COS': # letters to un-camelCase
                    basename = basename.replace(c, '-'+c.lower())
                slug = basename
                sys.stderr.write(u"Substituting %s for %s\n" % (fn, slug))
            else:
                sys.stderr.write(u"Skipping file %s, no id\n" % fn)
                continue
        
        slug = slug.replace(',', '') # Remove commas in slug
        
        title = s[0].text_content().strip()
        attributes = {}
        description = ''
        p = s.next('*')

        # Get fields
        while p.hasClass('stat-block-1'):
            attrname = p.children('b')
            for a in pqiter(attrname):
                label = normalize_attribute(a)
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
            p = p.next('*')

        # The rest is description
        while p and not p.hasClass('stat-block-title'):
            description += p.outerHtml()
            p = p.next('*')
            
        # From the school line get subschool and descriptors
        if 'school' in attributes:
            school = attributes['school']
            if '[' in school:
                position = school.index('[')
                descriptors = school[position+1:-1]
                school = school[:position-1].strip()
                attributes["school"] = school
                attributes["descriptor"] = descriptors
            if '(' in school:
                position = school.index('(')
                subschool = school[position+1:-1]
                school = school[:position-1].strip()
                attributes["school"] = school
                attributes["subschool"] = subschool

        # Reference
        reference = '/'.join(filename.split('/')[-3:-1])

        result.append({
            "model": "srd20.spell",
            "pk": len(result),
            "fields": {
                "name": title,
                "altname": slug,
                "school": attributes.get("school", ""),
                "subschool": attributes.get("subschool", ""),
                "descriptor": attributes.get("descriptor", ""),
                "level": attributes.get("level", ""),
                "components": attributes.get("components", ""),
                "casting_time": attributes.get("casting time", ""),
                "range": attributes.get("range", ""),
                "target": attributes.get("target", ""),
                "area": attributes.get("area", ""),
                "effect": attributes.get("effect", ""),
                "duration": attributes.get("duration", ""),
                "saving_throw": attributes.get("saving throw", ""),
                "spell_resistance": attributes.get("spell resistance", ""),
                "reference": reference,
                
                "description": description,
            }
        })
        if fn == 'transmutePotionToPoison.html':
            # This file has stat-block-title blocks which aren't spells
            break

print json.dumps(result, ensure_ascii=False, indent=4).encode('utf-8')
    
