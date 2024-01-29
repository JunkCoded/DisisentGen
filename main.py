import argparse


def cmd1(args):
    print(f'cmd1 with {args.option}')


def cmd2(args):
    print(f'cmd2 with {args.a} and {args.b}')


def main():
    parser = argparse.ArgumentParser(description='test desc')
    subparsers = parser.add_subparsers(title='cmds', dest='command')

    parser_cmd1 = subparsers.add_parser('cmd1', help='help cmd1')
    parser_cmd1.add_argument('--option', type=str, help='option help')

    parser_cmd2 = subparsers.add_parser('cmd2', help='help cmd1')
    parser_cmd2.add_argument('a', type=str, help='a help')
    parser_cmd2.add_argument('b', type=str, help='b help')

    args = parser.parse_args()

    if args.command == 'cmd1':
        cmd1(args)
    elif args.command == 'cmd2':
        cmd2(args)


if __name__ == '__main__':
    main()
