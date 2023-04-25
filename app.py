from flask import Flask, render_template, jsonify

app = Flask(__name__)
PRODUCT_CATEGORY = [
  {
    'id': 1,
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/Classic-White-CAP-asdge5trtydfv.jpg',
    'title': 'ACCESSORIES'
  },
    {
    'id': 2,
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/Kids-Collection.jpg',
    'title': 'KIDS'
  },
    {
    'id': 3,
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/Men-Collections.jpg',
    'title': 'MEN'
  },
    {
    'id': 4,
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/Wire-red-polo-sdlkjaf78jasd876f.jpg',
    'title': 'POLOS'
  },
  {
    'id': 5,
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/Blue-Tee-7865zxgfh987.jpg',
    'title': 'TEES'
  },
    {
    'id': 6,
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/01.jpg',
    'title': 'WOMEN'
  }
]

PRODUCTS = [
  {
    'id': 1,
    'title': 'YT Band Collar Iconic Polo for Men – White',
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/category-style-Polos-Blue.jpg',
    'price': '$90',
    'condition': 'Sale',
    'sale_price': '$40'
  },
  {
    'id': 2,
    'title': 'YT Kids Premium Graphic Tee – Black',
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/B0U014CRPC-BLK_02.jpg',
    'price': '$55',
    'condition': 'New',
    'sale_price': '$30'
  },
  {
    'id': 3,
    'title': 'YT Premium Graphic Tee – Pink (100% Cotton)',
    'img': 'https://ytfashion.us/wp-content/uploads/2023/01/GW313JTP-PINK-5.jpg',
    'price': '$60',
    'condition': 'New',
    'sale_price': '$30'
  },
  {
    'id': 4,
    'title': 'Classic Black FTWL Snapback',
    'img': 'https://ytfashion.us/wp-content/uploads/2023/02/56.jpg',
    'price': '$35',
    'condition': 'Sale',
    'sale_price': '$20'
  }
  
]


@app.route("/")
def hello_world():
  return render_template('home.html', products=PRODUCTS, prodcategory=PRODUCT_CATEGORY)
@app.route("/api/products")
def list_products():
  return jsonify(PRODUCTS, PRODUCT_CATEGORY)
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)