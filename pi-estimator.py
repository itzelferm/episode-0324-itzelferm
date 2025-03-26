import sys

DEFAULT_TOTAL = 1000

total_darts = DEFAULT_TOTAL
if len(sys.argv) > 1:
    total_darts = int(sys.argv[1])
print(f"Total darts: {total_darts}")

for i in range(total_darts):
    print(i)