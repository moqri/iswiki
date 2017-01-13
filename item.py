from pywikibot.data import api
import pywikibot
import pprint

def getItems(site, itemtitle):
        params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
        request = api.Request(site=site,**params)
        return request.submit()

site = pywikibot.Site()
repo = site.data_repository()
item = pywikibot.ItemPage(repo)
wikidataEntries = getItems(site, "author 102")
print wikidataEntries
data = {'labels': {'en': 'paper 102'}}
#item.editEntity(data, summary=u'Edit item')
#print item.get()
