# https://realpython.com/linear-programming-python/

# To define and solve optimization problems with SciPy, you need to import
from scipy.optimize import linprog

import numpy as np
import matplotlib.pyplot as plt
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

# 3. Optimize and Solve the problem
# c - refers to the coefficients from the objective function
# A_ub - refers to the left side coefficients from the inequality constraints
# b_ub - refers to the right side coefficients from the inequality constraints
# A_eq - refers to the left side coefficients from the equality constraints
# b_eq - refers to the right side coefficients from the equality constraints
# bounds - refers to the bounds of the x and y variables/lower and upper bounds on the decision variables
# method - refers to the algorithm that SciPy uses to solve the problem

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
               A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
               method="revised simplex")

# 4. Print the results
print(opt.success)

# .fun is the objective function value at the optimum (if found).
print(opt.fun)

# is a NumPy array holding the optimal values of the decision variables
print(opt.x)

# 5. Plot the results

# Generate a range of values for x
x = np.linspace(0, 20, 400)

# Calculate the boundary of each inequality based on the values of x
y1 = 20 - 2*x
y2 = (10 + 4*x) / 5
y3 = (x + 2) / 2
y4 = (15 + x) / 5

# Plot the inequalities
plt.plot(x, y1, label=r'$2x + y \leq 20$', color='red')
plt.fill_between(x, 0, y1, where=(y1>0), color='red', alpha=0.3)

plt.plot(x, y2, label=r'$-4x + 5y \leq 10$', color='blue')
plt.fill_betweenx(x, x, (10 + 4*x) / 5, where=(x<((10 + 4*x) / 5)), color='blue', alpha=0.3)

plt.plot(x, y3, label=r'$x - 2y \leq 2$', color='yellow')
plt.fill_betweenx(x, 0, (x + 2) / 2, color='yellow', alpha=0.3)

plt.axhline(y=3, color='green', label=r'$-x + 5y = 15$')

# Plot the optimal solution
plt.scatter(opt.x[0], opt.x[1], color='black', marker='o', label='Optimal Solution')

# Adjust plot settings
plt.xlim((0, 20))
plt.ylim((0, 20))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axvline(0, color='black',linewidth=0.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()