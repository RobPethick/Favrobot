from lib.models.card import Card
import unittest

class TestCard(unittest.TestCase):

    def test_constructorParsesDictionary(self):
        # Arrange        
        name = 'testCard'
        widgetId = '123'
        cardId = '987'
        columnId = '456'
        organizationId = '012'

        dictionary = {'name': name, 'widgetCommonId': widgetId, 'cardId': cardId, 'columnId': columnId, 'organizationId':organizationId}
        
        # Act
        card = Card(dictionary)

        # Assert
        self.assertEqual(name, card.name)
        self.assertEqual(widgetId, card.widgetId)
        self.assertEqual(cardId, card.cardId)
        self.assertEqual(columnId, card.columnId)
        self.assertEqual(organizationId, card.organizationId)

if __name__ == '__main__':
    unittest.main()