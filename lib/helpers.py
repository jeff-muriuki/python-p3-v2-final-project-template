# lib/helpers.py
from models.product import Product
from models.supplier import Supplier

def exit_program():
    print("Goodbye!")
    exit()

def list_suppliers():
    suppliers= Supplier.get_all()
    for supplier in suppliers:
        print(supplier)

def find_supplier_by_name():
    name= input("Enter the supplier's name: ")
    supplier= Supplier.find_by_name(name)
    print(supplier) if supplier else print(
        f"Supplier {name} not found"
    )

def find_supplier_by_id():
    id_=input("Enter the supplier's id: ")
    supplier= Supplier.find_by_id(id_)
    print(supplier) if supplier else print(
        f"supplier {id_} not found"
    )

def create_supplier():
    name= input("Enter the supplier's name: ")
    type= input("Enter the supplier's type: ")
    try: 
        supplier= Supplier.create(name, type)
        print(f"success: {supplier}")
    except Exception as exc:
        print('Error creating supplier: ', exc)

def update_supplier():
    id_= input("Enter the supplier's id: ")
    if supplier :=Supplier.find_by_id(id_):
        try:
            name= input("Enter the supplier's new name: ")
            supplier.name= name
            type= input("Enter the supplier's new type: ")
            supplier.type= type

            supplier.update()
            print(f"Success: {supplier}")
        except Exception as exc:
            print("Error updating supplier: ", exc)
    else:
        print(f"Supplier {id_} not found")

def delete_supplier():
    id_= input("Enter the supplier's id: ")
    if supplier := Supplier.find_by_id(id_):
        supplier.delete()
        print(f"Supplier {id_} deleted")
    else:
        print(f'Supplier {id_} not found')

#product functions

def list_products():
    products= Product.get_all()
    for product in products:
        print(product)

def find_product_by_name():
    name= input("Enter the product's name: ")
    product= Product.find_by_name(name)
    print (product) if product else print(f"Product {name} not found")

def find_product_by_id():
    id_= input("Enter the product's id: ")
    product= Product.find_by_id(id_)
    print(product) if product else print(f"Product {id_} not found")

def create_product():
    name = input("Enter the product's name: ")
    type = input("Enter the product's type: ")
    
    while True:
        quantity_str = input("Enter the product's quantity: ")
        if quantity_str.isdigit():
            quantity = int(quantity_str)
            break
        else:
            print("Quantity must be an integer. Please try again.")
    
    while True:
        supplier_id_str = input("Enter the product's supplier id: ")
        if supplier_id_str.isdigit():
            supplier_id= int(supplier_id_str)
            break
        else:
            print("supplier ID must be an integer")
    try:
        product = Product.create(name, type, quantity, supplier_id)
        print(f"Success: {product}")
    except Exception as exc:
        print('Error creating product: ', exc)

def update_product():
    id_ = input("Enter product's id: ")
    if product := Product.find_by_id(id_):
        try:
            name = input("Enter the product's new name: ")
            product.name = name

            type_ = input("Enter the product's new type: ")
            product.type = type_

            while True:
                quantity_str = input("Enter the product's new quantity: ")
                if quantity_str.isdigit():
                    quantity = int(quantity_str)
                    product.quantity = quantity
                    break
                else:
                    print("Quantity must be an integer. Please try again.")

            while True:
                supplier_id_str = input("Enter the product's supplier id: ")
                if supplier_id_str.isdigit():
                    supplier_id = int(supplier_id_str)
                    if Supplier.find_by_id(supplier_id): 
                        product.supplier_id = supplier_id
                        break
                    else:
                        print("Supplier ID must reference a supplier in the database. Please try again.")
                else:
                    print("Supplier ID must be an integer. Please try again.")

            product.update()
            print(f"Success: {product}")
        except Exception as exc:
            print('Error updating product:', exc)
    else:
        print(f"Product {id_} not found")

def delete_product():
    id_= input("Enter the product's id: ")
    if product := Product.find_by_id(id_):
        product.delete()
        print(f"Product {id_} deleted")
    else:
        print(f"Product {id_} not found")
    
def list_supplier_products():
    supplier_id_str = input("Enter the supplier's id: ")
    if not supplier_id_str.isdigit():
        print("Supplier ID must be an integer.")
        return
    
    supplier_id = int(supplier_id_str)
    supplier = Supplier.find_by_id(supplier_id)
    if not supplier:
        print(f"Supplier with ID {supplier_id} not found")
        return
    
    products = supplier.products()

    if not products:
        print(f"No products found for supplier '{supplier.name}'.")
    else:
        print(f"Products for supplier '{supplier.name}':")
        for prod in products:
            print(f"name: {prod.name} type: {prod.type}, Quantity: {prod.quantity}, product ID: {prod.id}")
1












