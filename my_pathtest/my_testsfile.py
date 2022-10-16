import os
from my_pathtest.context import ps6


def main():
    print(ps6)
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


if __name__ == "__main__":
    main()

#%%============================================================================
