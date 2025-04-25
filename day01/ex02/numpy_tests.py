import numpy as np
import time

results_python = 0
results_numpy = 0


python_tab = [i for i in range(10_000_000)]
numpy_tab = np.array(python_tab)

start_time = time.time()
double = numpy_tab * 2
res_numpy = (time.time() - start_time) // 1e-3

start_time = time.time()
double = [i * 2 for i in python_tab]
res_python = (time.time() - start_time) // 1e-3

print(f"numpy : {res_numpy} ms")
print(f"python : {res_python} ms")
print(f"numpy is {int(res_python / res_numpy)} times faster than python")
