#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create a new variable named INTVAL and assign it a value of 1
Create a new variable named FLOATVAL and assign it a value of 0.1
Create a new variable named DECVAL and assign it a value of one-tenth
Create a new variable named FRACVAL and assign it a value of one-tenth

You must import both the decimal and fractions modules to get access
to the Decimal and Fraction data types.
"""
from decimal import Decimal
from fractions import Fraction

INTVAL = 1
FLOATVAL = 0.1
DECVAL = Decimal(1) / Decimal(10)
FRACVAL = Fraction('1/10')

# print DECVAL
