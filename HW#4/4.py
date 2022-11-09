def f(suits, numbers):
    if len(suits) == 0 or len(numbers) == 0:
        return []
    else:
        ans = []
        for i in range(len(suits)):
            for j in range(len(numbers)):
                ans.append((suits[i], numbers[j]))
        return ans

print("f(['S', 'C'], [1,2,3]):", f(['S', 'C'], [1,2,3]))
print("f(['S', 'C'], [3,2,1]):", f(['S', 'C'], [3,2,1]))
print("f([], [3,2,1]:", f([], [3,2,1]))
print("f(['S', 'C'], []):", f(['S', 'C'], []))
