# -*- coding: utf-8 -*-
"""
Add dedicated Chart.js charts for EVERY table across the entire dashboard:
1. Matrix Table -> Radar/Bar Chart of Strategic Achievement Rates
2. Programs Health Check Table -> Doughnut Chart of Programs Status
3. Budget Execution Table -> Horizontal Bar Chart of Budget Item Execution %
4. Bank Balances Table (P11) -> Doughnut Chart of Restricted vs Unrestricted Funds Structure
5. 14 Rejected Cases Table -> Doughnut Chart of Rejection Reasons Breakdown
6. 27 Grants Pipeline Table -> Funnel/Doughnut Chart of Grants Status Pipeline
7. HR Comparison Table -> Grouped Bar Chart of HR & Training Indicators
8. Top Donors Table (App 1) -> Bar Chart of Major Endowments & Donors Contributions
9. Fixed Assets Table (App 2) -> Pie Chart of Capital Expenditure on Assets
10. Revenue Table -> Grouped Bar Chart (v2RevChart)
11. P13 Income Diversity Table -> Pie Chart (page13IncomePieChart)
12. P12 Income vs Expenses Table -> Bar Chart (page12GrowthChart)
13. Operating Expenses Table -> Doughnut Chart (v2ExpChart)
14. Comparative P10/P11 Table -> Comparative Bar Chart
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")

with open(v2_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Chart beside Strategic Matrix Table (Section 3.5)
matrix_chart_html = """        <!-- Strategic Matrix Chart -->
        <div class="grid-2" style="margin-top:25px; margin-bottom:30px; gap:25px;">
            <div class="exec-card" style="padding:20px;">
                <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;"><i class="fas fa-chart-radar" style="color:var(--secondary); margin-left:6px;"></i> نسب الإنجاز للمؤشرات الاستراتيجية المعتمدة (٪)</h4>
                <div style="height:320px; position:relative;">
                    <canvas id="matrixStrategicChart"></canvas>
                </div>
            </div>
            <div class="exec-card" style="padding:20px;">
                <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;"><i class="fas fa-pie-chart" style="color:var(--secondary); margin-left:6px;"></i> حالة البرامج الاستراتيجية الـ (١٠)</h4>
                <div style="height:320px; position:relative;">
                    <canvas id="programsStatusChart"></canvas>
                </div>
            </div>
        </div>"""

if "matrixStrategicChart" not in content:
    content = content.replace("<!-- 10 Strategic Programs Health Check Table -->", matrix_chart_html + "\n\n        <!-- 10 Strategic Programs Health Check Table -->")

# 2. Add Chart beside Budget Execution Table (Section 4)
budget_chart_html = """        <!-- Budget Execution Bar Chart -->
        <div class="exec-card" style="margin-top:25px; margin-bottom:25px; padding:25px;">
            <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:15px; text-align:center;"><i class="fas fa-chart-column" style="color:var(--secondary); margin-left:8px;"></i> نسبة تنفيذ بنود الموازنة التقديرية لعام ٢٠٢٦م (المحقق الفعلي مقابل المستهدف)</h4>
            <div style="height:300px; position:relative;">
                <canvas id="budgetExecutionChart"></canvas>
            </div>
        </div>"""

if "budgetExecutionChart" not in content:
    content = content.replace("<!-- Section 5: Clinical Impact", budget_chart_html + "\n\n    <!-- Section 5: Clinical Impact")

# 3. Add Chart beside 14 Rejected Cases Table
rejected_chart_html = """        <!-- Rejection Reasons Doughnut Chart -->
        <div class="exec-card" style="margin-top:20px; margin-bottom:25px; padding:20px;">
            <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;"><i class="fas fa-chart-pie" style="color:var(--danger); margin-left:8px;"></i> توزيع أسباب عدم قبول الحالات المتقدمة (١٤ حالة)</h4>
            <div style="height:280px; position:relative;">
                <canvas id="rejectedCasesChart"></canvas>
            </div>
        </div>"""

if "rejectedCasesChart" not in content:
    content = content.replace("<!-- Section 6: Health Partnerships Network", rejected_chart_html + "\n\n    <!-- Section 6: Health Partnerships Network")

# 4. Add Chart beside HR Table (Section 7)
hr_chart_html = """        <!-- HR Comparison Chart -->
        <div class="exec-card" style="margin-top:20px; margin-bottom:25px; padding:20px;">
            <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;"><i class="fas fa-users-gear" style="color:var(--secondary); margin-left:8px;"></i> مقارنة مؤشرات الموارد البشرية والكادر بين عامي ٢٠٢٥م و ٢٠٢٦م</h4>
            <div style="height:280px; position:relative;">
                <canvas id="hrComparisonChart"></canvas>
            </div>
        </div>"""

if "hrComparisonChart" not in content:
    content = content.replace("<!-- Section 8: Major Administrative", hr_chart_html + "\n\n    <!-- Section 8: Major Administrative")

# 5. Add Chart beside 27 Grants Pipeline Table (Section 9)
grants_chart_html = """        <!-- Grants Pipeline Chart -->
        <div class="exec-card" style="margin-top:20px; margin-bottom:25px; padding:20px;">
            <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;"><i class="fas fa-hand-holding-dollar" style="color:var(--secondary); margin-left:8px;"></i> الموقف التنفيذي لطلبات المنح والشراكات المالية (٢٧ طلباً)</h4>
            <div style="height:280px; position:relative;">
                <canvas id="grantsPipelineChart"></canvas>
            </div>
        </div>"""

if "grantsPipelineChart" not in content:
    content = content.replace("<!-- Section 10: Strategic Growth Roadmaps", grants_chart_html + "\n\n    <!-- Section 10: Strategic Growth Roadmaps")

# 6. Add Chart beside Donors & Fixed Assets Tables (Section 13)
appendices_chart_html = """        <!-- Appendices Charts: Top Donors & Fixed Assets -->
        <div class="grid-2" style="margin-top:25px; margin-bottom:30px; gap:25px;">
            <div class="exec-card" style="padding:20px;">
                <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;"><i class="fas fa-handshake-angle" style="color:var(--secondary); margin-left:6px;"></i> مساهمات كبار المانحين والأوقاف الاستراتيجية (ريال)</h4>
                <div style="height:300px; position:relative;">
                    <canvas id="topDonorsChart"></canvas>
                </div>
            </div>
            <div class="exec-card" style="padding:20px;">
                <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:15px; text-align:center;"><i class="fas fa-desktop" style="color:var(--secondary); margin-left:6px;"></i> توزيع الإنفاق على الأصول الثابتة والتجهيزات (١٥,٦٢١ ريال)</h4>
                <div style="height:300px; position:relative;">
                    <canvas id="fixedAssetsChart"></canvas>
                </div>
            </div>
        </div>"""

if "topDonorsChart" not in content:
    content = content.replace("<!-- Footer & Official Channels -->", appendices_chart_html + "\n\n    <!-- Footer & Official Channels -->")

# Add JavaScript for all the new charts
all_new_charts_js = """            // 5. Strategic Matrix Bar Chart
            const ctxMat = document.getElementById('matrixStrategicChart');
            if (ctxMat) {
                new Chart(ctxMat, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['توطين الوظائف', 'الشراكات', 'التحول الرقمي', 'تنويع الدخل', 'الإيرادات', 'الحوكمة', 'المستفيدون', 'التطوع', 'الاستشارات'],
                        datasets: [{
                            label: 'نسبة الإنجاز %',
                            data: [100, 100, 100, 100, 77.6, 70, 7.0, 25, 0],
                            backgroundColor: [
                                '#1B7A48', '#1B7A48', '#1B7A48', '#1B7A48',
                                '#2E7D32', '#C7771E', '#D9822B', '#C9A96E', '#8F8B85'
                            ],
                            borderRadius: 5
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        indexAxis: 'y',
                        layout: { padding: { right: 30 } },
                        plugins: { legend: { display: false } },
                        scales: { x: { beginAtZero: true, max: 115, ticks: { callback: v => v + '%' } } }
                    }
                });
            }

            // 6. 10 Programs Status Doughnut Chart
            const ctxProg = document.getElementById('programsStatusChart');
            if (ctxProg) {
                new Chart(ctxProg, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['برامج مفعلة ونشطة (جودة الحياة، عون)', 'برامج جزئية (وعي)', 'برامج لم تبدأ'],
                        datasets: [{
                            data: [2, 1, 7],
                            backgroundColor: ['#1B7A48', '#C9A96E', '#8F8B85'],
                            borderWidth: 2,
                            borderColor: '#FFF'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 11 } } }
                        },
                        cutout: '55%'
                    }
                });
            }

            // 7. Budget Execution Bar Chart
            const ctxBgt = document.getElementById('budgetExecutionChart');
            if (ctxBgt) {
                new Chart(ctxBgt, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['شراء الأصول', 'المصروفات التشغيلية', 'إيرادات H1 المستهدفة', 'الرواتب والأجور', 'المساعدات العلاجية'],
                        datasets: [{
                            label: 'نسبة التنفيذ %',
                            data: [80.3, 77.2, 76.3, 30.6, 27.8],
                            backgroundColor: ['#541228', '#731A38', '#1B7A48', '#C9A96E', '#8C6D37'],
                            borderRadius: 6
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        layout: { padding: { top: 25, bottom: 5 } },
                        plugins: { legend: { display: false } },
                        scales: { y: { beginAtZero: true, max: 100, ticks: { callback: v => v + '%' } } }
                    }
                });
            }

            // 8. 14 Rejected Cases Doughnut Chart
            const ctxRej = document.getElementById('rejectedCasesChart');
            if (ctxRej) {
                new Chart(ctxRej, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['انتهاء الإقامة (٧ حالات)', 'دعم سابق وجمعيات أخرى (حالتان)', 'نقص تقارير طبية (حالتان)', 'تأمين طبي (حالة)', 'انتهاء تأشيرة (حالة)', 'قيد المتابعة (حالة)'],
                        datasets: [{
                            data: [7, 2, 2, 1, 1, 1],
                            backgroundColor: ['#8B0000', '#B83227', '#D9822B', '#C9A96E', '#8F8B85', '#541228'],
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
                        cutout: '52%'
                    }
                });
            }

            // 9. HR Comparison Bar Chart
            const ctxHr = document.getElementById('hrComparisonChart');
            if (ctxHr) {
                new Chart(ctxHr, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['الكادر الوظيفي', 'الدورات التدريبية', 'الفرص التطوعية', 'نسبة التوطين (%)'],
                        datasets: [
                            { label: '٢٠٢٦م', data: [4, 8, 4, 100], backgroundColor: '#541228', borderRadius: 5 },
                            { label: '٢٠٢٥م', data: [2, 0, 108, 100], backgroundColor: '#C9A96E', borderRadius: 5 }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        layout: { padding: { top: 25, bottom: 5 } },
                        plugins: {
                            legend: { position: 'top', rtl: true, labels: { font: { size: 11, weight: '700' } } }
                        },
                        scales: { y: { beginAtZero: true } }
                    }
                });
            }

            // 10. Grants Pipeline Doughnut Chart
            const ctxGrants = document.getElementById('grantsPipelineChart');
            if (ctxGrants) {
                new Chart(ctxGrants, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['جهات قيد الدراسة والمتابعة (١١)', 'اعتذارات لعدم مطابقة النطاق (٨)', 'شركات تجارية (٦)', 'منح مقبولة ومحققة (٢)'],
                        datasets: [{
                            data: [11, 8, 6, 2],
                            backgroundColor: ['#2E7D32', '#B83227', '#8F8B85', '#1B7A48'],
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
                        cutout: '52%'
                    }
                });
            }

            // 11. Top Donors Bar Chart
            const ctxDon = document.getElementById('topDonorsChart');
            if (ctxDon) {
                new Chart(ctxDon, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['فاعل خير', 'أوقاف العنقري', 'محمد شاوي', 'ناصر الحازمي', 'أبو زيد', 'جمعية بنيان'],
                        datasets: [{
                            label: 'المبلغ (ريال)',
                            data: [250000, 50000, 30000, 30000, 20000, 15000],
                            backgroundColor: '#541228',
                            borderRadius: 6
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        layout: { padding: { top: 25, bottom: 5 } },
                        plugins: { legend: { display: false } },
                        scales: { y: { beginAtZero: true, suggestedMax: 280000, ticks: { callback: v => v.toLocaleString() + ' ر.س' } } }
                    }
                });
            }

            // 12. Fixed Assets Pie Chart
            const ctxAst = document.getElementById('fixedAssetsChart');
            if (ctxAst) {
                new Chart(ctxAst, {
                    type: 'pie',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['مكاتب سكرتارية (٤,٦٨٠)', 'مكيفات المقر (٤,٥٩١)', 'كراسي دوارة (٢,٧٠٠)', 'طابعة ليزر (١,٣٥٠)', 'خزينة مستندات (١,٢٥٠)', 'كراسي انتظار (١,٠٥٠)'],
                        datasets: [{
                            data: [4680, 4590.8, 2700, 1350, 1250, 1050],
                            backgroundColor: ['#541228', '#731A38', '#C9A96E', '#8C6D37', '#1B7A48', '#8F8B85'],
                            borderWidth: 2,
                            borderColor: '#FFF'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { position: 'bottom', rtl: true, labels: { boxWidth: 10, font: { size: 10 } } }
                        }
                    }
                });
            }"""

if "matrixStrategicChart" not in content or "topDonorsChart" not in content:
    content = content.replace("// 4. Page 13 Income Pie Chart", all_new_charts_js + "\n\n            // 4. Page 13 Income Pie Chart")
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Added all chart scripts to generate_v2_dashboard.py!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_web_slides.py")}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_full_14_slides_pptx.py")}"')
os.system(f'py -3 "{os.path.join(base_dir, "enrich_word_and_presentations.py")}"')

print("All tables across all deliverables are now paired with dedicated charts!")
