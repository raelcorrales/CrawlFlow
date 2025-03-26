

class abstractNode:
    def __init__(self, url, parent=None):
        self.url = url
        self.parent = parent
        self.visited = False
        
        self._title = ""
        self._description = ""
        self._author = ""
        self._content = ""
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def set_tittle(self, title):
        self._title = title
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def set_description(self, description):
        self._description = description
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def set_author(self, author):
        self._author = author
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def set_content(self, content):
        self._content = content
    