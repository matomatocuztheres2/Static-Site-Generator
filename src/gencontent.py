import os
from blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    print("Generated HTML:", html)
    print("Markdown content:", markdown_content)


    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_pages_recursive(content_dir, template_path, dest_dir):
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                # Get the relative path from content_dir
                from_path = os.path.join(root, file)
                # Create corresponding path in dest_dir
                rel_path = os.path.relpath(from_path, content_dir)
                rel_dir = os.path.dirname(rel_path)
                
                # Convert index.md to index.html, preserving the directory structure
                if file == "index.md":
                    dest_path = os.path.join(dest_dir, rel_dir, "index.html")
                else:
                    # For non-index files, just change extension
                    dest_path = os.path.join(dest_dir, os.path.splitext(rel_path)[0] + '.html')
                
                # Call generate_page
                generate_page(from_path, template_path, dest_path)
