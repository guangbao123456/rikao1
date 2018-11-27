# -*- coding: utf-8 -*-
import scrapy
import sys,io
import json
from ..items import CsdnItem
class BokeSpider(scrapy.Spider):
    name = 'boke'
    #allowed_domains = ['boke.com']
    start_urls = ['https://blog.csdn.net/IMbRl71u7pt5X29rlEu7/article/details/83443135']

    def parse(self, response):
        #sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

        title=response.xpath("//h1[@class='title-article']/text()").extract()[0]
        shijian=response.xpath("//div/span[@class='time']/text()").extract()[0]
        yuedushu=response.xpath("//div/span[@class='read-count']/text()").extract()[0]
        name=response.xpath("//a[@class='follow-nickName']/text()").extract()[0]
        zannum=response.xpath("//button[@class=' long-height hover-box btn-like ']/p/text()").extract()[0]
        pingnum=response.xpath("//a[@class='btn-comments long-height hover-box']/p/text()").extract()[0].strip()

        print(title,shijian,yuedushu,name,zannum,pingnum)
        like=response.xpath("//a[@class='btn-comments long-height hover-box']/p/text()").extract()[0].strip()
        article_num=response.xpath("//a[@class='btn-comments long-height hover-box']/p/text()").extract()[0].strip()
        fans=response.xpath("//a[@class='btn-comments long-height hover-box']/p/text()").extract()[0].strip()
        jifen=response.xpath("//a[@class='btn-comments long-height hover-box']/p/text()").extract()[0].strip()
        ranking=response.xpath("//a[@class='btn-comments long-height hover-box']/p/text()").extract()[0].strip()
        fangwen=response.xpath("//a[@class='btn-comments long-height hover-box']/p/text()").extract()[0].strip()
        author={'name':name,'article_num':article_num,'like':like,'fans':fans,'jifen':jifen,'ranking':ranking,'fangwen':fangwen}
        print(author)
        url='https://blog.csdn.net/IMbRl71u7pt5X29rlEu7/phoenix/comment/list/83443135?page=1&size=15&tree_type=1'
        yield scrapy.Request(url,callback=self.parse1)
    def parse1(self,response):

        all=json.loads(response.text)
        louceng=all['data']['floor_count']
        count=all['data']['count']
        print(count,louceng)
        for a in all['data']['list']:
            item=CsdnItem()
            neirong=a['info']['Content']
            articleid=a['info']['ArticleId']
            commentid=a['info']['CommentId']
            nickname=a['info']['NickName']
            posttime=a['info']['PostTime']
            ip=a['info']['IP']
            item['neirong']=neirong
            item['articleid']=articleid
            item['commentid']=commentid
            item['nickname']=nickname
            item['posttime']=posttime
            item['ip']=ip
            yield item


