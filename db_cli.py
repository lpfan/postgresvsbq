#!/usr/bin/env python
import random

import click
import psycopg2

from faker import Factory
from sqlalchemy import types as sql_types
from sqlalchemy import (
    Table,
    MetaData,
    Column,
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
    possible_column_type = [
        sql_types.Boolean,
        sql_types.Date,
        sql_types.DateTime,
        sql_types.Float,
        sql_types.Integer,
        sql_types.Numeric,
        sql_types.String,
        sql_types.Text
    ]


    if metadata is None:
        metadata = MetaData()
    columnset = [
        Column('id', sql_types.Integer, primary_key=True)
    ]

    for cc in range(column_count):
        column_type = random.choice(possible_column_type)
        columnset.append(
            Column('column_{}'.format(cc), column_type, nullable=True)
        )

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
@click.argument('db')
@click.option('--tables-count', type=click.INT, help='Specify how many tables you want to have in DB.')
@click.option('--table-width', type=click.INT, help='Specify how many columns every table should has.')
def prepare_db(db, tables_count, table_width ):
    click.echo('InitDB is executing')
    metadata = MetaData()

    for table_index in range(tables_count):
        _create_generic_table('table_{}'.format(table_index), table_width, metadata=metadata)

    engine = create_engine('postgresql://test:test@localhost:9887/test')
    import ipdb; ipdb.set_trace()  # XXX BREAKPOINT
    metadata.create_all(engine)


if __name__ == '__main__':
    cli()
