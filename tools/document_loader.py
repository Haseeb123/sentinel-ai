"""
Document Loader

Loads supported document formats for SentinelAI.
"""

from pathlib import Path

from pypdf import PdfReader


class DocumentLoader:
    """
    Utility class for loading documents.
    """

    SUPPORTED_TYPES = {
        ".txt",
        ".md",
        ".json",
        ".pdf",
    }

    def load(self, file_path: str) -> str:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} does not exist.")

        suffix = path.suffix.lower()

        if suffix not in self.SUPPORTED_TYPES:
            raise ValueError(f"Unsupported file type: {suffix}")

        if suffix == ".pdf":
            return self._load_pdf(path)

        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    def _load_pdf(self, path: Path) -> str:

        reader = PdfReader(path)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)
