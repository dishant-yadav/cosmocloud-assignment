# **Student Management System API**

This project is a backend application for managing students, built using **FastAPI** and **MongoDB**. It provides a set of APIs for creating, reading, updating, and listing students, with robust features for filtering and partial updates.


## **Features**
- Create a new student with structured data including name, age, and address.
- Retrieve student details using filters like age and country.
- Update student details partially or fully.
- Delete a student from the db
- Handles invalid data and ensures robust error handling.

---

## **Tech Stack**
- **Language**: Python
- **Framework**: FastAPI
- **Database**: MongoDB Atlas (Free M0 Cluster)
- **Deployment**: Render
- **Libraries**: 
  - `pymongo` for MongoDB integration.
  - `uvicorn` for serving the backend server

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-name>
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate       # For Linux/MacOS
venv\Scripts\activate          # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure MongoDB Atlas**
1. Create an account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Set up a free-tier cluster (M0).
3. Whitelist your IP address or set it to `0.0.0.0/0` for testing purposes.
4. Copy your connection string and update it in the `.env` file:
   
   ```env
   MONGODBURI=<link>
   ```

### **5. Run the Server**

```bash
fastapi dev
```

The API will now be accessible at: `http://127.0.0.1:8000`.

---

## **API Endpoints**

### **Base URL**
Replace `<base_url>` with https://cosmocloud-assignment-bwoi.onrender.com

| HTTP Method | Endpoint              | Description                 |
|-------------|-----------------------|-----------------------------|
| POST        | `/students`           | Create a new student        |
| GET         | `/students`           | List all students           |
| GET         | `/students/{id}`      | Get a student by ID         |
| PATCH       | `/students/{id}`      | Partially update a student  |
| DELETE      | `/students/{id}`      | Delete a student            |


### **Sample Requests**

#### **Create Student**
```bash
curl -X POST "<base_url>/students" \
-H "Content-Type: application/json" \
-d '{
    "name": "John Doe",
    "age": 20,
    "address": {
        "city": "New York",
        "country": "USA"
    }
}'
```

#### **List Students**
```bash
curl -X GET "<base_url>/students?country=USA&age=18"
```

#### **Get Student by ID**
```bash
curl -X GET "<base_url>/students/{id}"
```

#### **Update Student**
```bash
curl -X PATCH "<base_url>/students/{id}" \
-H "Content-Type: application/json" \
-d '{
    "address": {
        "city": "San Francisco"
    }
}'
```

#### **Delete Student**
```bash
curl -X DELETE "<base_url>/students/{id}"
```

---

## **Project Structure**

```
project/
├── app/
│   ├── crud.py           # CRUD operations
│   ├── routes.py         # API routes
│   ├── schema.py         # Pydantic schemas
│   ├── db.py             # MongoDB connection
│   ├── main.py           # Entry point
├── venv/                 # Virtual environment
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

---
