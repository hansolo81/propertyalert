"""parser.fullhouse"""
from lxml import html
import re
from time import strptime
from datetime import date

table_xpath='//form[@name="search_pro_result_form"]'
row_xpath='./div[@id="search_box"]'

def within_price_range(row):
    pr = row.xpath('.//tr[2]/td')[0].text.strip()
    pr = re.search(r'(((\d{1,3},)+\d{3})|\d+)', pr)
    pr = int(pr.group(1).replace(',', ''))

    if pr <= 1200:
        return True
    return False

def within_date_range(row):
    dt = row.xpath('.//tr/td[4]/br')[0].tail.strip()
    dt = re.search(r'(\d+)-(\w+)-(\d+)', dt)
    dt = date(int('20%s' % dt.group(3)), 
              strptime(dt.group(2),'%b').tm_mon, 
              int(dt.group(1)))
    diff = date.today() - dt
    #print diff.days

    if diff.days > 2:
        #row.getparent().remove(row)
        return False
    return True

def parse(str_to_parse=""):
    results = []
    tree = html.fromstring(str_to_parse)
    tbl = tree.xpath(table_xpath)[0]
    rows = tbl.xpath(row_xpath)

    for row in rows:
        result_dict = {}

        if not within_date_range(row) or not within_price_range(row):
            continue

        infocol = row.xpath('.//tr/td[3]')[0]
        thelot = infocol.xpath('.//tr/td')
        maininfo = thelot[0].iterchildren('a').next()
        result_dict['url'] = maininfo.get('href')
        result_dict['prop_name'] = maininfo.text.strip()
        result_dict['price'] = thelot[1].text.strip()

        thelot = thelot[2:]

        for x in thelot:
            txt = ''.join(x.xpath('.//text()')).strip().split(':')
            if len(txt) == 2:
                result_dict[txt[0]] = txt[1]

        results.append(result_dict)
        
    return results
        

        
    
        
    
