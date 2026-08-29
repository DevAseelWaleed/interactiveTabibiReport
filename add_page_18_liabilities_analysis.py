# -*- coding: utf-8 -*-
"""
Add Exact Page 18 Section: "بيان الالتزامات الدائنة إلى 30/06/2026م"
Features:
1. Movement of Liabilities Table:
   - Opening (01/01/2026): 18,211 SAR
   - Paid/Debit: 13,211 SAR (72.5% settled)
   - Credit: 0 SAR
   - Closing (30/06/2026): 5,000 SAR (مستحق مؤسسة مؤشرات النجاح الإدارية عن أعمال الحوكمة والتطوير المؤسسي)
2. Breakdown Table of Transferred 2025 Liabilities (18,211 SAR):
   - مستحق إيجار شهر للمقر السابق (ديسمبر 2025): 5,833 SAR
   - مستحق مؤسسة مؤشرات النجاح الإدارية (حوكمة): 5,000 SAR
   - مستحق مكتب المحاسب القانوني رائد الأحمدي (تدقيق 2025): 4,600 SAR
   - مستحق المحاسب المتعاون محمد الحسن (إقفال 2025): 2,000 SAR
   - مخصص مكافأة نهاية خدمة الموظف وائل هاشم: 778 SAR
   - Total: 18,211 SAR
3. Dedicated Chart for Settled vs Outstanding Liabilities (72.5% vs 27.5%).

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

page_18_html = """        <!-- Page 18: Payables & Transferred Liabilities (بيان الالتزامات الدائنة) -->
        <div class="table-card" style="margin-top:35px; border-top:4px solid var(--primary); background:#FFF; border-radius:var(--radius-xl); padding:30px; box-shadow:var(--shadow-md);">
            <div class="table-toolbar" style="margin-bottom:20px;">
                <div>
                    <h3 style="color:var(--primary); font-size:1.35rem;"><i class="fas fa-file-invoice-dollar" style="color:var(--secondary); margin-left:8px;"></i> بيان الالتزامات الدائنة وتحليل الالتزامات المرحلة وسدادها (صفحة ١٨ بالتقرير)</h3>
                    <p style="font-size:0.92rem; color:var(--text-muted);">حركة تسوية الالتزامات المالية المرحلة من عام ٢٠٢٥م وسداد ٧٢.٥٪ منها بنجاح خلال النصف الأول لعام ٢٠٢٦م</p>
                </div>
                <span class="tag-pill tag-success" style="font-size:1rem; padding:6px 16px;">تم سداد ١٣,٢١١ ر.س (٧٢.٥٪)</span>
            </div>

            <!-- Table 1: Movement of Liabilities -->
            <table class="custom-table" style="margin-bottom:25px;">
                <thead>
                    <tr>
                        <th style="width:25%;">البند</th>
                        <th style="width:15%; text-align:center;">الرصيد الافتتاحي (٠١/٠١/٢٠٢٦م)</th>
                        <th style="width:15%; text-align:center;">مدين (سداد)</th>
                        <th style="width:12%; text-align:center;">دائن</th>
                        <th style="width:15%; text-align:center;">الرصيد في (٣٠/٠٦/٢٠٢٦م)</th>
                        <th style="width:18%;">ملاحظات المعتمدة</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>حركة الالتزامات (الدائنة)</strong></td>
                        <td style="text-align:center; font-weight:700;">١٨,٢١١</td>
                        <td style="text-align:center; font-weight:700; color:var(--success);">١٣,٢١١</td>
                        <td style="text-align:center;">٠</td>
                        <td style="text-align:center; font-size:1.15rem; font-weight:900; color:var(--primary);">٥,٠٠٠</td>
                        <td>مستحق مؤسسة مؤشرات النجاح الإدارية عن أعمال الحوكمة والتطوير المؤسسي</td>
                    </tr>
                </tbody>
            </table>

            <!-- Table 2 & Chart Grid -->
            <div class="grid-2" style="align-items:start; gap:25px;">
                <!-- Right: Breakdown Table -->
                <div>
                    <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:12px;"><i class="fas fa-list-check" style="color:var(--secondary); margin-left:6px;"></i> تحليل الالتزامات الدائنة المرحلة من عام ٢٠٢٥م (١٨,٢١١ ريال):</h4>
                    <table class="custom-table" style="margin:0;">
                        <thead>
                            <tr>
                                <th style="width:70%;">البيان والتفصيل</th>
                                <th style="width:30%; text-align:center;">المبلغ (ريال)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>مستحق إيجار لشهر واحد المقر السابق للجمعية (ديسمبر ٢٠٢٥م)</td>
                                <td style="text-align:center; font-weight:700; color:var(--success);">٥,٨٣٣</td>
                            </tr>
                            <tr>
                                <td>مستحق مؤسسة مؤشرات النجاح الإدارية عن أعمال الحوكمة والتطوير المؤسسي</td>
                                <td style="text-align:center; font-weight:700; color:var(--primary);">٥,٠٠٠</td>
                            </tr>
                            <tr>
                                <td>مستحق مكتب المحاسب القانوني (رائد الأحمدي) - مراجعة وإعداد القوائم المالية ٢٠٢٥م</td>
                                <td style="text-align:center; font-weight:700; color:var(--success);">٤,٦٠٠</td>
                            </tr>
                            <tr>
                                <td>مستحق المحاسب المتعاون (محمد الحسن) - أعمال إقفال العام المالي ٢٠٢٥م</td>
                                <td style="text-align:center; font-weight:700; color:var(--success);">٢,٠٠٠</td>
                            </tr>
                            <tr>
                                <td>مخصص نهاية خدمة الموظف (وائل محمد ثلاب هاشم علي)</td>
                                <td style="text-align:center; font-weight:700; color:var(--success);">٧٧٨</td>
                            </tr>
                            <tr class="total-row" style="background:#FFF9F0;">
                                <td><strong>الإجمالي</strong></td>
                                <td style="text-align:center; font-size:1.15rem; font-weight:900; color:#541228;">١٨,٢١١</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Left: Chart -->
                <div style="background:var(--bg-subtle); padding:20px; border-radius:var(--radius-lg); border:1px solid rgba(0,0,0,0.05); text-align:center;">
                    <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:12px;"><i class="fas fa-chart-pie" style="color:var(--secondary); margin-left:6px;"></i> نسبة سداد الالتزامات المرحلة (٪)</h4>
                    <div style="height:250px; position:relative;">
                        <canvas id="page18LiabilitiesChart"></canvas>
                    </div>
                </div>
            </div>
        </div>"""

# Insert Page 18 right after Page 17
if "<!-- Page 18: Payables & Transferred Liabilities" not in dash_code:
    ins_marker_p18 = '<!-- Official Comparative Table (Pages 10 & 11 of Report) -->'
    dash_code = dash_code.replace(ins_marker_p18, page_18_html + "\n\n        " + ins_marker_p18)
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added Page 18 HTML to generate_v2_dashboard.py!")

# Add Chart initialization script for Page 18 in generate_v2_dashboard.py
p18_chart_js = """            // 14. Page 18 Liabilities Settlement Doughnut Chart
            const ctxP18 = document.getElementById('page18LiabilitiesChart');
            if (ctxP18) {
                new Chart(ctxP18, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['التزامات مسددة بنجاح (١٣,٢١١)', 'متبقي مستحق لحوكمة مؤشرات النجاح (٥,٠٠٠)'],
                        datasets: [{
                            data: [13211, 5000],
                            backgroundColor: ['#1B7A48', '#541228'],
                            borderWidth: 2,
                            borderColor: '#FFF'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 11 } } }
                        },
                        cutout: '55%'
                    }
                });
            }"""

if "page18LiabilitiesChart" not in dash_code:
    dash_code = dash_code.replace("// 13. Page 17 Financial Structure", p18_chart_js + "\n\n            // 13. Page 17 Financial Structure")
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added Page 18 Chart to JavaScript in generate_v2_dashboard.py!")

# 2. Update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    w_code = f.read()

word_p18_tables = """    add_rtl_heading(doc, "بيان الالتزامات الدائنة وتحليل الالتزامات المرحلة (صفحة ١٨ بالتقرير)", level=2)
    p_p18_1 = doc.add_paragraph()
    p_p18_1.paragraph_format.bidi = True
    p_p18_1.add_run("١. حركة الالتزامات الدائنة للنصف الأول لعام ٢٠٢٦م:")
    
    t_p18_1 = doc.add_table(rows=2, cols=5)
    t_p18_1.alignment = WD_TABLE_ALIGNMENT.CENTER
    p18_1_headers = ["البند", "الرصيد الافتتاحي (٠١/٠١)", "مدين (سداد)", "دائن", "الرصيد في (٣٠/٠٦)"]
    for j, h in enumerate(p18_1_headers):
        t_p18_1.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_p18_1.rows[0].cells[j], "6B1D3A")
        t_p18_1.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_p18_1.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_p18_1.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_p18_1.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9.5)
    
    p18_1_row = ["حركة الالتزامات (الدائنة)", "١٨,٢١١", "١٣,٢١١", "٠", "٥,٠٠٠"]
    for j, val in enumerate(p18_1_row):
        t_p18_1.rows[1].cells[j].paragraphs[0].text = val
        t_p18_1.rows[1].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_p18_1.rows[1].cells[j].paragraphs[0].runs[0].font.size = DPt(9)
        if j == 4:
            t_p18_1.rows[1].cells[j].paragraphs[0].runs[0].font.bold = True
            set_cell_background(t_p18_1.rows[1].cells[j], "FFF9F0")
    
    p_p18_2 = doc.add_paragraph()
    p_p18_2.paragraph_format.bidi = True
    p_p18_2.add_run("٢. بيان تحليل حركة الالتزامات الدائنة المرحلة من عام ٢٠٢٥م (إجمالي ١٨,٢١١ ريال):")
    
    t_p18_2 = doc.add_table(rows=7, cols=3)
    t_p18_2.alignment = WD_TABLE_ALIGNMENT.CENTER
    p18_2_headers = ["م", "البيان والتفصيل المعتمد", "المبلغ (ريال)"]
    for j, h in enumerate(p18_2_headers):
        t_p18_2.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_p18_2.rows[0].cells[j], "6B1D3A")
        t_p18_2.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_p18_2.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_p18_2.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_p18_2.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9.5)
    
    p18_2_rows = [
        ("١", "مستحق إيجار لشهر واحد المقر السابق للجمعية (ديسمبر ٢٠٢٥م)", "٥,٨٣٣"),
        ("٢", "مستحق مؤسسة مؤشرات النجاح الإدارية عن أعمال الحوكمة والتطوير المؤسسي", "٥,٠٠٠"),
        ("٣", "مستحق مكتب المحاسب القانوني (رائد الأحمدي) - مراجعة وإعداد القوائم المالية ٢٠٢٥م", "٤,٦٠٠"),
        ("٤", "مستحق المحاسب المتعاون (محمد الحسن) - عن أعمال إقفال العام المالي ٢٠٢٥م", "٢,٠٠٠"),
        ("٥", "مخصص نهاية خدمة الموظف (وائل محمد ثلاب هاشم علي)", "٧٧٨"),
        ("—", "إجمالي الالتزامات المرحلة من عام ٢٠٢٥م", "١٨,٢١١")
    ]
    for i, row in enumerate(p18_2_rows):
        r = t_p18_2.rows[i+1]
        for j, val in enumerate(row):
            r.cells[j].paragraphs[0].text = val
            r.cells[j].paragraphs[0].paragraph_format.bidi = True
            r.cells[j].paragraphs[0].runs[0].font.size = DPt(9)
            if i == 5:
                r.cells[j].paragraphs[0].runs[0].font.bold = True
                set_cell_background(r.cells[j], "FFF9F0")
            elif i % 2 == 1:
                set_cell_background(r.cells[j], "F8F6F0")
    doc.add_page_break()"""

if "بيان الالتزامات الدائنة وتحليل الالتزامات المرحلة (صفحة ١٨ بالتقرير)" not in w_code:
    w_code = w_code.replace('add_rtl_heading(doc, "ثانياً: المساعدات العلاجية', word_p18_tables + '\n    add_rtl_heading(doc, "ثانياً: المساعدات العلاجية')
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(w_code)
    print("Added Page 18 Tables to Word generator!")

# 3. Update PowerPoint (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

pptx_code = pptx_code.replace(
    '("الالتزامات الدائنة", "٥,٠٠٠", "٥,٠٠٠", "١٠٠٪", "مستحق حوكمة مؤشرات النجاح")',
    '("الالتزامات الدائنة المرحلة", "١٨,٢١١", "٥,٠٠٠", "٧٢.٥٪ مسدد", "سداد ١٣,٢١١ ر.س (إيجار، تدقيق، نهاية خدمة) ومتبقي ٥,٠٠٠ ر.س للحوكمة")'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated PowerPoint with Page 18 details!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated and recompiled with exact Page 18 Liabilities section!")
