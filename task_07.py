#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question.
Use the in operator to test whether or not the word
granaries exists within the WORDS variable
Save the result into a variable named GRANARIES_EXIST
"""

from is210_week3 import task_06

WORDS = task_06.WORDS

GRANARIES_EXIST = 'granaries' in WORDS

print GRANARIES_EXIST
