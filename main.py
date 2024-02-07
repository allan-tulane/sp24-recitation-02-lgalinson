"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	if n == 1:
		return 1  # Base case
	else:
        # Compute the value for the floor of n/b to handle non-integer results of division
		return(a * simple_work_calc(int(n/b), a, b) + n)

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if n == 1:
		return 1  # Base case
	else:
		return(a * work_calc(int(n/b), a, b, f) + f(n))

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if n == 1:
		return f(1)  # Assuming f(1) represents the base case work done
	else:
		recursive_span = span_calc(n/b, a, b, f)
		current_work = f(n)
		return recursive_span + current_work




def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1,
			span_fn2
			))
	return result





# TESTS

n = 329
a = 20
b = 2

# Test with f(n) = 1
result_f1 = work_calc(n, a, b, lambda x: 1)
print(f'W({n}) for a={a}, b={b}, f(n)=1: {result_f1}')

# Test with f(n) = log(n)
result_flog = work_calc(n, a, b, lambda x: max(1, int(x.bit_length())))
print(f'W({n}) for a={a}, b={b}, f(n)=log(n): {result_flog}')

# Test with f(n) = n
result_fn = work_calc(n, a, b, lambda x: x)
print(f'W({n}) for a={a}, b={b}, f(n)=n: {result_f1}')


