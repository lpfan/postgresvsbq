#!/usr/bin/env python

import click

from faker import Factory
from psycopg2.pool import ThreadedConnectionPool

import config


db_config_str = "dbname='{db}' user='{user}' host='{host}' port='{port}' password='{password}'"


def init_connection_pool():
    return ThreadedConnectionPool(1, 100, db_config_str.format(
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
def init_db():
    click.echo('InitDB is executing')


if __name__ == '__main__':
    cli()
