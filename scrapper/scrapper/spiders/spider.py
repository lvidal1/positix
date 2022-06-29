
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MesajilSpider(CrawlSpider):
    name = "mesajil"
    item_count = 0
    allowed_domain = [
        "mesajil.com"
    ]
    start_urls = [
        "https://mesajil.com/?s=rtx+tarjeta&post_type=product&dgwt_wcas=1"
    ]

    rules = {
        Rule(LinkExtractor(
            allow=(), restrict_xpaths=('//a[@class="next page-numbers"]'))),
        Rule(LinkExtractor(
            allow=(), restrict_xpaths=('//h3[@class="wd-entities-title"]')),
            callback='parse_item', follow=False
        ),
    }

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)

        # Product Info
        title = response.xpath(
            './/h1[@class="product_title wd-entities-title"]/text()').get()
        sku = response.xpath(
            './/span[@class="sku"]/text()').get()
        brand = response.xpath(
            './/tr[@class="woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_marca"]/td/p/text()').get()
        price = response.xpath(
            './/p[@class="price"]/span/bdi/text()').get()

        yield {'title': title,
               'sku': sku,
               'brand': brand,
               'price': price
               }
