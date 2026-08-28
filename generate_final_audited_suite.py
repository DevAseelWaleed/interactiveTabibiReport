# -*- coding: utf-8 -*-
"""
This script generates the complete updated deliverables for Tabibi Civil Association H1 2026:
1. generate_v2_dashboard.py -> index.html
2. generate_v2_all_deliverables.py -> Word .docx and PowerPoint .pptx
3. generate_web_slides.py -> presentation.html
"""
import sys, os, subprocess

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")

print("Generating and running all updated deliverables...")
