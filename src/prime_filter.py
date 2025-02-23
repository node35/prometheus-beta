def filter_primes(numbers):
    """
    Filter a list of numbers to return only prime numbers.
    
    A prime number is a natural number > 1 that is only divisible by 1 and itself.
    Negative numbers are not considered prime.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: A list of prime numbers from the input list
    
    Examples:
        >>> filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        [2, 3, 5, 7]
        >>> filter_primes([-1, 0, 1, 2, 3, 4, 5])
        [2, 3, 5]
    """
    def is_prime(n):
        # Numbers less than 2 are not prime
        if n < 2:
            return False
        
        # Check for divisibility up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    return [num for num in numbers if is_prime(num)]