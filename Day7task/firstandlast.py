
s = input("enter the string:")
if len(s) > 1:
    result = s[0].upper( ) + s[1: -1] + s[-1].upper( )
else:
    result = s.upper( )
print(result)
    
