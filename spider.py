#!/usr/bin/env python

import sys
import sqlite3
from mechanize import ParseResponse, urlopen, urljoin, _form
from lxml import html

sites = ('iproperty', 
         'fullhouse'
        )

def parse():
    for site in sites:
        modname = 'models.%s' % site
        __import__(modname)
        mod = sys.modules[modname]

        print 'parsing %s' % site
        url = 'http://%s' % mod.url
        
        ## some sites dont require forms. just pass parameters in url
        if not mod.isform:
            url += '?%s' % '&'.join(['%s=%s' % (k,v) for (k,v) in mod.searchparams.iteritems()])
            print url
            response = urlopen(url)
        else:
            forms = ParseResponse(response, backwards_compat=False)
            theform = [form for form in forms if form.name == mod.formname and form.action == mod.formaction][0]
        
            for ctrl in mod.formvalues:
                el = theform.find_control(ctrl)
                if el.type == 'select':
                    try:
                        theform.set_value(['%s' % mod.formvalues[ctrl]], name=ctrl)
                    except:
                        print 'potentially no item in element %s : %s' % (el.name, el.items) 
                        pass

            response = urlopen(form.click())       

        ## get only search results in html
        soup = html.fromstring(response.read())
        cont = ''.join([html.tostring(x) for x in soup.xpath(mod.xpath)])  

        file = open('%s.html' % site, 'w')
        file.write(cont)
        file.close()     

if __name__ == '__main__':
    parse()
