#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create a new variable named IS_TRUE and assign it a value of True
Create a new variable named IS_FALSE and assign it a value of False
Create a new variabled named IS_NONE and assign it a value of None
In a single, one-line statement, use the logical AND operator and
the equality operator to test if IS_TRUE is equal to 1 and IS_FALSE
is equal to 0 Store the result into a new variable named INTEGER_EQUIV
"""

IS_TRUE = True
IS_FALSE = False
IS_NONE = None

INTEGER_EQUIV = IS_TRUE == 1 and IS_FALSE == 0

print INTEGER_EQUIV # True
