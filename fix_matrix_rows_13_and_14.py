# -*- coding: utf-8 -*-
"""
Fix Row 13 & Row 14 in Strategic Matrix Table:
1. Row 13 (معايير الحوكمة ومنصة نوى):
   - المستهدف السنوي: 100%
   - مستهدف H1: 50%
   - المنجز الفعلي: تحقيق 70.00% (منصة نوى ومعايير الحوكمة)
   - نسبة إنجاز H1: 70.00% (أو متقدم 140% من مستهدف النصف)
   - الحالة: متقدم ومتميز (bg-green)
   - الملاحظات: إنجاز 70% من معايير الحوكمة ومنصة نوى مع تكليف فريق استشاري
2. Row 14 (تنويع مصادر الدخل الذاتي):
   - المستهدف السنوي: 6 مصادر
   - مستهدف H1: 6 مصادر
   - المنجز الفعلي: 6 مصادر نشطة ومحققة
   - نسبة إنجاز H1: 100.00% (مكتمل)
   - الحالة: مكتمل (bg-green)
   - الملاحظات: تفعيل كافة قنوات الدخل الست المستهدفة بنجاح 100%
"""
import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")

with open(v2_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace row 13 and 14 in generate_v2_dashboard.py
old_rows = """                    <tr>
                        <td>١٣</td>
                        <td><strong>معايير الحوكمة ومنصة نوى</strong></td>
                        <td>نسبة الامتثال للحوكمة</td>
                        <td>١٠٠٪</td>
                        <td>٥٠٪</td>
                        <td>قيد الاستعانة باستشاري</td>
                        <td><span class="tag-pill tag-warning">٢٥.٠٠٪</span></td>
                        <td><span class="badge-pill bg-yellow">متأخر</span></td>
                        <td>طلب موازنة استشارية (١٥-٢١ ألف ر.س) لاستكمال الملف</td>
                    </tr>
                    <tr>
                        <td>١٤</td>
                        <td><strong>تنويع مصادر الدخل الذاتي</strong></td>
                        <td>عدد مصادر الدخل</td>
                        <td>٦ مصادر مستدامة</td>
                        <td>٦ مصادر</td>
                        <td>٦ مصادر نشطة</td>
                        <td><span class="tag-pill tag-warning">٦٦.٦٧٪</span></td>
                        <td><span class="badge-pill bg-yellow">قيد التنفيذ</span></td>
                        <td>المصادر مفعلة ولكن الدخل متركز بنسبة ٤٣٪ بمانح فرد</td>
                    </tr>"""

new_rows = """                    <tr>
                        <td>١٣</td>
                        <td><strong>معايير الحوكمة ومنصة نوى</strong></td>
                        <td>نسبة الامتثال للحوكمة</td>
                        <td>١٠٠٪</td>
                        <td>٥٠٪</td>
                        <td>تم تحقيق ٧٠.٠٠٪</td>
                        <td><span class="tag-pill tag-success">٧٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">متقدم ومتميز</span></td>
                        <td>إنجاز ٧٠٪ من متطلبات الحوكمة وتفعيل منصة نوى بنجاح</td>
                    </tr>
                    <tr>
                        <td>١٤</td>
                        <td><strong>تنويع مصادر الدخل الذاتي</strong></td>
                        <td>عدد مصادر الدخل</td>
                        <td>٦ مصادر مستدامة</td>
                        <td>٦ مصادر</td>
                        <td>٦ مصادر نشطة</td>
                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">مكتمل</span></td>
                        <td>تفعيل كافة مصادر الدخل الـ ٦ بنجاح (زكاة، علاج، متجر، تبرع، دعم عام، عضوية)</td>
                    </tr>"""

if old_rows in content:
    content = content.replace(old_rows, new_rows)
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated Rows 13 & 14 in generate_v2_dashboard.py!")
else:
    print("Pattern for old rows not found directly, searching flexible match...")
    start_r13 = content.find('<td>١٣</td>')
    end_r14 = content.find('</tbody>', start_r13)
    if start_r13 != -1 and end_r14 != -1:
        prefix = content[:start_r13-24] # back to <tr>
        suffix = content[end_r14:]
        content = prefix + new_rows + "\n                " + suffix
        with open(v2_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated Rows 13 & 14 with flexible replacement!")

# Also update Word Generator (enrich_word_and_presentations.py)
word_file = os.path.join(base_dir, "enrich_word_and_presentations.py")
with open(word_file, "r", encoding="utf-8") as f:
    w_code = f.read()

w_code = w_code.replace('("معايير الحوكمة ومنصة نوى", "١٠٠٪", "٥٠٪", "قيد الاستعانة باستشاري", "٢٥.٠٠٪", "متأخر")', '("معايير الحوكمة ومنصة نوى", "١٠٠٪", "٥٠٪", "تم تحقيق ٧٠٪", "٧٠.٠٠٪", "متقدم ومتميز")')
w_code = w_code.replace('("تنويع مصادر الدخل", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "٦٦.٦٧٪", "قيد التنفيذ")', '("تنويع مصادر الدخل", "٦ مصادر", "٦ مصادر", "٦ مصادر نشطة", "١٠٠.٠٠٪", "مكتمل")')

with open(word_file, "w", encoding="utf-8") as f:
    f.write(w_code)

# Recompile generator
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "build_bulletproof_standalone_dashboard.py")}"')
os.system(f'py -3 "{word_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_full_14_slides_pptx.py")}"')

print("All deliverables updated with corrected Rows 13 & 14!")
