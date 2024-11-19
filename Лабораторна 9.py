def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file

file1_name = "TF23_1.txt"
file2_name = "TF23_2.txt"

# a) Створення файлу TF23_1
file_1_w = Open(file1_name, "w")

if file_1_w != None:
    file_1_w.write("111011, 1001, 01101.\n")
    file_1_w.write("Another line with 110011 and 0010.\n")
    file_1_w.write("Mix of text and numbers like 10101.\n")
    print("Information was successfully added to TF23_1.txt!")
    file_1_w.close()
    print("File TF23_1.txt was closed!")

# б) Обробка файла TF23_1 і запис результату в TF23_2
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r != None and file_2_w != None:
    for line in file_2_r:
        for char in line:
            if char == "1":
                file_2_w.write("0")
            elif char == "0":
                file_2_w.write("1")
            else:
                file_2_w.write(char)
    file_2_r.close()
    file_2_w.close()
    print("Files were closed!")

# в) Читання і виведення файлу TF23_2
print("New sequence:")

file_3_r = Open(file2_name, "r")

if file_3_r != None:
    for line in file_3_r:
        print(line.strip())
    print("File TF23_2.txt was closed!")
    file_3_r.close()
