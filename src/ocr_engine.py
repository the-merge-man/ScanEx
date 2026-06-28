import os
import logging
from PIL import Image
import pytesseract

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PhysicalCopyScanner:
    """
    Handles image preprocessing and Optical Character Recognition (OCR) 
    to extract string blocks from physical document photographs or scans.
    """
    def __init__(self, image_path: str):
        self.image_path = image_path

    def scan_to_text(self) -> str:
        """Loads physical document and runs OCR engine extraction."""
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"No scanned document image found at: {self.image_path}")
            
        logging.info(f"Optical scanner ingesting physical image: {self.image_path}")
        
        try:
            # Open physical copy scan using Pillow
            img = Image.open(self.image_path)
            
            # Execute standard Tesseract OCR extraction engine
            # --psm 6 tells the engine to assume a uniform block of text layout
            raw_text = pytesseract.image_to_string(img, config='--psm 6')
            
            logging.info("Physical copy text layer successfully rasterized.")
            return raw_text
            
        except Exception as e:
            logging.error(f"Critical failure during OCR image processing: {e}")
            raise e
