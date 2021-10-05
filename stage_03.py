
with open("artifect01.txt", "r") as f:
    text = f.read()
with open("artifect02.txt", "w") as f:
    text = f.write(text + "added line")

print("Stage 02")


print("End of Test2")