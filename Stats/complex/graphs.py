import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

image_file_path = "C:\\Users\\theon\\Documents\\GitHub\\StatisticsWebsiteClone\\Stats\\static\\"


def create_bell_graph(mean, std, user_x):
    """
    Creates a bell shaped graph png file
    :param mean: The mean value of the distribution
    :param std: The standard deviation of the distribution
    :param user_x: The x value entered by the user
    :return: None (creates a .png file)
    """
    mean = float(mean)
    std = float(std)

    plt.figure(figsize=(8, 6))

    x = np.linspace(mean - 5 * std, mean + 5 * std, 100)
    pdf = norm.pdf(x, mean, std)
    plt.plot(x, pdf, linewidth=1, color="r")

    plt.axvline(user_x, color="b", linestyle="-", label="x")

    shaded_area = np.where(x < user_x)
    plt.fill_between(x[shaded_area], pdf[shaded_area], color="gray", alpha=0.5, label="Probability")

    plt.xlabel("X-Axis")
    plt.ylabel("Probability Density")
    plt.title("Bell Shaped Graph")
    plt.legend()

    plt.grid(True)
    plt.savefig(image_file_path + "normal-graph.png")
    plt.close()
