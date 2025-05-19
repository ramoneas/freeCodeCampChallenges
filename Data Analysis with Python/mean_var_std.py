import numpy as np


def mean(input, matrix):
    return [np.average(matrix, axis=0).tolist(), np.average(matrix, axis=1).tolist(), np.average(input).tolist()]


def variance(input, matrix):
    return [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(input).tolist()]


def std(input, matrix):
    return [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(input).tolist()]


def get_max(input, matrix):
    return [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(input).tolist()]


def get_min(input, matrix):
    return [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(input).tolist()]


def summatory(input, matrix):
    return [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(input).tolist()]


def calculate(list):
    if len(list) < 9.0:
        raise ValueError("List must contain nine numbers.")

    a = np.array(list)
    matrix = a.reshape(3, 3)

    calculations = {
        'mean': mean(a, matrix),
        'variance': variance(a, matrix),
        'standard deviation': std(a, matrix),
        'max': get_max(a, matrix),
        'min': get_min(a, matrix),
        'sum': summatory(a, matrix)
    }

    return calculations
