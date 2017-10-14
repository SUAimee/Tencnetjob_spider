# -*- coding: utf-8 -*-
import scrapy
from Tencnet.items import TencnetItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        # 获取当前页面的所有节点
        node_list = response.xpath('//tr[@class="odd"]|//tr[@class="even"]')
        print('==****////*==========***///*',len(node_list))
        # 遍历节点列表
        for node in node_list:
            # 创建item实例
            item = TencnetItem()
            # 抽取数据 赋值到item对赢得键
            item['job_name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['detail_link'] ='http://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            item['job_type'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_time'] = node.xpath('./td[5]/text()').extract()[0]

            # 将数据返回给引擎(此处数据还没有结束先不返回，否则会直接处理)
            #  构建详情页面的请求
            # print(item)
            print(item['detail_link'])
            # yield scrapy.Request(item['detail_link'], callback=self.parse_detail, meta={'key1': item})
            yield scrapy.Request(item['detail_link'], callback=self.parse_detail, meta={"key1": item})
            # yield item
        # 获取下一页url
        try:
            next_url = 'http://hr.tencent.com/'+response.xpath('//*[@id="next"]/@href').extract()[0]
            # 将url做成请求，返回给引擎
            yield scrapy.Request(next_url, callback=self.parse)
        except Exception as e:
            print(e)
            pass



    # 定义一个解析详情页的函数
    # def parse_detail(self, response):
    #     #     抽取职责和要求并保存在item
    #     print("-------------------",response)
    #     item = response.meta['key1']
    #     print(item)
    #     # item['duty'] = ''.join(response.xpath('//*[@id="position_detail"]/div/table/tr[3]/td/ul/li/text()').extract())
    #     # item['require'] = ''.join(response.xpath('//*[@id="position_detail"]/div/table/tr[4]/td/ul/li/text()').extract())
    #
    #     #   返回数据给引擎
    #     yield item

    def parse_detail(self, response):
        item = response.meta['key1']
        # print (item)

        item['duty'] = ''.join(response.xpath('//*[@id="position_detail"]/div/table/tr[3]/td/ul/li/text()').extract())
        item['require'] = ''.join(response.xpath('//*[@id="position_detail"]/div/table/tr[4]/td/ul/li/text()').extract())

        # 返回数据给引擎
        yield item