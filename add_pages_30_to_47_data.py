# -*- coding: utf-8 -*-
"""
Inject all comprehensive content from Pages 30 to 47 of the original report into generate_v2_dashboard.py:
1. Pages 30-31: Human Resources & Vacancies (4 Staff + 3 Vacancies Pipeline)
2. Pages 32-33: Administrative & Financial Achievements (12 Major Achievements + HQ Relocation 25k Savings)
3. Pages 34-35: Resource Development & Grants (27 applied, 2 accepted, 11 under review, Ihsan pipeline, 8 declinations & 3 recommendations)
4. Pages 36-39: Strategic Aspirations, Advisory Team Proposal, 6 Justifications, 3-Phase Roadmap, 6 Control Guarantees, 8 Initiatives (including Tabibi Card)
5. Pages 40-42: Beneficiary Experiences & Verbatim Thank-You Letters (Samia Suleiman & Kandafa Mohammed)
6. Pages 43-45: Supervisory Bodies, Government Partners, Platforms & Key Donors/Endowments
7. Pages 46-47: Executive Management Closing Message & Official Contacts
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")

with open(v2_file, "r", encoding="utf-8") as f:
    content = f.read()

# Let's define the new rich HTML block for sections 5 through 10 from pages 30 to 47
pages_30_47_html = """
    <!-- ========================================================================= -->
    <!-- SECTION 5: Human Resources & Vacancy Pipeline (Pages 30-31) -->
    <!-- ========================================================================= -->
    <section class="container" id="human-resources" style="padding-top:50px;">
        <div class="section-intro">
            <span class="eyebrow-pill">رأس المال البشري</span>
            <h2 class="section-headline">الكادر الوظيفي وخطة سد الاحتياج (ص ٣٠-٣١)</h2>
            <p class="section-subtext">فريق العمل التنفيذي القائم بنسبة توطين ١٠٠٪، وحصر الشواغر الأساسية لدعم الهيكل الإداري</p>
        </div>

        <div class="grid-4" style="margin-bottom:30px;">
            <div class="exec-card" style="text-align:center; border-top:4px solid var(--primary);">
                <div style="width:60px; height:60px; border-radius:50%; background:rgba(107,29,58,0.1); color:var(--primary); display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.5rem; font-weight:800;">ب</div>
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:4px;">أ. بيان سعد المحمدي</h4>
                <div style="font-weight:700; color:var(--secondary-dark); font-size:0.9rem; margin-bottom:8px;">المدير التنفيذي</div>
                <span class="tag-pill tag-success">موظف رسمي (١٠٠٪ توطين)</span>
            </div>

            <div class="exec-card" style="text-align:center; border-top:4px solid var(--primary);">
                <div style="width:60px; height:60px; border-radius:50%; background:rgba(107,29,58,0.1); color:var(--primary); display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.5rem; font-weight:800;">غ</div>
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:4px;">أ. غدير أحمد الحربي</h4>
                <div style="font-weight:700; color:var(--secondary-dark); font-size:0.9rem; margin-bottom:8px;">المسؤول المالي والمشرفة على البرامج</div>
                <span class="tag-pill tag-success">موظفة رسمية (١٠٠٪ توطين)</span>
            </div>

            <div class="exec-card" style="text-align:center; border-top:4px solid var(--primary);">
                <div style="width:60px; height:60px; border-radius:50%; background:rgba(107,29,58,0.1); color:var(--primary); display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.5rem; font-weight:800;">ط</div>
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:4px;">أ. طراد محمد سمان</h4>
                <div style="font-weight:700; color:var(--secondary-dark); font-size:0.9rem; margin-bottom:8px;">سكرتير تنفيذي</div>
                <span class="tag-pill tag-success">موظف رسمي (١٠٠٪ توطين)</span>
            </div>

            <div class="exec-card" style="text-align:center; border-top:4px solid var(--secondary);">
                <div style="width:60px; height:60px; border-radius:50%; background:rgba(201,169,110,0.15); color:var(--secondary-dark); display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:1.5rem; font-weight:800;">م</div>
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:4px;">أ. محمد الحسن بشير</h4>
                <div style="font-weight:700; color:var(--secondary-dark); font-size:0.9rem; margin-bottom:8px;">محاسب قانوني متعاون</div>
                <span class="tag-pill tag-warning">كادر متعاون تخصصي</span>
            </div>
        </div>

        <!-- Vacancies Table -->
        <div class="table-card">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.3rem;"><i class="fas fa-user-plus" style="color:var(--secondary); margin-left:8px;"></i> خطة الشواغر والاحتياج الوظيفي (٣ وظائف أساسية)</h3>
                    <p style="font-size:0.9rem; color:var(--text-muted);">تعمل الإدارة التنفيذية على استقطاب وتعيين الكفاءات المؤهلة لتشغيل الهيكل التنظيمي المعتمد</p>
                </div>
            </div>
            <table class="custom-table">
                <thead>
                    <tr>
                        <th>المسمى الوظيفي</th>
                        <th>الحالة الراهنة</th>
                        <th>المرشح / الإجراء التنفيذي</th>
                        <th>الأهمية والأثر التشغيلي</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>موظف/ـة علاقات عامة وإعلام</strong></td>
                        <td><span class="badge-pill bg-yellow">قيد الترسيم</span></td>
                        <td>تم ترشيح <strong>أ. فيصل الجهني</strong> (يعمل منذ ٣ أشهر كمتعاون بدون أجر لحين الترسيم)</td>
                        <td>إدارة المنصات الرقمية وصناعة المحتوى والظهور الإعلامي والشراكات</td>
                    </tr>
                    <tr>
                        <td><strong>موظف/ـة تنمية موارد مالية</strong></td>
                        <td><span class="badge-pill bg-red">شاغرة (تحتاج استقطاب)</span></td>
                        <td>استقطاب كفاءة متخصصة في كتابة المشاريع والمنح والتواصل مع المانحين</td>
                        <td>رفع كفاءة الاستدامة المالية وتوسيع قاعدة المانحين والأوقاف</td>
                    </tr>
                    <tr>
                        <td><strong>موظف/ـة موارد بشرية</strong></td>
                        <td><span class="badge-pill bg-red">شاغرة (تحتاج استقطاب)</span></td>
                        <td>وظيفة أساسية لدعم الهيكل الإداري وتنظيم شؤون الموظفين والتدريب</td>
                        <td>متابعة لوائح العمل والتوطين وبناء ملفات التطوع والتدريب</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SECTION 6: Administrative & Financial Achievements & HQ (Pages 32-33) -->
    <!-- ========================================================================= -->
    <section class="container" id="admin-achievements" style="padding-top:50px;">
        <div class="section-intro">
            <span class="eyebrow-pill">البناء والترشيد المؤسسي</span>
            <h2 class="section-headline">الإنجازات الإدارية والمالية الـ (١٢) والانتقال للمقر الجديد (ص ٣٢-٣٣)</h2>
            <p class="section-subtext">حزمة التحسينات الهيكلية التي أسهمت في ضبط العمليات وخفض التكاليف التشغيلية</p>
        </div>

        <!-- Relocation Spotlight Banner -->
        <div class="exec-card" style="background:linear-gradient(135deg, #FFFDF9 0%, #F5EFEB 100%); border:2px solid var(--secondary); margin-bottom:30px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px;">
            <div style="max-width:800px;">
                <span class="tag-pill tag-success" style="font-size:0.95rem; margin-bottom:8px;"><i class="fas fa-building" style="margin-left:6px;"></i> الانتقال للمقر الجديد وترشيد النفقات</span>
                <h3 style="color:var(--primary); font-size:1.4rem; margin-bottom:8px;">وفر مالي سنوي قدره ٢٥,٠٠٠ ريال سعودي</h3>
                <p style="font-size:0.95rem; line-height:1.8; color:var(--text-main); text-align:justify;">
                    تم الانتقال من المقر السابق إلى المقر الحالي بإيجار سنوي قدره <strong>٤٥,٠٠٠ ريال</strong> (بدعم مباشر من نائب رئيس مجلس الإدارة)، مقارنة بالمقر السابق الذي بلغت قيمته الإيجارية السنوية <strong>٧٠,٠٠٠ ريال</strong>، مما خفض الأعباء الإدارية وعزز الكفاءة المالية للجمعية.
                </p>
            </div>
            <div style="text-align:center; background:var(--primary); color:#FFF; padding:18px 28px; border-radius:var(--radius-md); box-shadow:0 6px 16px rgba(107,29,58,0.2);">
                <div style="font-size:2rem; font-weight:900; color:var(--secondary-light);">٤٥,٠٠٠ ر.س</div>
                <div style="font-size:0.85rem; opacity:0.9;">الإيجار السنوي الجديد (بدلاً من ٧٠ ألف)</div>
            </div>
        </div>

        <!-- 12 Achievements Grid -->
        <div class="grid-3" style="margin-bottom:30px;">
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ١. أتمتة العمل بنظام «قيود»</h4><p style="font-size:0.9rem; color:var(--text-muted);">إدخال برنامج قيود السحابي المجاز رسمياً من المركز الوطني لتنمية القطاع غير الربحي.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٢. بناء الشجرة المحاسبية</h4><p style="font-size:0.9rem; color:var(--text-muted);">تأسيس دليل الحسابات وفق الدليل المحاسبي المعتمد الموحد للجمعيات الخيرية بالمملكة.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٣. إقفال حسابات عام ٢٠٢٥م</h4><p style="font-size:0.9rem; color:var(--text-muted);">إقفال الأرباع السنوية لعام ٢٠٢٥م بكفاءة وموثوقية وتدقيق متطلبات المحاسب القانوني.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٤. الموازنة التقديرية ٢٠٢٦م</h4><p style="font-size:0.9rem; color:var(--text-muted);">إعداد الموازنة واعتمادها رسمياً من قبل مجلس الإدارة والجمعية العمومية.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٥. جرد وحصر الأصول الفعلي</h4><p style="font-size:0.9rem; color:var(--text-muted);">تنفيذ جرد مالي شامل من الواقع لكافة أصول الجمعية وتوثيقها رسمياً بالسجلات.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٦. اعتماد القوائم المالية</h4><p style="font-size:0.9rem; color:var(--text-muted);">إعداد القوائم المالية واعتمادها من المركز الوطني للقطاع غير الربحي.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٧. الأرشفة الورقية والإلكترونية</h4><p style="font-size:0.9rem; color:var(--text-muted);">أرشفة جميع مستندات وملفات الجمعية رقمياً وورقياً بصورة مؤسسية حديثة.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٨. نظام الاتصالات الإدارية</h4><p style="font-size:0.9rem; color:var(--text-muted);">إنشاء نظام الصادر والوارد وتوثيق كافة المخاطبات والمعاملات الرسمية منذ بداية ٢٠٢٦م.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ٩. تطوير الموقع الإلكتروني</h4><p style="font-size:0.9rem; color:var(--text-muted);">تحديث البوابة الإلكترونية لتتوافق مع متطلبات الحوكمة والمركز الوطني وحفظ الخصوصية.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ١٠. تطوير السياسات الداخلية</h4><p style="font-size:0.9rem; color:var(--text-muted);">صياغة اللوائح والسياسات الداخلية ونشرها على الموقع الرسمي لتعزيز الشفافية.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--warning);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-hourglass-half" style="color:var(--warning); margin-left:6px;"></i> ١١. متابعة الامتثال والحوكمة</h4><p style="font-size:0.9rem; color:var(--text-muted);">استمرار العمل التنفيذي لاستيفاء معايير الحوكمة الشاملة ورفع تصنيف الجمعية.</p></div>
            <div class="exec-card" style="border-right:4px solid var(--success);"><h4 style="color:var(--primary); margin-bottom:6px;"><i class="fas fa-check-circle" style="color:var(--success); margin-left:6px;"></i> ١٢. إعادة هيكلة اللجان</h4><p style="font-size:0.9rem; color:var(--text-muted);">حل اللجان السابقة وترشيق العمل بالاكتفاء بلجنتين: (التنفيذية، ولجنة المساعدات الطبية).</p></div>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SECTION 7: Resource Development, Grants & Ihsan Pipeline (Pages 34-35) -->
    <!-- ========================================================================= -->
    <section class="container" id="resource-development" style="padding-top:50px;">
        <div class="section-intro">
            <span class="eyebrow-pill">تنمية الموارد والاستدامة</span>
            <h2 class="section-headline">مسار المنح الـ (٢٧) وفرص منصة إحسان (ص ٣٤-٣٥)</h2>
            <p class="section-subtext">تقرير شامل بطلبات المنح المقبولة، الطلبات قيد الدراسة، وفرص منصة إحسان، والاعتذارات والتوصيات</p>
        </div>

        <!-- Grants Metrics Row -->
        <div class="grid-3" style="margin-bottom:25px;">
            <div class="exec-card" style="text-align:center;">
                <div class="card-val" style="color:var(--primary);">٢٧ منحة</div>
                <div style="font-weight:700; color:var(--text-main); margin-top:4px;">إجمالي المنح المرفوعة</div>
                <div style="font-size:0.85rem; color:var(--text-muted);">تم التقديم عليها للجهات المانحة والصناديق</div>
            </div>
            <div class="exec-card" style="text-align:center; border:2px solid var(--success); background:#F9FCF9;">
                <div class="card-val" style="color:var(--success);">٤٠,٠٠٠ ر.س</div>
                <div style="font-weight:700; color:var(--text-main); margin-top:4px;">منحتان مقبولتان ومحققتان</div>
                <div style="font-size:0.85rem; color:var(--text-muted);">العنقري (٢٠ ألف) + أبو زيد (٢٠ ألف)</div>
            </div>
            <div class="exec-card" style="text-align:center;">
                <div class="card-val" style="color:var(--secondary-dark);">٠.٠٪</div>
                <div style="font-weight:700; color:var(--text-main); margin-top:4px;">تكلفة جمع التبرعات</div>
                <div style="font-size:0.85rem; color:var(--text-muted);">كفاءة عالية بدون أعباء تسويقية مدفوعة</div>
            </div>
        </div>

        <!-- 11 Under-Review Pipeline Table -->
        <div class="table-card">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.3rem;"><i class="fas fa-clock" style="color:var(--warning); margin-left:8px;"></i> الطلبات قيد الدراسة والمتابعة النشطة (١١ جهة)</h3>
                    <p style="font-size:0.9rem; color:var(--text-muted);">ملفات تم رفعها واستيفاء مسوغاتها وتتابعها الإدارة التنفيذية للحصول على التعميد</p>
                </div>
            </div>
            <table class="custom-table">
                <thead>
                    <tr>
                        <th>الجهة المانحة / الشريك</th>
                        <th>المشروع / البرنامج المرفوع</th>
                        <th>تاريخ التقديم</th>
                        <th>حالة الطلب والمتابعة</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>صندوق دعم الجمعيات</strong></td><td>برنامج «جودة حياة» (منحة البرامج والمشاريع)</td><td>٠١/٠٨/٢٠٢٦</td><td><span class="badge-pill bg-yellow">قيد الدراسة النشطة</span></td></tr>
                    <tr><td><strong>مؤسسة محمد صالح الشاوي الخيرية</strong></td><td>مبادرة عون للرعاية المستدامة وتوفير أدوية الأمراض المزمنة</td><td>٠٦/٠٨/٢٠٢٦</td><td><span class="badge-pill bg-yellow">قيد الدراسة</span></td></tr>
                    <tr><td><strong>أوقاف الشيخ صالح الراجحي</strong></td><td>برنامج «دفء وغذاء لعام ٢٠٢٧م»</td><td>١٢/٠٨/٢٠٢٦</td><td><span class="badge-pill bg-yellow">قيد الدراسة</span></td></tr>
                    <tr><td><strong>مجلس الأوقاف الرائدة</strong></td><td>تم تقديم ٣ برامج صحية وتنموية</td><td>يونيو ٢٠٢٦</td><td><span class="badge-pill bg-green">تمت الموافقة على «جودة الحياة»</span></td></tr>
                    <tr><td><strong>بنك الرياض</strong></td><td>طلب دعم مشاريع الرعاية الصحية</td><td>٠٦/٠٧/٢٠٢٦</td><td><span class="badge-pill bg-yellow">قيد المتابعة</span></td></tr>
                    <tr><td><strong>بنك البلاد</strong></td><td>طلب دعم البرامج الطبية</td><td>يوليو ٢٠٢٦</td><td><span class="badge-pill bg-yellow">قيد المتابعة</span></td></tr>
                    <tr><td><strong>شركات حجاج الداخل والمسؤولية المجتمعية</strong><br><small>(الراجحي، ضيوف البيت، هوليدي إن، أبراج مكة، مشارق الماسية، الرفادة)</small></td><td>برامج التوعية الصحية والرعاية لحجاج بيت الله الحرام</td><td>٠٧/٠٥/٢٠٢٦</td><td><span class="badge-pill bg-yellow">٦ شركات قيد المتابعة</span></td></tr>
                </tbody>
            </table>
        </div>

        <!-- Ihsan Platform & Rejections Breakdown -->
        <div class="grid-2" style="margin-top:25px;">
            <div class="exec-card" style="border-top:4px solid var(--secondary);">
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:12px;"><i class="fas fa-hand-holding-heart" style="color:var(--secondary); margin-left:8px;"></i> فرص منصة إحسان (تحت المعالجة التقنية)</h4>
                <div style="background:var(--bg-subtle); padding:12px; border-radius:var(--radius-sm); margin-bottom:10px;">
                    <strong>١. دعم المصاريف التشغيلية (٠١/٠٨/٢٠٢٦):</strong> رُفض بسبب مطابقة المجال، وتم التواصل مع إدارة المنصة لتعديل التصنيف وإعادة الرفع.
                </div>
                <div style="background:var(--bg-subtle); padding:12px; border-radius:var(--radius-sm);">
                    <strong>٢. جلسات غسيل الكلى (٠٥/٠٨/٢٠٢٦):</strong> رُفض لوجود ملاحظات بالتقارير، وتم إرسال إيميل استفسار وتحديث التقارير عبر البوابة.
                </div>
            </div>

            <div class="exec-card" style="border-top:4px solid var(--danger);">
                <h4 style="color:var(--danger); font-size:1.15rem; margin-bottom:12px;"><i class="fas fa-triangle-exclamation" style="margin-left:8px;"></i> اعتذارات المانحين والتوصيات الاستراتيجية</h4>
                <p style="font-size:0.9rem; line-height:1.7; color:var(--text-main); margin-bottom:10px;">
                    <strong>• انتهاء الموازنات (٤ جهات):</strong> مؤسسة الماجد، مؤسسة الشاوي، شركة طيبة، ومجموعة فنادق.<br>
                    <strong>• اشتراط الحوكمة ومسار التخصص (٤ جهات):</strong> أوقاف الضحيان، مؤسسة طلال (اشتراط الحوكمة)، مؤسسة الحمدان، ومؤسسة المهيدب (طفولة مبكرة).
                </p>
                <div style="background:rgba(198,40,40,0.06); padding:10px; border-radius:var(--radius-sm); font-size:0.88rem; color:var(--danger);">
                    <strong>توصية قسم البرامج:</strong> إعادة التقديم المبكر في الربع الأول ٢٠٢٧م، وتسريع ملف الحوكمة لاستيفاء شروط المانحين، ومتابعة فرص منصة إحسان (جود إحسان).
                </div>
            </div>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SECTION 8: Beneficiary Experiences & Verbatim Thank-You Letters (Pages 40-42) -->
    <!-- ========================================================================= -->
    <section class="container" id="beneficiary-experiences" style="padding-top:50px;">
        <div class="section-intro">
            <span class="eyebrow-pill">صوت المستفيد والأثر الملموس</span>
            <h2 class="section-headline">تجارب المستفيدين ورسائل الشكر والامتنان (ص ٤٠-٤٢)</h2>
            <p class="section-subtext">توثيق حي لقصص الشفاء والتدخلات الطبية العاجلة ورسائل العرفان الموجهة للجمعية وفريقها</p>
        </div>

        <div class="grid-2">
            <!-- Story 1: Samia Suleiman -->
            <div class="exec-card" style="border:2px solid var(--secondary); background:#FFFDFB;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <h3 style="color:var(--primary); font-size:1.3rem;">المستفيدة: سامية سليمان محمد</h3>
                    <span class="tag-pill tag-success">تكلفة العملية: ٦,٣٥٠ ر.س</span>
                </div>
                <div style="font-size:0.92rem; color:var(--text-muted); margin-bottom:12px;">
                    <strong>الجهة المعالجة:</strong> مستشفى المواساة بالمدينة المنورة | <strong>التشخيص:</strong> استئصال كتلة من الصدر
                </div>
                <p style="font-size:0.92rem; line-height:1.8; color:var(--text-main); text-align:justify; margin-bottom:15px;">
                    تقدمت المستفيدة بخطاب إحالة من مستشفى المواساة طالبة المساعدة في تكلفة العملية. وبعد إجراء البحث الاجتماعي ودراسة الحالة، عُرضت على مجلس المساعدات وتمت الموافقة على تغطية كامل التكلفة، وأُجريت العملية بنجاح تام واستعادت صحتها وعافيتها.
                </p>
                <div style="background:rgba(201,169,110,0.1); border-right:4px solid var(--secondary); padding:14px; border-radius:var(--radius-sm); font-style:italic; font-size:0.9rem; line-height:1.8; color:var(--text-dark);">
                    «إلى أعضاء جمعية طبيبي الكرام، تعجز كلمات الثناء والشكر أن تفيكم حقكم لما تقدمونه من جهود جليلة في خدمة المجتمع، فأنتم نموذج يُحتذى به في البذل والعطاء... شكراً لعطائكم السخي الذي يضيء حياة الكثيرين ويصنع الأمل، فكل مساهمة منكم هي بذرة خير تُثمر بسمة في قلب محتاج.»
                </div>
            </div>

            <!-- Story 2: Kandafa Mohammed -->
            <div class="exec-card" style="border:2px solid var(--secondary); background:#FFFDFB;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <h3 style="color:var(--primary); font-size:1.3rem;">المستفيدة: والدة كندفة محمد عتبة</h3>
                    <span class="tag-pill tag-success">مبلغ الدعم: ٧,٠٠٠ ر.س (من ٩,١٨٦)</span>
                </div>
                <div style="font-size:0.92rem; color:var(--text-muted); margin-bottom:12px;">
                    <strong>الجهة المعالجة:</strong> مدينة الملك سلمان الطبية | <strong>التشخيص:</strong> تنويم ورعاية تحت الملاحظة
                </div>
                <p style="font-size:0.92rem; line-height:1.8; color:var(--text-main); text-align:justify; margin-bottom:15px;">
                    تقدمت المستفيدة بطلب مساعدة لتغطية علاج التنويم لوالدتها. وبعد البحث الاجتماعي عُرضت الحالة واعتمد مجلس المساعدات مبلغ ٧,٠٠٠ ريال لتغطية الجزء الأكبر من الفاتورة واستقرار الحالة الصحية للوالدة وخروجها سالمة.
                </p>
                <div style="background:rgba(201,169,110,0.1); border-right:4px solid var(--secondary); padding:14px; border-radius:var(--radius-sm); font-style:italic; font-size:0.9rem; line-height:1.8; color:var(--text-dark);">
                    «من أعماق قلبي، أتقدم بخالص الشكر والامتنان لـ جمعية طبيبي. كنتم سبباً في تفريج كربتي في أصعب وقت... وأخص بالشكر الأستاذة غدير والأستاذ وائل وجميع الشباب العاملين في الجمعية، والله ما قصروا معنا أبداً وكانوا مثالاً للأخلاق والرحمة وحسن التعامل حتى اطمأن قلبي على والدتي.»
                </div>
            </div>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- SECTION 9: Supervisory Bodies, Platforms & Key Donors (Pages 43-45) -->
    <!-- ========================================================================= -->
    <section class="container" id="supervisory-donors" style="padding-top:50px;">
        <div class="section-intro">
            <span class="eyebrow-pill">المنظومة الوطنية والشركاء</span>
            <h2 class="section-headline">الجهات الإشرافية وشركاء العطاء والمانحين (ص ٤٣-٤٥)</h2>
            <p class="section-subtext">تكامل مع القطاعات الحكومية والمنصات الوطنية وقائمة الأوقاف والشركات الداعمة لمسيرة طبيبي</p>
        </div>

        <div class="grid-3" style="margin-bottom:30px;">
            <div class="exec-card" style="border-top:4px solid var(--primary);">
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:12px;"><i class="fas fa-landmark" style="margin-left:8px;"></i> الجهات الإشرافية والحكومية</h4>
                <ul style="list-style:none; line-height:2.2; color:var(--text-main); font-size:0.92rem;">
                    <li><i class="fas fa-check-double" style="color:var(--secondary); margin-left:6px;"></i> المركز الوطني لتنمية القطاع غير الربحي</li>
                    <li><i class="fas fa-check-double" style="color:var(--secondary); margin-left:6px;"></i> وزارة الصحة & تجمع المدينة الصحي</li>
                    <li><i class="fas fa-check-double" style="color:var(--secondary); margin-left:6px;"></i> إمارة منطقة المدينة المنورة</li>
                    <li><i class="fas fa-check-double" style="color:var(--secondary); margin-left:6px;"></i> وزارة الموارد البشرية والتنمية الاجتماعية</li>
                </ul>
            </div>

            <div class="exec-card" style="border-top:4px solid var(--secondary);">
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:12px;"><i class="fas fa-globe" style="margin-left:8px;"></i> المنصات والمتاجر الوطنية</h4>
                <ul style="list-style:none; line-height:2.2; color:var(--text-main); font-size:0.92rem;">
                    <li><i class="fas fa-hand-holding-heart" style="color:var(--secondary); margin-left:6px;"></i> منصة تبرع الوطنية المعتمدة</li>
                    <li><i class="fas fa-hand-holding-heart" style="color:var(--secondary); margin-left:6px;"></i> منصة إحسان الوطنية للعمل الخيري</li>
                    <li><i class="fas fa-hand-holding-heart" style="color:var(--secondary); margin-left:6px;"></i> منصة شفاء للخدمات العلاجية</li>
                    <li><i class="fas fa-hand-holding-heart" style="color:var(--secondary); margin-left:6px;"></i> المتجر الإلكتروني الرسمي للجمعية</li>
                </ul>
            </div>

            <div class="exec-card" style="border-top:4px solid var(--success);">
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:12px;"><i class="fas fa-ribbon" style="margin-left:8px;"></i> أبرز الأوقاف والجهات المانحة</h4>
                <ul style="list-style:none; line-height:2.2; color:var(--text-main); font-size:0.92rem;">
                    <li>• وقف الشيخ نغيمش الأحمدي (رحمه الله)</li>
                    <li>• شركة طابة المطورة للتطوير العمراني</li>
                    <li>• وقف الشيخ عبدالقادر شيبة الحمد</li>
                    <li>• مؤسسة سعيد محمد مكي الخيرية</li>
                    <li>• وقف عبدالرحيم عبدالرزاق</li>
                    <li>• وقف الشيخ عبدالعزيز عبدالله أبو زيد</li>
                </ul>
            </div>
        </div>
    </section>
"""

# Let's replace the existing Section 7 (governance) with the enriched Governance & Advisory Proposal (Pages 36-39)
# and append the new rich sections
governance_enriched_html = """
    <!-- ========================================================================= -->
    <!-- SECTION 10: Strategic Aspirations, Advisory Proposal & 8 Initiatives (Pages 36-39) -->
    <!-- ========================================================================= -->
    <section class="container" id="governance" style="padding-top:50px;">
        <div class="section-intro">
            <span class="eyebrow-pill">التحول المؤسسي والاستدامة</span>
            <h2 class="section-headline">التطلعات ومقترحات التطوير وخطة الفريق الاستشاري (ص ٣٦-٣٩)</h2>
            <p class="section-subtext">تشخيص الاحتياج المؤسسي المتكامل، مقترح التعاقد مع فريق استشاري، و ٨ مبادرات استراتيجية للنصف الثاني</p>
        </div>

        <!-- Comprehensive Advisory Team Proposal Box -->
        <div class="exec-card" style="background:#FFFDF9; border:2px solid var(--secondary); margin-bottom:30px;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:15px; margin-bottom:15px;">
                <div>
                    <span class="tag-pill tag-warning" style="font-size:0.95rem;"><i class="fas fa-user-tie" style="margin-left:6px;"></i> مقترح الإدارة التنفيذية الاستراتيجي</span>
                    <h3 style="color:var(--primary); font-size:1.4rem; margin-top:6px;">الاستعانة بفريق استشاري خارجي متخصص (لمدة ٣ أشهر)</h3>
                </div>
                <div style="background:var(--primary); color:#FFF; padding:10px 20px; border-radius:var(--radius-sm); font-weight:800; font-size:1.1rem;">
                    التكلفة التقديرية: ٥,٠٠٠ إلى ٧,٠٠٠ ر.س شهرياً
                </div>
            </div>
            <p style="font-size:0.95rem; line-height:1.8; color:var(--text-main); text-align:justify; margin-bottom:20px;">
                أظهر تشخيص الواقع أن الجمعية تحتاج إلى <strong>حزمة متكاملة</strong> تشمل: الحوكمة والامتثال، توظيف القوائم المالية للمنح، تفعيل المنصات (نوى وإحسان)، حصر الجهات المانحة، إغلاق المشاريع السابقة، تطوير الموقع، إعداد دليل البرامج، وتصميم العروض التمويلية للانتقال من مجرد تنفيذ الأعمال اليومية إلى بناء منظومة مؤسسية مستدامة.
            </p>

            <!-- 6 Justifications Table -->
            <table class="custom-table" style="margin-bottom:20px;">
                <thead>
                    <tr>
                        <th style="width:25%;">المبرر الاستراتيجي</th>
                        <th>التفصيل والأثر الإداري والمالي</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>تعدد التخصصات</strong></td><td>الأعمال تتطلب حوكمة وتنمية موارد وكتابة مشاريع وإدارة منصات ومحتوى معاً في آن واحد.</td></tr>
                    <tr><td><strong>الوفر المالي الكبير</strong></td><td>تكلفة الفريق الاستشاري (٥ إلى ٧ آلاف ريال) أقل من عُشر تكلفة التوظيف المباشر لكوادر متعددة.</td></tr>
                    <tr><td><strong>استثمار دائم لا مصروف</strong></td><td>المخرجات (ملفات، قواعد بيانات، أدلة، ولوائح) تبقى ملكاً للجمعية وتُفيدها لسنوات قادمة.</td></tr>
                    <tr><td><strong>رفع فرص التمويل</strong></td><td>اكتمال الملفات الأساسية والحوكمة شرط إلزامي للتقديم الاحترافي على المنح الكبرى.</td></tr>
                    <tr><td><strong>نقل المعرفة للكادر</strong></td><td>الفريق يبني النماذج ويُدرّب الموظفين القائمين ولا يحل محلهم.</td></tr>
                    <tr><td><strong>الرقابة التامة محفوظة</strong></td><td>ربط الدفعات بالمخرجات، تقارير دورية، مراجعة المدير التنفيذي، والالتزام الصارم بسرية البيانات.</td></tr>
                </tbody>
            </table>

            <!-- 6 Control Guarantees -->
            <div style="background:rgba(107,29,58,0.05); padding:16px; border-radius:var(--radius-sm);">
                <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:10px;"><i class="fas fa-shield-halved" style="color:var(--secondary-dark); margin-left:6px;"></i> ضمانات الرقابة لمجلس الإدارة الـ (٦):</h4>
                <div class="grid-3" style="gap:10px; font-size:0.88rem; color:var(--text-dark);">
                    <div>• اعتماد نطاق الأعمال والمخرجات مسبقاً.</div>
                    <div>• تحديد مسؤول اتصال رسمي من الجمعية.</div>
                    <div>• تقارير دورية منتظمة بنسب الإنجاز.</div>
                    <div>• عدم اعتماد وثيقة إلا بمراجعة المدير التنفيذي.</div>
                    <div>• ربط صرف الدفعات بالمخرجات الفعلية.</div>
                    <div>• تسليم الملفات بصيغ مفتوحة قابلة للتعديل.</div>
                </div>
            </div>
        </div>

        <!-- 3-Phase Execution Roadmap -->
        <div class="grid-3" style="margin-bottom:35px;">
            <div class="roadmap-card">
                <div>
                    <div class="roadmap-num">المرحلة ١</div>
                    <h3 style="color:var(--secondary-light); font-size:1.25rem; margin-bottom:10px;">الحوكمة ومنصة نوى</h3>
                    <p style="font-size:0.92rem; line-height:1.8; color:#F0EBE1;">
                        • إعداد القوائم المالية والحوكمة الشاملة.<br>
                        • محاضر الجمعية العمومية والمجلس.<br>
                        • تفعيل منصة نوى للمنح والشراكات.
                    </p>
                </div>
                <div style="margin-top:15px; font-weight:700; color:var(--secondary); font-size:0.85rem;">الشهر الأول</div>
            </div>

            <div class="roadmap-card">
                <div>
                    <div class="roadmap-num">المرحلة ٢</div>
                    <h3 style="color:var(--secondary-light); font-size:1.25rem; margin-bottom:10px;">إغلاق المشاريع والموقع</h3>
                    <p style="font-size:0.92rem; line-height:1.8; color:#F0EBE1;">
                        • إغلاق تقارير المشاريع السابقة.<br>
                        • تحديث وتطوير البوابة الإلكترونية.<br>
                        • بناء قاعدة بيانات المانحين والأوقاف.
                    </p>
                </div>
                <div style="margin-top:15px; font-weight:700; color:var(--secondary); font-size:0.85rem;">الشهر الثاني</div>
            </div>

            <div class="roadmap-card">
                <div>
                    <div class="roadmap-num">المرحلة ٣</div>
                    <h3 style="color:var(--secondary-light); font-size:1.25rem; margin-bottom:10px;">الحقائب والتمويل</h3>
                    <p style="font-size:0.92rem; line-height:1.8; color:#F0EBE1;">
                        • إعداد الحقائب التعريفية والعروض التمويلية.<br>
                        • البدء في تقديم طلبات المنح الكبرى.<br>
                        • الجاهزية المبكرة لموازنات Q1 2027.
                    </p>
                </div>
                <div style="margin-top:15px; font-weight:700; color:var(--secondary); font-size:0.85rem;">الشهر الثالث</div>
            </div>
        </div>

        <!-- 8 Strategic Development Initiatives (ص 39) -->
        <div class="table-card">
            <h3 style="color:var(--primary); font-size:1.25rem; margin-bottom:15px;"><i class="fas fa-rocket" style="color:var(--secondary); margin-left:8px;"></i> حزمة المبادرات والمقترحات التطويرية الـ (٨) المعتمدة (ص ٣٩)</h3>
            <div class="grid-2" style="gap:15px;">
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--primary);">
                    <strong>١. تنويع الشراكات ومصادر الدخل:</strong> التوسع في الأوقاف والشراكات مع القطاع الخاص لتعزيز الاستدامة المالية.
                </div>
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--primary);">
                    <strong>٢. تعزيز الظهور الإعلامي:</strong> حضور أوسع في المحافل المهمة والمنصات الرقمية لزيادة الوعي برسالة الجمعية.
                </div>
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--primary);">
                    <strong>٣. استقطاب الكفاءات:</strong> شغل الوظائف الشاغرة في الإعلام والموارد البشرية وتنمية الموارد المالية.
                </div>
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--secondary);">
                    <strong>٤. تنفيذ برنامج «بطاقة طبيبي»:</strong> بطاقة تتيح لحاملها تخفيضات لدى المستشفيات، المختبرات، النوادي، والمتاجر الصحية.
                </div>
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--secondary);">
                    <strong>٥. تعديل لائحة صرف المساعدات:</strong> اتخاذ إجراءات تصحيحية مرنة لرفع نسبة قبول الحالات المتقدمة للدعم.
                </div>
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--primary);">
                    <strong>٦. الاستعانة بالفريق الاستشاري:</strong> استكمال الحوكمة، القوائم المالية، منصة نوى، والعروض التمويلية.
                </div>
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--primary);">
                    <strong>٧. اعتماد مصفوفة الصلاحيات:</strong> لإتاحة فرصة سرعة ومرونة اتخاذ القرار ومواكبة متطلبات العمل اليومي.
                </div>
                <div style="background:var(--bg-subtle); padding:12px 16px; border-radius:var(--radius-sm); border-right:3px solid var(--primary);">
                    <strong>٨. تفعيل دور المجلس والعمومية:</strong> مساهمة الأعضاء في فتح قنوات الدعم المالي من المانحين والشركات.
                </div>
            </div>
        </div>
    </section>
"""

# Let's replace the existing Section 7 in generate_v2_dashboard.py with the new sections
# First let's check where <section class="container" id="governance"> is in content
start_gov = content.find('<section class="container" id="governance">')
end_gov = content.find('<section class="container" id="master-appendices">')

if start_gov != -1 and end_gov != -1:
    content = content[:start_gov] + pages_30_47_html + governance_enriched_html + content[end_gov:]
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated generate_v2_dashboard.py with full pages 30 to 47 data successfully!")
else:
    print("Could not find exact governance section boundaries.")
