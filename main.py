# main.py
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

# tests/test_sample.py
import pytest
from main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
