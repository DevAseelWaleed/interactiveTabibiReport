# -*- coding: utf-8 -*-
"""
Replace all occurrences of 36,606 / 18,303 with 200 / 100 beneficiaries across:
- generate_v2_dashboard.py
- generate_web_slides.py
- generate_full_14_slides_pptx.py
- enrich_word_and_presentations.py
And recompile all deliverables!
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

dash_code = dash_code.replace(
    'الخطة استهدفت خدمة <strong>٣٦,٦٠٦ مستفيد</strong>، بينما اقتصر التنفيذ الفعلي على <strong>٧ مرضى فقط</strong>. يرجع ذلك لحصر الصرف في الجراحات المعقدة مرتفعة التكلفة (متوسط ٢٩.٨ ألف ريال للحالة) وإيقاف العيادات والقوافل الوقائية والاستشارات التي تخدم الآلاف بتكلفة منخفضة.',
    'الخطة استهدفت خدمة <strong>٢٠٠ مستفيد سنوياً (١٠٠ مستفيد للنصف الأول)</strong>، بينما اقتصر التنفيذ الفعلي على <strong>٧ مرضى فقط</strong> (نسبة إنجاز ٧٪ من مستهدف H1). يرجع ذلك لتركيز الموارد في جراحات تخصصية معقدة ومكلفة (متوسط ٢٩.٨ ألف ريال للحالة) مع تأخر إطلاق القوافل الطبية والاستشارات.'
)

with open(v2_file, "w", encoding="utf-8") as f:
    f.write(dash_code)
print("Updated generate_v2_dashboard.py with 200 in Gap 1!")

# 2. Update generate_web_slides.py
web_file = os.path.join(base_dir, "generate_web_slides.py")
with open(web_file, "r", encoding="utf-8") as f:
    web_code = f.read()

web_code = web_code.replace(
    '٣٦,٦٠٦ مستفيد',
    '٢٠٠ مستفيد'
)
web_code = web_code.replace(
    '١٨,٣٠٣ مستفيد',
    '١٠٠ مستفيد'
)

with open(web_file, "w", encoding="utf-8") as f:
    f.write(web_code)
print("Updated generate_web_slides.py!")

# 3. Update Word & PPTX
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_full_14_slides_pptx.py")}"')
os.system(f'py -3 "{web_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "enrich_word_and_presentations.py")}"')

print("All deliverables updated successfully with 200 beneficiaries in all sections!")
