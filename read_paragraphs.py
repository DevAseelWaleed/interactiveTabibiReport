# -*- coding: utf-8 -*-
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))

from docx import Document

# Find the docx file
docx_files = [f for f in os.listdir(base_dir) if f.endswith('.docx')]

for docx_file in docx_files:
    full_path = os.path.join(base_dir, docx_file)
    print(f"\n{'='*60}")
    print(f"READING: {docx_file}")
    print('='*60)
    doc = Document(full_path)
    
    print("\n--- PARAGRAPHS ---")
    for i, para in enumerate(doc.paragraphs):
        if para.text.strip():
            print(f"P{i}: [{para.style.name}] {para.text}")
