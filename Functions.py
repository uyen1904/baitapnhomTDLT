def solve_equation(a, b):
    if a == 0:
        if b == 0:
            result = "Infinite solutions (any x satisfies the equation)"
        else:
            result = "No solution (inconsistent equation)"
    else:
        x = -b / a
        result = f"The solution is: x = {x}"
    return result
