import scrapy
class TaiwantodayPoliticsSpider(scrapy.Spider):
    name = 'taiwantodayPoliticsSpider'
    start_urls = ['https://www.taiwantoday.tw/list_tt.php?unit=2&unitname=Politics-Top-News']

    def smart_truncate(self, content, length=163, suffix='...'):
        if len(content) <= length:
            return content
        else:
            return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

    def parse(self, response):
        for post in response.css('li'):
            yield {
                'Topic': post.css('h3::text').get(),
                # 'Blurb': self.smart_truncate(post.css('a::attr(href)').extract()),
                'Image': post.css('a::attr(href)').extract()[0],
                'Link': post.css('a::attr(href)').extract()[0],
                'OP': "Taiwanese Today"
            }