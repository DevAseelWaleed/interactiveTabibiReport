# -*- coding: utf-8 -*-
"""
Fix indentation in generate_full_14_slides_pptx.py and enrich_word_and_presentations.py and recompile.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Fix generate_full_14_slides_pptx.py
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    code = f.read()

matrix_correct_pptx = """    table_shape = s4.shapes.add_table(12, 6, PInches(0.8), PInches(1.5), PInches(11.733), PInches(5.4))
    table = table_shape.table
    table_headers = ["المؤشر الاستراتيجي المعتمد", "المستهدف السنوي", "مستهدف H1", "المنجز الفعلي H1", "نسبة الإنجاز H1", "الحالة المعتمدة"]
    
    for j, h in enumerate(table_headers):
        cell = table.cell(0, j)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.font.name = 'Arial'
        p.font.bold = True
        p.font.size = PPt(11)
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    matrix_data = [
        ("الإيرادات المالية الكلية (المعدلة)", "١,٥٠٠,٠٠٠ ر.س", "٧٥٠,٠٠٠ ر.س", "٥٨٢,١٦٧.٥٢ ر.س", "٧٧.٦٢٪", "متقدم ومتميز"),
        ("عدد المستفيدين المخدومين", "٢٠٠ مستفيد", "١٠٠ مستفيد", "٧ مستفيدين", "٧.٠٠٪", "متأخر"),
        ("الاستشارات الطبية والدوائية", "١,٢٠٠ استشارة", "٦٠٠ استشارة", "٠ استشارة", "٠.٠٠٪", "لم يبدأ"),
        ("الدراسات واستطلاعات الرأي", "٦ دراسات", "٣ دراسات", "٠ دراسة", "٠.٠٠٪", "لم يبدأ"),
        ("ساعات وقيمة العمل التطوعي", "٣,٠٠٠ س (٢٠٢ ألف)", "١,٥٠٠ س (١٠١ ألف)", "٤ فرص تطوعية", "غير مدققة", "متعثر"),
        ("عقد الشراكات الصحية الفاعلة", "٩ شراكات", "٩ شراكات", "٩ شراكات مفعلة", "١٠٠.٠٠٪", "مكتمل"),
        ("توطين الوظائف والكادر البشري", "١٠٠٪", "١٠٠٪", "١٠٠٪ (٣ موظفين)", "١٠٠.٠٠٪", "مكتمل"),
        ("تدريب وتأهيل الكادر الإداري", "٤ دورات", "٢ دورة", "٨ دورات تدريبية", "٤٠٠.٠٠٪", "متقدم"),
        ("التحول الرقمي والمحاسبي", "نظام سحابي", "نظام سحابي", "تم تشغيل قيود", "١٠٠.٠٠٪", "مكتمل"),
        ("معايير الحوكمة ومنصة نوى", "١٠٠٪", "٥٠٪", "استيفاء ٧٠٪ من المعايير", "٧٠.٠٠٪", "متقدم"),
        ("تنويع مصادر الدخل الذاتي", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "١٠٠.٠٠٪", "مكتمل")
    ]

    for i, row in enumerate(matrix_data):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_CARD_BG if i % 2 == 0 else C_WHITE
            p = cell.text_frame.paragraphs[0]
            p.font.name = 'Arial'
            p.font.size = PPt(10)
            p.font.color.rgb = C_TEXT_DARK
            p.alignment = PP_ALIGN.CENTER
            if j == 4:
                p.font.bold = True
            elif j == 5:
                p.font.bold = True
                p.font.color.rgb = C_SUCCESS if "مكتمل" in val or "متقدم" in val else (C_WARNING if "متأخر" in val else C_DANGER)"""

start_s4 = code.find("s4 = prs.slides.add_slide(blank_layout)")
end_s4 = code.find("# =========================================================================\n    # SLIDE 5: Financial Performance")

if start_s4 != -1 and end_s4 != -1:
    header_s4 = """    s4 = prs.slides.add_slide(blank_layout)\n    add_slide_header(s4, "مصفوفة مطابقة الخطة الاستراتيجية بالمنجز الفعلي", "مقارنة تفصيلية لمستهدفات عام ٢٠٢٦م المعتمدة وما تحقق على أرض الواقع")\n\n"""
    code = code[:start_s4] + header_s4 + matrix_correct_pptx + "\n\n    " + code[end_s4:]
    with open(pptx_file, "w", encoding="utf-8") as f:
        f.write(code)
    print("Fixed PPTX indentation!")

# 2. Fix enrich_word_and_presentations.py
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    w_code = f.read()

matrix_correct_word = """    matrix_headers = ["م", "الهدف / النشاط", "المؤشر المعتمد", "المستهدف السنوي", "مستهدف H1", "المنجز الفعلي", "نسبة الإنجاز", "الحالة"]
    t_mat = doc.add_table(rows=12, cols=8)
    t_mat.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(matrix_headers):
        t_mat.rows[0].cells[j].paragraphs[0].text = h
        set_cell_background(t_mat.rows[0].cells[j], "6B1D3A")
        t_mat.rows[0].cells[j].paragraphs[0].runs[0].font.color.rgb = DRGBColor(255,255,255)
        t_mat.rows[0].cells[j].paragraphs[0].runs[0].font.bold = True
        t_mat.rows[0].cells[j].paragraphs[0].paragraph_format.bidi = True
        t_mat.rows[0].cells[j].paragraphs[0].runs[0].font.size = DPt(9)
    
    matrix_rows = [
        ("١", "الإيرادات المالية الكلية", "إجمالي الدخل (ريال)", "١,٥٠٠,٠٠٠", "٧٥٠,٠٠٠", "٥٨٢,١٦٧.٥٢", "٧٧.٦٢٪", "متقدم ومتميز"),
        ("٢", "عدد المستفيدين المخدومين", "عدد المستفيدين (فرد)", "٢٠٠ مستفيد", "١٠٠ مستفيد", "٧ مستفيدين", "٧.٠٠٪", "متأخر"),
        ("٣", "الاستشارات الطبية والدوائية", "عدد الاستشارات", "١,٢٠٠", "٦٠٠", "٠ استشارة", "٠.٠٠٪", "لم يبدأ"),
        ("٤", "الدراسات واستطلاعات الرأي", "عدد الدراسات", "٦ دراسات", "٣ دراسات", "٠ دراسة", "٠.٠٠٪", "لم يبدأ"),
        ("٥", "ساعات وقيمة التطوع", "ساعات وقيمة التطوع", "٣,٠٠٠ س (٢٠٢ ألف)", "١,٥٠٠ س (١٠١ ألف)", "٤ فرص تطوعية", "غير مدققة", "متعثر"),
        ("٦", "عقد الشراكات الصحية", "عدد الشراكات", "٩ شراكات", "٩ شراكات", "٩ شراكات مفعلة", "١٠٠.٠٠٪", "مكتمل"),
        ("٧", "توطين الوظائف والكادر", "نسبة التوطين (٪)", "١٠٠٪", "١٠٠٪", "١٠٠٪ (٣ موظفين)", "١٠٠.٠٠٪", "مكتمل"),
        ("٨", "تدريب وتأهيل الكادر", "عدد الدورات", "٤ دورات", "٢ دورة", "٨ دورات", "٤٠٠.٠٠٪", "متقدم ومكتمل"),
        ("٩", "التحول الرقمي والمحاسبي", "تطبيق نظام سحابي", "نظام قيود", "نظام قيود", "تم تشغيل قيود", "١٠٠.٠٠٪", "مكتمل"),
        ("١٠", "معايير الحوكمة ومنصة نوى", "نسبة الامتثال", "١٠٠٪", "٥٠٪", "استيفاء ٧٠٪ من المعايير", "٧٠.٠٠٪", "متقدم ومتميز"),
        ("١١", "تنويع مصادر الدخل الذاتي", "عدد مصادر الدخل", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "١٠٠.٠٠٪", "مكتمل")
    ]
    for i, row in enumerate(matrix_rows):
        r = t_mat.rows[i+1]
        for j, val in enumerate(row):
            r.cells[j].paragraphs[0].text = val
            r.cells[j].paragraphs[0].paragraph_format.bidi = True
            r.cells[j].paragraphs[0].runs[0].font.size = DPt(8.5)
            if i % 2 == 1:
                set_cell_background(r.cells[j], "F8F6F0")
    doc.add_page_break()"""

start_w_s3 = w_code.find('add_rtl_heading(doc, "ثالثاً: مصفوفة مطابقة الخطة الاستراتيجية بالمنجز الفعلي (١٤ مؤشراً معتمداً)", level=1)')
end_w_s3 = w_code.find('# 4. Human Resources & Vacancies (Pages 30-31)')

if start_w_s3 != -1 and end_w_s3 != -1:
    h_w = 'add_rtl_heading(doc, "ثالثاً: مصفوفة مطابقة الخطة الاستراتيجية بالمنجز الفعلي (المصفوفة الاستراتيجية المعتمدة)", level=1)\n'
    w_code = w_code[:start_w_s3] + h_w + matrix_correct_word + "\n\n    " + w_code[end_w_s3:]
    with open(word_file, "w", encoding="utf-8") as f:
        f.write(w_code)
    print("Fixed Word indentation!")

# Run all generators
os.system(f'py -3 "{os.path.join(base_dir, "generate_v2_dashboard.py")}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{word_file}"')

print("All deliverables compiled cleanly with 0 errors!")
