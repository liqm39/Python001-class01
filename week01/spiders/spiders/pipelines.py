# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline:
    def process_item(self, item, spider):
        moviename = item['moviename']
        #href = item['href']
        movietype = item['movietype']
        movietime = item['movietime']
        output = f'|{moviename}|\t|{movietype}|\t|{movietime}|\n\n'
        with open('./movie.txt', 'a+', encoding='gbk') as article:
            article.write(output)
        return item
