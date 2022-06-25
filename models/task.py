from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date, Text
from config.db import meta, engine
#from .user import users

tasks = Table(
            "tasks", meta, 
            Column('id', Integer, primary_key=True), 
            Column('name', String(255)),
            Column('description', Text),
            Column('date', Date)
            )

meta.create_all(engine)
