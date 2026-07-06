# 🛒 E-Commerce Product Recommendation System

A Machine Learning-based Product Recommendation System that suggests similar products based on **Category**, **Brand**, and **Product Description** using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 📌 Project Overview

Finding similar products from thousands of available products on an e-commerce platform can be difficult for customers. This project recommends the Top 5 similar products based on product information, helping users discover relevant products quickly.

---

## ✨ Features

- Product Search
- Top 5 Product Recommendations
- Product Details
- Category Filter
- Price Filter
- Error Handling
- Interactive Streamlit Dashboard

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## 📊 Dataset

The dataset contains **500 products** with the following fields:

- Product ID
- Product Name
- Category
- Brand
- Price
- Rating
- Description

---

## 📈 Exploratory Data Analysis

The following visualizations were created:

- Number of Products by Category
- Product Distribution by Brand
- Product Price Distribution (Histogram)

---

## ⚙ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. TF-IDF Vectorization
6. Cosine Similarity Calculation
7. Product Recommendation
8. Streamlit Deployment

---

## 🧠 Feature Engineering

A new column named **Features** was created by combining

- Category
- Brand
- Description

This combined text was used for similarity calculation.

---

## 🤖 Recommendation Algorithm

The recommendation system uses

- TF-IDF Vectorizer
- Cosine Similarity

to recommend the Top 5 most similar products.

---

## 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/E-Commerce-Product-Recommendation-System.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

Example:

- Home Page
- Search Product
- Recommendation Results
- Filters
- Product Details

---

## 📌 Future Improvements

- User Login
- Personalized Recommendations
- Collaborative Filtering
- Deep Learning Recommendations
- Real-Time Product Database
- Product Images
- Customer Reviews

---

## 👨‍💻 Author

**Vishal Vishwas Desai**

- Python
- Machine Learning
- Data Analytics
- Power BI
- SQL
