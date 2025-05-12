import sys
import argparse
from cpf.validator import validate_cpf
from cpf.generator import generate_cpf

def main():
    parser = argparse.ArgumentParser(description='CPF Generator and Validator CLI')
    subparsers = parser.add_subparsers(dest='command')
    generate_parser = subparsers.add_parser('generate', help='Generate a valid CPF')
    generate_parser.add_argument('--raw', action='store_true', help='Generate without formatting')
    validate_parser = subparsers.add_parser('validate', help='Validate a given CPF')
    validate_parser.add_argument('cpf', help='The CPF to validate')
    args = parser.parse_args()
    if args.command == 'generate':
        cpf = generate_cpf(formatted=not args.raw)
        print(f'Generated CPF: {cpf}')
    elif args.command == 'validate':
        result = validate_cpf(args.cpf)
        print(f'The CPF {args.cpf} is {"valid" if result else "invalid"}.')
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
