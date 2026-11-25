''''a="good morning"
print(a[2],a[-1])
"rnin"
print(a[7:11])
print(a[-1:-4])'''''

''''a=10+2
print(a)'''
'''''a=10+3
print(a,type(a))'''''
'''''a='hello'
print(a[3:0:-1])'''''
'''''''''a='hello'
print(a[2::])
print(a[::2])
print(a[1::])
print(a[-1::])
print(a[::-2])
print(a[2:-1:])'''''''''
'''a='good morning'
"ring"
print(a[-7::3])
print(a[-7:4:8])'''
'''a=10+5+2-4
print(a)'''
'''a=[10,20,30,40,]
print(a)
print(a,type(a))'''
'''a=(1,20,30,40,)
print(a)
print(a,type(a))'''
'''a='a';10 
print(a)'''
'''a="good morning"
"mrn"
print(a[7:3:-1])'''
'''a='good morning'
'orm'
print(a[2:1:-3])'''

'''''a='good morning'
'nnr'
print(a[-2:-8:-3])

'''''
'''a=list(input("enter:"))
print(type(a))'''
'''''a=eval(input("enter:"))
print(type(a))
'''''
'''''a=float(input("enter:"))
print(type(a))
'''''
'''''a=eval(input("enter:"))
print(a,type(a))
'''''
'''a=bool(input("enter:"))
print(type(a))'''
'''a=10+4
print(a)'''

'''''a=int(input("enter:"))
if a%2==0:
    print("even")
else:
    print("odd")'''''

'''a=list(input("enter:"))
if a[0]==a[-1]:
    print("same")
else:
    print("not same")'''

'''l=eval(input("enter list:"))
if len(l)==5:
    print("list has 5 elements")
else:
    print("list does not have 5 elements")'''

'''print(chr(65))
print(chr(97))'''

'''print(ord('A'))
print(ord('a'))
print(chr(ord('A')+32))'''

'''ch=input("enter:")
if "A"<=ch<="Z":
    print("upper")
elif "a"<=ch<="z":
    print("lower")
else: 
    print("not a letter")'''

'''un=input("enter:")
if un=='van_dana':
    print("valid username")
    pw=input("enter password:")
    if pw=='1234':
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")

'''

'''username='van_dana' 
password='1234'

un=input("enter username:")
if un==username:
    print("valid username")
    pw=input("enter password:")
    if pw==password:
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")
    '''
'''i=1
while i<=100:
    print(i)
    i+=1
    


'''

'''i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1'''
    


'''i=2
while i<=50:
    print(i)
    i+=2'''


'''n=int(input("enter num:"))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print("reversed number:",rev)'''



'''for i in range(1,101):
    print(i)'''



'''for i in range(1,51):
    if i%2==0:
        print("i,even")
'''


'''l=[10,20,30,40,50]
for i in l:
    print(i)
'''


'''''s=input("enter string:")
out=""
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=i<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i
        print("output:",out)

'''''


'''s=input("enter:")
rev=""
for i in s:
  rev=i+rev
  print("reversed string:",rev)
'''


'''''for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()'''''


'''for i in range(1,6):
    for j in range(1,6):
       if i==j:
        print("1",end="")
       else:
        print("@",end="")
    print()'''



'''for i in range(1,6):
    for j in range(1,6):
        if i<j:
            print("1",end="")
        else:
            print("@",end="")
    print()'''


'''for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print("1",end="")
        else:
            print("@",end="")
    print()'''


'''a=10,20,30
print(a,type(a))'''


'''a='happy birthday'
'htr'
print(a[-4:-7:-1])'''



'''def convert(s):
    'hello'
    out=""
    for i in s:
        if "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input("enter a string:")))'''


'''def convert(s,out):
    'hello'
    for i in s:
        if "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i

            print(out)
            return 10
print(convert(input("enter a string:"),""))'''



'''def convert():
    s=input("enter a string:")
    out=''
    'hello'
    for i in s:
        if "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i

            print(out)
convert()'''



'''def convert():
    s=input("enter a string:")
    out=''
    'hello'
    for i in s:
        if "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i

            return out
print(convert())
'''


from gc import collect


'''class college :
    cname="gpln"
    collegeloc="hoodi"
    s1=college()
    print(s1.cname,s1.collegeloc)
'''
    














































