# -*- coding: utf-8 -*-
import scrapy


class CccSpider(scrapy.Spider):
    name = 'ccc_spider'

    def start_requests(self):

        urls = [

            'http://www.ccc-ct.com/products/Pre-Rolled-Cones-c18238119',
            'http://www.ccc-ct.com/products/Cannabis-Oil-c18164003',
            'http://www.ccc-ct.com/products/Dry-Flower-c11606425',
            'http://www.ccc-ct.com/products/Indicas-c11606569',
            'http://www.ccc-ct.com/products/Hybrids-c11674238',
            'http://www.ccc-ct.com/products/Sativas-c11606568',
            # 'http://www.ccc-ct.com/products/CBD-c11674225',
            'http://www.ccc-ct.com/products/Edibles-c11988334',
            'http://www.ccc-ct.com/products/Concentrates-c11606184',
            'http://www.ccc-ct.com/products/High-CBD-c12689232',
            # 'http://www.ccc-ct.com/products/Tinctures-c11606512',
            'http://www.ccc-ct.com/products/Vaporizers-and-Cartridges-c11728483',
            # 'http://www.ccc-ct.com/products/Topicals-%26-Balms-c12626854',

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
