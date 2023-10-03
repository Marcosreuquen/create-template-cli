import argparse
import os
import shutil
import json

parser = argparse.ArgumentParser(description="API Template Generator")
parser.add_argument(
    "--type",
    choices=["restful", "express"],
    required=True,
    help="API type")
parser.add_argument(
    "--output",
    required=False,
    help="Output directory",
    default="./dist")
args = parser.parse_args()


def create_dist_folder(dist_folder="./dist"):
    if os.path.exists(dist_folder):
        # Delete the existing "./dist" folder and its contents
        shutil.rmtree(dist_folder)

    # Create a new "./dist" folder
    os.makedirs(dist_folder, exist_ok=True)


def create_directory_structure_from_json(data, base_dir="."):
    for item in data:
        if isinstance(item, dict):
            name = item.get("name")
            item_type = item.get("type")
            values = item.get("values", None)

            path = os.path.join(base_dir, name)

            if item_type == "folder":
                os.makedirs(path, exist_ok=True)
                if values:
                    create_directory_structure_from_json(values, path)
            elif item_type == "file":
                with open(path, "w") as f:
                    if values:
                        f.write(values)
        elif isinstance(item, str):
            # Handle plain strings as folder names
            path = os.path.join(base_dir, item)
            os.makedirs(path, exist_ok=True)


if __name__ == "__main__":
    args = parser.parse_args()
    create_dist_folder(args.output)
    with open("./templates/{}.json".format(args.type), "r") as json_file:
        directory_structure_json = json.load(json_file)
    create_directory_structure_from_json(directory_structure_json, args.output)
    pass
