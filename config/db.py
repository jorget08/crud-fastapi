from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:lolazolol@localhost:3306/task")

meta = MetaData()

conn = engine.connect()