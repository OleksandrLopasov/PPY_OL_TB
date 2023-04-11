from .my_tools import map_


def main() -> None:
    for x in map_(lambda x: x + 1, range(5)):
        print(x)


if __name__ == "__main__":
    main()
