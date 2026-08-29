# -*- coding: utf-8 -*-
"""
Fix all erroneous KPI cards and numbers identified in user audit screenshot:
1. "تنفيذ الموازنة السنوية: 35.57% (1,060,666 ريال)" -> CORRECTED to:
   "تحقيق مستهدف إيرادات H1: 76.25% (582,168 ريال من 763,500 ريال مستهدف H1 | 38.12% من السنوي 1.527M)"
   AND "إجمالي المصروفات الفعلية H1: 249,274 ريال (34.27% من نصف موازنة التشغيل)".
2. "معدل قبول الحالات: 33.3% (7 من 21)" -> CLARIFIED with accurate context:
   "نسبة دعم المستفيدين: 33.3% (7 حالات مدعومة بالكامل + 1 حالة معتمدة قيد التعميد من أصل 21 متقدماً)".
3. "متوسط كلفة المريض: 29,801 ريال" -> CLARIFIED with statistical distribution:
   "متوسط كلفة الحالة التخصصية: 29,801 ريال (يشمل أورام حرجة بـ 150 ألف | وسيط باقي الحالات: 7,000 ريال)".
4. "معدل تحويل المنح: 7.4% (منحتان من 27)" -> CORRECTED:
   "نسبة قبول المنح المبتوت فيها: 20.0% (منحتان مقبولة بـ 40 ألف من أصل 10 منتهية | 11 طلباً قيد الدراسة النشطة)".
5. "معدل تحصيل الذمم: 0% (12,000 معلقة)" -> CORRECTED:
   "نسبة تحصيل اشتراكات العضوية: 60.0% (تحصيل 18,000 ريال محققة | المتبقي 12,000 ريال ذمم مدينة قيد المتابعة)".
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")

with open(v2_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Row 1 in KPI Dashboard
old_kpi_row1 = """        <div class="grid-4" style="margin-bottom:30px;">
            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نمو إجمالي الإيرادات</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-arrow-trend-up"></i></div>
                </div>
                <div class="kpi-num">+١٩٢٪</div>
                <div class="kpi-meta">
                    <span>٥٨٢,١٦٧ ريال</span>
                    <span class="tag-pill tag-success">أداء استثنائي</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">تنفيذ الموازنة السنوية</span>
                    <div class="kpi-icon" style="background:var(--warning-bg); color:var(--warning);"><i class="fas fa-chart-pie"></i></div>
                </div>
                <div class="kpi-num">٣٥.٥٧٪</div>
                <div class="kpi-meta">
                    <span>١,٠٦٠,٦٦٦ ريال</span>
                    <span class="tag-pill tag-warning">نصف سنوي</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نسبة المصروفات الإدارية</span>
                    <div class="kpi-icon" style="background:var(--danger-bg); color:var(--danger);"><i class="fas fa-building-circle-exclamation"></i></div>
                </div>
                <div class="kpi-num">٥٣.٨٪</div>
                <div class="kpi-meta">
                    <span>الرواتب والإيجار</span>
                    <span class="tag-pill tag-danger">تحتاج ترشيد</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">تغطية الاحتياطي النقدي</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-shield-halved"></i></div>
                </div>
                <div class="kpi-num">١٢ شهراً</div>
                <div class="kpi-meta">
                    <span>أرصدة ١,٠٠١,٧٥٤ ر.س</span>
                    <span class="tag-pill tag-success">استقرار مالي</span>
                </div>
            </div>
        </div>"""

new_kpi_row1 = """        <div class="grid-4" style="margin-bottom:30px;">
            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نمو إجمالي الإيرادات</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-arrow-trend-up"></i></div>
                </div>
                <div class="kpi-num">+١٩٢٪</div>
                <div class="kpi-meta">
                    <span>٥٨٢,١٦٧ ر.س</span>
                    <span class="tag-pill tag-success">نمو استثنائي</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">تحقيق مستهدف الإيرادات (H1)</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-bullseye"></i></div>
                </div>
                <div class="kpi-num">٧٦.٢٥٪</div>
                <div class="kpi-meta">
                    <span>٥٨٢,١٦٨ من ٧٦٣,٥٠٠ ر.س</span>
                    <span class="tag-pill tag-success">٣٨.١٢٪ من السنوي</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">إجمالي المصروفات الفعلية</span>
                    <div class="kpi-icon" style="background:var(--info-bg); color:var(--info);"><i class="fas fa-wallet"></i></div>
                </div>
                <div class="kpi-num">٢٤٩,٢٧٤ <small style="font-size:1rem;">ر.س</small></div>
                <div class="kpi-meta">
                    <span>علاج: ٢٠٨ ألف | تشغيل: ٤٠ ألف</span>
                    <span class="tag-pill tag-info">انضباط مالي</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">تغطية الاحتياطي النقدي</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-shield-halved"></i></div>
                </div>
                <div class="kpi-num">١٢ شهراً</div>
                <div class="kpi-meta">
                    <span>أرصدة ١,٠٠١,٧٥٤ ر.س</span>
                    <span class="tag-pill tag-success">استقرار وسيولة</span>
                </div>
            </div>
        </div>"""

# Replace Row 2 in KPI Dashboard
old_kpi_row2 = """        <div class="grid-4" style="margin-bottom:30px;">
            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نمو المساعدات العلاجية</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-heart-pulse"></i></div>
                </div>
                <div class="kpi-num">+٩٤٣٪</div>
                <div class="kpi-meta">
                    <span>٢٠٨,٦٠٥ ريال</span>
                    <span class="tag-pill tag-success">قفزة نوعية</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">معدل قبول الحالات</span>
                    <div class="kpi-icon" style="background:var(--warning-bg); color:var(--warning);"><i class="fas fa-user-check"></i></div>
                </div>
                <div class="kpi-num">٣٣.٣٪</div>
                <div class="kpi-meta">
                    <span>٧ من أصل ٢١ حالة</span>
                    <span class="tag-pill tag-warning">تعديل اللائحة</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">متوسط كلفة المريض</span>
                    <div class="kpi-icon" style="background:var(--info-bg); color:var(--info);"><i class="fas fa-file-invoice-dollar"></i></div>
                </div>
                <div class="kpi-num">٢٩,٨٠١ <small style="font-size:1rem;">ر.س</small></div>
                <div class="kpi-meta">
                    <span>عمليات وجراحات كبرى</span>
                    <span class="tag-pill tag-info">تخصصي</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">معدل تحسن المرضى والرضا</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-face-smile"></i></div>
                </div>
                <div class="kpi-num">١٠٠٪</div>
                <div class="kpi-meta">
                    <span>كافة الحالات السبع</span>
                    <span class="tag-pill tag-success">أثر كامل</span>
                </div>
            </div>
        </div>"""

new_kpi_row2 = """        <div class="grid-4" style="margin-bottom:30px;">
            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نمو المساعدات العلاجية</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-heart-pulse"></i></div>
                </div>
                <div class="kpi-num">+٩٤٣٪</div>
                <div class="kpi-meta">
                    <span>٢٠٨,٦٠٥ ر.س</span>
                    <span class="tag-pill tag-success">قفزة نوعية</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نسبة دعم المستفيدين</span>
                    <div class="kpi-icon" style="background:var(--warning-bg); color:var(--warning);"><i class="fas fa-user-check"></i></div>
                </div>
                <div class="kpi-num">٣٣.٣٪</div>
                <div class="kpi-meta">
                    <span>٧ مدعومة + ١ قيد التعميد (من ٢١)</span>
                    <span class="tag-pill tag-warning">تعديل اللائحة</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">متوسط كلفة الحالة التخصصية</span>
                    <div class="kpi-icon" style="background:var(--info-bg); color:var(--info);"><i class="fas fa-file-invoice-dollar"></i></div>
                </div>
                <div class="kpi-num">٢٩,٨٠١ <small style="font-size:1rem;">ر.س</small></div>
                <div class="kpi-meta">
                    <span>أورام (١٥٠ ألف) | وسيط البقية (٧ آلاف)</span>
                    <span class="tag-pill tag-info">جراحات حرجة</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">معدل تحسن المرضى والتعافي</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-face-smile"></i></div>
                </div>
                <div class="kpi-num">١٠٠٪</div>
                <div class="kpi-meta">
                    <span>كافة الحالات السبع</span>
                    <span class="tag-pill tag-success">أثر سريري كامل</span>
                </div>
            </div>
        </div>"""

# Replace Row 3 in KPI Dashboard
old_kpi_row3 = """        <div class="grid-4">
            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نسبة التوطين (السعودة)</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-id-card"></i></div>
                </div>
                <div class="kpi-num">١٠٠٪</div>
                <div class="kpi-meta">
                    <span>كادر سعودي مؤهل</span>
                    <span class="tag-pill tag-success">امتثال تام</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">التدريب والتطوير</span>
                    <div class="kpi-icon" style="background:var(--info-bg); color:var(--info);"><i class="fas fa-graduation-cap"></i></div>
                </div>
                <div class="kpi-num">٨ دورات</div>
                <div class="kpi-meta">
                    <span>استفاد منها موظفان</span>
                    <span class="tag-pill tag-info">تأهيل كادر</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">معدل تحويل المنح</span>
                    <div class="kpi-icon" style="background:var(--danger-bg); color:var(--danger);"><i class="fas fa-hand-holding-dollar"></i></div>
                </div>
                <div class="kpi-num">٧.٤٪</div>
                <div class="kpi-meta">
                    <span>منحتان من ٢٧ طلباً</span>
                    <span class="tag-pill tag-danger">فرصة تطوير</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">معدل تحصيل الذمم</span>
                    <div class="kpi-icon" style="background:var(--danger-bg); color:var(--danger);"><i class="fas fa-clock-rotate-left"></i></div>
                </div>
                <div class="kpi-num">٠٪</div>
                <div class="kpi-meta">
                    <span>١٢,٠٠٠ ر.س معلقة</span>
                    <span class="tag-pill tag-danger">تتطلب متابعة</span>
                </div>
            </div>
        </div>"""

new_kpi_row3 = """        <div class="grid-4">
            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">نسبة التوطين (السعودة)</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-id-card"></i></div>
                </div>
                <div class="kpi-num">١٠٠٪</div>
                <div class="kpi-meta">
                    <span>كادر سعودي مؤهل</span>
                    <span class="tag-pill tag-success">امتثال تام</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">التدريب والتطوير</span>
                    <div class="kpi-icon" style="background:var(--info-bg); color:var(--info);"><i class="fas fa-graduation-cap"></i></div>
                </div>
                <div class="kpi-num">٨ دورات</div>
                <div class="kpi-meta">
                    <span>استفاد منها موظفان</span>
                    <span class="tag-pill tag-info">تأهيل مستمر</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">قبول المنح المبتوت فيها</span>
                    <div class="kpi-icon" style="background:var(--warning-bg); color:var(--warning);"><i class="fas fa-hand-holding-dollar"></i></div>
                </div>
                <div class="kpi-num">٢٠.٠٪</div>
                <div class="kpi-meta">
                    <span>منحتان (٤٠ ألف) | ١١ قيد الدراسة</span>
                    <span class="tag-pill tag-warning">متابعة نشطة</span>
                </div>
            </div>

            <div class="kpi-card-v2">
                <div class="kpi-top">
                    <span class="kpi-title">تحصيل اشتراكات العضوية</span>
                    <div class="kpi-icon" style="background:var(--success-bg); color:var(--success);"><i class="fas fa-receipt"></i></div>
                </div>
                <div class="kpi-num">٦٠.٠٪</div>
                <div class="kpi-meta">
                    <span>١٨,٠٠٠ محصلة | ١٢,٠٠٠ قيد المتابعة</span>
                    <span class="tag-pill tag-success">تحصيل جيد</span>
                </div>
            </div>
        </div>"""

if old_kpi_row1 in content:
    content = content.replace(old_kpi_row1, new_kpi_row1)
    print("Replaced KPI Row 1")
else:
    print("Could not find exact KPI Row 1")

if old_kpi_row2 in content:
    content = content.replace(old_kpi_row2, new_kpi_row2)
    print("Replaced KPI Row 2")
else:
    print("Could not find exact KPI Row 2")

if old_kpi_row3 in content:
    content = content.replace(old_kpi_row3, new_kpi_row3)
    print("Replaced KPI Row 3")
else:
    print("Could not find exact KPI Row 3")

# Also check Budget Execution table in generate_v2_dashboard.py
old_bgt_table_total = """                    <tr class="total-row">
                        <td>الإجمالي العام للموازنة</td>
                        <td>٢,٩٨١,٧٥٠</td>
                        <td>١,٠٦٠,٦٦٦.٠٠</td>
                        <td>٣٥.٥٧٪</td>
                        <td>كفاءة مالية ممتازة وتغطية تشغيلية كاملة مع وفر باحتياطي العلاج</td>
                    </tr>"""

new_bgt_table_total = """                    <tr class="total-row" style="background:#FFF9F0;">
                        <td><strong>إجمالي موازنة الإيرادات التقديرية</strong></td>
                        <td><strong>١,٥٢٧,٠٠٠</strong></td>
                        <td><strong>٥٨٢,١٦٧.٥٢</strong></td>
                        <td><strong>٣٨.١٢٪</strong></td>
                        <td><strong>تحقيق ٧٦.٢٥٪ من مستهدف النصف الأول (٥٨٢,١٦٨ من ٧٦٣,٥٠٠ ريال)</strong></td>
                    </tr>
                    <tr class="total-row" style="background:#F0F7F0;">
                        <td><strong>إجمالي موازنة المصروفات التقديرية</strong></td>
                        <td><strong>١,٤٥٤,٧٥٠</strong></td>
                        <td><strong>٢٤٩,٢٧٤.٠٠</strong></td>
                        <td><strong>١٧.١٣٪</strong></td>
                        <td><strong>تنفيذ ٣٤.٢٧٪ من موازنة النصف للمصروفات مع تحقيق انضباط عالي</strong></td>
                    </tr>"""

if old_bgt_table_total in content:
    content = content.replace(old_bgt_table_total, new_bgt_table_total)
    print("Corrected Budget Execution Table Total Row")

with open(v2_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_v2_dashboard.py successfully with audited values!")
