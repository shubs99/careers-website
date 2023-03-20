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


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
  rows = []
  for row in result.all():
    rows.append(row._mapping)
  if len(rows) == 0:
    return None
  else:
    return dict(rows[0])


# rows = []
# for row in result.all():
#   rows.append(row._mapping)
# if len(rows) == 0:
#   return None
# else:
#   return [dict(row) for row in rows]
