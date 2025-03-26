from crawlflow.core.pagenode.abstractnode import abstractNode

class EdgeNode(abstractNode):
    def __init__(self, url, parent=None):
        super().__init__(url, parent)