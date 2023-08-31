import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray


def generate_graph_data(data_set: np.ndarray):
    """
    Maps data set values to y values.
    :param data_set: the data set to be mapped
    :return: a tuple (x, y) x values =  data set values, y values = mapped values
    """
    x_values = data_set
    _range = np.ptp(data_set)

    if len(data_set) >= 3:
        y_values = np.linspace(float(np.min(data_set) - _range), float(np.max(data_set) + _range), len(data_set))
        return x_values, y_values
    else:
        raise ValueError("Not enough values in the data set")


def generate_line_graph(data_set: ndarray):
    """
    generates a line graph from data set values
    :param data_set: data set used to make graph
    :return: None
    """
    x_values, y_values = generate_graph_data(data_set)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, marker="o")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Trend Graph")
    plt.grid(True)

    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\line_graph.png"
    plt.savefig(graph_image_path)
    plt.close()


def generate_frequency_graph(data_set: ndarray):
    """
    generates a frequency graph from data set values
    :param data_set: data set used to make graph
    :return: None
    """
    plt.figure(figsize=(8, 6))
    frequencies, bins, _ = plt.hist(data_set, bins="auto", edgecolor="black", alpha=0.7)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Frequency Histogram')
    plt.grid(True)

    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\frequency_graph.png"
    plt.savefig(graph_image_path)
    plt.close()


def generate_boxplot(data_set: ndarray):
    """
    generates a boxplot from data set values
    :param data_set: data set used to make graph
    :return: None
    """
    plt.figure(figsize=(8, 6))
    plt.boxplot(data_set, vert=False)

    plt.xlabel('Values')
    plt.ylabel('Data Set')
    plt.title('Box and Whisker Plot')

    graph_image_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\boxplot.png"
    plt.savefig(graph_image_path)
    plt.close()
