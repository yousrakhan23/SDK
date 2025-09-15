from agents import function_tool

@function_tool
def plus(n1:int,n2:int)-> str:
    """Returns a string with the sum of n1 and n2.
        arg:
            n1:int
            n2:int
        return str
    """
    return f"Your answer is {n1+n2}"

@function_tool
async def subtract(n1:int,n2:int)-> str:
    """Returns a string with the difference of n1 and n2.
        arg:
            n1:int
            n2:int
        return str
    """
    return f"Your answer is {n1-n2}"


@function_tool
async def multiply(n1:int,n2:int)-> str:
    """Returns a string with the multiplacation of n1 and n2.
        arg:
            n1:int
            n2:int
        return str
    """
    return f"Your answer is {n1*n2}"

@function_tool
async def divide (n1:int,n2:int)-> str:
    """Returns a string with the division of n1 and n2.
        arg:
            n1:int
            n2:int
        return str
    """
    return f"Your answer is {n1/n2}"