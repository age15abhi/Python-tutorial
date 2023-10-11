def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("Odd")


# method - 1
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# method - 2
# def is_even(n):
#     return True if n % 2 == 0 else False


# method - 2
def is_even(n):
    return n % 2 == 0


main()
