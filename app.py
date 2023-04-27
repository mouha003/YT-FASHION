from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_prod_from_db

app = Flask(__name__)



@app.route("/")
def hello_world():
  products = load_jobs_from_db("products")
  prodcategory = load_jobs_from_db("product_category")
  return render_template('home.html', products=products, prodcategory=prodcategory)
@app.route("/api/products")
def list_products():
  products = load_jobs_from_db("products")
  prodcategory = load_jobs_from_db("product_category")
  return jsonify(products, prodcategory)

@app.route("/product/<id>")
def show_product(id):
  product = load_prod_from_db(id)
  return jsonify(product)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)