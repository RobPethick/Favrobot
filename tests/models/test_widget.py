
from lib.models.widget import Widget
import unittest
import datetime

class TestWidget(unittest.TestCase):

    def setUp(self):
        widgetType = 'board'
        name = 'testBoard'
        color = 'red'
        widgetId = '123'
        dictionary = {'type': widgetType, 'name': name, 'color': color, 'widgetCommonId': widgetId}
        self.basicWidget = Widget(dictionary)

    def test_constructorParsesDictionary(self):
        # Arrange
        widgetType = 'board'
        name = 'testBoard'
        color = 'red'
        widgetId = '123'
        dictionary = {'type': widgetType, 'name': name, 'color': color, 'widgetCommonId': widgetId}

        # Act
        widget = Widget(dictionary)

        # Assert
        self.assertEqual(widgetType, widget.type)
        self.assertEqual(name, widget.name)
        self.assertEqual(color, widget.color)
        self.assertEqual(widgetType, widget.type)

    def test_isDailyGoalsBoardReturnsFalseIfNotABoard(self):
        # Arrange
        self.basicWidget.type = 'backlog'      
        self.basicWidget.name = 'Daily Goals 13-01-20'
        
        # Act
        isDailyBoard = self.basicWidget.isDailyBoard()

        # Assert
        self.assertFalse(isDailyBoard)

    def test_isDailyGoalsBoardReturnsFalseIfNameDoesntMatch(self):
        # Arrange
        self.basicWidget.type = 'board'     
        self.basicWidget.name = 'TestBoard' 
        
        # Act
        isDailyBoard = self.basicWidget.isDailyBoard()

        # Assert
        self.assertFalse(isDailyBoard)

    def test_isDailyGoalsBoardReturnsTrueIfBoardAndNameMatches(self):
        # Arrange
        self.basicWidget.type = 'board'     
        self.basicWidget.name = 'Daily Goals 13-06-15' 
        
        # Act
        isDailyBoard = self.basicWidget.isDailyBoard()

        # Assert
        self.assertTrue(isDailyBoard)

    def test_returnDateReturnsNullIfNotDailyGoalsBoard(self):
        # Arrange
        self.basicWidget.type = 'backlog'     
        self.basicWidget.name = 'Daily Goals 13-06-15' 
        
        # Act
        isDailyBoard = self.basicWidget.getDate()

        # Assert
        self.assertIsNone(isDailyBoard)

    def test_correctlyParsesDate(self):
        # Arrange
        self.basicWidget.type = 'board'     
        self.basicWidget.name = 'Daily Goals 13-06-2020' 
        
        # Act
        isDailyBoard = self.basicWidget.getDate()

        # Assert
        self.assertEqual(isDailyBoard, datetime.datetime(2020, 6, 13))

 
if __name__ == '__main__':
    unittest.main()
