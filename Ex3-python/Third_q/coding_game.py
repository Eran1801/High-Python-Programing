class CGXFormat:
    def __init__(self):
        self.base_space = 4
        self.inside_string = False
        self.total_indentation = 0
        self.new_line = True  # When we start a new line this var will be True, False otherwise.
        self.lines_number = 0

    def read_lines(self):
        self.lines_number = int(
            input())  # This is the first input. here the program starts,we get here the number of lines
        for i in range(self.lines_number):
            line = input()  # we get the first line
            for character in line:  # on each line we get we go trow all his characters
                self.read_char(character)  # send each char to read_char function

    def read_char(self, char: str):
        if self.inside_string is True:
            if char == '\'':  # We finish to read to string
                self.inside_string = False  # We get out of a string. because of the ' char
            self.print_char(char)
        # When we are not inside the string
        else:
            self.read_char_outside_string(char)

    def read_char_outside_string(self, char: str):
        if char == ' ' or char == '\t':
            return  # There is nothing to print
        if char == '\'':
            self.inside_string = True  # The first ' indicate start of a string
            self.print_char(char)
        elif char == '(':
            if self.new_line is False:
                self.print_new_line()  # Instruction: A BLOCK starts on its own line.
            self.print_char(char)
            self.print_new_line()
            self.total_indentation += self.base_space  # indented 4 spaces from the marker of that BLOCK.
        elif char == ')':
            self.total_indentation -= self.base_space  # Each () in the same column, we are going back 4 steps
            if self.new_line is False:
                self.print_new_line()
            self.print_char(char)
        elif char == ';':
            self.print_char(char)
            self.print_new_line()
        else:
            self.print_char(char)  # Any other char beside all of the above

    def print_char(self, character: str):
        if self.new_line is True:
            for _ in range(self.total_indentation):
                print(' ', end='')  # We don't want to make a new line
            self.new_line = False
        print(character, end='')  # After we take care of all the indentation we print our character

    def print_new_line(self):
        print()
        self.new_line = True


if __name__ == "__main__":
    start = CGXFormat()
    start.read_lines()
