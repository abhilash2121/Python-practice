

import snowflake

QUERY_TO_VALIDATE_SNOWFLAKE_DATA_DETAILS = "select count(*) from INFORMATION_SCHEMA.columns where table_name = {}" \
                                           " and column_name = {}"

def get_snowflake_connection():
    ctx = snowflake.connector.connect(
        user="abhilash2121",
        password="Fazer@12345",
        account="ljb39130.us-east-1",
        database="SNOWFLAKE"
    )

    conn = ctx.cursor(DictCursor)
    return conn

"""
def check_schema(schema, conn):
    schemas = conn.execute("show schemas").fetchall()
    print(schemas)
    schema_list = [item["name"] for item in schemas]
    if schema in schema_list:
        return True
    else:
        return False
"""


conn = get_snowflake_connection()

res = conn.execute("select * from INFORMATION_SCHEMA.tables")
results = res.fetchall()
schema_list = [item["TABLE_SCHEMA"] for item in results]
table_list = [item["TABLE_NAME"] for item in results if item["TABLE_SCHEMA"] == "ACCOUNT_USAGE"]