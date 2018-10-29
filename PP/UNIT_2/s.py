s1=""
s2=str()
s3="welcome"
s4=str("welcome")
s5='hi'
s6="""hi"""
print(id(s3))
print(id(s4))
print(s3==s4)
print(s3)
for s in s3:
    print(s)
for s in s3:
    print(s,end="")
print(len(s))
# indexing
print(s3[1])
print(s3[-1])
print(s3[1.5])
print(s3[8])
# slicing
print(s3[0:7])
print(s3[0:-1])
print(s3[::-1])
print(s3[1:4])
print(s3[4:3])
print(s3[:4])
# concatenation
s5="hello"
print(s3+"snist")
s4=s5+s3
print(s4)
s9="welcome"
print(id(s9))
s9=s9+"snist"
print(id(s9))
print(s9)
#updation
s5[0]='b'
s5="bye"
#deletion
del s5
print(s5)
# repetation
print(s3*3)
#membership
print('i'in s3)
print('i' not in s3)
print('e' in s3)
# string functions
s7="Python Programming"
print(s7.upper())
print(s7.lower())
print(s7.count('e'))
s8="wel come to snist"
print(s8.capitalize())
x=s8.index('come')
print(x)
s9=s8.replace("snist","hyd")
s10="wel come"
print(s10.rindex('e'))
print(min(s10))
print(max(s10))
s11="Hello!"
suffix='!'
print(s11.endswith(suffix))
s12="Hello python"
print(s12.find("python"))
print(s12.join("Programming"))
































