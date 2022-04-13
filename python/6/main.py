n = int(input("Enter no. of words: "))

print('Enter',n,'words: ')
lst = list()
for i in range(n):
    ip=input()
    lst.append(ip)

# lst = ['bcdef','abcdef','cde','bcdef']

dict1 = dict()
for i in range(n):
    ip = lst[i]
    if ip not in dict1:
        dict1[ip] = 1
    else:
        dict1[ip] += 1
print('word cardinality:', dict1,'\n')

print('ANSWER:')
print(len(dict1))
for i in [i for i in dict1.values()]:
    print(i, end=" ")
