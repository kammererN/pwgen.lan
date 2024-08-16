
# Tests for "../pwgen/pwgen.py"
import sys
sys.path.append("/home/nkam/dev/py-web-pwgen/pwgen")
from pwgen import Pwgen


def test_pwgen(test_class: Pwgen) -> str:
    return test_class.pwgen()


def test_print_command(test_class: Pwgen) -> None:
    return test_class.print_command()


def main() -> None:
    testy = Pwgen()
    print(f"test_pwgen() -> {test_pwgen(testy)}")
    test_print_command(testy)
    


if (__name__ == "__main__"):
   main()

