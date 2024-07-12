import pytest as pytest

from Demo.sample import func
from Demo.sample import calculatorAdd
from Demo.sample import *
from Demo.conftest import *

@pytest.mark.sanity
def test_calculatorAddition():
        a=2
        b=3
        expected_result = 5
        result = calculatorAdd(a, b)
        assert result == expected_result
        print('Actual result ', result , 'Expected Result' ,expected_result)


@pytest.mark.sanity
def test_calculatorSubtraction():
        a=5
        b=3
        expected_result = 2
        result = calculatorSub(a, b)
        assert result == expected_result
        print('Actual result ', result , 'Expected Result' ,expected_result)



@pytest.mark.slow
def test_calculatorMultiplication():
        a=2
        b=3
        expected_result = 6
        result = calculatorMultiply(a, b)
        assert result == expected_result
        print('Actual result ', result , 'Expected Result' ,expected_result)

@pytest.mark.slow
def test_calculatorDevision():
        a=20
        b=0
        with pytest.raises(ValueError) as esc_info:
                calculatorDevide(a, b)
        assert str(esc_info.value) == "value of b=0 is not allowed"

@pytest.mark.slow
def test_calculatorDevisionExc():
        a=20
        b=0
        if(b==0):
                raise ZeroDivisionError("division by zero is not allowed")
        else:
                expected_result = 10
                result = calculatorDevide(a, b)
                assert result == expected_result
                print('Actual result ', result , 'Expected Result' ,expected_result)

@pytest.mark.parametrize("a,b,expected",[(2,3,5),4,5,10])
def test_add(a,b,expected):
        result = add(a,b)
        assert result == expected

@pytest.mark.slow
def test_add(sample_data):
        result = calculatorAdd(sample_data["a"],sample_data["b"])
        assert result ==5
