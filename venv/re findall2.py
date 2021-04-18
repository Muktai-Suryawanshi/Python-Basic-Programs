import re

s = "she is going to mumbai"

i = re.findall("bai$",s)

if(i):
    print("string match")
else:
    print("string is not match")
