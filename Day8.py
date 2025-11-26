from typing import Union

Number = Union[int, float]


def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> float:
    return x / y


def modulus(x: int, y: int) -> Number:
    return x % y


def floor_divide(x: int, y: int) -> Number:
    return x // y


print("Sum of a & b : ", add(20, 10))
print("Sub of a & b : ", subtract(20, 10))
print("mul of a & b : ", multiply(20, 10))
print("Module of a & b: ", modulus(20, 10))      # modulus operator
print("Divide of a & b: ", floor_divide(20, 10))     # floor division
print("Divide of a & b: ", divide(20, 10))     # division
