import pywikibot
site = pywikibot.Site()
repo = site.data_repository()
item = pywikibot.ItemPage(repo)
data = {'labels': {'en': 'paper 102'}}
item.editEntity(data, summary=u'Edit item')

print item.get()
