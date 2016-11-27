import unittest
from testHelpers.mockRequester import MockRequester
from lib.app.tagService import TagService

class TestTagService(unittest.TestCase):
    def setUp(self):
        self.requester = MockRequester()
        self.tagService = TagService(self.requester)

    def test_getCardByIdReturnsCorrectCard(self):
        # Arrange
        tagDictionary = {'name': 'testCard', 'tagId': '0001','color': '456', 'organizationId':'012'}
        
        self.requester.tag = tagDictionary

        # Act
        result = self.tagService.getTag('ABC')

        # Assert 
        self.assertEqual(result.name, 'testCard')

if __name__ == '__main__':
    unittest.main()