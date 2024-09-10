import sys

try:
    assert (len(sys.argv) == 2 and sys.argv[1] != ""), 'AssertionError: more than one argument is provided'
    assert (sys.argv[1][0] == '-' or sys.argv[1][0] == '+' or sys.argv[1][0].isdigit()), 'AssertionError: argument is not an integer'
    assert sys.argv[1][1:].isdigit(), 'AssertionError: argument is not an integer'
except AssertionError as msg:
    sys.exit(msg)

int_num = int(sys.argv[1])
if (int_num % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
