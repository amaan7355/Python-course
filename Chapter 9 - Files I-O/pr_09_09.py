import os
with open("ex.txt") as f:
    content = f.read()
with open('rename_by_python.txt','w') as f:
    f.write(content)
os.remove("ex.txt")