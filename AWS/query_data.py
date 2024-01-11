import psycopg2

# # FORMAT

# conn = psycopg2.connect(<connection_details>)
# cursor = conn.cursor()

# select_query = "SELECT * FROM <table_name>"

# cursor.execute(select_query)
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# cursor.close()
# conn.close()