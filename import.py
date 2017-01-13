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
