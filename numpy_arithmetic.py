import numpy

n,m = [int(i) for i in input().split()]

a = numpy.array([int(i) for i in input().split()])
b = numpy.array([int(i) for i in input().split()])


print (numpy.array(numpy.add(a, b), ndmin=2))
print (numpy.array(numpy.subtract(a, b), ndmin=2))
print (numpy.array(numpy.multiply(a, b), ndmin=2) )   #[  5.  12.  21.  32.]
print (numpy.array(numpy.floor_divide(a, b), ndmin=2))     #[ 0.2         0.33333333  0.42857143  0.5       ]
print (numpy.array(numpy.mod(a, b), ndmin=2)) #[ 1.  2.  3.  4.]
print (numpy.array(numpy.power(a, b), ndmin=2))         