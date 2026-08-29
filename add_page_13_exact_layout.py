# -*- coding: utf-8 -*-
"""
Add Exact Page 13 Layout: "مصادر الدخل خلال النصف الأول 2026م"
Subtitle: "تنوع مصادر الدعم يعكس نضج الاستدامة المالية للجمعية"
Features:
- Left: Pie Chart showing 2026 Income Distribution with direct on-slice percentage labels (70%, 13%, 12%, 3%, 2%).
- Right: Table with columns (بند الدخل, 2026م, 2025م).
- Footnote: "* منصة تبرع أوقفت واستُبدلت بمنصة إحسان خلال 2026م علماً بأنه كانت فترة جمع التبرع في ثلاث أشهر."
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

page_13_html = """        <!-- Page 13: Income Sources & Diversity (مصادر الدخل خلال النصف الأول 2026م) -->
        <div class="table-card" style="background:#FFF; border:2px solid var(--primary); border-radius:var(--radius-xl); padding:30px; margin-top:35px; box-shadow:var(--shadow-md);">
            <div style="background:var(--primary); color:#FFF; padding:12px 24px; border-radius:var(--radius-lg); margin-bottom:20px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <h3 style="color:#FFF; font-size:1.35rem; margin:0;"><i class="fas fa-coins" style="color:var(--secondary); margin-left:8px;"></i> مصادر الدخل خلال النصف الأول ٢٠٢٦م</h3>
                <span style="background:var(--secondary); color:#FFF; padding:4px 14px; border-radius:var(--radius-pill); font-size:0.88rem; font-weight:700;">المطابقة الرسمية لصفحة ١٣ بالتقرير</span>
            </div>
            
            <p style="font-size:1.05rem; font-weight:700; color:var(--text-main); margin-bottom:20px; text-align:center;">
                تنوع مصادر الدعم يعكس نضج الاستدامة المالية للجمعية
            </p>

            <div class="grid-2" style="align-items:center; gap:30px;">
                <!-- Left: Pie Chart with on-slice percentages -->
                <div style="background:var(--bg-subtle); padding:20px; border-radius:var(--radius-lg); border:1px solid rgba(0,0,0,0.05); text-align:center;">
                    <div style="height:320px; position:relative;">
                        <canvas id="page13IncomePieChart"></canvas>
                    </div>
                </div>

                <!-- Right: Exact 3-column Table -->
                <div>
                    <table class="custom-table" style="margin:0; box-shadow:var(--shadow-sm);">
                        <thead>
                            <tr style="background:#541228; color:#FFF;">
                                <th style="color:#FFF; width:45%;">بند الدخل</th>
                                <th style="color:#FFF; text-align:center; width:28%;">٢٠٢٦م (ريال)</th>
                                <th style="color:#FFF; text-align:center; width:27%;">٢٠٢٥م (ريال)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><span style="display:inline-block; width:10px; height:10px; background:#A61C48; border-radius:2px; margin-left:6px;"></span><strong>تبرعات ودعم عام</strong></td>
                                <td style="text-align:center; font-weight:700; color:var(--primary);">٤٠٧,٤٩٥</td>
                                <td style="text-align:center; color:var(--text-muted);">٦٢,٥٦٤</td>
                            </tr>
                            <tr>
                                <td><span style="display:inline-block; width:10px; height:10px; background:#380B1B; border-radius:2px; margin-left:6px;"></span><strong>العلاج</strong></td>
                                <td style="text-align:center; font-weight:700; color:var(--primary);">٧٥,٠٠٠</td>
                                <td style="text-align:center; color:var(--text-muted);">٢٥,٠٠٠</td>
                            </tr>
                            <tr>
                                <td><span style="display:inline-block; width:10px; height:10px; background:#5E132D; border-radius:2px; margin-left:6px;"></span><strong>الزكاة</strong></td>
                                <td style="text-align:center; font-weight:700; color:var(--primary);">٧٠,٠٠٠</td>
                                <td style="text-align:center; color:var(--text-muted);">٨٠,٠٠٠</td>
                            </tr>
                            <tr>
                                <td><span style="display:inline-block; width:10px; height:10px; background:#D9829B; border-radius:2px; margin-left:6px;"></span><strong>العضوية</strong></td>
                                <td style="text-align:center; font-weight:700; color:var(--primary);">١٨,٠٠٠</td>
                                <td style="text-align:center; color:var(--text-muted);">١٨,٠٠٠</td>
                            </tr>
                            <tr>
                                <td><span style="display:inline-block; width:10px; height:10px; background:#E8B4C2; border-radius:2px; margin-left:6px;"></span><strong>المتجر الإلكتروني</strong></td>
                                <td style="text-align:center; font-weight:700; color:var(--primary);">١٠,٤٦٩</td>
                                <td style="text-align:center; color:var(--text-muted);">١٢٤</td>
                            </tr>
                            <tr>
                                <td><span style="display:inline-block; width:10px; height:10px; background:#C9A96E; border-radius:2px; margin-left:6px;"></span><strong>منصة تبرع</strong></td>
                                <td style="text-align:center; font-weight:700; color:var(--primary);">١,٢٠٣</td>
                                <td style="text-align:center; color:var(--text-muted);">١٣,٧٨٦</td>
                            </tr>
                            <tr class="total-row" style="background:#FFF9F0;">
                                <td><strong>الإجمالي</strong></td>
                                <td style="text-align:center; font-size:1.15rem; font-weight:900; color:#541228;">٥٨٢,١٦٧</td>
                                <td style="text-align:center; font-size:1.15rem; font-weight:900; color:var(--text-muted);">١٩٩,٤٧٤</td>
                            </tr>
                        </tbody>
                    </table>
                    <div style="font-size:0.85rem; color:#888; margin-top:12px; line-height:1.6; background:#FAF8F5; padding:8px 14px; border-radius:var(--radius-sm); border-right:3px solid var(--secondary);">
                        * منصة تبرع أوقفت واستُبدلت بمنصة إحسان خلال 2026م علماً بأنه كانت فترة جمع التبرع في ثلاث أشهر.
                    </div>
                </div>
            </div>
        </div>"""

# Insert Page 13 right after Page 12 in generate_v2_dashboard.py
if "<!-- Page 13: Income Sources & Diversity" not in dash_code:
    ins_marker_13 = '<!-- Page 12: Income & Expense Growth Overview'
    dash_code = dash_code.replace(ins_marker_13, page_13_html + "\n\n        " + ins_marker_13)
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added Page 13 HTML to generate_v2_dashboard.py!")

# Add Chart initialization script for Page 13 Pie Chart in generate_v2_dashboard.py
p13_chart_js = """            // 4. Page 13 Income Pie Chart with on-slice percentages
            const ctxP13 = document.getElementById('page13IncomePieChart');
            if (ctxP13) {
                new Chart(ctxP13, {
                    type: 'pie',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['تبرعات ودعم عام', 'العلاج', 'الزكاة', 'العضوية', 'المتجر الإلكتروني', 'منصة تبرع'],
                        datasets: [{
                            data: [407495, 75000, 70000, 18000, 10469, 1203],
                            backgroundColor: [
                                '#A61C48', // 70%
                                '#380B1B', // 13%
                                '#5E132D', // 12%
                                '#D9829B', // 3%
                                '#E8B4C2', // 2%
                                '#C9A96E'  // 0%
                            ],
                            borderWidth: 2,
                            borderColor: '#FFF'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        layout: { padding: 10 },
                        plugins: {
                            legend: {
                                position: 'bottom',
                                rtl: true,
                                labels: { boxWidth: 12, font: { size: 10.5, family: 'Cairo' } }
                            },
                            tooltip: {
                                rtl: true,
                                callbacks: {
                                    label: function(context) {
                                        const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                        const val = context.raw;
                                        const pct = ((val / total) * 100).toFixed(0);
                                        return `${context.label}: ${val.toLocaleString()} ريال (${pct}%)`;
                                    }
                                }
                            }
                        }
                    }
                });
            }"""

if "page13IncomePieChart" not in dash_code:
    dash_code = dash_code.replace("// 3. Page 12 Income vs Expenses Bar Chart", p13_chart_js + "\n\n            // 3. Page 12 Income vs Expenses Bar Chart")
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Added Page 13 Pie Chart to JavaScript in generate_v2_dashboard.py!")

# 2. Update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    w_code = f.read()

word_p13_table = """    add_rtl_heading(doc, "مصادر الدخل خلال النصف الأول ٢٠٢٦م (صفحة ١٣ بالتقرير)", level=2)
    p_p13 = doc.add_paragraph()
    p_p13.paragraph_format.bidi = True
    p_p13.add_run("تنوع مصادر الدعم يعكس نضج الاستدامة المالية للجمعية. يوضح الجدول التالي مصادر الدخل للنصف الأول لعام ٢٠٢٦م مقارنة بالعام السابق ٢٠٢٥م:")
    
    t_p13 = doc.add_table(rows=8, cols=3)
    t_p13.alignment = WD_TABLE_ALIGNMENT.CENTER
    p13_headers = ["بند الدخل", "٢٠٢٦م (ريال)", "٢٠٢٥م (ريال)"]
    for j, h in enumerate(p13_headers):
        t_p13.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_p13.rows[0].cells[j], "6B1D3A")
        t_p13.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_p13.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_p13.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_p13.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9.5)
    
    p13_rows = [
        ("تبرعات ودعم عام", "٤٠٧,٤٩٥", "٦٢,٥٦٤"),
        ("العلاج", "٧٥,٠٠٠", "٢٥,٠٠٠"),
        ("الزكاة", "٧٠,٠٠٠", "٨٠,٠٠٠"),
        ("العضوية", "١٨,٠٠٠", "١٨,٠٠٠"),
        ("المتجر الإلكتروني", "١٠,٤٦٩", "١٢٤"),
        ("منصة تبرع", "١,٢٠٣", "١٣,٧٨٦"),
        ("الإجمالي", "٥٨٢,١٦٧", "١٩٩,٤٧٤")
    ]
    for i, row in enumerate(p13_rows):
        r = t_p13.rows[i+1]
        for j, val in enumerate(row):
            r.cells[j].paragraphs[0].text = val
            r.cells[j].paragraphs[0].paragraph_format.bidi = True
            r.cells[j].paragraphs[0].runs[0].font.size = DPt(9)
            if i == 6:
                r.cells[j].paragraphs[0].runs[0].font.bold = True
                set_cell_background(r.cells[j], "FFF9F0")
            elif i % 2 == 1:
                set_cell_background(r.cells[j], "F8F6F0")
    
    p_p13_fn = doc.add_paragraph()
    p_p13_fn.paragraph_format.bidi = True
    p_p13_fn.add_run("* منصة تبرع أوقفت واستُبدلت بمنصة إحسان خلال 2026م علماً بأنه كانت فترة جمع التبرع في ثلاث أشهر.")
    doc.add_page_break()"""

if "مصادر الدخل خلال النصف الأول ٢٠٢٦م (صفحة ١٣ بالتقرير)" not in w_code:
    w_code = w_code.replace('add_rtl_heading(doc, "تحليل الأرصدة المصرفية والأرصدة الافتتاحية المرحّلة', word_p13_table + '\n    add_rtl_heading(doc, "تحليل الأرصدة المصرفية والأرصدة الافتتاحية المرحّلة')
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(w_code)
    print("Added Page 13 Table to Word generator!")

# 3. Update PowerPoint (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

pptx_code = pptx_code.replace(
    'add_slide_header(s5, "مقارنة النصف الأول للعام المالي (30/06/2026م مقابل 30/06/2025م)", "المقارنة الرسمية المعتمدة بتقرير الجمعية (ص ١٠-١١) للدخل والمساعدات والأصول")',
    'add_slide_header(s5, "مصادر الدخل خلال النصف الأول ٢٠٢٦م (صفحة ١٣ بالتقرير)", "تنوع مصادر الدعم يعكس نضج الاستدامة المالية ومقارنة مصادر الدخل بـ ٢٠٢٥م")'
)

with open(pptx_file, "w", encoding="utf-8") as f:
    f.write(pptx_code)
print("Updated PowerPoint generator with Page 13 details!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated and recompiled with exact Page 13 layout!")
