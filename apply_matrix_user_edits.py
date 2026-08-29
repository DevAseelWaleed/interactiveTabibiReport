# -*- coding: utf-8 -*-
"""
Apply User's Visual Red-Line Edits on Strategic Matrix Table:
1. Row 1: Annual Target -> 1.5 M (1,500,000 SAR), H1 Target -> 750,000 SAR, Actual -> 582,167.52 SAR (77.62% / 38.81% annual), Status -> متقدم ومتميز.
2. DELETE Row 2: إيرادات الموازنة التشغيلية (Red X).
3. DELETE Row 3: المساعدات العلاجية المباشرة (Red X).
4. DELETE Row 4: عدد المستفيدين المخدومين (Red X).
5. DELETE Row 8: تفعيل محفظة البرامج الاستراتيجية (Red X).
6. Cleanly re-index the remaining 10 strategic KPIs (1 to 10).
7. Recompile all deliverables: Dashboard HTML, Word docx, PPTX 14-slide deck, and Web slides.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")

with open(v2_file, "r", encoding="utf-8") as f:
    content = f.read()

# Define the new, clean 10-indicator Strategic Matrix HTML Table
new_matrix_tbody = """                <tbody>
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
                        <td>نسبة الامتثال للحوكمة</td>
                        <td>١٠٠٪</td>
                        <td>٥٠٪</td>
                        <td>قيد الاستعانة باستشاري</td>
                        <td><span class="tag-pill tag-warning">٢٥.٠٠٪</span></td>
                        <td><span class="badge-pill bg-yellow">متأخر</span></td>
                        <td>طلب موازنة استشارية (١٥-٢١ ألف) لإنهاء معايير الحوكمة</td>
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

# Find tbody in table-card of Section 3.5 in generate_v2_dashboard.py
start_marker = '<table class="custom-table">\n                <thead>\n                    <tr>\n                        <th>م</th>\n                        <th>الهدف / النشاط المخطط</th>\n                        <th>المؤشر المعتمد</th>\n                        <th>المستهدف السنوي</th>\n                        <th>مستهدف H1</th>\n                        <th>المنجز الفعلي</th>\n                        <th>نسبة إنجاز H1</th>\n                        <th>الحالة المعتمدة</th>\n                        <th>الملاحظات الفنية ومصدر الدليل</th>\n                    </tr>\n                </thead>\n                <tbody>'
end_marker = '</table>\n        </div>\n\n        <!-- 10 Strategic Programs Health Check Table -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    header_part = content[start_idx:start_idx + len(start_marker)]
    content = content[:start_idx + len(start_marker) - len('<tbody>')] + new_matrix_tbody + '\n            ' + content[end_idx:]
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated generate_v2_dashboard.py with clean 10-indicator matrix table!")
else:
    print("Could not find exact matrix table markers in generate_v2_dashboard.py")

