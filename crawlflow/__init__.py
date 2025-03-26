from crawlflow.request import dinamicrequest, staticrequest, parsehtml
from urllib.parse import urljoin, urlparse

from crawlflow.core.pagenode.mainnode import MainNode
from crawlflow.core.pagenode.edgenode import EdgeNode

class Crawlflow(object):
    def __init__(self, url, request_class, delay = 1):
        self.url = url
        self.visited_urls = set()
        self.delay = delay
        
        self.request = request_class(self.url)
        
        self.node = self.generate_node(MainNode(self.url))
        self.current_node = 0
        self.keep_crawl = True
        self.nodes = [self.node]
        
    def generate_node(self, node):
        url = node.url
        self.request.fetch_page()
        # Get Link List
        for link in self.request.get_links():
            self.nodes.append(MainNode(link, url) if self.request.is_base(url, link) else EdgeNode(link, url))
        # Create Node
        node.visited = True
        node._title = self.request.get_title()
        node._content = self.request.get_content()
        
        # Return Node
        return node
    
    def crawl(self, url, depth=0):
        self.request.open_driver()
        while self.keep_crawl:
            self.generate_node(self.nodes[self.current_node].url)
            self.current_node += 1
            if self.current_node >= len(self.nodes):
                self.keep_crawl = False
                self.request.close()
            