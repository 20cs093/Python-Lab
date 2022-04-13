class Student:
    def __init__(self, r, n):
        self.rno = r
        self.name = n

class Exam(Student):
    def __init__(self,r,n,m):
        Student.__init__(self,r,n)
        self.marks=[]
        self.marks=m

class Result(Exam):
    def __init__(self,r,n,m):
        Exam.__init__(self,r,n,m)
        self.total = sum(self.marks)
    def __str__(self):
        avg = self.total/6
        return  "RollNo: {a} \t\t\t Name: {b} \nTotal Marks: {c}/600 \t Percentage: {d}"\
            .format(a=self.rno,b=self.name,c=self.total,d=avg)

# s1= Result(1,"Abhi",[5,2,6,4,3,1])
# print(s1.name,s1.total)
sList = []
N = int(input("Enter no. of students: "))
for i in range(N):
    r = int(input("Enter RollNo.: "))
    n = input("Enter name: ")
    print("Enter 6 marks: ")
    m = list(map(int, input().split()))
    # print(m)
    s = Result(r, n, m)
    sList.append(s)

print()
print("Displaying Result:")
for sl in sList:
    print(sl)


