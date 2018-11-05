import pytest
import calc
import sys

@pytest.mark.parametrize("test_input, expected_output",[(5,25),(9,81),(10,100)])
def test_calc_square(test_input, expected_output):
    result=calc.square(test_input)
    assert result==expected_output