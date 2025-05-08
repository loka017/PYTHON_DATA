#다중 반환

def calculate( *args):
    result1 = sum(args)
    result2 = sum(args) / len(args)
    result3 = max(args)
    result4 = min(args)

    return result1, result2, result3, result4

a, b, c, d = calculate(1,2,3,4)

result = calculate(1,2,3,4)

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')
print(f'result = {result}')