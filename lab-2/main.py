import numpy
import matplotlib.pyplot as plt
def first_task():
    sizes = [100, 500, 1000, 10000, 100000, 1000000]
    for i in sizes:
        sample_array = numpy.random.laplace(0, 0.5, i)
        # we can generate several samples of each size for better demonsration, 
        # but that is enough
        sample_mean = numpy.mean(sample_array)
        sample_var = numpy.var(sample_array)
        print ("mean: ", sample_mean, "var: ", sample_var, "with size: ", i)

def second_task():
    sizes = [100, 500, 1000, 10000, 100000, 1000000]
    for i in sizes:
        sample_array = numpy.random.binomial(4, 0.2, size = (100, i))
        sample_mean = numpy.mean(sample_array, axis=1)
        sample_theta_estimation = sample_mean/4
        sample_theta_estimation = numpy.mean(sample_theta_estimation)
        print ("Среднее оценки параметра(эмпирических значений) для выборок размера ", i, ": --", sample_theta_estimation)

first_task()
second_task()