#!/usr/bin/env python3

from integer import Integer
import time.perf_counter as pc

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
		f = Integer(i)
		print(f.fib())
		end = pc()
		fib_pure_py_timings.append(end - start)

		# Numba
		print(n)


		# C++

	print("Done with timing comparisons for fib_pure_py, fib_numba_py, fib (C++) with n = 30, ..., 45!\n")

	# Timings for fib_pure_py, fib_numba_py for n = 1, ..., 30
	print("Starting timing comparisons for fib_pure_py, fib_numba_py with n = 1, ..., 30...")
	for i in range(10):


	print("Done with timing comparisons for fib_pure_py, fib_numba_py with n = 1, ..., 30!\n")
		

	# n = 47 Fibonacci number
	print("Starting calculating fib_numba_py, fib (C++) with n = 47...")

	print("Done with calculating fib_numba_py, fib (C++) with n = 47!\n")

if __name__ == '__main__':
	main()