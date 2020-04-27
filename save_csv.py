import sqlite3

conn = sqlite3.connect("urls.db")
c = conn.cursor()
c.execute("SELECT checkdash, checkdot, checkifhttps, checklen, checkreq, checkanch, checkage, checkpop, phish from url where isparsed = 1")
rows = c.fetchall()
for row in rows:
  print row[0], ",", row[1], ",", row[2], ",", row[3], ",", row[4], ",", row[5], ",", row[6], ",", row[7], ",", row[8]
