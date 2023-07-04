from solutions.nico import Solution2
import pytest


@pytest.fixture
def solution():
    return Solution2()


def test_valid_brackets(solution):
    assert solution.is_valid("()")
    assert solution.is_valid("()[]{}")
    assert solution.is_valid("{[]}")
    assert solution.is_valid("[()]{}")
    assert solution.is_valid("([]){}")
    assert solution.is_valid("([]{})")


def test_empty_string(solution):
    assert solution.is_valid("") == True


def test_single_bracket(solution):
    assert solution.is_valid("(") == False
    assert solution.is_valid(")") == False
    assert solution.is_valid("[") == False
    assert solution.is_valid("]") == False
    assert solution.is_valid("{") == False
    assert solution.is_valid("}") == False


def test_nested_brackets(solution):
    assert solution.is_valid("([{}])")
    assert solution.is_valid("({[]})") == True
    assert solution.is_valid("[({})]") == True
    assert solution.is_valid("[{()}]") == True


def test_mismatched_brackets(solution):
    assert not solution.is_valid("{{}}]")
    assert not solution.is_valid("[{()}")
    assert not solution.is_valid("({[]}")
    assert not solution.is_valid("(]")
    assert not solution.is_valid("([)]")
    assert not solution.is_valid("([)]")
    assert not solution.is_valid("([)]")
    assert not solution.is_valid("([)]")
    assert not solution.is_valid("([)]")
