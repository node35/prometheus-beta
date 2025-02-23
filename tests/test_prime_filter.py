import pytest
from src.prime_filter import filter_primes

def test_filter_primes_basic():
    """Test basic prime number filtering"""
    assert filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]

def test_filter_primes_negative_numbers():
    """Test handling of negative numbers"""
    assert filter_primes([-1, 0, 1, 2, 3, 4, 5]) == [2, 3, 5]

def test_filter_primes_empty_list():
    """Test filtering an empty list"""
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    """Test list with no prime numbers"""
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []

def test_filter_primes_all_primes():
    """Test list with all prime numbers"""
    assert filter_primes([2, 3, 5, 7, 11, 13]) == [2, 3, 5, 7, 11, 13]

def test_filter_primes_large_numbers():
    """Test filtering larger prime and non-prime numbers"""
    assert filter_primes([17, 18, 19, 20, 23, 24, 29]) == [17, 19, 23, 29]