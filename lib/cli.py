# lib/cli.py

from helpers import (
    exit_program,
    list_suppliers,
    find_supplier_by_name,
    find_supplier_by_id,
    create_supplier,
    update_supplier,
    delete_supplier,
    list_products,
    find_product_by_name,
    find_product_by_id,
    create_product,
    update_product,
    delete_product,
    list_supplier_products,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_suppliers()
        elif choice== '2':
            find_supplier_by_name()
        elif choice== '3':
            find_supplier_by_id()
        elif choice == '4':
            create_supplier()
        elif choice== '5':
            update_supplier()
        elif choice== '6':
            delete_supplier()
        elif choice== '7':
            list_products()
        elif choice== '8':
            find_product_by_name()
        elif choice== '9':
            find_product_by_id()
        elif choice== '10':
            create_product()
        elif choice== '11':
            update_product()
        elif choice== '12':
            delete_product()
        elif choice== '13':
            list_supplier_products()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all suppliers")
    print("2. Find supplier by name")
    print("3. Find supplier by id")
    print("4. Create supplier")
    print("5. Update supplier")
    print("6. Delete supplier")
    print("7. List all products")
    print("8. Find product by name")
    print("9. Find product by id")
    print("10. Create product")
    print("11. Update product")
    print("12. Delete product")    
    print("13. List all products from a supplier")

if __name__ == "__main__":
    main()
