from dataclasses import dataclass
from twisted.internet import reactor

from .protocols import CrawlerProtocol, RunnerProtocol
from ..apple_pro.spiders.spider_apple_pro import AppleProSpider


@dataclass
class AppleProCrawler(CrawlerProtocol):
    runner: RunnerProtocol

    async def run_crawler(self):
        d = self.runner.crawl(AppleProSpider)
        d.addBoth(lambda _: reactor.stop())  # noqa
        reactor.run()  # noqa

    def stop_crawler(self):
        self.runner.stop()
