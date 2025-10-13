# The with statement is used in Python for resource management and clean-up actions.

# Think of it as a way to say:

# “I want to use this thing for a short time, and when I’m done, 
# make sure everything is cleaned up properly—no matter what happens.”


class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self  # Optional, can return anything

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with MyContext() as m:
    print("Inside the block")


