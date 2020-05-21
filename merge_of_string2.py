s1=input("enter the first string::")
s2=input("enter the second string::")
output=''
i=j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if i<len(s2):
        output=output+s2[j]
        j=j+1
print(output)
