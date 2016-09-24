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





if __name__ == '__main__':
    unittest.main()