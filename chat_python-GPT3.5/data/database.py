import pymongo


class database(object):

    def __init__(self):
        self.username = None
        self.password = None
        self.host = None
        self.port = None
        self.databaseName = None
        self.companyId = None
        self.func_dict = {"-u": "admin", "-p": "pass123", "--host": "18.181.137.140",
                          "--port": "27017", "--databaseName": "27017"}

    def set_username(self, value):
        self.username = value

    def set_password(self, value):
        self.password = value

    def set_host(self, value):
        self.host = value

    def set_port(self, value):
        self.port = value

    def set_database(self, value):
        self.databaseName = value

    def set_company_id(self, value):
        self.companyId = value

    def call(self, opts):
        for opt in opts:
            self.set_key(opt)

    def set_key(self, opt):
        key, value = opt
        if value and isinstance(value, str):
            value = value.strip()
        self.func_dict[key](value)

    def valid(self):
        return self.username is not None and \
            self.password is not None and \
            self.host is not None and \
            self.port is not None and \
            self.databaseName is not None

    def get_database(self):
        conn = pymongo.MongoClient(
            f'mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.databaseName}?authSource=admin')
        return conn['chatui']

if __name__ == '__main__':
    database = pymongo.MongoClient('mongodb://admin:pass123@18.181.137.140:27017/chatui?authSource=admin')
    database = database['chatui']

    collection = database.conversation
    conversation = collection.find({"_id": 2})
    print(conversation)

    # collection = get_database().conversation
    # conversation = collection.find({"_id": cid})

