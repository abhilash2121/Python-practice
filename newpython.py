d1 = {
    "data": {"shema": "SCHEMA",
             "table": "table"}
}

QUERY = """
select * from employees
where {}"""

where_clause = f"""
TABLE_SCHEMA = '{d1.get("data").get("schema").upper()}' and
TABLE_NAME = '{d1.get("data").get("table").upper()}'
"""

print(QUERY.format(where_clause))
