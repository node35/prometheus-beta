import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_lcs_basic_match():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"

def test_lcs_complete_match():
    assert longest_common_subsequence("ABCDEF", "ABCDEF") == "ABCDEF"

def test_lcs_no_match():
    assert longest_common_subsequence("XYZ", "ABC") == ""

def test_lcs_partial_match():
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_empty_strings():
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""

def test_lcs_different_lengths():
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_lcs_case_sensitive():
    assert longest_common_subsequence("abc", "ABC") == ""

def test_lcs_repeated_characters():
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("AABAAA", "BAAAAAA") == "AAAAA"