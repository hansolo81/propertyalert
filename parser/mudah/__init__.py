"""parser.mudah"""
from lxml import html
import re
from time import strptime
from datetime import date
from mechanize import urlopen, urljoin

table_xpath='//table[@class="listing_thumbs"]'
row_xpath='.//tr'

def within_date_range(row):
    try:
        dt = row.xpath('./th[@class="listing_thumbs_date"]')[0].text.strip()
        if dt in ('Yesterday', 'Today'):
            return True
    except:
        return False

    return False

def within_price_range(row):
    pr = row.xpath('./td[2]/br[1]')[0].tail.strip()
    pr = re.search(r'(((\d{1,3}\s)+\d{3})|\d+)', pr)
    pr = int(pr.group(1).replace(' ', ''))

    if pr <= 1200:
        return True
    return False

def parse(str_to_parse=""):
    results = []
    tree = html.fromstring(str_to_parse)
    tbl = tree.xpath(table_xpath)[0]

    for row in tbl.xpath(row_xpath):        
        result_dict = {}

        if within_date_range(row) and within_price_range(row):
            ln = row.xpath('./td[2]/a')[0]
            result_dict['url'] = ln.get('href')
            result_dict['prop_name'] = ln.text.strip()
            pg_response = urlopen(result_dict['url'])
            new_tree = html.fromstring(pg_response.read())
            adparams = new_tree.xpath('//table[@class="AdParams"]//tr/td')

            #print 'adparams is %s' % adparams

            for param in adparams:
                txt = ''.join(param.xpath('.//text()')).strip().replace('\n', '').replace('\t','').split(':')
                result_dict[txt[0]] = txt[1]
            #print 'result_dict is %s' % result_dict

            results.append(result_dict)    
    return results
        

        
    
        
    
