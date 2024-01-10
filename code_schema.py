import argparse

parser = argparse.ArgumentParser(description='Script so useful.')
parser.add_argument("--changed_files", type=str, default="")

args = parser.parse_args()

changed_files_value = args.changed_files
if len(changed_files_value) != 0:
    for file_name in changed_files_value.split(","):
        f = open(file_name, "r")
        print(f.read())
        f.close()
