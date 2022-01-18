#int
num=12
Num=65
print(type(num))
print(type(Num))
sum=num+Num
print(sum)
print(type(sum))

#float
num1=12.333
Num2=65.33
print(type(num1))
print(type(Num2))
sum=num1+Num2
print(sum)
print(type(sum))

#int+float
sum2=12.333+num
print(sum2)
print(type(sum))

#float
r3=2.345e10 #2.345*10^10
print(r3)
print(type(r3))

#complex Number
a=3+5j
b=9+11j
sum3=a+b
print(sum3)
print(a*b)
print(type(sum3))

print("_______________________________________________________________________")
#STRINGS
str='V'
print(str)
print(type(str))

str1="Vineet"
print(str1)
print(type(str1))

str2='Maithon'
print(str2)
print(type(str2))


str4=""""
VINEET KUMAR
I AM A STUDENT OF GLA UNIVERSITY
I AM FROM MAITHON JHARKHAND"""
print(str4)
print(type(str4))

#STRING SLICING AND IMPORTANT METHOD OF STRING
print("_______________________________________________________________________")
str5=""""
MY NAME IS VINEET KUMAR
I AM A STUDENT OF GLA UNIVERSITY
I AM FROM MAITHON JHARKHAND
I AM PURSUING BTECH CSE"""

print(str5)
print(type(str5))
print(str5[5:30])
print(str5[:9])
print(str5[10:])
print(str5[-1])
print(str5[-2])
print(str5[-5:-2])
#substring Search
if ('CSE' in str5):
    print("available")
else:
    print(" not available")
print("_________________________________________________________")
#Important Methods


str6="Vineet Kumar"

str7="       I am a Student         "

str8="3101"

print(str6)

print(str7)

print(str8)

#to find length
print(len(str7))

str9="vineet kumar"

#to capitalize first word in upper case of sentence
print(str9.capitalize())

#to add 40 space from left and right
print(str6.center(40))

#to count no of e
print(str6.count('e'))

#to find E index
print(str6.find('e'))

#To convert in lower Case
print(str6.lower())

#To convert in uppper Case
print(str6.upper())

#to Convert first alphabet into upper case of each word
print(str6.title())

# to replace a word
print(str7.replace('am','was'))

print("_________________________________________________________")

print(str7.split(' '))
#to eliminate extra space
str7=str7.strip()

print(str7)
#to spilt sentence by space
print(str7.split(' '))

str10="Vineet,Anshu,Aryan,Goli"
#to spilt sentence by comma
print(str10.split(','))

#to convert any string size 4--10 by adding zero
print(str8.zfill(10))

#to check if has only alphabet
print(str6.isalpha())

print(str8.isalpha())

str11="Vineet"
print(str11.isalpha())

#To Check if it is alpha numeric
str12="Vineet3101"
print(str12.isalnum())

#To Check if it has digit
print(str8.isdigit())

#To Check Lower Case
str13="Vineet"
print(str13.islower())

str14="vineet"
print(str14.islower())

#To Check Upper Case
str15="Vineet"
print(str15.isupper())

str16="VINEET"
print(str16.isupper())

#To Check Space
print(str6.isspace())

print("_________________________________________________________")

#FORMAT
marks=90
name='Vineet'
msg="My name is {}. I Got {} Marks"
print(msg.format(name,marks))

