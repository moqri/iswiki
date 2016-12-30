import pandas as pd
df=pd.read_table('auth.txt')
print df.head()
df['a1']=df.apply(lambda x:x['AF'])
