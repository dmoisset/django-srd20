#!/usr/bin/env python
# encoding: utf-8

import sys, os
import json 
from pyquery import PyQuery as Q

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
        
        title = s[0].text_content().strip()
        print slug,
        attributes = {}
        description = ''
        p = s.next('*')
        while p.hasClass('stat-block-1'):
            attrname = p.children('b')
            for a in pqiter(attrname):
                label = normalize_attribute(a)
#            if attrname:
#                label = normalize_attribute(attrname.html())
#                attrname.remove()  
#            html = p.outerHtml()
#            if label in ('description', 'prerequisite'):
#                if p[0].tag in ('p',):
#                    html = p.html()
#                else:
#                    sys.stderr.write(u"Skipping tag <%s> in %s['%s']\n" % (p[0].tag, title, label))
#                    html = u''
#            attributes[label] = attributes.get(label, u'') + html
            p = p.next('*')
#        result.append({
#            "model": "srd20.feat",
#            "pk": len(result),
#            "fields": {
#                "name": title,
#                "altname": slug,
#                "type": ', '.join(descriptors),
#                "multiple": False, # info not parseable
#                "stack": False, # info not parseable
#                "choice": "", # info not parseable
#                "prerequisite": attributes.get('prerequisite', ''),
#                "benefit": attributes.get('benefit', ''),
#                "normal": attributes.get('normal', ''),
#                "special": attributes.get('special', ''),
#                "reference": filename,
#                "description": attributes.get('description', ''),
#            }
#        })
        if fn == 'transmutePotionToPoison.html':
            # This file has stat-block-title blocks which aren't spells
            break

#print json.dumps(result, ensure_ascii=False, indent=4).encode('utf-8')
    
