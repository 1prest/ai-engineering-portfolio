# 🚀 Project 6: AI Model Deployment with FastAPI

**Live API:** [https://ai-engineering-portfolio-2.onrender.com](https://ai-engineering-portfolio-2.onrender.com)

---

## 🧠 Overview

This project demonstrates how to deploy a machine learning model as a REST API using **FastAPI**.  
The API can receive input data, process it, and return predictions in real time.

---

## 🔧 Architecture & Tech Stack

- **FastAPI** — web framework for building APIs  
- **Uvicorn** — ASGI server for running FastAPI  
- **Pickle** — for model serialization  
- **scikit-learn** — example ML model  
- **Python 3.11** — runtime on Render  

---

## 📦 Files & Structure

06-ai-api-deployment/
├── api.py # FastAPI application
├── model/
│ └── model.pkl # Serialized ML model
├── train_model.py # Script to train/save model
├── requirements.txt # Project dependencies
└── runtime.txt # Specifies Python version for Render


---

## 🔍 How to Use the API

### 1. Home Endpoint  
- **URL:** `/`  
- **Method:** GET  
- **Returns:**  
  ```json
  { "message": "API is working!" }
