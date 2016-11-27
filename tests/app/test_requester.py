import unittest
from lib.app.requester import Requester
from testHelpers.mockRequests import MockRequests
from testHelpers.mockCollection import MockCollection

class TestRequester(unittest.TestCase):
    def setUp(self):
        self.auth = ('fake@email.com', 'password')

    def test_getOrganizationsSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(200)

        # Act
        result = self.requester.getOrganizations()

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/organizations')

    def test_getOrganizationsError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(500)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Get organizations request returned 500 code'):
            self.requester.getOrganizations()

    def test_getCollectionsSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(200)

        # Act
        result = self.requester.getCollections()

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/collections')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})

    def test_getCollectionsError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(400)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Get collections request returned 400 code'):
            self.requester.getCollections()

    def test_getCollectionSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(200)

        # Act
        result = self.requester.getCollection("fakeCollectionId")

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/collections/fakeCollectionId')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})

    def test_getCollectionError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(400)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Get collection request returned 400 code'):
            self.requester.getCollection("collectionId")

    def test_getWidgetsSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(200)

        # Act
        result = self.requester.getWidgets("fakeCollectionId")

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/widgets')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})
        self.assertEqual(self.requester.requests.data, {'collectionId': 'fakeCollectionId'})

    def test_getWidgetsError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(404)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Get widgets request returned 404 code'):
            self.requester.getWidgets("collectionId")

    def test_createBoardSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(201)

        # Act
        result = self.requester.createBoard("boardName", "fakeCollectionId")

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/widgets')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})
        self.assertEqual(self.requester.requests.data, {'collectionId': 'fakeCollectionId', 'name': 'boardName', 'type': 'board'})

    def test_createBoardError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(404)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Post board request returned 404 code'):
            self.requester.createBoard("boardName", "fakeCollectionId")


    def test_addColumnToBoardSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(201)

        # Act
        result = self.requester.addColumnToBoard("columnName", "fakeBoardId")

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/columns')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})
        self.assertEqual(self.requester.requests.data, {'widgetCommonId': 'fakeBoardId', 'name': 'columnName'})

    def test_addColumnToBoardError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(404)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Post column request returned 404 code'):
            self.requester.addColumnToBoard("columnName", "fakeBoardId")

    def test_getTagByNameSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(200)

        # Act
        result = self.requester.getTagByName("tagName")

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/tags')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})
        self.assertEqual(self.requester.requests.data, {'name': 'tagName'})

    def test_getTagByNameError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(404)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Get tag request returned 404 code'):
            self.requester.getTagByName("tagName")

    def test_getCardByIdSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(200)

        # Act
        result = self.requester.getCardById("156")

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/cards/156')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})

    def test_getCardByIdError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(500)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Get card request returned 500 code'):
            self.requester.getCardById("256")

    def test_addTagToCardSuccess(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(200)

        # Act
        result = self.requester.addTagToCard("156", "987")

        # Assert
        self.assertEqual(self.requester.requests.auth, self.auth)
        self.assertEqual(self.requester.requests.url, 'https://favro.com/api/v1/cards/156')
        self.assertEqual(self.requester.requests.headers, {'organizationId': 'organizationId'})
        self.assertEqual(self.requester.requests.data, {'addTagIds': ['987']})

    def test_addTagToCardError(self):
        # Arrange
        self.requester = Requester('fake@email.com', 'password', 'organizationId')
        self.requester.requests = MockRequests(500)

        # Act/Assert
        with self.assertRaisesRegex(Exception, 'Update card request returned 500 code'):
            self.requester.addTagToCard("256", "987")


if __name__ == '__main__':
    unittest.main()