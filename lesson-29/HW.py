total = int(input())
student1 = set(input().split())
student2 = set(input().split())

print(total-len(student1|student2))