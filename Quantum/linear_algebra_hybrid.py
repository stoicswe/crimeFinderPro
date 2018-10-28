# Nathan Bunch
# 10/27/2018
# This part of the code is written as an accompaniment to the quantum kmeans
# algorithm. This file contains the functions necessary to perform the linear
# algebra mathematics for computing the kmeans and clustering the data.

import re, math, random # regexes, math functions, random numbers
import numpy as np
from functools import partial, reduce
from quantum_dot_product import dot, distance

def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    v_norm = np.linalg.norm(v)
    v = v / v_norm
    # the dot function here calls from the quantum_dot_product file
    return dot(v, v)

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))
