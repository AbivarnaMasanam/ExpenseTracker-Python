#Expense Tracker - Python (Flask + MySQL)

  A simple yet powerful Expense Tracker Web Application built with Python, Flask, SQLAlchemy, and MySQL.
This project allows users to add income, track expenses, calculate balance, and visualize financial data — making it perfect for learning full stack web development with Python.

Features

  •	Add Income → Record your earnings.
  
  •	Add Expenses → Track spending by category & notes.
  
  •	Real-Time Balance Calculation → Total Income – Total Expenses.
  
  •	Negative Balance Highlight → Shows red if spending exceeds income.
  
  •	MySQL Database Integration → Persistent data storage.
  
  •	Responsive UI → Clean and simple design.
  
  •	RESTful Architecture → Built on Flask routes and templates.
  
Tech Stack

    Frontend
      •	HTML5
      •	CSS3
      •	Bootstrap
    Backend
      •	Python (Flask)
      •	Flask-SQLAlchemy
      •	Jinja2 (templating)
    Database
      •	MySQL (via PyMySQL)
    Tools
      •	PyCharm / VS Code
      •	Git & GitHub
      •	Virtual Environment (venv)

📂 Project Structure

      ExpenseTracker/
      │
      ├── app.py                # Main Flask app
      ├── templates/            # HTML templates
      │   ├── index.html        # Dashboard (income, expenses, balance)
      │   ├── add.html          # Add expense form
      │   └── add_income.html   # Add income form
      ├── static/               # CSS, JS, images (if any)
      │
      ├── requirements.txt      # Python dependencies
      └── README.md             # Project documentation


⚙️ Installation & Setup
  1️⃣ Clone the Repository
  
        git clone https://github.com/yourusername/expense-tracker.git
        cd expense-tracker
2️⃣ Create Virtual Environment
        
        python -m venv venv
        venv\Scripts\activate   # On Windows
        source venv/bin/activate # On Linux/Mac

3️⃣ Install Dependencies

      pip install -r requirements.txt

4️⃣ Setup MySQL Database

      CREATE DATABASE expense_tracker;
      CREATE USER 'trackeruser'@'localhost' IDENTIFIED BY 'password123';
      GRANT ALL PRIVILEGES ON expense_tracker.* TO 'trackeruser'@'localhost';
      FLUSH PRIVILEGES;
      
  5️⃣ Run the Application   
  
        python app.py
        
Visit 👉 http://127.0.0.1:5000
  
📸 Screenshots




🔑 Core Logic Explained

1.	User adds income (money available).
2.	User adds expense (money spent).
3.	The system calculates:
    •	total_income = sum of all incomes
  	
    •	total_expense = sum of all expenses
  	
    •	balance = total_income – total_expense
  	
4.	If balance < 0, it’s displayed in red color (indicating overspending).



📦 requirements.txt

      Flask
      Flask-SQLAlchemy
      PyMySQL
      cryptography

🎯 Use Cases
  •	Personal Budget Management
    
  •	Student Expense Tracking
    
  •	Learning Flask + SQLAlchemy + MySQL Integration
    
  •	Portfolio Project for Python Developers

🌟 Future Enhancements

  •	📊 Add charts/graphs for expenses by category 
    
  •	👤 Add user authentication (login/signup)
    
  •	📱 Make UI fully responsive
    
  •	📧 Email notifications for overspending
    
  •	☁️ Deploy on AWS/Heroku



🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

🔗 Connect with Me

  •	💼 LinkedIn
  
          https://www.linkedin.com/in/abivarna
  •	🐙 GitHub
  
      https://github.com/AbivarnaMasanam



      
 
