fileName = "sample.txt"

try:
    with open(fileName, "r+") as file:
        readline1 = file.readlines(1)
        print("Line 1:", readline1)
        readline2 = file.readlines(2)
        print("Line 2:", readline2)
except FileNotFoundError:
    print("The File", fileName ,"was not found")