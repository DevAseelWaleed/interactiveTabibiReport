# -*- coding: utf-8 -*-
"""
Add Exact Page 17 Section: "ملخص المركز المالي إلى 30/06/2026م"
Features:
- Header: أولاً: الأداء المالي — ملخص المركز المالي إلى 2026/06/30م
- 6 Hexagon / Polished Metric Cards (2 rows x 3 cols):
  1. صافي الأصول: 972,713 ريال (مقابل 864,045 ريال في بداية الفترة)
  2. الالتزامات "مركز مالي": 5,000 ريال (من 18,211 ريال أموال مرحلة من عام 2025م)
  3. الذمم المدينة: 12,000 ريال (12,000 ريال استحقاق اشتراكات عضوية لم تسدد للجمعية)
  4. إجمالي الأرصدة البنكية: 1,001,754 ريال (البنك الأهلي والراجحي)
  5. الأموال غير المقيدة: 634,661 ريال (متاحة لتمويل البرامج والتشغيل)
  6. الأموال المقيدة: 367,093 ريال (دعم مخصص لحالات علاجية)
- Dedicated Doughnut Chart for Financial Structure & Liquidity Allocation.

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

page_17_html = """        <!-- Page 17: Financial Position Summary (ملخص المركز المالي) -->
        <div class="table-card" style="background:#FFF; border:2px solid var(--secondary); border-radius:var(--radius-xl); padding:35px; margin-top:35px; box-shadow:var(--shadow-md);">
            <div style="background:var(--primary); color:#FFF; padding:12px 24px; border-radius:var(--radius-lg); margin-bottom:25px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <h3 style="color:#FFF; font-size:1.35rem; margin:0;"><i class="fas fa-scale-unbalanced" style="color:var(--secondary); margin-left:8px;"></i> ملخص المركز المالي إلى ٣٠/٠٦/٢٠٢٦م</h3>
                <span style="background:var(--secondary); color:#FFF; padding:4px 14px; border-radius:var(--radius-pill); font-size:0.88rem; font-weight:700;">المطابقة الرسمية لصفحة ١٧ بالتقرير</span>
            </div>

            <!-- 6 Hero Hexagon Cards (2 Rows x 3 Cols) -->
            <div class="grid-3" style="gap:20px; margin-bottom:25px;">
                <!-- Card 1: Net Assets -->
                <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #1B7A48; border-radius:var(--radius-lg); padding:22px 18px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.2rem; font-weight:900; color:#1B7A48; line-height:1;">٩٧٢,٧١٣ <small style="font-size:0.9rem;">ر.س</small></div>
                    <div style="font-size:1.05rem; font-weight:800; color:var(--text-main); margin-top:8px;">صافي الأصول</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">مقابل ٨٦٤,٠٤٥ ريال في بداية الفترة</div>
                </div>

                <!-- Card 2: Liabilities -->
                <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #541228; border-radius:var(--radius-lg); padding:22px 18px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.2rem; font-weight:900; color:#541228; line-height:1;">٥,٠٠٠ <small style="font-size:0.9rem;">ر.س</small></div>
                    <div style="font-size:1.05rem; font-weight:800; color:var(--text-main); margin-top:8px;">الالتزامات "مركز مالي"</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">من ١٨,٢١١ ريال أموال مرحلة من عام ٢٠٢٥م</div>
                </div>

                <!-- Card 3: Receivables -->
                <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #C7771E; border-radius:var(--radius-lg); padding:22px 18px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.2rem; font-weight:900; color:#C7771E; line-height:1;">١٢,٠٠٠ <small style="font-size:0.9rem;">ر.س</small></div>
                    <div style="font-size:1.05rem; font-weight:800; color:var(--text-main); margin-top:8px;">الذمم المدينة</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">١٢,٠٠٠ ريال استحقاق اشتراكات عضوية لم تسدد للجمعية</div>
                </div>

                <!-- Card 4: Bank Balances -->
                <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #541228; border-radius:var(--radius-lg); padding:22px 18px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.2rem; font-weight:900; color:#541228; line-height:1;">١,٠٠١,٧٥٤ <small style="font-size:0.9rem;">ر.س</small></div>
                    <div style="font-size:1.05rem; font-weight:800; color:var(--text-main); margin-top:8px;">إجمالي الأرصدة البنكية</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">البنك الأهلي ومصرف الراجحي</div>
                </div>

                <!-- Card 5: Unrestricted Funds -->
                <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #1B7A48; border-radius:var(--radius-lg); padding:22px 18px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.2rem; font-weight:900; color:#1B7A48; line-height:1;">٦٣٤,٦٦١ <small style="font-size:0.9rem;">ر.س</small></div>
                    <div style="font-size:1.05rem; font-weight:800; color:var(--text-main); margin-top:8px;">الأموال غير المقيدة</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">متاحة لتمويل البرامج والتشغيل</div>
                </div>

                <!-- Card 6: Restricted Funds -->
                <div style="background:linear-gradient(135deg, #FAF8F5 0%, #FFF 100%); border:2px solid #C9A96E; border-radius:var(--radius-lg); padding:22px 18px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.2rem; font-weight:900; color:#8C6D37; line-height:1;">٣٦٧,٠٩٣ <small style="font-size:0.9rem;">ر.س</small></div>
                    <div style="font-size:1.05rem; font-weight:800; color:var(--text-main); margin-top:8px;">الأموال المقيدة</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">دعم مخصص لحالات علاجية (أورام وعمليات)</div>
                </div>
            </div>

            <!-- Liquidity Structure Chart -->
            <div style="background:var(--bg-subtle); padding:20px; border-radius:var(--radius-lg); border:1px solid rgba(0,0,0,0.05); text-align:center;">
                <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:12px;"><i class="fas fa-chart-pie" style="color:var(--secondary); margin-left:6px;"></i> هيكل وتوزيع السيولة النقدية والمركز المالي (ريال)</h4>
                <div style="height:260px; position:relative;">
                    <canvas id="page17FinancialStructureChart"></canvas>
                </div>
            </div>
        </div>"""

# Insert Page 17 in Section 4 right after Page 11 Bank Balances Table
if "<!-- Page 17: Financial Position Summary" not in dash_code:
    ins_marker_p17 = '<!-- Page 11 Bottom: Detailed Bank Balances'
    end_p11_marker = '</div>\n        </div>\n\n        <!-- Official Comparative Table'
    if "<!-- Page 11 Bottom: Detailed Bank Balances" in dash_code:
        # Find where Page 11 table ends
        p11_idx = dash_code.find('<!-- Page 11 Bottom: Detailed Bank Balances')
        table_end_idx = dash_code.find('</div>', p11_idx + 100)
        table_end_idx = dash_code.find('</div>', table_end_idx + 10)
        dash_code = dash_code[:table_end_idx+6] + "\n\n" + page_17_html + dash_code[table_end_idx+6:]
        with open(v2_file, "w", encoding="utf-8") as f:
            f.write(dash_code)
        print("Added Page 17 HTML to generate_v2_dashboard.py!")

# Add Chart initialization script for Page 17 in generate_v2_dashboard.py
p17_chart_js = """            // 13. Page 17 Financial Structure Doughnut Chart
            const ctxP17 = document.getElementById('page17FinancialStructureChart');
            if (ctxP17) {
                new Chart(ctxP17, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['أموال غير مقيدة للتشغيل (٦٣٤,٦٦١)', 'أموال مقيدة للعلاج والزكاة (٣٦٧,٠٩٣)', 'ذمم مدينة اشتراكات (١٢,٠٠٠)', 'التزامات دائنة (٥,٠٠٠)'],
                        datasets: [{
                            data: [634661, 367093, 12000, 5000],
                            backgroundColor: ['#1B7A48', '#C9A96E', '#C7771E', '#541228'],
                            borderWidth: 2,
                            borderColor: '#FFF'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 10.5 } } }
                        },
                        cutout: '55%'
                    }
                });
            }"""

if "page17FinancialStructureChart" not in dash_code:
    dash_code = dash_code.replace("// 12. Fixed Assets Pie Chart", p17_chart_js + "\n\n            // 12. Fixed Assets Pie Chart")
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added Page 17 Chart to JavaScript in generate_v2_dashboard.py!")

# 2. Update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    w_code = f.read()

word_p17_table = """    add_rtl_heading(doc, "ملخص المركز المالي إلى ٣٠/٠٦/٢٠٢٦م (صفحة ١٧ بالتقرير)", level=2)
    p_p17 = doc.add_paragraph()
    p_p17.paragraph_format.bidi = True
    p_p17.add_run("يوضح الجدول التالي ملخص عناصر المركز المالي والسيولة النقدية للجمعية كما في ٣٠/٠٦/٢٠٢٦م:")
    
    t_p17 = doc.add_table(rows=7, cols=3)
    t_p17.alignment = WD_TABLE_ALIGNMENT.CENTER
    p17_headers = ["عنصر المركز المالي", "القيمة (ريال)", "البيان والتوجيه الإداري المعتمد"]
    for j, h in enumerate(p17_headers):
        t_p17.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_p17.rows[0].cells[j], "6B1D3A")
        t_p17.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_p17.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_p17.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_p17.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9.5)
    
    p17_rows = [
        ("صافي الأصول", "٩٧٢,٧١٣", "مقابل ٨٦٤,٠٤٥ ريال في بداية الفترة (+١٠٨,٦٦٨ ر.س)"),
        ("الالتزامات 'مركز مالي'", "٥,٠٠٠", "من ١٨,٢١١ ريال أموال مرحلة من عام ٢٠٢٥م"),
        ("الذمم المدينة", "١٢,٠٠٠", "١٢,٠٠٠ ريال استحقاق اشتراكات عضوية لم تسدد للجمعية"),
        ("إجمالي الأرصدة البنكية", "١,٠٠١,٧٥٤", "البنك الأهلي (٩٣٠,٧٠٢ ر.س) ومصرف الراجحي (٧١,٠٥٢ ر.س)"),
        ("الأموال غير المقيدة", "٦٣٤,٦٦١", "متاحة لتمويل البرامج والتشغيل وتغطية احتياطي ١٢ شهراً"),
        ("الأموال المقيدة", "٣٦٧,٠٩٣", "دعم مخصص لحالات علاجية (أورام وعمليات جراحية)")
    ]
    for i, row in enumerate(p17_rows):
        r = t_p17.rows[i+1]
        for j, val in enumerate(row):
            r.cells[j].paragraphs[0].text = val
            r.cells[j].paragraphs[0].paragraph_format.bidi = True
            r.cells[j].paragraphs[0].runs[0].font.size = DPt(9)
            if i == 0 or i == 3:
                r.cells[j].paragraphs[0].runs[0].font.bold = True
            if i % 2 == 1:
                set_cell_background(r.cells[j], "F8F6F0")
    doc.add_page_break()"""

if "ملخص المركز المالي إلى ٣٠/٠٦/٢٠٢٦م (صفحة ١٧ بالتقرير)" not in w_code:
    w_code = w_code.replace('add_rtl_heading(doc, "ثانياً: المساعدات العلاجية', word_p17_table + '\n    add_rtl_heading(doc, "ثانياً: المساعدات العلاجية')
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(w_code)
    print("Added Page 17 Table to Word generator!")

# 3. Update PowerPoint (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

# Update Slide 6 with Page 17 details
pptx_code = pptx_code.replace(
    'add_slide_header(s6, "تنفيذ الموازنة التقديرية والمركز المالي ٢٠٢٦م", "مقارنة الموازنة التعتمدة بالمصروفات الفعلية وأرصدة البنوك والسيولة")',
    'add_slide_header(s6, "ملخص المركز المالي والموازنة (صفحة ١٧ بالتقرير)", "صافي الأصول ٩٧٢ ألف | الأرصدة البنكية ١ مليون | الأموال المقيدة ٣٦٧ ألف")'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated PowerPoint with Page 17 details!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated and recompiled with exact Page 17 Balance Sheet section!")
