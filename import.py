from pywikibot.data import api
import pywikibot
import pprint
def getItems(site, itemtitle):
        params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
        request = api.Request(site=site,**params)
        return request.submit()
site = pywikibot.Site()
repo = site.data_repository()

def addAuthor(author_name):
    wikidataEntries = getItems(site, author_name)
    if len(wikidataEntries['search']) == 0 :
     data = {'labels': {'en': author_name}}
     item = pywikibot.ItemPage(repo)
     item.editEntity(data, summary=u'new author')

def addArticle(title):
    wikidataEntries = getItems(site, title)
    if len(wikidataEntries['search']) == 0 :
     data = {'labels': {'en': title}}
     item = pywikibot.ItemPage(repo)
     item.editEntity(data, summary=u'new article')

def addAuthorStatement(article_item_page,author_name):
  claim = pywikibot.Claim(repo, u'P2')
  author_item = getItems(site, author_name)
  author_id= author_item['search'][0]['id']
  target = pywikibot.ItemPage(repo, author_id)
  claim.setTarget(target)
  article_item_page.addClaim(claim)

import pandas as pd
df=pd.read_csv("articles_2010.csv")
for i, row in df.iterrows():
 if i > 1000 :
     break
 title=row['TI']
 print title
 addArticle(title)

 authors=row['AF']
 authors_list=authors.split(';')
 article_item = getItems(site, title)
 article_id= article_item['search'][0]['id']
 print article_id
 
 for author in authors_list:
  author_name_split=reversed(author.strip().split(','))
  author_name=' '.join(name.strip() for name in author_name_split)
  print author_name
  addAuthor(author_name)
  article_item_page = pywikibot.ItemPage(repo, article_id)
  if 'P2' in article_item_page.get()["claims"]:
   article_author_claims=article_item_page.get()["claims"]['P2']
   article_author_names=[claim.getTarget().get()['labels']['en'] for claim in article_author_claims] 
   if (author_name in article_author_names):
    print 'author statement exists'
    continue
  addAuthorStatement(article_item_page,author_name)
