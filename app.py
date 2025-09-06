from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# MySQL connection (update credentials if needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://trackeruser:password123@localhost/expense_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Income model
class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


# Expense model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(120), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    incomes = Income.query.order_by(Income.date.desc()).all()

    total_income = sum(i.amount for i in incomes)
    total_expense = sum(e.amount for e in expenses)
    balance = total_income - total_expense

    return render_template(
        'index.html',
        expenses=expenses,
        total_income=total_income,
        total_expense=total_expense,
        balance=balance
    )


@app.route('/add_income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        new_income = Income(amount=amount)
        db.session.add(new_income)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_income.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        note = request.form.get('note', '')
        new_expense = Expense(amount=amount, category=category, note=note)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
