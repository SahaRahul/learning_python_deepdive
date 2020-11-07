import argparse

parser = argparse.ArgumentParser(description='sum the integers at the command line')  
parser.add_argument('intlist', 
                    metavar='int', nargs='+', type=int, help='an integer to be summed')  

args = parser.parse_args()  
print(sum(args.intlist))

