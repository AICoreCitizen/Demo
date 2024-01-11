import psycopg2

# FORMAT
# conn = psycopg2.connect(<connection_details>)
# cursor = conn.cursor()

# create_table_query = """
#     CREATE TABLE IF NOT EXISTS <table_name> (
#         <column_name1> <data_type1>,
#         <column_name2> <data_type2>,
#         ...
#     )
# """

# cursor.execute(create_table_query)
# conn.commit()

# cursor.close()
# conn.close()