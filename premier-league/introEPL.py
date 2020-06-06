print('Hello EPL!')
num = 71
numSqrt = num ** 0.5
print('Sqr Root of %0.3f is %0.3f' % (num, numSqrt))

print("==========================")

# Area of triangle
# a = float(input('1st side: '))
# b = float(input('2nd side: '))
# c = float(input('3rd side: '))
#
# s = (a + b + c) / 2
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print('Area: %0.2f' % area)

print("==========================")

# Strings
var1 = 'Los Angeles'
var2 = "Lakers"
print("var1[0]", var1[0])
print("var2[1:5]", var2[1:5])
print(var1 + " " + var2 + " " + "Yesss")
print(var1.upper())
print(var1.capitalize())
print(var1.lower())

print("==========================")

# replace() = returns a copy of the string in which the values of old string replaced with the new value
oldStr = "I like programming"
newStr = oldStr.replace('like', 'love')
print(newStr)

print("==========================")

# Join
print(":".join("Python"))
str1 = "Big Data Analytics"
print(''.join(reversed(str1)))

print("==========================")

# Tuples = Enables you to assign more than one variable at a time!
tup1 = ('Martina Hingis', 'Monica Seles', 'Steffi Graf', 'Coco Gouf')
tup2 = (1, 2, 3, 4, 5, 6)
tup3 = (6, 5, 4, 3, 2, 1)
print(tup1[3])
print(tup2[1:3])
print(tup3[1:3])

tup4 = ("Yekta", "Ozdemir", 27, "Student")          # tuple packing
(name, surname, age, job) = tup4                    # tuple unpacking
print(name)
print(job)

print("==========================")






















