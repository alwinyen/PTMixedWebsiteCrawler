import scrapy
class NewbloommagSocialSpider(scrapy.Spider):
    name = 'newbloommagSocialSpider'
    start_urls = ['https://newbloommag.net/category/main/social-movements/']

    def smart_truncate(self, content, length=163, suffix='...'):
        if len(content) <= length:
            return content
        else:
            return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'Topic': post.css('.cb-post-title a::text')[0].get(),
                'Blurb': self.smart_truncate(post.css('.cb-excerpt ::text')[0].get()),
                'Image': post.css('.cb-mask img::attr(src)').extract()[0],
                'Link': post.css('.cb-mask a::attr(href)').extract()[0],
                'OP': "New Bloom"
            }