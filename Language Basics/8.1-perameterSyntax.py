"""
Positional-Only and Keyword-Only Arguments
Demonstrates the use of `/` and `*` in function definitions in Python.

- `/` makes parameters positional-only.
- `*` makes parameters keyword-only.

These are useful for improving API clarity and preventing misuse.
"""


# `/` and `*`       before / are positional only and after * all are keyword only
def custom_func(a, b, /, c, *, d, e=10):
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

# Valid usages:
custom_func(1, 2, 3, d=4)                
custom_func(1, 2, 3, d=4, e=5)           

# Invalid usages:
# custom_func(a=1, b=2, c=3, d=4)        
# custom_func(1, 2, 3, 4)                
