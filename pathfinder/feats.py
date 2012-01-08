#!/usr/bin/env python
# encoding: utf-8

import sys
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
    attr = attr.strip()
    if attr.endswith(':'):
        attr = attr[:-1] # Remove trailing ':' if any
    if attr == 'Prerequisites':
        attr = 'Prerequisite' # Normalize
    if attr == 'Note':
        attr = 'Prerequisite' # Normalize a very special case (Versatile Channeler)
    if attr == 'Benefits':
        attr = 'Benefit' # Normalize
    if attr == 'Leadership Modifiers':
        attr = 'Benefit' # Normalize a very special case (Leadership)
    assert attr in ('Prerequisite', 'Benefit', 'Normal', 'Special')
    return attr.lower()

# Iterate over input files
result = []
for filename in sys.argv[1:]:
    feats_html = Q(filename=filename, parser='html')
    feats = feats_html("#feats-text h2")

    for f in pqiter(feats):
        slug = f.attr('id')
        if '-(' in slug:
            # Some id's include descriptors. remove them
            slug = slug.split('-(')[0]
        title = f[0].text_content() # Use this instead of html() to remove embedded links
        descriptors = []
        attributes = {}
        if '(' in title:
            title, descriptors = title.split('(')
            assert descriptors.endswith(')')
            descriptors = descriptors[:-1] # Remove ending ')'
            descriptors = [d.strip() for d in descriptors.split(',')]
        label = 'description'
        p = f.next('*')
        while p and p[0].tag != 'h2':
            attrname = p.children('b')
            if attrname:
                label = normalize_attribute(attrname.html())
                attrname.remove()  
            html = p.outerHtml()
            attributes[label] = attributes.get(label, u'') + html
            p = p.next('*')
        result.append({
            "model": "srd20.feat",
            "pk": len(result),
            "fields": {
                "name": title,
                "altname": slug,
                "type": ', '.join(descriptors),
                "multiple": False, # info not parseable
                "stack": False, # info not parseable
                "choice": "", # info not parseable
                "prerequisite": attributes.get('prerequisite', ''),
                "benefit": attributes.get('benefit', ''),
                "normal": attributes.get('normal', ''),
                "special": attributes.get('special', ''),
                "reference": filename,
                "description": attributes.get('description', ''),
            }
        })

print json.dumps(result, ensure_ascii=False, indent=4).encode('utf-8')
    
