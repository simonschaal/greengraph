from matplotlib import pyplot as plt
from graph import Greengraph

def plotGraph(start='London', end='Oxford', steps=20, out='greengraph.png'):
    mygraph=Greengraph(start, end)
    data = mygraph.green_between(steps)
    plt.plot(data)
    
    #plt.savefig(out)
    plt.show()

