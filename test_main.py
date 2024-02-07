from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

	# Additional cases
	assert simple_work_calc(3, 1, 2) == 4
	assert simple_work_calc(16, 2, 4) == 28
	assert simple_work_calc(25, 3, 5) == 49


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300

    # Additional cases
	assert work_calc(5, 2, 2, lambda n: n + 10) == 43
	assert work_calc(15, 2, 3, lambda n: 2*n) == 54
	assert work_calc(25, 1, 5, lambda n: n//2) == 15


def test_compare_work():
	# Parameters for the recurrence
    a, b = 2, 2
    c1, c2 = 0.5, 1.5 
    
    work_fn1 = lambda n: work_calc(n, a, b, lambda n: n**c1)
    work_fn2 = lambda n: work_calc(n, a, b, lambda n: n**c2)
    
    # Compare the work functions for different n sizes
    res = compare_work(work_fn1, work_fn2)
    
    # Print the comparison results
    for result in res:
        print(f"n={result[0]}: Work1={result[1]}, Work2={result[2]}")

	
def test_compare_span():
	a, b = 2, 2  
	c1, c2 = 0.5, 1.5  
    
	span_fn1 = lambda n: span_calc(n, a, b, lambda n: n**c1)
	span_fn2 = lambda n: span_calc(n, a, b, lambda n: n**c2)
    
    # Compare the spans for different n sizes
	res = compare_span(span_fn1, span_fn2)
    
    # Print the comparison results
	for result in res:
		print(f"n={result[0]}: Span1={result[1]}, Span2={result[2]}")

