# ========================  1️ Integers ======================== 

# 1. Assign your age to a variable and print it. 

age = 21
print(age)


# 2. Add 10 to your age and print the result. 

age +=10 
print(age)


# 3. Multiply 7 by 8 and store in a variable.

a = 7*8
print(a)

# 4. Divide 100 by 4 and print integer division result. 


b = 100/4
print(b)


# 5. Use modulo (%) to find remainder of 25 ÷ 4.

c = 25%4
print(c)


# 6. Increment a variable x=5 by 1.

x=5
x+=1
print(x)



# 7. Decrement a variable y=10 by 2.

y=10
y-=2
print(y)


# 8. Convert the string "50" to integer and add 10. 

string = "50"
integer = int(string)
print(integer+10)


# 9. Create two integers and swap their values.

int1 = 12
int2 = 10
print(int1,int2)
temp = int2
int2 = int1
int1 = temp
print(int1,int2)


# 10. Check if an integer is even or odd.


val = 3
if val%3==0:
  print("number is even")
else:
  print("number is odd")
  
  
# ======================== 2️ Float ======================== 


# 1. Assign your weight (e.g., 72.5) to a variable.

weight = 60.5
print(weight)


# 2. Add 5.5 to the float.


flo = 12.4
flo += 5.5
print(flo)


# 3. Subtract 2.3 from the float.


flo = 12.4
flo -= 2.3
print(flo)


# 4. Multiply 2.5 by 4.2.

flo = 2.5*4.2
print(flo)

# 5. Divide 7.5 by 2.

flo = 7.5/2
print(flo)

# 6. Round 3.14159 to 2 decimals.

flo = round(3.14159,2)
print(flo)

# 7. Convert integer 10 to float.

intger = float(10)
print(intger)


# 8. Find the absolute value of -5.75.

absolute = abs(-5.75)
print(absolute)


# 9. Compare two floats and check which is greater. 

float1 = 3.4
float2 = 5.3

if float1 < float2:
  print("float2 is greater")
else: 
  print("float1 is greater")


# 10. Calculate average of 3 float numbers.

float1 = 3.4
float2 = 5.3
float3 = 6.7
avg = (float1 + float2 + float3) / 3
print(avg)




# ======================== 3️⃣ Strings  ======================== 


 
# 1. Assign your first name to a variable. 

fname = "John"
print(fname)

# 2. Concatenate first name and last name. 

lname = "wick"
fullName = fname + " " + lname
print(fullName)


# 3. Find length of a string.

string = "Pakistan"
print(len(string))


# 4. Convert string to uppercase 

string = "Pakistan"
print(string.upper())


# 5. Convert string to lowercase. 


print(string.lower())


# 6. Check if string starts with "A"." 


print(string.startswith("A"))


# 7. Extract first 3 characters.

print(string[:3])


# 8. Replace "Hello" with "Hi".


string = "Hello World"
print(string.replace("Hello","Hi"))


# 9. Split a string "apple, banana, cherry" by comma. 

string = "apple, banana, cherry"
arr = string.split(",")
print(arr)

# 10. Join list ["Python", "R", "AI"] into a single string.

arr = ["Python", "R", "AI"]
str = ", ".join(arr)
print(str)




# ======================== 4️⃣ Boolean  ======================== 


# 1. Assign True to a variable. 

boolean = True

# 2. Assign False to a variable. 

boolean = False

# 3. Compare 5 > 3.

print(5 > 3)


# 4. Compare 10 == 10.

print(10 == 10)

# 5. Check if 7 != 7.

print(7 != 7)

# 6. Use "and" with True and False. 

print(12 < 11 and 9 > 3)

# 7. Use "or" with False and True.

print(12 < 11 or 9 > 3)

# 8. Negate a boolean value.

print(not False)

# 9. Check if string "Python" contains "p". 

print("p" in "Python")


# 10. Boolean from numeric comparison 5 >= 4.


print(5 >= 4)


# ======================== 5️ List  ======================== 


# 1. Create a list of 5 numbers. 

arr = [1,2,3,4,5]

# 2. Access 3rd element.

print(arr[2])

# 3. Change 2nd element. 

print(arr)
arr[1] = 10
print(arr)

# 4. Append a number.

arr.append(25)
print(arr)


# 5. Insert a number at position 2.

arr.insert(1,25)
print(arr)

# 6. Remove a number by value.

arr.remove(25)
print(arr)

# 7. Pop last element.

arr.pop()
print(arr)

# 8. Slice first 3 elements. 

print(arr[:3])

# 9. Find length of list. 

print(len(arr))

# 10. Reverse the list.


arr.reverse()
print(arr)
