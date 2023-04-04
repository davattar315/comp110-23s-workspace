"""read lines of data."""


from io import TextIOWrapper 


def read_lines(filename: str) -> list[str]:
    """Read a .txt file into a list of strings for each line."""
    lines: list[str] = []
    file_handle = open(filename, "r")
    file_handle: TextIOWrapper = open(filename, "r")
    for line in filename:
        # strip trailing whitespace
        line = line.strip()
        # make everything lowercase 
        lines.append(line)
        return lines 
