from flask import Flask, render_template, redirect, url_for, flash, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from keras.models import load_model
import cv2
import numpy as np
from flask import jsonify

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/violation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    uploads = db.relationship('Upload', backref='user', lazy=True)
    

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(280))
    video_path = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(50))
    ratings = db.Column(db.Integer, default=0)
    action = db.Column(db.String(50), default='Unblock')

class Admin(db.Model):
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

model = load_model('model.h5')
activities = ['Ak47', 'Gun', 'Knife', 'Sickle', 'Sword']

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists.', 'danger')
            return redirect(url_for('signup'))
        
        new_user = User(
            username=username,
            email=email,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and (user.password, password):
            upload = Upload.query.filter_by(user_id=user.id).first()
            if upload and upload.action == 'Block':
                flash('Your account has been blocked. Please contact the administrator.', 'danger')
            else:
                login_user(user)
                flash('Successfully logged in!!!', 'success')
                return redirect(url_for('usermenu'))
        else:
            flash('Invalid Username or Password', 'danger')

    return render_template('login.html')



@app.route("/admin", methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            flash('Admin login successful!', 'success')
            return render_template("admin_menu.html")
        else:
            flash('Invalid username or password', 'danger')
            return render_template("admin.html")
    return render_template("admin.html")

@app.route("/admin_menu", methods=['POST', 'GET'])
def admin_menu():
    return render_template("admin_menu.html")

@app.route('/usermenu', methods=['GET', 'POST'])
@login_required
def usermenu():
    return render_template('usermenu.html')



@app.route("/udetails", methods=['GET'])
def udetails():
    uploads = Upload.query.all()
    return render_template("udetails.html", uploads=uploads)

@app.route("/userview", methods=['GET'])
def userview():
    uploads = Upload.query.all()
    return render_template("userview.html", uploads=uploads)

def predict_violence(video_path):
    global model  

    # Load the video
    video_stream = cv2.VideoCapture(video_path)
    frame_count = int(video_stream.get(cv2.CAP_PROP_FRAME_COUNT))

    predicted_activities = set()

    for _ in range(frame_count):
        ret, frame = video_stream.read()
        if not ret:
            break

        
        resized_frame = cv2.resize(frame, (64, 64))
        normalized_frame = resized_frame / 255.0

    
        input_frame = np.expand_dims(normalized_frame, axis=0)

   
        pred = model.predict(input_frame)
        pred_label = np.argmax(pred)
        activity = activities[pred_label]

        # Add the predicted activity to the set
        predicted_activities.add(activity)

    confidence_threshold = 0.9  
    if np.max(pred) > confidence_threshold:
        status = 'Violent'
    else:
        status = 'Non-violent'


    video_stream.release()

    return status
@app.route('/delete_video/<int:upload_id>', methods=['GET'])
@login_required
def delete_video(upload_id):
    
    upload = Upload.query.get(upload_id)

    if upload:
        
        db.session.delete(upload)
        db.session.commit()
        flash('Video deleted successfully!', 'success')
    else:
        flash('Video not found.', 'danger')

    return redirect(url_for('udetails'))



@app.route('/rate_video/<int:upload_id>', methods=['POST'])
@login_required
def rate_video(upload_id):
    selected_rating = request.json.get('rating')
    print(f"Selected Rating: {selected_rating}")

    if selected_rating is not None:
        try:
            rating = int(selected_rating)
            
         
            rating = max(0, min(5, rating))

 
            upload = Upload.query.get(upload_id)

   
            upload.ratings = rating

            db.session.commit()

            return jsonify({'success': True})
        except ValueError as e:
            print(f"Error converting to int: {e}")
    else:
        print("Rating is None")

    return jsonify({'success': False, 'error': 'Invalid rating'})



@app.route('/userupload', methods=['GET', 'POST'])
@login_required
def userupload():
    if request.method == 'POST':
        tweet_content = request.form.get('tweet')

        if 'video' not in request.files:
            flash('No video file part', 'error')
            return redirect(request.url)

        video = request.files['video']

        if video.filename == '':
            flash('No selected video file', 'error')
            return redirect(request.url)

        if video:
            filename = secure_filename(video.filename)
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            video.save(video_path)
            video_path = video_path.replace('\\', '/')

           
            user = User.query.get(current_user.id)

            status = predict_violence(video_path)
            new_upload = Upload(tweet=tweet_content, video_path=video_path, user=user, status=status)

            db.session.add(new_upload)
            db.session.commit()

            flash('Tweet and video uploaded successfully!', 'success')
            return redirect(url_for('usermenu'))

    return render_template('upload.html')




@app.route('/block_video/<int:upload_id>', methods=['GET'])
@login_required
def block_video(upload_id):

    upload = Upload.query.get(upload_id)


    upload.action = 'Block'
    db.session.commit()

    flash('Video blocked successfully!', 'success')
    return redirect(url_for('udetails'))

@app.route('/unblock_video/<int:upload_id>', methods=['GET'])
@login_required
def unblock_video(upload_id):
 
    upload = Upload.query.get(upload_id)


    upload.action = 'Unblock'
    db.session.commit()

    flash('Video unblocked successfully!', 'success')
    return redirect(url_for('udetails'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
