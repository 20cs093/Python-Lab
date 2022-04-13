n = int(input("Enter no. of test cases: "))
print('Enter',n,'strings:')
lst = []
# lst = ['gaga', 'rotor', 'abcde', 'lol', 'papa']
for i in range(n):
    a = input()
    lst.append(a)

for ip in [i for i in lst]:
    ip1 = ip[:len(ip)//2]
    if(len(ip)%2 == 0):
        x = len(ip)//2
    else:
        x = len(ip)//2 + 1
    ip2 = ip[x:]
    lst1 = sorted(list(ip1))
    lst2 = sorted(list(ip2))
    # print(lst1, lst2)
    if lst1 == lst2:
        print("YES")
    else:
        print("NO")
