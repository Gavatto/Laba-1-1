import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=float)
parser.add_argument('args', type=str)
parser.add_argument("y", type=float)
print(parser.parse_args())
args = parser.parse_args()

result = 0

if str(args.args[1]) == "+":
    result = float(args.args[0]) + float(args.args[2])

elif str(args.args[1] == "-"):
    result = float(args.args[0]) + float(args.args[2])

elif str(args.args[1] == "*"):
    result = float(args.args[0]) + float(args.args[2])

elif str(args.args[1] == "/"):
    result = float(args.args[0]) + float(args.args[2])

    print("result is = ", result)
