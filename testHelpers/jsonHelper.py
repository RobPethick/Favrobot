
class JsonHelper(object):    
    def getBasicCollectionJsonWithNameAndId(name, id):
        return {
            'name': name,
            'collectionId': id, 
            'shareWidgetsByDefault': 'shareWidgetsByDefault', 
            'publicSharing': 'publicSharing', 
            'archived': 'archived', 
            'sharedToUsers': [
                {'userId': 'userId1', 'role': 'admin'},
                {'userId': 'userId2', 'role': 'admin'}]}

    