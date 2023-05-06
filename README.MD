# Building Supermarket Self-Service Application with Python.
### A. Background
Shopping at supermarkets often requires a lot of time and effort, especially when there are long queues at the cashier or when searching for desired items. Self-service applications in supermarkets have become an innovative solution to speed up the shopping process and reduce waiting time at the cashier. I build a simple self-service application using Python, one of the most popular and easy-to-learn programming languages.
### B. Requirements & Objectives
The requirements of this self-service supermarket application are:
* Primary functionality: The application must provide essential functionality such as adding items to the shopping list, updating item information, removing items, and completing transactions.
* Managing item data: The application should be able to store and access item data, such as item codes, item names, and prices. This data must be stored in an efficient and easily accessible data structure.
* Managing transactions: The application should be able to manage transactions, including calculating the total shopping cost, applying discounts, and saving transaction data into a database.
* Reliability: The application should be error-free and capable of handling various input scenarios and unexpected conditions. Extensive testing should be carried out to ensure the application's reliability.

The objectives of this self-service supermarket application are:<br>
* Increase transaction efficiency and speed: This application aims to expedite the transaction process at supermarkets by reducing the time required to process purchases and calculate the shopping total.
* Reduce human error: By automating the calculation of shopping totals and the application of discounts, this application aims to minimize errors that could occur when cashiers perform calculations manually.
* Enhance customer experience: This application is designed to provide a more convenient and straightforward shopping experience for customers, ultimately increasing customer satisfaction and retention.
* Facilitate tracking and data analysis: By storing transaction data in a database, this application enables supermarkets to track sales and analyze data to make better-informed business decisions.

### C. Flowchart and Code
#### 1. Flowchart
After identifying the main features, we will design an application flowchart to visually depict the workflow of the application. The flowchart will clarify how these features interact with each other and assist in planning the overall application structure.
![tugas drawio (1)](https://user-images.githubusercontent.com/54851225/236612303-9a3818c9-6b89-42ce-9c2e-2700511fe0cb.png)


`Start`: This is the starting point of the flowchart.

`Menu`: Create a decision box labeled "Menu Choice" with arrows pointing to decision boxes for each option in the menu (1-8).

`Input Shopping List`: From "Menu Choice", if the choice is 1, direct to the process "Input Item Code". Here are the steps:

```python
Request input for item code;
Request input for item quantity;
Add item to shopping list;
Return to Menu.
```
`Update Item Code`: to modify previously entered items. If the choice is 2, direct to the process "Update Item Code". Here are the steps:

```python
Request input for old item code;
Request input for new item code;
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
`Exit Application`: if the choice is 8, end.

#### 2. Library
```pandas``` : to perform mathematical operations in applications such as adding item prices or applying discounts. <br>
```SQLite```: used to store shopping data inputted by customers. <br>
```Tabulate```: used to display the shopping data in a neat and easy-to-read table format. <br>

#### 3.Code
* Create a Database for Items
Assume that the supermarket has already recorded its entire inventory, and each item has an ID. User who wants to input their purchases only needs to enter the item code and the quantity of the item.
```python
database = {
    '001': ['Beras', 10000],
    '002': ['Telur', 20000],
    '003': ['Gula', 15000],
    '004': ['Minyak Goreng', 25000],
    '005': ['Teh Celup', 5000],
    '006': ['Kopi', 3000],
    '007': ['Detergen', 20000],
    '008': ['Sabun Mandi', 15000],
    '009': ['Shampoo', 20000],
    '010': ['Pasta Gigi', 10000],
    '011': ['Buku Tulis', 5000],
    '012': ['Pensil', 2000],
    '013': ['Penghapus', 1000],
    '014': ['Rautan', 5000],
    '015': ['Pulpen', 3000],
    '016': ['Papan Tulis Kecil', 20000],
    '017': ['Spidol', 5000],
    '018': ['Penggaris', 3000],
    '019': ['Buku Gambar', 15000],
    '020': ['Crayon', 20000],
    '021': ['Tas Sekolah', 100000],
    '022': ['Sepatu Sekolah', 150000],
    '023': ['Seragam Sekolah', 200000],
    '024': ['Topi Sekolah', 50000],
    '025': ['Jas Almamater', 200000],
    '026': ['Kaos Olahraga', 50000],
    '027': ['Celana Olahraga', 50000],
    '028': ['Sepatu Olahraga', 150000],
    '029': ['Knee Pad', 50000],
    '030': ['Elbow Pad', 50000],
}
```
Save the file with the name `database.py` and import it into the `transactions.py` file.

* Create File ```Transactions.py```
To manage data and functions related to shopping transactions, this file will have the following attributes and methods:
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
* Create File `main.py`
`main.py` is responsible for handling user inputs, displaying menus, and executing the corresponding actions based on user choices. It imports the Transaction class from `transactions.py`, which manages the shopping transactions, as well as the necessary libraries such as `sqlite3`, `pandas`, and `tabulate`. Through a series of prompts and menu options, `main.py` guides the user to perform actions such as adding items to their shopping list, updating item information, deleting items, and completing the transaction.
