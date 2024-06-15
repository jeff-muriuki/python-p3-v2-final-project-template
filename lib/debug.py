#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.product import Product
from models.supplier import Supplier
import ipdb


def reset_database():    
    Product.create_table()
    Supplier.create_table()
    Product.drop_table()
    Supplier.drop_table()

reset_database()
ipdb.set_trace()
