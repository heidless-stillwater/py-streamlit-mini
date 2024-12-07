import click


@click.command()
@click.option("--who", default="world", help="Whom to greet.")
def say_hello(who):
    """ Simple CLI to greet someone! """
    print(f"hello {who}!")


if __name__ == "__main__":
    say_hello()

