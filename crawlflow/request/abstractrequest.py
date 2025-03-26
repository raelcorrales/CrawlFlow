


class abstractRequest:
    def __init__(self, url):
        self.url = url
    
    def open_driver(self):
        pass

    def fetch_page(self):
        pass
        
    def get_title(self):
        pass
    
    def get_description(self):
        pass
    
    def get_author(self):
        pass
    
    def get_content(self):
        pass
    
    def get_links(self):
        pass
    
    def get_metadata(self):
        pass
    
    def close(self):
        pass