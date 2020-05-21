

str1 = input("enter the string")
str2 = input("enter the sub string")

flag =0


if len(str1) > len(str2):
    for i in range(0,len(str2)):
        #print(i)
        if str1[i] == str2[i]:
            pass
            #i=i+1
        flag=flag+1
        
print(str1,str2,end="\n")
print("matched at position{}".format(flag))

            