import algorithms
import click
from algorithms.sorting_algorithm import SortingAlgorithm
import json

algorithms = { alg.__name__: alg for alg in SortingAlgorithm.__subclasses__() }

@click.command()
@click.option('-a', '--algorithm', required=True, type=click.Choice(list(algorithms.keys()), case_sensitive=False))
@click.option('-l', '--array', required=True, type=str)
def main(algorithm: SortingAlgorithm, array: str):
    array = json.loads(array)
    print(array)
    print(algorithms[algorithm]().sort(array))
