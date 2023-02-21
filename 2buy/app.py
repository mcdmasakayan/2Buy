from flask import Flask, render_template, redirect, url_for, request
import mysql.connector as mysql

class States:
    logged_in = False
    connected = False

app = Flask(__name__)
state = States()

#Database
while(state.connected == False):
        try:    #if database exists#
            db = mysql.connect(host="localhost", port=3306, user="root", passwd="root", database="2Buy")
            crsr = db.cursor()
            
            try:    #if table does not exist#
                query = """CREATE TABLE items (id int PRIMARY KEY AUTO_INCREMENT, quantity int UNSIGNED,
                        name VARCHAR(255), type VARCHAR(255), price int UNSIGNED)"""

                crsr.execute(query)

            except:    #if table exists#
                print("SYSTEM: Database connected.")
                state.connected = True
                crsr.execute("SELECT * FROM items")
                data = crsr.fetchall()

        except:    #if database does not exist#
            db = mysql.connect(host="localhost", port=3306, user="root", passwd="root")
            crsr = db.cursor()
            crsr.execute("CREATE DATABASE 2Buy")

#Web#
@app.route("/", methods=["POST", "GET"])
def base():
    if state.logged_in == True:
        print(data)
        return redirect(url_for("home_page", user="Backend", login_state=state.logged_in, data=data))
    else:
        return redirect(url_for("login_page"))

@app.route("/2buy-login", methods = ["POST", "GET"])
def login_page():
    page_name = "Login"
    state.logged_in = False

    if request.method == "POST":
        if (request.form['username-entry'] == "backend") and (request.form['password-entry'] == "developer"):
            state.logged_in = True

    if state.logged_in == False:
        state.logged_in = False
       
        return render_template("login.html", page_title=page_name)
    
    else:
        state.logged_in = True
        return redirect(url_for("base"))

@app.route("/2buy-<user>", methods=["POST", "GET"])
def home_page(user):
    page_name = user

    if request.method == "POST" and (request.form['quantity-entry'] and request.form['name-entry']
                                     and request.form['type-entry'] and request.form['price-entry']):
        crsr.execute("INSERT INTO items (quantity, name, type, price) VALUES (%s, %s, %s, %s)",
                     (request.form['quantity-entry'], request.form['name-entry'],
                      request.form['type-entry'], request.form['price-entry']))
        db.commit()

    crsr.execute("SELECT * FROM items")
    data = crsr.fetchall()
        
    if state.logged_in == True:
        state.logged_in = True

        return render_template("home.html", page_title=page_name, login_state=state.logged_in, data=data)
    else:
        state.logged_in = False
        return redirect(url_for("login_page"))

if __name__ == "__main__":
    app.secret_key = "2buykey"
    app.run(debug=True)