import scrapy

from ...apple_pro.items import TableItem
from ...apple_pro.spiders.utils import get_paths_from_response


class AppleProSpider(scrapy.Spider):
    name = "models_spider"
    start_urls = ['https://apple-pro.ru/services/remont-iphone/']

    def parse(self, response, **kwargs):
        model_links = get_paths_from_response(response.text)

        for link in model_links:
            full_link = 'https://apple-pro.ru/' + link
            yield scrapy.Request(full_link, callback=self.parse_table)

    def parse_table(self, response):
        item = TableItem(
            table=response.xpath("//table").get()
        )

        yield item
