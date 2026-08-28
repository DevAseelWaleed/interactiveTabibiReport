# -*- coding: utf-8 -*-
"""
Update all deliverables with the verified Strategic & Operational Plan Audit findings:
- Overall Weighted Strategic Achievement: 32.72% (Needs Significant Improvement & Realignment)
- 4 Balanced Scorecard Perspectives (Medical Impact: 13.95%, Financial: 32.96%, Operations/Partnerships: 55.00%, Governance/Institutional: 60.00%)
- 14-Point Strategic Plan vs Actual Performance Matrix
- 10 Strategic Programs Portfolio Status (1 active, 9 inactive)
- Critical Gap Analysis (Beneficiary Chasm: 7 vs 36,606; Rejection Rate: 66.7%; Donor Concentration: 43%; Volunteer Drop)
- Actionable H2 2026 Strategic Recommendations Roadmap
"""
import sys, os, shutil
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"e:\Work\زبون تقرير نصف سنوي طبيبي"
v2_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور")
v1_dir = os.path.join(base_dir, "التقرير_الجديد")

print("Updating deliverables with verified strategic audit data...")
