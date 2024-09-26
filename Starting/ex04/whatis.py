import sys

try:
    msg = 'AssertionError: more than one argument is provided'
    if len(sys.argv) == 1:
        sys.exit()
    assert (len(sys.argv) == 2 and sys.argv[1] != ""), msg
    assert int(sys.argv[1]) or int(sys.argv[1]) == 0, msg
except AssertionError as msg:
    sys.exit(msg)
except ValueError:
    sys.exit('AssertionError: argument is not an integer')

int_num = int(sys.argv[1])
if (int_num % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
