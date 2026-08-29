# -*- coding: utf-8 -*-
"""
Add Full Official Comparative Financial Table (from Pages 10 & 11 of official report):
Title: "مقارنة النصف الأول للعام المالي من (30/06/2025م) إلى (30/06/2026م)"
Columns:
1. البند المالي
2. النصف الأول 2026م (30/06/2026م)
3. النصف الأول 2025م (30/06/2025م)
4. التغير بالقيمة (ريال)
5. نسبة التغير %
6. الملاحظات الفنية والبيان المالي المعتمد

Includes:
- إيرادات الزكاة (70k vs 80k)
- إيرادات العلاج المقيد (75k vs 25k)
- إيرادات المتجر الإلكتروني (10,469 vs 124)
- إيرادات منصة تبرع (1,203 vs 13,786)
- التبرعات والدعم العام (407,495 vs 62,564)
- اشتراكات العضوية (18k vs 18k)
- إجمالي الدخل (582,167 vs 199,474 | +192%)
- المساعدات العلاجية للمرضى (208,605 vs 20,000 | +943%)
- الأصول والتجهيزات الثابتة (15,620 vs 34,776 | -55%)
- الأرصدة النقدية المصرفية (1,001,754 vs 849,421 مرحلة | +18%)
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

comparative_table_html = """        <!-- Official Comparative Table (Pages 10 & 11 of Report) -->
        <div class="table-card" style="margin-top:35px; border-top:4px solid var(--primary);">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.35rem;"><i class="fas fa-scale-balanced" style="color:var(--secondary); margin-left:8px;"></i> جدول مقارنة النصف الأول للعام المالي من (30/06/2025م) إلى (30/06/2026م)</h3>
                    <p style="font-size:0.92rem; color:var(--text-muted);">المطابقة الرسمية المعتمدة بتقرير الجمعية (صفحة ١٠ و ١١) للأداء المالي والمساعدات والأصول والأرصدة</p>
                </div>
                <span class="tag-pill tag-success" style="font-size:1rem; padding:6px 16px;">مقارنة معتمدة (H1 2026 vs H1 2025)</span>
            </div>

            <table class="custom-table">
                <thead>
                    <tr>
                        <th>البند المالي والتشغيلي</th>
                        <th>النصف الأول ٢٠٢٦م</th>
                        <th>النصف الأول ٢٠٢٥م</th>
                        <th>التغير بالقيمة (ريال)</th>
                        <th>نسبة التغير ٪</th>
                        <th>الملاحظات الفنية والبيان المعتمد بالتقرير</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background:#FAF8F5;"><td colspan="6"><strong>أولاً: بنود الدخل والإيرادات (صفحة ١٠ بالتقرير)</strong></td></tr>
                    <tr>
                        <td><strong>أموال الزكاة</strong></td>
                        <td>٧٠,٠٠٠</td>
                        <td>٨٠,٠٠٠</td>
                        <td style="color:var(--danger); font-weight:700;">-١٠,٠٠٠</td>
                        <td><span class="tag-pill tag-danger">-١٣٪</span></td>
                        <td>مصروفة بالكامل لمصارف المرضى المحتاجين</td>
                    </tr>
                    <tr>
                        <td><strong>العلاج (مساعدات مقيدة)</strong></td>
                        <td>٧٥,٠٠٠</td>
                        <td>٢٥,٠٠٠</td>
                        <td style="color:var(--success); font-weight:700;">+٥٠,٠٠٠</td>
                        <td><span class="tag-pill tag-success">+٢٠٠٪</span></td>
                        <td>تضاعف الدعم المخصص للعمليات الجراحية المباشرة</td>
                    </tr>
                    <tr>
                        <td><strong>المتجر الإلكتروني</strong></td>
                        <td>١٠,٤٦٩</td>
                        <td>١٢٤</td>
                        <td style="color:var(--success); font-weight:700;">+١٠,٣٤٥</td>
                        <td><span class="tag-pill tag-success">+٨,٣٤٣٪</span></td>
                        <td>تفعيل حلول الدفع الرقمي والتسويق الإلكتروني</td>
                    </tr>
                    <tr>
                        <td><strong>منصة تبرع</strong></td>
                        <td>١,٢٠٣</td>
                        <td>١٣,٧٨٦</td>
                        <td style="color:var(--warning); font-weight:700;">-١٢,٥٨٣</td>
                        <td><span class="tag-pill tag-warning">-٩١٪</span></td>
                        <td>متوقفة - تم استبدالها وضمها لمنصة إحسان الوطنية</td>
                    </tr>
                    <tr>
                        <td><strong>تبرعات ودعم عام</strong></td>
                        <td>٤٠٧,٤٩٥</td>
                        <td>٦٢,٥٦٤</td>
                        <td style="color:var(--success); font-weight:700;">+٣٤٤,٩٣١</td>
                        <td><span class="tag-pill tag-success">+٥٥١٪</span></td>
                        <td>دعم استثنائي من كبار المانحين والأوقاف الاستراتيجية</td>
                    </tr>
                    <tr>
                        <td><strong>اشتراكات العضوية</strong></td>
                        <td>١٨,٠٠٠</td>
                        <td>١٨,٠٠٠</td>
                        <td>٠</td>
                        <td><span class="tag-pill tag-info">٠٪</span></td>
                        <td>استقرار تحصيل اشتراكات أعضاء الجمعية العمومية</td>
                    </tr>
                    <tr class="total-row" style="background:#FFF9F0;">
                        <td><strong>إجمالي الدخل والإيرادات</strong></td>
                        <td><strong>٥٨٢,١٦٧</strong></td>
                        <td><strong>١٩٩,٤٧٤</strong></td>
                        <td><strong>+٣٨٢,٦٩٣</strong></td>
                        <td><strong>+١٩٢٪</strong></td>
                        <td><strong>نمو مالي قياسي يعكس ثقة المانحين بالجمعية</strong></td>
                    </tr>

                    <tr style="background:#FAF8F5;"><td colspan="6"><strong>ثانياً: المساعدات العلاجية والأصول والأرصدة (صفحة ١١ بالتقرير)</strong></td></tr>
                    <tr>
                        <td><strong>المساعدات العلاجية (مرفق)</strong></td>
                        <td>٢٠٨,٦٠٥</td>
                        <td>٢٠,٠٠٠</td>
                        <td style="color:var(--success); font-weight:700;">+١٨٨,٦٠٥</td>
                        <td><span class="tag-pill tag-success">+٩٤٣٪</span></td>
                        <td>إحالة ٤ حالات للمستشفيات (٢٢,٢٧٥ ر.س) + ٣ حالات بالألماني (١٨٦,٣٣٠ ر.س)</td>
                    </tr>
                    <tr>
                        <td><strong>الأصول الثابتة والتجهيزات (مرفق)</strong></td>
                        <td>١٥,٦٢٠</td>
                        <td>٣٤,٧٧٦</td>
                        <td style="color:var(--info); font-weight:700;">-١٩,١٥٦</td>
                        <td><span class="tag-pill tag-info">-٥٥٪</span></td>
                        <td>موازنة تقديرية ١٩,٤٥٠ ر.س (متبقي صرف ٣,٨٣٠ ر.س لتأثيث المقر)</td>
                    </tr>
                    <tr>
                        <td><strong>إجمالي الأرصدة المصرفية بالبنوك</strong></td>
                        <td>١,٠٠١,٧٥٤</td>
                        <td>٨٤٩,٤٢١</td>
                        <td style="color:var(--success); font-weight:700;">+١٥٢,٣٣٣</td>
                        <td><span class="tag-pill tag-success">+١٨٪</span></td>
                        <td>الأهلي: ٩٣٠,٧٠٢ ر.س | الراجحي: ٧١,٠٥٢ ر.س (مقارنة بأرصدة افتتاحية ٢٠٢٥)</td>
                    </tr>
                    <tr>
                        <td><strong>صافي الأصول بالمركز المالي</strong></td>
                        <td>٩٧٢,٧١٣</td>
                        <td>٨٦٤,٠٤٥</td>
                        <td style="color:var(--success); font-weight:700;">+١٠٨,٦٦٨</td>
                        <td><span class="tag-pill tag-success">+١٣٪</span></td>
                        <td>تعزيز الملاءة والاحتياطيات المالية للجمعية</td>
                    </tr>
                </tbody>
            </table>
        </div>"""

# Insert this table right after the Revenue Table in Section 4
marker = '<!-- Budget & Liquidity Split -->'
if marker in dash_code:
    dash_code = dash_code.replace(marker, comparative_table_html + "\n\n        " + marker)
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added Full Comparative Table to generate_v2_dashboard.py!")

# 2. Update PowerPoint Presentation (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

# Update Slide 5 title and content to make 2025 vs 2026 comparison explicit
pptx_code = pptx_code.replace(
    'add_slide_header(s5, "الأداء المالي ومصادر الدخل لنصف عام ٢٠٢٦م", "تحليل تفصيلي لمصادر الإيرادات والمقارنة بالنصف الأول لعام ٢٠٢٥م")',
    'add_slide_header(s5, "مقارنة النصف الأول للعام المالي (30/06/2026م مقابل 30/06/2025م)", "المقارنة الرسمية المعتمدة بتقرير الجمعية (ص ١٠-١١) للدخل والمساعدات والأصول")'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated generate_full_14_slides_pptx.py Slide 5 header!")

# 3. Update Word Document Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    word_code = f.read()

# Check if comparative table is in Word
word_comp_table = """    add_rtl_heading(doc, "مقارنة النصف الأول للعام المالي من (30/06/2025م) إلى (30/06/2026م) - صفحة ١٠ و ١١", level=2)
    comp_headers = ["البند المالي", "H1 2026 (ريال)", "H1 2025 (ريال)", "التغير (ريال)", "نسبة النمو", "البيان والدلالة المعتمدة"]
    t_comp = doc.add_table(rows=11, cols=6)
    t_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(comp_headers):
        t_comp.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_comp.rows[0].cells[j], "6B1D3A")
        t_comp.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_comp.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_comp.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_comp.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9)
    
    comp_rows = [
        ("أموال الزكاة", "٧٠,٠٠٠", "٨٠,٠٠٠", "-١٠,٠٠٠", "-١٣٪", "مصروفة لمصارف المرضى المحتاجين"),
        ("العلاج (مساعدات مقيدة)", "٧٥,٠٠٠", "٢٥,٠٠٠", "+٥٠,٠٠٠", "+٢٠٠٪", "تضاعف الدعم المخصص للعمليات"),
        ("المتجر الإلكتروني", "١٠,٤٦٩", "١٢٤", "+١٠,٣٤٥", "+٨,٣٤٣٪", "تفعيل الدفع الرقمي والتسويق"),
        ("منصة تبرع", "١,٢٠٣", "١٣,٧٨٦", "-١٢,٥٨٣", "-٩١٪", "استُبدلت بمنصة إحسان الوطنية"),
        ("تبرعات ودعم عام", "٤٠٧,٤٩٥", "٦٢,٥٦٤", "+٣٤٤,٩٣١", "+٥٥١٪", "دعم استثنائي من كبار المانحين والأوقاف"),
        ("اشتراكات العضوية", "١٨,٠٠٠", "١٨,٠٠٠", "٠", "٠٪", "استقرار تحصيل اشتراكات الأعضاء"),
        ("إجمالي الدخل والإيرادات", "٥٨٢,١٦٧", "١٩٩,٤٧٤", "+٣٨٢,٦٩٣", "+١٩٢٪", "نمو مالي استثنائي بنسبة ١٩٢٪"),
        ("المساعدات العلاجية (مرفق)", "٢٠٨,٦٠٥", "٢٠,٠٠٠", "+١٨٨,٦٠٥", "+٩٤٣٪", "إحالة ٤ حالات + ٣ حالات بالألماني"),
        ("الأصول الثابتة (مرفق)", "١٥,٦٢٠", "٣٤,٧٧٦", "-١٩,١٥٦", "-٥٥٪", "تجهيزات ومكاتب المقر الجديد"),
        ("الأرصدة المصرفية بالبنوك", "١,٠٠١,٧٥٤", "٨٤٩,٤٢١", "+١٥٢,٣٣٣", "+١٨٪", "الأهلي: ٩٣٠ ألف | الراجحي: ٧١ ألف")
    ]
    for i, row in enumerate(comp_rows):
        r = t_comp.rows[i+1]
        for j, val in enumerate(row):
            r.cells[j].paragraphs[0].text = val
            r.cells[j].paragraphs[0].paragraph_format.bidi = True
            r.cells[j].paragraphs[0].runs[0].font.size = DPt(8.5)
            if i == 6 or i == 7:
                r.cells[j].paragraphs[0].runs[0].font.bold = True
            if i % 2 == 1:
                set_cell_background(r.cells[j], "F8F6F0")
    doc.add_page_break()"""

start_w_fin = word_code.find('add_rtl_heading(doc, "أولاً: الأداء المالي والموازنة التشغيلية (H1 2026)", level=1)')
if start_w_fin != -1:
    h_w_fin = 'add_rtl_heading(doc, "أولاً: الأداء المالي والموازنة التشغيلية (H1 2026)", level=1)\n'
    word_code = word_code[:start_w_fin] + h_w_fin + word_comp_table + "\n    " + word_code[start_w_fin + len(h_w_fin):]
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(word_code)
    print("Added Full Comparative Table to Word document!")

# Re-run all generators
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated with the full comparative 2025 vs 2026 table!")
