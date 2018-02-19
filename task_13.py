#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports values from task 13 to test equality.

.. hint::

    You can access task_12 data in the following example type:

.. code:: python

    print task_12.FLOATVAL

"""

# import task_12
from is210_week3.task_12 import FLOATVAL, DECVAL

FRAC_DEC_EQUAL = DECVAL == FLOATVAL

DEC_FLOAT_INEQUAL = DECVAL != FLOATVAL

print FRAC_DEC_EQUAL

print DEC_FLOAT_INEQUAL
