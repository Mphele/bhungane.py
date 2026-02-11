import pytest
from final_assessment import *
from unittest.mock import patch
from io import StringIO
import sys

# Question 1 - Sales Report Generator

@pytest.mark.parametrize("sales_data, expected_output", [
    (
        [
            {"product": "Laptop", "price": 1000, "quantity": 2},
            {"product": "Mouse", "price": 25, "quantity": 5},
            {"product": "Laptop", "price": 1000, "quantity": 1}
        ],
        {"Laptop": {"total_revenue": 3000, "units_sold": 3}, "Mouse": {"total_revenue": 125, "units_sold": 5}}
    ),
    ([], {}),
    (
        [{"product": "Keyboard", "price": 50, "quantity": 10}],
        {"Keyboard": {"total_revenue": 500, "units_sold": 10}}
    ),
])
def test_sales_report_generator_logic(sales_data, expected_output):
    assert sales_report_generator(sales_data) == expected_output

def test_sales_report_generator_missing_keys():
    with pytest.raises(KeyError):
        sales_report_generator([{"product": "Test", "price": 10}])

def test_sales_report_generator_negative_values():
    with pytest.raises(ValueError):
        sales_report_generator([{"product": "Test", "price": -10, "quantity": 5}])

def test_sales_report_generator_large_dataset():
    data = [{"product": f"Product_{i % 100}", "price": 10, "quantity": 1} for i in range(10000)]
    result = sales_report_generator(data)
    assert len(result) == 100
    assert result["Product_0"]["units_sold"] == 100

def test_sales_report_generator_duplicate_products():
    data = [
        {"product": "Phone", "price": 500, "quantity": 2},
        {"product": "Phone", "price": 500, "quantity": 3}
    ]
    assert sales_report_generator(data) == {"Phone": {"total_revenue": 2500, "units_sold": 5}}

def test_sales_report_generator_mixed_products():
    data = [
        {"product": "A", "price": 100, "quantity": 1},
        {"product": "B", "price": 200, "quantity": 2},
        {"product": "A", "price": 100, "quantity": 2}
    ]
    result = sales_report_generator(data)
    assert result["A"]["total_revenue"] == 300
    assert result["B"]["total_revenue"] == 400

# ------------------------------------------------------------------------------------------ #

# Question 2 - Temperature Analyzer

def test_temperature_analyzer_all_above_threshold():
    temps = [25, 30, 28, 32]
    captured = StringIO()
    sys.stdout = captured
    temperature_analyzer(temps, 20)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "All temperatures above threshold" in output
    assert "Average: 28.75" in output

def test_temperature_analyzer_some_below_threshold():
    temps = [15, 25, 18, 30]
    captured = StringIO()
    sys.stdout = captured
    temperature_analyzer(temps, 20)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Warning: 2 readings below 20" in output
    assert "Average: 22.00" in output

def test_temperature_analyzer_all_below_threshold():
    temps = [10, 12, 8]
    captured = StringIO()
    sys.stdout = captured
    temperature_analyzer(temps, 15)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Warning: 3 readings below 15" in output

def test_temperature_analyzer_empty_list():
    captured = StringIO()
    sys.stdout = captured
    temperature_analyzer([], 20)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "No temperature data" in output

def test_temperature_analyzer_exact_threshold():
    temps = [20, 20, 20]
    captured = StringIO()
    sys.stdout = captured
    temperature_analyzer(temps, 20)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "All temperatures above threshold" in output

def test_temperature_analyzer_negative_temps():
    temps = [-5, 0, 5, 10]
    captured = StringIO()
    sys.stdout = captured
    temperature_analyzer(temps, 0)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Warning: 1 readings below 0" in output

# ------------------------------------------------------------------------------------------ #

# Question 3 - Password Validator with Retry

def test_password_validator_valid_first_try(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('ValidP@ss123\n'))
    captured = StringIO()
    sys.stdout = captured
    password_validator_with_retry(3)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Password accepted!" in output

def test_password_validator_max_attempts_exceeded(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('weak\nweak\nweak\n'))
    captured = StringIO()
    sys.stdout = captured
    password_validator_with_retry(3)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Maximum attempts reached" in output
    assert output.count("Enter password:") == 3

def test_password_validator_valid_on_last_attempt(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('weak\nweak\nValidP@ss1\n'))
    captured = StringIO()
    sys.stdout = captured
    password_validator_with_retry(3)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Password accepted!" in output
    assert output.count("Enter password:") == 3

def test_password_validator_various_weak_passwords(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('short\nNOUPPER123!\nnodigits!\nSecure123!\n'))
    captured = StringIO()
    sys.stdout = captured
    password_validator_with_retry(5)
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Password accepted!" in output

# ------------------------------------------------------------------------------------------ #

# Question 4 - Student Grade Processor

@pytest.mark.parametrize("students, expected_output", [
    (
        [
            {"name": "Alice", "grades": [85, 90, 88]},
            {"name": "Bob", "grades": [55, 60, 58]}
        ],
        {"passing": [{"name": "Alice", "average": 87.67}], "failing": [{"name": "Bob", "average": 57.67}]}
    ),
    (
        [{"name": "Charlie", "grades": [70, 75, 80]}],
        {"passing": [{"name": "Charlie", "average": 75.0}], "failing": []}
    ),
    ([], {"passing": [], "failing": []}),
])
def test_student_grade_processor_logic(students, expected_output):
    result = student_grade_processor(students)
    # Round averages for comparison
    for category in ["passing", "failing"]:
        for student in result[category]:
            student["average"] = round(student["average"], 2)
    for category in ["passing", "failing"]:
        for student in expected_output[category]:
            student["average"] = round(student["average"], 2)
    assert result == expected_output

def test_student_grade_processor_exact_pass_mark():
    students = [{"name": "Test", "grades": [60, 60, 60]}]
    result = student_grade_processor(students)
    assert len(result["passing"]) == 1
    assert result["passing"][0]["name"] == "Test"

def test_student_grade_processor_mixed_grades():
    students = [
        {"name": "Pass1", "grades": [80, 85, 90]},
        {"name": "Fail1", "grades": [40, 45, 50]},
        {"name": "Pass2", "grades": [65, 70, 75]}
    ]
    result = student_grade_processor(students)
    assert len(result["passing"]) == 2
    assert len(result["failing"]) == 1

def test_student_grade_processor_empty_grades():
    with pytest.raises(ValueError):
        student_grade_processor([{"name": "Test", "grades": []}])

def test_student_grade_processor_missing_keys():
    with pytest.raises(KeyError):
        student_grade_processor([{"name": "Test"}])

# ------------------------------------------------------------------------------------------ #

# Question 5 - Transaction Batcher

@pytest.mark.parametrize("transactions, batch_size, expected_batches", [
    (
        ["T1", "T2", "T3", "T4", "T5", "T6", "T7"],
        3,
        [["T1", "T2", "T3"], ["T4", "T5", "T6"], ["T7"]]
    ),
    (
        ["A", "B", "C", "D"],
        2,
        [["A", "B"], ["C", "D"]]
    ),
    ([], 5, []),
])
def test_transaction_batcher_logic(transactions, batch_size, expected_batches):
    assert transaction_batcher(transactions, batch_size) == expected_batches

def test_transaction_batcher_large_dataset():
    transactions = [f"TXN{i}" for i in range(10000)]
    result = transaction_batcher(transactions, 100)
    assert len(result) == 100
    assert all(len(batch) == 100 for batch in result)

def test_transaction_batcher_single_batch():
    assert transaction_batcher(["A", "B"], 5) == [["A", "B"]]

def test_transaction_batcher_invalid_batch_size():
    with pytest.raises(ValueError):
        transaction_batcher(["A", "B"], 0)

def test_transaction_batcher_preserve_order():
    transactions = ["First", "Second", "Third", "Fourth", "Fifth"]
    result = transaction_batcher(transactions, 2)
    assert result[0][0] == "First"
    assert result[-1][-1] == "Fifth"

# ------------------------------------------------------------------------------------------ #

# Question 6 - Network Graph Analyzer

@pytest.mark.parametrize("network, expected_stats", [
    (
        {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]},
        {"total_connections": 6, "most_connected": "A", "isolated_nodes": []}
    ),
    (
        {"X": ["Y"], "Y": [], "Z": []},
        {"total_connections": 1, "most_connected": "X", "isolated_nodes": ["Y", "Z"]}
    ),
    ({}, {"total_connections": 0, "most_connected": None, "isolated_nodes": []}),
])
def test_network_graph_analyzer_logic(network, expected_stats):
    result = network_graph_analyzer(network)
    # Handle case where multiple nodes have same max connections
    if expected_stats["most_connected"] is not None:
        assert result["most_connected"] in [node for node, conns in network.items() if len(conns) == max(len(c) for c in network.values())]
    else:
        assert result["most_connected"] is None
    assert result["total_connections"] == expected_stats["total_connections"]
    assert set(result["isolated_nodes"]) == set(expected_stats["isolated_nodes"])

def test_network_graph_analyzer_single_node():
    network = {"Node1": []}
    result = network_graph_analyzer(network)
    assert result["total_connections"] == 0
    assert result["isolated_nodes"] == ["Node1"]

def test_network_graph_analyzer_all_connected():
    network = {"A": ["B"], "B": ["A"]}
    result = network_graph_analyzer(network)
    assert result["isolated_nodes"] == []

def test_network_graph_analyzer_hub_network():
    network = {"Hub": ["A", "B", "C", "D"], "A": [], "B": [], "C": [], "D": []}
    result = network_graph_analyzer(network)
    assert result["most_connected"] == "Hub"
    assert len(result["isolated_nodes"]) == 4

# ------------------------------------------------------------------------------------------ #

# Question 7 - Sum of Digits (Recursive)

@pytest.mark.parametrize("n, expected_sum", [
    (123, 6),
    (0, 0),
    (9, 9),
    (1234, 10),
    (999, 27),
    (10000, 1),
])
def test_sum_of_digits_logic(n, expected_sum):
    assert sum_of_digits(n) == expected_sum

def test_sum_of_digits_large_number():
    assert sum_of_digits(123456789) == 45

def test_sum_of_digits_negative_number():
    with pytest.raises(ValueError):
        sum_of_digits(-123)

def test_sum_of_digits_non_integer():
    with pytest.raises(ValueError):
        sum_of_digits(12.34)

def test_is_recursion_implemented():
    with patch("final_assessment.sum_of_digits", wraps=sum_of_digits) as mocked:
        mocked(123)
        assert mocked.call_count > 1, "Recursion not detected"

def test_recursion_base_case():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5

def test_recursion_parameters():
    with patch("final_assessment.sum_of_digits", wraps=sum_of_digits) as mocked:
        mocked(456)
        for call in mocked.call_args_list:
            args, _ = call
            assert len(args) == 1
            assert isinstance(args[0], int)

# ------------------------------------------------------------------------------------------ #

# Question 8 - Data Pipeline Processor

@pytest.mark.parametrize("raw_data, transformations, expected_output", [
    (
        [1, 2, 3, 4, 5],
        ["double", "filter_even"],
        [2, 4, 6, 8, 10]
    ),
    (
        [10, 15, 20, 25],
        ["add_ten", "filter_even"],
        [20, 30]
    ),
    (
        [1, 2, 3],
        [],
        [1, 2, 3]
    ),
])
def test_data_pipeline_processor_logic(raw_data, transformations, expected_output):
    assert data_pipeline_processor(raw_data, transformations) == expected_output

def test_data_pipeline_processor_empty_data():
    assert data_pipeline_processor([], ["double"]) == []

def test_data_pipeline_processor_unknown_transformation():
    with pytest.raises(ValueError):
        data_pipeline_processor([1, 2, 3], ["unknown_transform"])

def test_data_pipeline_processor_multiple_transforms():
    result = data_pipeline_processor([1, 2, 3, 4], ["double", "add_ten", "filter_even"])
    assert result == [12, 14, 16, 18]

def test_data_pipeline_processor_square_transform():
    result = data_pipeline_processor([2, 3, 4], ["square"])
    assert result == [4, 9, 16]

def test_data_pipeline_processor_chained_filters():
    result = data_pipeline_processor([1, 2, 3, 4, 5, 6], ["filter_even", "double"])
    assert result == [4, 8, 12]

# ------------------------------------------------------------------------------------------ #

# Question 9 - Leaderboard Ranker

@pytest.mark.parametrize("scores, expected_ranking", [
    (
        [("Alice", 100), ("Bob", 150), ("Charlie", 120)],
        [("Bob", 150, 1), ("Charlie", 120, 2), ("Alice", 100, 3)]
    ),
    (
        [("Player1", 50)],
        [("Player1", 50, 1)]
    ),
    ([], []),
])
def test_leaderboard_ranker_logic(scores, expected_ranking):
    assert leaderboard_ranker(scores) == expected_ranking

def test_leaderboard_ranker_tied_scores():
    scores = [("A", 100), ("B", 100), ("C", 90)]
    result = leaderboard_ranker(scores)
    # Both tied players should have rank 1
    assert result[0][2] == 1
    assert result[1][2] == 1
    assert result[2][2] == 3  # Next rank is 3, not 2

def test_leaderboard_ranker_large_dataset():
    scores = [(f"Player{i}", i) for i in range(1000, 0, -1)]
    result = leaderboard_ranker(scores)
    assert result[0][1] == 1000  # Highest score
    assert result[-1][1] == 1    # Lowest score

def test_leaderboard_ranker_all_same_scores():
    scores = [("A", 50), ("B", 50), ("C", 50)]
    result = leaderboard_ranker(scores)
    assert all(player[2] == 1 for player in result)

def test_leaderboard_ranker_invalid_tuple():
    with pytest.raises(ValueError):
        leaderboard_ranker([("Player1", 100, "extra")])

# ------------------------------------------------------------------------------------------ #

# Question 10 - Smart Cache System

def test_smart_cache_basic_operations():
    cache = smart_cache_system(3)
    cache.put("key1", "value1")
    assert cache.get("key1") == "value1"

def test_smart_cache_eviction():
    cache = smart_cache_system(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)  # Should evict "a"
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3

def test_smart_cache_lru_order():
    cache = smart_cache_system(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.get("a")  # Access "a", making it recently used
    cache.put("d", 4)  # Should evict "b", not "a"
    assert cache.get("a") == 1
    assert cache.get("b") is None

def test_smart_cache_update_existing():
    cache = smart_cache_system(2)
    cache.put("key", "value1")
    cache.put("key", "value2")
    assert cache.get("key") == "value2"

def test_smart_cache_size_one():
    cache = smart_cache_system(1)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") is None
    assert cache.get("b") == 2

def test_smart_cache_invalid_capacity():
    with pytest.raises(ValueError):
        smart_cache_system(0)