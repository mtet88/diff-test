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
        # Write the output directly to the GITHUB_OUTPUT file
        with open(os.environ['GITHUB_OUTPUT'], 'a') as output_file:
            print(f"total={total}", file=output_file)
    except ValueError:
        print("::error::Inputs must be valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
