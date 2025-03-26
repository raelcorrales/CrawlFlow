from crawlflow.core.pagenode.abstractnode import abstractNode

class MainNode(abstractNode):
    def __init__(self, url, parent=None):
        super().__init__(url, parent)
        