from random import choice

def attempt_code(attempts):
    if attempts % 10 == 1:
      return str(attempts) + "st"
    elif attempts % 10 == 2:
      return str(attempts) + "nd"
    elif attempts % 10 == 3:
      return str(attempts) + "rd"
    else:
      return str(attempts)+ "th"

choice_number = 0
numero_correcto = 10
attempts = 1

while choice_number != numero_correcto:
    if choice_number != 0:
      print("The number", choice_number, "Came out")
      attempts +=1

    choice_number = choice ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Finaly, the number", numero_correcto, "Came out")
print(f"The number {numero_correcto} Came out on {attempt_code(attempts)} attempt")


