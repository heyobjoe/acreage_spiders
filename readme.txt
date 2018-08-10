Spider status:

hc...fully functional
cnd...fully functional
aac...1 start url functioning
sw...title lost loading csv to excel

ccc...js required
tvr...crawler required, js required?
bp...js required



Extracted data
This project extracts dispensary product price, size, and hyperlink data in csv format.  The extracted data looks like this sample:

{
	link,price,size,title
	https://www.link.com/,5.00,"3.5g","product name"
}
Spiders
This project contains a spider for each domain and you can list them using the list command:

$ scrapy list

You can learn more about the spiders by going through the Scrapy Tutorial.

Running the spiders
You can run a spider using the scrapy crawl command, such as:

$ scrapy crawl toscrape-css
All scraped data saves automatically to the data.csv file found in the directory