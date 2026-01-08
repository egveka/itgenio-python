score  = [int(i) for i in input().split()] 
score.sort(reverse=True)

for i in range(3):
        print(score[i])