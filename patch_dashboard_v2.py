# -*- coding: utf-8 -*-
import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")
v1_dir = os.path.join(base_dir, "التقرير_الجديد")

print("Executing comprehensive deliverables patch with verified strategic audit data...")

# =============================================================================
# 1. UPDATE generate_v2_dashboard.py
# =============================================================================
dashboard_path = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(dashboard_path, "r", encoding="utf-8") as f:
    dash_code = f.read()

# Update Nav links to include Strategic Audit
if '<li><a href="#strategic-audit">المطابقة الاستراتيجية</a></li>' not in dash_code:
    dash_code = dash_code.replace(
        '<li><a href="#kpi-dashboard">مؤشرات الأداء</a></li>',
        '<li><a href="#kpi-dashboard">مؤشرات الأداء</a></li>\n                <li><a href="#strategic-audit">المطابقة الاستراتيجية</a></li>'
    )

# Section 3.5 HTML definition
strategic_audit_section = """
    <!-- Section 3.5: Strategic Plan vs Actual Performance Audit Matrix -->
    <section class="container" id="strategic-audit" style="padding-top:20px; padding-bottom:40px;">
        <div class="section-intro">
            <span class="eyebrow-pill">التدقيق الأدائي والتقييم الاستراتيجي</span>
            <h2 class="section-headline">مصفوفة مطابقة الخطة الاستراتيجية بالمنجز الفعلي (٢٠٢٦م)</h2>
            <p class="section-subtext">مقارنة مدققة بين مستهدفات الخطة الاستراتيجية والتشغيلية وما تحقق فعلياً خلال النصف الأول وفق بطاقة الأداء المتوازن (BSC)</p>
        </div>

        <!-- BSC Strategic Perspectives Scorecards -->
        <div class="grid-4" style="margin-bottom:30px;">
            <div class="exec-card" style="border-right: 4px solid var(--danger);">
                <div style="font-size:0.85rem; color:var(--text-muted); font-weight:700; margin-bottom:6px;">محور الأثر والبرامج الطبية (٤٠٪)</div>
                <div style="font-size:1.8rem; font-weight:900; color:var(--danger); margin-bottom:6px;">١٣.٩٥٪</div>
                <div style="font-size:0.85rem; color:var(--text-muted);">٥.٥٨ من ٤٠ نقطة | خدمة ٧ مرضى فقط من ٣٦ ألف</div>
            </div>

            <div class="exec-card" style="border-right: 4px solid var(--warning);">
                <div style="font-size:0.85rem; color:var(--text-muted); font-weight:700; margin-bottom:6px;">المحور المالي والموازنة (٣٠٪)</div>
                <div style="font-size:1.8rem; font-weight:900; color:var(--warning); margin-bottom:6px;">٣٢.٩٦٪</div>
                <div style="font-size:0.85rem; color:var(--text-muted);">٩.٨٩ من ٣٠ نقطة | تحصيل ٥٨٢ ألف ر.س (+١٩٢٪ نمو)</div>
            </div>

            <div class="exec-card" style="border-right: 4px solid var(--info);">
                <div style="font-size:0.85rem; color:var(--text-muted); font-weight:700; margin-bottom:6px;">محور الشراكات والعمليات (١٥٪)</div>
                <div style="font-size:1.8rem; font-weight:900; color:var(--info); margin-bottom:6px;">٥٥.٠٠٪</div>
                <div style="font-size:0.85rem; color:var(--text-muted);">٨.٢٥ من ١٥ نقطة | ٩ شراكات مستشفيات فاعلة</div>
            </div>

            <div class="exec-card" style="border-right: 4px solid var(--success);">
                <div style="font-size:0.85rem; color:var(--text-muted); font-weight:700; margin-bottom:6px;">محور الحوكمة والمؤسسية (١٥٪)</div>
                <div style="font-size:1.8rem; font-weight:900; color:var(--success); margin-bottom:6px;">٦٠.٠٠٪</div>
                <div style="font-size:0.85rem; color:var(--text-muted);">٩.٠٠ من ١٥ نقطة | ١٠٠٪ توطين وتطبيق قيود</div>
            </div>
        </div>

        <!-- Overall Score Banner -->
        <div style="background:linear-gradient(135deg, #380B1B 0%, #541228 50%, #240713 100%); color:#FFF; padding:25px 30px; border-radius:var(--radius-lg); margin-bottom:35px; border:2px solid var(--secondary); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px;">
            <div>
                <span class="tag-pill" style="background:var(--secondary); color:#2E0B17; font-weight:800; margin-bottom:8px; display:inline-block;">التقييم العام المعتمد للأداء</span>
                <h3 style="color:#FFF; font-size:1.6rem; margin:0;">نسبة الإنجاز الاستراتيجي الإجمالية: <span style="color:var(--secondary-light); font-weight:900;">٣٢.٧٢٪</span></h3>
                <p style="margin:6px 0 0; opacity:0.85; font-size:0.95rem;">التقييم الموزون: <strong>يحتاج إلى تحسين جذري وإعادة ضبط مسار (Needs Significant Improvement & Realignment)</strong></p>
            </div>
            <div style="text-align:left;">
                <span style="font-size:0.9rem; opacity:0.8;">المنجز: ٤ مكتمل | ٢ قيد التنفيذ | ٤ متأخر | ٤ متعثر/لم يبدأ</span>
            </div>
        </div>

        <!-- Comprehensive Audit Matrix Table -->
        <div class="table-card" style="margin-bottom:35px;">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.3rem;"><i class="fas fa-scale-balanced" style="color:var(--secondary); margin-left:8px;"></i> جدول المطابقة الشاملة: مستهدفات الخطة الاستراتيجية مقابل المنجز الفعلي</h3>
                    <p style="font-size:0.9rem; color:var(--text-muted);">تحليل فني موثق بالأدلة لكافة المستهدفات الكمية والنوعية لعام ٢٠٢٦م</p>
                </div>
                <span class="tag-pill tag-info" style="font-size:0.9rem;">١٤ مؤشراً معتمداً</span>
            </div>

            <table class="custom-table">
                <thead>
                    <tr>
                        <th>م</th>
                        <th>الهدف / النشاط المخطط</th>
                        <th>المؤشر المعتمد</th>
                        <th>المستهدف السنوي</th>
                        <th>مستهدف H1</th>
                        <th>المنجز الفعلي</th>
                        <th>نسبة إنجاز H1</th>
                        <th>الحالة المعتمدة</th>
                        <th>الملاحظات الفنية ومصدر الدليل</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>١</td>
                        <td><strong>الإيرادات المالية الكلية</strong></td>
                        <td>إجمالي الدخل (ريال)</td>
                        <td>٦,٨٤٦,٠٠٠</td>
                        <td>٣,٤٢٣,٠٠٠</td>
                        <td>٥٨٢,١٦٧.٥٢</td>
                        <td><span class="tag-pill tag-danger">١٧.٠١٪</span></td>
                        <td><span class="badge-pill bg-red">متأخر حرِج</span></td>
                        <td>فجوة بين طموح الخطة والإيراد الفعلي (ص ١١)</td>
                    </tr>
                    <tr>
                        <td>٢</td>
                        <td><strong>إيرادات الموازنة التشغيلية</strong></td>
                        <td>إيراد الموازنة (ريال)</td>
                        <td>١,٥٢٧,٠٠٠</td>
                        <td>١,٥٢٧,٠٠٠</td>
                        <td>٥٨٢,١٦٧.٥٢</td>
                        <td><span class="tag-pill tag-warning">٣٨.١٢٪</span></td>
                        <td><span class="badge-pill bg-yellow">متأخر</span></td>
                        <td>تحقق ٣٨٪ من موازنة الدعم المقدرة للنصف الأول</td>
                    </tr>
                    <tr>
                        <td>٣</td>
                        <td><strong>المساعدات العلاجية المباشرة</strong></td>
                        <td>مبالغ المساعدات (ريال)</td>
                        <td>١,٥٠٠,٠٠٠</td>
                        <td>٧٥٠,٠٠٠</td>
                        <td>٢٠٨,٦٠٥.٠٠</td>
                        <td><span class="tag-pill tag-danger">٢٧.٨١٪</span></td>
                        <td><span class="badge-pill bg-red">متأخر حرِج</span></td>
                        <td>صرف ٢٨٪ فقط من مخصص المرضى بسبب تشدد اللائحة</td>
                    </tr>
                    <tr>
                        <td>٤</td>
                        <td><strong>عدد المستفيدين المخدومين</strong></td>
                        <td>عدد المستفيدين (فرد)</td>
                        <td>٣٦,٦٠٦</td>
                        <td>١٨,٣٠٣</td>
                        <td>٧ مستفيدين</td>
                        <td><span class="tag-pill tag-danger">٠.٠٣٨٪</span></td>
                        <td><span class="badge-pill bg-red">متعثر تماماً</span></td>
                        <td>خدمة ٧ مرضى فقط بدلاً من الآلاف المخطط لهم</td>
                    </tr>
                    <tr>
                        <td>٥</td>
                        <td><strong>الاستشارات الطبية والدوائية</strong></td>
                        <td>عدد الاستشارات</td>
                        <td>١,٢٠٠</td>
                        <td>٦٠٠</td>
                        <td>٠ استشارة</td>
                        <td><span class="tag-pill tag-danger">٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                        <td>برنامج الاستشارات الهاتفية لم يُفعل نهائياً</td>
                    </tr>
                    <tr>
                        <td>٦</td>
                        <td><strong>الدراسات واستطلاعات الرأي</strong></td>
                        <td>عدد الدراسات المنجزة</td>
                        <td>٦ دراسات</td>
                        <td>٣ دراسات</td>
                        <td>٠ دراسة</td>
                        <td><span class="tag-pill tag-danger">٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                        <td>لا توجد أي دراسة مسحية أو بحثية موثقة</td>
                    </tr>
                    <tr>
                        <td>٧</td>
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
                        <td>٨</td>
                        <td><strong>تفعيل محفظة البرامج الاستراتيجية</strong></td>
                        <td>عدد البرامج النشطة</td>
                        <td>١٠ برامج</td>
                        <td>١٠ برامج</td>
                        <td>برنامج واحد فقط</td>
                        <td><span class="tag-pill tag-danger">١٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-red">متعثر</span></td>
                        <td>تفعيل (جودة الحياة) وتعطيل ٩ برامج وقائية وتوعوية</td>
                    </tr>
                    <tr>
                        <td>٩</td>
                        <td><strong>عقد الشراكات الصحية الفاعلة</strong></td>
                        <td>عدد الشراكات</td>
                        <td>٩ شراكات</td>
                        <td>٩ شراكات</td>
                        <td>٩ شراكات مفعلة</td>
                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">مكتمل</span></td>
                        <td>إنجاز متميز بالتعاقد مع ٩ مستشفيات ومراكز كبرى</td>
                    </tr>
                    <tr>
                        <td>١٠</td>
                        <td><strong>توطين الوظائف والكادر البشري</strong></td>
                        <td>نسبة التوطين (٪)</td>
                        <td>١٠٠٪</td>
                        <td>١٠٠٪</td>
                        <td>١٠٠٪ (٣ موظفين)</td>
                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">مكتمل</span></td>
                        <td>التزام تام بمتطلبات السعودة الرسمية</td>
                    </tr>
                    <tr>
                        <td>١١</td>
                        <td><strong>تدريب وتأهيل الكادر الإداري</strong></td>
                        <td>عدد الدورات المنفذة</td>
                        <td>٤ دورات</td>
                        <td>٢ دورة</td>
                        <td>٨ دورات تدريبية</td>
                        <td><span class="tag-pill tag-success">٤٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">متقدم</span></td>
                        <td>تجاوز المستهدف بتقديم ٨ دورات للكوادر</td>
                    </tr>
                    <tr>
                        <td>١٢</td>
                        <td><strong>التحول الرقمي والمحاسبي</strong></td>
                        <td>تطبيق نظام سحابي</td>
                        <td>نظام سحابي</td>
                        <td>نظام سحابي</td>
                        <td>تم تشغيل نظام قيود</td>
                        <td><span class="tag-pill tag-success">١٠٠.٠٠٪</span></td>
                        <td><span class="badge-pill bg-green">مكتمل</span></td>
                        <td>تشغيل نظام قيود وإلغاء القيود الدفترية القديمة</td>
                    </tr>
                    <tr>
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
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- 10 Strategic Programs Portfolio Status Table -->
        <div class="table-card" style="margin-bottom:35px;">
            <h3 style="color:var(--primary); font-size:1.3rem; margin-bottom:15px;"><i class="fas fa-layer-group" style="color:var(--secondary); margin-left:8px;"></i> حالة محفظة البرامج الاستراتيجية الـ (١٠) المعتمدة في الخطة</h3>
            <table class="custom-table">
                <thead>
                    <tr>
                        <th>البرنامج المعتمد بالخطة</th>
                        <th>الهدف الاستراتيجي والمحتوى</th>
                        <th>الفئة المستهدفة</th>
                        <th>المنجز الفعلي بالنصف الأول</th>
                        <th>حالة التنفيذ</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>١. عيادتك</strong></td>
                        <td>عيادات استشارية بجميع التخصصات الطبية</td>
                        <td>فاقدو أهلية العلاج</td>
                        <td>لم تسجل أي عيادة ميدانية أو استشارية</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr>
                        <td><strong>٢. استشارات</strong></td>
                        <td>استشارات طبية هاتفية وعبر الواتساب</td>
                        <td>عموم المجتمع والمرضى</td>
                        <td>لم يتم تشغيل الخدمة الهاتفية</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr>
                        <td><strong>٣. علاج</strong></td>
                        <td>توفير الأدوية التخصصية والمزمنة للمحتاجين</td>
                        <td>المرضى المحتاجون للأدوية</td>
                        <td>لم يُسجل صرف مباشر لأدوية مستقلة</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr>
                        <td><strong>٤. وقف الحياة</strong></td>
                        <td>التعريف والحث على التبرع بالأعضاء</td>
                        <td>عموم المجتمع</td>
                        <td>لم تنفذ حملات وقفية متخصصة</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr>
                        <td><strong>٥. أطمئن</strong></td>
                        <td>فحوصات فورية للضغط والسكر والتهابات الكبد</td>
                        <td>عموم أفراد المجتمع</td>
                        <td>لم تنفذ قوافل فحص ميدانية</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr>
                        <td><strong>٦. حياة</strong></td>
                        <td>دعم وتمويل عمليات زراعة الأعضاء</td>
                        <td>مرضى الفشل العضوي</td>
                        <td>لم تسجل حالات زراعة أعضاء ممولة</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr>
                        <td><strong>٧. عون</strong></td>
                        <td>إعانات ومخصصات شهرية للأمراض المزمنة</td>
                        <td>المرضى المزمنون</td>
                        <td>لم تُصرف إعانات شهرية دورية</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr>
                        <td><strong>٨. ضيوفنا</strong></td>
                        <td>خدمات صحية لضيوف الرحمن بالحج والعمرة</td>
                        <td>الحجاج والمعتمرون</td>
                        <td>لم تُسجل مبادرات ميدانية بالمواسم</td>
                        <td><span class="badge-pill bg-red">لم يبدأ</span></td>
                    </tr>
                    <tr style="background:rgba(46, 125, 50, 0.06);">
                        <td><strong>٩. جودة الحياة</strong></td>
                        <td>تحمل تكاليف العمليات الجراحية بالمستشفيات</td>
                        <td>المرضى الأشد حاجة</td>
                        <td><strong>تم دعم ٧ حالات حرجة بمبلغ ٢٠٨,٦٠٥ ريال</strong></td>
                        <td><span class="badge-pill bg-green">مفعل ونشط (١٠٠٪)</span></td>
                    </tr>
                    <tr>
                        <td><strong>١٠. وعي</strong></td>
                        <td>نشر المعلومات التثقيفية والتوعوية بالأمراض</td>
                        <td>عموم المجتمع</td>
                        <td>اقتصر على منشورات عامة دون حملات مقاسة</td>
                        <td><span class="badge-pill bg-yellow">متأخر / جزئي</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Critical Gap Analysis Matrix -->
        <div class="grid-2">
            <div class="exec-card" style="border-top:4px solid var(--danger);">
                <h3 style="color:var(--danger); font-size:1.2rem; margin-bottom:12px;"><i class="fas fa-triangle-exclamation" style="margin-left:8px;"></i> الفجوة الاستراتيجية ١: انحسار نطاق المستفيدين</h3>
                <p style="font-size:0.95rem; line-height:1.8; color:var(--text-main); text-align:justify;">
                    الخطة استهدفت خدمة <strong>٣٦,٦٠٦ مستفيد</strong>، بينما اقتصر التنفيذ الفعلي على <strong>٧ مرضى فقط</strong>. يرجع ذلك لحصر الصرف في الجراحات المعقدة مرتفعة التكلفة (متوسط ٢٩.٨ ألف ريال للحالة) وإيقاف العيادات والقوافل الوقائية والاستشارات التي تخدم الآلاف بتكلفة منخفضة.
                </p>
            </div>

            <div class="exec-card" style="border-top:4px solid var(--warning);">
                <h3 style="color:var(--warning); font-size:1.2rem; margin-bottom:12px;"><i class="fas fa-user-xmark" style="margin-left:8px;"></i> الفجوة الاستراتيجية ٢: تشدد لائحة المساعدات العلاجية</h3>
                <p style="font-size:0.95rem; line-height:1.8; color:var(--text-main); text-align:justify;">
                    رُفضت <strong>١٤ حالة من أصل ٢١ متقدمة</strong> (نسبة رفض ٦٦.٧٪) معظمها بسبب انتهاء الإقامة النظامية أو نقص التقارير. نتج عن ذلك صرف ٢٠٨ ألف ريال فقط من موازنة المساعدات المعتمدة (٧٥٠ ألف ريال)، تاركة فائضاً علاجياً غير مستغل بأكثر من ٥٤١ ألف ريال.
                </p>
            </div>

            <div class="exec-card" style="border-top:4px solid var(--danger);">
                <h3 style="color:var(--danger); font-size:1.2rem; margin-bottom:12px;"><i class="fas fa-hand-holding-dollar" style="margin-left:8px;"></i> الفجوة الاستراتيجية ٣: مخاطر تركز الإيرادات والمنح</h3>
                <p style="font-size:0.95rem; line-height:1.8; color:var(--text-main); text-align:justify;">
                    يمثل تبرع واحد بمبلغ <strong>٢٥٠,٠٠٠ ريال ما نسبته ٤٣٪ من إجمالي الدخل</strong>. كما بلغت نسبة نجاح طلبات المنح ٧.٤٪ فقط (قبول منحتين من ٢٧ طلباً)، مع تراجع إيرادات منصة تبرع بنسبة -٩١٪، مما يؤكد الحاجة الملحة لتنويع قنوات الدخل المستدام.
                </p>
            </div>

            <div class="exec-card" style="border-top:4px solid var(--warning);">
                <h3 style="color:var(--warning); font-size:1.2rem; margin-bottom:12px;"><i class="fas fa-users-slash" style="margin-left:8px;"></i> الفجوة الاستراتيجية ٤: تراجع النشاط التطوعي المنظم</h3>
                <p style="font-size:0.95rem; line-height:1.8; color:var(--text-main); text-align:justify;">
                    استهدفت الخطة <strong>٣,٠٠٠ ساعة تطوعية بقيمة اقتصادية ٢٠٢,٥٠٠ ريال</strong>. الواقع سجل تنفيذ ٤ فرص تطوعية فقط دون توثيق للساعات أو قيمتها المالية (مقارنة بـ ١٠٨ فرص في عام ٢٠٢٥)، مما يتطلب إعادة هيكلة إدارة التطوع الصحي التخصصي.
                </p>
            </div>
        </div>
    </section>
"""

# Insert Section 3.5 right after section 3 ends
if 'id="strategic-audit"' not in dash_code:
    split_marker = '<!-- Section 4: Deep Financial Architecture -->'
    if split_marker in dash_code:
        dash_code = dash_code.replace(split_marker, strategic_audit_section + '\n\n    ' + split_marker)

# Write updated dashboard generator and run it
with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(dash_code)

print("Updated generate_v2_dashboard.py successfully.")
