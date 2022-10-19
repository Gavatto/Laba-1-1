import argparse
import math
import operator

parser = argparse.ArgumentParser(description="Calculating ")
parser.add_argument("x", type=float)
parser.add_argument("args", type=str)
parser.add_argument("y", type=float)
args = parser.parse_args()


def run_func(namespace):
    func_num1 = f'operator.{namespace.args}'
    func_num2 = f'math.{namespace.args}'
    if hasattr(operator, namespace.args):
        return eval(func_num1)(namespace.x, namespace.y)
    if hasattr(math, namespace.command):
        return eval(func_num2)(namespace.x, namespace.y)
    else:
        return ("Error")
