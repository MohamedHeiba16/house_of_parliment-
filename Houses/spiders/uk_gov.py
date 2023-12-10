import scrapy


class UkGovSpider(scrapy.Spider):
    name = "uk.gov"
    allowed_domains = ["www.shop.parliament.uk"]
    start_urls = ["https://www.shop.parliament.uk/collections/homeware"]

    def parse(self, response):
        urls=response.xpath('//div[@class="product-grid__single grid-cell grid-cell-1of3-1of2-1of1"]/a[1]/@href')
        for url in urls:
            relavinte_url = 'https://www.shop.parliament.uk'+ url.get()
            yield response.follow(relavinte_url, callback=self.parse_results)
            
        next_page = response.xpath("//span[@class='next']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_results(self, response):

        Title = response.xpath("//h1[@class='page-heading']/text()").get().strip()
        Price = response.xpath("//span[@class='product__price--current']/text()").get().strip()
        SKU = response.xpath("//span[@class='variant-sku']/text()").get().strip()
    
        yield{
            "title":Title,
            "price":Price,
            "SKU":SKU
              }
        


        
