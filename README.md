# 🚀 End-to-End MLOps Pipeline (Production-Level)

A complete, production-ready Machine Learning pipeline covering the full lifecycle — from data ingestion to deployment and monitoring — built using modern MLOps best practices.

---

## 📌 Project Overview

This project demonstrates how to build, track, deploy, and automate a machine learning system in a real-world production environment.

The pipeline includes:

* Data ingestion & preprocessing
* Model training & evaluation
* Experiment tracking with MLflow
* Model packaging & deployment using Docker
* REST API serving with Flask
* CI/CD automation using GitHub Actions
* Deployment on AWS EC2

---

## 🏗️ Architecture

```
Data → Ingestion → Preprocessing → Training → MLflow Tracking
      → Model Saving → Docker → Flask API → AWS EC2 Deployment
      → CI/CD Automation → Monitoring
```

---

## 🛠️ Tools & Technologies

### 👨‍💻 Programming & ML

* Python
* Scikit-learn
* Pandas, NumPy

### ⚙️ MLOps & Experiment Tracking

* MLflow (experiment tracking, model versioning)

### 🌐 Backend / API

* Flask (REST API for inference)

### 🐳 Containerization

* Docker

### 🔁 CI/CD

* GitHub Actions

### ☁️ Cloud Deployment

* AWS EC2

### 📦 Model Storage

* Joblib

---

## 📁 Project Structure

```
mlops-end-to-end/
│
├── data/                  # Raw dataset
├── src/                   # Training pipeline
├── app/                   # Flask API
├── models/                # Saved models
├── .github/workflows/     # CI/CD pipeline
├── Dockerfile             # Container setup
├── requirements.txt       # Dependencies
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/mlops-end-to-end.git
cd mlops-end-to-end
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train the Model

```bash
python src/train.py
```

This will:

* Train the model
* Log experiments in MLflow
* Save model in `models/`

---

### 5️⃣ Run MLflow UI (Optional)

```bash
mlflow ui
```

Open in browser:

```
http://localhost:5000
```

---

### 6️⃣ Start the Flask API

```bash
python app/app.py
```

API will run at:

```
http://localhost:5000
```

---

### 7️⃣ Test the API

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"input": [1,2,3,4]}'
```

---

## 🐳 Run Using Docker

### Build Image

```bash
docker build -t mlops-project .
```

### Run Container

```bash
docker run -p 5000:5000 mlops-project
```

---

## ☁️ AWS EC2 Deployment

1. Launch EC2 instance
2. Install Docker
3. Upload project or pull from GitHub
4. Run:

```bash
docker build -t mlops-project .
docker run -d -p 5000:5000 mlops-project
```

---

## 🔁 CI/CD Pipeline

The GitHub Actions workflow automates:

* Dependency installation
* Model training
* Docker image build
* (Optional) Deployment

Triggered on every push to the `main` branch.

---

## 📊 MLflow Tracking

Tracks:

* Parameters
* Metrics
* Model versions

Run locally using:

```bash
mlflow ui
```

---

## 🚀 Key Features

* End-to-end ML lifecycle automation
* Production-ready deployment
* Scalable containerized architecture
* Experiment tracking & reproducibility
* Automated CI/CD pipeline

---

## 📈 Future Enhancements

* Model monitoring (Prometheus + Grafana)
* Data drift detection (Evidently AI)
* Kubernetes deployment
* Feature store integration
* FastAPI for high-performance serving

---

## 👨‍💻 Author

**Alan Paul**
