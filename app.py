# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)
import urllib2
import json


@app.route('/')
def index():
    #Python is still broken so I'm taking a leap of faith with this one.
    prayer = urllib2.urlopen("https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=9fdb796382b04b4fb9c7958f34a6c767")
    news = prayer.read()

    #news = '''
    #{"status":"ok","source":"techcrunch","sortBy":"top","articles":[{"author":"Natasha Lomas","title":"I watched 1,000 hours of YouTube Kids’ content and this is what happened…","description":"What do you get if you endlessly recombine Spiderman and the Joker with Elsa from Frozen and lashings of product placement for junk food brands like..","url":"https://techcrunch.com/2017/11/12/i-watched-1000-hours-of-youtube-kids-content-and-this-is-what-happened/","urlToImage":"https://tctechcrunch2011.files.wordpress.com/2017/11/screen-shot-2017-11-12-at-11-06-33-am.png","publishedAt":"2017-11-12T10:18:56Z"},{"author":"Megan Rose Dickey","title":"What it’s like cooking with meal kit startup Chef’d","description":"I've tried both Blue Apron and HelloFresh before, but I don't like being locked into some subscription, so I decided to go with Chef'd this time around...","url":"https://techcrunch.com/2017/11/11/what-its-like-cooking-with-meal-kit-startup-chefd/","urlToImage":"https://tctechcrunch2011.files.wordpress.com/2017/11/img_4681.jpg","publishedAt":"2017-11-11T22:15:08Z"},{"author":"Jon Russell","title":"China’s second largest e-commerce firm just showed Alibaba has competition","description":"Alibaba invented China's biggest shopping day -- 11/11 aka Single's Day -- and it dominates the headlines with record sales year-on-year, but another company..","url":"https://techcrunch.com/2017/11/11/jd-com-singles-day/","urlToImage":"https://tctechcrunch2011.files.wordpress.com/2017/11/jd-com-1111.jpg","publishedAt":"2017-11-11T18:21:02Z"},{"author":"Lucas Matney","title":"Alibaba needed just 12 hours to equal last year’s Single’s Day sales","description":"Update: Alibaba ended Single's Day with $25 billion in GMV Well, it's 11/11 on the other side of the globe which means Alibaba is already raking in loads of..","url":"https://techcrunch.com/2017/11/10/alibaba-hits-nearly-18-billion-in-singles-day-orders-in-12-hours-already-surpassing-2016-sales/","urlToImage":"https://tctechcrunch2011.files.wordpress.com/2017/11/screen-shot-2017-11-10-at-3-52-59-pm.png","publishedAt":"2017-11-11T04:28:26Z"} ] }
    #'''
    nd = json.loads(news)
    articles = nd['articles']
    title = []
    author = []
    urls = []
    fv = []
    for article in articles:
        obj = {};
        obj['title'] = article['title']
        obj['author'] = article['author']
        obj['url'] = article['url']
        fv.append(obj)
    return render_template("index.html", articles=fv)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
