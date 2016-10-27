#!/usr/bin/env python
import click
import psycopg2

from faker import Factory
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    ForeignKey,
    create_engine
)

import config


db_config_str = "dbname='{db}' user='{user}' host='{host}' port='{port}' password='{password}'"


def _init_db_connection_pool():
    return psycopg2.pool.ThreadedConnectionPool(1, 100, db_config_str.format(
        db=config.DB['POSTGRES_STORE']['DB'],
        user=config.DB['POSTGRES_STORE']['USER'],
        host=config.DB['POSTGRES_STORE']['HOST'],
        port=config.DB['POSTGRES_STORE']['PORT'],
        password=config.DB['POSTGRES_STORE']['PASSWORD']
    ))


def _create_generic_table(table_name, column_count, metadata=None):
    if metadata is None:
        metadata = MetaData()
    columnset = [
        Column('id', Integer, primary_key=True)
    ]
    Table(table_name, metadata, *columnset)


def _init_db_connection():
    return psycopg2.connect(db_config_str.format(
        db=config.DB['POSTGRES_STORE']['DB'],
        user=config.DB['POSTGRES_STORE']['USER'],
        host=config.DB['POSTGRES_STORE']['HOST'],
        port=config.DB['POSTGRES_STORE']['PORT'],
        password=config.DB['POSTGRES_STORE']['PASSWORD']
    ))


@click.group()
def cli():
    pass


@cli.command()
def generate_csv():
    click.echo('Start generating the cvs')


@cli.command()
@click.argument('db', help='Set the DB you are going to work with.')
@click.option('--tables-count', type=click.INT, help='Specify how many tables you want to have in DB.')
@click.option('--table-width', type=click.INT, help='Specify how many columns every table should has.')
def prepare_db(db, tables_count, table_width ):
    click.echo('InitDB is executing')
    metadata = MetaData()

    for table_index in range(tables_count):
        _create_generic_table('some_name', table_width, metadata=metadata)

    engine = create_engine("postgresql://scott:tiger@localhost/test")
    metadata.create_all(engine)


if __name__ == '__main__':
    cli()
