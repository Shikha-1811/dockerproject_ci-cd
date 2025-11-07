# Docker CI/CD Project using Jenkins

This project demonstrates how to build and deploy a simple **Flask web application** using **Docker** and **Jenkins CI/CD pipeline**.  
It showcases the automation workflow from code to container deployment.

---

## 🚀 Project Overview

The application is a lightweight Python Flask app exposing two endpoints:
- `/info` → Returns basic information message.
- `/phone` → Returns a sample phone number.

### 🔧 Tech Stack
- **Python (Flask Framework)**
- **Docker (Containerization)**
- **Jenkins (CI/CD Automation)**
- **GitHub (Version Control)**
- **Vagrant / EuroLinux Box (Virtual Environment)**

---

## 🐳 Docker Setup

**Dockerfile**
```dockerfile
FROM redhat/ubi8
RUN yum install python3 -y
RUN pip3 install flask
COPY app.py /app.py
CMD ["python3", "/app.py"]

### 🧠 Build & Run the Container
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app

Access the app at → http://localhost:5000/info

🔁 Jenkins CI/CD Setup

This project uses a Freestyle Jenkins Pipeline to automate:

Source Code Integration: Pulls code from GitHub repository.

Build Stage: Builds Docker image from Dockerfile.

Test Stage: Runs test cases using pytest for validation.

Deployment Stage: Runs the container automatically on the server.

Jenkins Configuration Steps:

Create a new Freestyle project.

Connect with GitHub repository using credentials.

Add build steps:

Execute shell command to build Docker image:

docker build -t flask-app .


Run test file:

pytest test_app.py


Deploy container:

docker run -d -p 5000:5000 flask-app

🧩 Folder Structure
myapp/
│
├── app.py          # Flask Application
├── Dockerfile      # Containerization Instructions
├── test_app.py     # Unit Test File
└── README.md       # Project Documentation

🎯 Output

Application running in a Docker container

Jenkins automating the entire CI/CD flow

Flask app accessible on browser at port 5000

💬 Author

👩‍💻 Shikha Pal
Passionate about DevOps, Cloud, and Automation 🚀
GitHub Profile
