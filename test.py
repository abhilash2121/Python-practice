import snowflake.connector

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