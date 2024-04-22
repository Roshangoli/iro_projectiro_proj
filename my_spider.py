import scrapy

class My_Spider(scrapy.Spider):
    name = 'my_spider'
    start_urls = [
        'https://en.wikipedia.org/wiki/Mobile_phone',
        'https://en.wikipedia.org/wiki/Dog',
        'https://en.wikipedia.org/wiki/Cat',
        'https://en.wikipedia.org/wiki/YouTube',
        'https://en.wikipedia.org/wiki/Twitter',
        'https://en.wikipedia.org/wiki/Collage',
        'https://en.wikipedia.org/wiki/Google',
        'https://www.google.com/search?q=dog+food+and+cat+food',
        'https://www.google.com/search?q=dog',
        'https://www.google.com/search?q=dog+breeds',
        'https://www.google.com/search?q=dog+names',
        'https://www.google.com/search?q=dog+crate'
    ]
# here we are going to place url for spider to scrap

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 200,  #this are the  Max pages
        'DEPTH_LIMIT': 11 # this are the Max depth
    }
#here this will do the scraping througt the pages we provided
    def parse(self, response): 
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'content': response.css('body').get(),
        }
        # this loop is use ful for Follow links to other pages 
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
