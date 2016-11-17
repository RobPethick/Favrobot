class Card(object):
    def __init__(self, json):
        self.cardId = json['cardId']
        self.organizationId = json['organizationId']
        self.widgetId = json['widgetCommonId']
        self.columnId = json['columnId']
        self.name = json['name']
