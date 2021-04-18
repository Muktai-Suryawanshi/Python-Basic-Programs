import re

s = "there IS no reason Behind This scene"

i = re.findall("[A-Z]",s)
print(i)