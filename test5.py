count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 2

print "Good bye!"

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break



var = 2
while var == 1:
    num = raw_input("Enter a number  :")
    print "You entered: ", num

print "Good bye!"



fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print 'fruits:', fruits[index]

print "Good bye!"


def func1(str1,int1):
    print(str1+str(int1));

func1('hello',666);

total=0;
def func2(arg1,arg2):
    total=arg1 + arg2;
    print(total)
    #return total;

func2(2,6);

str=raw_input("input")
print "你输入的是"
