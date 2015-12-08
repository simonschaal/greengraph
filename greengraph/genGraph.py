from matplotlib import pyplot as plt
from graph import Greengraph

def plotGraph(start, end, steps, out=None):
    """ Generate a greeting string for a person.
    Parameters
    ----------
    start: str
    Starting city.
    end: str
    Ending city.
    steps: int
    Gives number of images to process between start and end.
    out: str
    Specifies output file for graph. If not given then graph will be displayed. 
    Returns
    -------
    Nothing
    """

    mygraph=Greengraph(start, end)
    data = mygraph.green_between(steps)
    plt.plot(data)
    plt.xlabel("steps")
    plt.ylabel("proportion of green pixels")
    plt.title("Greengraph from "+start+" to "+end)

    if out:
        plt.savefig(out)
    else:
        plt.show()

