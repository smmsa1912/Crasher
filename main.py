import os

i = 0

while True:

    num = open('Content/Created.txt', 'w')
    num.write(str(i))
    num.close()

    if i == 2:
        break
    i += 1
    py_name = f"Hack_{i}.py"
    file = open(f"Hack_{i}.py", "w")
    cont = open('Content/cont', 'r+')
    for text in cont:
        file.write(text)

    os.startfile(f"Hack_{i}.py")
    print('Hacked')
