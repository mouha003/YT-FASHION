from sqlalchemy import create_engine, text
import os

db_conn_string = os.getenv('DB_CONNECTION_STRING')
engine = create_engine( db_conn_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_jobs_from_db(products):
  query = "select * from "+ products
  with engine.connect() as conn:
    result = conn.execute(text(query))
    prods = []
    for row in result.all():
      prods.append(row._asdict())
    return prods

def load_prod_from_db(id):
  query = "select * from products where id ="+id
  with engine.connect() as conn:
    result = conn.execute(text(query))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

def add_product_to_db(data):
  with engine.connect() as conn:
    query = "INSERT INTO products (title, img, price, prod_condition, sale_price) \
    VALUES ('%s', '%s', '%s', '%s', '%s')" % ( data['title'],data['img'],data['price'], data['condition'], data['sale_price'] )
    
    conn.execute(text(query))