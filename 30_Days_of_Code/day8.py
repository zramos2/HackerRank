# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phoneBook = {j:k for j,k in name_numbers}

for _ in range(n):
    # https://stackoverflow.com/questions/42891603/how-to-remove-eoferror-eof-when-reading-a-line
    # check link on why we I used try-except
    try:
        name = input()
        if name in phoneBook.keys():
            # print(name,'=',phoneBook[name]) Same way
            # python can use C string format:
            print("%s=%s" % (name, phoneBook[name]))

        else:
            print("Not found")
    except:
        break
