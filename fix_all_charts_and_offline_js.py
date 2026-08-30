# -*- coding: utf-8 -*-
"""
Fix all Chart.js scripts and enable offline loading:
1. Include local chart.umd.min.js and fallback to CDN.
2. Initialize ALL 9 charts properly in JavaScript:
   - page13IncomePieChart (Page 13 Income Diversity)
   - page12GrowthChart (Page 12 Income vs Expenses)
   - page17FinancialStructureChart (Page 17 Balance Sheet Structure)
   - page18LiabilitiesChart (Page 18 Liabilities Settlement)
   - v2RevChart (Revenue Comparison H1 2026 vs H1 2025)
   - v2ExpChart (Expense Breakdown)
   - budgetExecutionChart (Budget Execution Rates %)
   - topDonorsChart (Top Endowments & Donors Contributions)
   - fixedAssetsChart (Fixed Assets Capital Expenditure Breakdown)
3. Ensure custom plugins (data values on bars, percentages on slices) execute reliably without throwing errors.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")

with open(v2_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update <head> to load local Chart.js first, then CDN fallback
old_head_script = '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'
new_head_script = """    <!-- Chart.js 4 (Local Offline + CDN Fallback) -->
    <script src="assets/js/chart.umd.min.js"></script>
    <script>
        if (typeof Chart === 'undefined') {
            document.write('<script src="https://cdn.jsdelivr.net/npm/chart.js"><\\/script>');
        }
    </script>"""

if old_head_script in content and "assets/js/chart.umd.min.js" not in content:
    content = content.replace(old_head_script, new_head_script)
    print("Updated head to include offline Chart.js!")

# 2. Comprehensive JavaScript block for all 9 charts
complete_script_block = """    <!-- Interactive Scripts & Chart.js with Direct On-Chart Labels -->
    <script>
        // Live Filter Function for tables
        function filterTable(inputId, tableId) {
            const input = document.getElementById(inputId);
            if (!input) return;
            const filter = input.value.toLowerCase();
            const table = document.getElementById(tableId);
            if (!table) return;
            const tr = table.getElementsByTagName('tr');

            for (let i = 1; i < tr.length; i++) {
                if (tr[i].classList.contains('total-row')) continue;
                let textContent = tr[i].textContent || tr[i].innerText;
                if (textContent.toLowerCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }

        // Custom Inline Chart.js Plugin for Bar Chart Value Labels
        const barValueLabelsPlugin = {
            id: 'barValueLabels',
            afterDatasetsDraw(chart, args, options) {
                const { ctx, data } = chart;
                ctx.save();
                ctx.font = 'bold 11px Cairo, Tajawal, sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'bottom';

                chart.data.datasets.forEach((dataset, datasetIndex) => {
                    const meta = chart.getDatasetMeta(datasetIndex);
                    if (!meta.hidden) {
                        meta.data.forEach((element, index) => {
                            const val = dataset.data[index];
                            if (val !== undefined && val !== null && val > 0) {
                                const formattedVal = Number(val).toLocaleString('ar-SA');
                                ctx.fillStyle = datasetIndex === 0 ? '#380B1B' : '#8C6D37';
                                ctx.fillText(formattedVal, element.x, element.y - 4);
                            }
                        });
                    }
                });
                ctx.restore();
            }
        };

        // Custom Inline Chart.js Plugin for Doughnut/Pie Chart Percentages
        const doughnutPercentagePlugin = {
            id: 'doughnutPercentages',
            afterDraw(chart, args, options) {
                const { ctx, chartArea } = chart;
                if (!chartArea) return;
                const meta = chart.getDatasetMeta(0);
                if (!meta || !meta.data || !meta.data.length) return;

                const dataset = chart.data.datasets[0];
                const total = dataset.data.reduce((acc, cur) => acc + (Number(cur) || 0), 0);
                if (total <= 0) return;

                ctx.save();
                ctx.font = 'bold 12px Cairo, Tajawal, sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';

                meta.data.forEach((element, index) => {
                    const value = Number(dataset.data[index]) || 0;
                    if (value <= 0) return;
                    const percentage = ((value / total) * 100).toFixed(0);
                    if (Number(percentage) < 2) return;

                    const angle = element.startAngle + (element.endAngle - element.startAngle) / 2;
                    const radius = (element.innerRadius || 0) + (element.outerRadius - (element.innerRadius || 0)) * 0.55;
                    const x = element.x + Math.cos(angle) * radius;
                    const y = element.y + Math.sin(angle) * radius;

                    ctx.shadowColor = 'rgba(0, 0, 0, 0.7)';
                    ctx.shadowBlur = 4;
                    ctx.shadowOffsetX = 1;
                    ctx.shadowOffsetY = 1;
                    ctx.fillStyle = '#FFFFFF';

                    ctx.fillText(`٪${Number(percentage).toLocaleString('ar-SA')}`, x, y);
                });
                ctx.restore();
            }
        };

        // Initialize All Dashboard Charts on DOM Load
        document.addEventListener('DOMContentLoaded', function() {
            if (typeof Chart === 'undefined') {
                console.error('Chart.js failed to load.');
                return;
            }

            Chart.defaults.font.family = "'Cairo', 'Tajawal', sans-serif";
            Chart.defaults.color = '#555';

            // 1. Page 13: Income Diversity Pie Chart (مصادر الدخل ص 13)
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
                                labels: { boxWidth: 12, font: { size: 11, family: 'Cairo' } }
                            },
                            tooltip: {
                                rtl: true,
                                callbacks: {
                                    label: function(context) {
                                        const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                        const val = context.raw;
                                        const pct = ((val / total) * 100).toFixed(1);
                                        return `${context.label}: ${val.toLocaleString()} ريال (${pct}%)`;
                                    }
                                }
                            }
                        }
                    }
                });
            }

            // 2. Page 12: Income vs Expenses Growth Chart (نمو الإيرادات والمصروفات ص 12)
            const ctxP12 = document.getElementById('page12GrowthChart');
            if (ctxP12) {
                new Chart(ctxP12, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['إجمالي الدخل', 'إجمالي المصروفات'],
                        datasets: [
                            {
                                label: 'H1 2026م',
                                data: [582167, 249274],
                                backgroundColor: '#541228',
                                borderRadius: 6
                            },
                            {
                                label: 'H1 2025م',
                                data: [199474, 103529],
                                backgroundColor: '#8F8B85',
                                borderRadius: 6
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        layout: { padding: { top: 25, bottom: 5 } },
                        plugins: {
                            legend: { display: false },
                            tooltip: { rtl: true }
                        },
                        scales: {
                            y: { 
                                beginAtZero: true, 
                                suggestedMax: 650000,
                                ticks: { callback: v => v.toLocaleString() + ' ر.س' } 
                            }
                        }
                    }
                });
            }

            // 3. Page 17: Financial Structure Doughnut Chart (هيكل وتوزيع السيولة ص 17)
            const ctxP17 = document.getElementById('page17FinancialStructureChart');
            if (ctxP17) {
                new Chart(ctxP17, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['أموال غير مقيدة للتشغيل (٦٣٤,٦٦١)', 'أموال مقيدة للعلاج والزكاة (٣٦٧,٠٩٣)', 'ذمم مدينة اشتراكات (١٢,٠٠٠)', 'التزامات دائنة (٥,٠٠٠)'],
                        datasets: [{
                            data: [634661, 367093, 12000, 5000],
                            backgroundColor: ['#1B7A48', '#C9A96E', '#C7771E', '#541228'],
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
                        cutout: '55%'
                    }
                });
            }

            // 4. Page 18: Liabilities Settlement Doughnut Chart (سداد الالتزامات ص 18)
            const ctxP18 = document.getElementById('page18LiabilitiesChart');
            if (ctxP18) {
                new Chart(ctxP18, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['التزامات مسددة بنجاح (١٣,٢١١)', 'متبقي مستحق لحوكمة مؤشرات النجاح (٥,٠٠٠)'],
                        datasets: [{
                            data: [13211, 5000],
                            backgroundColor: ['#1B7A48', '#541228'],
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

            // 5. Revenue Comparison Bar Chart (مقارنة الإيرادات H1)
            const ctxRev = document.getElementById('v2RevChart');
            if (ctxRev) {
                new Chart(ctxRev, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['الزكاة', 'علاج مقيد', 'المتجر', 'منصة تبرع', 'دعم عام', 'العضوية'],
                        datasets: [
                            {
                                label: 'H1 2026م (ريال)',
                                data: [70000, 75000, 10469, 1203, 407495, 18000],
                                backgroundColor: '#541228',
                                borderRadius: 6
                            },
                            {
                                label: 'H1 2025م (ريال)',
                                data: [80000, 25000, 124, 13786, 62564, 18000],
                                backgroundColor: '#C9A96E',
                                borderRadius: 6
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        layout: { padding: { top: 25, bottom: 5 } },
                        plugins: {
                            legend: { position: 'top', rtl: true, labels: { font: { size: 12, weight: '700' } } },
                            tooltip: { rtl: true }
                        },
                        scales: {
                            y: { 
                                beginAtZero: true, 
                                suggestedMax: 460000,
                                ticks: { callback: v => v.toLocaleString() + ' ر.س' } 
                            }
                        }
                    }
                });
            }

            // 6. Expenses Distribution Doughnut Chart (توزيع المصروفات)
            const ctxExp = document.getElementById('v2ExpChart');
            if (ctxExp) {
                new Chart(ctxExp, {
                    type: 'doughnut',
                    plugins: [doughnutPercentagePlugin],
                    data: {
                        labels: ['المساعدات الطبية (البرامج)', 'الرواتب والأجور', 'الإيجار والمقر', 'التأمينات والمتعاونين', 'الأصول الثابتة', 'مصروفات تشغيلية أخرى'],
                        datasets: [{
                            data: [208605, 144405, 63333, 27768, 15621, 18768],
                            backgroundColor: [
                                '#1B7A48',
                                '#541228',
                                '#C9A96E',
                                '#731A38',
                                '#C7771E',
                                '#8F8B85'
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
                            legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 11 } } },
                            tooltip: { 
                                rtl: true,
                                callbacks: {
                                    label: function(context) {
                                        const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                        const val = context.raw;
                                        const pct = ((val / total) * 100).toFixed(1);
                                        return `${context.label}: ${val.toLocaleString()} ريال (${pct}%)`;
                                    }
                                }
                            }
                        },
                        cutout: '58%'
                    }
                });
            }

            // 7. Budget Execution Bar Chart (تنفيذ الموازنة)
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

            // 8. Top Donors Bar Chart (كبار المانحين)
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

            // 9. Fixed Assets Pie Chart (الأصول والتجهيزات)
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
            }
        });
    </script>
</body>
</html>
\"\"\""""

# Find the script section in generate_v2_dashboard.py and replace it with complete_script_block
script_start = content.find('<!-- Interactive Scripts & Chart.js with Direct On-Chart Labels -->')
if script_start != -1:
    content = content[:script_start] + complete_script_block + "\n\nwith open(output_file, 'w', encoding='utf-8') as f:\n    f.write(html_content)\n\nprint(f'Generated Executive Dashboard V2 successfully: {output_file}')\n"
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced script section with complete 9-chart initialization block in generate_v2_dashboard.py!")

# Recompile dashboard
os.system(f'py -3 "{v2_file}"')
print("Recompiled dashboard successfully!")
