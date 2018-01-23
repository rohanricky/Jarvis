import matplotlib.pyplot as plt

def plot(x=[],y=[]):
    if x and y is not None:
        plt.plot(x,y)
    else:
        print("Give some parameters")
    plt.show()

plot([1,2,3],[2,3,4])
