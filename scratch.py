import re

if __name__ == "__main__":
    s = "Age: 56\n" \
        "js;lafjl;fdsa"
    x = re.search(r"Age:(.*)\n", s)
    result = str.strip(x.group(1))
    print(result)

