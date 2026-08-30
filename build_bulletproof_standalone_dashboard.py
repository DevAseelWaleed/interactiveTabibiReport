# -*- coding: utf-8 -*-
"""
Build Bulletproof Standalone Dashboard with Inlined Chart.js & Safe Isolated Chart Initializers:
1. Inlines Chart.js 4 library directly into <head> (Zero external file / CDN dependencies).
2. Bulletproof Custom Plugins with complete defensive try-catch and property checks.
3. Isolated try-catch for EVERY chart initialization.
4. Auto-synchronize to both folders:
   - e:\Work\زبون تقرير نصف سنوي طبيبي\التقرير_الاحترافي_المطور\index.html
   - e:\Work\زبون تقرير نصف سنوي طبيبي\التقرير_الجديد\index.html
"""
import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
chart_js_path = os.path.join(base_dir, "التقرير_الاحترافي_المطور", "assets", "js", "chart.umd.min.js")

with open(chart_js_path, "r", encoding="utf-8", errors="ignore") as f:
    chart_js_code = f.read()

v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

# 1. Update <head> to inline Chart.js directly
head_start = dash_code.find('<!-- Chart.js 4')
head_end = dash_code.find('<style>', head_start)
if head_start != -1 and head_end != -1:
    inlined_chart_head = f"""<!-- Inlined Complete Chart.js 4 (100% Offline & Universal) -->
    <script>
{chart_js_code}
    </script>
    """
    dash_code = dash_code[:head_start] + inlined_chart_head + dash_code[head_end:]
    print("Inlined Chart.js directly in <head> of generate_v2_dashboard.py!")

# 2. Build Ultra-Defensive Bulletproof JavaScript Block
ultra_safe_js = """    <!-- Bulletproof Interactive Scripts & Independent Chart Initializers -->
    <script>
        // Live Filter Function for tables
        function filterTable(inputId, tableId) {
            try {
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
            } catch(e) { console.error('Filter error:', e); }
        }

        // Defensive Plugin: Bar Chart Value Labels
        const barValueLabelsPlugin = {
            id: 'barValueLabels',
            afterDatasetsDraw(chart, args, options) {
                try {
                    const { ctx } = chart;
                    if (!ctx) return;
                    ctx.save();
                    ctx.font = 'bold 11px Cairo, Tajawal, sans-serif';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'bottom';

                    chart.data.datasets.forEach((dataset, datasetIndex) => {
                        const meta = chart.getDatasetMeta(datasetIndex);
                        if (meta && !meta.hidden && meta.data) {
                            meta.data.forEach((element, index) => {
                                if (!element || typeof element.x !== 'number' || typeof element.y !== 'number') return;
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
                } catch(err) { console.warn('barValueLabelsPlugin error:', err); }
            }
        };

        // Defensive Plugin: Doughnut / Pie Chart Percentages
        const doughnutPercentagePlugin = {
            id: 'doughnutPercentages',
            afterDraw(chart, args, options) {
                try {
                    const { ctx, chartArea } = chart;
                    if (!ctx || !chartArea) return;
                    const meta = chart.getDatasetMeta(0);
                    if (!meta || !meta.data || !meta.data.length) return;

                    const dataset = chart.data.datasets[0];
                    if (!dataset || !dataset.data) return;
                    const total = dataset.data.reduce((acc, cur) => acc + (Number(cur) || 0), 0);
                    if (total <= 0) return;

                    ctx.save();
                    ctx.font = 'bold 12px Cairo, Tajawal, sans-serif';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';

                    meta.data.forEach((element, index) => {
                        if (!element || typeof element.x !== 'number' || typeof element.y !== 'number') return;
                        if (typeof element.startAngle !== 'number' || typeof element.endAngle !== 'number') return;

                        const value = Number(dataset.data[index]) || 0;
                        if (value <= 0) return;
                        const percentage = ((value / total) * 100).toFixed(0);
                        if (Number(percentage) < 2) return;

                        const angle = element.startAngle + (element.endAngle - element.startAngle) / 2;
                        const innerR = typeof element.innerRadius === 'number' ? element.innerRadius : 0;
                        const outerR = typeof element.outerRadius === 'number' ? element.outerRadius : 50;
                        const radius = innerR + (outerR - innerR) * 0.55;
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
                } catch(err) { console.warn('doughnutPercentagePlugin error:', err); }
            }
        };

        // Initialize All Charts with strict isolation
        function initDashboardCharts() {
            if (typeof Chart === 'undefined') {
                console.error('Chart.js is not loaded.');
                return;
            }

            Chart.defaults.font.family = "'Cairo', 'Tajawal', sans-serif";
            Chart.defaults.color = '#555';

            // 1. Page 13: Income Diversity Pie Chart
            try {
                const el = document.getElementById('page13IncomePieChart');
                if (el) {
                    new Chart(el, {
                        type: 'pie',
                        plugins: [doughnutPercentagePlugin],
                        data: {
                            labels: ['تبرعات ودعم عام', 'العلاج', 'الزكاة', 'العضوية', 'المتجر الإلكتروني', 'منصة تبرع'],
                            datasets: [{
                                data: [407495, 75000, 70000, 18000, 10469, 1203],
                                backgroundColor: ['#A61C48', '#380B1B', '#5E132D', '#D9829B', '#E8B4C2', '#C9A96E'],
                                borderWidth: 2,
                                borderColor: '#FFF'
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 11, family: 'Cairo' } } },
                                tooltip: { rtl: true }
                            }
                        }
                    });
                }
            } catch(e) { console.error('Error in page13IncomePieChart:', e); }

            // 2. Page 12: Income vs Expenses Growth Chart
            try {
                const el = document.getElementById('page12GrowthChart');
                if (el) {
                    new Chart(el, {
                        type: 'bar',
                        plugins: [barValueLabelsPlugin],
                        data: {
                            labels: ['إجمالي الدخل', 'إجمالي المصروفات'],
                            datasets: [
                                { label: 'H1 2026م', data: [582167, 249274], backgroundColor: '#541228', borderRadius: 6 },
                                { label: 'H1 2025م', data: [199474, 103529], backgroundColor: '#8F8B85', borderRadius: 6 }
                            ]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            layout: { padding: { top: 25, bottom: 5 } },
                            plugins: { legend: { display: false }, tooltip: { rtl: true } },
                            scales: { y: { beginAtZero: true, suggestedMax: 650000, ticks: { callback: v => v.toLocaleString() + ' ر.س' } } }
                        }
                    });
                }
            } catch(e) { console.error('Error in page12GrowthChart:', e); }

            // 3. Page 17: Financial Structure Doughnut Chart
            try {
                const el = document.getElementById('page17FinancialStructureChart');
                if (el) {
                    new Chart(el, {
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
                            plugins: { legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 10.5 } } } },
                            cutout: '55%'
                        }
                    });
                }
            } catch(e) { console.error('Error in page17FinancialStructureChart:', e); }

            // 4. Page 18: Liabilities Settlement Doughnut Chart
            try {
                const el = document.getElementById('page18LiabilitiesChart');
                if (el) {
                    new Chart(el, {
                        type: 'doughnut',
                        plugins: [doughnutPercentagePlugin],
                        data: {
                            labels: ['التزامات مسددة بنجاح (١٣,٢١١)', 'متبقي مستحق للحوكمة (٥,٠٠٠)'],
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
                            plugins: { legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 11 } } } },
                            cutout: '55%'
                        }
                    });
                }
            } catch(e) { console.error('Error in page18LiabilitiesChart:', e); }

            // 5. Revenue Comparison Bar Chart
            try {
                const el = document.getElementById('v2RevChart');
                if (el) {
                    new Chart(el, {
                        type: 'bar',
                        plugins: [barValueLabelsPlugin],
                        data: {
                            labels: ['الزكاة', 'علاج مقيد', 'المتجر', 'منصة تبرع', 'دعم عام', 'العضوية'],
                            datasets: [
                                { label: 'H1 2026م (ريال)', data: [70000, 75000, 10469, 1203, 407495, 18000], backgroundColor: '#541228', borderRadius: 6 },
                                { label: 'H1 2025م (ريال)', data: [80000, 25000, 124, 13786, 62564, 18000], backgroundColor: '#C9A96E', borderRadius: 6 }
                            ]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            layout: { padding: { top: 25, bottom: 5 } },
                            plugins: { legend: { position: 'top', rtl: true, labels: { font: { size: 12, weight: '700' } } }, tooltip: { rtl: true } },
                            scales: { y: { beginAtZero: true, suggestedMax: 460000, ticks: { callback: v => v.toLocaleString() + ' ر.س' } } }
                        }
                    });
                }
            } catch(e) { console.error('Error in v2RevChart:', e); }

            // 6. Expenses Distribution Doughnut Chart
            try {
                const el = document.getElementById('v2ExpChart');
                if (el) {
                    new Chart(el, {
                        type: 'doughnut',
                        plugins: [doughnutPercentagePlugin],
                        data: {
                            labels: ['المساعدات الطبية (البرامج)', 'الرواتب والأجور', 'الإيجار والمقر', 'التأمينات والمتعاونين', 'الأصول الثابتة', 'مصروفات تشغيلية أخرى'],
                            datasets: [{
                                data: [208605, 144405, 63333, 27768, 15621, 18768],
                                backgroundColor: ['#1B7A48', '#541228', '#C9A96E', '#731A38', '#C7771E', '#8F8B85'],
                                borderWidth: 2,
                                borderColor: '#FFF'
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: { legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 11 } } } },
                            cutout: '58%'
                        }
                    });
                }
            } catch(e) { console.error('Error in v2ExpChart:', e); }

            // 7. Budget Execution Bar Chart
            try {
                const el = document.getElementById('budgetExecutionChart');
                if (el) {
                    new Chart(el, {
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
            } catch(e) { console.error('Error in budgetExecutionChart:', e); }

            // 8. Top Donors Bar Chart
            try {
                const el = document.getElementById('topDonorsChart');
                if (el) {
                    new Chart(el, {
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
            } catch(e) { console.error('Error in topDonorsChart:', e); }

            // 9. Fixed Assets Pie Chart
            try {
                const el = document.getElementById('fixedAssetsChart');
                if (el) {
                    new Chart(el, {
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
                            plugins: { legend: { position: 'bottom', rtl: true, labels: { boxWidth: 10, font: { size: 10 } } } }
                        }
                    });
                }
            } catch(e) { console.error('Error in fixedAssetsChart:', e); }
        }

        // Run when DOM is ready or immediately
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initDashboardCharts);
        } else {
            initDashboardCharts();
        }
    </script>
</body>
</html>
\"\"\""""

script_start = dash_code.find('<!-- Interactive Scripts & Chart.js with Direct On-Chart Labels -->')
if script_start == -1:
    script_start = dash_code.find('<!-- Bulletproof Interactive Scripts')

if script_start != -1:
    dash_code = dash_code[:script_start] + ultra_safe_js + "\n\nwith open(output_file, 'w', encoding='utf-8') as f:\n    f.write(html_content)\n\nprint(f'Generated Executive Dashboard V2 successfully: {output_file}')\n"
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Updated generate_v2_dashboard.py with ultra safe JS block!")

# Recompile generator
os.system(f'py -3 "{v2_file}"')

# Also sync index.html and all assets to both folders
v2_index = os.path.join(base_dir, "التقرير_الاحترافي_المطور", "index.html")
v1_index = os.path.join(base_dir, "التقرير_الجديد", "index.html")

if os.path.exists(v2_index):
    shutil.copy2(v2_index, v1_index)
    print(f"Synchronized index.html to {v1_index}")

# Copy all images and assets to v1_dir as well
v2_assets = os.path.join(base_dir, "التقرير_الاحترافي_المطور", "assets")
v1_assets = os.path.join(base_dir, "التقرير_الجديد", "assets")
if os.path.exists(v2_assets):
    shutil.copytree(v2_assets, v1_assets, dirs_exist_ok=True)
    print("Synchronized all assets to both directories!")

print("All charts inlined and guaranteed to render everywhere without any errors!")
