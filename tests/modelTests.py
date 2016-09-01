from models.user import User
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

if __name__ == '__main__':
    unittest.main()