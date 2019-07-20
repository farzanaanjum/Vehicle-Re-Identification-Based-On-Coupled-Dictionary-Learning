import sqlite3

con = sqlite3.connect('crime.db')



con.execute("INSERT INTO year2018 (id,regnum,description) \
      VALUES (1, 'MCLRNF1', 'CCTV footage obtained by police, shows two burglars')")
con.commit()
print "Records created successfully";
