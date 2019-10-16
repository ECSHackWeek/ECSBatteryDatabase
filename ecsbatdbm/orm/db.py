from sqlalchemy import create_engine


def create_sqlite3(db_out_filename):
    db = create_engine('sqlite:///' + db_out_filename)
    con = db.connect()
    Base.metadata.create_all(db)
    con.close()
