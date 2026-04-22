# test_somar.py

from app import somar

def test_somar():
    assert somar(2, 3) == 5

# Com pytest não é preciso isto.
if __name__ == "__main__":
    test_somar()
