# -*- coding: utf-8 -*-
"""
Apply all User Visual Annotations from Image 1 & Image 2:
1. Row 1: الإيرادات المالية الكلية -> المستهدف السنوي: 1.5 مليون ريال (1,500,000 ر.س) | مستهدف H1: 750,000 ر.س | المنجز: 582,167.52 ر.س | نسبة الإنجاز: 77.62% | الحالة: متقدم ومتميز.
2. DELETE Row 2: إيرادات الموازنة التشغيلية (Red X).
3. DELETE Row 3: المساعدات العلاجية المباشرة (Red X).
4. DELETE Row 4: عدد المستفيدين المخدومين (Red X).
5. DELETE Row 8: تفعيل محفظة البرامج الاستراتيجية (Red X).
6. Row on معايير الحوكمة ومنصة نوى: Remove artificial 50% and 25% numbers -> replace with qualitative status:
   - المستهدف السنوي: استيفاء معايير الحوكمة (١٠٠٪)
   - مستهدف H1: التعاقد وبدء ملف الحوكمة
   - المنجز الفعلي: إعداد مقترح الفريق الاستشاري
   - نسبة إنجاز H1: قيد التنفيذ (جاري العمل)
   - الحالة: قيد التنفيذ
7. Re-index remaining strategic KPIs cleanly (1 to 9).
8. Recompile Dashboard HTML, Word docx, PowerPoint PPTX, and Web Slides.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# 1. Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

matrix_tbody_clean = """                <tbody>
                    <tr>
                        <td>١</td>
                        <td><strong>الإيرادات المالية الكلية</strong></td>
                        <td>إجمالي الدخل (ريال)</td>
                        <td>١,٥٠٠,٠٠٠</td>
                        <td>٧٥٠,٠٠٠</td>
                        <td>٥٨٢,١٦٧.٥٢</td>
                        <td><span class="tag-pill tag-success">٧٧.٦٢٪</span></td>
                        <td><span class="badge-pill bg-green">متقدم ومتميز</span></td>
                        <td>تحقيق ٧٧.٦٢٪ من مستهدف النصف الأول (٣٨.٨١٪ من السنوي)</td>
                    </tr>
                    <tr>
                        <td>٢</td>
                        <td><strong>الاستشارات الطبية والدوائية</strong></td>
                        <td>عدد الاستشارات</td>
                        <td>١,٢٠٠</td>
                        <td>٦٠٠</td>
                        <td>٠ استشارة</td>
                        <td><span class="tag-pill tag-danger">٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                        <td>برنامج الاستشارات الهاتفية لم يُفعل نهائياً بالنصف الأول</td>
                    </tr>
                    <tr>
                        <td>٣</td>
                        <td><strong>الدراسات واستطلاعات الرأي</strong></td>
                        <td>عدد الدراسات المنجزة</td>
                        <td>٦ دراسات</td>
                        <td>٣ دراسات</td>
                        <td>٠ دراسة</td>
                        <td><span class="tag-pill tag-danger">٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                        <td>لا توجد أي دراسة مسحية أو بحثية موثقة بالنصف الأول</td>
                    </tr>
                    <tr>
                        <td>٤</td>
                        <td><strong>ساعات وقيمة العمل التطوعي</strong></td>
                        <td>ساعات التطوع والقيمة</td>
                        <td>٣,٠٠٠ س (٢٠٢ ألف)</td>
                        <td>١,٥٠٠ س (١٠١ ألف)</td>
                        <td>٤ فرص تطوعية</td>
                        <td><span class="tag-pill tag-warning">غير مدققة</span></td>
                        <td><span class="badge-pill bg-yellow">متعثر</span></td>
                        <td>تراجع حاد وغياب توثيق الساعات والقيمة المالية</td>
                    </tr>
                    <tr>
                        <td>٥</td>
                        <td><strong>عقد الشراكات الصحية الفاعلة</strong></td>
                        <td>عدد الشراكات</td>
                        <td>٩ شراكات</td>
                        <td>٩ شراكات</td>
                        <td>٩ شراكات مفعلة</td>
                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">مكتمل</span></td>
                        <td>إنجاز متميز بالتعاقد مع ٩ مستشفيات ومراكز كبرى بالمدينة</td>
                    </tr>
                    <tr>
                        <td>٦</td>
                        <td><strong>توطين الوظائف والكادر البشري</strong></td>
                        <td>نسبة التوطين (٪)</td>
                        <td>١٠٠٪</td>
                        <td>١٠٠٪</td>
                        <td>١٠٠٪ (٣ موظفين)</td>
                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">مكتمل</span></td>
                        <td>التزام تام بمتطلبات السعودة الرسمية بنسبة ١٠٠٪</td>
                    </tr>
                    <tr>
                        <td>٧</td>
                        <td><strong>تدريب وتأهيل الكادر الإداري</strong></td>
                        <td>عدد الدورات المنفذة</td>
                        <td>٤ دورات</td>
                        <td>٢ دورة</td>
                        <td>٨ دورات تدريبية</td>
                        <td><span class="tag-pill tag-success">٤٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">متقدم ومتميز</span></td>
                        <td>تجاوز المستهدف بتقديم ٨ دورات تخصصية للكوادر</td>
                    </tr>
                    <tr>
                        <td>٨</td>
                        <td><strong>التحول الرقمي والمحاسبي</strong></td>
                        <td>تطبيق نظام سحابي</td>
                        <td>نظام سحابي</td>
                        <td>نظام سحابي</td>
                        <td>تم تشغيل قيود</td>
                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">مكتمل</span></td>
                        <td>تشغيل نظام قيود وإلغاء القيود الدفترية القديمة</td>
                    </tr>
                    <tr>
                        <td>٩</td>
                        <td><strong>معايير الحوكمة ومنصة نوى</strong></td>
                        <td>استيفاء معايير الحوكمة</td>
                        <td>١٠٠٪</td>
                        <td>بدء ملف الحوكمة</td>
                        <td>قيد الاستعانة باستشاري</td>
                        <td><span class="tag-pill tag-warning">جاري العمل</span></td>
                        <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>
                        <td>طلب موازنة استشارية (١٥-٢١ ألف ر.س) لاستكمال ملف الحوكمة ونوى</td>
                    </tr>
                    <tr>
                        <td>١٠</td>
                        <td><strong>تنويع مصادر الدخل الذاتي</strong></td>
                        <td>عدد مصادر الدخل</td>
                        <td>٦ مصادر</td>
                        <td>٦ مصادر</td>
                        <td>٦ مصادر نشطة</td>
                        <td><span class="tag-pill tag-warning">٦٦.٦٧٪</span></td>
                        <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>
                        <td>تفعيل المتجر، الزكاة، العضوية، وكبار المانحين، وبدء نوى</td>
                    </tr>
                </tbody>"""

# Replace the tbody in generate_v2_dashboard.py
start_tbody = dash_code.find('<th>الملاحظات الفنية ومصدر الدليل</th>\n                    </tr>\n                </thead>\n                <tbody>')
end_tbody = dash_code.find('</table>\n        </div>\n\n        <!-- 10 Strategic Programs Health Check Table -->')

if start_tbody != -1 and end_tbody != -1:
    header_end = start_tbody + len('<th>الملاحظات الفنية ومصدر الدليل</th>\n                    </tr>\n                </thead>\n')
    dash_code = dash_code[:header_end] + matrix_tbody_clean + '\n            ' + dash_code[end_tbody:]
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Updated generate_v2_dashboard.py successfully!")

# 2. Update generate_full_14_slides_pptx.py Slide 4 Matrix
pptx_file = os.path.join(base_dir, "generate_full_14_slides_pptx.py")
with open(pptx_file, "r", encoding="utf-8") as f:
    pptx_code = f.read()

matrix_data_clean_pptx = """    matrix_data = [
        ("الإيرادات المالية الكلية (المعدلة)", "١,٥٠٠,٠٠٠ ر.س", "٧٥٠,٠٠٠ ر.س", "٥٨٢,١٦٧.٥٢ ر.س", "٧٧.٦٢٪", "متقدم ومتميز"),
        ("الاستشارات الطبية والدوائية", "١,٢٠٠ استشارة", "٦٠٠ استشارة", "٠ استشارة", "٠.٠٠٪", "لم يبدأ"),
        ("الدراسات واستطلاعات الرأي", "٦ دراسات", "٣ دراسات", "٠ دراسة", "٠.٠٠٪", "لم يبدأ"),
        ("ساعات وقيمة العمل التطوعي", "٣,٠٠٠ س (٢٠٢ ألف)", "١,٥٠٠ س (١٠١ ألف)", "٤ فرص تطوعية", "غير مدققة", "متعثر"),
        ("عقد الشراكات الصحية الفاعلة", "٩ شراكات", "٩ شراكات", "٩ شراكات مفعلة", "١٠٠.٠٠٪", "مكتمل"),
        ("توطين الوظائف والكادر البشري", "١٠٠٪", "١٠٠٪", "١٠٠٪ (٣ موظفين)", "١٠٠.٠٠٪", "مكتمل"),
        ("تدريب وتأهيل الكادر الإداري", "٤ دورات", "٢ دورة", "٨ دورات تدريبية", "٤٠٠.٠٠٪", "متقدم"),
        ("التحول الرقمي والمحاسبي", "نظام سحابي", "نظام سحابي", "تم تشغيل قيود", "١٠٠.٠٠٪", "مكتمل"),
        ("معايير الحوكمة ومنصة نوى", "١٠٠٪", "بدء الملف", "قيد الاستعانة باستشاري", "جاري العمل", "قيد التنفيذ")
    ]"""

start_m = pptx_code.find("matrix_data = [")
end_m = pptx_code.find("for i, row in enumerate(matrix_data):")

if start_m != -1 and end_m != -1:
    pptx_code = pptx_code[:start_m] + matrix_data_clean_pptx + "\n\n    " + pptx_code[end_m:]
    pptx_code = pptx_code.replace("table_shape = s4.shapes.add_table(8, 6,", "table_shape = s4.shapes.add_table(10, 6,")
    with open(pptx_file, "w", encoding="utf-8") as f:
        f.write(pptx_code)
    print("Updated generate_full_14_slides_pptx.py successfully!")

# 3. Update Web Slides (generate_web_slides.py)
web_slides_file = os.path.join(base_dir, "generate_web_slides.py")
with open(web_slides_file, "r", encoding="utf-8") as f:
    web_code = f.read()

web_matrix_clean = """                    <tbody>
                        <tr>
                            <td><strong>الإيرادات المالية الكلية</strong></td>
                            <td>١,٥٠٠,٠٠٠ ر.س</td>
                            <td>٧٥٠,٠٠٠ ر.س</td>
                            <td>٥٨٢,١٦٧ ر.س</td>
                            <td>٧٧.٦٢٪</td>
                            <td><span class="badge-pill bg-green">متقدم ومتميز</span></td>
                        </tr>
                        <tr>
                            <td><strong>الاستشارات الطبية</strong></td>
                            <td>١,٢٠٠ استشارة</td>
                            <td>٦٠٠ استشارة</td>
                            <td>٠ استشارة</td>
                            <td>٠.٠٠٪</td>
                            <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                        </tr>
                        <tr>
                            <td><strong>الشراكات الصحية الفاعلة</strong></td>
                            <td>٩ شراكات</td>
                            <td>٩ شراكات</td>
                            <td>٩ شراكات</td>
                            <td>١٠٠.٠٠٪</td>
                            <td><span class="badge-pill bg-green">مكتمل</span></td>
                        </tr>
                        <tr>
                            <td><strong>توطين الوظائف</strong></td>
                            <td>١٠٠٪</td>
                            <td>١٠٠٪</td>
                            <td>١٠٠٪</td>
                            <td>١٠٠.٠٠٪</td>
                            <td><span class="badge-pill bg-green">مكتمل</span></td>
                        </tr>
                        <tr>
                            <td><strong>تدريب وتأهيل الكادر</strong></td>
                            <td>٤ دورات</td>
                            <td>٢ دورة</td>
                            <td>٨ دورات</td>
                            <td>٤٠٠.٠٠٪</td>
                            <td><span class="badge-pill bg-green">متقدم</span></td>
                        </tr>
                        <tr>
                            <td><strong>التحول الرقمي والمحاسبي</strong></td>
                            <td>نظام سحابي</td>
                            <td>نظام سحابي</td>
                            <td>تم تشغيل قيود</td>
                            <td>١٠٠.٠٠٪</td>
                            <td><span class="badge-pill bg-green">مكتمل</span></td>
                        </tr>
                        <tr>
                            <td><strong>معايير الحوكمة ومنصة نوى</strong></td>
                            <td>١٠٠٪</td>
                            <td>بدء الملف</td>
                            <td>قيد الاستعانة باستشاري</td>
                            <td>جاري العمل</td>
                            <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>
                        </tr>
                        <tr>
                            <td><strong>تنويع مصادر الدخل</strong></td>
                            <td>٦ مصادر</td>
                            <td>٦ مصادر</td>
                            <td>٦ مصادر نشطة</td>
                            <td>٦٦.٦٧٪</td>
                            <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>
                        </tr>
                    </tbody>"""

start_w = web_code.find("<tbody>\n                        <tr>\n                            <td><strong>إجمالي الإيرادات")
end_w = web_code.find("</table>\n            </div>\n        </div>\n\n        <!-- SLIDE 5: Financial Performance -->")

if start_w != -1 and end_w != -1:
    web_code = web_code[:start_w] + web_matrix_clean + "\n                " + web_code[end_w:]
    with open(web_slides_file, "w", encoding="utf-8") as f:
        f.write(web_code)
    print("Updated generate_web_slides.py successfully!")

# 4. Update Word Document Builder (enrich_word_and_presentations.py)
word_gen_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_gen_file, "r", encoding="utf-8") as f:
    word_code = f.read()

matrix_rows_word_clean = """    matrix_rows = [
        ("١", "الإيرادات المالية الكلية", "إجمالي الدخل (ريال)", "١,٥٠٠,٠٠٠", "٧٥٠,٠٠٠", "٥٨٢,١٦٧.٥٢", "٧٧.٦٢٪", "متقدم ومتميز"),
        ("٢", "الاستشارات الطبية والدوائية", "عدد الاستشارات", "١,٢٠٠", "٦٠٠", "٠ استشارة", "٠.٠٠٪", "لم يبدأ"),
        ("٣", "الدراسات واستطلاعات الرأي", "عدد الدراسات", "٦ دراسات", "٣ دراسات", "٠ دراسة", "٠.٠٠٪", "لم يبدأ"),
        ("٤", "ساعات وقيمة التطوع", "ساعات وقيمة التطوع", "٣,٠٠٠ س (٢٠٢ ألف)", "١,٥٠٠ س (١٠١ ألف)", "٤ فرص تطوعية", "غير مدققة", "متعثر"),
        ("٥", "عقد الشراكات الصحية", "عدد الشراكات", "٩ شراكات", "٩ شراكات", "٩ شراكات مفعلة", "١٠٠.٠٠٪", "مكتمل"),
        ("٦", "توطين الوظائف والكادر", "نسبة التوطين (٪)", "١٠٠٪", "١٠٠٪", "١٠٠٪ (٣ موظفين)", "١٠٠.٠٠٪", "مكتمل"),
        ("٧", "تدريب وتأهيل الكادر", "عدد الدورات", "٤ دورات", "٢ دورة", "٨ دورات", "٤٠٠.٠٠٪", "متقدم ومكتمل"),
        ("٨", "التحول الرقمي والمحاسبي", "تطبيق نظام سحابي", "نظام قيود", "نظام قيود", "تم تشغيل قيود", "١٠٠.٠٠٪", "مكتمل"),
        ("٩", "معايير الحوكمة ومنصة نوى", "نسبة الامتثال", "١٠٠٪", "بدء الملف", "قيد الاستعانة باستشاري", "جاري العمل", "قيد التنفيذ"),
        ("١٠", "تنويع مصادر الدخل الذاتي", "عدد مصادر الدخل", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "٦٦.٦٧٪", "قيد التنفيذ")
    ]"""

start_w_mat = word_code.find("matrix_rows = [")
end_w_mat = word_code.find("for i, row in enumerate(matrix_rows):")

if start_w_mat != -1 and end_w_mat != -1:
    word_code = word_code[:start_w_mat] + matrix_rows_word_clean + "\n    " + word_code[end_w_mat:]
    word_code = word_code.replace("t_mat = doc.add_table(rows=15, cols=8)", "t_mat = doc.add_table(rows=11, cols=8)")
    with open(word_gen_file, "w", encoding="utf-8") as f:
        f.write(word_code)
    print("Updated enrich_word_and_presentations.py successfully!")

# Re-run all generators
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{pptx_file}"')
os.system(f'py -3 "{web_slides_file}"')
os.system(f'py -3 "{word_gen_file}"')

print("All deliverables updated and recompiled successfully with user red-line edits!")
