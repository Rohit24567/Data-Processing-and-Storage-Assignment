class InMemoryDB:

    def __init__(self):
        self.total_data = {}
        self.transaction_in_progress = False
        self.transaction_data = {}

    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("There is already a transaction in progress.")
        self.transaction_in_progress = True
        self.transaction_data = {}

    def put(self, key, value):
        if not self.transaction_in_progress:
            raise Exception("You cannot perform the put function since there is no transaction in progress.")

        self.transaction_data[key] = value

    def get(self, key):
        if key in self.transaction_data:
            return self.transaction_data[key]
        elif key in self.total_data:
            return self.total_data[key]
        else:
            return None

    def commit(self):
        if not self.transaction_in_progress:
            raise Exception("You cannot perform the commit function since there is no transaction in progress.")

        self.total_data.update(self.transaction_data)
        self.transaction_in_progress = False
        self.transaction_data = {}

    def rollback(self):
        if not self.transaction_in_progress:
            raise Exception("You cannot perform the rollback function since there is no transaction in progress.")

        self.transaction_in_progress = False
        self.transaction_data = {}


# Create an instance of the InMemoryDB class and stores it in the variable db
db = InMemoryDB()

# Begins a transaction
db.begin_transaction()

# Creates key value pairs with the first value being the key and the second value being the value
db.put("Rohit",5)
db.put("Anna",15)
db.put("Mike",12)
db.put("Isabel", 26)

# Returns the values associated with each of the keys inside the get function
print(db.get("Rohit")) # Returns 5
print(db.get("Anna")) # Returns 15
print(db.get("Mike")) # Returns 12
print(db.get("Isabel")) # Returns 26

# Takes the information from self.transaction_data and updates self.total_data, so that the data from this transaction will be stored for future use even if the transaction is completed
db.commit()

# Begins a transaction
db.begin_transaction()

# Abort all changes and return the class to its original state with there being no transaction in progress and the current transaction data having nothing
db.rollback()