print('Challenge 1:')


def sum_to(n):
    return sum(range(n+1))


print(sum_to(6))

print('Challenge 2:')


def largest(li):
    answer = li[0]
    for n in li:
        if n > answer:
            answer = n
    return answer


print(largest([1, 2, 3, 4, 5, 13, 9]))


print('Challenge 3:')


def occurances(str1, str2):
    count = str1.count(str2)
    return count


print(occurances('brett', 't'))


print('Challenge 4:')


def product(*args):
    answer = 1
    for arg in args:
        answer *= arg
    return answer


print(product(4, 0.5, 5))
