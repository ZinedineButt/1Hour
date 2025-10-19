import argparse
import click
"""
parser = argparse.ArgumentParser(description="Check a number.")
parser.add_argument("--number", type=int, required=True, help="An integer number to check.")
args = parser.parse_args()

if args.number > 10:
    print("True")
else:
    print("False")
"""

@click.command()
@click.option('--name', prompt='Your name', help='Your name')
def main(name):
    click.echo(f"Hello, {name}!")
if __name__ == '__main__':
    main()