from application import db , login_manager
from sqlalchemy.sql import func 
from flask_login import UserMixin


@login_manager.user_loader      
def load_user(user_id):
      return User.query.get(int(user_id))
     

class User(db.Model , UserMixin ):
        id = db.Column(db.Integer , primary_key = True)
        username = db.Column(db.String(20) , unique = True , nullable = False)
        email = db.Column(db.String(120) , unique = True , nullable = False)
        hostel_block = db.Column(db.String(100) , nullable=False)
        hostel_parts = db.Column(db.String(100) , nullable=False)
        hostel_room = db.Column(db.String(100) , nullable=False)
        password = db.Column(db.String(120) , nullable = False)
        createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
        facilities = db.relationship('Facilities' , backref = 'author' , lazy = True)
        integrity = db.relationship('Integrity' , backref = 'author' , lazy = True)
        shoutouts = db.relationship('Shoutouts' , backref = 'author' , lazy = True)
        chats = db.relationship('Chat', backref = 'author' ,lazy = True  )
        

        
        def _repr_(self):
           return f'User("{self.username}" , {self.email})'



class Facilities(db.Model , UserMixin):
       id = db.Column(db.Integer , primary_key = True)
       photo_evidence = db.Column(db.String() , default = 'None' ,  nullable = False )
       title = db.Column(db.String(1000) , default='None' , nullable = True)
       message = db.Column(db.String(1000) , default='None' , nullable = True)
       createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
       user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)


class Integrity(db.Model , UserMixin):
      id = db.Column(db.Integer , primary_key = True)
      photo_evidence = db.Column(db.String() , default = 'None' ,  nullable = False )
      title = db.Column(db.String(1000) , default='None' , nullable = True)
      message = db.Column(db.String(1000) , default='None' , nullable = True)
      createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
      user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

class Shoutouts(db.Model , UserMixin):
      id = db.Column(db.Integer , primary_key = True)
      photo_evidence = db.Column(db.String() , default = 'None' ,  nullable = False )
      title = db.Column(db.String(1000) , default='None' , nullable = True)
      message = db.Column(db.String(1000) , default='None' , nullable = True)
      createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
      user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)


class Chat(db.Model , UserMixin):
      id = db.Column(db.Integer , primary_key = True)
      message = db.Column(db.String() ,default = 'None' , nullable = True )
      createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
      user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = True)
      







        

