from robot.finch import Finch

def follow_instructions(finch_to_move, instructions):
    """
    :param finch_to_move: the finch object
    :param instructions: data that represents the instructions to tell the finch how to move
    :post: the finch follows the instructions (moves as guided)
    """
    #Didn't want to redo my code to get rid of vestigial target finch string, so not using it for now
    finch = finch_to_move
    for i in range(len(instructions)-1):
        if type(instructions[i][1]) is int:
            if instructions[i][0] == "T":
                #Only allows for turning rightward. Need to redo data structure to add support for turning anticlockwise.
                finch.turn("R", instructions[i][1], instructions[i][2])
            else:
                finch.move("F", instructions[i][1], instructions[i][2])

def reverse_instructions(instructions):
    """
    :param instructions: data that represents the instructions to tell the finch how to move
    :return: instructions that lead a finch the opposite way, i.e., if you follow instructions
             then follow reverse_instructions, you'll be back in your original position and orientation
    """

# Data format: [Robot name (str), [t (turning) or m (moving) (str), amount (int), speed (int)], Another instruction]
# Need to find a way to go into every list & subtract angles from 360
# Assume data has already been validated beforehand (for now)
    reversed_instructions = list(reversed(instructions))
    target = instructions[0]
    del reversed_instructions[len(instructions)-1]
    for i in range(len(instructions)-1):
        if type(reversed_instructions[i][1]) is int:
            # Check if turning, then subtract from 360
            # Finch doesn't take negative angles, but it does take negative movement values
            if reversed_instructions[i][0] == "T":
                reversed_instructions[i][1] = 360 - reversed_instructions[i][1]
            else:
                reversed_instructions[i][1] = -reversed_instructions[i][1]
    reversed_instructions.insert(0, target)
    return reversed_instructions

"""def main():
"""

def simplify_instructions(instructions):
    """
    :param instructions: data that represents the instructions to tell the finch how to move
    :return: shorter instructions if possible. Wherever there are consecutive directions repeated (e.g.,
           forward twice),the moves are combined into a single move that includes the total distance
    """
    raise NotImplementedError()

#def test_simplify_instructions():
#    assert 10 == 5  # example assert, should fail

def prompt_for_custom_instructions():
    """
    asks the user to use the keyboard to enter instructions one at a time until they decide to stop.
  Validates each and prompts user to fix when they have errors
    :return: a valid list of instructions (even if it is empty)
    """
    raise NotImplementedError()

def test_reverse_instructions():
    test1 = ["A", ["t", 302, 20]]
    test1out = ["A", ["t", -302, 20]]
    test2 = ["Z", ["t", 302, 20], ["m", 40, 60], ["t", -30, 1], ["m", -60, 10], ["m", 2, 2]]
    test2out = ["Z", ["m", -2, 2], ["m", 60, 10], ["t", 30, 1], ["m", -40, 60], ["t", -302, 20]]
    assert reverse_instructions(test1) == test1out
    assert reverse_instructions(test2) == test2out

def main():
    finch = Finch("A")
    instructions = ["vestige", ["m", 100, 100], ["t", 90, 100], ["m", 25, 100], ["m", -50, 100]]
    follow_instructions(finch, instructions)
    follow_instructions(finch, reverse_instructions(instructions))

if __name__ == "__main__":
    main()

