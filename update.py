"""
Update the datasets from the metadata harmoinzer
"""

from argparse import ArgumentParser
import rich
import os


def sys_command(cmd):
    if os.system(cmd) != 0:
        rich.print(f"[red]Error when executing command '{cmd}'")
        exit(1)

if __name__ == "__main__":
    argparser = ArgumentParser()
    argparser.add_argument("-m", "--metadata-harmonizer", type=str, help="Metadata harmonizer project path", default="../metadata-harmonizer")
    args = argparser.parse_args()

    if not os.path.isdir(args.metadata_harmonizer):
        rich.print("f[red]Could not find metadata harmonizer project!")
        exit(1)

    rich.print("removing datasets...")
    sys_command("rm -rf ./datasets")
    rich.print("copy new datasets...")
    sys_command(f"cp -r {args.metadata_harmonizer}/tests/datasets .")
    rich.print("copy new datasets.xml...")
    sys_command(f"cp {args.metadata_harmonizer}/tests/conf/datasets.xml conf/datasets.xml")
    rich.print(f"[green]done!")