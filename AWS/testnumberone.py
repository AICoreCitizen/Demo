import psycopg2

# Database connection details
host = "first-database.cuewdxmg0moe.eu-west-1.rds.amazonaws.com"
port = "5432"
database = "testnumberone"
user = "postgres"
password = "Kenshin1ce"

# Establish the connection
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Perform database operations using the connection
# ...
with conn.cursor() as cur:
    cur.execute("""SELECT table_name FROM information_schema.tables
    WHERE table_schema = 'public'""")
    for table in cur.fetchall():
        print(table)
# Close the connection when finished
conn.close()
