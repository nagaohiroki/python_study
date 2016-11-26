﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
import webbrowser
if __name__ == '__main__':
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

