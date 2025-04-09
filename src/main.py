import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    
    if __name__ == "__main__":
        # Ensure the public directory exists
        os.makedirs("public", exist_ok=True)
        
        # Copy static files (if this isn't already done elsewhere)
        # ... code to copy static files ...
        
        # Generate HTML pages from markdown
        generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()