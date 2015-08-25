__author__ = 'Zachary Andrews'

# import statements
import csv
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# name of the excel file containing the data
CSV_FILE = 'content.csv'

# name of the file for the scatter plot
SCATTER_FILE = 'scatter_solution.png'

# name of the file for the histogram
HISTOGRAM_FILE = 'histogram_solution.png'


def create_scatter(data):
    """
    :param data: list of Facebook data
    :return: none
    """

    # create lists to hold the points for num_likes and num_comments
    num_likes_list = []
    num_comments_list = []

    # remove the entry containing the labels for the data
    data.remove(data[0])

    # loop through the data, counting the number of likes and comments
    for x in data:

        # place the two numbers on a scatter plot
        if x[2] and x[3] != '':
            plt.scatter(x[2], x[3])
            num_likes_list.append(int(x[2]))
            num_comments_list.append(int(x[3]))

    # turn the lists into tuples to fit linear regression line
    num_likes_array = np.array(num_likes_list)
    num_comments_array = np.array(num_comments_list)

    # calculate line using slope-intercept form
    slope, intercept, r_value, p_value, std_err = \
        linregress(num_likes_array, num_comments_array)
    y = slope * num_likes_array + intercept

    # plot the line on the scatter plot
    plt.plot(num_likes_array, y)

    # add labels/title for the scatter plot
    plt.title('num_comments vs num_likes')
    plt.xlabel('num_likes')
    plt.ylabel('num_comments')

    plt.show()

    # save the scatter plot in the specified file
    plt.savefig(SCATTER_FILE)


def construct_histogram(type_count):
    """
    :param type_count: a list with the count of each type
    :return: none
    """

    # gather the number of bars, and space them evenly using numpy arrange
    num_groups = len(type_count)
    index = np.arange(num_groups)

    # construct the bars given the different data points
    data_points = (type_count[0], type_count[1], type_count[2],
                   type_count[3], type_count[4])

    # give the bars a specific width
    b_width = 0.50

    # plot the bars on the graph and add labels/title
    plt.bar(index, data_points, b_width,
                     color='b')
    plt.title('Histogram of Message Types')
    plt.ylabel('Counts')
    plt.xticks(index + b_width, ('Event', 'Link', 'Photo', 'Status', 'Video'))
    plt.show()

    # save the file to the specified filed name
    plt.savefig(HISTOGRAM_FILE)


def load_data(data):
    """
    :param data: list of Facebook data
    :return: a list of Facebook data
    """

    # gather the data from the csv file and store in the data list
    with open(CSV_FILE, mode='r', encoding='utf-8', newline="") as file:
        reader = csv.reader(file, doublequote='True', quotechar='"', delimiter=',',
                            quoting=csv.QUOTE_ALL, lineterminator='\r\n')

        # place reader data into the data list
        for x in reader:
            data.append(x)

    return data


def get_type_count(data):
    """
    :param data: list of Facebook data
    :return: a list with the count of each type
    """

    # get the count for each bar graph
    type_count = [0, 0, 0, 0, 0]
    for d in data:
        if d[1] == 'event':
            type_count[0] += 1
        if d[1] == 'link':
            type_count[1] += 1
        if d[1] == 'photo':
            type_count[2] += 1
        if d[1] == 'status':
            type_count[3] += 1
        if d[1] == 'video':
            type_count[4] += 1
    return type_count


def main():
    # list to store the data
    data = []

    # load the proper data into the list with the load function
    data = load_data(data)

    # get the type_count list from the type_count function
    type_count = get_type_count(data)

    # construct the histogram
    construct_histogram(type_count)

    # create a scatter plot of the data
    create_scatter(data)

if __name__ == '__main__':
    main()