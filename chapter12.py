### 2022 12 15 ### 12:25 ###

#### Chapter 12: Operator Precedence

# Python's operators have a set order of precedence, whic determines what operators are evaluated first in a 
# potentially abiguous expression. For instance, in the expression 3 * 2 + 7, first 3 is multiplied by 2, and then the
# result is added to 7, yielding 13. The expression is not evaluated the other way around, because * has  a higher
# precedence than +.

# Below is a list of operators by precende, and a brief description of what they (usually) do.


## Section 12.1: Simple Operator Precedence Examples in Python

# Python follows PEMDAS rule. PEMDAS stands fro Parentheses, Exponents, Multiplication and Division, and Addition
# and Subtraction.

# Example:
a, b, c, d = 2, 3, 5, 7
a ** (b + c) # parentheses
# 256
a * b ** c # exponent: same as `a * (b ** c)`
7776
a + b * c / d # multiplication / division: same as `a + (b * c / d)` 
4.142857142857142

# Extras: mathematical rules hold, but not always:

300 / 300 * 200
# 200.0
300 * 300 / 300
# 200.0
1e300 / 1e300 * 1e200
# 1e+200
1e300 * 1e200 / 1e300
# inf
