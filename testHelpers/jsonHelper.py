
class JsonHelper(object):    
    def getBasicCollectionJsonWithNameAndId(name, id):
        return {
            'name': name,
            'collectionId': id, 
            'shareWidgetsByDefault': 'shareWidgetsByDefault', 
            'publicSharing': 'publicSharing', 
            'archived': 'archived', 
            'sharedToUsers': JsonHelper.getBasicSharedToUsersArray()}

    def getBasicWidgetJsonWithNameAndId(name, id):
        return {
            'type': 'board',
            'name': name,
            'color': 'blue',
            'publicSharing': 'public', 
            'widgetCommonId': id, 
            'sharedToUsers': JsonHelper.getBasicSharedToUsersArray()}
    
    def getBasicSharedToUsersArray():
        return [
                {'userId': 'userId1', 'role': 'admin'},
                {'userId': 'userId2', 'role': 'admin'}]