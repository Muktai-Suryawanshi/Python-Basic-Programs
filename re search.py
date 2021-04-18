import re

a = "i am sapana suryawanshi,i am from osmanabad"

s = re.search("^i",a)

if(s):
    print("string match")
else:
    print("string not match")
