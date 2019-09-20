import itertools
import sys
import time
import random

light_colors = ['Green', 'Yellow', 'Red']
light_iter = itertools.cycle(light_colors)

while True:
   sys.stdout.write('\r      ')
   sys.stdout.flush()
   sys.stdout.write('\r' + next(light_iter))
   sys.stdout.flush()
   time.sleep(random.randrange(3,11))
