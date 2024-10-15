BOT_NAME = 'bookscraper'

SPIDER_MODULES = ['bookscraper.spiders']
NEWSPIDER_MODULE = 'bookscraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'bookscraper.pipelines.MongoDBPipeline': 300,
}

# MongoDB settings
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'bookscraper'