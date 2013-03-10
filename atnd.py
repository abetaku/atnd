# -*- coding: utf-8 -*-


class Atnd:

	def __init__(self, event_id='', keyword='', keyword_or='', category='', category_detail='',
				       ym='', ymd='', user_id='', nickname='', twitter_id='', facebook_id='',
				       google_plus_id='', owner_id='', owner_nickname='', owner_twitter_id='',
				       owner_facebook_id='', owner_google_plus_id='', start='', order='',
				       count='', formats=''):
		
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
							'format':formats }


	def get_query (self):
		query = []
		
		for key, val in self.query_pram.items():
			if not val=='':
				query.append('%s=%s' % (key, val))
		else:
			query_url = self.api_url + '&'.join(query)
			print query_url #test
		
		return query_url


if __name__ == '__main__':
	obj = Atnd(keyword_or='python,ruby', ym='201303')
	obj.get_query()
	
