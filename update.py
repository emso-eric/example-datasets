"""
Update the datasets from the metadata harmoinzer
"""

from argparse import ArgumentParser
import rich
import os


if __name__ == "__main__":
    argparser = ArgumentParser()
    argparser.add_argument("-m", "--metadata-harmonizer", type=str, help="Metadata harmonizer project path", default="../metadata-harmonizer")
    args = argparser.parse_args()

    if not os.path.isdir(args.metadata_harmonizer):
        rich.print("f[red]Could not find metadata harmonizer project!")
        exit(1)

    rich.print("removing datasets...")
    os.system("rm -rf ./datasets")
    rich.print("copy new datasets...")
    os.system(f"cp -r {args.metadata_harmonizer}/tests/datasets .")