#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Jamel Travis, Week 3 assignment (task_02).

Create a variable named WEEKS and, in a single statement:
Calculate the remainder of 19 divided by 10
Add the result to 100
Add that result to 2^8 (do exponentiation in Python!)
Divide all of the above by 7
"""

# I took advantage of Python having
# order of operations built in.
WEEKS = (19 % 10 + 100 + 2 ** 8) / 7
# print WEEKS