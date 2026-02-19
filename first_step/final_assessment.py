# final_assessment.py
# Complete the following functions according to their docstrings
import statistics


def sales_report_generator(sales_data):
    """
    Generate sales report aggregating revenue and units by product.

    Args:
        sales_data: List of dicts with keys: product, price, quantity

    Returns:
        dict: Keys are products, values are dicts with total_revenue and units_sold

    Raises:
        KeyError: If required keys are missing
        ValueError: If price or quantity is negative
    """
    
    new_dict = {}

    for item in sales_data:
        if item["price"]<0:
            raise ValueError
        item_revenue = item["price"]*item["quantity"]
        if item["product"] not in new_dict:
            new_dict[item["product"]] = {"total_revenue":item_revenue,
                                          "units_sold":item["quantity"]}
        else:
             new_dict[item["product"]]["total_revenue"]+=item_revenue
             new_dict[item["product"]]["units_sold"]+=item["quantity"]
    
    return new_dict



def temperature_analyzer(temperatures, threshold):
    """
    Analyze temperature readings against a threshold.

    Args:
        temperatures: List of temperature readings
        threshold: Minimum acceptable temperature

    Prints:
        - "No temperature data" if empty
        - "All temperatures above threshold" if all >= threshold
        - "Warning: X readings below Y" otherwise
        - "Average: X" (always, formatted to 2 decimals)
    """
    
    if not temperatures:
        print("No temperature data")
        
    
    elif all(temps>=threshold for temps in temperatures):
        print("All temperatures above threshold")
        average = statistics.mean(temperatures)
        print(f"Average: {average:.2f}")
    
    else:
        belowers = len([temp for temp in temperatures if temp<threshold])
        print(f"Warning: {belowers} readings below {threshold}")
        average = statistics.mean(temperatures)
        print(f"Average: {average:.2f}")

    




def password_validator_with_retry(max_attempts):
    """
    Validate password with limited retry attempts.

    Args:
        max_attempts: Maximum number of attempts allowed

    Behavior:
        - Prompt "Enter password:" for each attempt
        - Valid password requires: 8+ chars, upper, lower, digit, special (!@#$%^&*)
        - Print "Invalid password. Try again." for invalid
        - Print "Password accepted!" when valid
        - Print "Maximum attempts reached. Account locked." if exhausted
    """
    
    for _ in range(max_attempts):
        password = input("Enter password:")

        validity = True

        if len(password)<8:
            validity = False
            print("Invalid password. Try again.")
            continue

        if not any(char.isupper() for char in password):
            validity = False
            print("Invalid password. Try again.")
            continue

        if not any(char.islower() for char in password):
            validity = False
            print("Invalid password. Try again.")
            continue

        if not any(char.isdigit() for char in password):
            validity = False
            print("Invalid password. Try again.")
            continue

        if not any(char in '!@#$%^&*' for char in password):
            validity = False
            print("Invalid password. Try again.")
            continue

        print("Password accepted!")
        break

    if not validity:
        print("Maximum attempts reached. Account locked.")





def student_grade_processor(students):
    """
    Categorize students by passing/failing status with averages.

    Args:
        students: List of dicts with keys: name, grades (list)

    Returns:
        dict: Keys "passing" and "failing", values are lists of dicts with name and average

    Raises:
        KeyError: If required keys missing
        ValueError: If grades list is empty
    """

    classification = {'passing':[], 'failing':[]}

    for student in students:
        if not student["grades"]:
            raise ValueError
        student_average = statistics.mean(student["grades"])
        if student_average>=60:
            classification["passing"].append({"name":student["name"], 'average':student_average})
        else:
            classification["failing"].append({"name":student["name"], 'average':student_average})
        
    
    return classification




def transaction_batcher(transactions, batch_size):
    """
    Split transactions into batches of specified size.

    Args:
        transactions: List of transactions
        batch_size: Number of transactions per batch

    Returns:
        list: List of batches (each batch is a list)

    Raises:
        ValueError: If batch_size < 1
    """
    
    if not transactions:
        return []
    
    if batch_size<1:
        raise ValueError
    
    larger = []
    smaller = []
    for item in transactions:
        if len(smaller)==batch_size:
            larger.append(smaller)
            smaller=[]
        smaller.append(item)
    
    if smaller:
        larger.append(smaller)
    
    return larger


def network_graph_analyzer(network: dict[str, list[str]]):
    """
    Analyze network connectivity statistics.

    Args:
        network: Dict where keys are nodes, values are lists of connected nodes

    Returns:
        dict: Keys are total_connections, most_connected, isolated_nodes
    """

    if not network:
        return {"total_connections": 0, "most_connected": None, "isolated_nodes": []}
    
    total_cons = 0
    isolated = []
    node_to_con ={}

    for node, connections in network.items():
        total_cons+= len(connections)
        if not connections:
            isolated.append(node)
        
        node_to_con[node]=len(connections)
    
    most_connected = list(dict(sorted(network.items(), reverse=True, key=lambda item:item[1])))[0]
    return {"total_connections": total_cons, "most_connected": most_connected, "isolated_nodes":isolated}

        



    


def sum_of_digits(n):
    """
    Calculate sum of digits using RECURSION.

    IMPORTANT: You MUST use recursion. Iterative solutions will fail tests.

    Args:
        n: A non-negative integer

    Returns:
        int: Sum of all digits

    Raises:
        ValueError: If n is negative or not an integer
    """

    if not isinstance(n, int) or n<0:
        raise ValueError
    
    if n ==0:
        return 0
    
    else:
        return (n%10)+ sum_of_digits(n//10)



def data_pipeline_processor(raw_data, transformations):
    """
    Apply sequence of transformations to data.

    Args:
        raw_data: List of numbers
        transformations: List of transformation names

    Available transformations:
        - "double": multiply by 2
        - "add_ten": add 10
        - "filter_even": keep only even numbers
        - "square": square each number

    Returns:
        list: Transformed data

    Raises:
        ValueError: For unknown transformations
    """
    pass


def leaderboard_ranker(scores):
    """
    Rank players by score with proper tie handling.

    Args:
        scores: List of tuples (player_name, score)

    Returns:
        list: List of tuples (player_name, score, rank) sorted by score descending

    Raises:
        ValueError: If tuple doesn't have exactly 2 elements
    """
    pass


def smart_cache_system(capacity):
    """
    Create an LRU (Least Recently Used) cache system.

    IMPORTANT: You MUST implement this using a class.

    Args:
        capacity: Maximum number of items in cache

    Returns:
        Cache object with methods:
            - put(key, value): Add/update item
            - get(key): Retrieve item (returns None if not found)

    Raises:
        ValueError: If capacity < 1

    LRU Behavior:
        - When full, evict least recently used item
        - get() and put() mark items as recently used
    """
    pass
