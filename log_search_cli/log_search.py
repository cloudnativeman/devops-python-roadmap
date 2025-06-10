import argparse

parser = argparse.ArgumentParser(description="Search log for keyword")
parser.add_argument("logfile")
parser.add_argument("keyword")
args = parser.parse_args()

with open(args.logfile) as f:
    matches = [line for line in f if args.keyword in line]
for line in matches:
    print(line, end="")
print(f"\nTotal matches: {len(matches)}")