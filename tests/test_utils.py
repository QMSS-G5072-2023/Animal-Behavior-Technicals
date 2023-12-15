# tests/test_utils.py
from animal_behavior_technicals import utils

def test_is_status_accurate():
    assert utils.is_status_accurate('A') is True
    assert utils.is_status_accurate('B') is False

def test_is_high_temperature():
    assert utils.is_high_temperature(36) is True
    assert utils.is_high_temperature(25) is False

def test_is_low_temperature():
    assert utils.is_low_temperature(1) is True
    assert utils.is_low_temperature(10) is False

def test_get_climate_zone():
    assert utils.get_climate_zone(25) == 'Tropical'
    assert utils.get_climate_zone(45) == 'Temperate'
    assert utils.get_climate_zone(-75) == 'Polar'
    assert utils.get_climate_zone(120) == 'Unknown'
