import os

SOURCE_DIR = "docs/news"
OUTPUT_FILE = "docs/news.md"

# List and sort files (reverse = newest first)
entries = sorted(os.listdir(SOURCE_DIR), reverse=True)

with open(OUTPUT_FILE, "w") as out:
    out.write("---\nsearch:\nexclude: true\n---\n\n---\n\n")

    for fname in entries:
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(SOURCE_DIR, fname), "r") as f:
            content = f.read().strip()
            out.write(content)
            out.write("\n\n---\n")