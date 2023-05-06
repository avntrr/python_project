# Building Supermarket Self-Service Application with Python.
### A. Background
Shopping at supermarkets often requires a lot of time and effort, especially when there are long queues at the cashier or when searching for desired items. Self-service applications in supermarkets have become an innovative solution to speed up the shopping process and reduce waiting time at the cashier. I build a simple self-service application using Python, one of the most popular and easy-to-learn programming languages.
### B. Requirements
#### Library
```pandas``` : to perform mathematical operations in applications such as adding item prices or applying discounts. <br>
```SQLite```: used to store shopping data inputted by customers. <br>
```Tabulate```: used to display the shopping data in a neat and easy-to-read table format. <br>
```class Transactions``` : to manage data and functions related to shopping transactions, this class will have the following attributes and methods:
```python
Attributes:

items: a list that contains shopping items
transactions: a list that contains transaction data
conn: a connection object to access SQLite database
c: a cursor object to execute SQL commands on the database
```
```python
Methods:

init(): initializes the Transaction object and creates a table in the database if it does not exist.

add_item(): adds an item to the shopping list.

update_item_code(): updates the item code in the shopping list.

update_item_qty(): updates the quantity of an item in the shopping list.

delete_item(): deletes an item from the shopping list.

reset_transaction(): deletes all items from the shopping list.

insert_to_list(): inserts transaction data into the transactions list.

check_order(): displays the shopping list, calculates the total price, and applies any discounts.

insert_to_table(): saves transaction data to the database.

check_out(): finalizes the transaction and saves data to the database.

del(): closes the database connection when the object is deleted.
```
