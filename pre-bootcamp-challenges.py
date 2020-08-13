# Umuzi PreBoot Camp Challenges

#TASK 1
x = 0
y = 1
print(x)
print(y)

x = x + 3
y = y + x
print(x)
print(y)
    
#TASK 2
x = 1 + 1 * 2
print(x)

y = (1 + 1) * 2
print(y)

z = 1 + ( 1 * 2 )
print(z)

a =  1 + 1 * 2 / 2
print(a)

b =  (1 + 1 * 2 ) /  2
print(b)

#TASK 3

def test_num65(x,y):
    if x == 65 or y == 65 or (x + y) == 65:
        return True
    else:
        return False

print(test_num65(x,y))

#TASK 4

def test_num3(x,y):
    if x == 3 or y == 3 or (x + y) == (x + 3) or (x + y) == (y + 3):
        return True
    else:
        return False

print(test_num3(x,y))

#Task 5 (Using heron's formula)

#s = semi perimeter

def area_of_triangle(x,y,z):
    perimeter = (x + y+ z)
    s = perimeter / 2
    area = (s*(s-x)*(s-y)*(s-z)) **0.5
    print(area)
 
    
area_of_triangle(x,y,z)  



#TASK 6


def maximum(x,y,z): 
  
    if (x >= y) and (x >= z): 
        largest = x 
  
    elif (y >= x) and (y >= z): 
        largest = y 
    else: 
        largest = z 
          
    return largest 
    
    
print(maximum(x, y, z))   


#TASK 7

#Convert celcius to  Fahrenheit


def convert_celcius_to_fahrenheit(celcius):
    Fahrenheit = (celcius * 9/5) + 32
    print(Fahrenheit)
    
convert_celcius_to_fahrenheit(celcius)   

# Convert Fahrenheit to Celcius

def convert_fahrenheit_to_celcius(Fahrenheit):
    Celcius = (Fahrenheit -32) * 5/9
    print(Celcius)
    
convert_fahrenheit_to_celcius(Fahrenheit)


#Task 8

def Convert_any_number_to_hours_and_min(x):
    hours = x * 1 / 60
    minutes = x % (60)
    return ("hours", "minutes ")
    print(hours,minutes)

Convert_any_number_to_hours_and_min(x)


#TASK 9
sum = 0

for i in range(1,1000): 
    if i % 3 == 0 or i % 5 == 0:
        sum+=i

print(sum)

#TASK 10

def Check_Vow(string, vowels): 
    Vow = [each for each in string if each in vowels] 
    print(Vow) 
      
string = "Umuzi"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels)

#TASK 11
# Function to print common characters of two Strings 

from collections import Counter 
  
def common(str1,str2): 
      
    # convert strings into counter dictionary 
    dict1 = Counter(str1) 
    dict2 = Counter(str2) 
  
    # take intersection of these dictionaries 
    commonDict = dict1 & dict2 
  
    if len(commonDict) == 0: 
        print -1
        return
  
    # get a list of common elements 
    commonChars = list(commonDict.elements()) 
  
   

  
if __name__ == "__main__": 
    str1 = 'house'
    str2 = 'computers'
    common(str1, str2)