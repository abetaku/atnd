# -*- coding: utf-8 -*-

import datetime
import urllib2
import json

class Atnd:

        def __init__(self, event_id='', keyword='', keyword_or='', category='', category_detail='',
                     ym='', ymd='', user_id='', nickname='', twitter_id='', facebook_id='',
                     google_plus_id='', owner_id='', owner_nickname='', owner_twitter_id='',
                     owner_facebook_id='', owner_google_plus_id='', start='', order='',
                     count=''):
		
                self.api_url = 'http://api.atnd.org/eventatnd/event/?'
		
                self.query_pram = { 'event_id':event_id,
                                    'keyword':keyword,
                                    'keyword_or':keyword_or,
                                    'category':category,
                                    'category_detail':category_detail,
                                    'ym':ym,
                                    'ymd':ymd,
                                    'user_id':user_id,
                                    'nickname':nickname,
                                    'twitter_id':twitter_id,
                                    'facebook_id':facebook_id,
                                    'google_plus_id':google_plus_id,
                                    'owner_id':owner_id,
                                    'owner_nickname':owner_nickname,
                                    'owner_twitter_id':owner_twitter_id,
                                    'owner_facebook_id':owner_facebook_id,
                                    'owner_google_plus_id':owner_google_plus_id,
                                    'start':start,
                                    'order':order,
                                    'count':count,
                                    'format':'json' }

                query = []
                for key, val in self.query_pram.items():
                        if not val=='':
                                query.append('%s=%s' % (key, val))
                else:
                        self.query_url = self.api_url + '&'.join(query)

                self.json_data = {}

                #self.category_api_url = 'http://api.atnd.org/eventatnd/category/?format=json'
                #self.json_category_data = {}


        def get_json_data(self):
                response = urllib2.urlopen(self.query_url)
                res = response.read()
                response.close()
                self.json_data = json.loads(res)


        def show_results(self):
                date_func = lambda date_str: str(datetime.datetime.strptime(date_str[:19], "%Y-%m-%dT%H:%M:%S"))
                event_list = []
                for e in self.json_data['events'][0]['event']:
                        event = date_func(e['started_at']) + '\t' + e['title']+ '\t' + e['event_url']
                        event_list.append(event)
                        print event
                return event_list


if __name__ == '__main__':
        obj = Atnd(keyword='ruby', ym='201303')
        obj.get_json_data()
        obj.show_results()
        #print(json.dumps(obj.json_data["events"][0]["event"], sort_keys=True, indent=4))

        
	
