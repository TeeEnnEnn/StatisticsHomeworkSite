import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray


def generate_graph_data(data_set: np.ndarray):
    x_values = data_set
    _range = np.ptp(data_set)

    if len(data_set) >= 3:
        y_values = np.linspace(float(np.min(data_set) - _range), float(np.max(data_set) + _range), len(data_set))
        return x_values, y_values
    else:
        raise ValueError("Not enough values in the data set")


def generate_line_graph(data_set: ndarray):
    x_values, y_values = generate_graph_data(data_set)

    plt.plot(x_values, y_values, marker="o")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Trend Graph")
    plt.grid(True)

    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\line_graph.png"
    plt.savefig(graph_image_path)
    plt.close()


def generate_frequency_graph(data_set: ndarray):
    frequencies, bins, _ = plt.hist(data_set, bins="auto", edgecolor="black", alpha=0.7)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Frequency Histogram')
    plt.grid(True)

    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\frequency_graph.png"
    plt.savefig(graph_image_path)
    plt.close()
