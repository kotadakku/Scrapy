# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/b/ref=KCdls_brws_kdd?ie=UTF8&node=6165851011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=N0ZXWC80CN9JMWVV5EW8&pf_rd_r=N0ZXWC80CN9JMWVV5EW8&pf_rd_t=101&pf_rd_p=2a647384-3f89-4660-bbd3-703fe588a09b&pf_rd_p=2a647384-3f89-4660-bbd3-703fe588a09b&pf_rd_i=11552285011'
    ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css(".s-access-title::text").extract()
        product_author = response.css(".a-color-secondary .a-text-normal").css("::text").extract()
        product_price = response.css(".a-price-whole").css("::text").extract()
        product_imagelink = response.css(".cfMarker::attr(src)").extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
