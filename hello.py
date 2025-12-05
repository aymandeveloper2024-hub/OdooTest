import sys

def main(arg1, arg2):
    output1 = f"Argument 1: {arg1}"
    output2 = f"Argument 2: {arg2}"
    return output1, output2  # Return the outputs as a tuple

if __name__ == '__main__':
    if len(sys.argv) > 2:
        result = main(sys.argv[1], sys.argv[2])  # Call main and store the result
        print(result[0])  # Print the first argument output
        print(result[1])  # Print the second argument output
    else:
        print("Not enough arguments provided.")
