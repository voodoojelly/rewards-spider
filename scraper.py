import scrapy

class RewardSpider(scrapy.Spider):
    name = 'reward-spider'
    start_urls = ['https://www.citiworldprivileges.com/index.php/sg-singapore/bundlet/citigourmetpleasures']

# custom settings to create destination file
    custom_settings = { 
        'FEEDS' : { 'citibankdatapull.csv' : { 'format': 'csv',}}
    }


    def parse(self, response):
        INFO_SELECTOR = '.card2c__info'
        NAME_SELECTOR = '.card2c__title::text'
        IMAGE_SELECTOR = '.visible-xxs'
        OFFERPAGE_SELECTOR = '.card2c__getLink a::attr("href")'
        OFFERMAIN_SELECTOR = '.card2c__off'
        OFFERDETAILS_SELECTOR = '.offer-details__body'
        OFFERDISCLAIMER_SELECTOR = '.offer-disclaimer'
        CATEGORY_SELECTOR = '.card2c__category'
        TNCSTATIC_SELECTOR = '.tnc-content'
        NEXT_SELECTOR = '.tab__navitem a::attr("href")'

        for reward in response.css(INFO_SELECTOR):
            print(f'reward {reward}')
            print(f'reward css {reward.css(INFO_SELECTOR).extract_first()}')
            yield {
                'name': reward.css(NAME_SELECTOR).extract_first(),
                'image': reward.css(IMAGE_SELECTOR).extract_first(),
                'offerpage': reward.css(OFFERPAGE_SELECTOR).extract_first(),
                'offermain': reward.css(OFFERMAIN_SELECTOR).extract_first(),
                'offerdetails': reward.css(OFFERDETAILS_SELECTOR).extract_first(),
                'offerdisclaimer': reward.css(OFFERDISCLAIMER_SELECTOR).extract_first(),
                'category': reward.css(CATEGORY_SELECTOR).extract(),
                'terms': reward.css(TNCSTATIC_SELECTOR).extract_first(),
            }

# command to run is --> scrapy runspider scraper.py