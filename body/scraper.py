# 組み込みモジュール:urllib（URLを扱える）、BeautifulSoupパッケージ
# Googleニュースのウェブスクレイパー作成

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site=site
    # site:ウェブサイトのURLを受け取る

    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html=r.read()
        parser="html.parser"
        sp=BeautifulSoup(html,parser)
        
        with open("gnews.txt","w") as f:

            for tag in sp.find_all("a"):
                url=tag.get("href")
                if url is None:
                    continue
                if "http" in url:
                    if "news" in url:
                        print("\n"+url)
                        f.write("\n"+url)                

news="https://news.google.com/?tab=nn"
Scraper(news).scrape()