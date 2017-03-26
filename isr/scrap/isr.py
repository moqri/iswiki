import urllib
import urllib2
import httplib2
import time
import os.path
import random
from bs4 import BeautifulSoup
base="http://pubsonline.informs.org/toc/isre/"
url = base+'1/1'   
body = {}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
http = httplib2.Http()
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))
headers = {'Cookie': response['set-cookie']}

for v in range(6,28):
    for i in range(1,5):
        title='htmls/'+str(v)+'_'+str(i)
        if not os.path.isfile(title):
            print ([v,i])
            r=random.uniform(0, 1)
            time.sleep(r) # delays for 5 seconds
            url=base+str(v)+'/'+str(i)
            response, html = http.request(url, 'GET', headers=headers)
            f = open(title, 'w')
            f.write(html) 
            f.close()