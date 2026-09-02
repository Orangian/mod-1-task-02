from robot.finch import Finch
import pytest

def follow_instructions(finch_to_move, instructions):
    """
    :param finch_to_move: the finch object
    :param instructions: data that represents the instructions to tell the finch how to move
    :post: the finch follows the instructions (moves as guided)
    """
    #Didn't want to redo my code to get rid of vestigial target finch string, so not using it for now
    finch = finch_to_move
    for i in range(len(instructions)-1):
        print(i)
        print(instructions[i][0])
        if type(instructions[i][1]) is int:
            if instructions[i][0] == "t":
                #Only allows for turning rightward. Need to redo data structure to add support for turning anticlockwise.
                print("R", instructions[i][1], instructions[i][2])
                finch.turn("R", instructions[i][1], instructions[i][2])
            elif instructions[i][0] == "m":
                print("F", instructions[i][1], instructions[i][2])
                finch.move("F", instructions[i][1], instructions[i][2])
            else:
                print([instructions[i][0]])
                raise ValueError("Not turning or moving")

def reverse_instructions(instructions):
    """
    :param instructions: data that represents the instructions to tell the finch how to move
    :return: instructions that lead a finch the opposite way, i.e., if you follow instructions
             then follow reverse_instructions, you'll be back in your original position and orientation
    """

# Data format: ((f (forward) l (left) r (right) or b (backward) (str), amount (int), speed (int)), another instruction)
# Assume data has already been validated beforehand (for now)
    reversed_instructions = list(reversed(instructions))
    target = instructions[0]
    del reversed_instructions[len(instructions)-1]
    for i in range(len(instructions)-1):
        if type(reversed_instructions[i][1]) is int:
            # Check if turning, then subtract from 360
            # Finch doesn't take negative angles, but it does take negative movement values
            if reversed_instructions[i][0] == "t":
                reversed_instructions[i][1] = 360 - reversed_instructions[i][1]
            else:
                reversed_instructions[i][1] = -reversed_instructions[i][1]
    reversed_instructions.insert(0, target)
    return reversed_instructions

    """
    
    """

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

def generate_polygon_instructions(num_sides,distance=5,speed=5):
    angle = 360 / num_sides
    temporary_instruction_list = ["ABBA"]
    for i in range(num_sides):
        temporary_instruction_list.append(("m", distance, speed))
        temporary_instruction_list.append(("t", angle, speed))
        print(temporary_instruction_list)
        print(tuple(temporary_instruction_list))

    return tuple(temporary_instruction_list)

def is_instruction_valid(instruction):
    #Valid: ("m" or "t" (str), int, int)
    if type(instruction[0] == str):
        if instruction[0] == "t" or "m":
            if type(instruction[1] == int) and type(instruction[2] == int):
                print(instruction[2])
                if instruction[2] >= 0:
                    if instruction[0] == "t":
                        if instruction[1] >= 0:
                            return True
                        else:
                            raise(ValueError("Turn angle must be positive"))
                    else:
                        return True
                else:
                    raise(ValueError("Speed must be positive"))
            else:
                raise(ValueError("Second & third entries must be int"))
        else:
            raise(ValueError("First entry must be either t or m"))
    else:
        raise(ValueError("First entry must be a str"))

def test_is_instruction_valid():
    valid_turn = ("t", 50, 50)
    valid_move = ("m", 50, 50)
    negative_turn_angle = ("t", -20, 50)
    negative_move_angle = ("m", -20, 50)
    assert is_instruction_valid(valid_turn) == True
    assert is_instruction_valid(valid_move) == True
    assert is_instruction_valid(negative_move_angle) == True
    with pytest.raises(ValueError):
        is_instruction_valid(negative_turn_angle)

def test_are_instructions_valid():
    valid_instructions = ("M", ("t", 50, 50), ("m", 50, 50), ("t", 50, 50), ("m", 50, 50), ("t", 50, 50))
    negative_turn_angle = ("M", ("t", 50, 50), ("m", 50, 50), ("t", -50, 50), ("m", 50, 50), ("t", 50, 50))
    assert are_instructions_valid(valid_instructions) == True
    with pytest.raises(ValueError):
        are_instructions_valid(negative_turn_angle)

def are_instructions_valid(instructions):
    instruction_list = list(instructions)
    del instruction_list[0]
    for i in range(len(instruction_list)):
        is_instruction_valid(instruction_list[i])
    return True

def main():
    #finch = Finch("A")
    """instructions = [
        "vestige",
        ["m", 10, 5],
        ["t", 30, 35],
        ["m", 25, 10],
        ["t", 360, 20],
        ["m", -20, 15]
    ]
    follow_instructions(finch, instructions)
    follow_instructions(finch, reverse_instructions(instructions))"""
    num_sides=4
    distance=10
    speed=25
    #follow_instructions(finch, generate_polygon_instructions(num_sides, distance, speed))

if __name__ == "__main__":
    main()

