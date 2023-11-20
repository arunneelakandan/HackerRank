import time

start_time = time.time()

num_multiplies = 50000000
data = range(num_multiplies)
number = 1

for i in data:
    number *= 1.0000001

end_time = time.time()

print(number)
print("Run time = {}".format(end_time - start_time))