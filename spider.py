from urllib.request import urlopen
from linkFinder import linkFinder
from utilities import *

class spider:

    # Class variables (shared among all instances)
    projectName = ""
    baseUrl = ""
    domainName = ""
    queueFile = ""
    crawledFile = ""
    queue = set()
    crawled = set()

    def __init__(self, projectName, baseUrl, domainName) -> None:
        self.projectName = projectName
        self.baseUrl = baseUrl
        self.domainName = domainName
        self.queueFile = spider.projectName + "/queue.txt"
        self.crawledFile = spider.projectName + "/crawled.txt"
        self.boot()
        self.crawlPage("First spider", spider.baseUrl)
        
    def boot(self):
        createProjectDirectory(spider.projectName)
        createDataFiles(spider.projectName, spider.baseUrl)
        spider.queue = fileToSet(spider.queueFile)
        spider.crawled = fileToSet(spider.crawledFile)

    def crawlPage(self, spiderName, pageUrl):
        if pageUrl not in spider.crawled:
            print(spiderName + " now crawling " + pageUrl)
            print("Queued: " + str(len(spider.queue)) + " | Crawled: " + str(len(spider.crawled)))
            spider.addLinksToQueue(spider.gatherLinks(pageUrl))
            spider.queue.remove(pageUrl)
            spider.crawled.add(pageUrl)
            spider.updateFiles()

    def gatherLinks(self, pageUrl):
        htmlString = ""
        try:
            response = urlopen(pageUrl)
            if response.getheader("Content-Type") == "text/html":
                htmlBytes = response.read()
                htmlString = htmlBytes.decode("utf-8")
            finder = linkFinder(spider.baseUrl, spider.pageUrl)
        except:
            print("Error, cannot crawl page")
            return set()
        return finder.pageLinks()
    
    def addLinksToQueue(self, links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            if spider.domainName not in url:
                continue
            spider.queue.add(url)

    def updateFiles(self):
        setToFile(spider.queue, spider.queueFile)
        setToFile(spider.crawled, spider.crawledFile)