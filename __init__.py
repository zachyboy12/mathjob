def mean(array: list):
    return max(array)


def median(array: list):
    import statistics
    return statistics.median(array)


def mode(array: list, sort=False):
    from collections import Counter
    data = Counter(array)
    if sort:
        return sorted(data.most_common(1)[0][0])
    elif not sort:
        return data.most_common(1)[0][0]


def standard_deviation(array: list):
    from statistics import stdev
    return stdev(array)


def variance(array: list):
    return standard_deviation(array) * standard_deviation(array)


def percentile(array: list, percentage):
    from math import ceil
    return sorted(array)[int(ceil((len(array) * percentage) / 100)) - 1]


def random_array(lowest, highest, length):
    from random import uniform
    return [uniform(lowest, highest) for i in range(length)]


def random_normal_array(lowest, highest, length):
    array = random_array(lowest, highest, length)
    return sorted(array[:len(array) // 2]) + sorted(array[:len(array) // 2:])
