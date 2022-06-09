def palindrome(numbers):
    for number in numbers:
        if number == number[::-1]:
            print("True")
        else:
            print("False")


nums = list(map(str, input().split(", ")))
palindrome(nums)