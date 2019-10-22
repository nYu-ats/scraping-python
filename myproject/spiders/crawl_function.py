import scrapy

class TitySpider(scrapy.Spider):
    name='tity'
    allowed_domain = ['tity.ocnk.net']
    start_urls = ['https://tity.ocnk.net/']

    def parse(self, response):
        item = {}
        shop = {}
        shop['name'] = 'tity'
        shop['about'] = response.css('title::text').get()
        temp = response.css('.news_date::text').getall()
        shop['update'] = temp[0] + temp[1] + temp[2]

        for url in response.css('ul.side_contents pickupcategory_list a::attr("href")'):
            url += '?num=50&img=200&sort=rank'
            yield response.follow(url, self.fetchItemInfo)

        print(shop)
        print(item)

    def fetchItemInfo(self, response):
        itemCat = response.css('div.page_title h2::text').get()
        itemBody = response.css('ul.layout200.item_list.clearfix').get()
        itemTemp = []
        for n in range(0,5):
            css ='li:nth-child(' + str(n+1) +')'
            itemTemp = itemBody.css(css).get()

        for m in itemTemp:
            itemName = m.css('span.goods_name::text').get()
            itemPrice = m.css('div.selling_price::text').get()
            itemImage = m.css('div.global_photo.itemph_itemlist_15274 img::attr("href")')
            item[itemName] = [itemCat, itemImage, itemPrice]








