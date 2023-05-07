from tabulate import tabulate
import sqlite3
import pandas as pd
from database import database

class Transaction:
    def __init__(self):
        self.items = []
        self.transactions = []
        self.conn = sqlite3.connect('database.db')  # Membuat koneksi ke database SQLite
        self.c = self.conn.cursor()  # Membuat objek cursor untuk menjalankan perintah SQL
        # Membuat tabel jika belum ada
        self.c.execute('''CREATE TABLE IF NOT EXISTS transactions
                     (No_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     Kode_Item TEXT, 
                     Nama_Item TEXT, 
                     Jumlah_Item INTEGER, 
                     Harga REAL, 
                     Total_Harga REAL, 
                     Diskon REAL, 
                     Harga_Diskon REAL)''')

    def add_item(self, item_code, qty):
        item_name = database[item_code][0]
        item_price = database[item_code][1]
        self.items.append([item_code, item_name, qty, item_price])

    def update_item_code(self, old_code, new_code):
        for item in self.items:
            if item[0] == old_code:
                item[0] = new_code
                break

    def update_item_qty(self, item_code, new_qty):
        for item in self.items:
            if item[0] == item_code:
                item[1] = new_qty
                break

    def delete_item(self, item_code):
        self.items = [item for item in self.items if item[0] != item_code]
        self.transactions = [transaction for transaction in self.transactions if transaction[0] != item_code]

    def reset_transaction(self):
        self.items.clear()

    def insert_to_list(self, kode_item, nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon):
        transaction_data = [kode_item, nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon]
        self.transactions.append(transaction_data)

    def check_order(self):
        total = 0
        print("\nYour Shopping List:")
        if self.items:
            for item in self.items:
                kode_item = item[0]
                nama_item = database[kode_item][0]
                jumlah_item = item[2]
                harga = database[kode_item][1]
                subtotal = jumlah_item * harga
                discount = 0
                if subtotal > 500000:
                    discount = 0.07
                elif subtotal > 300000:
                    discount = 0.06
                elif subtotal > 200000:
                    discount = 0.05

                discounted_price = subtotal * (1 - discount)
                self.insert_to_list(kode_item, nama_item, jumlah_item, harga, subtotal, discount, discounted_price)
            print(tabulate(self.transactions, headers=['Item Code', 'Name', 'Quantity', 'Price/Item', 'Price', 'Discount', 'Total Price'], tablefmt='pretty'))
            self.transactions.clear()  # clear the transactions after printing
        else:
            print("Belum ada item yang ditambahkan.")

    def insert_to_table(self):
        # Memasukkan setiap transaksi ke dalam database
        for transaction in self.transactions:
            self.c.execute("INSERT INTO transactions (Kode_Item, Nama_Item, Jumlah_Item, Harga, Total_Harga, Diskon, Harga_Diskon) VALUES (?, ?, ?, ?, ?, ?, ?)", transaction)
        self.conn.commit()  # Menyimpan perubahan

    def check_out(self):
        total = 0
        print("\nYour Shopping List:")
        if self.items:
            for item in self.items:
                kode_item = item[0]
                nama_item = database[kode_item][0]
                jumlah_item = item[2]
                harga = database[kode_item][1]
                subtotal = jumlah_item * harga
                discount = 0
                if subtotal > 500000:
                    discount = 0.07
                elif subtotal > 300000:
                    discount = 0.06
                elif subtotal > 200000:
                    discount = 0.05

                discounted_price = subtotal * (1 - discount)
                total += discounted_price
                self.insert_to_list(kode_item, nama_item, jumlah_item, harga, subtotal, discount, discounted_price)
            print(tabulate(self.transactions, headers=['Item Code', 'Name', 'Quantity', 'Price/Item', 'Price', 'Discount', 'Total Price'], tablefmt='pretty'))
            print("Total Shopping: Rp", total)
            self.insert_to_table()
        else:
            print("No items have been added yet.")
        return total

    def __del__(self):
        # Menutup koneksi ke database ketika objek dihapus
        self.conn.close()   