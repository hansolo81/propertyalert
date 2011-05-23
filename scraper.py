#!/usr/bin/env python

import sys
import sqlite3
from mechanize import ParseResponse, urlopen, urljoin, _form
from lxml import etree, html
from lxml.html import builder as E
from models import *
from collections import defaultdict

def execute():
    engine = create_engine('sqlite:///sitesdb', echo=False)
    metadata = MetaData(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    #sites = session.query(Site)
    users = session.query(User)

    for user in users:
        ## cosmetics goes here
        root = E.HTML(E.HEAD(
                        #E.LINK(href="base.css", rel="stylesheet", type="text/css")
                        ),                      
                      )
        body = E.BODY() 
        root.append(body)

        searches = user.searches
        if len(searches) == 0:
            continue
        search_dict = defaultdict(list)

        for search in user.searches:
            params = search.params
            site = search.site
            paramnames = site.paramnames
            searchparam = []

            for name in paramnames:
                if paramnames[name] is not None and params[name] is not None:
                    searchparam.append('%s=%s' % (paramnames[name], params[name]))

            searchparam = '&'.join(searchparam)

            ## some sites dont require forms. just pass parameters in url
            if not site.isform:
                url = 'http://%s?%s' % (site.url, searchparam)
                print 'parsing %s' % url
                response = urlopen(url)
            else:
                forms = ParseResponse(response, backwards_compat=False)
                theform = [form for form in forms if form.name == mod.formname\
                               and form.action == mod.formaction][0]

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
            modname = 'parser.%s' % site
            __import__(modname)
            mod = sys.modules[modname]
            res = mod.parse(response.read())

            if len(res) == 0:
                continue # no result

            search_dict[site.url.split('/')[0]].extend(wrap(res))
            #print 'cont is : %s' % cont

        for siteurl, trees in search_dict.iteritems():
            ## wrap elements in a nice table wrapper
            tbl = E.TABLE(E.THEAD(E.TH('%s' % siteurl)),
                          E.TBODY(*trees), 
                          style="width:700px;font-family:sans-serif;text-align:left")
            body.append(tbl)

        file = open('html/%s.html' % user.email, 'w')
        file.write(html.tostring(root))
        file.close()     

def wrap(results=[]):
    rows = []

    for d in results:
        print 'result is %s' % d
        tr = E.TR(
               E.TD(
                #E.DIV('%s' % d['prop_name'].capitalize()),
                E.DIV(E.A('%s' % d['prop_name'], href='%s' % d['url'])),
                *list(E.DIV('%s:%s' % (k,v)) for k,v in d.iteritems() \
                          if k not in('prop_name', 'url')),
                style="padding:6px 6px 12px 1px;"
                ),
             )

        rows.append(tr)
    return rows

if __name__ == '__main__':
    execute()
