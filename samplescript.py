#!/usr/bin/env python3

from sys import exit
from argparse import ArgumentParser
from importlib import import_module

parser = ArgumentParser()


parser.add_argument("width", type=int)
parser.add_argument("height", type=int)
parser.add_argument("output_file", type=str)
parser.add_argument("--garden", "-g", type=str, default="garden.Garden")
parser.add_argument("--tree", "-t", type=str, default="tree.Tree")

args = parser.parse_args()


if args.width % 2 != 1:
    print("Width must be an odd number")
    exit(1)

if args.height % 2 != 1:
    print("Height must be an odd number")
    exit(1)

module_name, cls_name = args.garden.rsplit(".", 1)
module = import_module(module_name)
garden_cls = getattr(module, cls_name)

garden = garden_cls(args.width, args.height)


module_name, cls_name = args.tree.rsplit(".", 1)
module = import_module(module_name)
tree_cls = getattr(module, cls_name)

new_tree = tree_cls((1, 1), (255, 255, 255), garden)
garden.trees.append(new_tree)


garden.process()
image = garden.dump()
image.save(args.output_file, format="png")
