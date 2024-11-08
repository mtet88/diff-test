import sys

def main():
    if len(sys.argv) != 3:
        print("::error::Two arguments are required.")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total = num1 + num2
        print(f"::set-output name=total::{total}")
    except ValueError:
        print("::error::Inputs must be valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
