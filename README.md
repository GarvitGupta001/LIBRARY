# The Book Architects Library

A web-based library management system built with Flask, MySQL, and modern frontend technologies.

## Features

- User authentication (Admin, Member, Guest)
- Book search, view, add, update, and delete
- Author, Publisher, Vendor, Transaction, and Fine management
- Profile management with image upload
- Chatbot assistant integration

## Prerequisites

- Python 3.8+
- MySQL Server
- Node.js (for frontend asset management, if needed)
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/library-project.git
cd library-project
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/Mac:
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database

- Create a MySQL database named `LIBRARY`.
- Update the database URI in `app.py` if your MySQL username or password is different:

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/LIBRARY'
```

### 5. Import Preloaded Data

To preload the database with sample authors, publishers, books, etc., run the following command in your MySQL client:

```sql
SOURCE d:/LIBRARY/data.sql;
```

Or, from the command line:

```bash
mysql -u root -p LIBRARY < d:/LIBRARY/data.sql
```

### 6. Set Up Environment Variables (Optional)

You can set environment variables for secret keys and upload folders, or edit `config/config.py` as needed.

### 7. Run Database Migrations

```bash
flask db upgrade
```

### 8. Run the Application

```bash
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000).

## Directory Structure

```
LIBRARY/
│
├── app.py
├── config/
│   └── config.py
├── Models/
├── Routes/
├── Services/
├── Static/
│   ├── css/
│   ├── js/
│   └── media/
├── Templates/
│   └── *.html
├── requirements.txt
├── data.sql
└── README.md
```

## Notes

- Profile and book cover images are stored in `Static/media/profile_pics` and `Static/media/book_covers`.
- Make sure the folders exist and are writable.
- For chatbot integration, ensure you have internet access.

## Troubleshooting

- If you encounter issues with MySQL connection, check your credentials and database status.
- For missing dependencies, run `pip install -r requirements.txt` again.

