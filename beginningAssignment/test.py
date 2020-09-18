from multiprocessing import *
import numpy as np
import time

def f(x):
	y = x * x
	return y

def main():
	t1 = time.time()
	l = np.arange(0, 10000000)
	p = Pool(2)
	n = p.map(f, l)
	
	t2 = time.time()
	print('diff: %.2f' % (t2-t1))


if __name__ == '__main__':
	main()
