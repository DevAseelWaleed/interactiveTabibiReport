# -*- coding: utf-8 -*-
"""
Add Official Sections from Page 11 (Bank Balances Analysis) and Page 12 (Income vs Expense Growth Hero Cards):
1. Page 12 Layout:
   - Side-by-side Income vs Expenses Bar Chart (Income: 582,167 vs 199,474 | Expenses: 249,274 vs 103,529)
   - 3 Hero Chevron/Arrow KPI Cards:
     * Card 1: 582,167 SAR (إجمالي الدخل لعام 2026م | +382,693 ريال عن 2025م +192%)
     * Card 2: 1,001,754 SAR (إجمالي الأرصدة المصرفية حتى 30/06/2026م)
     * Card 3: 972,713 SAR (صافي الأصول إلى 30/06/2026م "المركز المالي")
2. Page 11 Bottom Table:
   - Full 3-column Bank Balances & Fund Allocation Table (AlAhli, AlRajhi, Treatment Fund 367k, General 616k, Membership 18k, Opening 849,421 SAR).
   - Ihsan Detailed Notes (250k grant for 4 cancer cases, 186k spent on 3 cases, 63k remaining, 303k available medical aid).
3. Apply across:
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

# Define the HTML for Page 12 Hero Section & Page 11 Bank Balances Table
page_12_html = """        <!-- Page 12: Income & Expense Growth Overview (نمو الإيرادات والمصروفات) -->
        <div class="table-card" style="background:#FFF; border:2px solid var(--secondary); border-radius:var(--radius-xl); padding:30px; margin-top:35px; box-shadow:var(--shadow-md);">
            <div style="background:var(--primary); color:#FFF; padding:12px 24px; border-radius:var(--radius-lg); margin-bottom:25px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <h3 style="color:#FFF; font-size:1.3rem; margin:0;"><i class="fas fa-chart-simple" style="color:var(--secondary); margin-left:8px;"></i> نمو الإيرادات والمصروفات (مقارنة النصف الأول لعام ٢٠٢٦م بالنصف الأول لعام ٢٠٢٥م)</h3>
                <span style="background:var(--secondary); color:#FFF; padding:4px 14px; border-radius:var(--radius-pill); font-size:0.88rem; font-weight:700;">المطابقة الرسمية لصفحة ١٢ بالتقرير</span>
            </div>

            <div class="grid-2" style="align-items:center;">
                <!-- Left: Chart & Comparison -->
                <div style="background:var(--bg-subtle); padding:20px; border-radius:var(--radius-lg); border:1px solid rgba(0,0,0,0.05);">
                    <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;">مقارنة إجمالي الدخل والمصروفات (ريال سعودي)</h4>
                    <div style="height:280px; position:relative;">
                        <canvas id="page12GrowthChart"></canvas>
                    </div>
                    <div style="display:flex; justify-content:space-around; margin-top:15px; padding-top:10px; border-top:1px dashed #DDD; font-size:0.88rem;">
                        <div style="text-align:center;">
                            <span style="display:inline-block; width:12px; height:12px; background:#541228; border-radius:3px; margin-left:4px;"></span>
                            <strong>H1 2026م</strong>
                        </div>
                        <div style="text-align:center;">
                            <span style="display:inline-block; width:12px; height:12px; background:#8F8B85; border-radius:3px; margin-left:4px;"></span>
                            <strong>H1 2025م</strong>
                        </div>
                    </div>
                </div>

                <!-- Right: 3 Hero Arrow Cards (Matching Page 12 Graphic Exactly) -->
                <div style="display:flex; flex-direction:column; gap:18px;">
                    <!-- Card 1: Total Revenue -->
                    <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #541228; border-right:8px solid #541228; border-radius:var(--radius-lg); padding:18px 24px; box-shadow:var(--shadow-sm); position:relative;">
                        <div style="font-size:2.2rem; font-weight:900; color:#541228; line-height:1.1;">٥٨٢,١٦٧ <small style="font-size:1rem; font-weight:700; color:var(--text-muted);">ر.س</small></div>
                        <div style="font-size:1.05rem; font-weight:700; color:var(--text-main); margin-top:4px;">إجمالي الدخل لعام ٢٠٢٦م</div>
                        <div style="font-size:0.9rem; color:var(--success); font-weight:700; margin-top:4px;">
                            <i class="fas fa-arrow-up"></i> +٣٨٢,٦٩٣ ريال عن ٢٠٢٥م (+١٩٢٪)
                        </div>
                    </div>

                    <!-- Card 2: Bank Balances -->
                    <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #C9A96E; border-right:8px solid #C9A96E; border-radius:var(--radius-lg); padding:18px 24px; box-shadow:var(--shadow-sm); position:relative;">
                        <div style="font-size:2.2rem; font-weight:900; color:#8C6D37; line-height:1.1;">١,٠٠١,٧٥٤ <small style="font-size:1rem; font-weight:700; color:var(--text-muted);">ر.س</small></div>
                        <div style="font-size:1.05rem; font-weight:700; color:var(--text-main); margin-top:4px;">إجمالي الأرصدة المصرفية حتى ٣٠/٠٦/٢٠٢٦م</div>
                        <div style="font-size:0.88rem; color:var(--text-muted); margin-top:4px;">
                            (الأهلي: ٩٣٠,٧٠٢ ر.س | الراجحي: ٧١,٠٥٢ ر.س)
                        </div>
                    </div>

                    <!-- Card 3: Net Assets -->
                    <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #1B7A48; border-right:8px solid #1B7A48; border-radius:var(--radius-lg); padding:18px 24px; box-shadow:var(--shadow-sm); position:relative;">
                        <div style="font-size:2.2rem; font-weight:900; color:#1B7A48; line-height:1.1;">٩٧٢,٧١٣ <small style="font-size:1rem; font-weight:700; color:var(--text-muted);">ر.س</small></div>
                        <div style="font-size:1.05rem; font-weight:700; color:var(--text-main); margin-top:4px;">صافي الأصول إلى ٣٠/٠٦/٢٠٢٦م "المركز المالي"</div>
                        <div style="font-size:0.88rem; color:var(--success); font-weight:700; margin-top:4px;">
                            مقابل ٨٦٤,٠٤٥ ر.س في بداية الفترة (+١٠٨,٦٦٨ ر.س)
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Page 11 Bottom: Detailed Bank Balances & Fund Allocation Table -->
        <div class="table-card" style="margin-top:35px; border-top:4px solid var(--secondary);">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.35rem;"><i class="fas fa-building-columns" style="color:var(--secondary); margin-left:8px;"></i> بيان الأرصدة المصرفية وتحليل القيود والأرصدة الافتتاحية (صفحة ١١ بالتقرير)</h3>
                    <p style="font-size:0.92rem; color:var(--text-muted);">التفصيل الرسمي المعتمد لأرصدة البنوك، توزيع الأموال المقيدة وغير المقيدة، وملاحظات دعم منصة إحسان</p>
                </div>
                <span class="tag-pill tag-info" style="font-size:1rem; padding:6px 16px;">المطابقة الكاملة لصفحة ١١</span>
            </div>

            <table class="custom-table">
                <thead>
                    <tr>
                        <th style="width:25%;">الأرصدة المصرفية كما في ٣٠/٠٦/٢٠٢٦م</th>
                        <th style="width:25%;">تحليل الأرصدة والقيود (٣٠/٠٦/٢٠٢٦م)</th>
                        <th style="width:22%;">الأرصدة الافتتاحية (٠١/٠١/٢٠٢٦م مرحلة من ٢٠٢٥م)</th>
                        <th style="width:28%;">ملاحظات الأرصدة المصرفية المعتمدة</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                                <span>البنك الأهلي:</span>
                                <strong>٩٣٠,٧٠٢ ر.س</strong>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span>مصرف الراجحي:</span>
                                <strong>٧١,٠٥٢ ر.س</strong>
                            </div>
                        </td>
                        <td>
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <span>العلاج (أموال مقيدة):</span>
                                <strong style="color:var(--primary);">٣٦٧,٠٩٣ ر.س</strong>
                            </div>
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <span>الدعم والتبرعات العامة:</span>
                                <strong>٦١٦,٦٦١ ر.س</strong>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span>اشتراكات العضوية:</span>
                                <strong>١٨,٠٠٠ ر.س</strong>
                            </div>
                        </td>
                        <td>
                            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                                <span>البنك الأهلي:</span>
                                <strong>٨٤٨,٨٢٠ ر.س</strong>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span>مصرف الراجحي:</span>
                                <strong>٦٠١ ر.س</strong>
                            </div>
                        </td>
                        <td rowspan="2" style="vertical-align:top; font-size:0.88rem; line-height:1.7; background:#FAF8F5;">
                            <p style="margin-bottom:8px;">
                                • <strong>مبلغ (٢٥٠,٠٠٠) ريال:</strong> دعم مشروط مقيد من منصة إحسان لعلاج ٤ حالات سرطانية؛ تم علاج ٣ حالات بالمستشفى الألماني بمبلغ <strong>(١٨٦,٣٣٠) ريال</strong>، وتبقى مبلغ <strong>(٦٣,٦٧٠) ريال</strong> للحالة الرابعة.
                            </p>
                            <p style="margin:0;">
                                • <strong>الرصيد المتاح للدعم الطبي:</strong> من غير المتبقي من دعم منصة إحسان يبلغ <strong>(٣٠٣,٤٢٣) ريال</strong>.
                            </p>
                        </td>
                    </tr>
                    <tr class="total-row" style="background:#FFF9F0;">
                        <td><strong>الإجمالي: ١,٠٠١,٧٥٤ ر.س</strong></td>
                        <td><strong>الإجمالي: ١,٠٠١,٧٥٤ ر.س</strong></td>
                        <td><strong>الإجمالي: ٨٤٩,٤٢١ ر.س</strong></td>
                    </tr>
                </tbody>
            </table>
        </div>"""

# Insert this block right after comparative_table_html in Section 4
if "<!-- Page 12: Income & Expense Growth Overview" not in dash_code:
    target_pos = dash_code.find('<!-- Page 11 Bottom: Detailed Bank Balances')
    if target_pos == -1:
        ins_marker = '<div class="table-card" style="margin-top:35px; border-top:4px solid var(--primary);">'
        dash_code = dash_code.replace(ins_marker, page_12_html + "\n\n        " + ins_marker)
        with open(v2_file, "w", encoding="utf-8") as f:
            f.write(dash_code)
        print("Added Page 11 & 12 sections to generate_v2_dashboard.py!")

# Add Chart initialization script for Page 12 chart in generate_v2_dashboard.py
p12_chart_js = """            // 3. Page 12 Income vs Expenses Bar Chart
            const ctxP12 = document.getElementById('page12GrowthChart');
            if (ctxP12) {
                new Chart(ctxP12, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['إجمالي الدخل', 'إجمالي المصروفات'],
                        datasets: [
                            {
                                label: '٢٠٢٦م',
                                data: [582167, 249274],
                                backgroundColor: '#541228',
                                borderRadius: 6
                            },
                            {
                                label: '٢٠٢٥م',
                                data: [199474, 103529],
                                backgroundColor: '#8F8B85',
                                borderRadius: 6
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        layout: { padding: { top: 25, bottom: 5 } },
                        plugins: {
                            legend: { display: false },
                            tooltip: { rtl: true }
                        },
                        scales: {
                            y: { 
                                beginAtZero: true, 
                                suggestedMax: 650000,
                                ticks: { callback: v => v.toLocaleString() + ' ر.س' } 
                            }
                        }
                    }
                });
            }"""

if "page12GrowthChart" not in dash_code:
    dash_code = dash_code.replace("// 2. Expenses Distribution Doughnut Chart", p12_chart_js + "\n\n            // 2. Expenses Distribution Doughnut Chart")
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added Page 12 Chart to JavaScript in generate_v2_dashboard.py!")

# 2. Update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    w_code = f.read()

word_p11_table = """    add_rtl_heading(doc, "تحليل الأرصدة المصرفية والأرصدة الافتتاحية المرحّلة (صفحة ١١ بالتقرير)", level=2)
    p_bgt_desc = doc.add_paragraph()
    p_bgt_desc.paragraph_format.bidi = True
    p_bgt_desc.add_run("يوضح الجدول التالي تحليل الأرصدة المصرفية بحسابات الجمعية لدى البنك الأهلي ومصرف الراجحي كما في ٣٠/٠٦/٢٠٢٦م، وتوزيع القيود على الأموال المقيدة وغير المقيدة، ومقارنتها بالأرصدة الافتتاحية المرحّلة من عام ٢٠٢٥م، مع تفصيل دعم منصة إحسان:")
    
    t_bank = doc.add_table(rows=5, cols=4)
    t_bank.alignment = WD_TABLE_ALIGNMENT.CENTER
    bank_headers = ["الأرصدة المصرفية (٣٠/٠٦/٢٠٢٦م)", "تحليل القيود (٣٠/٠٦/٢٠٢٦م)", "الأرصدة الافتتاحية (٠١/٠١/٢٠٢٦م)", "ملاحظات الدعم المقيد وإحسان"]
    for j, h in enumerate(bank_headers):
        t_bank.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_bank.rows[0].cells[j], "6B1D3A")
        t_bank.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_bank.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_bank.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_bank.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9)
    
    bank_rows = [
        ("البنك الأهلي: ٩٣٠,٧٠٢ ر.س", "العلاج (مقيد): ٣٦٧,٠٩٣ ر.س", "البنك الأهلي: ٨٤٨,٨٢٠ ر.س", "دعم إحسان (٢٥٠ ألف ر.س) لعلاج ٤ حالات سرطانية"),
        ("مصرف الراجحي: ٧١,٠٥٢ ر.س", "الدعم العام: ٦١٦,٦٦١ ر.س", "مصرف الراجحي: ٦٠١ ر.س", "علاج ٣ حالات بالألماني بـ (١٨٦,٣٣٠ ر.س)"),
        ("—", "العضوية: ١٨,٠٠٠ ر.س", "—", "متبقي إحسان للحالة الرابعة: (٦٣,٦٧٠ ر.س)"),
        ("الإجمالي: ١,٠٠١,٧٥٤ ر.س", "الإجمالي: ١,٠٠١,٧٥٤ ر.س", "الإجمالي: ٨٤٩,٤٢١ ر.س", "المتاح للدعم الطبي دون إحسان: (٣٠٣,٤٢٣ ر.س)")
    ]
    for i, row in enumerate(bank_rows):
        r = t_bank.rows[i+1]
        for j, val in enumerate(row):
            r.cells[j].paragraphs[0].text = val
            r.cells[j].paragraphs[0].paragraph_format.bidi = True
            r.cells[j].paragraphs[0].runs[0].font.size = DPt(8.5)
            if i == 3:
                r.cells[j].paragraphs[0].runs[0].font.bold = True
                set_cell_background(r.cells[j], "FFF9F0")
            elif i % 2 == 1:
                set_cell_background(r.cells[j], "F8F6F0")
    doc.add_page_break()"""

if "تحليل الأرصدة المصرفية والأرصدة الافتتاحية المرحّلة" not in w_code:
    w_code = w_code.replace('add_rtl_heading(doc, "ثانياً: المساعدات العلاجية ونطاق الأثر السريري للمرضى (H1 2026)", level=1)', word_p11_table + '\n    add_rtl_heading(doc, "ثانياً: المساعدات العلاجية ونطاق الأثر السريري للمرضى (H1 2026)", level=1)')
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(w_code)
    print("Added Bank Balances Table to Word generator!")

# 3. Update PowerPoint (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

# Update Slide 5 insight box to include the full verbatim breakdown from Page 11 & Page 12
pptx_code = pptx_code.replace(
    'p_f2.text = "\\n• إجمالي النقدية بالبنوك: ١,٠٠١,٧٥٤ ريال\\n  - البنك الأهلي: ٩٣٠,٧٠٢ ريال\\n  - مصرف الراجحي: ٧١,٠٥٢ ريال\\n\\n• هيكل الأموال المتاحة:\\n  - أموال مقيدة (زكاة وعلاج): ٣٦٧,٠٩٣ ريال\\n  - أموال غير مقيدة: ٦٣٤,٦٦١ ريال\\n\\n• كفاية الاحتياطي النقدي: تغطية المصروفات التشغيلية لمدة ١٢ شهراً.\\n\\n• مخاطر التركز: تبرع واحد من فاعل خير بـ ٢٥٠ ألف ريال يمثل ٤٣٪ من إجمالي الدخل."',
    'p_f2.text = "\\n• إجمالي النقدية بالبنوك: ١,٠٠١,٧٥٤ ريال (الأهلي: ٩٣٠,٧٠٢ | الراجحي: ٧١,٠٥٢)\\n• الأرصدة الافتتاحية المرحّلة من ٢٠٢٥م: ٨٤٩,٤٢١ ريال (الأهلي: ٨٤٨,٨٢٠ | الراجحي: ٦٠١)\\n\\n• تحليل قيود الأرصدة (ص ١١):\\n  - العلاج (مقيد): ٣٦٧,٠٩٣ ريال (يشمل ٢٥٠ ألف دعم إحسان لأورام)\\n  - التبرعات والدعم العام: ٦١٦,٦٦١ ريال\\n  - اشتراكات العضوية: ١٨,٠٠٠ ريال\\n\\n• كفاءة الدخل والمصروفات (ص ١٢):\\n  - إجمالي الدخل: ٥٨٢,١٦٧ ريال (+١٩٢٪)\\n  - إجمالي المصروفات: ٢٤٩,٢٧٤ ريال\\n  - صافي الأصول بالمركز المالي: ٩٧٢,٧١٣ ريال"'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated PowerPoint Slide 5 with exact Page 11 & 12 details!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated and recompiled with official Pages 11 & 12 sections!")
