from lib.models.tag import Tag
import unittest

class TestTag(unittest.TestCase):

    def test_constructorParsesDictionary(self):
        # Arrange        
        name = 'testCard'
        tagId = '123'
        organizationId = '012'
        color = 'green'

        dictionary = {'name': name, 'tagId': tagId, 'color': color, 'organizationId':organizationId}
        
        # Act
        card = Tag(dictionary)

        # Assert
        self.assertEqual(name, card.name)
        self.assertEqual(tagId, card.tagId)
        self.assertEqual(organizationId, card.organizationId)
        self.assertEqual(color, card.color)

if __name__ == '__main__':
    unittest.main()