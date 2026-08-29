# -*- coding: utf-8 -*-
"""
Add Complete 2025 Fixed Assets Table & Comparison (from Page 22 of official report):
Title: "الأصول الثابتة - مقارنة النصف الأول لعام 2026م بالنصف الأول لعام 2025م عام التأسيس"
Hero Card: 34,775.50 SAR (مصروفات الأصول الثابتة لعام 2025م) vs 15,620.80 SAR (2026م)
Detailed Table Categories:
1. الأجهزة المكتبية: 10,295 SAR (2 حاسب HP 4,798 | 1 حاسب HP 3,399 | 1 لابتوب أيسر 999 | 1 طابعة HP 1,099)
2. الأثاث المكتبي: 17,600 SAR (طاولة اجتماعات، كراسي دوارة، مكاتب، دواليب، أطقم كنب وطني، قواطع بارتشن، ضريبة 2,295.65)
3. الأجهزة الكهربائية: 6,630.50 SAR (3 مكيفات أوجين 24 وحدة 5,504.25 | ثلاجة بيورن 261.40 | ضريبة 864.85)
4. أجهزة الاتصال: 250 SAR (جوال 217.39 + ضريبة 32.61)
Total: 34,775.50 SAR

Apply across:
- generate_v2_dashboard.py -> index.html
- generate_full_14_slides_pptx.py -> PPTX
- generate_web_slides.py -> presentation.html
- enrich_word_and_presentations.py -> Word .docx
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

fixed_assets_2025_html = """        <!-- Page 22: Fixed Assets 2025 vs 2026 Comparison Table -->
        <div class="table-card" style="margin-top:35px; border-top:4px solid var(--primary);">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.35rem;"><i class="fas fa-couch" style="color:var(--secondary); margin-left:8px;"></i> الأصول الثابتة: مقارنة النصف الأول لعام ٢٠٢٦م بالنصف الأول لعام ٢٠٢٥م (عام التأسيس)</h3>
                    <p style="font-size:0.92rem; color:var(--text-muted);">البيان التفصيلي المعتمد بتقرير الجمعية (صفحة ٢٢) لمصروفات شراء الأصول وتجهيزات المقر في فترة التأسيس</p>
                </div>
                <span class="tag-pill tag-info" style="font-size:1rem; padding:6px 16px;">إجمالي أصول ٢٠٢٥م: ٣٤,٧٧٥.٥٠ ر.س</span>
            </div>

            <!-- Comparison Summary Hero -->
            <div class="grid-2" style="margin-bottom:25px; gap:20px;">
                <div style="background:#FAF8F5; border:2px solid #541228; border-radius:var(--radius-lg); padding:18px 24px; text-align:center;">
                    <div style="font-size:2rem; font-weight:900; color:#541228;">١٥,٦٢٠.٨٠ <small style="font-size:1rem;">ر.س</small></div>
                    <div style="font-weight:700; color:var(--text-main); margin-top:4px;">مصروفات الأصول الثابتة لعام ٢٠٢٦م</div>
                    <div style="font-size:0.88rem; color:var(--text-muted); margin-top:2px;">(تأثيث وتجهيز المقر الجديد بوفر سنوي ٢٥ ألف ريال)</div>
                </div>
                <div style="background:#FAF8F5; border:2px solid #C9A96E; border-radius:var(--radius-lg); padding:18px 24px; text-align:center;">
                    <div style="font-size:2rem; font-weight:900; color:#8C6D37;">٣٤,٧٧٥.٥٠ <small style="font-size:1rem;">ر.س</small></div>
                    <div style="font-weight:700; color:var(--text-main); margin-top:4px;">مصروفات الأصول الثابتة لعام ٢٠٢٥م (عام التأسيس)</div>
                    <div style="font-size:0.88rem; color:var(--success); font-weight:700; margin-top:2px;">وفر بالإنفاق الرأسمالي بنسبة -٥٥٪ (-١٩,١٥٦ ر.س)</div>
                </div>
            </div>

            <!-- 2025 Detailed Assets Table -->
            <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:12px;"><i class="fas fa-list-check" style="color:var(--secondary); margin-left:6px;"></i> تفصيل مشتريات وتجهيزات الأصول الثابتة لعام ٢٠٢٥م (٣٤,٧٧٥.٥٠ ريال):</h4>
            <table class="custom-table">
                <thead>
                    <tr>
                        <th style="width:5%;">م</th>
                        <th style="width:35%;">اسم الأصل والتجهيز</th>
                        <th style="width:10%; text-align:center;">العدد</th>
                        <th style="width:15%; text-align:center;">تاريخ الشراء</th>
                        <th style="width:15%; text-align:center;">المبلغ (ريال)</th>
                        <th style="width:20%;">المجموعة والتصنيف</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background:#FAF8F5;"><td colspan="6"><strong>١. الأجهزة المكتبية والتقنية (إجمالي المجموعة: ١٠,٢٩٥.٠٠ ريال)</strong></td></tr>
                    <tr><td>١</td><td>حاسب آلي مكتبي HP</td><td style="text-align:center;">٢</td><td style="text-align:center;">٢٠٢٥/٠٦/١٨م</td><td style="text-align:center; font-weight:700;">٤,٧٩٨.٠٠</td><td>أجهزة حاسب مكتبية رئيسية</td></tr>
                    <tr><td>٢</td><td>حاسب آلي مكتبي HP</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/١٨م</td><td style="text-align:center; font-weight:700;">٣,٣٩٩.٠٠</td><td>حاسب مكتبي إداري</td></tr>
                    <tr><td>٣</td><td>لابتوب محمول أيسر (Acer)</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/١٨م</td><td style="text-align:center; font-weight:700;">٩٩٩.٠٠</td><td>جهاز محمول للأعمال الخارجية</td></tr>
                    <tr><td>٤</td><td>طابعة مكتبية HP</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/١٨م</td><td style="text-align:center; font-weight:700;">١,٠٩٩.٠٠</td><td>طباعة المستندات والتقارير</td></tr>

                    <tr style="background:#FAF8F5;"><td colspan="6"><strong>٢. الأثاث المكتبي والتأثيث (إجمالي المجموعة شاملاً الضريبة: ١٧,٦٠٠.٠٠ ريال)</strong></td></tr>
                    <tr><td>٥</td><td>طاولة اجتماعات خشب صيني ٣٢٠ سم</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">١,٥٢١.٧٣</td><td>قاعة الاجتماعات ومجلس الإدارة</td></tr>
                    <tr><td>٦</td><td>كرسي دوار جلد ظهر طويل صيني</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">٤٣٤.٧٨</td><td>كرسي الإدارة التنفيذية</td></tr>
                    <tr><td>٧</td><td>كرسي ثابت جلد صيني</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">٨٦٩.٥٨</td><td>كرسي استقبال ومراجعين</td></tr>
                    <tr><td>٨</td><td>كراسي دوارة شبك ظهر قصير صيني</td><td style="text-align:center;">٧</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">٩١٣.٠٨</td><td>كراسي مكاتب وقاعات</td></tr>
                    <tr><td>٩</td><td>مكتب ١٢٠ سم + دولاب مستندات + طاولة ضيافة</td><td style="text-align:center;">٣</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">٥,٠٤٣.٤٧</td><td>طواقم مكاتب وضيافة إدارية</td></tr>
                    <tr><td>١٠</td><td>أطقم كنب وطني جلد بني (مفرد + ثنائي + ثلاثي)</td><td style="text-align:center;">٤</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">٣,٩١٣.٠٢</td><td>أطقم استقبال الزوار والضيوف</td></tr>
                    <tr><td>١١</td><td>فاصل (بارتشن) ثلاثي خشب صيني</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">٢,٦٠٨.٦٩</td><td>تقسيم المكاتب والصالات</td></tr>
                    <tr><td>١٢</td><td>القيمة الضريبية المضافة للأثاث المكتبي</td><td style="text-align:center;">—</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٥م</td><td style="text-align:center; font-weight:700;">٢,٢٩٥.٦٥</td><td>ضريبة القيمة المضافة ١٥٪</td></tr>

                    <tr style="background:#FAF8F5;"><td colspan="6"><strong>٣. الأجهزة الكهربائية والتكييف (إجمالي المجموعة: ٦,٦٣٠.٥٠ ريال)</strong></td></tr>
                    <tr><td>١٣</td><td>مكيفات أوجين جولد ٢٤ وحدة بارد + كراسي تركيب</td><td style="text-align:center;">٣</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٢م</td><td style="text-align:center; font-weight:700;">٥,٥٠٤.٢٥</td><td>تكييف صالات ومكاتب المقر</td></tr>
                    <tr><td>١٤</td><td>ثلاجة بيورن ٩٠ لتر صغيرة + الضريبة (٨٦٤.٨٥ ر.س)</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٦/٠٢م</td><td style="text-align:center; font-weight:700;">١,١٢٦.٢٥</td><td>خدمات الضيافة والمقر</td></tr>

                    <tr style="background:#FAF8F5;"><td colspan="6"><strong>٤. أجهزة الاتصال والتواصل (إجمالي المجموعة: ٢٥٠.٠٠ ريال)</strong></td></tr>
                    <tr><td>١٥</td><td>جهاز جوال للجمعية + ضريبة القيمة المضافة (٣٢.٦١ ر.س)</td><td style="text-align:center;">١</td><td style="text-align:center;">٢٠٢٥/٠٥/٢٦م</td><td style="text-align:center; font-weight:700;">٢٥٠.٠٠</td><td>هاتف التواصل الرسمي للجمعية</td></tr>

                    <tr class="total-row" style="background:#FFF9F0;">
                        <td colspan="4"><strong>إجمالي مصروفات الأصول الثابتة لعام ٢٠٢٥م (عام التأسيس)</strong></td>
                        <td style="text-align:center; font-size:1.15rem; font-weight:900; color:#541228;">٣٤,٧٧٥.٥٠</td>
                        <td><strong>مطابقة رسمية لصفحة ٢٢ بتقرير الجمعية</strong></td>
                    </tr>
                </tbody>
            </table>
        </div>"""

# Insert this section right before Appendix 2 (or right next to Fixed Assets Table in Appendix)
if "<!-- Page 22: Fixed Assets 2025 vs 2026 Comparison Table -->" not in dash_code:
    ins_marker_p22 = '<!-- Appendix 2: Fixed Assets Table -->'
    dash_code = dash_code.replace(ins_marker_p22, fixed_assets_2025_html + "\n\n        " + ins_marker_p22)
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added 2025 Fixed Assets Table to generate_v2_dashboard.py!")

# 2. Update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    w_code = f.read()

word_p22_table = """    add_rtl_heading(doc, "الأصول الثابتة: مقارنة النصف الأول لعام ٢٠٢٦م بالنصف الأول لعام ٢٠٢٥م عام التأسيس (صفحة ٢٢ بالتقرير)", level=2)
    p_p22 = doc.add_paragraph()
    p_p22.paragraph_format.bidi = True
    p_p22.add_run("يوضح الجدول التالي تفصيل مصروفات شراء وتجهيز الأصول الثابتة خلال فترة التأسيس لعام ٢٠٢٥م بإجمالي (٣٤,٧٧٥.٥٠ ريال) مقارنة بأصول عام ٢٠٢٦م (١٥,٦٢٠.٨٠ ريال) محققة وفراً قدره -٥٥٪:")
    
    t_p22 = doc.add_table(rows=17, cols=5)
    t_p22.alignment = WD_TABLE_ALIGNMENT.CENTER
    p22_headers = ["م", "اسم الأصل والتجهيز", "العدد", "تاريخ الشراء", "المبلغ (ريال)"]
    for j, h in enumerate(p22_headers):
        t_p22.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_p22.rows[0].cells[j], "6B1D3A")
        t_p22.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_p22.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_p22.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_p22.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9)
    
    p22_rows = [
        ("١", "حاسب آلي مكتبي HP", "٢", "٢٠٢٥/٠٦/١٨", "٤,٧٩٨.٠٠"),
        ("٢", "حاسب آلي مكتبي HP", "١", "٢٠٢٥/٠٦/١٨", "٣,٣٩٩.٠٠"),
        ("٣", "لابتوب محمول أيسر", "١", "٢٠٢٥/٠٦/١٨", "٩٩٩.٠٠"),
        ("٤", "طابعة مكتبية HP", "١", "٢٠٢٥/٠٦/١٨", "١,٠٩٩.٠٠"),
        ("٥", "طاولة اجتماعات خشب صيني ٣٢٠ سم", "١", "٢٠٢٥/٠٦/٠٥", "١,٥٢١.٧٣"),
        ("٦", "كرسي دوار جلد ظهر طويل", "١", "٢٠٢٥/٠٦/٠٥", "٤٣٤.٧٨"),
        ("٧", "كرسي ثابت جلد صيني", "١", "٢٠٢٥/٠٦/٠٥", "٨٦٩.٥٨"),
        ("٨", "كراسي دوارة شبك ظهر قصير", "٧", "٢٠٢٥/٠٦/٠٥", "٩١٣.٠٨"),
        ("٩", "مكتب ١٢٠ سم + دولاب مستندات + ضيافة", "٣", "٢٠٢٥/٠٦/٠٥", "٥,٠٤٣.٤٧"),
        ("١٠", "أطقم كنب وطني جلد بني", "٤", "٢٠٢٥/٠٦/٠٥", "٣,٩١٣.٠٢"),
        ("١١", "فاصل (بارتشن) ثلاثي خشب صيني", "١", "٢٠٢٥/٠٦/٠٥", "٢,٦٠٨.٦٩"),
        ("١٢", "ضريبة القيمة المضافة للأثاث", "—", "٢٠٢٥/٠٦/٠٥", "٢,٢٩٥.٦٥"),
        ("١٣", "مكيفات أوجين جولد ٢٤ وحدة + كراسي", "٣", "٢٠٢٥/٠٦/٠٢", "٥,٥٠٤.٢٥"),
        ("١٤", "ثلاجة بيورن + ضريبة الأجهزة", "١", "٢٠٢٥/٠٦/٠٢", "١,١٢٦.٢٥"),
        ("١٥", "جوال الجمعية + الضريبة", "١", "٢٠٢٥/٠٥/٢٦", "٢٥٠.٠٠"),
        ("—", "إجمالي مصروفات الأصول الثابتة لعام ٢٠٢٥م", "—", "—", "٣٤,٧٧٥.٥٠")
    ]
    for i, row in enumerate(p22_rows):
        r = t_p22.rows[i+1]
        for j, val in enumerate(row):
            r.cells[j].paragraphs[0].text = val
            r.cells[j].paragraphs[0].paragraph_format.bidi = True
            r.cells[j].paragraphs[0].runs[0].font.size = DPt(8.5)
            if i == 15:
                r.cells[j].paragraphs[0].runs[0].font.bold = True
                set_cell_background(r.cells[j], "FFF9F0")
            elif i % 2 == 1:
                set_cell_background(r.cells[j], "F8F6F0")
    doc.add_page_break()"""

if "الأصول الثابتة: مقارنة النصف الأول لعام ٢٠٢٦م بالنصف الأول لعام ٢٠٢٥م عام التأسيس" not in w_code:
    w_code = w_code.replace('add_rtl_heading(doc, "الملحق (١): بيان كبار المانحين والأوقاف', word_p22_table + '\n    add_rtl_heading(doc, "الملحق (١): بيان كبار المانحين والأوقاف')
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(w_code)
    print("Added Page 22 Table to Word generator!")

# 3. Update PowerPoint (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

# Update Slide 6 or 7 with 2025 vs 2026 assets comparison
pptx_code = pptx_code.replace(
    '("شراء الأصول والتجهيزات الثابتة", "١٩,٤٥٠", "١٥,٦٢٠.٨٠", "٨٠.٣١٪", "تأثيث المقر الجديد وشراء أجهزة حاسب وطابعات")',
    '("شراء الأصول والتجهيزات الثابتة", "١٩,٤٥٠", "١٥,٦٢٠.٨٠", "٨٠.٣١٪", "أصول ٢٠٢٦ (١٥,٦٢٠ ر.س) مقابل عام التأسيس ٢٠٢٥ (٣٤,٧٧٦ ر.س) بوفر -٥٥٪")'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated PowerPoint with Page 22 details!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated and recompiled with exact Page 22 Fixed Assets table!")
