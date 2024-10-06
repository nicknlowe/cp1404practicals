"""
CP1404/CP5632 - Practical
Collection of programs aimed to utilise the correct file-reading technique
"""


# Question 1
def question1():
    name = input("Name: ")
    out_file = open("name.txt", 'w')
    print(name, file=out_file)
    out_file.close()


# Question 2
def question2():
    in_file = open("name.txt")
    print(f"Hi {in_file.read().strip()}!")
    in_file.close()


# Question 3
def question3():
    with open("numbers.txt") as in_file:
        first_number = int(in_file.readline())
        second_number = int(in_file.readline())
        print(first_number + second_number)


# Question 4
def question4():
    total = 0
    with open("numbers.txt") as in_file:
        for line in in_file:
            total += int(line)
    print(total)


question1()
question2()
question3()
question4()
