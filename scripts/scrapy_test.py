import scrapy


class CameraGear(scrapy.Item):
    price = scrapy.Field()


class BlogSpider(scrapy.Spider):
    name, start_urls = 'blogspider', ['http://www.adorama.com/SG18250EOSM.html']

    def parse(self, response):
        gear = [CameraGear(price=e.extract()) for e in response.css("span.BigPrice span::text")]
        print gear
        return

