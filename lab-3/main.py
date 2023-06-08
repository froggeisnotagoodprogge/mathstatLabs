import numpy
import scipy.stats
nu_1=2
nu_2=1
disp=1
n1 = 25
n2 = 10000
k = 1000
counter=0

q = scipy.stats.t.ppf(q = 0.975, df = 2 * n1 - 2)
precalculated_half = q * numpy.sqrt(2.0/(n1*(2*n1-2)))
for i in range (k):
    X_sample = numpy.random.normal(size=n1, loc = nu_1, scale=disp)
    Y_sample = numpy.random.normal(size=n1, loc= nu_2, scale=disp)
    lower_limit = numpy.mean(X_sample) - numpy.mean(Y_sample) - q * precalculated_half*numpy.sqrt(n1 * (numpy.var(X_sample, ddof=1) + numpy.var(Y_sample, ddof=1)))
    higher_limit = numpy.mean(X_sample) - numpy.mean(Y_sample) + q * precalculated_half*numpy.sqrt(n1 * (numpy.var(X_sample, ddof=1) + numpy.var(Y_sample, ddof=1)))
    if(lower_limit < (nu_1 - nu_2) and (nu_1 - nu_2) < higher_limit):
        counter+=1
print(counter)

q = scipy.stats.t.ppf(q = 0.975, df = 2 * n2 - 2)
precalculated_half = q * numpy.sqrt(2.0/(n2*(2*n2-2)))
for i in range (k):
    X_sample = numpy.random.normal(size=n2, loc = nu_1)
    Y_sample = numpy.random.normal(size=n2, loc= nu_2)
    lower_limit = numpy.mean(X_sample) - numpy.mean(Y_sample) - q * precalculated_half*numpy.sqrt(n2 * (numpy.var(X_sample) + numpy.var(Y_sample)))
    higher_limit = numpy.mean(X_sample) - numpy.mean(Y_sample) + q * precalculated_half*numpy.sqrt(n2 * (numpy.var(X_sample) + numpy.var(Y_sample)))
    if(lower_limit < (nu_1 - nu_2) and (nu_1 - nu_2) < higher_limit):
        counter+=1
print(counter)