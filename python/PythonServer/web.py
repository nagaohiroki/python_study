#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import webbrowser
import urllib
import requests
import mechanicalsoup

def ReqTest():
    url = 'https://www.google.co.jp/?gws_rd=ssl'
    target_html = requests.get(url).text
    req = urllib.request.Request(url)
    local_filename, headers = urllib.request.urlretrieve(url)
   # print(target_html)
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    title =  login_page.soup.select('head')


def Feed():
    chrome = "'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' %s"
    browser = webbrowser.get(chrome)
    rss_url = 'http://qiita.com/tags/vim/feed.atom'
    # rss_url = "http://rss.dailynews.yahoo.co.jp/fc/rss.xml"
    yahoo_news_dic = feedparser.parse(rss_url)
    for entry in yahoo_news_dic.entries:
        print(entry.link)
        print(entry.title)
        browser.open(entry.link)
        break

if __name__ == '__main__':
    ReqTest()
