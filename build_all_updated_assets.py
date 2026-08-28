# -*- coding: utf-8 -*-
"""
Build all updated deliverables with verified strategic audit findings for Tabibi Civil Association H1 2026.
"""
import sys, os, shutil

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")
v1_dir = os.path.join(base_dir, "التقرير_الجديد")

print("Building all updated deliverables...")
