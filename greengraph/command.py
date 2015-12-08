from argparse import ArgumentParser
from genGraph import plotGraph

def process():
    parser = ArgumentParser(description = "Generate a graph of the proportion of green pixels in a series of satellite images between two points")
    parser.add_argument(’--from’, ’-f’)
    parser.add_argument(’--to’, ’-t’)
    parser.add_argument(’--steps’, ’-s’)
    parser.add_argument('--out', '-o')
    arguments= parser.parse_args()

    plotGraph(arguments.from, arguments.to, arguments.steps, arguments.out)
    
    
if __name__ == "__main__":
    process()
