# Data Processing and Storage Assignment

This assignment builds an in memory database and allows transactions to go through and update the database. The begin_transaction() function starts a new transaction. The put(key, value) function creates a key value pair as part of the transaction that was previously created. The get(key) function returns the value of the certain key you are looking for. The commit() function copies the changes made to the current transaction and updates the main state of the database. The rollback() function aborts all changes and returns the database to the state in which there is no current transaction.

## How to Run the Code

First, you want to create an instance of the InMemoryDB class and store it in a variable. This is shown in line 45 of the memoryDB.py file. Next, you want to start a new transaction since there is no current transaction using the begin_transaction function. You can then use the put(key,value) function in order to create key-value pairs that will be associated with the current transaction. You can use the get(key) function in order to return the value of a certain key for the current transaction. You can use the commit() function in order to store the content of the current transation to the main state of the database. This is important if you want to use the get(key) function for a previous transaction that is not the current transaction. Finally, you can use the rollback() function in order to go back to the initial state of the instance, where there is no current transaction and no data inside self.transaction_data.

## How This Assignment Should Be Modified

I do think that the instructions are clear enough for this assignment to be an official assignment. One thing I would modify is the option of including more functions, such as a way to store the values for each customer. Since this assignment is about transactions, something that would make this assignment better is to try and have students build a database where the accounts of the customers are saved automatically for each transaction. For example, if customer A transfers $10 to customer B, then the database would store the intitial values of customer A and customer B, and then update both values after the $10 transfer goes through. I think this would be enough in order to make this assignment official.

