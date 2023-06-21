from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')






class User:  #replace Class name
    DB = 'registration' # replace schema and all the table names including after self.
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    

    # @staticmethod
    # def validate_email(new_email):
    #     is_vaild = True
    #     if not EMAIL_REGEX.match(new_email['email']):
    #         flash('Email not valid!')
    #         is_vaild = False
        
    #     query = """
    #     SELECT * FROM users
    #     WHERE email = %(email)s;
    #     """
    #     results= connectToMySQL(User.DB).query_db(query, new_email)
    #     print(results)

    #     if results:
    #         flash('Email already exists!')
    #         is_vaild = False
    #     return is_vaild


    @staticmethod
    def validate_user(register):
        is_valid = True
        if len(register['first_name']) < 2:
            flash("First Name must be at least 2 character.")
            is_valid = False
        if len(register['last_name']) < 2:
            flash("Last Name must be at least 2 character.")
            is_valid = False
        if not EMAIL_REGEX.match(register['email']):
            flash('Please enter valid Email')
            is_valid = False
        if len(register['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if register['password'] != register['confirm_password']:
            flash("Passwords must match")
            is_valid = False
        return is_valid
    

    @classmethod
    def CreateUser(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    
    @classmethod
    def GetUserById(cls,data):
        query = """
        SELECT * FROM users
        WHERE id = %(user_id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    

    @classmethod
    def GetUserByEmail(cls,data):
        query = """
        SELECT * FROM users
        WHERE email = %(email)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    














    # @classmethod
    # def get_all(cls):
    #     query = """SELECT * FROM users;"""
    #     results = connectToMySQL(cls.DB).query_db(query)
    #     all_users = []
    #     for users in results:
    #         all_users.append( cls(users) )
    #     return all_users
    

    # @classmethod
    # def add_one(cls, data):
    #     query = """
    #     INSERT INTO users (first_name, last_name, email, password)
    #     VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );
    #     """
    #     results = connectToMySQL(cls.DB).query_db(query, data)
    #     return results
    
    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO users (user) VALUES (%(user)s);"
    #     return connectToMySQL(cls.DB).query_db(query,data)
    


    # @classmethod
    # def delete(cls,data):
    #         query = """
    #         DELETE FROM users WHERE id = %(id)s ; """ #<--
    #         results = connectToMySQL(cls.DB).query_db(query, data)
    #         return results
    
