# task2 ში დაწერეთ ფუნქცია რომელიც მიიღებს რიცხვს და დააბრუნებს რიცხვის ციფრების ჯამს. მაგალითად : 1121 -> 1 + 1 + 2 + 1 = 5 , 2024 -> 8
def sum_of_digits(number):
    total_sum = 0
    for i in str(number):
        total_sum += int(i)
    return total_sum


print(sum_of_digits(16720))