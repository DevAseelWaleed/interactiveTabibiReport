# -*- coding: utf-8 -*-
import os, sys, json

base_dir = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(base_dir, "التقرير_الجديد", "index.html")

html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>التقرير النصف سنوي الشامل ٢٠٢٦م | جمعية طبيبي الأهلية</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        :root {
            --primary: #6B1D3A;
            --primary-dark: #4A1226;
            --primary-light: #8B254B;
            --secondary: #C9A96E;
            --secondary-light: #DFCA9B;
            --secondary-dark: #A68547;
            --accent: #9E2A54;
            --bg-base: #F8F7F4;
            --bg-card: #FFFFFF;
            --bg-alt: #F1EFEA;
            --text-main: #242220;
            --text-muted: #6B6864;
            --text-light: #9C9892;
            --success: #1E824C;
            --success-bg: #E8F8F0;
            --warning: #D9822B;
            --warning-bg: #FEF6EB;
            --danger: #C0392B;
            --danger-bg: #FDEDEC;
            --info: #2980B9;
            --info-bg: #EBF5FB;
            --radius-lg: 24px;
            --radius-md: 16px;
            --radius-sm: 10px;
            --shadow-subtle: 0 4px 20px rgba(107, 29, 58, 0.04);
            --shadow-card: 0 10px 30px rgba(107, 29, 58, 0.07);
            --shadow-hover: 0 20px 45px rgba(107, 29, 58, 0.13);
            --transition-smooth: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
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
            background-color: var(--bg-base);
            color: var(--text-main);
            line-height: 1.8;
            overflow-x: hidden;
            font-size: 16px;
        }

        /* Floating Header Nav */
        .header-nav {
            position: fixed;
            top: 18px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: center;
            z-index: 1000;
            pointer-events: none;
        }

        .nav-pill {
            pointer-events: auto;
            background: rgba(255, 255, 255, 0.88);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: 10px 24px;
            border-radius: 50px;
            box-shadow: 0 10px 35px rgba(107, 29, 58, 0.12);
            border: 1px solid rgba(201, 169, 110, 0.3);
            display: flex;
            gap: 16px;
            align-items: center;
            transition: var(--transition-smooth);
        }

        .nav-brand {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 800;
            color: var(--primary);
            text-decoration: none;
            padding-left: 15px;
            border-left: 1.5px solid rgba(107, 29, 58, 0.15);
            font-size: 1.05rem;
        }

        .nav-brand i {
            color: var(--secondary);
            font-size: 1.25rem;
        }

        .nav-links {
            display: flex;
            gap: 14px;
            list-style: none;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-main);
            font-weight: 600;
            font-size: 0.92rem;
            padding: 6px 14px;
            border-radius: 20px;
            transition: var(--transition-smooth);
        }

        .nav-links a:hover, .nav-links a.active {
            background: var(--primary);
            color: #fff;
        }

        .nav-actions {
            display: flex;
            gap: 8px;
            margin-right: 8px;
        }

        .btn-print {
            background: var(--secondary);
            color: #fff;
            border: none;
            padding: 7px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: var(--transition-smooth);
        }

        .btn-print:hover {
            background: var(--secondary-dark);
            transform: scale(1.03);
        }

        /* Container & Grid Standards */
        .section-wrapper {
            max-width: 1420px;
            margin: 0 auto;
            padding: 90px 30px;
        }

        .section-header {
            text-align: center;
            margin-bottom: 55px;
            position: relative;
        }

        .section-eyebrow {
            display: inline-block;
            color: var(--secondary-dark);
            font-weight: 800;
            font-size: 0.95rem;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 8px;
            background: rgba(201, 169, 110, 0.12);
            padding: 4px 16px;
            border-radius: 30px;
        }

        .section-title {
            color: var(--primary);
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 12px;
            position: relative;
            display: inline-block;
        }

        .section-desc {
            color: var(--text-muted);
            font-size: 1.1rem;
            max-width: 750px;
            margin: 0 auto;
        }

        /* Double-Bezel Card Technique */
        .bezel-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(245, 240, 235, 0.6));
            padding: 7px;
            border-radius: var(--radius-lg);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: var(--shadow-card);
            transition: var(--transition-smooth);
            height: 100%;
        }

        .bezel-card:hover {
            transform: translateY(-8px);
            box-shadow: var(--shadow-hover);
            border-color: rgba(201, 169, 110, 0.4);
        }

        .bezel-core {
            background: #FFFFFF;
            border-radius: calc(var(--radius-lg) - 6px);
            padding: 32px;
            height: 100%;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
            box-shadow: inset 0 1px 2px rgba(255,255,255,0.8);
        }

        /* Hero / Cover Section */
        .hero-section {
            min-height: 100vh;
            background: linear-gradient(145deg, #50132A 0%, #6B1D3A 40%, #380B1B 100%);
            color: #fff;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 120px 25px 80px;
            overflow: hidden;
        }

        .hero-pattern {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: radial-gradient(rgba(201, 169, 110, 0.15) 1px, transparent 1px);
            background-size: 36px 36px;
            opacity: 0.6;
        }

        .hero-decor-orb {
            position: absolute;
            width: 500px;
            height: 500px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(201, 169, 110, 0.25) 0%, rgba(107, 29, 58, 0) 70%);
            filter: blur(60px);
            top: 10%;
            left: 5%;
            pointer-events: none;
        }

        .hero-content {
            position: relative;
            z-index: 2;
            max-width: 1050px;
        }

        .hero-logo-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 110px;
            height: 110px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 2px solid var(--secondary);
            color: var(--secondary);
            font-size: 3.2rem;
            margin-bottom: 25px;
            box-shadow: 0 0 45px rgba(201, 169, 110, 0.3);
            animation: pulse-glow 3s infinite alternate;
        }

        @keyframes pulse-glow {
            0% { box-shadow: 0 0 25px rgba(201, 169, 110, 0.2); transform: scale(1); }
            100% { box-shadow: 0 0 55px rgba(201, 169, 110, 0.5); transform: scale(1.04); }
        }

        .hero-entity-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 0.5px;
        }

        .hero-entity-sub {
            font-size: 1.1rem;
            color: var(--secondary-light);
            font-weight: 500;
            margin-bottom: 25px;
            letter-spacing: 1px;
        }

        .hero-main-title {
            font-size: 3.8rem;
            font-weight: 900;
            line-height: 1.2;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #FFFFFF 30%, var(--secondary-light) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-period-tag {
            display: inline-block;
            background: rgba(201, 169, 110, 0.18);
            border: 1px solid rgba(201, 169, 110, 0.4);
            padding: 8px 24px;
            border-radius: 30px;
            font-size: 1.15rem;
            font-weight: 600;
            color: #FFFFFF;
            margin-bottom: 30px;
        }

        .hero-motto-strip {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            font-size: 1.7rem;
            font-weight: 800;
            color: var(--secondary);
            margin: 25px 0 40px;
        }

        .hero-motto-strip span {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .hero-motto-strip i {
            font-size: 0.8rem;
            opacity: 0.7;
        }

        .hero-meta-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 35px;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.15);
        }

        .hero-meta-item {
            font-size: 0.95rem;
            color: rgba(255, 255, 255, 0.85);
        }

        .hero-meta-item strong {
            display: block;
            color: var(--secondary-light);
            font-size: 1.1rem;
            margin-bottom: 4px;
        }

        /* Royal Leadership Section */
        .royal-section {
            background: #FFFFFF;
            padding: 80px 30px;
            border-bottom: 1px solid rgba(107, 29, 58, 0.08);
        }

        .royal-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            max-width: 1350px;
            margin: 0 auto;
        }

        .royal-card {
            background: linear-gradient(145deg, #4A1226, #2E0B17);
            border-radius: var(--radius-lg);
            padding: 40px 30px;
            color: #fff;
            text-align: center;
            position: relative;
            box-shadow: 0 15px 35px rgba(74, 18, 38, 0.2);
            border: 1px solid rgba(201, 169, 110, 0.35);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .royal-emblem {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            border: 3px solid var(--secondary);
            margin: 0 auto 20px;
            overflow: hidden;
            background: #FFF;
            box-shadow: 0 0 25px rgba(201, 169, 110, 0.35);
        }

        .royal-emblem img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top center;
        }

        .royal-card h3 {
            color: var(--secondary);
            font-size: 1.35rem;
            font-weight: 800;
            margin-bottom: 6px;
        }

        .royal-role {
            font-size: 0.95rem;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 20px;
            font-weight: 600;
        }

        .royal-quote {
            font-size: 1.02rem;
            line-height: 1.8;
            color: #F8F7F4;
            font-style: italic;
            background: rgba(0, 0, 0, 0.2);
            padding: 20px;
            border-radius: var(--radius-md);
            border-right: 3px solid var(--secondary);
            text-align: justify;
        }

        /* Chairman & Board Section */
        .speech-card {
            background: #FFFFFF;
            border-radius: var(--radius-lg);
            padding: 50px;
            box-shadow: var(--shadow-card);
            border: 1px solid rgba(107, 29, 58, 0.08);
            position: relative;
            margin-bottom: 40px;
        }

        .speech-quote-icon {
            position: absolute;
            top: 30px;
            left: 40px;
            font-size: 4rem;
            color: rgba(201, 169, 110, 0.15);
        }

        .speech-content p {
            font-size: 1.15rem;
            line-height: 2.1;
            color: var(--text-main);
            margin-bottom: 20px;
            text-align: justify;
        }

        .speech-author {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 20px;
            margin-top: 30px;
            padding-top: 25px;
            border-top: 1px solid rgba(107, 29, 58, 0.08);
        }

        .speech-author-info h4 {
            font-size: 1.3rem;
            color: var(--primary);
            font-weight: 800;
        }

        .speech-author-info p {
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        /* KPI Master Grid */
        .kpi-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            margin-bottom: 35px;
        }

        .kpi-card {
            position: relative;
        }

        .kpi-icon-wrap {
            width: 58px;
            height: 58px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            margin-bottom: 18px;
        }

        .kpi-icon-primary { background: rgba(107, 29, 58, 0.08); color: var(--primary); }
        .kpi-icon-success { background: var(--success-bg); color: var(--success); }
        .kpi-icon-warning { background: var(--warning-bg); color: var(--warning); }
        .kpi-icon-info { background: var(--info-bg); color: var(--info); }
        .kpi-icon-danger { background: var(--danger-bg); color: var(--danger); }

        .kpi-label {
            font-size: 0.98rem;
            font-weight: 600;
            color: var(--text-muted);
            margin-bottom: 6px;
        }

        .kpi-value {
            font-size: 2.2rem;
            font-weight: 900;
            color: var(--primary);
            line-height: 1.2;
            margin-bottom: 10px;
        }

        .kpi-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
        }

        .badge-success { background: var(--success-bg); color: var(--success); }
        .badge-warning { background: var(--warning-bg); color: var(--warning); }
        .badge-danger { background: var(--danger-bg); color: var(--danger); }
        .badge-info { background: var(--info-bg); color: var(--info); }

        .kpi-hint {
            font-size: 0.85rem;
            color: var(--text-light);
            margin-top: 10px;
            line-height: 1.4;
        }

        /* Budget Gauges & Progress */
        .progress-block {
            margin-bottom: 22px;
        }

        .progress-labels {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
            font-weight: 700;
            font-size: 0.95rem;
        }

        .progress-track {
            height: 14px;
            background: #EBE8E1;
            border-radius: 30px;
            overflow: hidden;
            position: relative;
        }

        .progress-bar-fill {
            height: 100%;
            border-radius: 30px;
            background: linear-gradient(90deg, var(--secondary), var(--primary));
            transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* Tables Styling */
        .custom-table-card {
            background: #FFFFFF;
            border-radius: var(--radius-lg);
            padding: 30px;
            box-shadow: var(--shadow-card);
            border: 1px solid rgba(107, 29, 58, 0.07);
            margin-bottom: 40px;
            overflow-x: auto;
        }

        .data-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            text-align: right;
        }

        .data-table th {
            background: #F6F4EE;
            color: var(--primary);
            font-weight: 800;
            font-size: 0.95rem;
            padding: 16px 20px;
            border-bottom: 2px solid rgba(107, 29, 58, 0.15);
        }

        .data-table th:first-child { border-top-right-radius: 12px; }
        .data-table th:last-child { border-top-left-radius: 12px; }

        .data-table td {
            padding: 15px 20px;
            border-bottom: 1px solid #EFECE6;
            color: var(--text-main);
            font-size: 0.95rem;
        }

        .data-table tr:hover td {
            background-color: rgba(201, 169, 110, 0.05);
        }

        .table-total-row td {
            background: #FAF8F4;
            font-weight: 800;
            color: var(--primary);
            border-top: 2px solid rgba(107, 29, 58, 0.2);
            font-size: 1.05rem;
        }

        /* Interactive Charts Container */
        .chart-box {
            position: relative;
            height: 360px;
            width: 100%;
            margin-top: 15px;
        }

        /* 2-Col and 3-Col Grids */
        .grid-2 {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
            margin-bottom: 40px;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-bottom: 40px;
        }

        .grid-4 {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            margin-bottom: 40px;
        }

        /* Patient Cards */
        .patient-card {
            border-right: 4px solid var(--secondary);
            position: relative;
        }

        .patient-badge-cost {
            position: absolute;
            top: 25px;
            left: 25px;
            background: rgba(107, 29, 58, 0.08);
            color: var(--primary);
            padding: 6px 14px;
            border-radius: 30px;
            font-weight: 800;
            font-size: 1.1rem;
        }

        .patient-name {
            font-size: 1.3rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 6px;
        }

        .patient-hospital {
            font-size: 0.95rem;
            color: var(--secondary-dark);
            font-weight: 700;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .patient-diagnosis {
            font-size: 0.95rem;
            color: var(--text-muted);
            background: var(--bg-alt);
            padding: 8px 14px;
            border-radius: var(--radius-sm);
            display: inline-block;
        }

        /* Partner Logos/Cards */
        .partner-card {
            text-align: center;
            padding: 25px 15px;
            background: #FFFFFF;
            border-radius: var(--radius-md);
            border: 1px solid rgba(107, 29, 58, 0.06);
            box-shadow: var(--shadow-subtle);
            transition: var(--transition-smooth);
        }

        .partner-card:hover {
            border-color: var(--secondary);
            transform: translateY(-5px);
        }

        .partner-icon {
            font-size: 2.4rem;
            color: var(--primary);
            margin-bottom: 15px;
        }

        .partner-title {
            font-weight: 700;
            font-size: 1.05rem;
            color: var(--text-main);
        }

        /* Timeline / Phases */
        .phase-step {
            position: relative;
            padding-right: 35px;
            margin-bottom: 25px;
            border-right: 2px dashed var(--secondary);
        }

        .phase-step:last-child {
            border-right: 2px solid transparent;
            margin-bottom: 0;
        }

        .phase-bullet {
            position: absolute;
            right: -13px;
            top: 0;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--primary);
            border: 3px solid var(--secondary);
        }

        .phase-title {
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 6px;
        }

        .phase-desc {
            font-size: 0.95rem;
            color: var(--text-muted);
            line-height: 1.6;
        }

        /* Footer */
        .site-footer {
            background: linear-gradient(145deg, #2E0B17 0%, #541228 45%, #1F0710 100%);
            border-top: 3px solid var(--secondary);
            color: #FFFFFF;
            padding: 70px 25px 35px;
            position: relative;
        }

        .footer-top {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 40px;
            max-width: 1400px;
            margin: 0 auto 50px;
        }

        .footer-brand h3 {
            color: var(--secondary);
            font-size: 1.6rem;
            margin-bottom: 12px;
        }

        .footer-brand p {
            color: rgba(255, 255, 255, 0.7);
            max-width: 500px;
            line-height: 1.8;
        }

        .footer-contacts h4, .footer-supervision h4 {
            color: #FFFFFF;
            font-size: 1.15rem;
            margin-bottom: 18px;
            border-bottom: 2px solid var(--secondary);
            padding-bottom: 6px;
            display: inline-block;
        }

        .footer-contacts ul {
            list-style: none;
        }

        .footer-contacts li {
            margin-bottom: 12px;
            color: rgba(255, 255, 255, 0.8);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .footer-contacts i {
            color: var(--secondary);
            font-size: 1.1rem;
        }

        .footer-bottom {
            max-width: 1400px;
            margin: 0 auto;
            text-align: center;
            padding-top: 25px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.9rem;
        }

        /* Responsive Breakpoints */
        @media (max-width: 1100px) {
            .kpi-row, .grid-4 { grid-template-columns: repeat(2, 1fr); }
            .royal-grid, .grid-3 { grid-template-columns: repeat(2, 1fr); }
            .hero-main-title { font-size: 2.8rem; }
        }

        @media (max-width: 768px) {
            .nav-pill { padding: 8px 16px; gap: 8px; }
            .nav-links { display: none; }
            .hero-main-title { font-size: 2.2rem; }
            .hero-meta-grid { grid-template-columns: 1fr; gap: 15px; }
            .royal-grid, .grid-2, .grid-3, .grid-4, .kpi-row { grid-template-columns: 1fr; }
            .footer-top { grid-template-columns: 1fr; gap: 30px; }
            .section-wrapper { padding: 60px 15px; }
        }

        /* Print Media Styles */
        @media print {
            .header-nav, .btn-print, .nav-wrapper, .floating-nav { display: none !important; visibility: hidden !important; }
            * {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
                color-adjust: exact !important;
            }
            body { background: #FAFAF7 !important; color: #1E1A1C !important; font-size: 11pt !important; margin: 0 !important; }
            .hero-section { min-height: auto !important; padding: 50px 20px !important; background: #6B1D3A !important; -webkit-print-color-adjust: exact !important; page-break-after: always !important; }
            .bezel-card, .custom-table-card, .speech-card, .royal-card { box-shadow: none !important; border: 1px solid #CCC !important; page-break-inside: avoid !important; }
            .section-wrapper { padding: 30px 15px !important; }
            table { page-break-inside: auto !important; }
            tr { page-break-inside: avoid !important; }
            thead { display: table-header-group !important; }
            @page { size: A4 landscape; margin: 0.8cm 0.8cm; }
        }
    </style>
</head>
<body>

    <!-- Floating Navigation Bar -->
    <div class="header-nav">
        <div class="nav-pill">
            <a href="#cover" class="nav-brand">
                <i class="fas fa-heart-pulse"></i>
                <span>طبيبي</span>
            </a>
            <ul class="nav-links">
                <li><a href="#summary">الملخص</a></li>
                <li><a href="#kpi-matrix">مؤشرات الأداء</a></li>
                <li><a href="#finance">الأداء المالي</a></li>
                <li><a href="#medical-programs">البرامج الطبية</a></li>
                <li><a href="#partnerships">الشراكات</a></li>
                <li><a href="#governance">الحوكمة والتطلعات</a></li>
                <li><a href="#appendices">الملاحق</a></li>
            </ul>
            <div class="nav-actions">
                <button class="btn-print" onclick="window.print()">
                    <i class="fas fa-print"></i>
                    <span>طباعة التقرير</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Section 1: Hero / Cover -->
    <section id="cover" class="hero-section">
        <div class="hero-pattern"></div>
        <div class="hero-decor-orb"></div>
        <div class="hero-content">
            <div class="hero-logo-badge">
                <i class="fas fa-hand-holding-medical"></i>
            </div>
            <div class="hero-entity-title">جمعية طبيبي الأهلية بالمدينة المنورة</div>
            <div class="hero-entity-sub">TABIBI Civil Association | ترخيص رقم: ١٠٠٠٧٣٠٧٠٠</div>
            
            <h1 class="hero-main-title">التقرير النصف سنوي الشامل</h1>
            <div class="hero-period-tag">
                <i class="fas fa-calendar-alt" style="margin-left: 8px; color: var(--secondary);"></i>
                الفترة من ١ يناير إلى ٣٠ يونيو ٢٠٢٦م
            </div>

            <div class="hero-motto-strip">
                <span>ثقة</span>
                <i class="fas fa-circle"></i>
                <span>أثر</span>
                <i class="fas fa-circle"></i>
                <span>استدامة</span>
            </div>

            <div class="hero-meta-grid">
                <div class="hero-meta-item">
                    <strong>الجهة المشرفة</strong>
                    المركز الوطني لتنمية القطاع غير الربحي
                </div>
                <div class="hero-meta-item">
                    <strong>القطاع الصحي</strong>
                    تجمع المدينة المنورة الصحي & وزارة الصحة
                </div>
                <div class="hero-meta-item">
                    <strong>الإشراف والتحرير</strong>
                    أ. بيان بن سعد المحمدي - المدير التنفيذي
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Royal Leadership Page -->
    <section class="royal-section">
        <div class="section-header">
            <span class="section-eyebrow">الرؤية والتمكين</span>
            <h2 class="section-title">القيادة الرشيدة</h2>
            <p class="section-desc">نسترشد بتوجيهات قيادتنا الحكيمة في ترسيخ مساهمة القطاع غير الربحي في الرعاية الصحية وتحقيق جودة الحياة</p>
        </div>

        <div class="royal-grid">
            <!-- Crown Prince Mohammed bin Salman (Right) -->
            <div class="royal-card">
                <div>
                    <div class="royal-emblem">
                        <img src="assets/images/crown_prince.jpg" alt="الأمير محمد بن سلمان">
                    </div>
                    <h3>صاحب السمو الملكي</h3>
                    <div class="royal-role">الأمير محمد بن سلمان بن عبدالعزيز آل سعود<br><small>ولي العهد رئيس مجلس الوزراء</small></div>
                </div>
                <div class="royal-quote">
                    «نهدف للوصول إلى قطاع غير ربحي مهم، مبادر وداعم ومؤثر في التعليم والصحة والثقافة والمجالات البحثية، وسنعتمد عليه بشكل رئيسي.»
                </div>
            </div>

            <!-- King Salman (Center / Middle) -->
            <div class="royal-card" style="border: 2px solid var(--secondary); box-shadow: 0 10px 30px rgba(201, 169, 110, 0.25);">
                <div>
                    <div class="royal-emblem" style="width:135px; height:135px; border-width:3.5px;">
                        <img src="assets/images/king_salman.jpg" alt="الملك سلمان بن عبدالعزيز">
                    </div>
                    <h3 style="font-size:1.4rem;">خادم الحرمين الشريفين</h3>
                    <div class="royal-role" style="font-weight:700;">الملك سلمان بن عبدالعزيز آل سعود</div>
                </div>
                <div class="royal-quote">
                    «ما يميز هذه البلاد هو حرص قادتها على الخير والتشجيع عليه، وما نراه من مؤسسات خيرية في مختلف المجالات… إلا جانبًا من الجوانب المشرقة لبلادنا.»
                </div>
            </div>

            <!-- Prince Salman bin Sultan (Left) -->
            <div class="royal-card">
                <div>
                    <div class="royal-emblem">
                        <img src="assets/images/prince_salman.jpg" alt="الأمير سلمان بن سلطان">
                    </div>
                    <h3>صاحب السمو الملكي</h3>
                    <div class="royal-role">الأمير سلمان بن سلطان بن عبدالعزيز آل سعود<br><small>أمير منطقة المدينة المنورة</small></div>
                </div>
                <div class="royal-quote">
                    «نسعد بالإنجازات التي حققتها الجمعيات الأهلية على مستوى المنطقة باعتبارها شريكًا استراتيجيًا للقطاعين العام والخاص في تحسين جودة الحياة وتعزيز الاستقرار الاجتماعي والاقتصادي.»
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Chairman's Address & Board -->
    <div class="section-wrapper" id="summary">
        <div class="section-header">
            <span class="section-eyebrow">رسالة القيادة المؤسسية</span>
            <h2 class="section-title">كلمة رئيس مجلس الإدارة</h2>
        </div>

        <div class="speech-card">
            <i class="fas fa-quote-right speech-quote-icon"></i>
            <div class="speech-content">
                <p><strong>الحمد لله رب العالمين، والصلاة والسلام على نبينا محمد وعلى آله وصحبه أجمعين.. وبعد:</strong></p>
                <p>يسرني أن أضع بين أيديكم التقرير النصف سنوي لجمعية طبيبي الأهلية، والذي يعكس ما تحقق خلال النصف الأول من عام ٢٠٢٦م من نمو مالي وتشغيلي، وتطور في البنية المؤسسية والحوكمة، وتوسع في الخدمات المقدمة للمستفيدين المرضى في طيبة الطيبة.</p>
                <p>وما تحقق من إنجازات - بعد توفيق الله - هو ثمرة تكامل جهود مجلس الإدارة والجمعية العمومية والإدارة التنفيذية والعاملين والمتطوعين، ودعم الشركاء والمانحين الأفاضل الذين نعتز بثقتهم وإسهامهم في رسالة الجمعية التنموية والإنسانية.</p>
                <p>وننظر إلى هذا التقرير بوصفه أداة للتقييم والتطوير المستمر، لا مجرد عرض للمنجزات؛ بما يساعد على تحديد أولويات المرحلة القادمة، وتعزيز الاستدامة المالية، ورفع الأثر الصحي والاجتماعي المحقق للمستفيدين.</p>
            </div>
            <div class="speech-author">
                <div class="speech-author-info">
                    <h4>أ.د. منصور محمد النزهة</h4>
                    <p>رئيس مجلس الإدارة | جمعية طبيبي الأهلية</p>
                </div>
            </div>
        </div>

        <!-- Board Members Cards -->
        <div class="section-header" style="margin-top: 50px;">
            <span class="section-eyebrow">الحوكمة والرقابة</span>
            <h2 class="section-title" style="font-size: 1.9rem;">مجلس الإدارة (٩ أعضاء)</h2>
        </div>
        <div class="grid-3">
            <div class="bezel-card"><div class="bezel-core" style="text-align: center; padding: 25px;">
                <div style="width:70px; height:70px; border-radius:50%; background:rgba(107,29,58,0.08); color:var(--primary); display:flex; align-items:center; justify-content:center; font-size:1.8rem; margin:0 auto 12px;"><i class="fas fa-user-tie"></i></div>
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:4px;">أ.د. منصور محمد النزهة</h4>
                <p style="color:var(--secondary-dark); font-weight:700; font-size:0.9rem;">رئيس مجلس الإدارة</p>
            </div></div>

            <div class="bezel-card"><div class="bezel-core" style="text-align: center; padding: 25px;">
                <div style="width:70px; height:70px; border-radius:50%; background:rgba(107,29,58,0.08); color:var(--primary); display:flex; align-items:center; justify-content:center; font-size:1.8rem; margin:0 auto 12px;"><i class="fas fa-user-tie"></i></div>
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:4px;">نائب رئيس المجلس</h4>
                <p style="color:var(--secondary-dark); font-weight:700; font-size:0.9rem;">داعم مبادرة المقر والبرامج</p>
            </div></div>

            <div class="bezel-card"><div class="bezel-core" style="text-align: center; padding: 25px;">
                <div style="width:70px; height:70px; border-radius:50%; background:rgba(107,29,58,0.08); color:var(--primary); display:flex; align-items:center; justify-content:center; font-size:1.8rem; margin:0 auto 12px;"><i class="fas fa-users-cog"></i></div>
                <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:4px;">أعضاء مجلس الإدارة</h4>
                <p style="color:var(--text-muted); font-size:0.9rem;">٧ أعضاء ممثلين للجمعية العمومية ولجان الحوكمة</p>
            </div></div>
        </div>
    </div>

    <!-- Section 4: Master KPI Dashboard -->
    <div class="section-wrapper" id="kpi-matrix" style="background: #F4F1EA; border-radius: var(--radius-lg); margin-top: 40px; margin-bottom: 60px;">
        <div class="section-header">
            <span class="section-eyebrow">لوحة التحكم التفاعلية</span>
            <h2 class="section-title">مؤشرات الأداء الرئيسية الشاملة (KPIs)</h2>
            <p class="section-desc">مصفوفة القياس التراكمي والمقارن لتقييم الأداء المالي، الطبي، البشري، والحوكمي للنصف الأول ٢٠٢٦م</p>
        </div>

        <!-- KPI Category 1: Financial Performance -->
        <h3 style="color: var(--primary); font-size: 1.35rem; margin-bottom: 18px; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-coins" style="color: var(--secondary);"></i>
            <span>المؤشرات المالية والاستدامة</span>
        </h3>
        <div class="kpi-row">
            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-success"><i class="fas fa-arrow-trend-up"></i></div>
                <div class="kpi-label">نمو إجمالي الإيرادات</div>
                <div class="kpi-value">+١٩٢٪</div>
                <div><span class="kpi-badge badge-success"><i class="fas fa-check-double"></i> ٥٨٢,١٦٧ ريال</span></div>
                <div class="kpi-hint">مقارنة بـ ١٩٩,٤٧٤ ريال لنفس الفترة من عام ٢٠٢٥م</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-warning"><i class="fas fa-chart-pie"></i></div>
                <div class="kpi-label">تنفيذ الموازنة السنوية</div>
                <div class="kpi-value">٣٥.٥٧٪</div>
                <div><span class="kpi-badge badge-warning"><i class="fas fa-clock"></i> ١,٠٦٠,٦٦٦ ريال</span></div>
                <div class="kpi-hint">من مستهدف سنوي معتمد قدره ٢,٩٨١,٧٥٠ ريال</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-danger"><i class="fas fa-building-circle-exclamation"></i></div>
                <div class="kpi-label">نسبة المصاريف الإدارية</div>
                <div class="kpi-value">٥٣.٨٪</div>
                <div><span class="kpi-badge badge-danger"><i class="fas fa-exclamation-triangle"></i> تحتاج ترشيد</span></div>
                <div class="kpi-hint">المرتكزة في الرواتب والإيجار؛ المستهدف النظامي دون ٢٥٪</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-success"><i class="fas fa-vault"></i></div>
                <div class="kpi-label">تغطية الاحتياطي النقدي</div>
                <div class="kpi-value">١٢ شهر</div>
                <div><span class="kpi-badge badge-success"><i class="fas fa-shield-alt"></i> استقرار مالي آمن</span></div>
                <div class="kpi-hint">أرصدة بنكية ١,٠٠١,٧٥٤ ريال تغطي النفقات التشغيلية لعام كامل</div>
            </div></div>
        </div>

        <!-- KPI Category 2: Medical Impact & Satisfaction -->
        <h3 style="color: var(--primary); font-size: 1.35rem; margin-bottom: 18px; margin-top: 35px; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-hand-holding-medical" style="color: var(--secondary);"></i>
            <span>مؤشرات الأثر الطبي ورضا المستفيدين</span>
        </h3>
        <div class="kpi-row">
            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-success"><i class="fas fa-heart-pulse"></i></div>
                <div class="kpi-label">نمو المساعدات العلاجية</div>
                <div class="kpi-value">+٩٤٣٪</div>
                <div><span class="kpi-badge badge-success"><i class="fas fa-arrow-up"></i> ٢٠٨,٦٠٥ ريال</span></div>
                <div class="kpi-hint">مقابل ٢٠,٠٠٠ ريال فقط بالنصف الأول ٢٠٢٥م</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-warning"><i class="fas fa-filter-circle-dollar"></i></div>
                <div class="kpi-label">معدل قبول الحالات</div>
                <div class="kpi-value">٣٣.٣٪</div>
                <div><span class="kpi-badge badge-warning"><i class="fas fa-user-check"></i> ٧ حالات مدعومة</span></div>
                <div class="kpi-hint">من أصل ٢١ حالة متقدمة تمت دراستها وبحثها اجتماعياً</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-info"><i class="fas fa-receipt"></i></div>
                <div class="kpi-label">متوسط كلفة المريض</div>
                <div class="kpi-value">٢٩,٨٠١ ر.س</div>
                <div><span class="kpi-badge badge-info"><i class="fas fa-calculator"></i> تغطية عمليات كبرى</span></div>
                <div class="kpi-hint">تشمل أورام وسرطانات الدم والعظام والعمليات التخصصية</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-success"><i class="fas fa-face-smile-beam"></i></div>
                <div class="kpi-label">مؤشر التحسن والرضا</div>
                <div class="kpi-value">١٠٠٪</div>
                <div><span class="kpi-badge badge-success"><i class="fas fa-star"></i> أثر علاجي ناجح</span></div>
                <div class="kpi-hint">كافة الحالات المدعومة السبع تحسنت صحياً مع توثيق قصص الأثر</div>
            </div></div>
        </div>

        <!-- KPI Category 3: Institutional, HR & Governance -->
        <h3 style="color: var(--primary); font-size: 1.35rem; margin-bottom: 18px; margin-top: 35px; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-users-gear" style="color: var(--secondary);"></i>
            <span>الموارد البشرية والحوكمة وتنمية الموارد</span>
        </h3>
        <div class="kpi-row">
            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-success"><i class="fas fa-id-card-clip"></i></div>
                <div class="kpi-label">نسبة التوطين (السعودة)</div>
                <div class="kpi-value">١٠٠٪</div>
                <div><span class="kpi-badge badge-success"><i class="fas fa-flag"></i> كادر وطني مؤهل</span></div>
                <div class="kpi-hint">٣ موظفين رسميين + محاسب متعاون + مسؤول إعلام قيد الترسيم</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-info"><i class="fas fa-graduation-cap"></i></div>
                <div class="kpi-label">التدريب والتطوير</div>
                <div class="kpi-value">٨ دورات</div>
                <div><span class="kpi-badge badge-info"><i class="fas fa-award"></i> رفع الكفاءة</span></div>
                <div class="kpi-hint">استفاد منها موظفان خلال الفترة لتعزيز الجاهزية الإدارية</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-danger"><i class="fas fa-handshake-angle"></i></div>
                <div class="kpi-label">معدل تحويل المنح</div>
                <div class="kpi-value">٧.٤٪</div>
                <div><span class="kpi-badge badge-danger"><i class="fas fa-file-excel"></i> ٢ منحة مقبولة</span></div>
                <div class="kpi-hint">من أصل ٢٧ طلباً؛ العائق الرئيسي كان اشتراط درجة الحوكمة</div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <div class="kpi-icon-wrap kpi-icon-danger"><i class="fas fa-hand-holding-dollar"></i></div>
                <div class="kpi-label">تحصيل الذمم المدينة</div>
                <div class="kpi-value">٠٪</div>
                <div><span class="kpi-badge badge-danger"><i class="fas fa-triangle-exclamation"></i> ١٢,٠٠٠ ر.س معلقة</span></div>
                <div class="kpi-hint">اشتراكات عضوية غير مسددة لـ ١٢ عضواً تتطلب متابعة تحصيل</div>
            </div></div>
        </div>
    </div>

    <!-- Section 5: Financial Performance Deep Dive -->
    <div class="section-wrapper" id="finance">
        <div class="section-header">
            <span class="section-eyebrow">التحليل المالي المتعمق</span>
            <h2 class="section-title">الأداء المالي والموازنة التشغيلية</h2>
            <p class="section-desc">مقارنة شاملة بين المحقق الفعلي لعام ٢٠٢٦م والفترة المماثلة لعام ٢٠٢٥م مع بيان مصادر الدخل والمصروفات</p>
        </div>

        <!-- Revenue Comparison Table -->
        <div class="custom-table-card">
            <h3 style="color:var(--primary); margin-bottom:18px; display:flex; align-items:center; justify-content:space-between;">
                <span><i class="fas fa-table-list" style="color:var(--secondary); margin-left:8px;"></i> جدول مقارنة مصادر الدخل (H1 2026 vs H1 2025)</span>
                <span class="badge-success kpi-badge">صافي نمو الإيرادات: +١٩٢٪</span>
            </h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>بند الإيراد</th>
                        <th>النصف الأول ٢٠٢٦م (ريال)</th>
                        <th>النصف الأول ٢٠٢٥م (ريال)</th>
                        <th>قيمة التغير (ريال)</th>
                        <th>نسبة النمو</th>
                        <th>ملاحظات الأداء</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>أموال الزكاة</strong></td>
                        <td>٧٠,٠٠٠</td>
                        <td>٨٠,٠٠٠</td>
                        <td style="color:var(--danger);">-١٠,٠٠٠</td>
                        <td><span class="kpi-badge badge-danger">-١٣٪</span></td>
                        <td>مصروفة بالكامل في مصارفها الشرعية للمرضى</td>
                    </tr>
                    <tr>
                        <td><strong>علاج مقيد (مساعدات طبية)</strong></td>
                        <td>٧٥,٠٠٠</td>
                        <td>٢٥,٠٠٠</td>
                        <td style="color:var(--success);">+٥٠,٠٠٠</td>
                        <td><span class="kpi-badge badge-success">+٢٠٠٪</span></td>
                        <td>نمو التبرعات المشروطة لدعم العمليات والأدوية</td>
                    </tr>
                    <tr>
                        <td><strong>المتجر الإلكتروني</strong></td>
                        <td>١٠,٤٦٩</td>
                        <td>١٢٤</td>
                        <td style="color:var(--success);">+١٠,٣٤٥</td>
                        <td><span class="kpi-badge badge-success">+٨,٣٤٣٪</span></td>
                        <td>تفعيل قنوات الدفع الرقمية والحملات التسويقية</td>
                    </tr>
                    <tr>
                        <td><strong>منصة تبرع الوطنية</strong></td>
                        <td>١,٢٠٣</td>
                        <td>١٣,٧٨٦</td>
                        <td style="color:var(--warning);">-١٢,٥٨٣</td>
                        <td><span class="kpi-badge badge-warning">-٩١٪</span></td>
                        <td>تحول المنصة والتركيز على منصة إحسان الوطنية</td>
                    </tr>
                    <tr>
                        <td><strong>تبرعات ودعم عام</strong></td>
                        <td>٤٠٧,٤٩٥</td>
                        <td>٦٢,٥٦٤</td>
                        <td style="color:var(--success);">+٣٤٤,٩٣١</td>
                        <td><span class="kpi-badge badge-success">+٥٥١٪</span></td>
                        <td>بدعم رئيسي من كبار المانحين والأوقاف</td>
                    </tr>
                    <tr>
                        <td><strong>اشتراكات العضوية</strong></td>
                        <td>١٨,٠٠٠</td>
                        <td>١٨,٠٠٠</td>
                        <td>٠</td>
                        <td><span class="kpi-badge badge-info">٠٪</span></td>
                        <td>تحصيل مستقر لاشتراكات أعضاء الجمعية العمومية</td>
                    </tr>
                    <tr class="table-total-row">
                        <td>الإجمالي العام</td>
                        <td>٥٨٢,١٦٧</td>
                        <td>١٩٩,٤٧٤</td>
                        <td>+٣٨٢,٦٩٣</td>
                        <td>+١٩٢٪</td>
                        <td>المبلغ التفصيلي الدقيق: ٥٨٢,١٦٧.٥٢ ريال</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Budget Execution with Animated Visual Progress Bars -->
        <div class="grid-2">
            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); margin-bottom:20px;"><i class="fas fa-bullseye" style="color:var(--secondary); margin-left:8px;"></i> مستوى تنفيذ الموازنة التقديرية (٢٠٢٦م)</h3>
                
                <div class="progress-block">
                    <div class="progress-labels">
                        <span>التبرعات والدعم (الإيرادات)</span>
                        <span style="color:var(--primary);">٥٨٢,١٦٧ / ١,٥٢٧,٠٠٠ ريال (٤٠.٠٢٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 40.02%;"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-labels">
                        <span>المساعدات العلاجية للمرضى</span>
                        <span style="color:var(--primary);">٢٠٨,٦٠٥ / ٧٥٠,٠٠٠ ريال (٢٧.٨١٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 27.81%;"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-labels">
                        <span>الرواتب والأجور والكادر</span>
                        <span style="color:var(--primary);">١٤٤,٤٠٥ / ٤٧٢,٠٠٠ ريال (٣٠.٥٩٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 30.59%;"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-labels">
                        <span>المصروفات التشغيلية والإيجار</span>
                        <span style="color:var(--warning);">١٠٩,٨٦٩ / ١٤٢,٣٠٠ ريال (٧٧.٢١٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 77.21%; background: linear-gradient(90deg, #D9822B, #C0392B);"></div></div>
                </div>

                <div class="progress-block">
                    <div class="progress-labels">
                        <span>شراء الأصول والتجهيزات</span>
                        <span style="color:var(--danger);">١٥,٦٢١ / ١٩,٤٥٠ ريال (٨٠.٣١٪)</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 80.31%; background: linear-gradient(90deg, #C9A96E, #C0392B);"></div></div>
                </div>

                <div style="background:var(--bg-alt); padding:15px 20px; border-radius:var(--radius-sm); margin-top:25px; display:flex; justify-content:space-between; align-items:center;">
                    <div><strong>إجمالي المنفذ من الموازنة:</strong></div>
                    <div style="font-size:1.3rem; font-weight:900; color:var(--primary);">١,٠٦٠,٦٦٦ من ٢,٩٨١,٧٥٠ ريال (٣٥.٥٧٪)</div>
                </div>
            </div></div>

            <!-- Financial Position & Liquidity Structure -->
            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); margin-bottom:20px;"><i class="fas fa-building-columns" style="color:var(--secondary); margin-left:8px;"></i> هيكل المركز المالي والسيولة النقدية</h3>
                
                <div style="background:linear-gradient(135deg, var(--primary), var(--primary-dark)); color:#fff; padding:25px; border-radius:var(--radius-md); margin-bottom:20px;">
                    <div style="font-size:0.95rem; opacity:0.85; margin-bottom:5px;">إجمالي الأرصدة المصرفية المتوفرة:</div>
                    <div style="font-size:2.4rem; font-weight:900; color:var(--secondary-light);">١,٠٠١,٧٥٤ ر.س</div>
                    <div style="display:flex; justify-content:space-between; margin-top:15px; padding-top:15px; border-top:1px solid rgba(255,255,255,0.15); font-size:0.95rem;">
                        <span>البنك الأهلي السعودي: <strong>٩٣٠,٧٠٢ ريال</strong></span>
                        <span>مصرف الراجحي: <strong>٧١,٠٥٢ ريال</strong></span>
                    </div>
                </div>

                <div class="grid-2" style="gap:15px; margin-bottom:0;">
                    <div style="background:var(--bg-alt); padding:18px; border-radius:var(--radius-sm); text-align:center;">
                        <div style="font-size:0.88rem; color:var(--text-muted);">الأموال المقيدة (مخصصة)</div>
                        <div style="font-size:1.4rem; font-weight:800; color:var(--primary); margin-top:4px;">٣٦٧,٠٩٣ ر.س</div>
                        <div style="font-size:0.8rem; color:var(--text-light);">٣٦.٧٪ من السيولة</div>
                    </div>

                    <div style="background:var(--bg-alt); padding:18px; border-radius:var(--radius-sm); text-align:center;">
                        <div style="font-size:0.88rem; color:var(--text-muted);">الأموال غير المقيدة (عامة)</div>
                        <div style="font-size:1.4rem; font-weight:800; color:var(--success); margin-top:4px;">٦٣٤,٦٦١ ر.س</div>
                        <div style="font-size:0.8rem; color:var(--text-light);">٦٣.٣٪ من السيولة</div>
                    </div>
                </div>

                <div style="margin-top:20px; padding:15px; border-right:3px solid var(--secondary); background:rgba(201,169,110,0.08); border-radius:0 var(--radius-sm) var(--radius-sm) 0; font-size:0.92rem;">
                    <strong>صافي الأصول المحققة:</strong> ٩٧٢,٧١٣ ريال (رصيد بداية ٨٦٤,٠٤٥ + دخل ٥٨٢,١٦٧ - استخدامات ٤٧٣,٤٩٩ ريال).
                </div>
            </div></div>
        </div>

        <!-- Interactive Charts Grid -->
        <div class="grid-2">
            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); font-size:1.15rem;"><i class="fas fa-chart-column" style="color:var(--secondary); margin-left:8px;"></i> مقارنة نمو الإيرادات حسب القنوات (ريال)</h3>
                <div class="chart-box"><canvas id="revComparisonChart"></canvas></div>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); font-size:1.15rem;"><i class="fas fa-chart-pie" style="color:var(--secondary); margin-left:8px;"></i> توزيع النفقات والاستخدامات المالية (H1 2026)</h3>
                <div class="chart-box"><canvas id="expenseDistributionChart"></canvas></div>
            </div></div>
        </div>

        <!-- Operating Expenses Full Breakdown -->
        <div class="custom-table-card">
            <h3 style="color:var(--primary); margin-bottom:18px;"><i class="fas fa-file-invoice-dollar" style="color:var(--secondary); margin-left:8px;"></i> البيان التفصيلي للمصروفات التشغيلية (١٦ بنداً)</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>م</th>
                        <th>بند المصروف</th>
                        <th>المبلغ H1 2026 (ريال)</th>
                        <th>المبلغ H1 2025 (ريال)</th>
                        <th>نسبة التغير</th>
                        <th>الوزن النسبي</th>
                        <th>التبرير الإداري</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>١</td><td><strong>الرواتب الأساسية</strong></td><td>١٤٤,٤٠٥</td><td>٤٥,٢٦٤</td><td><span class="badge-danger kpi-badge">+٢١٩٪</span></td><td>٥٦.٨٪</td><td>توسيع الكادر الوظيفي واستقطاب المدير والمشرفة والموظفين</td></tr>
                    <tr><td>٢</td><td><strong>الإيجار المكتبي</strong></td><td>٦٣,٣٣٣</td><td>٣٥,٠٠٠</td><td><span class="badge-danger kpi-badge">+٨١٪</span></td><td>٢٤.٩٪</td><td>الانتقال لمقر جديد (وفر سنوي ٢٥,٠٠٠ ريال لاحقاً)</td></tr>
                    <tr><td>٣</td><td><strong>التأمينات الاجتماعية</strong></td><td>١٤,٧٦٨</td><td>٩,٩٨٠</td><td><span class="badge-danger kpi-badge">+٤٨٪</span></td><td>٥.٨٪</td><td>اشتراكات الموظفين السعوديين المسجلين بالتأمينات</td></tr>
                    <tr><td>٤</td><td><strong>أجور متعاونين</strong></td><td>١٣,٠٠٠</td><td>٩,٠٦٠</td><td><span class="badge-danger kpi-badge">+٤٣٪</span></td><td>٥.١٪</td><td>أتعاب محاسب متعاون وفريق مساند في التأسيس</td></tr>
                    <tr><td>٥</td><td><strong>المحاسب القانوني</strong></td><td>٤,٦٠٠</td><td>٠</td><td>—</td><td>١.٨٪</td><td>مراجعة واعتماد القوائم المالية لعام ٢٠٢٥م</td></tr>
                    <tr><td>٦</td><td><strong>الكهرباء والخدمات</strong></td><td>٣,٨٦٧</td><td>٠</td><td>—</td><td>١.٥٪</td><td>فواتير المقر الإداري المشغل حديثاً</td></tr>
                    <tr><td>٧</td><td><strong>تصميم وتطوير الموقع الإلكتروني</strong></td><td>٣,٠٠٠</td><td>٠</td><td>—</td><td>١.٢٪</td><td>بناء البوابة الرسمية وتحديث بيانات الحوكمة</td></tr>
                    <tr><td>٨</td><td><strong>نقل وتركيب الأصول للمقر</strong></td><td>٢,٤٣٠</td><td>٠</td><td>—</td><td>١.٠٪</td><td>تكاليف تجهيز ونقل الأثاث والمكيفات للمقر الجديد</td></tr>
                    <tr><td>٩</td><td><strong>الهاتف والإنترنت</strong></td><td>١,٣١٦</td><td>١,٣٤٢</td><td><span class="badge-success kpi-badge">-٢٪</span></td><td>٠.٥٪</td><td>خطوط الاتصال والإنترنت السحابي</td></tr>
                    <tr><td>١٠</td><td><strong>صيانة متنوعة</strong></td><td>١,٠٦٠</td><td>١,٣٩٣</td><td><span class="badge-success kpi-badge">-٢٤٪</span></td><td>٠.٤٪</td><td>صيانة دورية للأجهزة والمرافق</td></tr>
                    <tr><td>١١</td><td><strong>نظافة ومنظفات</strong></td><td>٩٠٠</td><td>٥٣١</td><td><span class="badge-danger kpi-badge">+٦٩٪</span></td><td>٠.٣٥٪</td><td>أدوات ومواد نظافة المقر الجديد</td></tr>
                    <tr><td>١٢</td><td><strong>طباعة ومطبوعات</strong></td><td>٥٠٨</td><td>٠</td><td>—</td><td>٠.٢٪</td><td>نماذج ولوائح ومستندات الجمعية الرسمية</td></tr>
                    <tr><td>١٣</td><td><strong>رسوم وعمولات مصرفية</strong></td><td>٣٨٠</td><td>٠</td><td>—</td><td>٠.١٥٪</td><td>رسوم العمليات البنكية والحوالات</td></tr>
                    <tr><td>١٤</td><td><strong>ضيافة واستقبال</strong></td><td>٣٧٥</td><td>٥٩٢</td><td><span class="badge-success kpi-badge">-٣٧٪</span></td><td>٠.١٥٪</td><td>ضيافة اجتماعات اللجان والزوار والمانحين</td></tr>
                    <tr><td>١٥</td><td><strong>أحبار طابعات</strong></td><td>١٨٠</td><td>٠</td><td>—</td><td>٠.٠٧٪</td><td>أحبار طابعة الليزر الجديدة</td></tr>
                    <tr><td>١٦</td><td><strong>أدوات مكتبية وقرطاسية</strong></td><td>١٥٢</td><td>٣٦٧</td><td><span class="badge-success kpi-badge">-٥٩٪</span></td><td>٠.٠٦٪</td><td>مستلزمات مكتبية استهلاكية</td></tr>
                    <tr class="table-total-row">
                        <td colspan="2">إجمالي المصروفات التشغيلية التفصيلية</td>
                        <td>٢٥٤,٢٧٤</td>
                        <td>٦٣,٥٣٦</td>
                        <td>+٣٠٠٪</td>
                        <td>١٠٠٪</td>
                        <td>الفارق مع ملخص النمو (٥,٠٠٠ ريال) قيد المطابقة الحسابية</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Section 6: Medical Programs & Patient Assistance -->
    <div class="section-wrapper" id="medical-programs" style="background: #FFFFFF; border-radius: var(--radius-lg); padding-top: 80px;">
        <div class="section-header">
            <span class="section-eyebrow">الرعاية والأثر الميداني</span>
            <h2 class="section-title">البرامج والخدمات الطبية للمستفيدين</h2>
            <p class="section-desc">تنفيذ برنامج "جودة حياة" لتقديم المساعدات العلاجية والعمليات الجراحية للمرضى الأشد حاجة بالمدينة المنورة</p>
        </div>

        <!-- 7 Supported Cases -->
        <h3 style="color:var(--primary); margin-bottom:25px; display:flex; align-items:center; justify-content:space-between;">
            <span><i class="fas fa-check-circle" style="color:var(--success); margin-left:8px;"></i> الحالات الطبية المدعومة بالنصف الأول (٧ حالات - ٢٠٨,٦٠٥.٣١ ريال)</span>
            <span class="badge-success kpi-badge">نسبة تحسن الحالات: ١٠٠٪</span>
        </h3>

        <div class="grid-2">
            <!-- Patient 1 -->
            <div class="bezel-card"><div class="bezel-core patient-card">
                <div class="patient-badge-cost">١٥٠,٠٠٠ ر.س</div>
                <div class="patient-name">فايز أحمد عبدالعزيز</div>
                <div class="patient-hospital"><i class="fas fa-hospital"></i> المستشفى السعودي الألماني</div>
                <div class="patient-diagnosis"><i class="fas fa-stethoscope"></i> التشخيص: سرطان الدم (علاج مناعي وكيماوي)</div>
                <p style="margin-top:12px; font-size:0.92rem; color:var(--text-muted);">تمت تغطية المرحلة العلاجية الحرجة واستقرار المؤشرات الحيوية للمريض بعد التدخل الطبي السريع.</p>
            </div></div>

            <!-- Patient 2 -->
            <div class="bezel-card"><div class="bezel-core patient-card">
                <div class="patient-badge-cost">٣٠,٠٠٠ ر.س</div>
                <div class="patient-name">زينب عمر علي</div>
                <div class="patient-hospital"><i class="fas fa-hospital"></i> المستشفى السعودي الألماني</div>
                <div class="patient-diagnosis"><i class="fas fa-stethoscope"></i> التشخيص: سرطان نخر العظم</div>
                <p style="margin-top:12px; font-size:0.92rem; color:var(--text-muted);">توفير العلاجات النوعية التخصصية وجلسات المتابعة الطبية المنتظمة بنجاح كامل.</p>
            </div></div>

            <!-- Patient 3 -->
            <div class="bezel-card"><div class="bezel-core patient-card">
                <div class="patient-badge-cost">٧,٠٠٠ ر.س</div>
                <div class="patient-name">كندفة محمد عتبة</div>
                <div class="patient-hospital"><i class="fas fa-hospital"></i> مدينة الملك سلمان الطبية</div>
                <div class="patient-diagnosis"><i class="fas fa-stethoscope"></i> التشخيص: تنويم ورعاية تحت الملاحظة الفائقة</div>
                <p style="margin-top:12px; font-size:0.92rem; color:var(--text-muted);">تغطية الفاتورة الطبية للمستفيدة وتحسن حالتها بعد خطاب إحالة المدينة الطبية وتجاوز الأزمة.</p>
            </div></div>

            <!-- Patient 4 -->
            <div class="bezel-card"><div class="bezel-core patient-card">
                <div class="patient-badge-cost">٧,٠٠٠ ر.س</div>
                <div class="patient-name">شوق حسن الأنور</div>
                <div class="patient-hospital"><i class="fas fa-hospital"></i> المستشفى السعودي الألماني</div>
                <div class="patient-diagnosis"><i class="fas fa-stethoscope"></i> التشخيص: إجراء منظار جراحي متقدم</div>
                <p style="margin-top:12px; font-size:0.92rem; color:var(--text-muted);">إجراء الفحص التداخلي بنجاح وتشخيص المسببات ووضع الخطة العلاجية الشافية بإذن الله.</p>
            </div></div>

            <!-- Patient 5 -->
            <div class="bezel-card"><div class="bezel-core patient-card">
                <div class="patient-badge-cost">٦,٣٥٠ ر.س</div>
                <div class="patient-name">سامية سليمان محمد</div>
                <div class="patient-hospital"><i class="fas fa-hospital"></i> مستشفى المواساة بالمدينة</div>
                <div class="patient-diagnosis"><i class="fas fa-stethoscope"></i> التشخيص: استئصال كتلة ورمية بالصدر</div>
                <p style="margin-top:12px; font-size:0.92rem; color:var(--text-muted);">إجراء العملية الجراحية بالكامل وشفاء المستفيدة وتقديمها رسالة شكر وعرفان للجمعية ومانحيها.</p>
            </div></div>

            <!-- Patient 6 & 7 combined -->
            <div class="bezel-card"><div class="bezel-core patient-card">
                <div class="patient-badge-cost">٨,٢٥٥.٣١ ر.س</div>
                <div class="patient-name">زبيدة شمس الدين & محمد الشرفي</div>
                <div class="patient-hospital"><i class="fas fa-hospital"></i> السعودي الألماني & مستشفى المواساة</div>
                <div class="patient-diagnosis"><i class="fas fa-stethoscope"></i> ورم قولون (٦,٣٣٠.٣١ ر.س) & أشعة رنين (١,٩٢٥ ر.س)</div>
                <p style="margin-top:12px; font-size:0.92rem; color:var(--text-muted);">تقديم التدخلات التشخيصية والعلاجية واستكمال البروتوكول الدوائي لحالتين من أشد المرضى حاجة.</p>
            </div></div>
        </div>

        <!-- Case Rejection Analysis & Governance Insights -->
        <div class="custom-table-card" style="margin-top: 40px;">
            <h3 style="color:var(--primary); margin-bottom:15px; display:flex; justify-content:space-between; align-items:center;">
                <span><i class="fas fa-user-xmark" style="color:var(--danger); margin-left:8px;"></i> تحليل الحالات الـ ١٤ غير المقبولة وأسباب عدم الصرف</span>
                <span class="badge-warning kpi-badge">توصية: تعديل لائحة المساعدات</span>
            </h3>
            <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:20px;">
                أظهرت دراسة طلبات المساعدة أن ٥٠٪ من أسباب الرفض ترجع لانتهاء صلاحية الإقامة، يليه التغطية من جمعيات أخرى أو وجود تأمين طبي سابق:
            </p>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>سبب عدم القبول</th>
                        <th>عدد الحالات</th>
                        <th>نسبة التمثيل</th>
                        <th>أبرز أسماء المستفيدين المتقدمين</th>
                        <th>الإجراء والتوصية المقترحة</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>انتهاء صلاحية الإقامة</strong></td>
                        <td>٧ حالات</td>
                        <td>٥٠.٠٪</td>
                        <td>بسمة هارون، سيد الأمين، فريدة عظيم، عطور عباس، هاجر الصادق، عبدالله دياب، أحمد خير</td>
                        <td>تنسيق مع المانحين لقبول الحالات الإنسانية الطارئة وتعديل اللائحة</td>
                    </tr>
                    <tr>
                        <td><strong>تغطية كاملة من جمعية أخرى</strong></td>
                        <td>حالتان</td>
                        <td>١٤.٣٪</td>
                        <td>هديباء عواده الجهني (مياه بيضاء)، علي قايد علي (قلب وشرايين)</td>
                        <td>تفعيل الربط الإلكتروني لمنع ازدواجية الدعم وتسريع خدمة مرضى آخرين</td>
                    </tr>
                    <tr>
                        <td><strong>أخطاء بالتقرير الطبي / اختلاف التشخيص</strong></td>
                        <td>حالتان</td>
                        <td>١٤.٣٪</td>
                        <td>ريم فواز زاده (ورم ليفي)، جوهرة منصور خان (أخطاء تقرير وتواريخ)</td>
                        <td>إرشاد المستفيد لتصحيح التقارير الطبية وإعادة الرفع عبر المستشفيات الشريكة</td>
                    </tr>
                    <tr>
                        <td><strong>وجود تأمين طبي ساري المفعول</strong></td>
                        <td>حالة واحدة</td>
                        <td>٧.١٪</td>
                        <td>فؤاد لطف محمد (ميلوما متعددة)</td>
                        <td>توجيه المستفيد للاستفادة من وثيقة التأمين المعتمدة لشركته</td>
                    </tr>
                    <tr>
                        <td><strong>انتهاء تأشيرة الزيارة وسفر المستفيد</strong></td>
                        <td>حالة واحدة</td>
                        <td>٧.١٪</td>
                        <td>حمزة محمد هندية (سكري نوع أول)</td>
                        <td>إغلاق الملف لانتفاء شرط الإقامة المحلية</td>
                    </tr>
                    <tr>
                        <td><strong>مقبولة ولم تستلم التعميد</strong></td>
                        <td>حالة واحدة</td>
                        <td>٧.١٪</td>
                        <td>مزاهر عبدالله الهادي (ضعف نظر)</td>
                        <td>متابعة التواصل لتسليم التعميد وبدء الخطة العلاجية فوراً</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Section 7: Healthcare Partnerships & Ecosystem -->
    <div class="section-wrapper" id="partnerships">
        <div class="section-header">
            <span class="section-eyebrow">التكامل والتحالفات الاستراتيجية</span>
            <h2 class="section-title">شبكة الشراكات الصحية والمؤسسية</h2>
            <p class="section-desc">عقدت جمعية طبيبي شراكات وتفاهمات فاعلة مع ٩ جهات ومستشفيات طبية رائدة لتقديم الرعاية بأعلى جودة وأفضل تسعيرة</p>
        </div>

        <div class="grid-3">
            <div class="partner-card">
                <i class="fas fa-hospital-user partner-icon"></i>
                <div class="partner-title">المستشفى السعودي الألماني</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">علاج الأورام وجراحات القلب والمناظير التخصصية</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-hospital partner-icon"></i>
                <div class="partner-title">مستشفى المواساة بالمدينة</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">العمليات الجراحية الدقيقة والرنين المغناطيسي</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-square-h partner-icon"></i>
                <div class="partner-title">مدينة الملك سلمان الطبية</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">الرعاية المرجعية المتقدمة والتنويم التخصصي</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-user-doctor partner-icon"></i>
                <div class="partner-title">مستشفى د. حامد الأحمدي</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">جراحات اليوم الواحد والعيادات الاستشارية</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-clinic-medical partner-icon"></i>
                <div class="partner-title">مستشفى المدينة الوطني</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">خدمات الطوارئ والملاحظة والتحاليل الطبية</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-house-medical partner-icon"></i>
                <div class="partner-title">مستشفى المدينة الطبي العام</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">الفحوصات العامة ورعاية الأمراض المزمنة</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-stethoscope partner-icon"></i>
                <div class="partner-title">مستشفى واد الطبي</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">علاج الإصابات الرياضية وجراحة العظام</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-briefcase-medical partner-icon"></i>
                <div class="partner-title">شركة مداواة ورعاية الطبية</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">توفير الأدوية والمستلزمات الطبية المنزلية</p>
            </div>

            <div class="partner-card">
                <i class="fas fa-wheelchair partner-icon"></i>
                <div class="partner-title">جمعية جَنَى لتأهيل المعاقات</div>
                <p style="font-size:0.88rem; color:var(--text-muted); margin-top:8px;">التأهيل الطبي والتكامل مع ذوي الإعاقة</p>
            </div>
        </div>

        <!-- Donors Breakdown & Grants Status -->
        <div class="grid-2" style="margin-top:30px;">
            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); margin-bottom:15px;"><i class="fas fa-hand-holding-dollar" style="color:var(--secondary); margin-left:8px;"></i> كبار المانحين والشركاء بالنصف الأول</h3>
                <ul style="list-style:none; line-height:2.4; font-size:0.95rem;">
                    <li><i class="fas fa-star" style="color:var(--secondary); margin-left:8px;"></i> <strong>سعد بن محمد حسين:</strong> ٢٥٠,٠٠٠ ريال (تبرع عام رئيسي)</li>
                    <li><i class="fas fa-check" style="color:var(--primary); margin-left:8px;"></i> <strong>أ. أسامة جعفر فقيه:</strong> ٥٠,٠٠٠ ريال (زكاة)</li>
                    <li><i class="fas fa-check" style="color:var(--primary); margin-left:8px;"></i> <strong>وقف الشيخ نغيمش الأحمدي:</strong> ٥٠,٠٠٠ ريال (٣٥ ألف علاج + ١٥ ألف عام)</li>
                    <li><i class="fas fa-check" style="color:var(--primary); margin-left:8px;"></i> <strong>وقف الشيخ عبدالقادر شيبة الحمد:</strong> ٥٠,٠٠٠ ريال (عام)</li>
                    <li><i class="fas fa-check" style="color:var(--primary); margin-left:8px;"></i> <strong>سلطان محمد الفقيهي:</strong> ٣٠,٠٠٠ ريال (عام)</li>
                    <li><i class="fas fa-check" style="color:var(--primary); margin-left:8px;"></i> <strong>مؤسسات أوقاف مانحة (أبو زيد، شيبة الحمد، طابة):</strong> ٦٠,٠٠٠ ريال</li>
                </ul>
            </div></div>

            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); margin-bottom:15px;"><i class="fas fa-chart-line-up" style="color:var(--secondary); margin-left:8px;"></i> مسارات تنمية الموارد والمنح (٢٧ طلباً)</h3>
                <div style="margin-bottom:15px;">
                    <div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:5px;">
                        <span>منح مقبولة ومحققة (٢ جهة)</span>
                        <span style="color:var(--success);">٤٠,٠٠٠ ريال</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 7.4%; background:var(--success);"></div></div>
                    <small style="color:var(--text-muted);">مؤسسة إبراهيم العنقري (٢٠ ألف) + وقف عبدالعزيز أبو زيد (٢٠ ألف)</small>
                </div>

                <div style="margin-bottom:15px;">
                    <div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:5px;">
                        <span>طلبات قيد الدراسة والمتابعة (١١ جهة)</span>
                        <span style="color:var(--warning);">صناديق وبنوك وشركات</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 40.7%; background:var(--warning);"></div></div>
                    <small style="color:var(--text-muted);">صندوق دعم الجمعيات، أوقاف الراجحي، بنك البلاد، بنك الرياض، ٦ شركات حجاج</small>
                </div>

                <div>
                    <div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:5px;">
                        <span>اعتذارات بسبب الموازنة أو الحوكمة (٨ جهات)</span>
                        <span style="color:var(--danger);">استعداد لـ Q1 2027</span>
                    </div>
                    <div class="progress-track"><div class="progress-bar-fill" style="width: 29.6%; background:var(--danger);"></div></div>
                    <small style="color:var(--text-muted);">أوقاف الضحيان، مؤسسة طلال، مؤسسة الماجد، شركة طيبة، فنادق مكة</small>
                </div>
            </div></div>
        </div>
    </div>

    <!-- Section 8: Governance, Systems & Future Outlook -->
    <div class="section-wrapper" id="governance">
        <div class="section-header">
            <span class="section-eyebrow">التحول المؤسسي والاستدامة</span>
            <h2 class="section-title">الحوكمة والأنظمة وخطة النصف الثاني</h2>
            <p class="section-desc">بناء البنية المؤسسية الرقمية وإطلاق مبادرات الاستدامة والتعاقد مع فريق استشاري تخصصي لتسريع الإنجاز</p>
        </div>

        <div class="grid-2">
            <!-- Systems & Administration -->
            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); margin-bottom:20px;"><i class="fas fa-cubes" style="color:var(--secondary); margin-left:8px;"></i> أبرز الإنجازات الإدارية والتقنية</h3>
                <ul style="list-style:none; line-height:2.3; font-size:0.95rem;">
                    <li><i class="fas fa-check-circle" style="color:var(--success); margin-left:8px;"></i> <strong>الانتقال لمقر جديد:</strong> بإيجار سنوي ٤٥,٠٠٠ ريال بدلاً من ٧٠,٠٠٠ ريال (وفر ٢٥,٠٠٠ ر.س).</li>
                    <li><i class="fas fa-check-circle" style="color:var(--success); margin-left:8px;"></i> <strong>نظام المحاسبة السحابي (قيود):</strong> بناء الشجرة المحاسبية الرسمية المعتمدة.</li>
                    <li><i class="fas fa-check-circle" style="color:var(--success); margin-left:8px;"></i> <strong>إقفال القوائم المالية ٢٠٢٥م:</strong> واعتمادها من المحاسب القانوني والمركز الوطني.</li>
                    <li><i class="fas fa-check-circle" style="color:var(--success); margin-left:8px;"></i> <strong>إعادة هيكلة اللجان:</strong> تقليصها إلى (اللجنة التنفيذية + لجنة المساعدات الطبية).</li>
                    <li><i class="fas fa-check-circle" style="color:var(--success); margin-left:8px;"></i> <strong>الأرشفة والصادر والوارد:</strong> تطبيق نظام أرشفة ورقية وإلكترونية متكاملة مع جرد الأصول.</li>
                </ul>
            </div></div>

            <!-- Future Outlook & 3-Phase Roadmap -->
            <div class="bezel-card"><div class="bezel-core">
                <h3 style="color:var(--primary); margin-bottom:20px;"><i class="fas fa-route" style="color:var(--secondary); margin-left:8px;"></i> خارطة طريق النصف الثاني ٢٠٢٦م (٣ مراحل)</h3>
                
                <div class="phase-step">
                    <div class="phase-bullet"></div>
                    <div class="phase-title">المرحلة ١: استكمال الحوكمة ومنصة نوى</div>
                    <div class="phase-desc">استيفاء متطلبات معيار الامتثال والحوكمة ورفع درجة التقييم المعتمدة، وتفعيل منصة نوى للمنح والشراكات.</div>
                </div>

                <div class="phase-step">
                    <div class="phase-bullet"></div>
                    <div class="phase-title">المرحلة ٢: تنمية الموارد وإطلاق "بطاقة طبيبي"</div>
                    <div class="phase-desc">تعديل لائحة المساعدات وإطلاق بطاقة طبيبي للخصومات الطبية وبناء قاعدة بيانات المانحين الاستراتيجيين.</div>
                </div>

                <div class="phase-step">
                    <div class="phase-bullet"></div>
                    <div class="phase-title">المرحلة ٣: الاستعداد للربع الأول ٢٠٢٧م</div>
                    <div class="phase-desc">تقديم الحقائب الاستثمارية للصناديق الكبرى والشركات التي أغلقت موازناتها، وتفعيل دور أعضاء الجمعية العمومية.</div>
                </div>
            </div></div>
        </div>
    </div>

    <!-- Section 9: Detailed Appendices (Full Original Data) -->
    <div class="section-wrapper" id="appendices">
        <div class="section-header">
            <span class="section-eyebrow">الوثائق والبيانات المعتمدة</span>
            <h2 class="section-title">الملاحق المالية والتفصيلية الكاملة</h2>
            <p class="section-desc">سجلات الداعمين التفصيلية، الذمم المدينة لاشتراكات العضوية، وبيان الأصول الثابتة المعتمد</p>
        </div>

        <!-- Appendix 1: All 22 Donors Complete Table -->
        <div class="custom-table-card">
            <h3 style="color:var(--primary); margin-bottom:18px;"><i class="fas fa-hand-holding-heart" style="color:var(--secondary); margin-left:8px;"></i> الملحق (١): بيان الداعمين التفصيلي لعام ٢٠٢٦م (٥٨٢,١٦٧.٥٢ ريال)</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>م</th>
                        <th>الجهة الداعمة / المانح</th>
                        <th>التاريخ</th>
                        <th>المبلغ (ريال)</th>
                        <th>مجال الدعم</th>
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
                    <tr class="table-total-row">
                        <td colspan="3">الإجمالي التراكمي المعتمد لبيان الداعمين</td>
                        <td>٥٨٢,١٦٧.٥٢</td>
                        <td>زكاة: ٧٠ ألف | علاج: ٨٥,٦٧١.٨٨ | عام: ٤٢٦,٤٩٥.٦٤</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Appendix 2: Fixed Assets Table -->
        <div class="custom-table-card" style="margin-bottom:0;">
            <h3 style="color:var(--primary); margin-bottom:15px;"><i class="fas fa-desktop" style="color:var(--secondary); margin-left:8px;"></i> الملحق (٢): بيان الأصول والتجهيزات المشتراة (٢٠٢٦م)</h3>
            <table class="data-table">
                <thead>
                    <tr><th>الأصل / التجهيز</th><th>العدد</th><th>التاريخ</th><th>القيمة (ريال)</th><th>المورد المعتمد</th></tr>
                </thead>
                <tbody>
                    <tr><td>طابعة ليزر ملون HP</td><td>١</td><td>١١/٠٥/٢٠٢٦</td><td>١,٣٥٠</td><td>شركة سمرة الرقمية</td></tr>
                    <tr><td>مكتب سكرتارية خشب بني</td><td>٦</td><td>٢٧/٠٦/٢٠٢٦</td><td>٤,٦٨٠</td><td>الصفوة الجديدة للأثاث</td></tr>
                    <tr><td>كرسي دوار جلد رصاصي</td><td>٦</td><td>٢٧/٠٦/٢٠٢٦</td><td>٢,٧٠٠</td><td>الصفوة الجديدة للأثاث</td></tr>
                    <tr><td>مكيفات أوجين ٢٤ وحدة</td><td>٣</td><td>٢٧/٠٦/٢٠٢٦</td><td>٤,٥٩٠.٨٠</td><td>محل بن بلال للأجهزة</td></tr>
                    <tr><td>خزينة حديدية للمستندات</td><td>١</td><td>٢٧/٠٦/٢٠٢٦</td><td>١,٢٥٠</td><td>الصفوة الجديدة للأثاث</td></tr>
                    <tr><td>كرسي انتظار كروم للمراجعين</td><td>٣</td><td>٢٧/٠٦/٢٠٢٦</td><td>١,٠٥٠</td><td>مؤسسة الشرق هوم</td></tr>
                    <tr class="table-total-row">
                        <td colspan="3">إجمالي مشتريات الأصول بالنصف الأول</td>
                        <td colspan="2">١٥,٦٢٠.٨٠ ريال (مقارنة بـ ٣٤,٧٧٥.٥٠ ريال في الفترة المماثلة)</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Section 10: Official Footer & Contact Details -->
    <footer class="site-footer" id="contact">
        <div class="footer-top">
            <div class="footer-brand">
                <h3>جمعية طبيبي الأهلية بالمدينة المنورة</h3>
                <p>جمعية صحية أهلية مسجلة بالمركز الوطني لتنمية القطاع غير الربحي برقم (١٠٠٠٧٣٠٧٠٠)، تهدف لتقديم المساعدات العلاجية والرعاية الصحية النوعية للمرضى الأشد حاجة في طيبة الطيبة.</p>
                <div style="margin-top:20px; display:flex; gap:15px; color:var(--secondary); font-size:1.3rem;">
                    <i class="fas fa-heart-pulse"></i>
                    <i class="fas fa-hand-holding-medical"></i>
                    <i class="fas fa-hospital-user"></i>
                </div>
            </div>

            <div class="footer-contacts">
                <h4>بيانات التواصل</h4>
                <ul>
                    <li><i class="fas fa-phone"></i> <span>00966555606347</span></li>
                    <li><i class="fas fa-envelope"></i> <span>tabibi2025med@gmail.com</span></li>
                    <li><i class="fas fa-location-dot"></i> <span>المدينة المنورة - حي الفتح</span></li>
                </ul>
            </div>

            <div class="footer-supervision">
                <h4>الجهات المشرفة والمنصات</h4>
                <ul style="list-style:none; line-height:2.2; color:rgba(255,255,255,0.75);">
                    <li>• المركز الوطني لتنمية القطاع غير الربحي</li>
                    <li>• وزارة الموارد البشرية والتنمية الاجتماعية</li>
                    <li>• وزارة الصحة & تجمع المدينة الصحي</li>
                    <li>• منصة إحسان & منصة شفاء & منصة نوى</li>
                </ul>
            </div>
        </div>

        <div class="footer-bottom">
            <p>جميع الحقوق محفوظة © جمعية طبيبي الأهلية بالمدينة المنورة ٢٠٢٦م | تم إعداد وإخراج التقرير بأعلى المعايير المهنية والتفاعلية</p>
        </div>
    </footer>

    <!-- Interactive Charts Initialization Scripts -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Chart defaults
            Chart.defaults.font.family = "'Cairo', sans-serif";
            Chart.defaults.color = '#555';

            // 1. Revenue Comparison Chart (Bar)
            const ctxRev = document.getElementById('revComparisonChart');
            if (ctxRev) {
                new Chart(ctxRev, {
                    type: 'bar',
                    data: {
                        labels: ['الزكاة', 'علاج مقيد', 'المتجر الإلكتروني', 'منصة تبرع', 'دعم عام', 'العضوية'],
                        datasets: [
                            {
                                label: 'النصف الأول ٢٠٢٦م',
                                data: [70000, 75000, 10469, 1203, 407495, 18000],
                                backgroundColor: '#6B1D3A',
                                borderRadius: 6
                            },
                            {
                                label: 'النصف الأول ٢٠٢٥م',
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

            // 2. Expense Distribution Chart (Doughnut)
            const ctxExp = document.getElementById('expenseDistributionChart');
            if (ctxExp) {
                new Chart(ctxExp, {
                    type: 'doughnut',
                    data: {
                        labels: ['المساعدات الطبية (البرامج)', 'الرواتب والأجور', 'الإيجار والمقر', 'التأمينات والمتعاونين', 'التجهيزات والأصول', 'مصروفات تشغيلية أخرى'],
                        datasets: [{
                            data: [208605, 144405, 63333, 27768, 15621, 18768],
                            backgroundColor: [
                                '#1E824C',
                                '#6B1D3A',
                                '#C9A96E',
                                '#9E2A54',
                                '#D9822B',
                                '#85929E'
                            ],
                            borderWidth: 2,
                            borderColor: '#FFFFFF'
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

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated clean full-data report successfully: {target_file} ({len(html_content):,} chars)")
