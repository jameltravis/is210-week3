#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The cat must have slept on the keyboard!!!

Strip this terribly formatted string of its excess characters.

Use the strip() function to remove whitespace from NERVOUS_AS
and save the result back into the NERVOUS_AS variable
In a single-line statement, use rstrip() and lstrip()
to remove the commas (,), and forward slashes (/) from
NERVOUS_AS storing the result back into the NERVOUS_AS variable.
Note

Depending upon what a function returns, it is possible to chain
together multiple function calls as a form of shorthand. This is
possible because these functions either return the original object
or an object of the exact same time (eg, a string) so subsequenct
.function() calls may be strung together one after another.
"""


NERVOUS_AS = """




 //////////A long-tailed cat in a room full of rockin' chairs.,,,,,,,,,, 





"""
NERVOUS_AS = NERVOUS_AS.replace('"""', "'")

NERVOUS_AS = NERVOUS_AS.strip().lstrip('/').rstrip(',')

# print NERVOUS_AS
