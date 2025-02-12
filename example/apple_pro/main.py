from dataclasses import dataclass

from lib.parsers.apple_pro.spiders.spider_apple_pro import AppleProSpider
from lib.protocols import CrawlerProtocol, RunnerProtocol


@dataclass
class AppleProCrawler(CrawlerProtocol):
    runner: RunnerProtocol
    crawler: AppleProSpider = None

    async def run_crawler(self):
        self.crawler = self.runner.create_crawler(AppleProSpider)
        self.runner.crawl(self.crawler)

    def stop_crawler(self):
        if self.crawler:
            self.crawler.stop()
