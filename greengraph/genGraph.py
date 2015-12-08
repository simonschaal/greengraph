from matplotlib import pyplot as plt
from graph import Greengraph

def plotGraph(start, end, steps, out):
    mygraph=Greengraph(start, end)
    data = mygraph.green_between(steps)
    plt.plot(data)

    if out:
        plt.savefig(out)
    plt.show()

