import unittest
from testHelpers.mockRequester import MockRequester
from lib.app.cardService import CardService

class TestCardService(unittest.TestCase):
    def setUp(self):
        self.requester = MockRequester()
        self.cardService = CardService(self.requester)

    def test_getCardByIdReturnsCorrectCard(self):
        # Arrange
        cardDictionary = {'name': 'testCard', 'widgetCommonId': '123', 'cardId': '987', 'columnId': '456', 'organizationId':'012'}
        
        self.requester.card = cardDictionary

        # Act
        result = self.cardService.getCard('ABC')

        # Assert 
        self.assertEqual(result.name, 'testCard')

if __name__ == '__main__':
    unittest.main()