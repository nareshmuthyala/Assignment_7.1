import numpy as np


def moving_average(list1, window_size):
    """
    function to find moving average
    Iterate the list, find the moving average, add it to another list and return the same
    :param list1:
    :param window_size:
    :return: list
    """
    list2 = []
    n = len(list1)
    no_of_moving_averages = n - window_size + 1
    for i, val in enumerate(list1):
        if i < no_of_moving_averages:
            list2.append(np.sum(list1[i:i + window_size]) / window_size)
    return list2


print(moving_average([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 4))
print(moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150], 3))
print(moving_average([3., 5., 2., 8., 1., 2., 9., 1.5, 7.5, 5.5], 4))