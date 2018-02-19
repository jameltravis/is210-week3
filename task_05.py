#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Jamel Travis, Week 3, task_05.

Splinter would be proud.

Use the string .split() program to split up the TEENAGE_MUTANT_NINJAS
variable using a period + space '. ' as the delimiter.
Save the result into a new variable named TURTLE_POWER
"""


TEENAGE_MUTANT_NINJAS = ('Michaelangelo. Leonardo. Rafael. Donatello. Heroes '
                         'in a half shell.')

TURTLE_POWER = TEENAGE_MUTANT_NINJAS.split('. ')

print TURTLE_POWER
