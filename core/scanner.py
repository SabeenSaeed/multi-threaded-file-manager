from pathlib import Path
from datetime import datetime
from docx import Document
import PyPDF2
from PIL import Image   # Pillow for image handling

class FileScanner:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)

    def scan(self):
        """Generator that yields metadata for each file."""
        for file_path in self.root_dir.rglob('*'):
            if file_path.is_file():
                yield self.get_metadata(file_path)

    def get_metadata(self, file_path):
        stat = file_path.stat()
        return {
            'name': file_path.name,
            'path': str(file_path),
            'size_kb': round(stat.st_size / 1024, 2),
            'created': datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            'extension': file_path.suffix.lower(),
            'preview': self.get_text_preview(file_path)
        }

    def get_text_preview(self, file_path, max_chars=200):
        ext = file_path.suffix.lower()
        try:
            if ext == '.txt':
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read(max_chars).strip()

            elif ext == '.docx':
                doc = Document(file_path)
                text = '\n'.join([p.text for p in doc.paragraphs])
                return text[:max_chars].strip()

            elif ext == '.pdf':
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    text = ''
                    for page in reader.pages[:2]:
                        text += page.extract_text() or ''
                    return text[:max_chars].strip()

            elif ext in ('.jpg', '.jpeg', '.png', '.gif'):
                img = Image.open(file_path)
                return f"[Image: {img.format}, {img.size[0]}x{img.size[1]} px, Mode: {img.mode}]"

            else:
                return "[No preview available for this file type]"

        except Exception as e:
            return f"[Error reading file: {e}]"
