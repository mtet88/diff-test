import sys

def main():
    if len(sys.argv) != 3:
        print("::error::Two arguments are required.")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total = num1 + num2
        # Write to GITHUB_OUTPUT for GitHub Actions to recognize it
        with open('/home/runner/work/_temp/_github_output', 'a') as f:  # Standard GitHub Actions temp path
            f.write(f"total={total}\n")
    except ValueError:
        print("::error::Inputs must be valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
