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

        # Check if GITHUB_OUTPUT is available
        github_output_path = os.getenv('GITHUB_OUTPUT')
        print(f"GITHUB_OUTPUT path: {github_output_path}")

        if github_output_path:
            # Write to GITHUB_OUTPUT if the path exists
            with open(github_output_path, 'a') as github_output:
                github_output.write(f"total={total}\n")
        else:
            print("::error::GITHUB_OUTPUT environment variable not found.")
            sys.exit(1)
    except ValueError:
        print("::error::Inputs must be valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
