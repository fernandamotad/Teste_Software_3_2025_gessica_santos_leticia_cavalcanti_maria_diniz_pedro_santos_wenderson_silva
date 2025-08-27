import pytest
from simple_calculator.main import SimpleCalculator

@pytest.fixture
def calc():
    return SimpleCalculator()

# --- DIV ---
def test_div_normal(calc):
    assert calc.div(10, 2) == 5
    assert calc.div(-10, 2) == -5
    assert calc.div(0, 5) == 0
    assert calc.div(5, -2) == -2.5

def test_div_zero(calc):
    # Dependendo da implementação, pode retornar None ou float('inf')
    result = calc.div(10, 0)
    assert result is None or result == float('inf')

def test_div_negative(calc):
    assert calc.div(-10, -2) == 5
    assert calc.div(-10, 5) == -2

# --- AVG ---
def test_avg_normal(calc):
    assert calc.avg([2, 4, 6]) == 4
    assert calc.avg([1, 2, 3, 4, 5]) == 3

def test_avg_single(calc):
    assert calc.avg([5]) == 5
    assert calc.avg([0]) == 0

def test_avg_empty(calc):
    # Lista vazia: deve retornar None ou 0
    result = calc.avg([])
    assert result is None or result == 0

def test_avg_negative_numbers(calc):
    assert calc.avg([-1, -2, -3]) == -2
    assert calc.avg([-1, 0, 1]) == 0

def test_avg_mixed_numbers(calc):
    assert calc.avg([-5, 0, 5]) == 0
    assert calc.avg([1.5, 2.5, 3.5]) == 2.5


# --- AVG --- 
def test_avg_respects_upper_threshold(calc):
    # Lista com valores acima do limite superior
    numbers = [1, 2, 10, 3, 4]  # 10 está acima do limite superior
    # Definindo limite superior em 5
    ut = 5
    # A média deve ignorar 10, mas continuar com 3 e 4
    expected_average = (1 + 2 + 3 + 4) / 4
    assert calc.avg(numbers, ut=ut) == expected_average

