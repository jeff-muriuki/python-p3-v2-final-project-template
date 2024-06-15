# lib/models/product.py
from models.__init__ import CURSOR,CONN
from models.supplier import Supplier

class Product:
    all= {}

    def __init__(self, name, type, quantity, supplier_id, id= None):
        self.id= id
        self.name= name
        self.type= type
        self.quantity= quantity
        self.supplier_id= supplier_id

    def __repr__(self):
        return (
            f"<Product {self.id}: {self.name}, {self.type}, {self.quantity}, " +
            f"Supplier ID: {self.supplier_id}>"
        )
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name= name    
        else:
            raise ValueError("name nust be a non empty string")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if isinstance(type, str) and len(type):
            self._type= type
        else:
            raise ValueError("type must be a non empty string")

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        if type(quantity) is int:
            self._quantity= quantity
        else:
            raise ValueError('quantity must be an integer')
        
    @property
    def supplier_id(self):
        return self._supplier_id
    
    @supplier_id.setter
    def supplier_id(self, supplier_id):
        if type(supplier_id) is int and Supplier.find_by_id(supplier_id):
            self._supplier_id =supplier_id
        else:
            raise ValueError('Supplier ID must reference a supplier in the database')
            
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            quantity INTEGER,
            supplier_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql= """
            DROP TABLE IF EXISTS products;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
            INSERT INTO products (name, type,quantity, supplier_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type, self.quantity, self.supplier_id))
        CONN.commit()

        self.id= CURSOR.lastrowid
        type(self).all[self.id]= self

    @classmethod
    def create(cls, name, type, quantity, supplier_id):
        product= cls(name, type, quantity, supplier_id)
        product.save()
        return product
    
    def update(self):
        sql="""
            UPDATE products
            SET name= ?, type= ?, quantity= ?, supplier_id= ?
            WHERE id= ?
        """
        CURSOR.execute(sql, (self.name, self.type, self.quantity, self.supplier_id, self.id))
        CONN.commit()

    def delete(self):
        sql= """
            DELETE FROM products
            WHERE id= ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id= None

    @classmethod
    def instance_from_db(cls, row):
        product= cls.all.get(row[0])
        if product:
            product.name= row[1]
            product.type= row[2]
            product.quantity= row[3]
            product.supplier_id= row[4]
        else:
            product= cls(row[1], row[2], row[3], row[4])
            product.id= row[0]
            cls.all[product.id]= product
        return product
    
    @classmethod
    def get_all(cls):
        sql= """
            SELECT *
            FROM products
        """
        rows= CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql= """
            SELECT * 
            FROM products
            WHERE id= ?
        """
        row=CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql="""
            SELECT * 
            FROM products
            WHERE name = ?
        """
        row= CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    