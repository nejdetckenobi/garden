#!/usr/bin/env python3

from sys import exit
from argparse import ArgumentParser
from importlib import import_module


def import_obj(path):
    module_name, obj_name = path.rsplit(".", 1)
    module = import_module(module_name)
    return getattr(module, obj_name)


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


garden_cls = import_obj(args.garden)
shared_memory: dict = {}

garden = garden_cls(
    width=args.width,
    height=args.height,
    memory=shared_memory,
)

tree_cls = import_obj(args.tree)

new_tree = tree_cls(
    start_point=(1, 1),
    color=(255, 255, 255),
    width=args.width,
    height=args.height,
    memory=shared_memory,
)
garden.trees.append(new_tree)


garden.process()
image = garden.dump()
image.save(args.output_file, format="png")
