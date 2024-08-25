from flask import render_template , flash , redirect , url_for , abort
from application import app , db , bcrypt
from application.form import LoginForm , RegistrationForm , FacilitiesForm , IntegrityForm , PromotionForm , ChatForm
from flask_login import current_user , login_user , logout_user , login_required
from application.models import User , Facilities , Integrity , Shoutouts , Chat
from werkzeug.utils import secure_filename
import uuid as uuid
import os


@app.route("/" , methods = ['POST' , 'GET'])
def index():

   


    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Successful!')
        user = User.query.filter_by(email = form.email.data , hostel_block = form.hostelblock.data , hostel_parts = form.hostelparts.data , hostel_room = form.hostelroom.data).first()
        if user and bcrypt.check_password_hash(user.password , form.password.data):
            login_user(user , remember = form.remember.data)
            return redirect(url_for('home'))
    return render_template("login.html" , form = form)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup" , methods = ['POST' , 'GET'])
def signup():

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data ,  hostel_block = form.hostelblock.data , hostel_parts = form.hostelparts.data , hostel_room = form.hostelroom.data , email = form.email.data , password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('index'))
    return render_template('signup.html' , form = form)


@app.route('/home')
@login_required

def home():
    return render_template('home.html')


@app.route('/facilitiesform' , methods = ['POST' , 'GET'])
@login_required

def facilitiesform():
    form = FacilitiesForm()
    if form.validate_on_submit():

      if form.photo_evidence.data:
        photo_evidence = form.photo_evidence.data
        photo_evidence_filename = secure_filename(photo_evidence.filename)
        photo_evidence_name = str(uuid.uuid1()) + '_' + photo_evidence_filename
        photo_evidence.save(os.path.join(app.config['UPLOADED_FOLDER'] , photo_evidence_name))

      else:

        photo_evidence_name = None


      facilities = Facilities(title = form.title.data , message = form.message.data ,  hostel_block = form.hostelblock.data , hostel_parts = form.hostelparts.data , hostel_room = form.hostelroom.data, photo_evidence = photo_evidence_name , author = current_user)
      db.session.add(facilities)    
      db.session.commit()       
      flash(f'Message is sent!')
      return redirect(url_for('facilitiesform'))

    return render_template('facilitiesform.html' , form = form)

@app.route('/mycomplaints')
@login_required
def mycomplaints():
    facilities = Facilities.query.all()
    return render_template('mycomplaints.html' , facilities = facilities)

@app.route('/integrityform')
@login_required
def integrityform():
    form = IntegrityForm()
    if form.validate_on_submit():

      if form.photo_evidence.data:
        photo_evidence = form.photo_evidence.data
        photo_evidence_filename = secure_filename(photo_evidence.filename)
        photo_evidence_name = str(uuid.uuid1()) + '_' + photo_evidence_filename
        photo_evidence.save(os.path.join(app.config['UPLOADED_FOLDER'] , photo_evidence_name))

      else:

        photo_evidence_name = None


      facilities = Facilities(title = form.title.data , message = form.message.data , photo_evidence = photo_evidence_name , author = current_user)
      db.session.add(facilities)    
      db.session.commit()       
      flash(f'Message is sent!')
      return redirect(url_for('integrityform'))

    return render_template('integrityform.html' , form = form)


@app.route('/promotions' , methods = ['POST' , 'GET'])
def promotionsform():
    form = PromotionForm()

    if form.validate_on_submit():


        if form.photo_evidence.data:
            photo_evidence = form.photo_evidence.data
            photo_evidence_filename = secure_filename(photo_evidence.filename)
            photo_evidence_name = str(uuid.uuid1()) + '_' + photo_evidence_filename
            photo_evidence.save(os.path.join(app.config['UPLOADED_FOLDER'] , photo_evidence_name))


        else:
            photo_evidence_name = None

        shoutouts = Shoutouts(title = form.title.data , message = form.message.data , photo_evidence = photo_evidence_name , author = current_user )
        db.session.add(shoutouts)
        db.session.commit()
        return redirect(url_for('home'))


    return render_template('promotions.html' , form = form)


@app.route('/profilepage')

def profilepage():
    return render_template("profile.html")


@app.route('/announcements')
def announcements():
    announcements = Shoutouts.query.all()
    return render_template("announcements.html" , announcements = announcements)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/chat' , methods = ['POST' , 'GET'])
def chat():
   form = ChatForm()

   if form.validate_on_submit():
      chats = Chat(message = form.message.data , author = current_user)
      db.session.add(chats)
      db.session.commit()
      return redirect(url_for('chat'))
   

   return render_template('chat.html' , form = form)



    





