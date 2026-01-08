# try:
#     number1 = int(input())
#     number2 = int(input())
#     if number2 == 0:
#         raise ZeroDivisionError
#     print(number1/number2)
# except (ValueError, NameError):
#     print("ValueError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except:
#     print("unexpected error!")

try:
    number = int(input("Enter a number: "))
    print(number / 0)
except ValueError:
    print("incorrect input value")
finally:
    print("Im a code that is always executed, ", end=" ")
    print("Nothing can stop me! ha-ha!")
    
print("code after exceptipn handling")