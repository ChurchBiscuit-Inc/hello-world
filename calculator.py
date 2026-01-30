#!/usr/bin/env python3
"""
Simple CLI Calculator
Supports addition, subtraction, multiplication, and division.
"""

import argparse
import sys


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Simple CLI Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python calculator.py add 5 3
  python calculator.py subtract 10 4
  python calculator.py multiply 6 7
  python calculator.py divide 20 4
        """
    )
    
    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First number")
    add_parser.add_argument("b", type=float, help="Second number")
    
    # Subtract command
    sub_parser = subparsers.add_parser("subtract", help="Subtract second number from first")
    sub_parser.add_argument("a", type=float, help="First number")
    sub_parser.add_argument("b", type=float, help="Second number")
    
    # Multiply command
    mul_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    mul_parser.add_argument("a", type=float, help="First number")
    mul_parser.add_argument("b", type=float, help="Second number")
    
    # Divide command
    div_parser = subparsers.add_parser("divide", help="Divide first number by second")
    div_parser.add_argument("a", type=float, help="First number")
    div_parser.add_argument("b", type=float, help="Second number")
    
    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_args()
    
    if not args.operation:
        print("Error: No operation specified. Use --help for usage.", file=sys.stderr)
        return 1
    
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    
    try:
        result = operations[args.operation](args.a, args.b)
        print(result)
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
