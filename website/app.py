from flask import Flask, render_template
import sqlite3
import pathlib

cwd = pathlib.Path.cwd()
base_path = pathlib.Path(r'C:\Users\gregory.odiase\Documents\Greg\school work\DAB 111 - Python\projects\flask_project\database')
db_name = "customers.db"
db_path = base_path / db_name
print(db_path)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    columns = [
        [
            'row_number', 'numerical', 'sequential order of data'
        ],
        [
            'invoice_id', 'categorical', 'identity number on invoice'
        ],
    ]
    return render_template("about.html", columns=columns)

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    students = cursor.execute("SELECT * FROM customer_data limit 10").fetchall()
    con.close()

    columns = ['row_number', 'invoice_id', 'branch', 'customer_id', 'gender', 'age',
       'customer_type', 'credit_score', 'product_category',
       'number_of_products', 'tax_amount', 'price', 'total_amount', 'ratings',
       'customer_churn']
    
    return render_template("data_table.html", columns=columns, students=students)

if __name__=="__main__":
    app.run(debug=True)