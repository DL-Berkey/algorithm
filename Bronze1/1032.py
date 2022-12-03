N = int(input())

answer = []

for _ in range(N):
    if not answer:
        answer = list(input())
    else:
        file = list(input())
        
        for i in range(len(answer)):
            if (answer[i] != file[i]):
                answer[i] = "?"
                
print("".join(answer))
