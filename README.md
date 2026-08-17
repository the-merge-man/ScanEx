# ScanEx

Turns handwritten food-assistance check-in sheets into clean,
cross-checked spreadsheet data, flagging anything that needs
a human's eyes before it's trusted.

**Status:** 🚧 early development — core pipeline isn't functional yet.

## The problem

Food-assistance programs still rely heavily on paper sign-in sheets to
track who received aid. Verifying and transcribing those sheets by hand
(checking for errors, catching duplicates, typing every row into a
spreadsheet, etc) is slow and repetitive, and it eats hours that staff
usually don't have to spare.

ScanEx is meant to take that transcription work off someone's plate.
Feed it a scanned or photographed sign-in sheet, and it extracts the
data into a spreadsheet automatically, flagging anything that looks
uncertain: a smudged checkbox, a missing field, a duplicate name, so
a person only has to review the entries that actually need a second
look, instead of retyping the whole sheet.

## How it's meant to work:
PDF -> Image Extraction -> table/cell detection -> OCR -> validation/flagging -> Excel sheet export
Each stage is being built and tested independently before they're
wired together — see the roadmap below for where things currently stand.

## Getting started

### System dependencies
- `tesseract-ocr`
- `poppler-utils`

### Python environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Roadmap

- [ ] PDF → image conversion
- [ ] Table/cell layout detection
- [ ] OCR extraction
- [ ] Checkbox detection
- [ ] Excel export
- [ ] Validation / flagging rules
- [ ] API wrapper
- [ ] Front end
- [ ] Export formats beyond Excel (CSV, JSON)
- [ ] Integration hooks for downstream systems (e.g. case management
      databases) — exploratory, not yet implemented

## A note on data privacy

This repo only ever ships with synthetic, made-up sample sheets —
no real personal or case data. Given what this tool touches, that's
a hard rule for this project, not just a formality.
