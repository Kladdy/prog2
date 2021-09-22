#!/usr/bin/env python3

from integer import Integer
from matplotlib import pyplot as plt
from time import perf_counter as pc
from numba import njit

# I use the Fibonacci sequence 1, 1, 2, 3, ... (not starting with 0)
@njit
def fib_numba_py(n):
        if n <= 1:
                return 1
        else:
                return(fib_numba_py(n-1) + fib_numba_py(n-2))

def fib_pure_py(n):
        if n <= 1:
                return 1
        else:
                return(fib_pure_py(n-1) + fib_pure_py(n-2))

def main():

	# Timings for fib_pure_py, fib_numba_py, fib (C++) for n = 30, ..., 45
	n_list = range(30, 46)
	fib_pure_py_timings = []
	fib_numba_py_timings = []
	fib_Cpp_timings = []

	print("Starting timing comparisons for fib_pure_py, fib_numba_py, fib (C++) with n = 30, ..., 45...")
	print("Running n = ", end="")
	for n in n_list:
		print(n, end=" ")

		# Pure python
		start = pc()
		fib_pure_py(n)
		end = pc()
		fib_pure_py_timings.append(end - start)

		# Numba
		start = pc()
		fib_numba_py(n)
		end = pc()
		fib_numba_py_timings.append(end - start)

		# C++
		start = pc()
		f = Integer(n)
		f.fib()
		end = pc()
		fib_Cpp_timings.append(end - start)

	plt.plot(n_list, fib_pure_py_timings, 'r', marker="x")
	plt.plot(n_list, fib_numba_py_timings, 'g', marker="s")
	plt.plot(n_list, fib_Cpp_timings, 'b', marker="v")
	plt.legend(["Pure python", "Numba", "C++"])
	plt.ylabel("time (s)")
	plt.xlabel("n")
	plt.savefig("comparison_pure_numba_Cpp_n_30_45.png")
	plt.clf()

	print("Done with timing comparisons for fib_pure_py, fib_numba_py, fib (C++) with n = 30, ..., 45!\n")

	# Timings for fib_pure_py, fib_numba_py for n = 1, ..., 30
	n_list = range(1, 31)
	fib_pure_py_timings = []
	fib_numba_py_timings = []

	print("Starting timing comparisons for fib_pure_py, fib_numba_py with n = 1, ..., 30...")
	print("Running n = ", end="")
	for n in n_list:
		print(n, end=" ")

		# Pure python
		start = pc()
		fib_pure_py(n)
		end = pc()
		fib_pure_py_timings.append(end - start)

		# Numba
		start = pc()
		fib_numba_py(n)
		end = pc()
		fib_numba_py_timings.append(end - start)

	plt.plot(n_list, fib_pure_py_timings, 'r', marker="x")
	plt.plot(n_list, fib_numba_py_timings, 'g', marker="v")
	plt.legend(["Pure python", "Numba"])
	plt.ylabel("time (s)")
	plt.xlabel("n")
	plt.savefig("comparison_pure_numba_n_1_30.png")

	print("Done with timing comparisons for fib_pure_py, fib_numba_py with n = 1, ..., 30!\n")
		

	# n = 47 Fibonacci number
	print("Starting calculating fib_numba_py, fib (C++) with n = 47...")
	f = Integer(47)
	print(f"Fibonnaci number with fib_numba_py: {fib_numba_py(47)}")
	print(f"Fibonnaci number with fib (C++): {f.fib()}")
	print("Done with calculating fib_numba_py, fib (C++) with n = 47!\n")

if __name__ == '__main__':
	main()


# Fibonnaci number with fib_numba_py: 4807526976
# Fibonnaci number with fib (C++): 512559680
# Why? In C++, the max value for int is 2147483647. Hence, the value
# overflows and returs to the minimum value, which is -2147483647 - 1.
# Hence, the value is much smaller 