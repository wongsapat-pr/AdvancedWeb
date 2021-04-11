# House of Card
def cards_needed(n):
    if n < 0:
        return "invalid"
    else:
        return n * (3 * n + 1) // 2


# Sum of Odd and Even Numbers
def sum_odd_and_even(lst):
    sum = [0, 0]
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            sum[0] += lst[i]
        else:
            sum[1] += lst[i]

    return sum


# Adding Numbers
def add(n1, n2):
    if n1 is not None and n1 != "":
        if n2 is not None and n2 != "":
            a = a = int(n1) + int(n2)
            return str(a)
        else:
            return "Invalid Operation"
    else:
        return "Invalid Operation"


# Next Prime
def next_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0 or num % 2 == 0:
                num += 1
                next_prime(num)
    else:
        num += 1
        next_prime(num)
    return num


# Calculated Bonus
def bonus(days):
    if days >= 48:
        d1 = days - 32
        if d1 >= 8:
            d2 = days - 40
            d3 = days - 48
            d2 = d2 - d3
            d1 = d1 - d2 - d3
        sum = (d1 * 325) + (d2 * 550) + (d3 * 600)
    elif days >= 41:
        d1 = days - 32
        d2 = 0
        if d1 >= 8:
            d2 = days - 40
            d1 = d1 - d2
        sum = (d1 * 325) + (d2 * 550)
    elif days >= 33:
        d1 = days - 32
        sum = d1 * 325
    else:
        sum = 0
    return sum
