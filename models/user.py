class User(object):
    def __init__(self, json):
        self.userId = json['userId']
        self.role = json['role']
