def two_number_sum(target_sum):
    my_numbers = [3, 5, -4, 8, 11, 1, -1, 6]
    for num1 in my_numbers:
        for num2 in my_numbers:
            if (target_sum == num1 + num2) and (num1 != num2):
                return [num1, num2]
    else:
        return[]

print(two_number_sum(10))
