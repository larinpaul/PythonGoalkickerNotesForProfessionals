### 2022 14 12 ### 13:25 ###
#### Chapter 11: Boolean Operations

## Section 11.1: `and` and `or` are not guaranteed to return a boolean

# When you use or, it will either return the first value in the expression if it's true, else it will blindly return the second
# value. I.e. or is equivalent to:
def or_(a, b):
    if a:
        return a
    else:
        return b
  
 # For and, it will return its first value if it's false, else it returns the last value:
def and_(a, b):
    if not a:
        return a
    else:
        return b

 
## Section 11.2: A simple example
# In Python you can compare a single element using two binary operators-- one on either side:
if 3.14 < x < 3.142:
    print("x is near pi")
# In many (most?) programming languages, this would be evaluated in a way contrary to regular math: (3.14 < x) < 3.142,
# but in Python it is treated like 3.14 < x and x < 3.142, just like most non-programmers would expect.


## Section 11.3: Short-circuit evaluation

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"


