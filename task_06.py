#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Jamel Travis, Week 3, Task_06

A very long book.

Add a new line and, in a single line, split the text with split()
and use len() to count the number of words.
Save the resulting number in a new variable named WORDCT
"""

import os

DPATH = os.path.dirname(os.path.abspath(__file__))

FHANDLER = open(os.path.join(DPATH, 'war_and_peace.txt'), 'r')

WORDS = FHANDLER.read()

FHANDLER.close()

WORDCT = len(WORDS.split(' '))

# print WORDCT