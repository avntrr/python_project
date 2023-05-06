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
### C. Flowchart
After identifying the main features, we will design an application flowchart to visually depict the workflow of the application. The flowchart will clarify how these features interact with each other and assist in planning the overall application structure.
![tugas drawio](https://user-images.githubusercontent.com/54851225/236611753-95620a7b-c6bf-4d4b-a1bb-0f22e72787fe.png)

`Start`: This is the starting point of the flowchart.

`Menu`: Create a decision box labeled "Menu Choice" with arrows pointing to decision boxes for each option in the menu (1-8).

`Input Shopping List`: From "Menu Choice", if the choice is 1, direct to the process "Input Item Code". Here are the steps:

```python
Request input for item name;
Request input for item quantity;
Request input for item price;
Add item to shopping list;
Return to Menu.
```
`Update Item Code`: to modify previously entered items. If the choice is 2, direct to the process "Update Item Code". Here are the steps:

```python
Request input for old item name;
Request input for new item name;
Update item name;
Return to Menu.
```
`Update Item Quantity`: to change the quantity of previously entered items. If the choice is 3, direct to the process "Update Item Quantity". Here are the steps:

```python
Request input for item code;
Request input for new item quantity;
Update item quantity;
Return to Menu.
```
`Delete Item`: to delete previously entered items. If the choice is 4, direct to the process "Delete Item". Here are the steps:

```python
Request input for item code;
Delete item from shopping list;
Return to Menu.
```
`Check Order`: if the choice is 5, direct to the process "Check Order". Here are the steps:

```python
Display the shopping list;
Return to Menu.
```
`Complete Shopping`: if the choice is 6, direct to the process "Complete Shopping". Here are the steps:

```python
Display the shopping list and total price;
Save the transaction to the database;
End.
```
`Reset Transaction`: if the choice is 7, direct to the process "Reset Transaction". Here are the steps:

```python
Delete all items from the shopping list;
Return to Menu.
```
`Exit Application`: If the choice is 8, end.
