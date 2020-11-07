import argparse

parser = argparse.ArgumentParser(description='sum the integers at the command line')  

parser.add_argument(dest='num1', type=int, help="receive interger value")
parser.add_argument('--val2', dest='num2', type=int, help="receive interger value")

args = parser.parse_args()

print(args.num1 + args.num2)