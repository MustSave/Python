'''
제작 당시 퀘이사존 robots.txt 내용
User-agent: *
Allow: /
Disallow: /*memo*/
Disallow: /*comment*/
Disallow: /*cart*/
Disallow: /*cart*/
Disallow: /*data/editor*/
Disallow: /*data/file*/
Disallow: /*bbs/sns_send.php
Disallow: /*bbs/view_img.php
Disallow: /*bbs/board.php
Disallow: /*bbs/link.php
Disallow: /*bbs/search.php
Disallow: /*bbs/password.php
Disallow: /*bbbs/view_img.php
Disallow: /*login*/
Disallow: /*qe_sale/sale*/
Disallow: /*bbs/qsz_qna*/
'''


import os
import requests
from bs4 import BeautifulSoup
import telegram as telepot

def isnew(vic):
    DIR = os.getcwd()+'/'
    with open(DIR+"list.txt", 'r', -1, 'utf-8') as f:
        prod = f.readline().strip()
    
    if prod == vic.strip():
        return False, prod
    else:
        f = open(DIR+"list.txt", 'w', -1, 'utf-8')
        f.write(vic)
        f.close()
        return True, prod

def telegram(msg, token, id):
    try:
        bot = telepot.Bot(token)
        bot.sendMessage(id, msg)
    except:
        pass
            

URL = "https://quasarzone.com/bbs/qb_tsy"
N = ""


req = requests.get(URL)
html = req.text
bs = BeautifulSoup(html, 'html.parser')



table = bs.find("div", "market-type-list market-info-type-list relative")
table = table.find("tbody").find_all("tr")

for idx, tr in enumerate(table):
    tr = tr.find('div', 'market-info-list-cont')

    link = "https://quasarzone.com"+tr.find('a', 'subject-link')['href']
    label = tr.find('span', 'label').text
    name = tr.find('span', 'ellipsis-with-reply-cnt').text
    price = tr.find('span', 'text-orange').text
    
    
    
    if idx == 0:
        b, N = isnew(link)
        if b == False:
            break

    if N.strip() == list.strip():
        break
    
    res = label + "\n\n" + name + "\n" + price + "\n\n" + link
    #print(res)
    #telegram(res, "", '')
