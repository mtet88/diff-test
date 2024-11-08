import sys
import os

def main():
    if len(sys.argv) != 3:
        print("::error::Two arguments are required.")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total = num1 + num2
        set_output(total, 'total')
    except ValueError:
        print("::error::Inputs must be valid numbers.")
        sys.exit(1)

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)

if __name__ == "__main__":
    main()
