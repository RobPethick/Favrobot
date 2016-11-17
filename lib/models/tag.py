class Tag(object):
    def __init__(self, json):
        self.tagId = json['tagId']
        self.organizationId = json['organizationId']
        self.color = json['color']
        self.name = json['name']
