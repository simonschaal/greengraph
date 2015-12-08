from argparse import ArgumentParser
from genGraph import plotGraph
import sys

def process():
    parser = ArgumentParser(description = "Generates a graph of the proportion of green pixels in a series of satellite images between two points")
    parser.add_argument('--from', dest="start", help="Starting city for Greengraph")
    parser.add_argument('--to', dest="end", help="End city for Greengraph")
    parser.add_argument('--steps', help="Number of images to process between the cities")
    parser.add_argument('--out', help="Destination file to save the graph")
    arguments= parser.parse_args()

    #Make sure all necessary arguments are given
    if len(sys.argv[1:])<3:
        parser.print_help()
        parser.exit()

    plotGraph(arguments.start, arguments.end, arguments.steps, arguments.out)
 
    
    
if __name__ == "__main__":
    process()
