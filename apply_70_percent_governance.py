# -*- coding: utf-8 -*-
"""
Update Governance & Compliance (معايير الحوكمة ومنصة نوى) to 70.00% across all deliverables:
- Annual Target: 100%
- H1 Target: 50%
- Actual Achievement: استيفاء ٧٠٪ من معايير الحوكمة والسياسات المعتمدة
- Achievement Rate H1: 70.00% (or 140.0% vs H1 target) -> 70.00%
- Status: متقدم وجيد جداً (شارة خضراء)
- Recalculate Governance Perspective to 92.50% (13.88 / 15)
- Recalculate Overall Weighted BSC Score to 52.12%
- Rebuild index.html, presentation.html, Word .docx, and PowerPoint .pptx
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

# Replace Governance card and overall score in dashboard
dash_code = dash_code.replace(
    'محور الحوكمة والمؤسسية (١٥٪)</div>\n                <div style="font-size:1.8rem; font-weight:900; color:var(--success); margin-bottom:6px;">٦٠.٠٠٪</div>\n                <div style="font-size:0.85rem; color:var(--text-muted);">٩.٠٠ من ١٥ نقطة',
    'محور الحوكمة والمؤسسية (١٥٪)</div>\n                <div style="font-size:1.8rem; font-weight:900; color:var(--success); margin-bottom:6px;">٩٢.٥٠٪</div>\n                <div style="font-size:0.85rem; color:var(--text-muted);">١٣.٨٨ من ١٥ نقطة'
)
dash_code = dash_code.replace(
    'نسبة الإنجاز الاستراتيجي الإجمالية: <span style="color:var(--secondary-light); font-weight:900;">٤١.٧٣٪</span>',
    'نسبة الإنجاز الاستراتيجي الإجمالية: <span style="color:var(--secondary-light); font-weight:900;">٥٢.١٢٪</span>'
)

# Update row in matrix table
old_gov_row = """                    <tr>
                        <td>٩</td>
                        <td><strong>معايير الحوكمة ومنصة نوى</strong></td>
                        <td>استيفاء معايير الحوكمة</td>
                        <td>١٠٠٪</td>
                        <td>بدء ملف الحوكمة</td>
                        <td>قيد الاستعانة باستشاري</td>
                        <td><span class="tag-pill tag-warning">جاري العمل</span></td>
                        <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>
                        <td>طلب موازنة استشارية (١٥-٢١ ألف ر.س) لاستكمال ملف الحوكمة ونوى</td>
                    </tr>"""

new_gov_row = """                    <tr>
                        <td>٩</td>
                        <td><strong>معايير الحوكمة ومنصة نوى</strong></td>
                        <td>استيفاء معايير الحوكمة</td>
                        <td>١٠٠٪</td>
                        <td>٥٠٪</td>
                        <td>استيفاء ٧٠٪ من المعايير والسياسات</td>
                        <td><span class="tag-pill tag-success">٧٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">متقدم ومتميز</span></td>
                        <td>اعتماد القوائم والسياسات والموقع، وجاري إنهاء نوى عبر الاستشاري</td>
                    </tr>"""

if old_gov_row in dash_code:
    dash_code = dash_code.replace(old_gov_row, new_gov_row)
else:
    # Alternative replace
    dash_code = dash_code.replace(
        '<td><strong>معايير الحوكمة ومنصة نوى</strong></td>\n                        <td>استيفاء معايير الحوكمة</td>\n                        <td>١٠٠٪</td>\n                        <td>بدء ملف الحوكمة</td>\n                        <td>قيد الاستعانة باستشاري</td>\n                        <td><span class="tag-pill tag-warning">جاري العمل</span></td>\n                        <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>\n                        <td>طلب موازنة استشارية (١٥-٢١ ألف ر.س) لاستكمال ملف الحوكمة ونوى</td>',
        '<td><strong>معايير الحوكمة ومنصة نوى</strong></td>\n                        <td>استيفاء معايير الحوكمة</td>\n                        <td>١٠٠٪</td>\n                        <td>٥٠٪</td>\n                        <td>استيفاء ٧٠٪ من المعايير والسياسات</td>\n                        <td><span class="tag-pill tag-success">٧٠.٠٠٪</span></td>\n                        <td><span class="badge-pill bg-green">متقدم ومتميز</span></td>\n                        <td>اعتماد القوائم والسياسات والموقع، وجاري إنهاء نوى عبر الاستشاري</td>'
    )

with open(v2_file, "w", encoding="utf-8") as f:
    f.write(dash_code)
print("Updated generate_v2_dashboard.py with 70% Governance!")

# 2. Update generate_full_14_slides_pptx.py
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

pptx_code = pptx_code.replace(
    '("محور الحوكمة والمؤسسية (١٥٪)", "٦٠.٠٠٪", "٩.٠٠ من ١٥ نقطة\\n١٠٠٪ توطين وتطبيق نظام قيود السحابي", C_SUCCESS, 9.8)',
    '("محور الحوكمة والمؤسسية (١٥٪)", "٩٢.٥٠٪", "١٣.٨٨ من ١٥ نقطة\\nتحقيق ٧٠٪ من معايير الحوكمة و١٠٠٪ توطين", C_SUCCESS, 9.8)'
)
pptx_code = pptx_code.replace(
    'نسبة الإنجاز الاستراتيجي الإجمالية الموزونة: ٤١.٧٣٪',
    'نسبة الإنجاز الاستراتيجي الإجمالية الموزونة: ٥٢.١٢٪'
)
pptx_code = pptx_code.replace(
    '("معايير الحوكمة ومنصة نوى", "١٠٠٪", "بدء الملف", "قيد الاستعانة باستشاري", "جاري العمل", "قيد التنفيذ")',
    '("معايير الحوكمة ومنصة نوى", "١٠٠٪", "٥٠٪", "استيفاء ٧٠٪ من المعايير", "٧٠.٠٠٪", "متقدم")'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated generate_full_14_slides_pptx.py.")

# 3. Update Web Slides (generate_web_slides.py)
web_file = os.path.join(base_dir, "generate_web_slides.py")
with open(web_file, "r", encoding="utf-8") as f:
    web_code = f.read()

web_code = web_code.replace(
    '<div class="card-label">الحوكمة والمؤسسية (١٥٪)</div>\n                    <div class="card-val" style="color:var(--success);">٦٠.٠٠٪</div>\n                    <div style="font-size:0.8rem; color:var(--text-muted);">٩.٠٠ من ١٥',
    '<div class="card-label">الحوكمة والمؤسسية (١٥٪)</div>\n                    <div class="card-val" style="color:var(--success);">٩٢.٥٠٪</div>\n                    <div style="font-size:0.8rem; color:var(--text-muted);">١٣.٨٨ من ١٥'
)
web_code = web_code.replace(
    '٤١.٧٣٪ <small style="font-size:1rem; font-weight:400; opacity:0.9;">(تحسن ملحوظ بعد تعديل المستهدف المالي إلى ١.٥ مليون)</small>',
    '٥٢.١٢٪ <small style="font-size:1rem; font-weight:400; opacity:0.9;">(أداء متقدم وتجاوز نصف المستهدفات المعتمدة)</small>'
)
web_code = web_code.replace(
    '<td><strong>معايير الحوكمة ومنصة نوى</strong></td>\n                            <td>١٠٠٪</td>\n                            <td>بدء الملف</td>\n                            <td>قيد الاستعانة باستشاري</td>\n                            <td>جاري العمل</td>\n                            <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>',
    '<td><strong>معايير الحوكمة ومنصة نوى</strong></td>\n                            <td>١٠٠٪</td>\n                            <td>٥٠٪</td>\n                            <td>استيفاء ٧٠٪ من المعايير</td>\n                            <td>٧٠.٠٠٪</td>\n                            <td><span class="badge-pill bg-green">متقدم</span></td>'
)

with open(web_file, "w", encoding="utf-8") as f:
    f.write(web_code)
print("Updated generate_web_slides.py.")

# 4. Update Word Document Builder (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    word_code = f.read()

word_code = word_code.replace(
    "('٤. محور الحوكمة والقدرات المؤسسية', '١٥٪', '٦٠.٠٠٪', '٩.٠٠ من ١٥')",
    "('٤. محور الحوكمة والقدرات المؤسسية', '١٥٪', '٩٢.٥٠٪', '١٣.٨٨ من ١٥')"
)
word_code = word_code.replace(
    "('الإجمالي العام الموزون للأداء الاستراتيجي (H1 2026)', '١٠٠٪', '٤١.٧٣٪', '٤١.٧٣ من ١٠٠ (بعد مواءمة المستهدف)')",
    "('الإجمالي العام الموزون للأداء الاستراتيجي (H1 2026)', '١٠٠٪', '٥٢.١٢٪', '٥٢.١٢ من ١٠٠ (أداء متقدم ومتميز)')"
)
word_code = word_code.replace(
    '("٩", "معايير الحوكمة ومنصة نوى", "نسبة الامتثال", "١٠٠٪", "بدء الملف", "قيد الاستعانة باستشاري", "جاري العمل", "قيد التنفيذ")',
    '("٩", "معايير الحوكمة ومنصة نوى", "نسبة الامتثال", "١٠٠٪", "٥٠٪", "استيفاء ٧٠٪ من المعايير", "٧٠.٠٠٪", "متقدم ومتميز")'
)

with open(word_file, "w", encoding="utf-8") as f:
    f.write(word_code)
print("Updated enrich_word_and_presentations.py.")

# Re-run all generators
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{web_file}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated successfully with 70% Governance and 52.12% Overall BSC Score!")
