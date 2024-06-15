#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.supplier import Supplier
from models.product import Product

    
def seed_database():
    Product.drop_table()       
    Supplier.drop_table()
    Supplier.create_table()
    Product.create_table()

    copia= Supplier.create("Copia", "Distributor")
    bidco= Supplier.create("BIDCO", "Manufacturer")
    stima= Supplier.create('KPLC', 'Manufuacturer')
    Product.create('printing papers', 'stationery', 5, copia.id)
    Product.create('fresh fri', "oil", 2, bidco.id)
    Product.create('nails', 'building material', 200, copia.id)
    Product.create('menengai', 'soap', 10, bidco.id)
    Product.create('ushindi', 'soap', 7, bidco.id)
    Product.create('Electric poles', 'wood', 1000, stima.id)

seed_database()
print('Seeded database')
