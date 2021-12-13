import numpy as np
import cProfile


def list_add_two(l, iterations):
    for _ in range(iterations):
        l = [i + 2 for i in l]
    return l


def array_add_two(a, iterations):
    for _ in range(iterations):
        a = a + 2
    return a


def test():
    my_list = list(range(1000000))
    my_array = np.array(my_list)
    iterations = 100

    list_add_two(my_list, iterations)
    array_add_two(my_array, iterations)


cProfile.run('test()')