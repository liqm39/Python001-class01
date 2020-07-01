# -*- coding: utf-8 -*-
import scrapy

#from bs4 import BeautifulSoup as bs

from spiders.items import SpidersItem

from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        i = 0
        base_urls = 'https://maoyan.com'
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies:
            if i == 10:
                break
            item = SpidersItem()
            moviename = movie.xpath('./a/text()')
            moviehref = movie.xpath('./a/@href')
            item['moviename'] = moviename.extract_first().strip()
            item['href'] = base_urls + moviehref.extract_first().strip()

            i += 1
            yield scrapy.Request(url=item['href'], meta={'item': item}, callback=self.parse2)


    def parse2(self, response):

        item = response.meta['item']
        movieinfos = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for movieinfo in movieinfos:
            movietype = movieinfo.xpath('./ul/li/a/text()')
            movietime = movieinfo.xpath('./ul/li[last()]/text()')
            item['movietype'] = movietype.extract()
            item['movietime'] = movietime.extract_first().strip()
        yield item





