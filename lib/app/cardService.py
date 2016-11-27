from lib.models.card import Card

class CardService(object):
    def __init__(self, requester):
        self.requester = requester 

    def getCard(self, cardId):
        cardJson = self.requester.getCardById(cardId)
        card = Card(cardJson)
        return card
