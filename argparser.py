import argparse

# Create a parser
# parser = argparse.ArgumentParser(
#     description="Example script to demonstrate argparse features",
#     epilog="Thank you for using this program!")

# # Add a positional argument (required by default)
# parser.add_argument('name', help="The name of the user")

# # Add an optional argument with type, choices, and a default value
# parser.add_argument('-c', '--color', choices=['red', 'blue', 'green'], default='blue', help="Favorite color")

# # Add a flag with store_true action (for boolean values)
# parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose mode")

# # Add an argument that takes multiple values using nargs
# parser.add_argument('-s', '--scores', nargs='+', type=int, help="List of scores")

# # Parse arguments
# args = parser.parse_args()

# # Use the parsed arguments
# print(f"Name: {args.name}")
# print(f"Favorite color: {args.color}")
# if args.verbose:
#     print("Verbose mode is enabled.")
# if args.scores:
#     print(f"Scores: {args.scores}")


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)',)

args = parser.parse_args()
print(args.accumulate(args.integers))
