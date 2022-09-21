from datetime import timedelta
import requests
from bs4 import BeautifulSoup
import ast
import json
import urllib.parse

class LowTide():
    def __init__(self, location):
        self.location = location
        self.base_url = "https://www.tide-forecast.com/locations/"
        self.tide = "tides/latest"

    def location_url(self):
        """The Location medthod takes the location and base_url then returns the complete url"""
        if self.location == "Huntington Beach California":
            self.location = self.location[0:16]

        location = self.location.replace(" ", "-")
        print(location)
        url = self.base_url+location+"/"+self.tide
        return url 
    def convert_data(self):
        """The convert_data method uses beautifulsoup to find the script tag with the CData. 
        It then convert the Cdata to a python dictionary"""
        try: 
            total_url = self.location_url()
            r = requests.get(total_url)
            soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
            script_tag = soup.findAll('script')
            for i, script in enumerate(script_tag):
                 if 'CDATA' in script.contents or 'jQuery' in script.contents:
                        print(i, script) #identify the script that contains the data
                
            data = script_tag[19].contents
            scriptcontent = data[0].replace('//<![CDATA[', '').replace('window.FCGON =', '').replace('//]]>','').replace(';', '')
            data_dict = json.loads(scriptcontent)
            #print(data)
            return data_dict
        except Exception as e:
            print(e)
            return {}
         
    
    def low_tide(self):
        """The low_tide method queries the data_dict and return the Low tide data between sunset and sunrise"""
        data = self.convert_data()
        low_tide_list = []
        #print(data)
        tide_days = data['tideDays']
        
        try: 
            for j in tide_days:
                low_tide_dict = {}
                sunrise  = j['sunrise']
                sunset = j['sunset']
                date =j['date']
                tide_info = j['tides']
                for info in tide_info:
                    if sunrise <= info['timestamp'] <= sunset and info['type'] =='low':
                        low_tide_dict['Date'] = date
                        low_tide_dict['Time'] = info['time']
                        low_tide_dict['Height'] = round(info['height'], 2)
                        low_tide_list.append(low_tide_dict)
                        #print(date, info['time'], info['height'], info['type'])
            return {'status':1, 'data': low_tide_list}
        except Exception as e:
            print(e)
            return {'status':0, 'data': None}





low_tide = LowTide("Huntington Beach California")
print(low_tide.low_tide())
