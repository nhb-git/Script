# -*- coding: utf-8 -*-
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description='A Python-Mysql Client.')
    parser.add_argument(
        '--host', action='store', dest='host', required=True,
        help='mysql server addr'
    )
    parser.add_argument(
        '-u', action='store', dest='user', required=True, help='login username'
    )
    parser.add_argument(
        '-p', action='store', dest='password', required=True,
        help="'login user's password"
    )
    parser.add_argument(
        '-P', action='store', dest='port', default=3306, type=int,
        help='mysql server port number, default 3306'
    )
    parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s 0.1'
    )
    return parser.parse_args()


def main():
    parser = _argparse()
    conn_args = dict(
        host=parser.host, user=parser.user, password=parser.password,
        port=parser.port
    )
    print(conn_args)


if __name__ == "__main__":
    main()
