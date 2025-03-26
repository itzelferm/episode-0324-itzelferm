import sys
import random

DEFAULT_TOTAL = 1000

total_darts = DEFAULT_TOTAL
if len(sys.argv) > 1:
    total_darts = int(sys.argv[1])
print(f"Total darts: {total_darts}")

total_inside_darts = 0
for i in range(total_darts):
    x = random.random()
    y = random.random()

    if x * x + y * y <= 1:
        total_inside_darts += 1
print(f"Inside darts : {total_inside_darts}, total darts: {total_darts}")

pi_estimator = 4 * total_inside_darts/total_darts
print(f"The π estimate is: {pi_estimator}")