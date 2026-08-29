# -*- coding: utf-8 -*-
"""
Apply 1.5M SAR annual revenue target update across all deliverables:
- Update Strategic Plan Target from 6,846,000 SAR to 1,527,000 SAR (1.5M SAR)
- Update H1 target to 763,500 SAR
- Recalculate H1 revenue achievement rate to 76.25% (and 38.12% vs annual)
- Recalculate Financial Perspective to 63.01% (18.90 / 30)
- Recalculate Overall Weighted BSC Score to 41.73%
- Rebuild index.html, presentation.html, Word .docx, and PowerPoint .pptx
"""
import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")
v1_dir = os.path.join(base_dir, "التقرير_الجديد")

print("Applying 1.5M target update across all deliverables...")

# 1. Update generate_v2_dashboard.py
dash_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(dash_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

# Replace BSC Financial & Total scores in dashboard
dash_code = dash_code.replace(
    'المحور المالي والموازنة (٣٠٪)</div>\n                <div style="font-size:1.8rem; font-weight:900; color:var(--warning); margin-bottom:6px;">٣٢.٩٦٪</div>\n                <div style="font-size:0.85rem; color:var(--text-muted);">٩.٨٩ من ٣٠ نقطة',
    'المحور المالي والموازنة (٣٠٪)</div>\n                <div style="font-size:1.8rem; font-weight:900; color:var(--success); margin-bottom:6px;">٦٣.٠١٪</div>\n                <div style="font-size:0.85rem; color:var(--text-muted);">١٨.٩٠ من ٣٠ نقطة'
)
dash_code = dash_code.replace(
    'نسبة الإنجاز الاستراتيجي الإجمالية: <span style="color:var(--secondary-light); font-weight:900;">٣٢.٧٢٪</span>',
    'نسبة الإنجاز الاستراتيجي الإجمالية: <span style="color:var(--secondary-light); font-weight:900;">٤١.٧٣٪</span>'
)

# Replace 6,846,000 row with 1,527,000 in matrix table
dash_code = dash_code.replace(
    '<td><strong>الإيرادات المالية الكلية</strong></td>\n                        <td>إجمالي الدخل (ريال)</td>\n                        <td>٦,٨٤٦,٠٠٠</td>\n                        <td>٣,٤٢٣,٠٠٠</td>\n                        <td>٥٨٢,١٦٧.٥٢</td>\n                        <td><span class="tag-pill tag-danger">١٧.٠١٪</span></td>\n                        <td><span class="badge-pill bg-red">متأخر حرِج</span></td>\n                        <td>فجوة بين طموح الخطة والإيراد الفعلي (ص ١١)</td>',
    '<td><strong>الإيرادات المالية الكلية (المعدلة)</strong></td>\n                        <td>إجمالي الدخل (ريال)</td>\n                        <td>١,٥٢٧,٠٠٠</td>\n                        <td>٧٦٣,٥٠٠</td>\n                        <td>٥٨٢,١٦٧.٥٢</td>\n                        <td><span class="tag-pill tag-success">٧٦.٢٥٪</span></td>\n                        <td><span class="badge-pill bg-green">متقدم وجيد</span></td>\n                        <td>تحقيق ٧٦.٢٥٪ من مستهدف النصف الأول (٣٨.١٢٪ من السنوي)</td>'
)

with open(dash_file, "w", encoding="utf-8") as f:
    f.write(dash_code)

# 2. Update generate_web_slides.py
web_slides_file = os.path.join(base_dir, "generate_web_slides.py")
with open(web_slides_file, "r", encoding="utf-8") as f:
    web_code = f.read()

web_code = web_code.replace(
    '<div class="card-label">المحور المالي (٣٠٪)</div>\n                    <div class="card-val" style="color:var(--warning);">٣٢.٩٦٪</div>\n                    <div style="font-size:0.8rem; color:var(--text-muted);">٩.٨٩ من ٣٠',
    '<div class="card-label">المحور المالي (٣٠٪)</div>\n                    <div class="card-val" style="color:var(--success);">٦٣.٠١٪</div>\n                    <div style="font-size:0.8rem; color:var(--text-muted);">١٨.٩٠ من ٣٠'
)
web_code = web_code.replace(
    '٣٢.٧٢٪ <small style="font-size:1rem; font-weight:400; opacity:0.9;">(يحتاج إلى تحسين جذري وإعادة ضبط مسار)</small>',
    '٤١.٧٣٪ <small style="font-size:1rem; font-weight:400; opacity:0.9;">(تحسن ملحوظ بعد تعديل المستهدف المالي إلى ١.٥ مليون)</small>'
)
web_code = web_code.replace(
    '<td><strong>إجمالي الإيرادات الكلية</strong></td>\n                            <td>٦,٨٤٦,٠٠٠ ر.س</td>\n                            <td>٣,٤٢٣,٠٠٠ ر.س</td>\n                            <td>٥٨٢,١٦٧ ر.س</td>\n                            <td>١٧.٠١٪</td>\n                            <td><span class="badge-pill bg-red">متأخر حرِج</span></td>',
    '<td><strong>إجمالي الإيرادات (المعدلة)</strong></td>\n                            <td>١,٥٢٧,٠٠٠ ر.س</td>\n                            <td>٧٦٣,٥٠٠ ر.س</td>\n                            <td>٥٨٢,١٦٧ ر.س</td>\n                            <td>٧٦.٢٥٪</td>\n                            <td><span class="badge-pill bg-green">متقدم وجيد</span></td>'
)

with open(web_slides_file, "w", encoding="utf-8") as f:
    f.write(web_code)

# 3. Update generate_full_14_slides_pptx.py
pptx_gen_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_gen_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

pptx_code = pptx_code.replace(
    '("المحور المالي والموازنة (٣٠٪)", "٣٢.٩٦٪", "٩.٨٩ من ٣٠ نقطة\\nتحصيل ٥٨٢ ألف ر.س (+١٩٢٪ نمو سنوي)", C_WARNING, 3.8)',
    '("المحور المالي والموازنة (٣٠٪)", "٦٣.٠١٪", "١٨.٩٠ من ٣٠ نقطة\\nتحصيل ٥٨٢ ألف ر.س (٧٦.٢٥٪ من H1)", C_SUCCESS, 3.8)'
)
pptx_code = pptx_code.replace(
    'نسبة الإنجاز الاستراتيجي الإجمالية الموزونة: ٣٢.٧٢٪',
    'نسبة الإنجاز الاستراتيجي الإجمالية الموزونة: ٤١.٧٣٪'
)
pptx_code = pptx_code.replace(
    '("إجمالي الإيرادات الكلية للجمعية", "٦,٨٤٦,٠٠٠ ر.س", "٣,٤٢٣,٠٠٠ ر.س", "٥٨٢,١٦٧.٥٢ ر.س", "١٧.٠١٪", "متأخر حرِج")',
    '("إجمالي الإيرادات الكلية (المعدلة)", "١,٥٢٧,٠٠٠ ر.س", "٧٦٣,٥٠٠ ر.س", "٥٨٢,١٦٧.٥٢ ر.س", "٧٦.٢٥٪", "متقدم وجيد")'
)

with open(pptx_gen_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)

# 4. Update Word builder script
word_gen_file = os.path.join(base_dir, "build_v2_deliverables.py")
with open(word_gen_file, "r", encoding="utf-8") as f:
    word_code = f.read()

word_code = word_code.replace(
    "('٢. المحور المالي والموازنة التشغيلية', '٣٠٪', '٣٢.٩٦٪', '٩.٨٩ من ٣٠')",
    "('٢. المحور المالي والموازنة التشغيلية', '٣٠٪', '٦٣.٠١٪', '١٨.٩٠ من ٣٠')"
)
word_code = word_code.replace(
    "('الإجمالي العام الموزون للأداء الاستراتيجي (H1 2026)', '١٠٠٪', '٣٢.٧٢٪', '٣٢.٧٢ من ١٠٠ (يحتاج تحسين)')",
    "('الإجمالي العام الموزون للأداء الاستراتيجي (H1 2026)', '١٠٠٪', '٤١.٧٣٪', '٤١.٧٣ من ١٠٠ (بعد تعديل المستهدف المالي)')"
)
word_code = word_code.replace(
    "('١', 'الإيرادات الكلية للجمعية', 'إجمالي الدخل (ريال)', '٦,٨٤٦,٠٠٠', '٣,٤٢٣,٠٠٠', '٥٨٢,١٦٧.٥٢', '١٧.٠١٪', 'متأخر حرِج')",
    "('١', 'الإيرادات الكلية (المعدلة)', 'إجمالي الدخل (ريال)', '١,٥٢٧,٠٠٠', '٧٦٣,٥٠٠', '٥٨٢,١٦٧.٥٢', '٧٦.٢٥٪', 'متقدم وجيد')"
)

with open(word_gen_file, "w", encoding="utf-8") as f:
    f.write(word_code)

print("Running all generators to re-compile deliverables with 1.5M target...")
os.system(f'py -3 "{dash_file}"')
os.system(f'py -3 "{web_slides_file}"')
os.system(f'py -3 "{pptx_gen_file}"')
os.system(f'py -3 "{word_gen_file}"')

print("All deliverables updated successfully with 1.5M financial target!")
