import os
import psycopg2
import sys
import urlparse
import time

con=None

urlparse.uses_netloc.append('postgres')
url = urlparse.urlparse(os.environ['DATABASE_URL'])


def dbexecute(sqlcommand, receiveback):
  databasename=os.environ['DATABASE_URL']
  #username=''
  con=psycopg2.connect(
    database= url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
  )
  result=''
  cur=con.cursor()

  cur.execute(sqlcommand)
  if receiveback:
      result=cur.fetchall()

  con.commit()
  cur.close()
  con.close()
  return result
