"""models.iproperty"""
isform = False   
url = 'www.iproperty.com.my/property/searchresult.aspx'
formname = None
formaction = None
searchparams = {'t': 'R',
                'gpt': 'AR',
                'st': 'KL',
                'ct': 'Keramat',
                'lo': '3' 
               }
params = {'proptype_param': 'gpt',
          'state_param': 'st',
          'city_param': 'ct',
          'range_param': 'lo'
         }
xpath = '//div[@id="ct_result"]'
                    

    

    
