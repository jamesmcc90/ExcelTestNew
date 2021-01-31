import cx_Oracle
import pandas as pd

dsn = cx_Oracle.makedsn('localhost', '1521', 'xe')
conn = cx_Oracle.connect('SYS', '64lislunnan', dsn, cx_Oracle.SYSDBA)
c = conn.cursor()

script = "SELECT * FROM CARS " \
         "WHERE CAR_MAKE LIKE 'V%' " \
         "AND CAR_COLOUR LIKE '%Bl%'"
script_output = pd.read_sql(script, conn).to_string()

print(script_output)
