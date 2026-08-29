# -*- coding: utf-8 -*-
"""
Update KPI: تنويع مصادر الدخل الذاتي to 100.00% (مكتمل) across all deliverables:
- Target: 6 sources | H1 Target: 6 sources | Actual: 6 active sources achieved (6/6 = 100%)
- Status: مكتمل
- Notes: تفعيل ٦ مصادر دخل متنوعة (تبرعات، زكاة، علاج، متجر، منصات، اشتراكات عضوية)
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

dash_code = dash_code.replace(
    '<td><strong>تنويع مصادر الدخل الذاتي</strong></td>\n                        <td>عدد مصادر الدخل</td>\n                        <td>٦ مصادر</td>\n                        <td>٦ مصادر</td>\n                        <td>٦ مصادر نشطة</td>\n                        <td><span class="tag-pill tag-warning">٦٦.٦٧٪</span></td>\n                        <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>\n                        <td>تفعيل المتجر، الزكاة، العضوية، وكبار المانحين، وبدء نوى</td>',
    '<td><strong>تنويع مصادر الدخل الذاتي</strong></td>\n                        <td>عدد مصادر الدخل</td>\n                        <td>٦ مصادر</td>\n                        <td>٦ مصادر</td>\n                        <td>٦ مصادر نشطة ومحققة</td>\n                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>\n                        <td><span class="badge-pill bg-green">مكتمل</span></td>\n                        <td>تفعيل ٦ قنوات دخل (تبرعات، زكاة، علاج، متجر، منصات، عضوية)</td>'
)

with open(v2_file, "w", encoding="utf-8") as f:
    f.write(dash_code)
print("Updated generate_v2_dashboard.py with 100% income diversity.")

# 2. Update generate_full_14_slides_pptx.py
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

pptx_code = pptx_code.replace(
    '("معايير الحوكمة ومنصة نوى", "١٠٠٪", "بدء الملف", "قيد الاستعانة باستشاري", "جاري العمل", "قيد التنفيذ")',
    '("معايير الحوكمة ومنصة نوى", "١٠٠٪", "بدء الملف", "قيد الاستعانة باستشاري", "جاري العمل", "قيد التنفيذ"),\n        ("تنويع مصادر الدخل الذاتي", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "١٠٠.٠٠٪", "مكتمل")'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated generate_full_14_slides_pptx.py.")

# 3. Update Web Slides (generate_web_slides.py)
web_file = os.path.join(base_dir, "generate_web_slides.py")
with open(web_file, "r", encoding="utf-8") as f:
    web_code = f.read()

web_code = web_code.replace(
    '<td><strong>تنويع مصادر الدخل</strong></td>\n                            <td>٦ مصادر</td>\n                            <td>٦ مصادر</td>\n                            <td>٦ مصادر نشطة</td>\n                            <td>٦٦.٦٧٪</td>\n                            <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>',
    '<td><strong>تنويع مصادر الدخل</strong></td>\n                            <td>٦ مصادر</td>\n                            <td>٦ مصادر</td>\n                            <td>٦ مصادر نشطة</td>\n                            <td>١٠٠.٠٠٪</td>\n                            <td><span class="badge-pill bg-green">مكتمل</span></td>'
)

with open(web_file, "w", encoding="utf-8") as f:
    f.write(web_code)
print("Updated generate_web_slides.py.")

# 4. Update Word Document builder (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    word_code = f.read()

word_code = word_code.replace(
    '("١٠", "تنويع مصادر الدخل الذاتي", "عدد مصادر الدخل", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "٦٦.٦٧٪", "قيد التنفيذ")',
    '("١٠", "تنويع مصادر الدخل الذاتي", "عدد مصادر الدخل", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "١٠٠.٠٠٪", "مكتمل")'
)

with open(word_file, "w", encoding="utf-8") as f:
    f.write(word_code)
print("Updated enrich_word_and_presentations.py.")

# Re-run all generators
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{web_file}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated successfully with 100% KPI!")
