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
        self.assertEquals(name, card.name)
        self.assertEquals(tagId, card.tagId)
        self.assertEquals(organizationId, card.organizationId)
        self.assertEquals(color, card.color)

if __name__ == '__main__':
    unittest.main()