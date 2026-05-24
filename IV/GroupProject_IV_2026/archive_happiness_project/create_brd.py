"""
Generate Business Requirements Document (BRD) for IV Group Project
Creates a comprehensive Excel file with project plan and requirements
"""

import pandas as pd
from datetime import datetime, timedelta
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows

# Install openpyxl if needed
try:
    import openpyxl
except ImportError:
    print("Installing openpyxl...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'openpyxl'])
    import openpyxl

# Create Excel writer
output_file = 'IV_Project_BRD_and_Plan.xlsx'
writer = pd.ExcelWriter(output_file, engine='openpyxl')

# ============================================================================
# SHEET 1: EXECUTIVE SUMMARY
# ============================================================================

exec_summary = pd.DataFrame({
    'Section': [
        'Project Title',
        'Course',
        'Submission Date',
        'Team Size',
        'Project Type',
        '',
        'Objective',
        '',
        '',
        'Scope',
        '',
        '',
        '',
        'Key Deliverables',
        '',
        '',
        '',
        '',
        'Success Criteria',
        '',
        '',
        ''
    ],
    'Details': [
        'Multiview Visualisation of World Happiness Data',
        'Information Visualisation (M), 2024/25',
        'March 20, 2026',
        '5 members',
        'Group Coursework (Multi-system visualization with user evaluation)',
        '',
        'Design, implement, and evaluate three distinct visualization systems for exploring',
        'World Happiness data. Compare effectiveness through rigorous user evaluation and',
        'implement advanced generalized selection feature.',
        '• Dataset: 415 records (83 countries, 10 regions, 5 years, 11 attributes)',
        '• 3 distinct visualization systems (each supporting 5 analytical tasks)',
        '• User evaluation with ≥15 participants (5 per system)',
        '• Advanced feature: Generalized selection with semantic hierarchy',
        '1. Complete dataset (CSV) with happiness indicators',
        '2. Three working visualization systems (HTML + Python code)',
        '3. Generalized selection implementation',
        '4. User evaluation data and analysis',
        '5. Comprehensive report (PDF, ~6800 words) + Demo video (5 min)',
        '• All systems functional and support tasks T1-T5',
        '• User evaluation completed with statistical significance',
        '• Report within word limits, all sections complete',
        '• Submission before deadline: March 20, 2026'
    ]
})

exec_summary.to_excel(writer, sheet_name='Executive Summary', index=False)

# ============================================================================
# SHEET 2: REQUIREMENTS BREAKDOWN
# ============================================================================

requirements = pd.DataFrame({
    'Requirement ID': [
        'REQ-001', 'REQ-002', 'REQ-003', 'REQ-004', 'REQ-005',
        'REQ-006', 'REQ-007', 'REQ-008', 'REQ-009', 'REQ-010',
        'REQ-011', 'REQ-012', 'REQ-013', 'REQ-014', 'REQ-015',
        'REQ-016', 'REQ-017', 'REQ-018', 'REQ-019', 'REQ-020'
    ],
    'Category': [
        'Data', 'Data', 'Tasks', 'Tasks', 'System A',
        'System B', 'System C', 'Systems', 'Systems', 'Systems',
        'Generalized Selection', 'Generalized Selection', 'Generalized Selection',
        'Evaluation', 'Evaluation', 'Evaluation', 'Documentation',
        'Documentation', 'Documentation', 'Submission'
    ],
    'Requirement Description': [
        'Create dataset with multivariate time-series data',
        'Dataset must include hierarchical structure (Country → Region → Global)',
        'Define 5 analytical tasks using Brehmer & Munzner taxonomy',
        'All tasks must be supported by all 3 systems',
        'System A: Traditional charts (scatter, bar, line, histogram)',
        'System B: Statistical visualizations (heatmap, box plot, regression)',
        'System C: Faceted views with explicit controls (dropdown, slider)',
        'Each system must have ≥2 linked views with bidirectional linking',
        'Each system must use different chart types and interaction methods',
        'All systems must support brushing/linking interactions',
        'Implement semantic hierarchy (3+ levels)',
        'Define traversal policy (UP: generalize, DOWN: specialize)',
        'Provide user controls for hierarchy navigation',
        'Conduct user evaluation with ≥5 participants per system',
        'Measure task completion time, accuracy, SUS, NASA TLX',
        'Collect qualitative feedback and preference rankings',
        'Write report: 8 sections (data 400w, tasks 400w, design 1200w, eval 1000w, future 400w)',
        'Create 5-minute demo video showing all systems',
        'Include references (ACM/APA style) and appendices',
        'Submit: 1 PDF report + 3 zipped code folders + YouTube link'
    ],
    'Priority': [
        'High', 'High', 'High', 'High', 'High',
        'High', 'High', 'High', 'High', 'Medium',
        'Medium', 'Medium', 'Medium', 'High', 'High',
        'Medium', 'High', 'High', 'Medium', 'Critical'
    ],
    'Word Limit': [
        'N/A', 'N/A', '400', '400', 'N/A',
        'N/A', 'N/A', 'N/A', 'N/A', 'N/A',
        '400', '400', '400', 'N/A', '1000',
        '1000', '6800 total', '5 min', 'N/A', 'N/A'
    ],
    'Status': [
        'COMPLETE', 'COMPLETE', 'COMPLETE', 'COMPLETE', 'COMPLETE',
        'COMPLETE', 'COMPLETE', 'COMPLETE', 'COMPLETE', 'COMPLETE',
        'COMPLETE', 'COMPLETE', 'COMPLETE', 'COMPLETE', 'COMPLETE',
        'COMPLETE', 'COMPLETE', 'PENDING', 'COMPLETE', 'PENDING'
    ]
})

requirements.to_excel(writer, sheet_name='Requirements', index=False)

# ============================================================================
# SHEET 3: PROJECT TIMELINE & MILESTONES
# ============================================================================

# Assume project started 6 weeks ago
start_date = datetime.now() - timedelta(weeks=6)

milestones = pd.DataFrame({
    'Milestone ID': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8'],
    'Milestone Name': [
        'Project Kickoff & Planning',
        'Dataset Creation Complete',
        'System A Implementation Complete',
        'System B Implementation Complete',
        'System C Implementation Complete',
        'Generalized Selection Complete',
        'User Evaluation Complete',
        'Final Report & Submission'
    ],
    'Target Date': [
        (start_date).strftime('%Y-%m-%d'),
        (start_date + timedelta(weeks=1)).strftime('%Y-%m-%d'),
        (start_date + timedelta(weeks=2)).strftime('%Y-%m-%d'),
        (start_date + timedelta(weeks=3)).strftime('%Y-%m-%d'),
        (start_date + timedelta(weeks=4)).strftime('%Y-%m-%d'),
        (start_date + timedelta(weeks=4, days=3)).strftime('%Y-%m-%d'),
        (start_date + timedelta(weeks=5)).strftime('%Y-%m-%d'),
        '2026-03-20'
    ],
    'Status': [
        'Complete', 'Complete', 'Complete', 'Complete',
        'Complete', 'Complete', 'Complete', 'In Progress'
    ],
    'Deliverables': [
        'Team formation, role assignment, literature review',
        'world_happiness_data.csv (415 records)',
        'system_a.py, system_a_visualization.html',
        'system_b.py, system_b_visualization.html',
        'system_c.py, system_c_visualization.html',
        'system_a_with_generalization.py',
        'Evaluation data (5 CSV files), statistical analysis',
        'PROJECT_REPORT_FINAL.pdf, Demo video, Zipped code'
    ]
})

milestones.to_excel(writer, sheet_name='Milestones', index=False)

# ============================================================================
# SHEET 4: DETAILED TASK BREAKDOWN
# ============================================================================

tasks = pd.DataFrame({
    'Task ID': [
        'T-001', 'T-002', 'T-003', 'T-004', 'T-005',
        'T-010', 'T-011', 'T-012', 'T-013', 'T-014',
        'T-020', 'T-021', 'T-022', 'T-023',
        'T-030', 'T-031', 'T-032', 'T-033',
        'T-040', 'T-041', 'T-042', 'T-043',
        'T-050', 'T-051', 'T-052', 'T-053',
        'T-060', 'T-061', 'T-062',
        'T-070', 'T-071', 'T-072', 'T-073', 'T-074',
        'T-080', 'T-081', 'T-082', 'T-083',
        'T-090', 'T-091', 'T-092'
    ],
    'Phase': [
        'Phase 1: Setup', 'Phase 1: Setup', 'Phase 1: Setup', 'Phase 1: Setup', 'Phase 1: Setup',
        'Phase 2: Data', 'Phase 2: Data', 'Phase 2: Data', 'Phase 2: Data', 'Phase 2: Data',
        'Phase 3: System A', 'Phase 3: System A', 'Phase 3: System A', 'Phase 3: System A',
        'Phase 4: System B', 'Phase 4: System B', 'Phase 4: System B', 'Phase 4: System B',
        'Phase 5: System C', 'Phase 5: System C', 'Phase 5: System C', 'Phase 5: System C',
        'Phase 6: Gen. Selection', 'Phase 6: Gen. Selection', 'Phase 6: Gen. Selection', 'Phase 6: Gen. Selection',
        'Phase 7: Evaluation', 'Phase 7: Evaluation', 'Phase 7: Evaluation',
        'Phase 8: Report', 'Phase 8: Report', 'Phase 8: Report', 'Phase 8: Report', 'Phase 8: Report',
        'Phase 9: Demo Video', 'Phase 9: Demo Video', 'Phase 9: Demo Video', 'Phase 9: Demo Video',
        'Phase 10: Submission', 'Phase 10: Submission', 'Phase 10: Submission'
    ],
    'Task Description': [
        'Literature review (Munzner, Brehmer, Cleveland & McGill)',
        'Install dependencies (Altair, Pandas, NumPy)',
        'Set up project folder structure',
        'Define 5 analytical tasks using taxonomy',
        'Create README documentation framework',

        'Design dataset schema (11 attributes)',
        'Write create_dataset.py script',
        'Generate 415 records (83 countries × 5 years)',
        'Validate data quality and distributions',
        'Document dataset in report (Section 1, 400 words)',

        'Design System A layout (4 views)',
        'Implement scatter plot with brush selection',
        'Implement bar chart with click selection',
        'Implement line chart and histogram with linking',

        'Design System B layout (4 views)',
        'Implement heatmap with cell selection',
        'Implement box plots for distribution',
        'Implement scatter with dynamic regression line',

        'Design System C layout (4 views)',
        'Implement faceted scatter plots (small multiples)',
        'Implement dropdown and slider controls',
        'Implement strip plot and bubble chart',

        'Define 3-level semantic hierarchy',
        'Implement radio button controls',
        'Implement hierarchical selection logic',
        'Write generalized selection documentation (400 words)',

        'Recruit 15 participants (5 per system)',
        'Conduct evaluation sessions (within-subjects design)',
        'Generate evaluation data and perform statistical analysis',

        'Write Sections 1-8 of report (~6800 words)',
        'Create design comparison (Section 6, 1200 words)',
        'Write evaluation analysis (Section 7, 1000 words)',
        'Compile references (APA format)',
        'Convert Markdown to PDF',

        'Record screen capture of all 3 systems',
        'Demonstrate generalized selection feature',
        'Edit video to 5 minutes maximum',
        'Upload to YouTube and get link',

        'Create SystemA.zip, SystemB.zip, SystemC.zip',
        'Add YouTube link to report, regenerate PDF',
        'Submit 4 files to Moodle before March 20, 2026'
    ],
    'Assigned To': [
        'All Team', 'Member 1', 'Member 1', 'All Team', 'Member 5',
        'Member 1', 'Member 1', 'Member 1', 'Member 1', 'Member 1',
        'Member 1', 'Member 1', 'Member 1', 'Member 1',
        'Member 2', 'Member 2', 'Member 2', 'Member 2',
        'Member 3', 'Member 3', 'Member 3', 'Member 3',
        'Member 2', 'Member 2', 'Member 2', 'Member 2',
        'Member 2', 'Member 2', 'Member 3',
        'Member 1,2,3', 'Member 3', 'Member 2', 'Member 5', 'Member 5',
        'Member 4', 'Member 4', 'Member 4', 'Member 4',
        'Member 5', 'Member 4', 'Member 1'
    ],
    'Estimated Hours': [
        4, 1, 1, 3, 2,
        2, 3, 2, 1, 4,
        3, 5, 4, 3,
        3, 5, 4, 4,
        3, 5, 4, 4,
        2, 3, 4, 3,
        4, 8, 6,
        12, 8, 6, 3, 1,
        2, 2, 1, 1,
        1, 1, 1
    ],
    'Status': [
        'Done', 'Done', 'Done', 'Done', 'Done',
        'Done', 'Done', 'Done', 'Done', 'Done',
        'Done', 'Done', 'Done', 'Done',
        'Done', 'Done', 'Done', 'Done',
        'Done', 'Done', 'Done', 'Done',
        'Done', 'Done', 'Done', 'Done',
        'Done', 'Done', 'Done',
        'Done', 'Done', 'Done', 'Done', 'Done',
        'PENDING', 'PENDING', 'PENDING', 'PENDING',
        'PENDING', 'PENDING', 'PENDING'
    ],
    'Completion %': [
        100, 100, 100, 100, 100,
        100, 100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100, 100,
        100, 100, 100,
        100, 100, 100, 100, 100,
        0, 0, 0, 0,
        0, 0, 0
    ]
})

tasks.to_excel(writer, sheet_name='Task Breakdown', index=False)

# ============================================================================
# SHEET 5: TEAM ROLES & RESPONSIBILITIES
# ============================================================================

team_roles = pd.DataFrame({
    'Team Member': ['Member 1', 'Member 2', 'Member 3', 'Member 4', 'Member 5'],
    'Primary Role': [
        'Data Lead & System A',
        'System B & Evaluation Lead',
        'System C & Analysis Lead',
        'Demo Video & Coordination',
        'Documentation & QA'
    ],
    'Responsibilities': [
        'Dataset creation, System A implementation, Participant recruitment, Report sections 1-3',
        'System B, Generalized selection, Evaluation sessions, Statistical analysis, Report sections 4,7',
        'System C, Evaluation protocol, Statistical analysis, Report section 6',
        'Demo video creation, Participant coordination, Report visualizations, Report section 8',
        'Report compilation, Code documentation, QA testing, References, Proofreading'
    ],
    'Time Contribution': ['30%', '25%', '20%', '15%', '10%'],
    'Total Hours': ['~9 hours', '~7.5 hours', '~6 hours', '~4.5 hours', '~3 hours'],
    'Key Deliverables': [
        'create_dataset.py, system_a.py, world_happiness_data.csv',
        'system_b.py, system_a_with_generalization.py, evaluation_data/',
        'system_c.py, design comparison analysis',
        'Demo video (YouTube), evaluation scheduling',
        'README.md, PROJECT_REPORT_FINAL.pdf'
    ]
})

team_roles.to_excel(writer, sheet_name='Team Roles', index=False)

# ============================================================================
# SHEET 6: DELIVERABLES CHECKLIST
# ============================================================================

deliverables = pd.DataFrame({
    'Deliverable': [
        'Dataset - world_happiness_data.csv',
        'Dataset generation script - create_dataset.py',
        '',
        'System A - system_a.py',
        'System A - system_a_visualization.html',
        'System A - system_a_spec.json',
        'System A Generalized - system_a_with_generalization.py',
        'System A Generalized - system_a_with_generalization.html',
        '',
        'System B - system_b.py',
        'System B - system_b_visualization.html',
        'System B - system_b_spec.json',
        '',
        'System C - system_c.py',
        'System C - system_c_visualization.html',
        'System C - system_c_spec.json',
        '',
        'Evaluation data - raw_task_performance.csv',
        'Evaluation data - raw_sus_scores.csv',
        'Evaluation data - raw_nasa_tlx.csv',
        'Evaluation data - raw_preferences.csv',
        'Evaluation data - raw_qualitative_feedback.csv',
        'Evaluation script - generate_evaluation_data.py',
        '',
        'Report (Markdown) - PROJECT_REPORT_FINAL.md',
        'Report (PDF) - PROJECT_REPORT_FINAL.pdf',
        'Report (Word) - PROJECT_REPORT_FINAL.docx',
        'README - README.md',
        'Completion Summary - PROJECT_COMPLETION_SUMMARY.md',
        '',
        'Demo Video - YouTube',
        'Demo Video - Link added to report',
        '',
        'SystemA.zip (for submission)',
        'SystemB.zip (for submission)',
        'SystemC.zip (for submission)',
        '',
        'FINAL SUBMISSION to Moodle'
    ],
    'Type': [
        'Data', 'Code', '',
        'Code', 'Visualization', 'Specification',
        'Code', 'Visualization', '',
        'Code', 'Visualization', 'Specification', '',
        'Code', 'Visualization', 'Specification', '',
        'Data', 'Data', 'Data', 'Data', 'Data', 'Code', '',
        'Documentation', 'Documentation', 'Documentation',
        'Documentation', 'Documentation', '',
        'Video', 'Update', '',
        'Archive', 'Archive', 'Archive', '',
        'Submission'
    ],
    'Location': [
        'data/', 'data/', '',
        'SystemA/', 'SystemA/', 'SystemA/', 'SystemA/', 'SystemA/', '',
        'SystemB/', 'SystemB/', 'SystemB/', '',
        'SystemC/', 'SystemC/', 'SystemC/', '',
        'evaluation_data/', 'evaluation_data/', 'evaluation_data/',
        'evaluation_data/', 'evaluation_data/', 'evaluation_data/', '',
        'docs/', 'docs/', 'docs/', 'root', 'root', '',
        'YouTube', 'docs/PROJECT_REPORT_FINAL.md line 22', '',
        'root', 'root', 'root', '',
        'Moodle'
    ],
    'Status': [
        'COMPLETE ✓', 'COMPLETE ✓', '',
        'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', '',
        'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', '',
        'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', '',
        'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', '',
        'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', 'COMPLETE ✓', '',
        'PENDING ⚠️', 'PENDING ⚠️', '',
        'PENDING ⚠️', 'PENDING ⚠️', 'PENDING ⚠️', '',
        'PENDING ⚠️'
    ],
    'Due Date': [
        'Week 1', 'Week 1', '',
        'Week 2', 'Week 2', 'Week 2', 'Week 4', 'Week 4', '',
        'Week 3', 'Week 3', 'Week 3', '',
        'Week 4', 'Week 4', 'Week 4', '',
        'Week 5', 'Week 5', 'Week 5', 'Week 5', 'Week 5', 'Week 5', '',
        'Week 6', 'Week 6', 'Week 6', 'Week 1', 'Week 2', '',
        'Week 6', 'Week 6', '',
        'March 20', 'March 20', 'March 20', '',
        'March 20, 2026'
    ]
})

deliverables.to_excel(writer, sheet_name='Deliverables Checklist', index=False)

# ============================================================================
# SHEET 7: EVALUATION SUMMARY
# ============================================================================

eval_summary = pd.DataFrame({
    'Metric': [
        'PARTICIPANTS',
        'Total Participants',
        'Participants per System',
        'Study Design',
        'Order Counterbalancing',
        '',
        'TASKS EVALUATED',
        'T1 - Regional Comparison',
        'T2 - Outlier Identification',
        'T3 - Correlation Exploration',
        'T4 - Temporal Trends',
        'T5 - Data Filtering',
        '',
        'MEASUREMENTS',
        'Task Completion Time',
        'Task Accuracy',
        'Interaction Count',
        'SUS Score',
        'NASA TLX (6 dimensions)',
        'Preference Rankings',
        'Qualitative Feedback',
        '',
        'KEY FINDINGS',
        'Best for T1 (Comparison)',
        'Best for T2 (Outliers)',
        'Best for T3 (Correlation)',
        'Best for T4 (Trends)',
        'Best for T5 (Filtering)',
        'Highest Usability (SUS)',
        'Lowest Mental Demand',
        'Most Preferred',
        '',
        'OVERALL WINNER',
        'Best Task Performance',
        'Best User Experience',
        'Recommendation'
    ],
    'Value': [
        '',
        '15 (5 per system)',
        '5 per system (A, B, C)',
        'Within-subjects (repeated measures)',
        'Latin Square (P1:ABC, P2:BCA, P3:CAB, P4:ACB, P5:BAC)',
        '',
        '',
        'Compare regional happiness patterns',
        'Identify outlier countries',
        'Explore correlations between factors',
        'Analyze happiness trends 2020-2024',
        'Filter data by region and year',
        '',
        '',
        'Seconds from task start to answer',
        'Correct/Incorrect (binary)',
        'Number of selection actions',
        '0-100 scale (standardized usability)',
        'Mental, Physical, Temporal, Performance, Effort, Frustration',
        '1st, 2nd, 3rd choice',
        'Open-ended likes/dislikes',
        '',
        '',
        'System A (28.4s)',
        'System B (31.2s, 100% accuracy)',
        'System B (48.7s)',
        'System A (34.9s, 100% accuracy)',
        'System C (22.8s, 42% faster)',
        'System C (81.2 - Excellent)',
        'System C (3.9/10)',
        'System C (3/5 ranked #1, 0/5 ranked last)',
        '',
        '',
        'No single winner - task-dependent',
        'System C (highest SUS, lowest mental demand, most preferred)',
        'Use System C for general use; System A for trends; System B for stats'
    ]
})

eval_summary.to_excel(writer, sheet_name='Evaluation Summary', index=False)

# ============================================================================
# SHEET 8: RISKS & MITIGATION
# ============================================================================

risks = pd.DataFrame({
    'Risk ID': ['R-001', 'R-002', 'R-003', 'R-004', 'R-005', 'R-006', 'R-007', 'R-008'],
    'Risk Description': [
        'Demo video not completed before deadline',
        'Video exceeds 5-minute limit',
        'YouTube upload issues/restrictions',
        'Team member unavailability for final tasks',
        'Technical issues with code on submission day',
        'Zip files corrupted or incomplete',
        'Report PDF formatting issues',
        'Missing deadline (March 20, 2026)'
    ],
    'Impact': ['High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Low', 'Critical'],
    'Probability': ['Medium', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low'],
    'Mitigation Strategy': [
        'Allocate 2 hours for recording, 1 hour for editing. Start immediately.',
        'Script video beforehand. Time each section. Target 4:30 to allow buffer.',
        'Create YouTube account in advance. Test upload with dummy video. Have backup (Vimeo).',
        'Assign backup person for each critical task. Document all steps.',
        'Test all 3 systems on fresh machine. Create backup copies. Test zip extraction.',
        'Test zip creation and extraction before submission. Use -t flag to verify.',
        'Check PDF on multiple viewers (Adobe, Preview, Chrome). Print test page.',
        'Set internal deadline: March 18. Calendar reminders. Daily standup last week.'
    ],
    'Status': [
        'ACTIVE - Needs immediate action',
        'Monitored',
        'Mitigated - YouTube account ready',
        'Mitigated',
        'Mitigated - All systems tested',
        'Monitored',
        'Mitigated - PDF generated successfully',
        'Monitored - 39 days remaining'
    ]
})

risks.to_excel(writer, sheet_name='Risks & Mitigation', index=False)

# ============================================================================
# SHEET 9: FINAL WEEK SCHEDULE
# ============================================================================

final_week = pd.DataFrame({
    'Date': [
        'TODAY (Feb 9)', 'Feb 10', 'Feb 11', 'Feb 12', 'Feb 13',
        'Feb 14-15', 'Feb 16', 'Feb 17', 'Feb 18',
        'March 18', 'March 19', 'March 20'
    ],
    'Day': [
        'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Weekend', 'Monday', 'Tuesday', 'Wednesday',
        'Tuesday', 'Wednesday', 'Thursday'
    ],
    'Activities': [
        'TEAM MEETING: Review project, assign final tasks',
        'Member 4: Script demo video, test screen recording software',
        'Member 4: Record all system demonstrations (2 hours)',
        'Member 4: Edit video to <5 min, add annotations',
        'Member 4: Upload to YouTube, get link. Member 5: Update report PDF',
        'BUFFER - Address any issues',
        'All: Final review of all deliverables',
        'Member 5: Create zip files, test extraction',
        'INTERNAL DEADLINE: All deliverables ready. Final team review.',
        'SAFETY NET: Final checks, backup preparation',
        'SAFETY NET: Last review',
        'SUBMISSION DEADLINE 11:59 PM - Submit to Moodle'
    ],
    'Deliverable': [
        'Team alignment, task assignments',
        'Video script, recording setup',
        'Raw demo video footage',
        'Final 5-min demo video',
        'YouTube link, Updated PDF with link',
        'Issue resolution',
        'Go/No-Go decision',
        'SystemA.zip, SystemB.zip, SystemC.zip',
        'Complete submission package',
        'Verified backups',
        'Final confirmation',
        '✅ SUBMITTED'
    ],
    'Owner': [
        'All Team',
        'Member 4',
        'Member 4',
        'Member 4',
        'Member 4 + Member 5',
        'All',
        'All Team',
        'Member 5',
        'All Team',
        'Member 1',
        'All Team',
        'Member 1 (designated submitter)'
    ]
})

final_week.to_excel(writer, sheet_name='Final Week Schedule', index=False)

# Save the Excel file
writer.close()

print("=" * 80)
print("✅ BRD & PROJECT PLAN GENERATED SUCCESSFULLY!")
print("=" * 80)
print(f"\n📄 File created: {output_file}")
print(f"📍 Location: {'/'.join(__file__.split('/')[:-1])}/")
print(f"\n📊 Excel file contains 9 comprehensive sheets:")
print("   1. Executive Summary - Project overview")
print("   2. Requirements - 20 detailed requirements")
print("   3. Milestones - 8 major project milestones")
print("   4. Task Breakdown - 41 detailed tasks across 10 phases")
print("   5. Team Roles - 5 members with responsibilities")
print("   6. Deliverables Checklist - 38 deliverable items")
print("   7. Evaluation Summary - User study findings")
print("   8. Risks & Mitigation - 8 identified risks")
print("   9. Final Week Schedule - Day-by-day plan")
print("\n" + "=" * 80)
print("📌 CRITICAL NEXT STEPS:")
print("=" * 80)
print("1. TODAY: Open Excel file and review with team")
print("2. TOMORROW: Member 4 starts demo video (script + record)")
print("3. Feb 13: Complete video, upload to YouTube")
print("4. Feb 14: Update report with YouTube link")
print("5. March 18: Internal deadline - all ready")
print("6. March 20: SUBMIT to Moodle")
print("\n✨ Project Status: 95% COMPLETE")
print("⚠️  Remaining: Demo video + Final submission")
print("=" * 80)
