from models.user import User
from models.widget import Widget
import unittest

class TestUserMethods(unittest.TestCase):

    def test_constructorParsesDictionary(self):
        # Arrange
        userId = 'abc123'
        role = 'admin'
        dictionary = {'userId': userId, 'role': role}

        # Act
        user = User(dictionary)

        #Assert
        self.assertEqual(userId, user.userId)
        self.assertEqual(role, user.role)

class TestWidgetMethods(unittest.TestCase):

    def test_constructorParsesDictionary(self):
        # Arrange
        widgetType = 'board'
        name = 'testBoard'
        color = 'red'
        publicSharing = 'none'
        widgetId = '123'
        userId1 = 'abc123'
        userId2 = 'xyz789'
        userDictionary1 = {'userId': userId1, 'role': 'admin'}
        userDictionary2 = {'userId': userId2, 'role': 'admin'}
        dictionary = {'type': widgetType, 'name': name, 'color': color, 'publicSharing': publicSharing, 'widgetCommonId': widgetId, 'sharedToUsers': [userDictionary1, userDictionary2]}

        # Act
        widget = Widget(dictionary)

        # Assert
        self.assertEqual(widgetType, widget.type)
        self.assertEqual(name, widget.name)
        self.assertEqual(color, widget.color)
        self.assertEqual(publicSharing, widget.publicSharing)
        self.assertEqual(widgetType, widget.type)
        self.assertEqual(2, len(widget.users))
        self.assertEqual(userId1, widget.users[0].userId)
        self.assertEqual(userId2, widget.users[1].userId)

        

if __name__ == '__main__':
    unittest.main()
