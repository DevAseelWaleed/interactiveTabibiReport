# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))

from docx import Document

docx_files = [f for f in os.listdir(base_dir) if f.endswith('.docx')]

for docx_file in docx_files:
    full_path = os.path.join(base_dir, docx_file)
    print(f"\n{'='*60}")
    print(f"TABLES IN: {docx_file}")
    print('='*60)
    doc = Document(full_path)
    
    for t_idx, table in enumerate(doc.tables):
        print(f"\n  Table {t_idx} ({len(table.rows)}x{len(table.columns)}):")
        for r_idx, row in enumerate(table.rows):
            cells = [cell.text.strip().replace('\n', ' | ') for cell in row.cells]
            print(f"    R{r_idx}: {cells}")
