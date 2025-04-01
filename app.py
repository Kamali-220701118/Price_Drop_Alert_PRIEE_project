from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, template_folder="templates")

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
cursor = db.cursor()
@app.route('/')
def home():
    return render_template('front.html')
# Route to Display Products
@app.route('/view_product')
def view_product():
    #print("open")
    #return "Page opened"
    cursor.execute("SELECT product_name, price, image_url FROM product")
    products = cursor.fetchall()  # Fetch all products from DB
    return render_template('view_product.html', products=products)

@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)
