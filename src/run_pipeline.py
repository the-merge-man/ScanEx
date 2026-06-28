import os
from PIL import Image, ImageDraw
from src.ocr_engine import PhysicalCopyScanner
from src.parser_engine import IntakeSheetParser

def create_mock_scanned_image_fallback(target_img_path: str):
    """Generates a dummy png file if no real scan is uploaded yet."""
    if not os.path.exists(target_img_path):
        os.makedirs(os.path.dirname(target_img_path), exist_ok=True)
        # Create a white canvas to serve as digital "paper"
        img = Image.new('RGB', (800, 300), color='white')
        d = ImageDraw.Draw(img)
        
        # Write clean synthetic print onto the canvas to test out the logic pipeline
        d.text((10, 10), "SHEET ID: 104-IH", fill='black')
        d.text((10, 40), "ITEM: Fresh Fruits Box   | WEIGHT: 18.5 lbs | EXP: 2026-07-02", fill='black')
        d.text((10, 70), "ITEM: Canned Vegetables  | WEIGHT: 52.1 lbs | EXP: 2026-12-01", fill='black')
        d.text((10, 100), "ITEM: Artisan Sourdough  | WEIGHT: 08.4 lbs | EXP: 2026-06-29", fill='black')
        
        img.save(target_img_path)

if __name__ == "__main__":
    # Path settings
    INPUT_SCAN = os.path.join("data", "scanned_page.png")
    OUTPUT_EXCEL = os.path.join("data", "island_harvest_intake.xlsx")

    # 1. Build test mock image file if no real scan is placed inside the directory
    create_mock_scanned_image_fallback(INPUT_SCAN)

    # 2. Extract text from the physical layout file using OCR
    scanner = PhysicalCopyScanner(image_path=INPUT_SCAN)
    raw_text_stream = scanner.scan_to_text()

    # 3. Parse the data strings directly into formatted Excel rows
    parser = IntakeSheetParser(text_content=raw_text_stream)
    parser.parse_text_stream()
    parser.export_to_excel(output_excel_path=OUTPUT_EXCEL)
