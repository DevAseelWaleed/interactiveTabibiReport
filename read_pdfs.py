# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))

# Read the big PDF
import pymupdf
pdf_files = [f for f in os.listdir(base_dir) if f.endswith('.pdf')]
for pdf_file in pdf_files:
    full_path = os.path.join(base_dir, pdf_file)
    doc = pymupdf.open(full_path)
    print(f"\n{'='*60}")
    print(f"PDF: {pdf_file} ({len(doc)} pages)")
    print('='*60)
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        if text.strip():
            print(f"\n--- Page {page_num+1} ---")
            print(text[:3000])
