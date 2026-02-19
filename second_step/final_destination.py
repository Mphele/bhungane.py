# final_assessment_v2.py
# Complete the following functions according to their docstrings

from statistics import mean

def inventory_report_generator(inventory_data:list[dict]):
    """
    Generate inventory report aggregating stock and value by category.

    Args:
        inventory_data: List of dicts with keys: category, unit_cost, stock_count

    Returns:
        dict: Keys are categories, values are dicts with total_value and total_stock

    Raises:
        KeyError: If required keys are missing
        ValueError: If unit_cost or stock_count is negative
    """
    final_dict ={}

    for item in inventory_data:

        value = item["unit_cost"]*item["stock_count"]
        if value<0:
            raise ValueError
        
        if item["stock_count"]<0:
            raise ValueError

        if item["category"] not in final_dict:
            
            final_dict[item["category"]] = {"total_value":value, "total_stock": item["stock_count"] }
        
        else:
            final_dict[item["category"]]["total_value"] +=value
            final_dict[item["category"]]["total_stock"]+= item["stock_count"]
        
    return final_dict



def rainfall_analyzer(readings, threshold):
    """
    Analyze rainfall readings against a threshold.

    Args:
        readings: List of rainfall readings (mm)
        threshold: Maximum acceptable rainfall (mm)

    Prints:
        - "No rainfall data" if empty
        - "All readings within threshold" if all <= threshold
        - "Warning: X readings above Y" otherwise
        - "Average: X" (always when data exists, formatted to 2 decimals)
    """

    if not readings:
        print("No rainfall data")
        
    
    elif all(items<=threshold for items in readings):
        print("All readings within threshold")
        print(f"Average: {mean(readings):.2f}")
    
    else:
        oultliers = len([i for i in readings if i>threshold])
        print(f"Warning: {oultliers} readings above {threshold}")
        print(f"Average: {mean(readings):.2f}")






    




def username_validator_with_retry(max_attempts):
    """
    Validate a username with limited retry attempts.

    Args:
        max_attempts: Maximum number of attempts allowed

    Behavior:
        - Prompt "Enter username:" for each attempt
        - Valid username requires: 5-15 chars, only letters, digits, or underscores,
          must start with a letter
        - Print "Invalid username. Try again." for invalid
        - Print "Username accepted!" when valid
        - Print "Maximum attempts reached. Access denied." if exhausted
    """
    
    for _ in range(max_attempts):
        username = input("Enter username:")

        validity = True

        if len(username)>15 or len(username)<5:
            validity = False
            print("Invalid username. Try again.")
            continue

        if not all(char.isalnum() or char== "_" for char in username):
            validity = False
            print("Invalid username. Try again.")
            continue

        if not username[0].isalpha():
            validity = False
            print("Invalid username. Try again.")
            continue


        print("Username accepted!")
        break

    if not validity:
        print("Maximum attempts reached. Access denied.")

# username_validator_with_retry(3)``

def employee_performance_processor(employees):
    """
    Categorize employees by performance rating.

    Args:
        employees: List of dicts with keys: name, scores (list of ints 0-100)

    Returns:
        dict: Keys "high_performers" (avg >= 80) and "needs_improvement" (avg < 80),
              values are lists of dicts with name and average

    Raises:
        KeyError: If required keys are missing
        ValueError: If scores list is empty
    """
    pass





def order_batcher(orders, batch_size):
    """
    Split orders into batches of specified size.

    Args:
        orders: List of orders
        batch_size: Number of orders per batch

    Returns:
        list: List of batches (each batch is a list)

    Raises:
        ValueError: If batch_size < 1
    """
    pass


def social_network_analyzer(network: dict[str, list[str]]):
    """
    Analyze a social network's follow relationships.

    Args:
        network: Dict where keys are users, values are lists of users they follow

    Returns:
        dict with keys:
            - total_follows (int): sum of all follow relationships
            - most_followed (str | None): user who appears most in others' follow lists
            - no_followers (list[str]): users that nobody follows
    """
    pass


def count_vowels(s, count=0):
    """
    Count vowels in a string using RECURSION.

    IMPORTANT: You MUST use recursion. Iterative solutions will fail tests.

    Args:
        s: A string

    Returns:
        int: Number of vowels (a, e, i, o, u — case-insensitive)

    Raises:
        TypeError: If s is not a string
    """
    pass


def text_pipeline_processor(raw_texts, transformations):
    """
    Apply a sequence of transformations to a list of strings.

    Args:
        raw_texts: List of strings
        transformations: List of transformation names

    Available transformations:
        - "uppercase": convert to uppercase
        - "strip": remove leading/trailing whitespace
        - "remove_empty": remove empty strings
        - "reverse": reverse each string

    Returns:
        list: Transformed data

    Raises:
        ValueError: For unknown transformations
    """
    pass


def score_ranker(scores):
    """
    Rank competitors by score with proper tie handling.

    Args:
        scores: List of tuples (competitor_name, score)

    Returns:
        list: List of tuples (competitor_name, score, rank) sorted by score descending.
              Tied competitors share the same rank; the next rank skips accordingly.

    Raises:
        ValueError: If any tuple doesn't have exactly 2 elements
    """
    pass


def fibonacci(n):
    """
    Return the nth Fibonacci number using RECURSION.

    IMPORTANT: You MUST use recursion. Iterative solutions will fail tests.

    Args:
        n: A non-negative integer

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative or not an integer
    """
    pass
