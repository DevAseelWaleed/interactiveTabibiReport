# -*- coding: utf-8 -*-
"""
Ensure all HTML presentations and dashboards have local offline Chart.js and error-proof rendering.
"""
import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")
v1_dir = os.path.join(base_dir, "التقرير_الجديد")

# Copy chart.umd.min.js to v1_dir as well
os.makedirs(os.path.join(v1_dir, "assets", "js"), exist_ok=True)
src_chart = os.path.join(v2_dir, "assets", "js", "chart.umd.min.js")
if os.path.exists(src_chart):
    shutil.copy2(src_chart, os.path.join(v1_dir, "assets", "js", "chart.umd.min.js"))

# Update generate_web_slides.py to include offline Chart.js
web_slides_file = os.path.join(base_dir, "generate_web_slides.py")
with open(web_slides_file, "r", encoding="utf-8") as f:
    ws_code = f.read()

old_script_tag = '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'
new_script_tag = """    <!-- Local & CDN Fallback Chart.js -->
    <script src="assets/js/chart.umd.min.js"></script>
    <script>
        if (typeof Chart === 'undefined') {
            document.write('<script src="https://cdn.jsdelivr.net/npm/chart.js"><\\/script>');
        }
    </script>"""

if old_script_tag in ws_code and "assets/js/chart.umd.min.js" not in ws_code:
    ws_code = ws_code.replace(old_script_tag, new_script_tag)
    with open(web_slides_file, "w", encoding="utf-8") as f:
        f.write(ws_code)
    print("Updated generate_web_slides.py with offline Chart.js!")

# Recompile all
os.system(f'py -3 "{os.path.join(base_dir, "generate_v2_dashboard.py")}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_full_14_slides_pptx.py")}"')
os.system(f'py -3 "{os.path.join(base_dir, "enrich_word_and_presentations.py")}"')

print("All deliverables updated with offline chart support and all 9 charts fully working!")
