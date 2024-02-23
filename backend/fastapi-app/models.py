from sqlalchemy import Table, Column, Integer, String, MetaData


metadata = MetaData()

Contact = Table(
    "contacts",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("email", String, index=True),
    Column("message", String),
)
