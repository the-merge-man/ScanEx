import logging
import re
import pandas as pd

class IntakeSheetParser:
    """
    Ingests raw digital text blocks, parses item features using regular expressions, 
    and handles downstream Excel compilation.
    """
    def __init__(self, text_content: str):
        self.text_content = text_content
        self.extracted_records = []

    def parse_text_stream(self) -> list:
        """Scans string lines looking for structured logistics entries."""
        logging.info("Processing structural text metrics via pattern matching...")
        
        item_regex = re.compile(r"ITEM:\s*(.*?)\s*\|")
        weight_regex = re.compile(r"WEIGHT:\s*([\d\.]+)\s*lbs")
        exp_regex = re.compile(r"EXP:\s*([\d\-\/]+)")

        # Split text content block by newlines to iterate through lines
        lines = self.text_content.split('\n')

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if "ITEM:" in line:
                item_match = item_regex.search(line)
                weight_match = weight_regex.search(line)
                exp_match = exp_regex.search(line)

                if item_match and weight_match and exp_match:
                    self.extracted_records.append({
                        "Item Description": item_match.group(1).strip(),
                        "Weight (lbs)": float(weight_match.group(1).strip()),
                        "Expiration Date": exp_match.group(1).strip()
                    })
                else:
                    if line: # Avoid empty padding log warnings
                        logging.warning(f"Line {line_num} failed layout structure validation: '{line}'")
                        
        logging.info(f"Extracted {len(self.extracted_records)} valid line records from scanned document.")
        return self.extracted_records

    def export_to_excel(self, output_excel_path: str):
        """Generates clear, tabular Excel documents using OpenPyXL engine layers."""
        if not self.extracted_records:
            logging.error("Export canceled: No matching item records available.")
            return

        df = pd.DataFrame(self.extracted_records)
        logging.info(f"Writing dataset to relational spreadsheet grid...")
        
        with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Intake Logs', index=False)
            
        logging.info(f"Spreadsheet upload pipeline completed successfully! Saved to {output_excel_path}")
