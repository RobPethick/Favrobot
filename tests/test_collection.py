from models.collection import Collection
import unittest


class TestCollectionMethods(unittest.TestCase):

    def setUp(self):
        name = 'testCollection'
        shareWidgetsByDefault = 'public'
        collectionId = '135'
        publicSharing = 'True'
        archived = 'False'
        userId1 = 'abc123'
        userId2 = 'xyz789'
        userDictionary1 = {'userId': userId1, 'role': 'admin'}
        userDictionary2 = {'userId': userId2, 'role': 'admin'}
        dictionary = {'name': name, 'collectionId': collectionId, 'shareWidgetsByDefault': shareWidgetsByDefault, 'publicSharing': publicSharing, 'archived': archived, 'sharedToUsers': [userDictionary1, userDictionary2]}      
        self.basicCollection = Collection(dictionary)


    def test_constructorParsesDictionary(self):
        # Arrange
        name = 'testCollection'
        shareWidgetsByDefault = 'public'
        collectionId = '135'
        publicSharing = 'True'
        archived = 'False'
        userId1 = 'abc123'
        userId2 = 'xyz789'
        userDictionary1 = {'userId': userId1, 'role': 'admin'}
        userDictionary2 = {'userId': userId2, 'role': 'admin'}
        dictionary = {'name': name, 'collectionId': collectionId, 'shareWidgetsByDefault': shareWidgetsByDefault, 'publicSharing': publicSharing, 'archived': archived, 'sharedToUsers': [userDictionary1, userDictionary2]}

        # Act
        collection = Collection(dictionary)

        # Assert
        self.assertEqual(name, collection.name)
        self.assertEqual(publicSharing, collection.publicSharing)
        self.assertEqual(shareWidgetsByDefault, collection.shareWidgetsByDefault)
        self.assertEqual(collectionId, collection.collectionId)
        self.assertEqual(archived, collection.archived)
        self.assertEqual(2, len(collection.users))
        self.assertEqual(userId1, collection.users[0].userId)
        self.assertEqual(userId2, collection.users[1].userId)

    def test_addWidgetsAddsValuesToArray(self):
        # Arrange
        fakeWidgetList = ['A', 'B']

        # Act
        self.basicCollection.addWidgets(fakeWidgetList)
        
        # Assert

if __name__ == '__main__':
    unittest.main()