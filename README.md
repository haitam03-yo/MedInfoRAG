# **Med Info RAG**

This is a project for a Retrieval-Augmented Generation (RAG) system designed to answer questions related to medications. It will later be integrated into a larger mobile application project.

---

## **Requirements**

* Python 3.12 or later
* MiniConda for environment management

---

## **Setup Instructions**

### **1. Install MiniConda**

* Download and install MiniConda from [Miniconda Downloads](https://docs.anaconda.com/miniconda/install/).
* Choose the installer that matches your operating system (Windows, macOS, or Linux).

### **2. Create a Python Environment**

* Open your terminal or command prompt and run the following command to create a new environment:

  ```bash
  conda create -n mini-rag-app python=3.12
  ```

### **3. Activate the Environment**

* Activate your newly created environment:

  ```bash
  conda activate mini-rag-app
  ```

## Installation

### Install the Required Packages

```bash
pip install -r requirements.txt
```

### Setup the Environment Variables

```
cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastApi Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/med-info-rag.postman_collection.json](/assets/med-info-rag.postman_collection.json)
