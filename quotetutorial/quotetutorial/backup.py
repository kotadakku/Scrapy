import scrapy
from scrapy import FormRequest
from scrapy.utils.response import open_in_browser
from .items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    # start_urls = [
    #     'http://quotes.toscrape.com/'
    # ]
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    def parse(self, response):

        all_div_quotes = response.css('div.quote')


        for quote in all_div_quotes:
            items = QuotetutorialItem()
            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tag = quote.css('a.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tag

            yield items

            yield {'titletext':title,
                   'author':author,
                   'tag':tag
                   }
        # next_page = response.css('li.next a::attr(href)').get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        next_page = 'http://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number +=1
            yield response.follow(next_page, callback=self.parse)
