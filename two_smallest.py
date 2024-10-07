def find_two_smallest(number):
    """The function receives a list of integers as a parameter and returns two smallest list values"""
    if len(number) < 2:
        raise ValueError("List must have at least two numbers!")
    small1 = min(number)
    number.remove(small1)
    small2 = min(number)
    return small1, small2