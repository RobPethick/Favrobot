import unittest
from testHelpers.mockRequester import MockRequester
from testHelpers.jsonHelper import JsonHelper
from lib.app.widgetService import WidgetService
from lib.models.collection import Collection

class TestWidgetService(unittest.TestCase):
    def setUp(self):
        self.requester = MockRequester()
        self.widgetService = WidgetService(self.requester)

    def test_getWidgetsReturnsWidgetsCorrectly(self):
        # Arrange
        widgetA = JsonHelper.getBasicWidgetJsonWithNameAndId("WidgetA", "AAA")
        widgetB = JsonHelper.getBasicWidgetJsonWithNameAndId("WidgetB", "BBB")
        widgetC = JsonHelper.getBasicWidgetJsonWithNameAndId("WidgetC", "CCC")
        widgetD = JsonHelper.getBasicWidgetJsonWithNameAndId("WidgetD", "DDD")

        self.requester.widgets = {'entities': [widgetA, widgetB, widgetC, widgetD]}

        # Act
        result = self.widgetService.getWidgets("1234567")

        # Assert
        self.assertTrue(self.requester.hasGetWidgetsBeenCalled)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].widgetId, "AAA")
    
    def test_addWeeklyBoardCreatesBoardAndCorrectColumnList(self):
        # Arrange
        widget = JsonHelper.getBasicWidgetJsonWithNameAndId("Daily Goals Board", "12345")
        self.requester.widget = widget

        # Act
        self.widgetService.addWeeklyBoard(Collection(JsonHelper.getBasicCollectionJsonWithNameAndId("Daily Goals", 123456)), "Daily Goals 01-01-2017")

        # Assert
        self.assertTrue(self.requester.hasCreateBoardBeenCalled)
        self.assertEqual(self.requester.columnsAdded, ['Doing', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])


if __name__ == '__main__':
    unittest.main()