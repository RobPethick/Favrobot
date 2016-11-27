from lib.models.tag import Tag

class TagService(object):
    def __init__(self, requester):
        self.requester = requester 

    def getTag(self, name):
        tagJson = self.requester.getTagByName(name)
        tag = Tag(tagJson)
        return tag 
