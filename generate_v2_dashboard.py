# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "التقرير_الاحترافي_المطور", "index.html")

html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>التقرير النصف سنوي التنفيذي ٢٠٢٦م | جمعية طبيبي الأهلية</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <!-- FontAwesome 6.5 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Chart.js 4 -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        :root {
            --primary: #541228;
            --primary-light: #731A38;
            --primary-dark: #380B1B;
            --secondary: #C9A96E;
            --secondary-light: #E2D2B0;
            --secondary-dark: #9E7F43;
            --bg-body: #FAF8F5;
            --bg-surface: #FFFFFF;
            --bg-subtle: #F3EFE8;
            --text-title: #1E1A1C;
            --text-body: #3D383A;
            --text-muted: #736C6F;
            --success: #1B7A48;
            --success-bg: #E8F6EF;
            --warning: #C7771E;
            --warning-bg: #FDF3E7;
            --danger: #B83227;
            --danger-bg: #FCECEB;
            --info: #1A6E9E;
            --info-bg: #EAF4FA;
            --border-light: rgba(84, 18, 40, 0.08);
            --border-gold: rgba(201, 169, 110, 0.35);
            --radius-xl: 24px;
            --radius-lg: 16px;
            --radius-md: 12px;
            --radius-sm: 8px;
            --shadow-subtle: 0 4px 20px rgba(84, 18, 40, 0.04);
            --shadow-card: 0 10px 30px rgba(84, 18, 40, 0.06);
            --shadow-hover: 0 20px 45px rgba(84, 18, 40, 0.12);
            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Cairo', 'Tajawal', sans-serif;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-body);
            color: var(--text-body);
            line-height: 1.8;
            font-size: 16px;
            overflow-x: hidden;
        }

        /* Top Executive Bar */
        .exec-nav-wrapper {
            position: fixed;
            top: 15px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: center;
            z-index: 1000;
            pointer-events: none;
        }

        .exec-nav {
            pointer-events: auto;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: 10px 28px;
            border-radius: 50px;
            box-shadow: 0 10px 35px rgba(84, 18, 40, 0.12);
            border: 1px solid var(--border-gold);
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .exec-brand {
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: var(--primary);
            font-weight: 800;
            font-size: 1.15rem;
            padding-left: 16px;
            border-left: 1.5px solid var(--border-light);
        }

        .exec-brand i {
            color: var(--secondary);
            font-size: 1.3rem;
        }

        .exec-links {
            display: flex;
            gap: 10px;
            list-style: none;
        }

        .exec-links a {
            text-decoration: none;
            color: var(--text-body);
            font-weight: 600;
            font-size: 0.92rem;
            padding: 6px 14px;
            border-radius: 30px;
            transition: var(--transition);
        }

        .exec-links a:hover, .exec-links a.active {
            background: var(--primary);
            color: #FFF;
        }

        .btn-action {
            background: linear-gradient(135deg, var(--secondary), var(--secondary-dark));
            color: #FFF;
            border: none;
            padding: 7px 18px;
            border-radius: 30px;
            font-weight: 700;
            font-size: 0.85rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: var(--transition);
        }

        .btn-action:hover {
            transform: scale(1.04);
            box-shadow: 0 4px 15px rgba(201, 169, 110, 0.4);
        }

        /* Container */
        .container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 90px 30px;
        }

        .section-intro {
            text-align: center;
            margin-bottom: 50px;
        }

        .eyebrow-pill {
            display: inline-block;
            background: rgba(201, 169, 110, 0.14);
            color: var(--secondary-dark);
            font-weight: 800;
            font-size: 0.9rem;
            padding: 4px 18px;
            border-radius: 30px;
            margin-bottom: 12px;
            letter-spacing: 0.5px;
        }

        .section-headline {
            font-size: 2.6rem;
            font-weight: 900;
            color: var(--primary);
            margin-bottom: 12px;
        }

        .section-subtext {
            color: var(--text-muted);
            font-size: 1.15rem;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
        }

        /* Hero / Cover Section (Executive Hook) */
        .hero-banner {
            min-height: 100vh;
            background: linear-gradient(145deg, #2E0B17 0%, #541228 45%, #1F0710 100%);
            color: #FFF;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 120px 25px 80px;
            overflow: hidden;
        }

        .hero-pattern-layer {
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(201, 169, 110, 0.18) 1px, transparent 1px);
            background-size: 32px 32px;
            opacity: 0.6;
        }

        .hero-inner {
            position: relative;
            z-index: 2;
            max-width: 1100px;
        }

        .hero-license-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-gold);
            padding: 6px 20px;
            border-radius: 30px;
            font-size: 0.95rem;
            color: var(--secondary-light);
            margin-bottom: 25px;
        }

        .hero-title-main {
            font-size: 4rem;
            font-weight: 900;
            line-height: 1.2;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #FFFFFF 40%, var(--secondary-light) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-story-hook {
            font-size: 1.45rem;
            color: var(--secondary-light);
            max-width: 850px;
            margin: 0 auto 35px;
            line-height: 1.7;
            font-weight: 500;
        }

        /* Executive Takeaways Bento in Hero */
        .hero-bento-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 40px;
            text-align: right;
        }

        .hero-bento-card {
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(201, 169, 110, 0.25);
            border-radius: var(--radius-lg);
            padding: 22px;
            transition: var(--transition);
        }

        .hero-bento-card:hover {
            background: rgba(255, 255, 255, 0.12);
            transform: translateY(-5px);
            border-color: var(--secondary);
        }

        .hero-bento-card .bento-label {
            font-size: 0.88rem;
            color: rgba(255, 255, 255, 0.75);
            margin-bottom: 4px;
        }

        .hero-bento-card .bento-val {
            font-size: 2.2rem;
            font-weight: 900;
            color: #FFF;
            margin-bottom: 6px;
        }

        .hero-bento-card .bento-badge {
            font-size: 0.8rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 12px;
            display: inline-block;
        }

        /* Cards & Double Bezel */
        .exec-card {
            background: var(--bg-surface);
            border-radius: var(--radius-xl);
            padding: 32px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-light);
            position: relative;
            transition: var(--transition);
        }

        .exec-card:hover {
            box-shadow: var(--shadow-hover);
            transform: translateY(-5px);
            border-color: var(--border-gold);
        }

        /* Grid Utilities */
        .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px; }
        .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
        .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }

        /* KPI Card System (SMART Level) */
        .kpi-card-v2 {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: #FFFFFF;
            border-radius: var(--radius-lg);
            padding: 26px;
            box-shadow: var(--shadow-card);
            border: 1px solid rgba(84, 18, 40, 0.06);
            transition: var(--transition);
        }

        .kpi-card-v2:hover {
            transform: translateY(-6px);
            box-shadow: var(--shadow-hover);
            border-color: var(--secondary);
        }

        .kpi-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 12px;
        }

        .kpi-title {
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-muted);
        }

        .kpi-icon {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
        }

        .kpi-num {
            font-size: 2.3rem;
            font-weight: 900;
            color: var(--primary);
            line-height: 1.2;
            margin-bottom: 10px;
        }

        .kpi-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid var(--border-light);
            padding-top: 12px;
            font-size: 0.88rem;
            color: var(--text-muted);
        }

        .tag-pill {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 3px 10px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.82rem;
        }

        .tag-success { background: var(--success-bg); color: var(--success); }
        .tag-warning { background: var(--warning-bg); color: var(--warning); }
        .tag-danger { background: var(--danger-bg); color: var(--danger); }
        .tag-info { background: var(--info-bg); color: var(--info); }

        /* Tables & Search */
        .table-card {
            background: #FFF;
            border-radius: var(--radius-xl);
            padding: 32px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-light);
            margin-bottom: 40px;
            overflow-x: auto;
        }

        .table-toolbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            gap: 15px;
            flex-wrap: wrap;
        }

        .search-input-wrap {
            position: relative;
            min-width: 280px;
        }

        .search-input-wrap input {
            width: 100%;
            padding: 10px 40px 10px 16px;
            border-radius: 30px;
            border: 1.5px solid #E5E0D8;
            font-size: 0.95rem;
            outline: none;
            transition: var(--transition);
        }

        .search-input-wrap input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 10px rgba(84, 18, 40, 0.1);
        }

        .search-input-wrap i {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
        }

        .custom-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            text-align: right;
        }

        .custom-table th {
            background: #F5F2EB;
            color: var(--primary);
            font-weight: 800;
            font-size: 0.95rem;
            padding: 16px 20px;
            border-bottom: 2px solid rgba(84, 18, 40, 0.12);
        }

        .custom-table th:first-child { border-top-right-radius: var(--radius-sm); }
        .custom-table th:last-child { border-top-left-radius: var(--radius-sm); }

        .custom-table td {
            padding: 14px 20px;
            border-bottom: 1px solid #ECE8E0;
            color: var(--text-body);
            font-size: 0.95rem;
        }

        .custom-table tr:hover td {
            background: rgba(201, 169, 110, 0.04);
        }

        .custom-table .total-row td {
            background: #F6F3EC;
            font-weight: 800;
            color: var(--primary);
            font-size: 1.05rem;
            border-top: 2px solid rgba(84, 18, 40, 0.2);
        }

        /* Progress Bars */
        .progress-block {
            margin-bottom: 20px;
        }

        .progress-meta {
            display: flex;
            justify-content: space-between;
            font-weight: 700;
            font-size: 0.95rem;
            margin-bottom: 6px;
        }

        .progress-track {
            height: 12px;
            background: #EBE7DF;
            border-radius: 20px;
            overflow: hidden;
        }

        .progress-bar-inner {
            height: 100%;
            border-radius: 20px;
            background: linear-gradient(90deg, var(--secondary), var(--primary));
            transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* Patient Cards */
        .patient-box {
            border-right: 4px solid var(--secondary);
            position: relative;
        }

        .patient-cost-tag {
            position: absolute;
            top: 24px;
            left: 24px;
            background: rgba(84, 18, 40, 0.08);
            color: var(--primary);
            padding: 4px 14px;
            border-radius: 20px;
            font-weight: 800;
            font-size: 1.1rem;
        }

        /* Partner Cards */
        .partner-box {
            text-align: center;
            padding: 26px 18px;
            border: 1px solid var(--border-light);
            border-radius: var(--radius-md);
            background: #FFF;
            transition: var(--transition);
        }

        .partner-box:hover {
            border-color: var(--secondary);
            transform: translateY(-6px);
            box-shadow: var(--shadow-card);
        }

        .partner-box i {
            font-size: 2.4rem;
            color: var(--primary);
            margin-bottom: 12px;
        }

        /* Strategic Roadmap Steps */
        .roadmap-card {
            background: linear-gradient(145deg, #4A1226, #2E0B17);
            color: #FFF;
            border-radius: var(--radius-lg);
            padding: 30px;
            border: 1px solid var(--border-gold);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .roadmap-num {
            font-size: 2rem;
            font-weight: 900;
            color: var(--secondary);
            margin-bottom: 8px;
        }

        /* Charts */
        .chart-box {
            position: relative;
            height: 350px;
            width: 100%;
            margin-top: 15px;
        }

        /* Royal Cards */
        .royal-card-v2 {
            background: linear-gradient(145deg, #380B1B, #200610);
            color: #FFF;
            border-radius: var(--radius-xl);
            padding: 35px 25px;
            text-align: center;
            border: 1px solid rgba(201, 169, 110, 0.3);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .royal-img-wrap {
            width: 125px;
            height: 125px;
            border-radius: 50%;
            border: 3px solid var(--secondary);
            box-shadow: 0 8px 25px rgba(201, 169, 110, 0.35);
            margin: 0 auto 16px;
            overflow: hidden;
            background: #FFF;
        }

        .royal-portrait {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top center;
        }
            justify-content: center;
            font-size: 2.4rem;
            color: var(--secondary);
            margin: 0 auto 15px;
            background: rgba(255, 255, 255, 0.05);
        }

        /* Footer */
        .footer-v2 {
            background: linear-gradient(145deg, #2E0B17 0%, #541228 45%, #1F0710 100%);
            border-top: 3px solid var(--secondary);
            color: #FFF;
            padding: 70px 30px 35px;
            position: relative;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 40px;
            max-width: 1440px;
            margin: 0 auto 50px;
        }

        @media (max-width: 1100px) {
            .grid-4, .hero-bento-grid { grid-template-columns: repeat(2, 1fr); }
            .grid-3 { grid-template-columns: repeat(2, 1fr); }
            .hero-title-main { font-size: 3rem; }
        }

        @media (max-width: 768px) {
            .exec-links { display: none; }
            .grid-2, .grid-3, .grid-4, .hero-bento-grid, .footer-grid { grid-template-columns: 1fr; }
            .hero-title-main { font-size: 2.2rem; }
            .container { padding: 60px 15px; }
        }

        /* PDF Export & Print Stylesheet */
        @media print {
            /* Hide ONLY navbar and search controls */
            .exec-nav-wrapper,
            .exec-nav,
            .search-input-wrap,
            .btn-action {
                display: none !important;
                visibility: hidden !important;
            }

            /* Preserve exact graphics, backgrounds, and colors */
            * {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
                color-adjust: exact !important;
            }

            body {
                background: #FAF8F5 !important;
                color: #1E1A1C !important;
                font-size: 11pt !important;
                margin: 0 !important;
                padding: 0 !important;
            }

            .hero-banner {
                min-height: auto !important;
                padding: 60px 30px !important;
                background: linear-gradient(145deg, #2E0B17 0%, #541228 45%, #1F0710 100%) !important;
                -webkit-print-color-adjust: exact !important;
                page-break-after: always !important;
                break-after: page !important;
            }

            .container {
                max-width: 100% !important;
                padding: 30px 15px !important;
                margin: 0 auto !important;
            }

            .exec-card, .table-card, .kpi-card-v2, .royal-card-v2, .roadmap-card, .partner-box {
                box-shadow: none !important;
                border: 1px solid #D8D2C6 !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }

            .grid-2, .grid-3, .grid-4, .hero-bento-grid {
                display: grid !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }

            .table-card {
                overflow: visible !important;
            }

            table {
                page-break-inside: auto !important;
                width: 100% !important;
            }

            tr {
                page-break-inside: avoid !important;
                page-break-after: auto !important;
            }

            thead {
                display: table-header-group !important;
            }

            .chart-box {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }

            @page {
                size: A4 landscape;
                margin: 0.8cm 0.8cm;
            }
        }
    </style>
</head>
<body>

    <!-- Floating Executive Navigation -->
    <div class="exec-nav-wrapper">
        <nav class="exec-nav">
            <a href="#hero" class="exec-brand">
                <i class="fas fa-heart-pulse"></i>
                <span>طبيبي ٢٠٢٦م</span>
            </a>
            <ul class="exec-links">
                <li><a href="#narrative">القصة والأثر</a></li>
                <li><a href="#kpi-dashboard">مؤشرات الأداء</a></li>
                <li><a href="#strategic-audit">المطابقة الاستراتيجية</a></li>
                <li><a href="#financials">الأداء المالي</a></li>
                <li><a href="#clinical">البرامج الطبية</a></li>
                <li><a href="#partners">الشراكات</a></li>
                <li><a href="#governance">الحوكمة وخارطة الطريق</a></li>
                <li><a href="#master-appendices">الملاحق الكاملة</a></li>
            </ul>
            <button class="btn-action" onclick="window.print()">
                <i class="fas fa-file-pdf"></i>
                <span>تصدير PDF</span>
            </button>
        </nav>
    </div>

    <!-- Section 1: Executive Narrative Hook (Hero) -->
    <header id="hero" class="hero-banner">
        <div class="hero-pattern-layer"></div>
        <div class="hero-inner">
            <div class="hero-license-badge">
                <i class="fas fa-certificate" style="color:var(--secondary)"></i>
                <span>ترخيص المركز الوطني لتنمية القطاع غير الربحي رقم: (١٠٠٠٧٣٠٧٠٠) | المدينة المنورة</span>
            </div>
            
            <h1 class="hero-title-main">التقرير النصف سنوي الشامل</h1>
            <p class="hero-story-hook">
                «٦ أشهر من التحول المؤسسي والأثر الصحي المستدام في طيبة الطيبة: مضاعفة المساعدات العلاجية بنسبة +٩٤٣٪ ونمو الإيرادات بنسبة +١٩٢٪»
            </p>

            <div style="font-size:1.5rem; font-weight:800; color:var(--secondary); letter-spacing:2px; margin-bottom:30px;">
                ثـقـة  •  أثــر  •  اسـتـدامـة
            </div>

            <!-- Executive Bento Grid -->
            <div class="hero-bento-grid">
                <div class="hero-bento-card">
                    <div class="bento-label">إجمالي الإيرادات المحققة</div>
                    <div class="bento-val">٥٨٢,١٦٧ <small style="font-size:1rem;">ر.س</small></div>
                    <span class="bento-badge" style="background:var(--success-bg); color:var(--success);">↑ نمو +١٩٢٪</span>
                </div>

                <div class="hero-bento-card">
                    <div class="bento-label">المساعدات الطبية المباشرة</div>
                    <div class="bento-val">٢٠٨,٦٠٥ <small style="font-size:1rem;">ر.س</small></div>
                    <span class="bento-badge" style="background:var(--success-bg); color:var(--success);">↑ نمو +٩٤٣٪</span>
                </div>

                <div class="hero-bento-card">
                    <div class="bento-label">الأرصدة المصرفية المتوفرة</div>
                    <div class="bento-val">١,٠٠١,٧٥٤ <small style="font-size:1rem;">ر.س</small></div>
                    <span class="bento-badge" style="background:var(--info-bg); color:var(--info);">تغطية احتياطي ١٢ شهراً</span>
                </div>

                <div class="hero-bento-card">
                    <div class="bento-label">نسبة التوطين وتحسن المرضى</div>
                    <div class="bento-val">١٠٠٪</div>
                    <span class="bento-badge" style="background:var(--success-bg); color:var(--success);">كفاءة تشغيلية كاملة</span>
                </div>
            </div>
        </div>
    </header>

    <!-- Section 2: Leadership & Vision (Setup & Governance) -->
    <section class="container" id="narrative" style="padding-top:70px;">
        <div class="section-intro">
            <span class="eyebrow-pill">الرؤية والتمكين الوطني</span>
            <h2 class="section-headline">القيادة الرشيدة ومجلس الإدارة</h2>
            <p class="section-subtext">تكامل الجهود لتحقيق مستهدفات رؤية المملكة ٢٠٣٠ في ترسيخ مساهمة القطاع الصحي غير الربحي في جودة الحياة</p>
        </div>

        <div class="grid-3" style="margin-bottom:40px;">
            <!-- Crown Prince (Right) -->
            <div class="royal-card-v2">
                <div>
                    <div class="royal-img-wrap">
                        <img src="assets/images/crown_prince.jpg" alt="صاحب السمو الملكي الأمير محمد بن سلمان" class="royal-portrait">
                    </div>
                    <h3 style="color:var(--secondary); font-size:1.25rem;">صاحب السمو الملكي</h3>
                    <p style="font-size:0.95rem; opacity:0.8; margin-bottom:15px;">الأمير محمد بن سلمان بن عبدالعزيز</p>
                </div>
                <p style="font-style:italic; font-size:0.95rem; line-height:1.8; color:#F0EBE1; border-right:3px solid var(--secondary); padding-right:12px; text-align:justify;">
                    «نهدف للوصول إلى قطاع غير ربحي مهم، مبادر وداعم ومؤثر في التعليم والصحة والثقافة والمجالات البحثية، وسنعتمد عليه بشكل رئيسي.»
                </p>
            </div>

            <!-- King Salman (Center / Middle) -->
            <div class="royal-card-v2" style="border: 1.5px solid var(--secondary); box-shadow: 0 10px 30px rgba(201, 169, 110, 0.2);">
                <div>
                    <div class="royal-img-wrap" style="width:135px; height:135px; border-width:3.5px;">
                        <img src="assets/images/king_salman.jpg" alt="خادم الحرمين الشريفين الملك سلمان بن عبدالعزيز" class="royal-portrait">
                    </div>
                    <h3 style="color:var(--secondary); font-size:1.3rem;">خادم الحرمين الشريفين</h3>
                    <p style="font-size:0.95rem; opacity:0.9; margin-bottom:15px; font-weight:700;">الملك سلمان بن عبدالعزيز آل سعود</p>
                </div>
                <p style="font-style:italic; font-size:0.95rem; line-height:1.8; color:#F0EBE1; border-right:3px solid var(--secondary); padding-right:12px; text-align:justify;">
                    «ما يميز هذه البلاد هو حرص قادتها على الخير والتشجيع عليه، وما نراه من مؤسسات خيرية في مختلف المجالات… إلا جانبًا من الجوانب المشرقة لبلادنا.»
                </p>
            </div>

            <!-- Prince Salman bin Sultan (Left) -->
            <div class="royal-card-v2">
                <div>
                    <div class="royal-img-wrap">
                        <img src="assets/images/prince_salman.jpg" alt="صاحب السمو الملكي الأمير سلمان بن سلطان" class="royal-portrait">
                    </div>
                    <h3 style="color:var(--secondary); font-size:1.25rem;">صاحب السمو الملكي</h3>
                    <p style="font-size:0.95rem; opacity:0.8; margin-bottom:15px;">الأمير سلمان بن سلطان بن عبدالعزيز</p>
                </div>
                <p style="font-style:italic; font-size:0.95rem; line-height:1.8; color:#F0EBE1; border-right:3px solid var(--secondary); padding-right:12px; text-align:justify;">
                    «نسعد بالإنجازات التي حققتها الجمعيات الأهلية بالمنطقة باعتبارها شريكًا استراتيجيًا للقطاعين العام والخاص في تحسين جودة الحياة وتعزيز الاستقرار.»
                </p>
            </div>
        </div>

        <!-- Chairman Message Box -->
        <div class="exec-card" style="padding:45px;">
            <div class="grid-2" style="align-items:center;">
                <div>
                    <span class="eyebrow-pill">كلمة رئيس مجلس الإدارة</span>
                    <h3 style="color:var(--primary); font-size:1.8rem; margin-bottom:15px;">رسالة القيادة المؤسسية</h3>
                    <p style="font-size:1.05rem; line-height:2.0; color:var(--text-body); text-align:justify; margin-bottom:15px;">
                        «يسرني أن أضع بين أيديكم التقرير النصف سنوي لجمعية طبيبي الأهلية، والذي يعكس ما تحقق خلال النصف الأول من عام ٢٠٢٦م من نمو مالي وتشغيلي، وتطور في البنية المؤسسية والحوكمة، وتوسع في الخدمات المقدمة للمستفيدين المرضى في طيبة الطيبة. وننظر إلى هذا التقرير بوصفه أداة للتقييم والتطوير المستمر بما يرفع الأثر الصحي والاجتماعي المحقق.»
                    </p>
                    <div style="font-weight:800; color:var(--primary); font-size:1.15rem;">
                        أ.د. منصور محمد النزهة <br>
                        <span style="font-size:0.95rem; color:var(--text-muted); font-weight:600;">رئيس مجلس الإدارة | جمعية طبيبي الأهلية</span>
                    </div>
                </div>
                <div style="background:var(--bg-subtle); padding:30px; border-radius:var(--radius-lg); border-right:4px solid var(--primary);">
                    <h4 style="color:var(--primary); font-size:1.2rem; margin-bottom:12px;"><i class="fas fa-users-gear" style="color:var(--secondary); margin-left:8px;"></i> مجلس الإدارة (٩ أعضاء)</h4>
                    <p style="font-size:0.95rem; line-height:1.8; color:var(--text-body);">
                        يتشكل المجلس من ٩ أعضاء بخبرات قيادية وطبية وإدارية، يشرفون على لجان الحوكمة واللجنة التنفيذية ولجنة المساعدات الطبية، ويتابعون مع الإدارة التنفيذية برئاسة <strong>أ. بيان بن سعد المحمدي</strong> تنفيذ الخطط التشغيلية والموازنات المعتمدة.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Master KPI Dashboard (SMART Framework) -->
    <section class="container" id="kpi-dashboard" style="background:#F4EFE6; border-radius:var(--radius-xl); margin-top:30px; margin-bottom:60px;">
        <div class="section-intro">
            <span class="eyebrow-pill">لوحة القيادة التنفيذية (KPI Matrix)</span>
            <h2 class="section-headline">مؤشرات الأداء الرئيسية الشاملة</h2>
            <p class="section-subtext">منظومة قياس الأداء الاستراتيجي والتشغيلي للنصف الأول ٢٠٢٦م مدعمة بمؤشرات المقارنة والاتجاهات</p>
        </div>

        <!-- Row 1: Strategic & Financial KPIs -->
        <h3 style="color:var(--primary); font-size:1.3rem; margin-bottom:15px; display:flex; align-items:center; gap:8px;">
            <i class="fas fa-sack-dollar" style="color:var(--secondary);"></i>
            <span>المؤشرات المالية والاستدامة</span>
        </h3>
        <div class="grid-4" style="margin-bottom:30px;">
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
        </div>

        <!-- Row 2: Medical Impact & Satisfaction KPIs -->
        <h3 style="color:var(--primary); font-size:1.3rem; margin-bottom:15px; display:flex; align-items:center; gap:8px;">
            <i class="fas fa-stethoscope" style="color:var(--secondary);"></i>
            <span>مؤشرات الأثر الطبي ورضا المستفيدين</span>
        </h3>
        <div class="grid-4" style="margin-bottom:30px;">
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
        </div>

        <!-- Row 3: Human Capital & Governance KPIs -->
        <h3 style="color:var(--primary); font-size:1.3rem; margin-bottom:15px; display:flex; align-items:center; gap:8px;">
            <i class="fas fa-users-viewfinder" style="color:var(--secondary);"></i>
            <span>الموارد البشرية والحوكمة وتنمية الموارد</span>
        </h3>
        <div class="grid-4">
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
        </div>
    </section>

    
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


    <!-- Section 4: Deep Financial Architecture -->
    <section class="container" id="financials">
        <div class="section-intro">
            <span class="eyebrow-pill">التحليل المالي والشفافية</span>
            <h2 class="section-headline">الأداء المالي والموازنة التشغيلية</h2>
            <p class="section-subtext">مقارنة تفصيلية لمصادر الإيرادات، نسب تنفيذ الموازنة التقديرية، وهيكل المصروفات التشغيلية لعام ٢٠٢٦م</p>
        </div>

        <!-- Revenue Table -->
        <div class="table-card">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.3rem;"><i class="fas fa-chart-line" style="color:var(--secondary); margin-left:8px;"></i> مقارنة مصادر الدخل (H1 2026 vs H1 2025)</h3>
                    <p style="font-size:0.9rem; color:var(--text-muted);">نمو شامل في معظم قنوات الدخل مع تعويض توقف منصة تبرع بالمتجر الإلكتروني وكبار المانحين</p>
                </div>
                <span class="tag-pill tag-success" style="font-size:1rem; padding:6px 16px;">صافي نمو الإيرادات: +١٩٢٪</span>
            </div>

            <table class="custom-table">
                <thead>
                    <tr>
                        <th>بند الإيراد</th>
                        <th>H1 2026 (ريال)</th>
                        <th>H1 2025 (ريال)</th>
                        <th>التغير بالقيمة (ريال)</th>
                        <th>نسبة النمو</th>
                        <th>التحليل والدلالة المالية</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>أموال الزكاة المقيدة</strong></td>
                        <td>٧٠,٠٠٠</td>
                        <td>٨٠,٠٠٠</td>
                        <td style="color:var(--danger); font-weight:700;">-١٠,٠٠٠</td>
                        <td><span class="tag-pill tag-danger">-١٣٪</span></td>
                        <td>مصروفة بالكامل لمصارف المرضى المحتاجين</td>
                    </tr>
                    <tr>
                        <td><strong>علاج مقيد (مساعدات طبية)</strong></td>
                        <td>٧٥,٠٠٠</td>
                        <td>٢٥,٠٠٠</td>
                        <td style="color:var(--success); font-weight:700;">+٥٠,٠٠٠</td>
                        <td><span class="tag-pill tag-success">+٢٠٠٪</span></td>
                        <td>تضاعف الدعم المخصص للعمليات الجراحية المباشرة</td>
                    </tr>
                    <tr>
                        <td><strong>المتجر الإلكتروني</strong></td>
                        <td>١٠,٤٦٩</td>
                        <td>١٢٤</td>
                        <td style="color:var(--success); font-weight:700;">+١٠,٣٤٥</td>
                        <td><span class="tag-pill tag-success">+٨,٣٤٣٪</span></td>
                        <td>تفعيل حلول الدفع الرقمي والتسويق الإلكتروني</td>
                    </tr>
                    <tr>
                        <td><strong>منصة تبرع الوطنية</strong></td>
                        <td>١,٢٠٣</td>
                        <td>١٣,٧٨٦</td>
                        <td style="color:var(--warning); font-weight:700;">-١٢,٥٨٣</td>
                        <td><span class="tag-pill tag-warning">-٩١٪</span></td>
                        <td>التحول لمنصة إحسان الوطنية بعد تحديث منصة تبرع</td>
                    </tr>
                    <tr>
                        <td><strong>تبرعات ودعم عام</strong></td>
                        <td>٤٠٧,٤٩٥</td>
                        <td>٦٢,٥٦٤</td>
                        <td style="color:var(--success); font-weight:700;">+٣٤٤,٩٣١</td>
                        <td><span class="tag-pill tag-success">+٥٥١٪</span></td>
                        <td>دعم استثنائي من كبار المانحين والأوقاف الاستراتيجية</td>
                    </tr>
                    <tr>
                        <td><strong>اشتراكات العضوية</strong></td>
                        <td>١٨,٠٠٠</td>
                        <td>١٨,٠٠٠</td>
                        <td>٠</td>
                        <td><span class="tag-pill tag-info">٠٪</span></td>
                        <td>استقرار تحصيل اشتراكات أعضاء الجمعية العمومية</td>
                    </tr>
                    <tr class="total-row">
                        <td>الإجمالي العام المعتمد</td>
                        <td>٥٨٢,١٦٧</td>
                        <td>١٩٩,٤٧٤</td>
                        <td>+٣٨٢,٦٩٣</td>
                        <td>+١٩٢٪</td>
                        <td>المبلغ الدقيق: ٥٨٢,١٦٧.٥٢ ريال سعودي</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Budget & Liquidity Split -->
        <div class="grid-2">
            <!-- Budget Execution Trackers -->
            <div class="exec-card">
                <h3 style="color:var(--primary); font-size:1.3rem; margin-bottom:20px;"><i class="fas fa-bullseye" style="color:var(--secondary); margin-left:8px;"></i> نسب إنجاز بنود الموازنة التقديرية (٢٠٢٦م)</h3>
                
                <div class="progress-block">
                    <div class="progress-meta">
                        <span>التبرعات والدعم (الإيرادات)</span>
                        <span style="color:var(--primary);">٥٨٢,١٦٧ / ١,٥٢٧,٠٠٠ ريال (٤٠.٠٢٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-inner" style="width:40.02%;"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-meta">
                        <span>المساعدات العلاجية للمرضى</span>
                        <span style="color:var(--primary);">٢٠٨,٦٠٥ / ٧٥٠,٠٠٠ ريال (٢٧.٨١٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-inner" style="width:27.81%;"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-meta">
                        <span>الرواتب والأجور والكادر</span>
                        <span style="color:var(--primary);">١٤٤,٤٠٥ / ٤٧٢,٠٠٠ ريال (٣٠.٥٩٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-inner" style="width:30.59%;"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-meta">
                        <span>المصروفات التشغيلية والإيجار</span>
                        <span style="color:var(--warning);">١٠٩,٨٦٩ / ١٤٢,٣٠٠ ريال (٧٧.٢١٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-inner" style="width:77.21%; background:linear-gradient(90deg, #D9822B, #B83227);"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-meta">
                        <span>شراء الأصول والتجهيزات</span>
                        <span style="color:var(--danger);">١٥,٦٢١ / ١٩,٤٥٠ ريال (٨٠.٣١٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-inner" style="width:80.31%; background:linear-gradient(90deg, #C9A96E, #B83227);"></div></div>
                </div>

                <div style="background:var(--bg-subtle); padding:16px 20px; border-radius:var(--radius-md); margin-top:25px; display:flex; justify-content:space-between; align-items:center;">
                    <strong>إجمالي المنفذ الفعلي من الموازنة:</strong>
                    <span style="font-size:1.3rem; font-weight:900; color:var(--primary);">١,٠٦٠,٦٦٦ من ٢,٩٨١,٧٥٠ ريال (٣٥.٥٧٪)</span>
                </div>
            </div>

            <!-- Liquidity & Financial Position -->
            <div class="exec-card">
                <h3 style="color:var(--primary); font-size:1.3rem; margin-bottom:20px;"><i class="fas fa-building-columns" style="color:var(--secondary); margin-left:8px;"></i> المركز المالي وتوزيع السيولة النقدية</h3>
                
                <div style="background:linear-gradient(135deg, var(--primary), var(--primary-dark)); color:#FFF; padding:25px; border-radius:var(--radius-lg); margin-bottom:20px;">
                    <div style="font-size:0.95rem; opacity:0.85;">إجمالي الأرصدة المصرفية المتوفرة:</div>
                    <div style="font-size:2.5rem; font-weight:900; color:var(--secondary-light); margin:5px 0;">١,٠٠١,٧٥٤ <small style="font-size:1.2rem;">ر.س</small></div>
                    <div style="display:flex; justify-content:space-between; border-top:1px solid rgba(255,255,255,0.15); padding-top:12px; font-size:0.95rem;">
                        <span>البنك الأهلي السعودي: <strong>٩٣٠,٧٠٢ ريال</strong></span>
                        <span>مصرف الراجحي: <strong>٧١,٠٥٢ ريال</strong></span>
                    </div>
                </div>

                <div class="grid-2" style="gap:15px; margin-bottom:15px;">
                    <div style="background:var(--bg-subtle); padding:16px; border-radius:var(--radius-md); text-align:center;">
                        <div style="font-size:0.88rem; color:var(--text-muted);">الأموال المقيدة (مخصصة)</div>
                        <div style="font-size:1.4rem; font-weight:800; color:var(--primary);">٣٦٧,٠٩٣ ر.س</div>
                        <div style="font-size:0.8rem; color:var(--text-muted);">٣٦.٧٪ من السيولة</div>
                    </div>

                    <div style="background:var(--bg-subtle); padding:16px; border-radius:var(--radius-md); text-align:center;">
                        <div style="font-size:0.88rem; color:var(--text-muted);">الأموال غير المقيدة (عامة)</div>
                        <div style="font-size:1.4rem; font-weight:800; color:var(--success);">٦٣٤,٦٦١ ر.س</div>
                        <div style="font-size:0.8rem; color:var(--text-muted);">٦٣.٣٪ من السيولة</div>
                    </div>
                </div>

                <div style="padding:14px 18px; border-right:3px solid var(--secondary); background:rgba(201,169,110,0.08); border-radius:0 var(--radius-sm) var(--radius-sm) 0; font-size:0.92rem;">
                    <strong>صافي الأصول:</strong> ٩٧٢,٧١٣ ريال (رصيد بداية المدة ٨٦٤,٠٤٥ + إيراد ٥٨٢,١٦٧ - استخدامات ٤٧٣,٤٩٩ ريال).
                </div>
            </div>
        </div>

        <!-- Charts Container -->
        <div class="grid-2" style="margin-top:30px;">
            <div class="exec-card">
                <h4 style="color:var(--primary); font-size:1.15rem;"><i class="fas fa-chart-column" style="color:var(--secondary); margin-left:8px;"></i> نمو الإيرادات حسب القنوات (ريال)</h4>
                <div class="chart-box"><canvas id="v2RevChart"></canvas></div>
            </div>

            <div class="exec-card">
                <h4 style="color:var(--primary); font-size:1.15rem;"><i class="fas fa-chart-pie" style="color:var(--secondary); margin-left:8px;"></i> توزيع النفقات والاستخدامات الفعلية (H1 2026)</h4>
                <div class="chart-box"><canvas id="v2ExpChart"></canvas></div>
            </div>
        </div>

        <!-- Full 16 Operating Expenses Table -->
        <div class="table-card" style="margin-top:40px;">
            <div class="table-toolbar">
                <h3 style="color:var(--primary); font-size:1.3rem;"><i class="fas fa-file-lines" style="color:var(--secondary); margin-left:8px;"></i> البيان التفصيلي لكافة المصروفات التشغيلية (١٦ بنداً)</h3>
                <div class="search-input-wrap">
                    <i class="fas fa-search"></i>
                    <input type="text" id="expenseSearch" placeholder="بحث في بنود المصروفات..." onkeyup="filterTable('expenseSearch', 'expenseTable')">
                </div>
            </div>

            <table class="custom-table" id="expenseTable">
                <thead>
                    <tr>
                        <th>م</th>
                        <th>بند المصروف</th>
                        <th>H1 2026 (ريال)</th>
                        <th>H1 2025 (ريال)</th>
                        <th>التغير %</th>
                        <th>الوزن النسبي</th>
                        <th>البيان والتوجيه الإداري</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>١</td><td><strong>الرواتب الأساسية</strong></td><td>١٤٤,٤٠٥</td><td>٤٥,٢٦٤</td><td><span class="tag-pill tag-danger">+٢١٩٪</span></td><td>٥٦.٨٪</td><td>استقطاب الكادر الإداري والتنفيذي بدوام كامل</td></tr>
                    <tr><td>٢</td><td><strong>الإيجار المكتبي</strong></td><td>٦٣,٣٣٣</td><td>٣٥,٠٠٠</td><td><span class="tag-pill tag-danger">+٨١٪</span></td><td>٢٤.٩٪</td><td>الانتقال لمقر جديد بإيجار أقل (وفر ٢٥ ألف ريال سنوياً)</td></tr>
                    <tr><td>٣</td><td><strong>التأمينات الاجتماعية</strong></td><td>١٤,٧٦٨</td><td>٩,٩٨٠</td><td><span class="tag-pill tag-danger">+٤٨٪</span></td><td>٥.٨٪</td><td>اشتراكات الموظفين السعوديين بنظام التأمينات</td></tr>
                    <tr><td>٤</td><td><strong>أجور متعاونين ومحاسب</strong></td><td>١٣,٠٠٠</td><td>٩,٠٦٠</td><td><span class="tag-pill tag-danger">+٤٣٪</span></td><td>٥.١٪</td><td>أتعاب المحاسب والفرق المساندة في التأسيس</td></tr>
                    <tr><td>٥</td><td><strong>المحاسب القانوني المعتمد</strong></td><td>٤,٦٠٠</td><td>٠</td><td>—</td><td>١.٨٪</td><td>مراجعة وتدقيق القوائم المالية لعام ٢٠٢٥م</td></tr>
                    <tr><td>٦</td><td><strong>الكهرباء والخدمات</strong></td><td>٣,٨٦٧</td><td>٠</td><td>—</td><td>١.٥٪</td><td>فواتير تشغيل المقر الجديد</td></tr>
                    <tr><td>٧</td><td><strong>تصميم وتطوير الموقع</strong></td><td>٣,٠٠٠</td><td>٠</td><td>—</td><td>١.٢٪</td><td>بناء البوابة الإلكترونية ولوائح الحوكمة</td></tr>
                    <tr><td>٨</td><td><strong>نقل وتركيب الأصول</strong></td><td>٢,٤٣٠</td><td>٠</td><td>—</td><td>١.٠٪</td><td>تجهيز ونقل الأثاث والمكيفات للمقر</td></tr>
                    <tr><td>٩</td><td><strong>الهاتف والإنترنت</strong></td><td>١,٣١٦</td><td>١,٣٤٢</td><td><span class="tag-pill tag-success">-٢٪</span></td><td>٠.٥٪</td><td>خطوط الاتصال والأرشفة السحابية</td></tr>
                    <tr><td>١٠</td><td><strong>صيانة متنوعة</strong></td><td>١,٠٦٠</td><td>١,٣٩٣</td><td><span class="tag-pill tag-success">-٢٤٪</span></td><td>٠.٤٪</td><td>صيانة دورية وتجهيز المرافق</td></tr>
                    <tr><td>١١</td><td><strong>نظافة ومنظفات</strong></td><td>٩٠٠</td><td>٥٣١</td><td><span class="tag-pill tag-danger">+٦٩٪</span></td><td>٠.٣٥٪</td><td>مستلزمات نظافة المقر المكتبي</td></tr>
                    <tr><td>١٢</td><td><strong>طباعة ومطبوعات</strong></td><td>٥٠٨</td><td>٠</td><td>—</td><td>٠.٢٪</td><td>نماذج ومستندات العمل الرسمية</td></tr>
                    <tr><td>١٣</td><td><strong>رسوم وعمولات مصرفية</strong></td><td>٣٨٠</td><td>٠</td><td>—</td><td>٠.١٥٪</td><td>رسوم العمليات المصرفية والحوالات</td></tr>
                    <tr><td>١٤</td><td><strong>ضيافة واستقبال</strong></td><td>٣٧٥</td><td>٥٩٢</td><td><span class="tag-pill tag-success">-٣٧٪</span></td><td>٠.١٥٪</td><td>استقبال الزوار والمانحين واللجان</td></tr>
                    <tr><td>١٥</td><td><strong>أحبار طابعات</strong></td><td>١٨٠</td><td>٠</td><td>—</td><td>٠.٠٧٪</td><td>أحبار طابعة الليزر الملونة</td></tr>
                    <tr><td>١٦</td><td><strong>أدوات مكتبية وقرطاسية</strong></td><td>١٥٢</td><td>٣٦٧</td><td><span class="tag-pill tag-success">-٥٩٪</span></td><td>٠.٠٦٪</td><td>قرطاسية ومستلزمات استهلاكية</td></tr>
                    <tr class="total-row">
                        <td colspan="2">إجمالي المصروفات التشغيلية</td>
                        <td>٢٥٤,٢٧٤</td>
                        <td>٦٣,٥٣٦</td>
                        <td>+٣٠٠٪</td>
                        <td>١٠٠٪</td>
                        <td>المصروفات الفعلية المدققة لعمليات H1 2026</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Section 5: Clinical Impact & Patient Health Journey -->
    <section class="container" id="clinical" style="background:#FFF; border-radius:var(--radius-xl); padding-top:70px;">
        <div class="section-intro">
            <span class="eyebrow-pill">الرعاية والأثر الميداني</span>
            <h2 class="section-headline">البرامج والخدمات الطبية (برنامج جودة حياة)</h2>
            <p class="section-subtext">تغطية العمليات الجراحية والأورام الحرجة لـ ٧ حالات محققة نسبة تحسن وشفاء ١٠٠٪ بإجمالي ٢٠٨,٦٠٥.٣١ ريال</p>
        </div>

        <div class="grid-2" style="margin-bottom:40px;">
            <!-- Case 1 -->
            <div class="exec-card patient-box">
                <div class="patient-cost-tag">١٥٠,٠٠٠ ر.س</div>
                <h3 style="color:var(--primary); font-size:1.35rem; margin-bottom:4px;">فايز أحمد عبدالعزيز</h3>
                <div style="color:var(--secondary-dark); font-weight:700; font-size:0.95rem; margin-bottom:10px;"><i class="fas fa-hospital"></i> المستشفى السعودي الألماني</div>
                <div style="background:var(--bg-subtle); padding:6px 14px; border-radius:var(--radius-sm); font-size:0.92rem; display:inline-block; margin-bottom:10px;">
                    <strong>التشخيص:</strong> سرطان الدم (علاج مناعي وكيماوي تخصصي)
                </div>
                <p style="font-size:0.95rem; color:var(--text-muted);">تم التدخل الطبي العاجل وتوفير البروتوكول الدوائي التخصصي وتجاوز المرحلة الحرجة واستقرار الحالة بفضل الله.</p>
            </div>

            <!-- Case 2 -->
            <div class="exec-card patient-box">
                <div class="patient-cost-tag">٣٠,٠٠٠ ر.س</div>
                <h3 style="color:var(--primary); font-size:1.35rem; margin-bottom:4px;">زينب عمر علي</h3>
                <div style="color:var(--secondary-dark); font-weight:700; font-size:0.95rem; margin-bottom:10px;"><i class="fas fa-hospital"></i> المستشفى السعودي الألماني</div>
                <div style="background:var(--bg-subtle); padding:6px 14px; border-radius:var(--radius-sm); font-size:0.92rem; display:inline-block; margin-bottom:10px;">
                    <strong>التشخيص:</strong> سرطان نخر العظم
                </div>
                <p style="font-size:0.95rem; color:var(--text-muted);">توفير العلاج النوعي والمتابعة السريرية المتقدمة لإنقاذ الطرف المصاب وتحسن مؤشرات التعافي الكامل.</p>
            </div>

            <!-- Case 3 -->
            <div class="exec-card patient-box">
                <div class="patient-cost-tag">٧,٠٠٠ ر.س</div>
                <h3 style="color:var(--primary); font-size:1.35rem; margin-bottom:4px;">كندفة محمد عتبة</h3>
                <div style="color:var(--secondary-dark); font-weight:700; font-size:0.95rem; margin-bottom:10px;"><i class="fas fa-hospital"></i> مدينة الملك سلمان الطبية</div>
                <div style="background:var(--bg-subtle); padding:6px 14px; border-radius:var(--radius-sm); font-size:0.92rem; display:inline-block; margin-bottom:10px;">
                    <strong>التشخيص:</strong> تنويم ورعاية تحت الملاحظة الفائقة
                </div>
                <p style="font-size:0.95rem; color:var(--text-muted);">تغطية نفقات التنويم والرعاية التخصصية بعد إحالة المدينة الطبية واستقرار حالة المريضة وخروجها سالمة.</p>
            </div>

            <!-- Case 4 -->
            <div class="exec-card patient-box">
                <div class="patient-cost-tag">٧,٠٠٠ ر.س</div>
                <h3 style="color:var(--primary); font-size:1.35rem; margin-bottom:4px;">شوق حسن الأنور</h3>
                <div style="color:var(--secondary-dark); font-weight:700; font-size:0.95rem; margin-bottom:10px;"><i class="fas fa-hospital"></i> المستشفى السعودي الألماني</div>
                <div style="background:var(--bg-subtle); padding:6px 14px; border-radius:var(--radius-sm); font-size:0.92rem; display:inline-block; margin-bottom:10px;">
                    <strong>التشخيص:</strong> منظار جراحي متقدم
                </div>
                <p style="font-size:0.95rem; color:var(--text-muted);">إجراء الفحص التداخلي الدقيق وتحديد الخطة العلاجية الشافية واستكمال العلاج دون مضاعفات.</p>
            </div>

            <!-- Case 5 -->
            <div class="exec-card patient-box">
                <div class="patient-cost-tag">٦,٣٥٠ ر.س</div>
                <h3 style="color:var(--primary); font-size:1.35rem; margin-bottom:4px;">سامية سليمان محمد</h3>
                <div style="color:var(--secondary-dark); font-weight:700; font-size:0.95rem; margin-bottom:10px;"><i class="fas fa-hospital"></i> مستشفى المواساة بالمدينة</div>
                <div style="background:var(--bg-subtle); padding:6px 14px; border-radius:var(--radius-sm); font-size:0.92rem; display:inline-block; margin-bottom:10px;">
                    <strong>التشخيص:</strong> استئصال كتلة ورمية بالصدر
                </div>
                <p style="font-size:0.95rem; color:var(--text-muted);">نجاح العملية الجراحية بالكامل وشفاء المستفيدة وتقديمها رسالة شكر وعرفان لجمعية طبيبي وداعميها.</p>
            </div>

            <!-- Case 6 & 7 -->
            <div class="exec-card patient-box">
                <div class="patient-cost-tag">٨,٢٥٥.٣١ ر.س</div>
                <h3 style="color:var(--primary); font-size:1.35rem; margin-bottom:4px;">زبيدة شمس الدين & محمد الشرفي</h3>
                <div style="color:var(--secondary-dark); font-weight:700; font-size:0.95rem; margin-bottom:10px;"><i class="fas fa-hospital"></i> السعودي الألماني & مستشفى المواساة</div>
                <div style="background:var(--bg-subtle); padding:6px 14px; border-radius:var(--radius-sm); font-size:0.92rem; display:inline-block; margin-bottom:10px;">
                    <strong>التشخيص:</strong> ورم قولون (٦,٣٣٠ ر.س) & أشعة رنين (١,٩٢٥ ر.س)
                </div>
                <p style="font-size:0.95rem; color:var(--text-muted);">تقديم التدخلات التشخيصية والعلاجية واستكمال البروتوكول الطبي لحالتين من أشد المرضى حاجة.</p>
            </div>
        </div>

        <!-- 14 Rejected Cases Drilldown Table -->
        <div class="table-card">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.3rem;"><i class="fas fa-user-xmark" style="color:var(--danger); margin-left:8px;"></i> التحليل التدقيقي للحالات الـ (١٤) غير المقبولة وأسباب عدم الصرف</h3>
                    <p style="font-size:0.9rem; color:var(--text-muted);">توضح المؤشرات أن ٥٠٪ من أسباب الرفض ترجع لانتهاء الإقامة النظامية، مما يبرز أهمية تحديث اللائحة بالتنسيق مع المانحين</p>
                </div>
                <span class="tag-pill tag-warning" style="font-size:0.95rem; padding:6px 16px;">توصية الحوكمة: مراجعة معايير اللائحة</span>
            </div>

            <table class="custom-table">
                <thead>
                    <tr>
                        <th>سبب عدم القبول</th>
                        <th>العدد</th>
                        <th>النسبة %</th>
                        <th>أبرز أسماء المستفيدين المتقدمين</th>
                        <th>الإجراء الإداري والتوصية المعتمدة</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>انتهاء صلاحية الإقامة</strong></td>
                        <td>٧ حالات</td>
                        <td>٥٠.٠٪</td>
                        <td>بسمة هارون، سيد الأمين، فريدة عظيم، عطور عباس، هاجر الصادق، عبدالله دياب، أحمد خير</td>
                        <td>التنسيق مع كبار المانحين لإنشاء صندوق خاص للحالات الإنسانية الحرجة</td>
                    </tr>
                    <tr>
                        <td><strong>تغطية كاملة من جمعية أخرى</strong></td>
                        <td>حالتان</td>
                        <td>١٤.٣٪</td>
                        <td>هديباء عواده الجهني (مياه بيضاء)، علي قايد علي (قلب وشرايين)</td>
                        <td>تفعيل الربط الإلكتروني لتفادي ازدواجية الصرف وتسريع خدمة مرضى آخرين</td>
                    </tr>
                    <tr>
                        <td><strong>أخطاء بالتقرير الطبي / اختلاف التشخيص</strong></td>
                        <td>حالتان</td>
                        <td>١٤.٣٪</td>
                        <td>ريم فواز زاده (ورم ليفي)، جوهرة منصور خان (أخطاء تقرير وتواريخ)</td>
                        <td>إرشاد المستفيدين لتصحيح المستندات الطبية مع المستشفيات الشريكة وإعادة الرفع</td>
                    </tr>
                    <tr>
                        <td><strong>وجود تأمين طبي ساري المفعول</strong></td>
                        <td>حالة واحدة</td>
                        <td>٧.١٪</td>
                        <td>فؤاد لطف محمد (ميلوما متعددة)</td>
                        <td>توجيه المستفيد للاستفادة من وثيقة التأمين الطبي المعتمدة لجهة عمله</td>
                    </tr>
                    <tr>
                        <td><strong>انتهاء تأشيرة الزيارة وسفر المستفيد</strong></td>
                        <td>حالة واحدة</td>
                        <td>٧.١٪</td>
                        <td>حمزة محمد هندية (سكري نوع أول)</td>
                        <td>إغلاق الملف لانتفاء شرط الإقامة النظامية المحلية</td>
                    </tr>
                    <tr>
                        <td><strong>مقبولة وقيد استلام التعميد</strong></td>
                        <td>حالة واحدة</td>
                        <td>٧.١٪</td>
                        <td>مزاهر عبدالله الهادي (ضعف نظر)</td>
                        <td>متابعة التواصل لتسليم التعميد الطبي وبدء المتابعة العلاجية</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Section 6: Healthcare Partnerships Ecosystem -->
    <section class="container" id="partners">
        <div class="section-intro">
            <span class="eyebrow-pill">التحالفات والتكامل</span>
            <h2 class="section-headline">شبكة الشراكات الصحية الـ (٩) المفعّلة</h2>
            <p class="section-subtext">تكامل مع كبرى الصروح الطبية لتقديم الرعاية للمستفيدين بأعلى جودة وأفضل تسعيرة</p>
        </div>

        <div class="grid-3">
            <div class="partner-box"><i class="fas fa-hospital-user"></i><h4 style="color:var(--primary); font-size:1.15rem;">المستشفى السعودي الألماني</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">علاج الأورام وسرطانات الدم والمناظير التخصصية</p></div>
            <div class="partner-box"><i class="fas fa-hospital"></i><h4 style="color:var(--primary); font-size:1.15rem;">مستشفى المواساة بالمدينة</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">الجراحات المتقدمة والأشعة المقطعية والرنين المغناطيسي</p></div>
            <div class="partner-box"><i class="fas fa-square-h"></i><h4 style="color:var(--primary); font-size:1.15rem;">مدينة الملك سلمان الطبية</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">الرعاية التخصصية المرجعية والتنويم والعناية الفائقة</p></div>
            <div class="partner-box"><i class="fas fa-user-doctor"></i><h4 style="color:var(--primary); font-size:1.15rem;">مستشفى د. حامد الأحمدي</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">جراحات اليوم الواحد والعيادات الاستشارية الشاملة</p></div>
            <div class="partner-box"><i class="fas fa-clinic-medical"></i><h4 style="color:var(--primary); font-size:1.15rem;">مستشفى المدينة الوطني</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">خدمات الطوارئ والملاحظة والتحاليل والمختبرات</p></div>
            <div class="partner-box"><i class="fas fa-house-medical"></i><h4 style="color:var(--primary); font-size:1.15rem;">مستشفى المدينة الطبي العام</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">الفحوصات العامة ورعاية الأمراض المزمنة والمتابعة</p></div>
            <div class="partner-box"><i class="fas fa-stethoscope"></i><h4 style="color:var(--primary); font-size:1.15rem;">مستشفى واد الطبي</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">علاج الإصابات الرياضية وجراحة العظام والمفاصل</p></div>
            <div class="partner-box"><i class="fas fa-briefcase-medical"></i><h4 style="color:var(--primary); font-size:1.15rem;">شركة مداواة ورعاية الطبية</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">توفير الأدوية والمستلزمات الطبية والرعاية المنزلية</p></div>
            <div class="partner-box"><i class="fas fa-wheelchair"></i><h4 style="color:var(--primary); font-size:1.15rem;">جمعية جَنَى لتأهيل المعاقات</h4><p style="font-size:0.9rem; color:var(--text-muted); margin-top:6px;">التأهيل الطبي المتخصص والتكامل مع ذوي الإعاقة</p></div>
        </div>
    </section>

    <!-- Section 7: Governance & Strategic Roadmap -->
    <section class="container" id="governance">
        <div class="section-intro">
            <span class="eyebrow-pill">التحول المؤسسي والاستدامة</span>
            <h2 class="section-headline">الحوكمة وخارطة طريق النصف الثاني (٣ مراحل)</h2>
            <p class="section-subtext">تطبيق نظام قيود السحابي، وفر المقر الجديد، والتعاقد مع فريق استشاري تخصصي لرفع درجة الحوكمة</p>
        </div>

        <div class="grid-3" style="margin-bottom:40px;">
            <div class="roadmap-card">
                <div>
                    <div class="roadmap-num">المرحلة ١</div>
                    <h3 style="color:var(--secondary-light); font-size:1.3rem; margin-bottom:12px;">استكمال الحوكمة ومنصة نوى</h3>
                    <p style="font-size:0.95rem; line-height:1.8; color:#F0EBE1;">
                        • استيفاء معايير الامتثال والحوكمة المعتمدة لدى المركز الوطني.<br>
                        • رفع درجة تقييم الجمعية الرسمية لفتح مسارات الدعم الحكومي.<br>
                        • تفعيل منصة نوى للمنح وتوظيف القوائم المالية المدققة.
                    </p>
                </div>
                <div style="margin-top:20px; font-weight:700; color:var(--secondary); font-size:0.9rem;">المدى الزمني: الشهر الأول</div>
            </div>

            <div class="roadmap-card">
                <div>
                    <div class="roadmap-num">المرحلة ٢</div>
                    <h3 style="color:var(--secondary-light); font-size:1.3rem; margin-bottom:12px;">تنمية الموارد وبطاقة طبيبي</h3>
                    <p style="font-size:0.95rem; line-height:1.8; color:#F0EBE1;">
                        • إطلاق مبادرة «بطاقة طبيبي» للمزايا والخصومات الصحية للمستفيدين.<br>
                        • تعديل لائحة المساعدات العلاجية لرفع معدل قبول الحالات الحرجة.<br>
                        • بناء قاعدة بيانات المانحين والأوقاف الاستراتيجية.
                    </p>
                </div>
                <div style="margin-top:20px; font-weight:700; color:var(--secondary); font-size:0.9rem;">المدى الزمني: الشهر الثاني</div>
            </div>

            <div class="roadmap-card">
                <div>
                    <div class="roadmap-num">المرحلة ٣</div>
                    <h3 style="color:var(--secondary-light); font-size:1.3rem; margin-bottom:12px;">الاستعداد المبكر لـ Q1 2027</h3>
                    <p style="font-size:0.95rem; line-height:1.8; color:#F0EBE1;">
                        • إعداد وتقديم الحقائب الاستثمارية للصناديق الكبرى والشركات.<br>
                        • استهداف المانحين الذين أغلقت موازناتهم بالنصف الأول.<br>
                        • تفعيل دور الجمعية العمومية والمجلس في الاستدامة.
                    </p>
                </div>
                <div style="margin-top:20px; font-weight:700; color:var(--secondary); font-size:0.9rem;">المدى الزمني: الشهر الثالث</div>
            </div>
        </div>
    </section>

    <!-- Section 8: Master Appendices with Instant Live Search -->
    <section class="container" id="master-appendices">
        <div class="section-intro">
            <span class="eyebrow-pill">البيانات الرسمية غير المنقوصة</span>
            <h2 class="section-headline">الملاحق المالية والتفصيلية الكاملة</h2>
            <p class="section-subtext">بيان الداعمين الـ (٢٢) كاملاً، وبيان الأصول والتجهيزات الثابتة المعتمد</p>
        </div>

        <!-- Appendix 1: Complete 22 Donors Table with Search -->
        <div class="table-card">
            <div class="table-toolbar">
                <div>
                    <h3 style="color:var(--primary); font-size:1.3rem;"><i class="fas fa-hand-holding-dollar" style="color:var(--secondary); margin-left:8px;"></i> الملحق (١): بيان الداعمين التفصيلي لعام ٢٠٢٦م (٥٨٢,١٦٧.٥٢ ريال)</h3>
                    <p style="font-size:0.9rem; color:var(--text-muted);">سجل كافة التبرعات والمساهمات الواردة لحسابات الجمعية بالنصف الأول ٢٠٢٦م</p>
                </div>
                <div class="search-input-wrap">
                    <i class="fas fa-search"></i>
                    <input type="text" id="donorSearch" placeholder="بحث باسم المانح أو المجال..." onkeyup="filterTable('donorSearch', 'donorTable')">
                </div>
            </div>

            <table class="custom-table" id="donorTable">
                <thead>
                    <tr>
                        <th>م</th>
                        <th>الجهة الداعمة / المانح</th>
                        <th>التاريخ</th>
                        <th>المبلغ (ريال)</th>
                        <th>مجال الدعم والتخصيص</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>١</td><td>أسامة جعفر إبراهيم فقيه</td><td>٢٢/٠١/٢٠٢٦</td><td>٥٠,٠٠٠</td><td>زكاة مقيدة</td></tr>
                    <tr><td>٢</td><td>مريم حبيب محمود أحمد</td><td>١٣/٠٢/٢٠٢٦</td><td>٢٠,٠٠٠</td><td>زكاة مقيدة</td></tr>
                    <tr><td>٣</td><td>وقف الشيخ نغيمش الأحمدي (رحمه الله)</td><td>١٦/٠٢/٢٠٢٦</td><td>٥٠,٠٠٠</td><td>٣٥,٠٠٠ علاج + ١٥,٠٠٠ عام</td></tr>
                    <tr><td>٤</td><td>أسامة عدنان حبيب محمود أحمد</td><td>١٦/٠٢/٢٠٢٦</td><td>١٠,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>٥</td><td>شركة طابة المطورة للتطوير العمراني</td><td>٢٣/٠٢/٢٠٢٦</td><td>٢٠,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>٦</td><td>وقف الشيخ عبدالقادر شيبة الحمد</td><td>٢٧/٠٢/٢٠٢٦</td><td>٥٠,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>٧</td><td>شركة حسن محمد حجري</td><td>٢٧/٠٢/٢٠٢٦</td><td>٥,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>٨</td><td>سمر فتح الرحمن علي</td><td>٠١/٠٣/٢٠٢٦</td><td>٢,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>٩</td><td>سعد بن محمد حسين</td><td>٠٣/٠٣/٢٠٢٦</td><td>٢٥٠,٠٠٠</td><td>دعم عام (أكبر متبرع)</td></tr>
                    <tr><td>١٠</td><td>مربا بنت محمد محروس</td><td>٠٤/٠٣/٢٠٢٦</td><td>٢٠٠</td><td>دعم عام</td></tr>
                    <tr><td>١١</td><td>مؤسسة سعيد محمد مكي</td><td>٠٨/٠٣/٢٠٢٦</td><td>٣,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>١٢</td><td>ضيف (فاعل خير)</td><td>٠٩/٠٣/٢٠٢٦</td><td>٥,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>١٣</td><td>سلطان محمد الفقيهي</td><td>١٠/٠٣/٢٠٢٦</td><td>٣٠,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>١٤</td><td>وقف عبدالرحيم عبدالرزاق</td><td>١٢/٠٣/٢٠٢٦</td><td>١٠,٠٠٠</td><td>دعم عام</td></tr>
                    <tr><td>١٥</td><td>مؤسسة سهيلة شيبة الحمد الخيرية</td><td>٠٩/٠٤/٢٠٢٦</td><td>٢٠,٠٠٠</td><td>علاج ومساعدات طبية</td></tr>
                    <tr><td>١٦</td><td>وقف عبدالعزيز عبدالله أبو زيد</td><td>٢٨/٠٦/٢٠٢٦</td><td>٢٠,٠٠٠</td><td>علاج ومساعدات طبية</td></tr>
                    <tr><td>١٧</td><td>المتجر الإلكتروني للجمعية</td><td>متفرقة</td><td>١٠,٤٦٩</td><td>علاج مقيد</td></tr>
                    <tr><td>١٨</td><td>منصة تبرع الوطنية</td><td>٢٣/٠٢/٢٠٢٦</td><td>١,٢٠٢.٨٨</td><td>علاج مقيد</td></tr>
                    <tr><td>١٩</td><td>متفرقات وتبرعات نقدية</td><td>متفرقة</td><td>٣٩٥.٣٠</td><td>دعم عام</td></tr>
                    <tr><td>٢٠</td><td>حوالات مصرفية صغيرة متفرقة</td><td>متفرقة</td><td>٦,٩٠٠.٣٤</td><td>دعم عام</td></tr>
                    <tr><td>٢١</td><td>رسوم اشتراكات العضوية المحصلة</td><td>متفرقة</td><td>١٨,٠٠٠</td><td>دعم عام</td></tr>
                    <tr class="total-row">
                        <td colspan="3">الإجمالي التراكمي المعتمد لبيان الداعمين</td>
                        <td>٥٨٢,١٦٧.٥٢</td>
                        <td>زكاة: ٧٠ ألف | علاج: ٨٥,٦٧٢ | عام: ٤٢٦,٤٩٦</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Appendix 2: Fixed Assets Table -->
        <div class="table-card" style="margin-bottom:0;">
            <h3 style="color:var(--primary); font-size:1.25rem; margin-bottom:15px;"><i class="fas fa-desktop" style="color:var(--secondary); margin-left:8px;"></i> الملحق (٢): بيان الأصول والتجهيزات المشتراة لعام ٢٠٢٦م (١٥,٦٢٠.٨٠ ريال)</h3>
            <table class="custom-table">
                <thead>
                    <tr><th>الأصل والتجهيز</th><th>العدد</th><th>القيمة (ريال)</th><th>المورد المعتمد</th><th>الاستخدام والتوزيع</th></tr>
                </thead>
                <tbody>
                    <tr><td>طابعة ليزر ملون HP</td><td>١</td><td>١,٣٥٠</td><td>شركة سمرة الرقمية</td><td>طباعة التقارير والمعاملات الرسمية</td></tr>
                    <tr><td>مكتب سكرتارية خشب بني</td><td>٦</td><td>٤,٦٨٠</td><td>الصفوة الجديدة للأثاث</td><td>تأثيث مكاتب الإدارة والمقر الجديد</td></tr>
                    <tr><td>كرسي دوار جلد رصاصي</td><td>٦</td><td>٢,٧٠٠</td><td>الصفوة الجديدة للأثاث</td><td>كراسي مكاتب الموظفين</td></tr>
                    <tr><td>مكيفات أوجين ٢٤ وحدة</td><td>٣</td><td>٤,٥٩٠.٨٠</td><td>محل بن بلال للأجهزة</td><td>تكييف صالات ومكاتب المقر</td></tr>
                    <tr><td>خزينة حديدية للمستندات</td><td>١</td><td>١,٢٥٠</td><td>الصفوة الجديدة للأثاث</td><td>حفظ الوثائق والملفات المالية السرية</td></tr>
                    <tr><td>كرسي انتظار كروم للمراجعين</td><td>٣</td><td>١,٠٥٠</td><td>مؤسسة الشرق هوم</td><td>استقبال مراجعي الجمعية والمرضى</td></tr>
                    <tr class="total-row">
                        <td colspan="2">إجمالي الأصول الثابتة المضافة لعام ٢٠٢٦م</td>
                        <td colspan="3">١٥,٦٢٠.٨٠ ريال سعودي (مقارنة بـ ٣٤,٧٧٥.٥٠ ريال في الفترة المماثلة)</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Footer & Official Channels -->
    <footer class="footer-v2">
        <div class="footer-grid">
            <div>
                <h3 style="color:var(--secondary); font-size:1.6rem; margin-bottom:12px;">جمعية طبيبي الأهلية بالمدينة المنورة</h3>
                <p style="color:rgba(255,255,255,0.75); line-height:1.9;">
                    جمعية صحية أهلية مسجلة بالمركز الوطني لتنمية القطاع غير الربحي برقم (١٠٠٠٧٣٠٧٠٠)، تهدف لتقديم المساعدات العلاجية والرعاية الصحية النوعية للمرضى الأشد حاجة في طيبة الطيبة تحقيقاً لمبدأ التكافل وتعزيزاً لجودة الحياة.
                </p>
            </div>

            <div>
                <h4 style="color:#FFF; font-size:1.2rem; margin-bottom:15px; border-bottom:2px solid var(--secondary); padding-bottom:6px; display:inline-block;">بيانات التواصل</h4>
                <ul style="list-style:none; line-height:2.4; color:rgba(255,255,255,0.85);">
                    <li><i class="fas fa-phone" style="color:var(--secondary); margin-left:8px;"></i> 00966555606347</li>
                    <li><i class="fas fa-envelope" style="color:var(--secondary); margin-left:8px;"></i> tabibi2025med@gmail.com</li>
                    <li><i class="fas fa-map-marker-alt" style="color:var(--secondary); margin-left:8px;"></i> المدينة المنورة - حي الفتح</li>
                </ul>
            </div>

            <div>
                <h4 style="color:#FFF; font-size:1.2rem; margin-bottom:15px; border-bottom:2px solid var(--secondary); padding-bottom:6px; display:inline-block;">الجهات المشرفة والمنصات</h4>
                <ul style="list-style:none; line-height:2.4; color:rgba(255,255,255,0.8);">
                    <li>• المركز الوطني للقطاع غير الربحي</li>
                    <li>• وزارة الموارد البشرية والتنمية الاجتماعية</li>
                    <li>• وزارة الصحة & تجمع المدينة الصحي</li>
                    <li>• منصة إحسان & منصة شفاء & منصة نوى</li>
                </ul>
            </div>
        </div>

        <div style="max-width:1440px; margin:0 auto; text-align:center; padding-top:25px; border-top:1px solid rgba(255,255,255,0.1); color:rgba(255,255,255,0.6); font-size:0.9rem;">
            جميع الحقوق محفوظة © جمعية طبيبي الأهلية بالمدينة المنورة ٢٠٢٦م | إعداد وإخراج تنفيذي متكامل
        </div>
    </footer>

    <!-- Interactive Scripts & Chart.js -->
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

        // Initialize Charts
        document.addEventListener('DOMContentLoaded', function() {
            Chart.defaults.font.family = "'Cairo', sans-serif";
            Chart.defaults.color = '#666';

            // 1. Revenue Comparison Bar Chart
            const ctxRev = document.getElementById('v2RevChart');
            if (ctxRev) {
                new Chart(ctxRev, {
                    type: 'bar',
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
                        plugins: {
                            legend: { position: 'top', rtl: true, labels: { font: { size: 12, weight: '700' } } },
                            tooltip: { rtl: true }
                        },
                        scales: {
                            y: { beginAtZero: true, ticks: { callback: v => v.toLocaleString() + ' ر.س' } }
                        }
                    }
                });
            }

            // 2. Expenses Distribution Doughnut Chart
            const ctxExp = document.getElementById('v2ExpChart');
            if (ctxExp) {
                new Chart(ctxExp, {
                    type: 'doughnut',
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
                        plugins: {
                            legend: { position: 'bottom', rtl: true, labels: { boxWidth: 12, font: { size: 11 } } },
                            tooltip: { rtl: true }
                        },
                        cutout: '62%'
                    }
                });
            }
        });
    </script>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated Executive Dashboard V2 successfully: {output_file}")
