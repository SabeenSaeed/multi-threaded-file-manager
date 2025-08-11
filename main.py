import json
from core.scanner import FileScanner
from core.tagger import tag_files

def main():
    # 1️⃣ Scan files
    scanner = FileScanner("C:/Users/Administrator/Documents/test_folder")
    all_files = list(scanner.scan())

    print(f"Total files found: {len(all_files)}\n")

    # 2️⃣ Tag files
    tagged_files = tag_files(all_files)

    # 3️⃣ Convert to dictionary format
    result = {
        f["name"]: {
            "tags": f["tags"],
            "size_kb": f["size_kb"],
            "created": f["created"],
            "preview": f["preview"],
        }
        for f in tagged_files
    }

    # 4️⃣ Pretty print as clean JSON
    print(json.dumps(result, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
