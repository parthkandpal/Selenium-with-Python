import pytest
import calc
import sys

# @pytest.mark.skipif(sys.version_info>(3,5),reason="skip it for now")
# def test_calc_total():
#     total= calc.calc_total(2,3)
#     assert total==5
#
# def test_calc_multiply():
#     result=calc.calc_multiply(3,2)
#     assert result==6
#
# def test_dummy():
#     assert True

#Custom Markers

@pytest.mark.window
def test_window1():
    pass

@pytest.mark.window
def test_window2():
    pass

@pytest.mark.mac
def test_mac1():
    pass

@pytest.mark.mac
def test_mac2():
    pass