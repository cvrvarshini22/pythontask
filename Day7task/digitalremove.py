s =  input("enter the words: ")
m = " "
for char in s:
    if not char.isdigit ( ):
        m += char
print (m)
