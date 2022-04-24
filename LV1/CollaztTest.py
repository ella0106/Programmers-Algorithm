def solution(num):
    count = 0
    while num != 1:
        if num%2==0:
            num //= 2
        else:
            num = num*3+1
        count += 1
        #print(count, num)
        if count >= 500:
            return -1
    return count

print(solution(6))
print(solution(16))
print(solution(626331))
print(solution(1))
