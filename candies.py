def kidsWithCandies(candies, extraCandies):

    max_value = max(candies)
    for index, value in enumerate(candies):
        candies[index] = (abs(value-max_value) <= extraCandies)
    return candies


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
