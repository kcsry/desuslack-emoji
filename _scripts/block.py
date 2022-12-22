import argparse

from update import blash


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name", nargs="+")
    args = ap.parse_args()
    print(repr(set(sorted(blash(name) for name in args.name))))


if __name__ == "__main__":
    main()
