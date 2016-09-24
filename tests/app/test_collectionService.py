import unittest
from testHelpers.mockRequester import MockRequester
from testHelpers.mockWidgetService import MockWidgetService
from testHelpers.jsonHelper import JsonHelper
from lib.app.collectionService import CollectionService

class TestCollectionService(unittest.TestCase):
    def setUp(self):
        self.requester = MockRequester()
        self.widgetService = MockWidgetService()
        self.collectionService = CollectionService(self.requester, self.widgetService)

    def test_getCollectionIdFromNameReturnsCorrectIdForName(self):
        # Arrange
        collectionA = JsonHelper.getBasicCollectionJsonWithNameAndId("CollectionA", "AAAAA")
        collectionB = JsonHelper.getBasicCollectionJsonWithNameAndId("CollectionB", "BBBBB")
        collectionC = JsonHelper.getBasicCollectionJsonWithNameAndId("CollectionC", "CCCCC")

        self.requester.collections = {'entities': [collectionA, collectionB, collectionC]}

        # Act
        result = self.collectionService.getCollectionIdFromName("CollectionB")

        # Assert 
        self.assertTrue(self.requester.hasGetCollectionsBeenCalled)
        self.assertEqual(result, "BBBBB")


if __name__ == '__main__':
    unittest.main()