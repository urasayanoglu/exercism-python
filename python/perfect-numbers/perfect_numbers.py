def classify(number):
    if number < 0 or number == 0:
        raise ValueError(f"{number} is not a positive integer.")
    factors = []
    i = 1
    while i < number:
        if number % i == 0:
            factors.append(i)
        i += 1
    if sum(factors) > number:
        return "abundant"
    elif sum(factors) == number:
        return "perfect"
    elif sum(factors) < number:
        return "deficient"
