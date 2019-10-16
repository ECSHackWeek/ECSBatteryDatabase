#!/usr/bin/env python

import click
import ecsbatdbm.orm


@click.command()
@click.option('-d', '--db_file', 'db_file', type=str, required=True,
                help='a sqlite3 database filename to be created')
def create_sqlite3_db(db_file):
    """
    Create a SQLite3 database with the ECS Battery Database Model
    """
    ecsbatdbm.orm.create_sqlite3(db_file)

if __name__ == '__main__':
    create_sqlite3_db()
