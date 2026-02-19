# final_assessment_v2.py
# Complete the following functions according to their docstrings

from collections import Counter
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

def employee_performance_processor(employees: list[dict[str:list]]):
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

    final = {"high_performers":[], "needs_improvement": []}

    for employee in employees:
        name, scores = employee["name"], employee["scores"]

        average = mean(scores)

        if average>=80:
            final["high_performers"].append({"name":name, "average":round(average,2)})
        else:
            final["needs_improvement"].append({"name":name, "average":round(average,2)})
    
    return final


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

    if not orders:
        return []
    
    if batch_size<1:
        raise ValueError
    
    wrapper = []
    batch = []

    for item in orders:

        batch.append(item)

        if len(batch)==batch_size:
            wrapper.append(batch)
            batch =[]
        
       
    
    if batch:
        wrapper.append(batch)
    
    return wrapper

print(order_batcher(["O1", "O2", "O3", "O4", "O5"],
        2))

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

    if all(lists ==[] for person, lists in network.items()):
        return {"total_follows": 0, "most_followed": None, "no_followers": [person for person, lists in network.items()]}
    
    total_follows = 0
    follows = []
    no_follow = []


    for person, following in network.items():
        total_follows+=len(following)
        follows.extend(following)
    
    follow_count = Counter(follows)
    sorted_follow = sorted(follow_count.items(), key=lambda item:item[1], reverse=True)
    most_followed = sorted_follow[0][0]
    
    for name in network.keys():
        if name not in follow_count:
            no_follow.append(name)
    
    return {"total_follows": total_follows, "most_followed": most_followed, "no_followers":no_follow}


social_network_analyzer({
    "Alice": ["Bob", "Carol"],
    "Bob":   ["Carol"],
    "Carol": [],
})
    



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
    
    vowels = "AEIOUaeiou"
    if not isinstance(s, str):
        raise TypeError
    
    if not s:
        return 0
    
    if s[0] in vowels:
        return 1+ count_vowels(s[1:])
    else:
         return count_vowels(s[1:])

    


def text_pipeline_processor(raw_texts:list[str], transformations):
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
    
    if not all(word in ["uppercase", "strip", "remove_empty", "reverse"] for word in transformations ):
        raise ValueError
    
    edited = raw_texts.copy()
    for trans in transformations:
        if trans == "uppercase":
            edited = [word.upper() for word in edited]
        
        elif trans =="strip":
            edited = [word.strip() for word in edited]
        
        elif trans =="remove_empty":
            edited = [word for word in edited if word]
        
        else:
            edited = [word[::-1] for word in edited]
    
    return edited


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
    if not scores:
        return []
    rank = 1
    count =1
    last_score = 0
    with_rank =[]
    dict_scores = dict(scores)
    sorted_scores = sorted(dict_scores.items(), reverse=True, key = lambda item:item[1])

    last_score = sorted_scores[0][0]

    for person in sorted_scores:
        name, score = person

        if score!=last_score:
            rank = count

        last_score = score
        with_rank.append((name, score, rank))
        count+=1
    
    return with_rank
        





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
    
    if n in [0,1]:
        return n
    
    if n<0 or not isinstance(n, int):
        raise ValueError
    
    return fibonacci(n-1) + fibonacci(n-2)

def reverse_string(s):

    if not s:
        return []
    
    return [s[-1]] + reverse_string(s[:-1])


import math

n =5

pascal = [[math.comb(row, col) for col in range(row+1)] for row in range(n)]
print(pascal)