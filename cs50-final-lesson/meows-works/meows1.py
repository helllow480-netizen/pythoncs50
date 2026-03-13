import argparse

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n", type=int, help="number of times to meow", default=1)
args = parser.parse_args()
for i in range(args.n):
    print("Meow")