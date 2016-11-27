from lib.models.card import Card

class CardService(object):
    def __init__(self, requester):
        self.requester = requester 

    def getCard(self, cardId):
        cardJson = self.requester.getCardById(cardId)
        card = Card(cardJson)
        return card
    
    def addTagToCard(self, card, tag):
        cardJson = self.requester.addTagToCard(self, card.cardId, tag.tagId)
        card = Card(cardJson)
        return card