This program was created for a Private Equity firm seeking data for price analysis of several medical marijuana dispensaries.

Extracted data:
This project extracts dispensary product price, size, and hyperlink data in csv format.  The extracted data looks like this sample:

{
	link,price,size,title
	https://www.link.com/,5.00,"3.5g","product name"
}

Spiders:
This project contains a spider for each domain and you can list them using the list command:

$ scrapy list

Running the spiders
You can run a spider using the scrapy crawl command, such as:

$ scrapy crawl toscrape-css

All scraped data saves automatically to the data.csv file found in the directory
