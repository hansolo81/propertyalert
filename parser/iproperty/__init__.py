"""parser.iproperty"""
from lxml import html
import re
from time import strptime
from datetime import date

table_xpath='//div[@id="ct_result"]/*/table'
row_xpath='.//tr'

def within_price_range(row):
    pr = row.xpath('.//td[3]/span[2]')[0].text.strip()
    pr = re.search(r'(((\d{1,3},)+\d{3})|\d+)', pr)
    pr = int(pr.group(1).replace(',', ''))

    if pr <= 1200:
        return True
    return False


def parse(str_to_parse=""):
    results = []
    tree = html.fromstring(str_to_parse)
    tbl = tree.xpath(table_xpath)[0]
    rows = tbl.xpath(row_xpath)

    for row in rows:
        result_dict = {}
        if len(row.getchildren()) == 1 or not within_price_range(row):
            continue
        infocol = row.xpath('./td[3]')[0]
        maininfo = infocol.xpath('./span[1]/a')[0]
        result_dict['url'] = maininfo.get('href')
        result_dict['prop_name'] = maininfo.iterchildren('u').next().text
        result_dict['Price'] = infocol.xpath('./span[2]')[0].text
        thelot = infocol.xpath('br')

        for x in thelot:
            if x.tail is not None:
                txt = x.tail.split(':')
                if len(txt) == 2:
                    result_dict[txt[0]]= txt[1]

        results.append(result_dict)
        #print 'result_dict %s' % result_dict

    return results

        

        
    
        
    
