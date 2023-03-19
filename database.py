import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    jobs_list = []
    column_names = result.keys()
    for row in result.all():
      jobs_list.append(dict(zip(column_names, row)))
      print(jobs_list)
    return jobs_list
