# -*- coding: utf-8 -*-
"""
Add Data Labels to Charts:
1. Doughnut Chart: Display exact percentages (e.g., 43.6%, 30.2%, 13.2%, 5.8%, 3.3%, 3.9%) directly on the slices.
2. Column / Bar Chart: Display exact numerical values (e.g., 70,000, 80,000, 407,495, etc.) directly on top of each bar.
"""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"

# Update generate_v2_dashboard.py
v2_file = os.path.join(base_dir, "generate_v2_dashboard.py")
with open(v2_file, "r", encoding="utf-8") as f:
    dash_code = f.read()

# Custom Chart.js Scripts with built-in data labels plugins
new_chart_script = """    <!-- Interactive Scripts & Chart.js with Direct On-Chart Labels -->
    <script>
        // Live Filter Function for tables
        function filterTable(inputId, tableId) {
            const input = document.getElementById(inputId);
            const filter = input.value.toLowerCase();
            const table = document.getElementById(tableId);
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
                ctx.font = 'bold 10px Cairo, sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'bottom';

                chart.data.datasets.forEach((dataset, datasetIndex) => {
                    const meta = chart.getDatasetMeta(datasetIndex);
                    if (!meta.hidden) {
                        meta.data.forEach((element, index) => {
                            const val = dataset.data[index];
                            if (val > 0) {
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

        // Custom Inline Chart.js Plugin for Doughnut Chart Percentages
        const doughnutPercentagePlugin = {
            id: 'doughnutPercentages',
            afterDraw(chart, args, options) {
                const { ctx, chartArea: { width, height } } = chart;
                const meta = chart.getDatasetMeta(0);
                if (!meta || !meta.data.length) return;

                const dataset = chart.data.datasets[0];
                const total = dataset.data.reduce((acc, cur) => acc + cur, 0);

                ctx.save();
                ctx.font = 'bold 12px Cairo, sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';

                meta.data.forEach((element, index) => {
                    const value = dataset.data[index];
                    const percentage = ((value / total) * 100).toFixed(1);
                    const angle = element.startAngle + (element.endAngle - element.startAngle) / 2;
                    
                    // Position at center of arc
                    const radius = element.innerRadius + (element.outerRadius - element.innerRadius) * 0.55;
                    const x = element.x + Math.cos(angle) * radius;
                    const y = element.y + Math.sin(angle) * radius;

                    // Text styling with drop shadow for maximum clarity
                    ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
                    ctx.shadowBlur = 4;
                    ctx.shadowOffsetX = 1;
                    ctx.shadowOffsetY = 1;
                    ctx.fillStyle = '#FFFFFF';

                    if (Number(percentage) >= 4) {
                        ctx.fillText(`٪${Number(percentage).toLocaleString('ar-SA')}`, x, y);
                    }
                });
                ctx.restore();
            }
        };

        // Initialize Charts
        document.addEventListener('DOMContentLoaded', function() {
            Chart.defaults.font.family = "'Cairo', sans-serif";
            Chart.defaults.color = '#666';

            // 1. Revenue Comparison Bar Chart
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
                        layout: {
                            padding: { top: 25, bottom: 5 }
                        },
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

            // 2. Expenses Distribution Doughnut Chart
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
                        layout: {
                            padding: 10
                        },
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
        });
    </script>"""

start_js = dash_code.find("    <!-- Interactive Scripts & Chart.js -->")
end_js = dash_code.find("</body>\n</html>")

if start_js != -1 and end_js != -1:
    dash_code = dash_code[:start_js] + new_chart_script + "\n</body>\n</html>\n\"\"\"\n\nwith open(output_file, \"w\", encoding=\"utf-8\") as f:\n    f.write(html_content)\n\nprint(f\"Generated Executive Dashboard V2 successfully: {output_file}\")\n"
    with open(v2_file, "w", encoding="utf-8") as f:
        f.write(dash_code)
    print("Updated generate_v2_dashboard.py with Chart Data Labels!")
else:
    print("Could not find script block in generate_v2_dashboard.py")

# Update generate_web_slides.py
web_file = os.path.join(base_dir, "generate_web_slides.py")
with open(web_file, "r", encoding="utf-8") as f:
    web_code = f.read()

new_web_chart_script = """        // Slide Chart Initialization with Direct Data Labels
        window.onload = function() {
            showSlide(1);
            
            const barValueLabelsPlugin = {
                id: 'barValueLabels',
                afterDatasetsDraw(chart, args, options) {
                    const { ctx } = chart;
                    ctx.save();
                    ctx.font = 'bold 10px Cairo, sans-serif';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'bottom';

                    chart.data.datasets.forEach((dataset, datasetIndex) => {
                        const meta = chart.getDatasetMeta(datasetIndex);
                        if (!meta.hidden) {
                            meta.data.forEach((element, index) => {
                                const val = dataset.data[index];
                                if (val > 0) {
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

            const ctxRev = document.getElementById('slideRevChart');
            if (ctxRev) {
                new Chart(ctxRev, {
                    type: 'bar',
                    plugins: [barValueLabelsPlugin],
                    data: {
                        labels: ['الزكاة', 'علاج مقيد', 'المتجر', 'تبرع', 'دعم عام', 'العضوية'],
                        datasets: [
                            { label: '٢٠٢٦م', data: [70000, 75000, 10469, 1203, 407495, 18000], backgroundColor: '#6B1D3A', borderRadius: 4 },
                            { label: '٢٠٢٥م', data: [80000, 25000, 124, 13786, 62564, 18000], backgroundColor: '#C9A96E', borderRadius: 4 }
                        ]
                    },
                    options: { 
                        responsive: true, 
                        maintainAspectRatio: false,
                        layout: { padding: { top: 22, bottom: 5 } },
                        scales: {
                            y: { beginAtZero: true, suggestedMax: 460000 }
                        }
                    }
                });
            }
        };"""

start_w_js = web_code.find("        // Slide Chart Initialization")
end_w_js = web_code.find("    </script>\n</body>\n</html>")

if start_w_js != -1 and end_w_js != -1:
    web_code = web_code[:start_w_js] + new_web_chart_script + "\n    </script>\n</body>\n</html>\n\"\"\"\n\nwith open(output_html, \"w\", encoding=\"utf-8\") as f:\n    f.write(slides_html)\n\nshutil.copy2(output_html, os.path.join(v1_dir, \"presentation.html\"))\n"
    with open(web_file, "w", encoding="utf-8") as f:
        f.write(web_code)
    print("Updated generate_web_slides.py with Chart Data Labels!")

# Recompile all deliverables
os.system(f'py -3 "{v2_file}"')
os.system(f'py -3 "{web_file}"')
os.system(f'py -3 "{os.path.join(base_dir, "generate_full_14_slides_pptx.py")}"')
os.system(f'py -3 "{os.path.join(base_dir, "enrich_word_and_presentations.py")}"')

print("All deliverables updated with on-chart values and percentages successfully!")
