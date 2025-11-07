# 🚀 Flask App CI/CD Pipeline with Jenkins, Docker & GitHub Integration

This project demonstrates a complete **CI/CD pipeline** for a Flask-based web application using **Jenkins**, **Docker**, and **GitHub**.  
The pipeline is fully automated — from code changes on GitHub to Docker image build, test, and push to DockerHub.

---

## 🧩 Tech Stack

- **Frontend / Backend:** Python (Flask)
- **Version Control:** Git & GitHub
- **CI/CD Tool:** Jenkins
- **Containerization:** Docker
- **Image Registry:** DockerHub
- **Testing:** pytest

---

## 📁 Project Structure
```
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build configuration
├── test_app.py # Unit tests for Flask app
└── README.md # Documentation


## ⚙️ **Prerequisites**

Before setting up the pipeline, ensure the following are **installed and configured**:

* **Git** (for version control)
* **Python 3.x** (to run Flask app)
* **Docker** (for containerization)
* **Jenkins** (for CI/CD automation)
* **DockerHub Account** (to push Docker images)
* **GitHub Repository** (for source code management)

## 🧠 Build & Run the Container (Locally)

If you want to test the application locally before automating via Jenkins:

```bash
# Clone the project
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Build Docker image
docker build -t flask-app .

# Run the container
docker run -d -p 5000:5000 flask-app

Once the container runs, visit 👉 http://localhost:5000
 to see your Flask app running.

## 🧪 Run Tests

Run unit tests inside the container to ensure your application is functioning correctly.

```bash
# Run tests
pytest test_app.py

If all tests pass ✅, Jenkins will automatically proceed to the next stage (image push).

☁️ Push Image to DockerHub (Automated via Jenkins)

The Docker image push process is completely automated in Jenkins — no manual steps required.

🔒 Jenkins handles:

Logging into DockerHub using stored credentials

Tagging the built image with your DockerHub repository name

Pushing the image to DockerHub

Example (runs inside Jenkins shell step)
# Build image
docker build -t flask-app .

# Login securely using Jenkins credentials
echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

# Tag & push image
docker tag flask-app $DOCKERHUB_USERNAME/flask-app:latest
docker push $DOCKERHUB_USERNAME/flask-app:latest


## 🧠 Jenkins credentials are stored securely under:
Manage Jenkins → Credentials → Global → Add Credentials

Never hardcode credentials in your script or Jenkinsfile.

## 🔁 Jenkins CI/CD Setup

This project uses a Freestyle Jenkins job integrated with GitHub and DockerHub.
The pipeline is configured to run automatically whenever you push changes to GitHub.

## 🧩 Pipeline Workflow

Trigger: Code pushed to GitHub → Jenkins job automatically starts

Checkout: Jenkins pulls the latest code

Build: Jenkins runs docker build to create the Docker image

Test: Jenkins executes pytest test_app.py to validate the app

Push: Jenkins logs in to DockerHub and pushes the new image

Deploy: Jenkins can optionally deploy or run the new container

## ⚡ Jenkins Configuration Steps
### 1️⃣ Install Required Plugins

Git Plugin

Docker Plugin

Docker Pipeline Plugin

Credentials Binding Plugin

### 2️⃣ Configure Jenkins Credentials

Add your DockerHub credentials in Jenkins:

Go to: Manage Jenkins → Credentials → Add Credentials

Type: Username and Password

ID Example: dockerhub_credentials

### 3️⃣ Create Jenkins Job

Choose Freestyle Project

Under Source Code Management, select Git → Add your repository URL

Under Build Triggers, select:

✅ GitHub hook trigger for GITScm polling

or ✅ Poll SCM (H/5 * * * *) for every 5 minutes

### 4️⃣ Add Build Steps

Add the following Shell Command inside Jenkins:

# Build Docker image
docker build -t flask-app .

# Run tests
pytest test_app.py

# Login & Push Image
echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
docker tag flask-app $DOCKERHUB_USERNAME/flask-app:latest
docker push $DOCKERHUB_USERNAME/flask-app:latest

# Optional: Deploy the container
docker run -d -p 5000:5000 $DOCKERHUB_USERNAME/flask-app:latest

## 🔄 Automated Trigger on GitHub Changes

Jenkins automatically starts the pipeline whenever there’s a new commit or PR in GitHub.

## 🧠 Methods:

Poll SCM :

In Jenkins → Build Triggers → Enable Poll SCM

Schedule example: * * * * * (checks every  minute)

## 📦 DockerHub Output

After a successful Jenkins build, your image is pushed automatically to your DockerHub repository.

Example:

Successfully built abc123
Successfully tagged shikhapal/flask-app:latest
The push refers to repository [docker.io/shikhapal/flask-app]
latest: digest: sha256:... size: 1783


### ✅ You can verify this on DockerHub
 under your repositories.

## 🎯 Summary
Step	Description	Automated?
Code Push	Push code to GitHub	✅
Build	Jenkins builds Docker image	✅
Test	Run unit tests	✅
Push to DockerHub	Jenkins pushes image	✅
Deploy	Jenkins runs container	✅ (optional)
🌟 Outcome

This setup ensures:

Continuous Integration and Continuous Deployment

Secure Credential Handling

Automated Trigger on Code Changes

Fully Dockerized and Reproducible Builds

## ✨ Author

👩‍💻 Shikha Pal
💬 Cloud & DevOps Enthusiast
🔗 
 | GitHub
