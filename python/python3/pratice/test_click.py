# -*- coding:utf-8 -*-
import click


@click.command()
@click.option(
    '--count', default=1, type=int, help='Number of greetings.'
)
@click.option(
    '--name', prompt='Your name', help='The person to greet.'
)
def hello(count, name):
    """ test test """
    for x in range(count):
        click.echo('hello %s!' % name)


if __name__ == "__main__":
    hello()
