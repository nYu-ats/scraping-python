class ItemInfo(scrapy.Item):
    item_name =  scrapy.Field()
    item_image = scrapy.Field()
    item_category =  scrapy.Field()
    item_url =  scrapy.Field()
    item_price =  scrapy.Field()

class ShopInfo(scrapy.Item):
    shop_name = scrapy.Field()
    shop_url =  scrapy.Field()
    shop_update =  scrapy.Field()

