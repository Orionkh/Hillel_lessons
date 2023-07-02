f = open('new_file.txt', mode='w')
f.write('Hello world')
f.close()

# f = open('new_file.txt', 'r')
# print(f.readline())
# f.close()
# using same code with context manager
with open('new_file.txt', 'r') as f:
    print(f.readline())

f = open('new_file.txt', mode='a')
f.write('\nHello there')
f.close()

# f = open('new_file.txt', 'r')
# for line in f.readlines():
#     print(line)
# f.close()
# using same code with context manager
with open('new_file.txt', 'r') as f:
    print(f.read())


filename = "new_file.txt"

with open(filename, "a") as file:
    while True:
        data = input("type exit to exit(lol): ")
        if data.lower() == "exit":
            break
        file.write('\n' + data)

with open('new_file.txt', 'r') as f:
    print(f.read())

