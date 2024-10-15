# book_scraper
## Project Description

This is a web scraping project developed using the Scrapy framework to extract book information from the [http://books.toscrape.com](http://books.toscrape.com) website. The scraped data includes book titles, prices, and availability status, which are then stored in a MongoDB database.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Elliexyeung777/book_scraper.git
   cd bookscraper
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure MongoDB is installed and running.

## Usage

1. Run the spider:
   ```
   scrapy crawl bookspider
   ```

2. Check the data in MongoDB:
   ```
   python check_mongodb.py
   ```

## Project Structure

- `bookspider.py`: Defines the spider logic
- `pipelines.py`: Handles data storage to MongoDB
- `settings.py`: Contains project settings
- `items.py`: Defines the structure of data items
- `middlewares.py`: Contains custom middlewares
- `check_mongodb.py`: Used to verify stored data

## Configuration

Modify MongoDB connection settings in the `settings.py` file:

```python
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'bookscraper'
```

## Features

- Scrapes book information including title, price, and availability
- Stores data in MongoDB for easy access and analysis
- Implements custom retry logic and user-agent rotation for improved scraping reliability
- Provides a script to verify stored data

## Customization

You can customize the scraper by modifying the following:

- `bookspider.py`: Adjust the parsing logic or add new fields to scrape
- `middlewares.py`: Modify existing middlewares or add new ones for custom behavior
- `settings.py`: Adjust Scrapy settings or add new configuration options

## Troubleshooting

If you encounter any issues:

1. Ensure MongoDB is running and accessible
2. Check the console output for any error messages
3. Verify your internet connection
4. Make sure the target website's structure hasn't changed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Scrapy documentation](https://docs.scrapy.org/en/latest/)
- [Books to Scrape](http://books.toscrape.com) for providing a scraping-friendly website for testing
```
