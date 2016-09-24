
class MockRequester(object):
    def __init__(self):
        self.hasGetCollectionBeenCalled = False
        self.hasGetCollectionsBeenCalled = False
        self.hasGetWidgetsBeenCalled = False
        self.hasCreateBoardBeenCalled = False
        self.columnsAdded = []
    
    def getCollections(self):
        self.hasGetCollectionsBeenCalled = True
        return self.collections

    def getCollection(self, id):
        self.hasGetCollectionBeenCalled = True
        return self.collection
        
    def getWidgets(self, id):
        self.hasGetWidgetsBeenCalled = True
        return self.widgets

    def createBoard(self, boardName, collectionId):
        self.hasCreateBoardBeenCalled = True
        return self.widget
    
    def addColumnToBoard(self, columnName, boardId):
        self.columnsAdded.append(columnName)
