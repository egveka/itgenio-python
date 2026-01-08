print("Enter a mark:")

score = int(input())

if score >= 0 and score <= 40:
    print("Not good")
elif score >= 41 and score <= 60:
    print("Normal")
elif score >= 61 and score <= 80:
    print("Good")
elif score >= 81 and score <= 90:
    print("Excellent")
else:
    print("Incredible!")