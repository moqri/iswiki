from pywikibot.data import api
import pywikibot
import pprint

def getItems(site, itemtitle):
	params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
	request = api.Request(site=site,**params)
	return request.submit()

import pywikibot
site = pywikibot.Site()
repo = site.data_repository()
item = pywikibot.ItemPage(repo, u"Q4")
claim = pywikibot.Claim(repo, u'P2')

wikidataEntries = getItems(site, "author 102")
author_id= wikidataEntries['search'][0]['id']

target = pywikibot.ItemPage(repo, author_id)
claim.setTarget(target)
item.addClaim(claim)

