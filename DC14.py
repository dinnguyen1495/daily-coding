# Daily Coding 14:
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random
import math

def monte_carlos(N):
    total_count = N
    # total_sample = np.random.uniform(low = 0, high = 1, size = (total_count, 2))
    # inside_sample = [(x, y) for (x, y) in total_sample if x**2 + y**2 <= 1]
    # inside_count = len(inside_sample)
    while True:
        inside_count = 0
        for i in range(total_count):
            if math.hypot(random.uniform(0, 1), random.uniform(0, 1)) <= 1:
                inside_count += 1
        estimator = round(inside_count * 4 / total_count, 3)
        if abs(math.pi - estimator) < 1e-3:
            return estimator
            break

def main():
    N = 30000
    print("Pi estimator with N = %i: %.3f" %(N, monte_carlos(N)))

if __name__ == "__main__":
    main()