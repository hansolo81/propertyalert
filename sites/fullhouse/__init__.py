"""models.fullhouse"""
isform=False    
url = 'www.fullhouse.com.my/public/pub_search_result.asp'
formname = None
formaction = None
searchparams = {'ad_type': 'r',
                'state': 'kl',
                'city': '554',
                'city': '658',
                'pro_type': 'r'
               } 
params = {'proptype_param' : 'pro_type',
          'searchtype_param' : 'ad_type',
          'state_param' : 'state',
          'city_param': 'city',
         } 
xpath='//div[@id="search_box"]'                    
