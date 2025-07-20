# 🛒 FastAPI E-Commerce Backend

This is a sample E-Commerce backend built with **FastAPI** and **MongoDB** using the async `motor` driver.

---

## 📦 Features

- Create & list products with size/price
- Place orders containing multiple products
- Fetch orders by user ID with product details and total amount
- MongoDB Atlas cloud integration
- Async endpoints for performance

---

## 🧪 Tech Stack

- **FastAPI** for API
- **MongoDB Atlas** (cloud) as the database
- **Motor** async driver for MongoDB
- **Pydantic** for schema validation

---

## 🧾 MongoDB Setup

We're using **MongoDB Atlas** (cloud).

1. Create a free cluster at [https://www.mongodb.com/cloud](https://www.mongodb.com/cloud)
2. Create a database named: `ecommerce`
3. Create collections:
   - `products`
   - `orders`
4. Add your IP to network access (or allow all)
5. Create a database user and get your **MongoDB URI**.

## ⚙️ Installation & Run
# Clone
git clone <repo-url>
cd ecommerce_api

# Install packages
pip install -r requirements.txt

# Set MongoDB URI in .env
touch .env
# Add: MONGO_URI=your-connection-uri

# Run server
uvicorn app.main:app --reload

##API Routes

## POST /products

<img width="737" height="502" alt="products-post" src="https://github.com/user-attachments/assets/43e8e278-3def-4fd0-8e80-ce7505786bd3" />
<img width="737" height="502" alt="products-post" src="https://github.com/user-attachments/assets/8449987d-8715-4532-b750-e7bf75e0f5f4" />

## GET /products

<img width="737" height="502" alt="products-post" src="https://github.com/user-attachments/assets/7dc98ea6-f16a-4f01-afd1-a240a8d1f9ec" />

## POST /orders
<img width="737" height="502" alt="products-post" src="https://github.com/user-attachments/assets/4931bfd0-6501-4716-976a-f197294bc175" />
<img width="737" height="502" alt="products-post" src="https://github.com/user-attachments/assets/b3dba453-c0a2-42fa-9d94-8bc9682a3724" />

## GET /orders/{user_id}
<img width="548" height="372" alt="order-et" src="https://github.com/user-attachments/assets/3a659a7e-d393-408f-bd0d-d1cf60074aae" />
<img width="936" height="626" alt="list" src="https://github.com/user-attachments/assets/34bf4027-9a85-4d2c-9cb9-323f6ce940ef" />


All these are accessible at /docs in FAST-api.
@Backend Task for HR-One
