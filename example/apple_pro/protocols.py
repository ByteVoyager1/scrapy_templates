from typing import Protocol

from scrapy.utils.defer import Deferred


class RunnerProtocol(Protocol):
    def crawl(self, spider_cls, *args, **kwargs) -> Deferred:
        ...


class CrawlerProtocol(Protocol):
    runner: RunnerProtocol

    async def run_crawler(self):
        ...

    def stop_crawler(self):
        ...
