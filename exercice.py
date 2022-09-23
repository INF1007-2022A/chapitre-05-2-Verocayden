#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	price_before_tx = 0.00
	tx = 0.00
	price_after_tx = 0.00

	for object in data:
		price_before_tx += object[INDEX_QUANTITY] * object[INDEX_PRICE]
	tx = 0.15 * price_before_tx
	price_after_tx = price_before_tx + tx

	price_before_tx = "{:.2f}".format(price_before_tx, 2)
	tx = "{:.2f}".format(tx, 2)
	price_after_tx = "{:.2f}".format(price_after_tx, 2)

	bill = f"""
	{f"{name}": <20}\n
	{"SOUS-TOTAL": <10}  {f"{price_before_tx} $":>20}
	{"TAXES": <10}  {f"{tx} $":>20}
	{"TOTAL": <10}  {f"{price_after_tx} $":>20}
		   """


	return bill


def format_number(number, num_decimal_digits):

	str_number = str(round(number, num_decimal_digits))[::-1] # Invert string and round.
	format_number = ""

	count = 0

	for i in str_number:
		if i == "-":
			format_number += i
		elif i == ".":
			format_number += i
			count = 0
		elif count == 3:
			format_number += " " + i
			count = 0
		elif count != 3:
			format_number += i
			count += 1

	format_number = format_number[::-1]

	new_number = "" # Without space after the "."
	for i in format_number:
		if i != ".":
			new_number += i
		elif i == ".":
			for i in format_number[format_number.find(".")::]:
				if i != " ":
					new_number += i
			break

	return new_number

def get_triangle(num_rows):
	max_A_number = 2*num_rows-1+2
	A_format = "A"
	triangle = ""
	count = 0

	border_row = ""
	for i in range(max_A_number):
		border_row += "+"
	triangle += f"{border_row}\n" # Top row

	for i in range(num_rows): # Add rows with A
		count += 1
		space = " " * (num_rows-count)
		triangle += "+" + space + A_format + space + "+\n"
		A_format += 'AA'

	triangle += f"{border_row}\n" # Bottom row

	return triangle


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.6789, 4))

	print(get_triangle(2))
	print(get_triangle(5))
