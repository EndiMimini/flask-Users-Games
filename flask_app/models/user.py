from flask_app.config.mysqlconnection import connectToMySQL
# user.py
class User:
    db='teams'
    def __init__(self,data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * from users;'
        results = connectToMySQL(cls.db).query_db(query)
        users= []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * from users WHERE id= %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def getOneForLogin(cls, data):
        query = 'SELECT * from users WHERE email= %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        return results[0]['id']


    @classmethod
    def save(cls, data):
        query= 'INSERT INTO users (firstName, lastName, email) VALUES (%(firstName)s, %(lastName)s, %(email)s);'
        return connectToMySQL(cls.db).query_db(query, data)
    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET firstName=%(firstName)s, lastName=%(lastName)s, email=%(email)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query= 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

