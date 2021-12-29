
# Strings: ordered, immutable, text representation

my_string = "Hello World"
print(my_string)

# substring

substring = my_string[1:5]
print(substring)

substring = my_string[1:]
print(substring)

substring = my_string[:5]
print(substring)

substring = my_string[::2]
print(substring)

substring = my_string[::1]
print(substring)

substring = my_string[::-1]
print(substring)

#########

greeting = "Hello"
for i in greeting:
    print(i)

if "e" in greeting:
    print("yes")
else:
    print("no")

# remove wide space

my_string = "   Hello World   "
print(my_string)

my_string = my_string.strip()
print(my_string)

print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("Hello"))
print(my_string.endswith("Hello"))
print(my_string[1])
print(my_string.count("o"))
print(my_string.replace("World", "Universe"))

#######

my_string = "how are you doing"

my_list = my_string.split(" ")
print(my_list)

my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)

my_string = "how are you doing"
my_list = my_string.split()
print(my_list)

new_string = " ".join(my_list)
print(new_string)

print(" ".join(my_list))

#############

# formatting strings: %, format(), f-strings

var1 = "Tom"
var2 = 2.3854
var3 = 6
#####
my_string = "How are you %s, your gpa is %f and your rank is %i" % (var1, var2, var3)
print(my_string)

my_string = "How are you %s, your gpa is %0.2f and your rank is %i" % (var1, var2, var3)
print(my_string)
#####
my_string = "How are you,{} your gpa is {} and your rank is {}".format(var1, var2, var3)
print(my_string)

my_string = "How are you {}, your gpa is {:0.2f} and your rank is {}".format(var1, var2, var3)
print(my_string)
######
my_string = f"How are you {var1}, your gpa is {var2} and your rank is {var3}"
print(my_string)

my_string = f"How are you {var1}, your gpa is {var2:0.2f} and your rank is {var3}"
print(my_string)