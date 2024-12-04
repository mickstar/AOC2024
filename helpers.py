def abs(x: int) -> int:
    if x < 0:
        return -x
    return x


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines() if x.strip() != ""]

def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()