import sys
from pysideuic import compileUi


def convert(ui_file):
    output_file = ".".join(ui_file.split(".")[:-1]) + ".py"
    with open(output_file, "w") as fp:
        compileUi(ui_file, fp, False, 4, False)

if __name__ == "__main__" and len(sys.argv) == 2:
    convert(sys.argv[1])
