def reverse_instructions(instructions):
    """
    :param instructions: data that represents the instructions to tell the finch how to move
    :return: instructions that lead a finch the opposite way, i.e., if you follow instructions
             then follow reverse_instructions, you'll be back in your original position and orientation
    """

# Data format: [Robot name (str), [t (turning) or m (moving) (str), amount (int), speed (int)], Another instruction]
# Need to find a way to go into every list & subtract angles from 360
# Assume data has already been validated beforehand (for now)
    reversed_instructions = []
    item = len(instructions) - 1
    for i in range(len(instructions)):
        if i == 0:
            return reversed_instructions
        reversed_instructions.append(instructions[item])
        reversed_instructions[i][1] = -reversed_instructions[i][1]
        item -= 1

def main():
    test1 = ["A", ["t", 302, 20]]
    test1out = ["A", ["t", -302, 20]]
    test2 = ["Z", ["t", 302, 20], ["m", 40, 60], ["t", -30, 1], ["m", -60, 10], ["m", 2, 2]]
    test2out = ["Z", ["t", -302, 20], ["m", -40, 60], ["t", 30, 1], ["m", 60, 10], ["m", -2, 2]]
    print(reverse_instructions(test1))
    print(reverse_instructions(test2))
    assert reverse_instructions(test1) == test1out
    assert reverse_instructions(test2) == test2out


main()


