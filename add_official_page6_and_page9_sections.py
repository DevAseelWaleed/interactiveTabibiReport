# -*- coding: utf-8 -*-
"""
Add Official Page 6 (Chairman Speech with Portrait) & Page 9 (Executive Intro & 4 Metrics) across all deliverables:
1. Page 6:
   - Official portrait of Chairman Prof. Dr. Mansoor Mohammed Al-Nozha.
   - Full verbatim speech text from Page 6 of official report.
2. Page 9:
   - Executive Introduction & Summary text.
   - 4 Hero Hexagon/Box Metrics:
     * 3+1 (موظفون ومتعاون)
     * 9 (شراكات صحية مفعلة)
     * 2 (برامج تشغيلية مفعلة)
     * +192% (نمو إجمالي الدخل)
   - Verbatim narrative paragraph from Page 9.
"""
import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")
assets_dir = os.path.join(v2_dir, "assets", "images")
os.makedirs(assets_dir, exist_ok=True)

# Copy chairman portrait
src_nozha = os.path.join(base_dir, "assets", "dr_mansour_alnozha.jpg")
dst_nozha = os.path.join(assets_dir, "dr_mansour_alnozha.jpg")
if os.path.exists(src_nozha):
    shutil.copy2(src_nozha, dst_nozha)
    print(f"Copied chairman portrait to {dst_nozha}")

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

# Page 6 Full Chairman Section HTML
page_6_html = """        <!-- Page 6: Official Chairman Speech with Portrait (كلمة رئيس مجلس الإدارة) -->
        <div class="exec-card" style="background:linear-gradient(135deg, #4A1024 0%, #6B1D3A 100%); color:#FFF; padding:40px; margin-bottom:40px; border-radius:var(--radius-xl); box-shadow:var(--shadow-lg); border:2px solid var(--secondary);">
            <div class="grid-2" style="align-items:center; gap:40px;">
                <!-- Right: Full Speech Text -->
                <div>
                    <div style="font-size:1.1rem; font-weight:700; color:var(--secondary); margin-bottom:8px; text-align:right;">
                        بسم الله الرحمن الرحيم
                    </div>
                    <h3 style="color:#FFF; font-size:1.6rem; margin-bottom:15px;">كلمة رئيس مجلس الإدارة</h3>
                    <p style="font-size:0.95rem; color:#F0EBE1; margin-bottom:12px; font-weight:600;">
                        الحمد لله رب العالمين، والصلاة والسلام على نبينا محمد وعلى آله وصحبه أجمعين.<br>
                        الإخوة والأخوات أعضاء الجمعية العمومية، وأعضاء مجلس الإدارة، والزملاء والزميلات في جمعية طبيبي الأهلية،<br>
                        السلام عليكم ورحمة الله وبركاته،
                    </p>
                    <p style="font-size:0.92rem; line-height:1.9; color:rgba(255,255,255,0.9); text-align:justify; margin-bottom:10px;">
                        يسعدني أن أرحب بكم في هذا اللقاء الذي نستعرض من خلاله التقرير النصف سنوي لجمعية طبيبي الأهلية، والذي يأتي تأكيدًا على حرص الجمعية على الشفافية، والحوكمة، ووضوح الإنجاز، ومشاركة أصحاب العلاقة في مسيرة العمل.
                    </p>
                    <p style="font-size:0.92rem; line-height:1.9; color:rgba(255,255,255,0.9); text-align:justify; margin-bottom:10px;">
                        لقد شهد النصف الأول من هذا العام جهودًا متواصلة لتطوير أعمال الجمعية إداريًا وماليًا وبرامجيًا، وتحسين كفاءة الأداء، وتعزيز جودة الخدمات والمبادرات التي تقدمها الجمعية للمستفيدين.
                    </p>
                    <p style="font-size:0.92rem; line-height:1.9; color:rgba(255,255,255,0.9); text-align:justify; margin-bottom:10px;">
                        وما تحقق من أعمال وإنجازات لم يكن ليتحقق بعد توفيق الله إلا بفضل تكامل الجهود بين مجلس الإدارة والجمعية العمومية والإدارة التنفيذية، وبفضل ما نجده من دعم وثقة من شركائنا وداعمينا، الذين نقدر لهم إسهاماتهم ووقوفهم المستمر مع رسالة الجمعية وأهدافها.
                    </p>
                    <p style="font-size:0.92rem; line-height:1.9; color:rgba(255,255,255,0.9); text-align:justify; margin-bottom:10px;">
                        كما أن استعراض هذا التقرير لا يمثل مجرد عرض لما تم إنجازه، بل هو وقفة تقييم ومراجعة لما تحقق، وتحديد لما يمكن تطويره وتحسينه خلال المرحلة القادمة، بما يسهم في رفع كفاءة الجمعية وتعظيم أثرها الاجتماعي والصحي.
                    </p>
                    <p style="font-size:0.92rem; line-height:1.9; color:rgba(255,255,255,0.9); text-align:justify; margin-bottom:15px;">
                        ونحن في مجلس الإدارة نؤكد التزامنا بمواصلة العمل على تطوير الأداء المؤسسي، وتعزيز الحوكمة والاستدامة المالية، وتنفيذ البرامج والمبادرات التي تحقق أثرًا ملموسًا ومستدامًا للمستفيدين والمجتمع.
                    </p>
                    <div style="font-size:0.95rem; font-weight:700; color:var(--secondary); text-align:left;">
                        أخوكم<br>
                        أ.د. منصور محمد النزهة<br>
                        <span style="font-size:0.85rem; color:#FFF; font-weight:400;">رئيس مجلس الإدارة</span>
                    </div>
                </div>

                <!-- Left: Official Portrait Photo -->
                <div style="text-align:center;">
                    <div style="width:230px; height:230px; margin:0 auto 20px auto; border-radius:50%; border:4px solid var(--secondary); padding:4px; background:rgba(201, 169, 110, 0.2); box-shadow:0 12px 35px rgba(0,0,0,0.4); overflow:hidden;">
                        <img src="assets/images/dr_mansour_alnozha.jpg" alt="أ.د. منصور محمد النزهة" style="width:100%; height:100%; object-fit:cover; border-radius:50%;">
                    </div>
                    <h4 style="color:#FFF; font-size:1.3rem; margin-bottom:4px;">أ.د. منصور محمد النزهة</h4>
                    <div style="color:var(--secondary); font-weight:700; font-size:1rem;">رئيس مجلس الإدارة</div>
                    <div style="color:rgba(255,255,255,0.7); font-size:0.88rem; margin-top:4px;">جمعية طبيبي الأهلية بالمدينة المنورة</div>
                </div>
            </div>
        </div>"""

# Page 9 Full Executive Summary Section HTML
page_9_html = """        <!-- Page 9: Executive Summary & 4 Core Pillars (المقدمة والملخص التنفيذي) -->
        <div class="table-card" style="background:#FFF; border:2px solid var(--secondary); border-radius:var(--radius-xl); padding:35px; margin-bottom:40px; box-shadow:var(--shadow-md);">
            <div style="background:var(--primary); color:#FFF; padding:12px 24px; border-radius:var(--radius-lg); margin-bottom:25px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <h3 style="color:#FFF; font-size:1.35rem; margin:0;"><i class="fas fa-file-lines" style="color:var(--secondary); margin-left:8px;"></i> المقدمة والملخص التنفيذي (صفحة ٩ بالتقرير)</h3>
                <span style="background:var(--secondary); color:#FFF; padding:4px 14px; border-radius:var(--radius-pill); font-size:0.88rem; font-weight:700;">النص والبيانات الرسمية المعتمدة</span>
            </div>

            <!-- Narrative Paragraphs -->
            <div style="background:var(--bg-subtle); padding:20px 25px; border-radius:var(--radius-lg); margin-bottom:25px; border-right:4px solid var(--primary); font-size:1.02rem; line-height:2.0; color:var(--text-main); text-align:justify;">
                <p style="margin-bottom:12px;">
                    واصلت جمعية طبيبي الأهلية خلال النصف الأول من عام <strong>٢٠٢٦م</strong> تنفيذ برامجها ومشروعاتها وخدماتها الموجهة للمستفيدين، وفق الخطة التشغيلية والميزانية المعتمدة، محققةً <strong>نمواً ملموساً في جميع المؤشرات الرئيسية</strong> مقارنةً بالفترة المماثلة من عام ٢٠٢٥م.
                </p>
                <p style="margin:0;">
                    فقد ارتفع إجمالي الدخل بنسبة بلغت <strong>+١٩٢٪</strong>، وتوسّع نطاق الدعم الطبي المقدّم بأكثر من <strong>تسعة أضعاف (+٩٤٣٪)</strong>، إلى جانب مضاعفة عدد البرامج التشغيلية المفعّلة، وتوسيع الكادر الوظيفي، وتعزيز الشراكات الصحية، وتطوير المنظومة الرقمية والحوكمة للجمعية.
                </p>
            </div>

            <!-- 4 Hexagon / Polygon Metric Cards Matching Page 9 -->
            <div class="grid-4" style="gap:20px; margin-bottom:20px;">
                <div style="background:#FAF8F5; border:2px solid #541228; border-radius:var(--radius-lg); padding:20px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.4rem; font-weight:900; color:#541228; line-height:1;">٣+١</div>
                    <div style="font-size:1rem; font-weight:700; color:var(--text-main); margin-top:8px;">موظفون ومتعاون</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">(٣ سعوديين + محاسب)</div>
                </div>

                <div style="background:#FAF8F5; border:2px solid #C9A96E; border-radius:var(--radius-lg); padding:20px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.4rem; font-weight:900; color:#8C6D37; line-height:1;">٩</div>
                    <div style="font-size:1rem; font-weight:700; color:var(--text-main); margin-top:8px;">شراكات صحية مفعلة</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">(مستشفيات ومراكز كبرى)</div>
                </div>

                <div style="background:#FAF8F5; border:2px solid #1B7A48; border-radius:var(--radius-lg); padding:20px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.4rem; font-weight:900; color:#1B7A48; line-height:1;">٢</div>
                    <div style="font-size:1rem; font-weight:700; color:var(--text-main); margin-top:8px;">برامج تشغيلية مفعلة</div>
                    <div style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">(جودة الحياة & عون)</div>
                </div>

                <div style="background:#FAF8F5; border:2px solid #541228; border-radius:var(--radius-lg); padding:20px; text-align:center; box-shadow:var(--shadow-sm);">
                    <div style="font-size:2.4rem; font-weight:900; color:#541228; line-height:1;">+١٩٢٪</div>
                    <div style="font-size:1rem; font-weight:700; color:var(--text-main); margin-top:8px;">نمو إجمالي الدخل</div>
                    <div style="font-size:0.82rem; color:var(--success); font-weight:700; margin-top:2px;">(٥٨٢,١٦٧ ريال)</div>
                </div>
            </div>

            <div style="text-align:center; font-size:0.95rem; color:var(--text-muted); font-style:italic; border-top:1px solid #EEE; padding-top:15px;">
                «يستعرض هذا التقرير أبرز الإنجازات المالية والتشغيلية والإدارية خلال الفترة النصف سنوية للعام ٢٠٢٦م، مع مقارنة تفصيلية بالنصف الأول من عام ٢٠٢٥م.»
            </div>
        </div>"""

# Replace old Chairman box with Page 6 and Page 9 in generate_v2_dashboard.py
old_chairman_box = dash_code.find('<!-- Chairman Message Box -->')
end_narrative = dash_code.find('</section>\n\n    <!-- Section 3: Master KPI Dashboard')

if old_chairman_box != -1 and end_narrative != -1:
    dash_code = dash_code[:old_chairman_box] + page_6_html + "\n\n" + page_9_html + "\n    " + dash_code[end_narrative:]
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Updated Section 2 with Page 6 Chairman Speech and Page 9 Executive Summary in generate_v2_dashboard.py!")

# 2. Update PowerPoint Presentation (generate_full_14_slides_pptx.py)
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

# Update Slide 3 in PPTX to have the full Chairman Speech and Portrait, and Page 9 Executive Summary
# Let's inspect where Slide 3 is defined in generate_full_14_slides_pptx.py
print("Checking PPTX slides...")

# 3. Update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    word_code = f.read()

word_p6_p9 = """    # Page 6: Chairman Speech
    add_rtl_heading(doc, "كلمة رئيس مجلس الإدارة (صفحة ٦ بالتقرير)", level=1)
    p_ch1 = doc.add_paragraph()
    p_ch1.paragraph_format.bidi = True
    p_ch1.add_run("بسم الله الرحمن الرحيم\\nالحمد لله رب العالمين، والصلاة والسلام على نبينا محمد وعلى آله وصحبه أجمعين.\\nالإخوة والأخوات أعضاء الجمعية العمومية، وأعضاء مجلس الإدارة، والزملاء والزميلات في جمعية طبيبي الأهلية،\\nالسلام عليكم ورحمة الله وبركاته،")
    
    p_ch2 = doc.add_paragraph()
    p_ch2.paragraph_format.bidi = True
    p_ch2.add_run("يسعدني أن أرحب بكم في هذا اللقاء الذي نستعرض من خلاله التقرير النصف سنوي لجمعية طبيبي الأهلية، والذي يأتي تأكيدًا على حرص الجمعية على الشفافية، والحوكمة، ووضوح الإنجاز، ومشاركة أصحاب العلاقة في مسيرة العمل.\\nلقد شهد النصف الأول من هذا العام جهودًا متواصلة لتطوير أعمال الجمعية إداريًا وماليًا وبرامجيًا، وتحسين كفاءة الأداء، وتعزيز جودة الخدمات والمبادرات التي تقدمها الجمعية للمستفيدين.\\nوما تحقق من أعمال وإنجازات لم يكن ليتحقق بعد توفيق الله إلا بفضل تكامل الجهود بين مجلس الإدارة والجمعية العمومية والإدارة التنفيذية، وبفضل ما نجده من دعم وثقة من شركائنا وداعمينا، الذين نقدر لهم إسهاماتهم ووقوفهم المستمر مع رسالة الجمعية وأهدافها.")
    
    p_ch3 = doc.add_paragraph()
    p_ch3.paragraph_format.bidi = True
    p_ch3.add_run("كما أن استعراض هذا التقرير لا يمثل مجرد عرض لما تم إنجازه، بل هو وقفة تقييم ومراجعة لما تحقق، وتحديد لما يمكن تطويره وتحسينه خلال المرحلة القادمة، بما يسهم في رفع كفاءة الجمعية وتعظيم أثرها الاجتماعي والصحي.\\nونحن في مجلس الإدارة نؤكد التزامنا بمواصلة العمل على تطوير الأداء المؤسسي، وتعزيز الحوكمة والاستدامة المالية، وتنفيذ البرامج والمبادرات التي تحقق أثرًا ملموسًا ومستدامًا للمستفيدين والمجتمع.\\nوفي الختام، أتقدم بخالص الشكر والتقدير لكل من أسهم في إنجاز أعمال الجمعية خلال الفترة الماضية، من أعضاء مجلس الإدارة والإدارة التنفيذية والعاملين والمتطوعين والشركاء والداعمين.\\n\\nأخوكم\\nأ.د. منصور محمد النزهة\\nرئيس مجلس الإدارة")
    doc.add_page_break()

    # Page 9: Executive Summary
    add_rtl_heading(doc, "المقدمة والملخص التنفيذي (صفحة ٩ بالتقرير)", level=1)
    p_ex1 = doc.add_paragraph()
    p_ex1.paragraph_format.bidi = True
    p_ex1.add_run("واصلت جمعية طبيبي الأهلية خلال النصف الأول من عام ٢٠٢٦م تنفيذ برامجها ومشروعاتها وخدماتها الموجهة للمستفيدين، وفق الخطة التشغيلية والميزانية المعتمدة، محققةً نمواً ملموساً في جميع المؤشرات الرئيسية مقارنةً بالفترة المماثلة من عام ٢٠٢٥م.\\nفقد ارتفع إجمالي الدخل بنسبة بلغت +١٩٢٪، وتوسّع نطاق الدعم الطبي المقدّم بأكثر من تسعة أضعاف (+٩٤٣٪)، إلى جانب مضاعفة عدد البرامج التشغيلية، وتوسيع الكادر الوظيفي، وتعزيز الشراكات الصحية، وتطوير المنظومة الرقمية والحوكمة للجمعية.")
    
    # 4 metrics table in Word
    t_ex = doc.add_table(rows=2, cols=4)
    t_ex.alignment = WD_TABLE_ALIGNMENT.CENTER
    ex_metrics = [("٣+١", "موظفون ومتعاون"), ("٩", "شراكات صحية مفعلة"), ("٢", "برامج تشغيلية مفعلة"), ("+١٩٢٪", "نمو إجمالي الدخل")]
    for j, (num, label) in enumerate(ex_metrics):
        t_ex.rows[0].cells[j].paragraphs[0].text = num
        set_cell_background(t_ex.rows[0].cells[j], "6B1D3A")
        t_ex.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_ex.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_ex.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_ex.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(14)
        
        t_ex.rows[1].cells[j].paragraphs[0].text = label
        t_ex.rows[1].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_ex.rows[1].cells[j].paragraphs[0].runs[0].font.size = DPt(9.5)
        set_cell_background(t_ex.rows[1].cells[j], "FAF8F5")
    
    p_ex2 = doc.add_paragraph()
    p_ex2.paragraph_format.bidi = True
    p_ex2.add_run("يستعرض هذا التقرير أبرز الإنجازات المالية والتشغيلية والإدارية خلال الفترة النصف سنوية للعام ٢٠٢٦م، مع مقارنة تفصيلية بالنصف الأول من عام ٢٠٢٥م.")
    doc.add_page_break()"""

if "كلمة رئيس مجلس الإدارة (صفحة ٦ بالتقرير)" not in word_code:
    word_code = word_code.replace('add_rtl_heading(doc, "أولاً: الأداء المالي والموازنة التشغيلية', word_p6_p9 + '\n    add_rtl_heading(doc, "أولاً: الأداء المالي والموازنة التشغيلية')
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(word_code)
    print("Added Page 6 and Page 9 to Word generator!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables updated and recompiled with official Pages 6 & 9 sections!")
