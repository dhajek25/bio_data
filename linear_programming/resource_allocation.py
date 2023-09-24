from scipy.optimize import linprog

import numpy as np
import matplotlib.pyplot as plt

# Resource Allocation
# maximase profit -> 20x1 + 12x2 + 40x3 + 25x4
# manpower -> x1 + x2 + x3 + x4 <= 50
# material A -> 3x1 + 2x2 + x3 <= 100
# material B -> x2 + 2x3 + 3x4 <= 90
# x1, x2, x3, x4 >= 0

# 1. Define the input values
obj = [-20, -12, -40, -25]

lhs_ineq = [[1, 1, 1, 1],  # Manpower
            [3, 2, 1, 0],  # Material A
            [0, 1, 2, 3]]  # Material B

rhs_ineq = [ 50,  # Manpower
            100,  # Material A
             90]  # Material B

# 2. Define the bounds for each variable
# Definitoi of bounds is redundant because linprog() takes these bounds (zero to positive infinity) by default.

# 3. Optimize and Solve the problem
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="revised simplex")

# 4. Print the results
print(opt.success)

# .fun is the objective function value at the optimum (if found).
# The maximum profit is 1900
print(opt.fun)

# is a NumPy array holding the optimal values of the decision variables
# Maximum profit is achieved when x1 = 5, x2 = 0, x3 = 45, x4 = 0
print(opt.x)

# The first slack is 0, which means that the values of the left and right sides of the manpower
# (first) constraint are the same. The factory produces 50 units per day, and that’s its full capacity.

# The second slack is 40 because the factory consumes 60 units of raw material A
# (15 units for the first product plus 45 for the third) out of a potential 100 units.

# The third slack is 0 because the factory consumes 90 units of raw material B
# (45 units for the second product plus 45 for the third) out of a potential 90 units.
#
print(opt.slack)

