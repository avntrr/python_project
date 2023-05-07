from transactions import Transaction
from database import database

trnsct_123 = Transaction()

while True:
    print("\nMenu:")
    print("1. Input Shopping List")
    print("2. Update Item Code")
    print("3. Update Item Quantity")
    print("4. Delete Item")
    print("5. Check Order")
    print("6. Complete Shopping")
    print("7. Reset")
    print("8. Exit")

    try:
        pilihan = int(input("\nSelect Menu (1-8): "))
    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue

    cancel = False
    batal = 'c'

    if pilihan == 1:
        while True:
            item_code = input("Item Code (type 'c' to cancel): ")
            if item_code.lower() == batal:
                cancel = True
                break # keluar dari loop

            if item_code not in database:
                print("Item code not found, please try again.")
                continue

            while True:
                jumlah_item = input("Item Quantity (type 'c' to cancel): ")
                if jumlah_item.lower() == batal:
                    cancel = True
                    break # keluar dari loop
                try:
                    jumlah_item = int(jumlah_item)
                    break
                except ValueError:
                    print("Enter a number!")
                    continue # kembali ke awal loop
            if cancel:
                break

            trnsct_123.add_item(item_code, jumlah_item)
            break # jika semua input valid, keluar dari loop

    elif pilihan == 2:
        while True:
            old_code = input("Item Code (type 'c' to cancel): ")
            if old_code.lower() == batal:
                cancel = True
                break
            if any(item[0] == old_code for item in trnsct_123.items):
                while True:
                    new_code = input("New Item Code (type 'c' to cancel): ")
                    if new_code.lower() == batal:
                        cancel = True
                        break
                    try:
                        trnsct_123.update_item_code(old_code, new_code)
                        print(f'Item "{old_code}" has been updated to "{new_code}"."!')
                        break
                    except ValueError:
                        print("The item code you entered does not exist. Please try again.")
                        continue
                if not cancel:
                    break
            else:
                print("The item code you entered does not exist. Please try again.")

    elif pilihan == 3:
        while True:
            item_code = input("Item Code (type 'c' to cancel): ")
            if item_code.lower() == batal:
                cancel = True
                break
            if any(item[0] == item_code for item in trnsct_123.items):
                while True:
                    new_qty = input("New Item Quantity (type 'c' to cancel): ")
                    if new_qty.lower() == batal:
                        cancel = True
                        break
                    try:
                        new_qty = int(new_qty)
                        trnsct_123.update_item_qty(item_code, new_qty)
                        print(f'Quantity of item "{item_code}" has been updated to {new_qty}.!')
                        break
                    except ValueError:
                        print("Enter a number!")
                        continue
                if not cancel:
                    break
            else:
                print("The item code you entered does not exist. Please try again.")

    elif pilihan == 4:
            while True:
                item_code = input("Item Code (type 'c' to cancel): ")
                if item_code.lower() == batal:
                    cancel = True
                    break
                if any(item[0] == item_code for item in trnsct_123.items):
                    while True:
                        trnsct_123.delete_item(item_code)
                        print(f'Item "{item_code}" has been deleted!')
                        break
                    if not cancel:
                        break
                else:
                    print("The item code you entered does not exist. Please try again.")

    elif pilihan == 5:
        trnsct_123.check_order()

    elif pilihan == 6:
        trnsct_123.check_out()
        break
    
    elif pilihan == 7:
        trnsct_123.reset_transaction()
        print("Transaction has been reset!")

    elif pilihan == 8:
        break

    else:
        print("Invalid choice. Please enter a number from 1-8.")