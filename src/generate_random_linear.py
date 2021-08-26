import argparse
import random
from random import randrange, uniform
parser = argparse.ArgumentParser()
parser.add_argument('--formula', '-f', help='The formula for the data', nargs=2, type=float, default=None)
parser.add_argument('--size', '-si', help='Quantity of data', type=int, default=100, nargs='?')
parser.add_argument('--range', '-r', help='Range of the values to a and b from the followed arg in the form of: first to the second', type=float, nargs=2, default=[0.5, 0.2])
parser.add_argument('--step', '-st', help='Step range for each x, from 0 to [your argument]', type=int, nargs='?', default=3)
args = parser.parse_args()

file = open('random_generated.csv', 'w')
file.write('Variável independente, Variável dependente\n')
if(args.formula != None):
    for i in range(0, args.size):
        x = i
        file.write(f'{x},{args.formula[0] + args.formula[1]*x}\n')
else:
    a = random.uniform(args.range[0], args.range[1])
    b = random.uniform(args.range[0], args.range[1])

    for i in range(0, args.size):
        x = i + (random.uniform(args.step/2, args.step)*random.uniform(1, args.step)*args.size/random.uniform(1, args.step))
        ra = random.random()
        rb = random.uniform(0, args.range[1]*random.random())
        if random.random() > 0.5:
            rb = -rb
        file.write(f'{x},{b+rb + (a+ra)*x}\n')
