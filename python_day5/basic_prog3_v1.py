import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('val1', type=int,
                    help='accept an integer')

args = parser.parse_args()
print(args.val1)