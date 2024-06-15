# lib/models/supplier.py
from models.__init__ import CURSOR, CONN

class Supplier:
    all= {}

    def __init__(self, name, type, id=None):
        self.id= id
        self.name= name
        self.type= type 

    def __repr__(self):
        return f"<Supplier {self.id}: {self.name}, {self.type}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name= name
        else:
            raise ValueError("Name must be a non empty sting")

    @property  
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str) and len(type):
            self._type = type
        else:
            raise ValueError('Type must be a non empty string')
        
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS suppliers(
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql= """
            DROP TABLE IF EXISTS suppliers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
            INSERT INTO suppliers (name, type)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type))
        CONN.commit()

        self.id= CURSOR.lastrowid
        type(self).all[self.id]= self

    @classmethod
    def create(cls, name, type):
        supplier= cls(name, type)
        supplier.save()
        return supplier
    
    def update(self):
        sql="""
            UPDATE suppliers
            SET name= ?, type= ?
            WHERE id= ?
        """
        CURSOR.execute(sql, (self.name, self.type, self.id))
        CONN.commit()

    def delete(self):
        sql= """
            DELETE FROM suppliers
            WHERE id= ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id= None

    @classmethod
    def instance_from_db(cls, row):
        supplier= cls.all.get(row[0])
        if supplier:
            supplier.name= row[1]
            supplier.type= row[2]
        else:
            supplier= cls(row[1], row[2])
            supplier.id= row[0]
            cls.all[supplier.id]= supplier
        return supplier
    
    @classmethod
    def get_all(cls):
        sql= """
            SELECT *
            FROM suppliers
        """
        rows= CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql= """
            SELECT * 
            FROM suppliers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql="""
            SELECT * 
            FROM suppliers
            WHERE name = ?
        """
        row= CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def products(self):
        from models.product import Product
        sql= """
            SELECT * FROM products
            WHERE supplier_id= ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows= CURSOR.fetchall()
        return [Product.instance_from_db(row) for row in rows]