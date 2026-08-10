# 🛡️ Social Media Network Filtering Using ML

<p align="center">
  <img src="static/img/bg.jpg" alt="Social Media Network Filtering" width="700">
</p>

<h3 align="center">
  🤖 AI-Powered Video Content Filtering & Moderation System
</h3>

<p align="center">
  A Flask-based machine learning application for detecting potentially harmful visual content in uploaded videos.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/TensorFlow-2.21-orange?logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/Keras-3.15-red?logo=keras&logoColor=white">
  <img src="https://img.shields.io/badge/OpenCV-5.0-green?logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-3.1-black?logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/MySQL-Database-blue?logo=mysql&logoColor=white">
</p>

---

## 🌟 Overview

**Social Media Network Filtering Using ML** is a machine-learning-powered web application developed to identify potentially harmful or inappropriate visual content in uploaded videos.

🎥 The system extracts frames from uploaded videos and analyzes them using a trained **Convolutional Neural Network (CNN)** model.

When potentially harmful content is detected, the result can be reviewed through the **administrator interface**.

### 🎯 Main Goals

* 🔍 Detect potentially harmful visual content
* 🎥 Analyze uploaded videos frame-by-frame
* 🧠 Use deep learning for content classification
* 👤 Provide user registration and authentication
* 👨‍💼 Provide an administrator review system
* ⭐ Support content rating/review
* 🗄️ Store application information in MySQL

---

# 🧠 Machine Learning

The application uses a trained **CNN image-classification model**.

### 🏷️ Supported Classes

The current model contains **8 classes**:

| #     | Class     | Category       |
| ----- | --------- | -------------- |
| 🔫 1  | `AK47`    | Weapon         |
| 🐕 2  | `Animal`  | General        |
| 🔫 3  | `Gun`     | Weapon         |
| ⚠️ 4  | `Guntime` | Weapon-related |
| 🔪 5  | `Knife`   | Weapon         |
| 🎬 6  | `Salaar`  | Movie/Action   |
| ⚔️ 7  | `Sickle`  | Weapon         |
| 🗡️ 8 | `Sword`   | Weapon         |

The trained model is:

```text
model_8class.h5
```

---

# 🔄 How It Works

```text
             👤 USER
                │
                ▼
        📤 Upload Video
                │
                ▼
        🎥 Video Processing
                │
                ▼
       🖼️ Extract Video Frames
                │
                ▼
       🔬 OpenCV Processing
                │
                ▼
       🧠 CNN ML Model
        model_8class.h5
                │
                ▼
        🔍 Class Prediction
                │
                ▼
       📊 Content Evaluation
                │
                ▼
        👨‍💼 Admin Review
                │
                ▼
        ✅ / ❌ Final Action
```

---

# ✨ Key Features

### 👤 User Management

* 📝 User registration
* 🔐 Secure login
* 🚪 Logout
* 👤 User authentication
* 📋 User details management

### 🎥 Video Filtering

* 📤 Upload videos
* 🖼️ Extract frames using OpenCV
* 🧠 CNN-based classification
* 🔍 Detect trained content categories
* 📊 Display prediction results

### 👨‍💼 Admin Panel

* 🔐 Administrator login
* 👥 Manage/view users
* 🎥 Review uploaded videos
* 🔍 Review detected content
* ⭐ Review ratings
* 🗑️ Manage inappropriate content

### 🗄️ Database

The application uses:

* 🐬 MySQL
* 🔗 Flask-SQLAlchemy
* ⚡ PyMySQL
* 🛠️ SQLAlchemy

---

# 🛠️ Technology Stack

| Technology              | Purpose                      |
| ----------------------- | ---------------------------- |
| 🐍 **Python 3.12**      | Application & ML development |
| 🌐 **Flask**            | Web application              |
| 🧠 **TensorFlow**       | Deep learning                |
| 🤖 **Keras**            | CNN model                    |
| 👁️ **OpenCV**          | Video/frame processing       |
| 🔢 **NumPy**            | Numerical processing         |
| 🐬 **MySQL**            | Database                     |
| 🔗 **Flask-SQLAlchemy** | Database integration         |
| 🔐 **Flask-Login**      | Authentication               |
| 🔑 **Werkzeug**         | Password hashing             |
| 📓 **Jupyter Notebook** | Model development            |
| 🌿 **Git**              | Version control              |
| 🐙 **GitHub**           | Repository hosting           |

---

# 📁 Project Structure

```text
📦 SMN-Filtering-Using-ML-Model
│
├── 📂 algo code/
│   ├── 📓 Resnet vgg16.ipynb
│   └── 📓 train.ipynb
│
├── 📂 static/
│   ├── 📂 css/
│   │   └── 🎨 style.css
│   │
│   └── 📂 img/
│       └── 🖼️ bg.jpg
│
├── 📂 templates/
│   ├── 👨‍💼 admin.html
│   ├── 👨‍💼 admin_menu.html
│   ├── 🏠 index.html
│   ├── 🔐 login.html
│   ├── 📝 signup.html
│   ├── 👤 udetails.html
│   ├── 📤 upload.html
│   ├── 👤 usermenu.html
│   └── 👀 userview.html
│
├── 🐍 app.py
├── 🗄️ db.sql
├── 🧠 model_8class.h5
├── 📦 requirements.txt
├── 📓 train.ipynb
├── 🐍 train_fixed.py
├── 📓 Resnet vgg16.ipynb
├── 📄 how to run steps.txt
├── ⚖️ LICENSE
└── 🚫 .gitignore
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Suryadev03/SMN-Filtering-Using-ML-Model.git
```

Then:

```bash
cd SMN-Filtering-Using-ML-Model
```

---

## 2️⃣ Create Virtual Environment

This project is tested with **Python 3.12**.

Create the environment:

```bash
python -m venv tf
```

Activate it on Windows:

```cmd
tf\Scripts\activate
```

You should see:

```text
(tf)
```

in your terminal.

---

## 3️⃣ Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

### 📦 Main Dependencies

```text
Flask
Flask-Login
Flask-SQLAlchemy
Werkzeug
PyMySQL
TensorFlow
Keras
OpenCV
NumPy
```

---

# 🗄️ Database Setup

The project uses **MySQL**.

### 🐬 Create Database

Open MySQL and execute:

```sql
CREATE DATABASE violation;
```

Then import:

```text
db.sql
```

into the `violation` database.

### 🔗 Database Configuration

The application uses the following local configuration:

```python
mysql+pymysql://root:root@localhost/violation
```

Therefore, the expected local setup is:

```text
🖥️ Host     : localhost
👤 Username : root
🔑 Password : root
🗄️ Database : violation
```

> ⚠️ **Security:** For production deployment, never hard-code database credentials. Use environment variables or a secrets manager.

---

# ▶️ Run the Application

Activate the environment:

```cmd
tf\Scripts\activate
```

Navigate to the project directory:

```cmd
cd "D:\Projects\Social Media Network Filtering Using ML\final video"
```

Start Flask:

```cmd
python app.py
```

The application will run at:

```text
🌐 http://127.0.0.1:5000
```

Open the URL in your browser.

---

# 🧪 Testing

You can test the application by uploading videos containing visual content related to the trained classes.

### Example Test Categories

```text
🔫 AK47
🔫 Gun
⚠️ Guntime
🔪 Knife
🗡️ Sword
⚔️ Sickle
🐕 Animal
🎬 Salaar
```

The model analyzes video frames and generates predictions based on the visual patterns learned during training.

---

# 📓 Model Training

The repository includes training resources for the machine-learning model.

### 🧪 `train.ipynb`

Contains the CNN model training workflow.

### 🐍 `train_fixed.py`

Python training implementation used for generating the current model.

### 🧠 `Resnet vgg16.ipynb`

Contains experiments involving ResNet/VGG16 approaches.

### 💾 Trained Model

```text
model_8class.h5
```

The Flask application loads this model for video classification.

---

# 🎯 Application Architecture

```text
                    🌐 WEB APPLICATION
                           │
              ┌────────────┴────────────┐
              │                         │
           👤 USER                   👨‍💼 ADMIN
              │                         │
              ▼                         ▼
       📤 Upload Video            📊 Review Content
              │                         │
              ▼                         │
       🎥 Frame Extraction             │
              │                         │
              ▼                         │
       🧠 CNN Prediction ───────────────┘
              │
              ▼
       📊 Classification
              │
              ▼
       🗄️ MySQL Database
```

---

# ⚠️ Model Limitations

This project is primarily intended for **academic, educational, and demonstration purposes**.

The model can only recognize patterns represented in its training dataset.

Predictions may be affected by:

* 📉 Low-quality videos
* 🌫️ Blurry frames
* 💡 Poor lighting
* 📐 Different camera angles
* 🖼️ Partially visible objects
* 👥 Multiple objects in a frame
* 🧩 Unseen content
* 🎞️ Complex scenes

Therefore, predictions should be considered **AI-assisted classification**, not an absolute moderation decision.

---

# 🔐 Security Considerations

Before deploying this application publicly, consider implementing:

* 🔑 Environment-based database credentials
* 🛡️ CSRF protection
* 📦 File-size restrictions
* 📁 Secure file upload validation
* 🔐 Strong authentication
* 👮 Role-based authorization
* 🚫 Disable Flask debug mode
* 📝 Application logging
* 🔍 Security monitoring
* ☁️ Secure production deployment

---

# 🚀 Future Enhancements

The project can be extended with:

* 🤖 YOLO-based object detection
* 🎞️ Advanced video action recognition
* 🧠 CNN-LSTM video classification
* 🔊 Audio analysis
* 🗣️ Speech recognition
* 💬 NLP-based text moderation
* 📊 AI confidence scores
* ⭐ Automated content risk scoring
* 📧 Admin email notifications
* 🔔 Real-time moderation alerts
* 📱 Responsive mobile interface
* ☁️ Cloud deployment
* 📈 Admin analytics dashboard
* 🔄 Continuous model improvement
* 🎯 Improved dataset balancing

---

# 🧭 Future AI Moderation Pipeline

```text
                         🎥 VIDEO
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        🖼️ Visual        🔊 Audio        📝 Text
         Analysis        Analysis       Analysis
             │              │              │
             ▼              ▼              ▼
          🧠 CNN          🤖 AI/NLP       💬 NLP
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                    📊 RISK SCORING
                            │
                            ▼
                     👨‍💼 ADMIN REVIEW
                            │
                     ┌──────┴──────┐
                     ▼             ▼
                  ✅ Allow      ❌ Remove
```

---

# 📊 Project Highlights

| Feature                     |         Status        |
| --------------------------- | :-------------------: |
| 🌐 Flask Web Application    |           ✅           |
| 👤 User Authentication      |           ✅           |
| 👨‍💼 Admin Panel           |           ✅           |
| 🎥 Video Upload             |           ✅           |
| 🖼️ Frame Extraction        |           ✅           |
| 🧠 CNN Classification       |           ✅           |
| 🗄️ MySQL Integration       |           ✅           |
| 🔐 Password Hashing         |           ✅           |
| 📓 Model Training Notebooks |           ✅           |
| 🚀 Production Deployment    | 🔄 Future Enhancement |

---

# 👨‍💻 Author

### **Surya**

🐙 GitHub:
**https://github.com/Suryadev03**

---

# ⭐ Repository

If this project helped you understand **Machine Learning + Computer Vision + Flask**, consider giving it a ⭐!

🐙 **GitHub Repository:**

https://github.com/Suryadev03/SMN-Filtering-Using-ML-Model

---

## 📜 License

This project is available under the license included in the `LICENSE` file.

---

<p align="center">
  🚀 <b>Social Media Network Filtering Using ML</b>
  <br>
  🤖 Machine Learning • 🎥 Computer Vision • 🌐 Flask • 🗄️ MySQL
  <br><br>
  ⭐ <b>Built for learning, experimentation, and academic demonstration.</b>
</p>
