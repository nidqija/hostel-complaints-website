from application import db 
from sqlalchemy.sql import func 
from flask_login import UserMixin



      

class User(db.Model , UserMixin ):
        id = db.Column(db.Integer , primary_key = True)
        username = db.Column(db.String(20) , unique = True , nullable = False)
        mmu_id = db.Column(db.String(150) , unique = True , nullable = True)
        email = db.Column(db.String(120) , unique = True , nullable = False)
        password = db.Column(db.String(120) , nullable = False)
        createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
       

        
        def _repr_(self):
           return f'User("{self.username}" , {self.email} , {self.mmu_id})'
        

