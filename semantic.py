import pandas as pd
import os

articles_csv='../data/articles.csv'
articles_file='articles.txt'
authors_file='authors.txt'
keywords_file='keywords.txt'
try:
    os.remove(authors_file)
except OSError:
    pass
try:
    os.remove(articles_file)
except OSError:
    pass
try:
    os.remove(keywords_file)
except OSError:
    pass

df=pd.read_csv(articles_csv)
df.DE.fillna('',inplace=True)
articles_file=open(articles_file,'a')
authors_file=open(authors_file,'a')
keywords_file=open(keywords_file,'a')
all_authors=[]
all_keywords=[]

def addAuthor(author_name):
    if author_name in all_authors:
		return
    all_authors.append(author_name)    	
    text='''    
---start---
\'\'\'this_title\'\'\'
{{author papers}}
[[Category:author]]
---end---
'''
    text= text.replace('this_title',author_name)
    authors_file.write(text)
    

def addKeyword(keyword):
    if keyword in all_keywords:
		return
    all_keywords.append(keyword)    	
    text='''
---start---
\'\'\'this_title\'\'\'
{{keyword papers}}
[[Category:keyword]]
---end---
'''
    text= text.replace('this_title',keyword)
    keywords_file.write(text)
    

def addArticle(paper):
    authors_list=paper['authors'].split(';') 
    i=0
    authors_text=''
    for author in authors_list:
        author_name_split=reversed(author.strip().split(','))
        author_name=' '.join(name.strip() for name in author_name_split)
        addAuthor(author_name)
        authors_text=authors_text+ author_name +','
    keywords_list=paper['keywords'].split(';') 
    i=0
    keywords_text=''
    for keyword in keywords_list:
        keyword=keyword.strip()
        if keyword != '':
            addKeyword(keyword)
            keywords_text=keywords_text+ keyword+','
        
    text=''' 
---start---
\'\'\'this_title\'\'\'
{{header}}
{{article
|author= this_author
|source= this_source
|year= this_year
|abstract = this_abstract
|keyword = this_keyword
}}
{{topics}}
{{theories}}
{{methods}}
{{footer}}
[[Category:article]]
---end---
'''
    text= text.replace('this_title',paper['title'])
    text= text.replace('this_author',authors_text)
    text= text.replace('this_source',paper['source'])
    text= text.replace('this_year',str(paper['year']))
    text= text.replace('this_abstract',paper['abstract'])
    text= text.replace('this_keyword',keywords_text)
    articles_file.write(text)

for i,row in df.iterrows():
    if i > 10000 : break
    paper={
    'title':row['TI'],
    'authors':row['AF'],
    'source':row['SO'],
    'keywords':row['DE'],
    'abstract':row['AB'],
    'year':row['PY'],
    'volum':row['VL'],
    'issue':row['IS'],
    'bpage':row['BP'],
    'epage':row['EP']
        }
    print paper['title']

    addArticle(paper)

articles_file.close()
authors_file.close()
keywords_file.close()


