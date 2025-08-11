from abc import ABC, abstractmethod

# Abstract base class
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    # Concrete method (shared implementation)
    def get_connection_status(self):
        return "Checking connection status..."

# Concrete implementation 1
class MySQLDatabase(Database):
    def __init__(self, host, username):
        self.host = host
        self.username = username
        self.connected = False
    
    def connect(self):
        self.connected = True
        return f"Connected to MySQL database at {self.host}"
    
    def disconnect(self):
        self.connected = False
        return "Disconnected from MySQL database"
    
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not connected to database"
        return f"Executing MySQL query: {query}"

# Concrete implementation 2
class PostgreSQLDatabase(Database):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False
    
    def connect(self):
        self.connected = True
        return f"Connected to PostgreSQL at {self.host}:{self.port}"
    
    def disconnect(self):
        self.connected = False
        return "Disconnected from PostgreSQL"
    
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not connected"
        return f"Executing PostgreSQL query: {query}"

# Cannot instantiate abstract class
# db = Database()  # TypeError: Can't instantiate abstract class

# Can instantiate concrete classes
mysql_db = MySQLDatabase("localhost", "admin")
postgres_db = PostgreSQLDatabase("localhost", 5432)

# Use abstraction - same interface for different implementations
def database_operations(db):
    print(db.connect())
    print(db.get_connection_status())
    print(db.execute_query("SELECT * FROM users"))
    print(db.disconnect())
    print()

database_operations(mysql_db)
database_operations(postgres_db)