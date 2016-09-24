
class MockRequester(object):
    def __init__(self):
        self.hasGetCollectionBeenCalled = False
        self.hasGetCollectionsBeenCalled = False
    
    def getCollections(self):
        self.hasGetCollectionsBeenCalled = True
        return self.collections

    def getCollection(self, id):
        self.hasGetCollectionBeenCalled = True
        return self.collection