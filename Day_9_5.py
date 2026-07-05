# Dependency Inversion Priciple
# Depend on abstraction , not concrete implementations


class MySQLDatabase:
    def connect(self):
        # some mwthod to connect with a db 
        
        
class App:
    def __init__(self):
        self.db = MySQLDatabase()
        
    def start(self):
        self.db.connect()
        
        
# correct way to implement is using abstraction

from abc import ABC, abstractmethod

#abstraction
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

# concrete implementation    
class My_SQL_DataBase(Database):
    def connect(self):
        # method that will connect the database 
        print("Connecting to SQL batabase !")

class Postgre_SQL_Database(database):
    def connect(self):
        # method that will connect the database 
        print("Connecting Postgre batabase !")
  
# High-level module depends on abstraction 
class App:
    def __init__(self, db: Database):
        self.db = db
        
    def start(self):
        self.db.connect()
        
if __name__ == "__main__":
    app = App(Postgre_SQL_Database())
    app.start()
    
    app2 = App(My_SQL_DataBase())
    app2.start()
        
