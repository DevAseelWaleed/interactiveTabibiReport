# -*- coding: utf-8 -*-
"""
Update Program 7: "عون" to "مفعل ونشط" across all deliverables:
- Program: ٧. عون
- Objective: توفير الأدوية والرعاية المستدامة لمرضى الأمراض المزمنة
- Target Beneficiaries: المرضى المزمنون والأشد حاجة
- Actual Achievement H1: تفعيل المبادرة ورفع مشروع رعاية مرضى الأمراض المزمنة وتوفير الدواء (مؤسسة الشاوي والجهات المانحة)
- Status: مفعل ونشط (شارة خضراء)
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

old_awn_html = """                    <tr>
                        <td><strong>٧. عون</strong></td>
                        <td>إعانات ومخصصات شهرية للأمراض المزمنة</td>
                        <td>المرضى المزمنون</td>
                        <td>لم تُصرف إعانات شهرية دورية</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>"""

new_awn_html = """                    <tr style="background:rgba(46, 125, 50, 0.06);">
                        <td><strong>٧. عون</strong></td>
                        <td>توفير الأدوية والرعاية المستدامة لمرضى الأمراض المزمنة</td>
                        <td>المرضى المزمنون والأشد حاجة</td>
                        <td><strong>تفعيل المبادرة ورفع مشروع رعاية مرضى الأمراض المزمنة وتوفير الدواء (الشاوي والمانحين)</strong></td>
                        <td><span class="badge-pill bg-green">مفعل ونشط</span></td>
                    </tr>"""

if old_awn_html in dash_code:
    dash_code = dash_code.replace(old_awn_html, new_awn_html)
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Updated generate_v2_dashboard.py: عون -> مفعل ونشط")
else:
    print("Could not find exact awn row in generate_v2_dashboard.py")

# 2. Update Word builder (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    word_code = f.read()

# Check if programs mention exists in Word
if "برنامج جودة حياة" in word_code:
    word_code = word_code.replace(
        "برنامج جودة حياة (تغطية العمليات الجراحية)",
        "برنامجا (جودة حياة لتغطية العمليات الجراحية، وعون لتوفير أدوية الأمراض المزمنة والرعاية المستدامة)"
    )
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(word_code)
    print("Updated enrich_word_and_presentations.py with active Awn program.")

# 3. Update PowerPoint (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

pptx_code = pptx_code.replace(
    "البرامج والخدمات الطبية للمرضى (برنامج جودة حياة)",
    "البرامج والخدمات الطبية للمرضى (برنامجا جودة حياة & عون)"
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated generate_full_14_slides_pptx.py.")

# Re-run all generators
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated successfully with active 'Awn' program!")
