import requests

class Requester(object):

    def __init__(self, email, password, organizationId):
        self.authHeader = (email, password)
        self.organization = {'organizationId': organizationId}
        self.favroBaseUrl = 'https://favro.com/api/v1/'

    def getOrganizations(self):
        r = requests.get(self.favroBaseUrl + 'organizations', auth= self.authHeader)
        if r.status_code!=200:
            raise Exception("Get organizations request returned " + str(r.status_code) + " code")
        return r.json()

    def getCollections(self):
        r = requests.get(self.favroBaseUrl + 'collections', auth= self.authHeader, headers= self.organization)
        if r.status_code!=200:
            raise Exception("Get collections request returned " + str(r.status_code) + " code")
        return r.json()

    def getCollection(self, collectionId):
        r = requests.get(self.favroBaseUrl + 'collections/' + collectionId, auth= self.authHeader, headers= self.organization)
        if r.status_code!=200:
            raise Exception("Get collection request returned " + str(r.status_code) + " code")
        return r.json()

    def getWidgets(self, collectionId):
        data = {'collectionId': collectionId}
        r = requests.get(self.favroBaseUrl + 'widgets', auth= self.authHeader, headers= self.organization, data= data)
        if r.status_code!=200:
            raise Exception("Get widgets request returned " + str(r.status_code) + " code")
        return r.json()

    def createBoard(self, boardName, collectionId):
        data = {'collectionId': collectionId, 'name': boardName, 'type': 'board'}
        r = requests.post(self.favroBaseUrl + 'widgets',auth= self.authHeader, headers= self.organization, data= data)
        if r.status_code!=201:
            raise Exception("Post board request returned " + str(r.status_code) + " code")
        return r.json()

    def addColumnToBoard(self, columnName, boardId):
        data = {'widgetCommonId': boardId, 'name': columnName}
        r = requests.post(self.favroBaseUrl + 'columns', auth= self.authHeader, headers= self.organization, data= data)
        if r.status_code!=201:
            raise Exception("Post column request returned " + str(r.status_code) + " code")
        return r.json()