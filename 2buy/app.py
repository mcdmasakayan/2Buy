from flask import Flask, render_template, redirect, url_for, request
import mysql.connector as mysql

app = Flask(__name__)

app.secret_key = "root123"
logged_in = False

#Database#
connected = False

while(connected == False):
    try:    #if database exists#
        global db, crsr

        db = mysql.connect(host="localhost", port=3306, user="root", passwd="root", database="2Buy")
        crsr = db.cursor()
        
        try:    #if table does not exist#
            query = """CREATE TABLE items (id int PRIMARY KEY AUTO_INCREMENT, quantity int UNSIGNED,
                    name VARCHAR(255), type VARCHAR(255), price int UNSIGNED)"""

            crsr.execute(query)

        except:    #if table exists#
            connected = True

    except:    #if database does not exist#
        db = mysql.connect(host="localhost", port=3306, user="root", passwd="root")
        crsr = db.cursor()
        crsr.execute("CREATE DATABASE 2Buy")

#Data Handling#
def insert_data(item_quantity, item_name, item_type, item_price):
    crsr.execute("INSERT INTO items (quantity, name, type, price) VALUES (%s, %s, %s, %s)",
                     (item_quantity, item_name, item_type, item_price))
    db.commit()

#Landing Page#
@app.route("/")
def base_page():
    if logged_in == False:
        return redirect(url_for("login_page"))
    else:
        return redirect(url_for("home_page"))

@app.route("/login")
def login_page():
    page = "Login"

    return render_template("login.html", page_title=page)

@app.route("/signup")
def signup_page():
    page = "Signup"

    return render_template("signup.html", page_title=page)

#Home Page#
@app.route("/home", methods = ["POST", "GET"])
def home_page():
    page = "Home"

    if request.method == "POST":
        item_quantity = request.form['quantity-entry']
        item_name = request.form['name-entry']
        item_type = request.form['type-entry']
        item_price = request.form['price-entry']

        insert_data(item_quantity, item_name,
                    item_type, item_price)
        
        return redirect(url_for("home_page", page_title=page,
                                item_quantity=item_quantity,
                                item_name=item_name,
                                item_type=item_type,
                                item_price=item_price))
    else:
        return render_template("home.html", page_title=page)

if __name__ == "__main__":
    app.run(debug=True)