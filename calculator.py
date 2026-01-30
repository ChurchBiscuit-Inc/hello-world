#!/usr/bin/env python3
"""
Simple CLI Calculator
Supports: add, subtract, multiply, divide
"""

import sys
import argparse


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    parser = argparse.ArgumentParser(
        description="Simple CLI calculator"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform"
    )
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    
    args = parser.parse_args()
    
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    try:
        result = operations[args.operation](args.a, args.b)
        print(f"{args.a} {get_operator(args.operation)} {args.b} = {result}")
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def get_operator(operation):
    operators = {
        "add": "+",
        "subtract": "-",
        "multiply": "*",
        "divide": "/"
    }
    return operators[operation]


if __name__ == "__main__":
    sys.exit(main())
