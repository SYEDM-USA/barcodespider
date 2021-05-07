import pandas as pd
import sqlite3 as sq
data = <This is going to be your pandas dataframe>
sql_data = 'D:\\SA.sqlite' #- Creates DB names SQLite
conn = sq.connect(sql_data)
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS SA''')
data.to_sql('SA', conn, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
pd.read_sql('select * from SentimentAnalysis', conn)
conn.commit()
conn.close()