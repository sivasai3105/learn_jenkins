import sys
from src.main import Learn


def main(sys_argv=sys.argv):
    print(sys_argv)
    with Learn(2, 3) as obj:
        a = obj.do()
        print(a)


if __name__ == '__main__':
    main()
