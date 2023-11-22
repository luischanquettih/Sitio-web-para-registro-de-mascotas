def username():
    return 'username_de_mongodb'

def password():
    return 'clave_de_mongodb'

def mongo_uri():
    return 'mongodb+srv://{}:{}@cluster.vpw698x.mongodb.net/?retryWrites=true&w=majority'.format(username(),password())
    

