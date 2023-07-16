with open("this.txt") as f:
    content = f.read()
with open("copy.txt") as f:
    content2 = f.read()
if content == content2:
    print("files are identical")
else:
    print("files are not identical")