

from organism import math_util


def product_aggregation(x):  # note: `x` is a list or other iterable
    return reduce(mul, x, 1.0)



def sum_aggregation(x):
    return sum(x)



def max_aggregation(x):
    return max(x)



def min_aggregation(x):
    return min(x)



def maxabs_aggregation(x):
    return max(x, key=abs)



def median_aggregation(x):
    return median2(x)



def mean_aggregation(x):
    return mean(x)


AggregationFunctionSet = [
product_aggregation,
sum_aggregation,
max_aggregation,
min_aggregation,
maxabs_aggregation,
median_aggregation,
mean_aggregation
]
