fileName = "../output.txt"

try:
    with open(fileName, "r+") as file1:
        user_input1 = input("Enter text to write to the file: ")
        file1.write(user_input1 + "\n")
        file1.close()
        print("Data successfully written to:", fileName)

    with open(fileName, "a") as file2:
        user_input2 = input("Enter additional text to append: ")
        file2.write(user_input2 + "\n")
        file2.close()
        print("Data successfully appended.")
        
    with open(fileName, "r+") as file3:
        final_content = file3.read()
        print("Final content of", fileName + ":")
        print(final_content)

except FileNotFoundError:
    print("The File", fileName ,"was not found")