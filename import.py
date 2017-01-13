from pywikibot.data import api
import pywikibot
import pprint
def getItems(site, itemtitle):
        params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
        request = api.Request(site=site,**params)
        return request.submit()
site = pywikibot.Site()
repo = site.data_repository()


import pandas as pd
df=pd.read_csv("articles_2010.csv")
for i in range(1):
    row=next(df.iterrows())[1]
    title=row['TI']
    authors=row['AF']

authors_list=authors.split(';')
for author in authors_list:
    last,first= author.strip().split(',')
    author_name=first +" "+ last
    print author_name
    wikidataEntries = getItems(site, author_name)   
    if len(wikidataEntries['search']) == 0 :
     data = {'labels': {'en': author_name}}
     item = pywikibot.ItemPage(repo)
     item.editEntity(data, summary=u'Edit item')
 
