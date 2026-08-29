# -*- coding: utf-8 -*-
"""
Fix Operating & General Expenses Table (Page 16 of official report verbatim):
- 2025 Total: 103,529 SAR (was mistakenly shown as 63,536 in one summary row)
- 2026 Total: 254,274 SAR
- Net Change: +150,745 SAR (+146%)
- Include all 16 items and official notes exactly as in Page 16 of report.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

new_op_table_tbody = """                <tbody>
                    <tr><td>١</td><td><strong>الرواتب</strong></td><td>١٤٤,٤٠٥</td><td>٤٥,٢٦٤</td><td style="color:var(--danger); font-weight:700;">+٩٩,١٤١</td><td><span class="tag-pill tag-danger">+٢١٩٪</span></td><td>٥٦.٨٪</td><td>عدد (٣) موظفين ٢٠٢٦م - عدد (١) موظف ٢٠٢٥م</td></tr>
                    <tr><td>٢</td><td><strong>أجور متعاونين</strong></td><td>١٣,٠٠٠</td><td>٩,٠٦٠</td><td style="color:var(--danger); font-weight:700;">+٣,٩٤٠</td><td><span class="tag-pill tag-danger">+٤٣٪</span></td><td>٥.١٪</td><td>عدد (١) موظف متعاون مكلف (محاسب) ٢٠٢٦م - منصة أطوع ٢٠٢٥م</td></tr>
                    <tr><td>٣</td><td><strong>التأمينات الاجتماعية</strong></td><td>١٤,٧٦٨</td><td>٩,٩٨٠</td><td style="color:var(--danger); font-weight:700;">+٤,٧٨٨</td><td><span class="tag-pill tag-danger">+٤٨٪</span></td><td>٥.٨٪</td><td>اشتراكات الموظفين السعوديين بنظام التأمينات الاجتماعية</td></tr>
                    <tr><td>٤</td><td><strong>الهاتف</strong></td><td>١,٣١٦</td><td>١,٣٤٢</td><td style="color:var(--success); font-weight:700;">-٢٦</td><td><span class="tag-pill tag-success">-٢٪</span></td><td>٠.٥٪</td><td>خطوط الاتصال والإنترنت والأرشفة</td></tr>
                    <tr><td>٥</td><td><strong>الكهرباء</strong></td><td>٣,٨٦٧</td><td>٠</td><td style="color:var(--danger); font-weight:700;">+٣,٨٦٧</td><td><span class="tag-pill tag-danger">—</span></td><td>١.٥٪</td><td>فواتير الكهرباء وتشغيل المقر الجديد</td></tr>
                    <tr><td>٦</td><td><strong>الإيجار</strong></td><td>٦٣,٣٣٣</td><td>٣٥,٠٠٠</td><td style="color:var(--danger); font-weight:700;">+٢٨,٣٣٣</td><td><span class="tag-pill tag-danger">+٨١٪</span></td><td>٢٤.٩٪</td><td>متضمن نصف إيجار المقر القديم + شهر إضافي (وفر المقر الجديد ٢٥ ألف/سنة)</td></tr>
                    <tr><td>٧</td><td><strong>مكتب المحاسب القانوني - رائد الأحمدي</strong></td><td>٤,٦٠٠</td><td>٠</td><td style="color:var(--danger); font-weight:700;">+٤,٦٠٠</td><td><span class="tag-pill tag-danger">—</span></td><td>١.٨٪</td><td>الباب الثاني - الموازنة (مراجعة وتدقيق القوائم المالية ٢٠٢٥م)</td></tr>
                    <tr><td>٨</td><td><strong>رسوم مصرفية</strong></td><td>٣٨٠</td><td>٠</td><td style="color:var(--danger); font-weight:700;">+٣٨٠</td><td><span class="tag-pill tag-danger">—</span></td><td>٠.١٥٪</td><td>رسوم وعمولات الحوالات والخدمات البنكية</td></tr>
                    <tr><td>٩</td><td><strong>طباعة</strong></td><td>٥٠٨</td><td>٠</td><td style="color:var(--danger); font-weight:700;">+٥٠٨</td><td><span class="tag-pill tag-danger">—</span></td><td>٠.٢٪</td><td>طباعة النماذج والمستندات الرسمية</td></tr>
                    <tr><td>١٠</td><td><strong>أدوات مكتبية</strong></td><td>١٥٢</td><td>٣٦٧</td><td style="color:var(--success); font-weight:700;">-٢١٥</td><td><span class="tag-pill tag-success">-٥٩٪</span></td><td>٠.٠٦٪</td><td>قرطاسية ومستلزمات استهلاكية</td></tr>
                    <tr><td>١١</td><td><strong>أحبار</strong></td><td>١٨٠</td><td>٠</td><td style="color:var(--danger); font-weight:700;">+١٨٠</td><td><span class="tag-pill tag-danger">—</span></td><td>٠.٠٧٪</td><td>أحبار طابعة الليزر الملونة</td></tr>
                    <tr><td>١٢</td><td><strong>نظافة ومنظفات</strong></td><td>٩٠٠</td><td>٥٣١</td><td style="color:var(--danger); font-weight:700;">+٣٦٩</td><td><span class="tag-pill tag-danger">+٦٩٪</span></td><td>٠.٣٥٪</td><td>مستلزمات نظافة المقر المكتبي</td></tr>
                    <tr><td>١٣</td><td><strong>ضيافة</strong></td><td>٣٧٥</td><td>٥٩٢</td><td style="color:var(--success); font-weight:700;">-٢١٧</td><td><span class="tag-pill tag-success">-٣٧٪</span></td><td>٠.١٥٪</td><td>استقبال الزوار والمانحين واللجان</td></tr>
                    <tr><td>١٤</td><td><strong>تصميم وتطوير الموقع الإلكتروني</strong></td><td>٣,٠٠٠</td><td>٠</td><td style="color:var(--danger); font-weight:700;">+٣,٠٠٠</td><td><span class="tag-pill tag-danger">—</span></td><td>١.٢٪</td><td>المشاريع المساندة (الحملة الإعلامية ٣٠,٠٠٠ ريال لم يتم الصرف منها)</td></tr>
                    <tr><td>١٥</td><td><strong>أجور نقل وتركيب أصول الجمعية للمقر الجديد</strong></td><td>٢,٤٣٠</td><td>٠</td><td style="color:var(--danger); font-weight:700;">+٢,٤٣٠</td><td><span class="tag-pill tag-danger">—</span></td><td>١.٠٪</td><td>الباب الخامس - الموازنة (التطوير المالي والإداري ٤١,٠٠٠ ريال لم يتم الصرف منها)</td></tr>
                    <tr><td>١٦</td><td><strong>صيانة متنوعة</strong></td><td>١,٠٦٠</td><td>١,٣٩٣</td><td style="color:var(--success); font-weight:700;">-٣٣٣</td><td><span class="tag-pill tag-success">-٢٤٪</span></td><td>٠.٤٪</td><td>صيانة دورية وتجهيز المرافق</td></tr>
                    <tr class="total-row" style="background:#FFF9F0;">
                        <td colspan="2"><strong>إجمالي المصروفات العمومية والإدارية (التشغيلية)</strong></td>
                        <td><strong>٢٥٤,٢٧٤</strong></td>
                        <td><strong>١٠٣,٥٢٩</strong></td>
                        <td><strong>+١٥٠,٧٤٥</strong></td>
                        <td><strong>+١٤٦٪</strong></td>
                        <td><strong>١٠٠٪</strong></td>
                        <td><strong>المطابقة الرسمية لصفحة ١٦ بتقرير الجمعية لعام ٢٠٢٦م</strong></td>
                    </tr>
                </tbody>"""

# Replace in generate_v2_dashboard.py
start_op = dash_code.find('<th>الوزن النسبي %</th>\n                        <th>البيان والتوجيه الإداري</th>\n                    </tr>\n                </thead>\n                <tbody>')
end_op = dash_code.find('</table>\n        </div>\n    </section>\n\n    <!-- Section 5: Clinical Impact')

if start_op != -1 and end_op != -1:
    header_end = start_op + len('<th>الوزن النسبي %</th>\n                        <th>البيان والتوجيه الإداري</th>\n                    </tr>\n                </thead>\n')
    dash_code = dash_code[:header_end] + new_op_table_tbody + '\n            ' + dash_code[end_op:]
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Updated Operating Expenses Table in generate_v2_dashboard.py!")
else:
    # Alternative replace
    old_total_str = '<td>٢٥٤,٢٧٤</td>\n                        <td>٦٣,٥٣٦</td>'
    new_total_str = '<td>٢٥٤,٢٧٤</td>\n                        <td>١٠٣,٥٢٩</td>'
    if old_total_str in dash_code:
        dash_code = dash_code.replace(old_total_str, new_total_str)
        with open(v2_file, "w", encoding="utf-8") as f:
            f.write(dash_code)
        print("Replaced total row in generate_v2_dashboard.py!")

# 2. Update PowerPoint Slide 7
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

pptx_code = pptx_code.replace("٦٣,٥٣٦ ريال", "١٠٣,٥٢٩ ريال")
pptx_code = pptx_code.replace("63,536", "103,529")

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated PowerPoint generate_full_14_slides_pptx.py!")

# 3. Update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    word_code = f.read()

word_code = word_code.replace("٦٣,٥٣٦", "١٠٣,٥٢٩")
word_code = word_code.replace("63,536", "103,529")

with open(word_file, "w", encoding="utf-8") as f:
    f.write(word_code)
print("Updated Word generator enrich_word_and_presentations.py!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables successfully recompiled with exact 103,529 SAR total for H1 2025 operating expenses!")
