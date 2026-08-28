# -*- coding: utf-8 -*-
"""
Build and execute the fully updated suite of deliverables with all verified strategic audit findings.
"""
import sys, os, shutil
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")
v1_dir = os.path.join(base_dir, "التقرير_الجديد")

print("Generating fully updated deliverables...")
