#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for string and integer conversion.
Concatenate the variables NOT_THE_QUESTION and ANSWER by using the
concatenation operator and the str() function.
Store the result into a new variable named THANKS_FOR_THE_FISH
"""


NOT_THE_QUESTION = 'The answer to life, the universe, and everything? It\'s '
ANSWER = 42

THANKS_FOR_THE_FISH = NOT_THE_QUESTION + str(ANSWER)

print THANKS_FOR_THE_FISH
