import math


def manhatten_distance(point_1, point_2):
    assert len(point_1) == len(point_2), "Error calculating manhatten distance. Points were of different dimensions."
    return sum([math.fabs(point_1[idx]-point_2[idx]) for idx in range(len(point_1))])



