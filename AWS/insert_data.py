import psycopg2

# # FORMAT
# conn = psycopg2.connect(<connection_details>)
# cursor = conn.cursor()

# insert_query = """
#     INSERT INTO <table_name> (<column_name1>, <column_name2>, ...)
#     VALUES (%s, %s, ...)
# """

# data = (<value1>, <value2>, ...)
# cursor.execute(insert_query, data)
# conn.commit()

# cursor.close()
# conn.close()