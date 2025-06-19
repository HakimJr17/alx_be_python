# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, handling potential ZeroDivisionError
    and ValueError for non-numeric inputs.

    Args:
        numerator: The top number in the division.
        denominator: The bottom number in the division.

    Returns:
        A string indicating the result of the division or an error message.
    """
    try:
        # Attempt to convert both inputs to float.
        # This will raise a ValueError if inputs are non-numeric.
        num = float(numerator)
        den = float(denominator)

        # Perform the division.
        # This will raise a ZeroDivisionError if denominator is zero.
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # Catch and handle division by zero error
        return "Error: Cannot divide by zero."
    except ValueError:
        # Catch and handle non-numeric input error
        return "Error: Please enter numeric values only."