# read .txt file and write it into .txt file

def main():
    f = open("anu.txt", "w+")
    f = open("anu.txt", "a+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    f.close()

    # Open the file back and read the contents

    f = open("anu.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print contents


# readlines read the individual line into a list

fl = f.readlines()
for x in fl:
    print x
if __name__ == "__main__":
    main()
