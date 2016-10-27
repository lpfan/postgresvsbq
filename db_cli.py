#!/usr/bin/env python

import click

from sqlalchemy import create_engine


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
