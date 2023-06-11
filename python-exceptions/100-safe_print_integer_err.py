#!/usr/bin/python3
## Write a function that prints an integer.
import sys
def safe_print_integer_err(value):
	try:
		print("{:d}".format(value))
		return True
	except Exception as error:
		print("Exception: {}".format(error), file=sys.stderr)
		return False
