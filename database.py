from sqlalchemy import create_engine, text
import os

db_conn_string = os.environ['DB_CONNECTION_STRING']
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
