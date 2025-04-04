import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )
    if __name__ == "__main__":
        # Ensure the public directory exists
        os.makedirs("public", exist_ok=True)
        
        # Copy static files (if this isn't already done elsewhere)
        # ... code to copy static files ...
        
        # Generate HTML pages from markdown
        generate_pages_recursive("content", "template.html", "public")


main()