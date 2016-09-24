import unittest
from lib.app.app import App
from testHelpers.mockRequester import MockRequester
from testHelpers.mockCollection import MockCollection

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = App('fake@email.com', 'password', 'organizationId')
        self.app.requester = MockRequester()
        self.basicCollection = {'name': 'name', 'collectionId': 'collectionId', 'shareWidgetsByDefault': 'shareWidgetsByDefault', 'publicSharing': 'publicSharing', 'archived': 'archived', 'sharedToUsers': [{'userId': 'userId1', 'role': 'admin'}, {'userId': 'userId2', 'role': 'admin'}]}


if __name__ == '__main__':
    unittest.main()