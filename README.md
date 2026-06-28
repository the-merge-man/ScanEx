# ScanEx
## Island Harvest Automated Document Intake Pipeline

An automated data pipeline designed to scan, analyze, and upload community relief intake forms directly into an organized Excel database format from a physical paper copy.

##  How It Works
1. **Ingest & Rasterize:** Accepts image captures (`.png`, `.jpg`) of physical handwritten or typed paper forms.
2. **OCR Engine:** Leverages Tesseract OCR (`pytesseract`) to translate visual layouts into raw string arrays.
3. **Data Regularization:** Uses regex token layers to parse item specs, weights, and dates while stripping layout anomalies.
4. **Excel Sync:** Exports sanitized vectors directly to functional target tables via `openpyxl`.
