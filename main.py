from core.scanner import FileScanner

def main():
    folder_path = r"C:\Users\Administrator\Documents\test_folder"
    scanner = FileScanner(folder_path)

    print("\n🔍 Scanning files...\n")
    count = 0

    for metadata in scanner.scan():  # Generator in action
        count += 1
        print(f"📄 {metadata['name']} ({metadata['size_kb']} KB, {metadata['extension']})")
        print(f"   Path: {metadata['path']}")
        print(f"   Created: {metadata['created']}")
        print(f"   Preview: {metadata['preview']}")
        print("-" * 50)

    print(f"\n✅ Total files scanned: {count}")

if __name__ == "__main__":
    main()
