#!/usr/bin/env python
# encoding: utf-8

# Importer for spell description. This is separate from the spell
# importer because descriptions are only on the spell lists
# This outputs a csv with two columns: slug and description

import sys, os, csv
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

# Iterate over input files
output = csv.writer(sys.stdout)
for filename in sys.argv[1:]:
    list_html = Q(filename=filename, parser='html')
    spells = list_html("#body p b a")

    for s in pqiter(spells):
        target = s.attr('href')
        try:
            target = target.split('#')[1]
        except IndexError:
            target = os.path.basename(target)
            sys.stderr.write("Looking up rename for %s\n" % target)
            target = {
                'deathwatch.html': '_deathwatch',
                'fly.html': '_fly',                
                'fogCloud.html': '_fog-cloud',
            }[target]
        if target.startswith('_'):
            target = target[1:]
        target = target.replace(',', '') # Remove commas (usde in ", mass" ", greater", etc)
        
        desc_elem = s[0].getparent()
        description = desc_elem.tail or ''
        while desc_elem.getnext() is not None:
            desc_elem = desc_elem.getnext()
            description += lxml.etree.tostring(desc_elem)

        description = description.split(':')[1].strip()
        output.writerow([target.encode('utf-8'), description.encode('utf-8')])
