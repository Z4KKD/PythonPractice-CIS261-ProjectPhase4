
def add(*num):   #*args
    sum = 0
    for i in num:
        sum += i
    return sum

print(add(1,2,3,4,5))



def hello(**names): #**kwargs
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")

hello(title="Mr.",first="Big",middle="Old",last="Test")

students = (("Batman", "D", 60),
            ("Superman", "C", 50),
            ("Smoke", "A", 90),
            ("Joker", "B", 25))

age = lambda ages:ages[2] #lambda
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print("\n", i)





