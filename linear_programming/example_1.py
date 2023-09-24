# https://realpython.com/linear-programming-python/

# To define and solve optimization problems with SciPy, you need to import
from scipy.optimize import linprog

# Example 1

# objective function -> maximize z = x + 2y

# 2x + y <= 20
# -4x + 5y <= 10
# -x + 2y >= -2
# -x + 5y = 15

# linprog() solves only minimization (not maximization) problems and doesn’t allow inequality constraints
# with the greater than or equal to sign (≥).
# To work around these issues, you need to modify your problem before starting optimization:

# objective function -> minimize -z = -x - 2y

# 2x + y <= 20 - RED
# -4x + 5y <= 10 - BLUE
# x - 2y <= 2 - YELLOW
# -x + 5y = 15 - GREEN

# 1. Define the input values

obj = [-1, -2]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

lhs_ineq = [[ 2,  1],  # Red constraint left side
             [-4,  5],  # Blue constraint left side
             [ 1, -2]]  # Yellow constraint left side

rhs_ineq = [20,  # Red constraint right side
            10,  # Blue constraint right side
             2]  # Yellow constraint right side

lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]       # Green constraint right side

# 2. Define the bounds for each variable
# The next step is to define the bounds for each variable in the same order as the coefficients.
# In this case, they’re both between zero and positive infinity

bnd = [(0, float("inf")),  # Bounds of x
       (0, float("inf"))]  # Bounds of y