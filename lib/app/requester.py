import requests

class Requester(object):

    def __init__(self, email, password, organizationId):
        self.authHeader = (email, password)
        self.organization = {'organizationId': organizationId}
        self.favroBaseUrl = 'https://favro.com/api/v1/'
        self.requests = requests

    def getOrganizations(self):
        r = self.requests.get(self.favroBaseUrl + 'organizations', auth= self.authHeader)
        if r.status_code!=200:
            raise Exception("Get organizations request returned " + str(r.status_code) + " code")
        return r.json()

    def getCollections(self):
        r = self.requests.get(self.favroBaseUrl + 'collections', auth= self.authHeader, headers= self.organization)
        if r.status_code!=200:
            raise Exception("Get collections request returned " + str(r.status_code) + " code")
        return r.json()

    def getCollection(self, collectionId):
        r = self.requests.get(self.favroBaseUrl + 'collections/' + collectionId, auth= self.authHeader, headers= self.organization)
        if r.status_code!=200:
            raise Exception("Get collection request returned " + str(r.status_code) + " code")
        return r.json()

    def getWidgets(self, collectionId):
        data = {'collectionId': collectionId}
        r = self.requests.get(self.favroBaseUrl + 'widgets', auth= self.authHeader, headers= self.organization, data= data)
        if r.status_code!=200:
            raise Exception("Get widgets request returned " + str(r.status_code) + " code")
        return r.json()

    def createBoard(self, boardName, collectionId):
        data = {'collectionId': collectionId, 'name': boardName, 'type': 'board'}
        r = self.requests.post(self.favroBaseUrl + 'widgets',auth= self.authHeader, headers= self.organization, data= data)
        if r.status_code!=201:
            raise Exception("Post board request returned " + str(r.status_code) + " code")
        return r.json()

    def addColumnToBoard(self, columnName, boardId):
        data = {'widgetCommonId': boardId, 'name': columnName}
        r = self.requests.post(self.favroBaseUrl + 'columns', auth= self.authHeader, headers= self.organization, data= data)
        if r.status_code!=201:
            raise Exception("Post column request returned " + str(r.status_code) + " code")
        return r.json()

    def getTagByName(self, tagName):
        data = {'name': tagName}
        r = self.requests.get(self.favroBaseUrl + 'tags', auth= self.authHeader, headers= self.organization, data= data)
        if r.status_code!=200:
            raise Exception("Get tag request returned " + str(r.status_code) + " code")
        return r.json()

    def getCardById(self, cardId):
        r = self.requests.get(self.favroBaseUrl + 'cards/' + cardId, auth= self.authHeader, headers= self.organization)
        if r.status_code!=200:
            raise Exception("Get card request returned " + str(r.status_code) + " code")
        return r.json()

    def addTagToCard(self, cardId, tagId):
        data = {'addTagIds':[tagId]}
        r = self.requests.put(self.favroBaseUrl + 'cards/' + cardId, auth=self.authHeader, headers= self.organization)
        if r.status_code!=200:
            raise Exception("Update card request returned " + str(r.status_code) + " code")
    