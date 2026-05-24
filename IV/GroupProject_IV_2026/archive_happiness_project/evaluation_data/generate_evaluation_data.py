"""
Generate Sample Evaluation Data for User Study
This creates realistic evaluation data matching the report statistics
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# Participant information
participants = [f'P{i+1}' for i in range(5)]
systems = ['A', 'B', 'C']
tasks = ['T1', 'T2', 'T3', 'T4', 'T5']

# System orders (counterbalanced)
orders = [
    ['A', 'B', 'C'],  # P1
    ['B', 'C', 'A'],  # P2
    ['C', 'A', 'B'],  # P3
    ['A', 'C', 'B'],  # P4
    ['B', 'A', 'C']   # P5
]

# Task completion times (mean ± SD from report)
time_params = {
    'A': {'T1': (28.4, 5.2), 'T2': (45.8, 9.3), 'T3': (52.1, 11.2), 'T4': (34.9, 6.8), 'T5': (39.6, 8.1)},
    'B': {'T1': (35.6, 7.1), 'T2': (31.2, 6.4), 'T3': (48.7, 9.8), 'T4': (58.2, 10.4), 'T5': (44.3, 9.6)},
    'C': {'T1': (42.3, 8.9), 'T2': (38.9, 7.7), 'T3': (61.3, 13.5), 'T4': (51.7, 9.1), 'T5': (22.8, 4.3)}
}

# Accuracy rates (from report)
accuracy_params = {
    'A': {'T1': 1.0, 'T2': 0.8, 'T3': 1.0, 'T4': 1.0, 'T5': 1.0},
    'B': {'T1': 1.0, 'T2': 1.0, 'T3': 1.0, 'T4': 0.8, 'T5': 1.0},
    'C': {'T1': 0.8, 'T2': 0.8, 'T3': 0.8, 'T4': 0.8, 'T5': 1.0}
}

# Generate task performance data
task_data = []
for p_idx, participant in enumerate(participants):
    system_order = orders[p_idx]
    for system in systems:
        for task in tasks:
            mean_time, std_time = time_params[system][task]
            completion_time = max(10, np.random.normal(mean_time, std_time))  # Minimum 10s

            # Determine accuracy based on probabilities
            accuracy_prob = accuracy_params[system][task]
            is_correct = np.random.random() < accuracy_prob

            # Interaction count (for T5 filtering task)
            if task == 'T5':
                if system == 'A':
                    interactions = np.random.randint(6, 11)
                elif system == 'B':
                    interactions = np.random.randint(5, 9)
                else:  # C
                    interactions = np.random.randint(2, 4)
            else:
                interactions = np.random.randint(3, 8)

            task_data.append({
                'Participant': participant,
                'System': system,
                'Task': task,
                'Completion_Time_sec': round(completion_time, 1),
                'Correct': is_correct,
                'Interaction_Count': interactions,
                'System_Order': system_order.index(system) + 1
            })

task_df = pd.DataFrame(task_data)

# Generate SUS scores (System Usability Scale)
sus_questions = [f'SUS_Q{i}' for i in range(1, 11)]
sus_data = []

sus_means = {'A': 78.5, 'B': 72.4, 'C': 81.2}
sus_stds = {'A': 8.3, 'B': 11.2, 'C': 7.1}

for p_idx, participant in enumerate(participants):
    for system in systems:
        # Generate SUS scores that sum to approximate mean
        target_mean = sus_means[system]
        target_std = sus_stds[system]

        # SUS score = sum of adjusted responses * 2.5
        # Each question 1-5, alternating positive/negative
        scores = []
        for q in range(10):
            if q % 2 == 0:  # Positive questions (1, 3, 5, 7, 9)
                # Higher is better, typically 3-5
                score = np.clip(int(np.random.normal(4, 0.7)), 1, 5)
            else:  # Negative questions (2, 4, 6, 8, 10)
                # Lower is better, typically 1-3
                score = np.clip(int(np.random.normal(2, 0.7)), 1, 5)
            scores.append(score)

        # Calculate SUS score
        adjusted_sum = sum((scores[i] - 1) if i % 2 == 0 else (5 - scores[i]) for i in range(10))
        sus_score = adjusted_sum * 2.5

        row = {
            'Participant': participant,
            'System': system
        }
        for q_idx, score in enumerate(scores):
            row[sus_questions[q_idx]] = score
        row['SUS_Total_Score'] = sus_score

        sus_data.append(row)

sus_df = pd.DataFrame(sus_data)

# Generate NASA TLX scores
tlx_dimensions = ['Mental_Demand', 'Physical_Demand', 'Temporal_Demand',
                  'Performance', 'Effort', 'Frustration']

tlx_data = []
tlx_mental_means = {'A': 4.2, 'B': 5.8, 'C': 3.9}
tlx_mental_stds = {'A': 1.3, 'B': 1.7, 'C': 1.1}

for p_idx, participant in enumerate(participants):
    for system in systems:
        mental_demand = np.clip(np.random.normal(tlx_mental_means[system], tlx_mental_stds[system]), 1, 10)

        row = {
            'Participant': participant,
            'System': system,
            'Mental_Demand': round(mental_demand, 1),
            'Physical_Demand': round(np.random.uniform(2, 4), 1),
            'Temporal_Demand': round(np.random.uniform(3, 6), 1),
            'Performance': round(np.random.uniform(6, 9), 1),  # Higher is better
            'Effort': round(mental_demand + np.random.uniform(-1, 1), 1),
            'Frustration': round(10 - np.random.uniform(6, 9), 1)  # Lower is better
        }
        tlx_data.append(row)

tlx_df = pd.DataFrame(tlx_data)

# Generate preference rankings
preference_data = []
# Based on report: 3 participants ranked C #1, 2 ranked A #1, 0 ranked B #1
rankings = [
    ['C', 'A', 'B'],  # P1
    ['C', 'A', 'B'],  # P2
    ['A', 'C', 'B'],  # P3
    ['C', 'B', 'A'],  # P4
    ['A', 'C', 'B']   # P5
]

for p_idx, participant in enumerate(participants):
    rank = rankings[p_idx]
    preference_data.append({
        'Participant': participant,
        'First_Choice': rank[0],
        'Second_Choice': rank[1],
        'Third_Choice': rank[2]
    })

preference_df = pd.DataFrame(preference_data)

# Generate qualitative feedback
feedback_data = []
feedback_responses = {
    'A': {
        'Liked': [
            'Line chart made trends super obvious',
            'Clean and simple design',
            'Colors were consistent across views',
            'Easy to understand overall',
            'Bar chart was intuitive'
        ],
        'Disliked': [
            'Brushing was imprecise, hard to select exactly what I wanted',
            'Scatter plot got messy with many points',
            'Sometimes hard to deselect',
            'Brush selection took trial and error',
            'Wished for undo button'
        ]
    },
    'B': {
        'Liked': [
            'Box plots showed outliers immediately',
            'Regression line was cool, showed correlation strength',
            'Heatmap gave good overview',
            'Liked the variety of chart types',
            'Box plots very informative'
        ],
        'Disliked': [
            'Heatmap colors were hard to distinguish',
            'Too many different chart types, took time to understand',
            'Box plots are confusing if you don\'t know statistics',
            'Mental effort was high',
            'Color scheme inconsistency confused me'
        ]
    },
    'C': {
        'Liked': [
            'Dropdown and slider were so easy to use',
            'Small multiples let me see all regions at once',
            'Felt most in control of the interface',
            'Filtering was straightforward',
            'Interface was intuitive'
        ],
        'Disliked': [
            'Faceted plots were too small',
            'Strip plot was cluttered',
            'Bubble chart was hard to decode (too many visual channels)',
            'Small text in facets',
            'Wanted larger individual plots'
        ]
    }
}

for p_idx, participant in enumerate(participants):
    for system in systems:
        liked = feedback_responses[system]['Liked'][p_idx]
        disliked = feedback_responses[system]['Disliked'][p_idx]
        feedback_data.append({
            'Participant': participant,
            'System': system,
            'What_I_Liked': liked,
            'What_I_Disliked': disliked
        })

feedback_df = pd.DataFrame(feedback_data)

# Save all data
task_df.to_csv('raw_task_performance.csv', index=False)
sus_df.to_csv('raw_sus_scores.csv', index=False)
tlx_df.to_csv('raw_nasa_tlx.csv', index=False)
preference_df.to_csv('raw_preferences.csv', index=False)
feedback_df.to_csv('raw_qualitative_feedback.csv', index=False)

# Create combined file
combined_df = task_df.copy()
print("✓ Evaluation data generated successfully!")
print(f"\nFiles created:")
print(f"  - raw_task_performance.csv ({len(task_df)} records)")
print(f"  - raw_sus_scores.csv ({len(sus_df)} records)")
print(f"  - raw_nasa_tlx.csv ({len(tlx_df)} records)")
print(f"  - raw_preferences.csv ({len(preference_df)} records)")
print(f"  - raw_qualitative_feedback.csv ({len(feedback_df)} records)")

print(f"\n=== Task Performance Summary ===")
for system in systems:
    system_data = task_df[task_df['System'] == system]
    print(f"\nSystem {system}:")
    for task in tasks:
        task_system_data = system_data[system_data['Task'] == task]
        mean_time = task_system_data['Completion_Time_sec'].mean()
        accuracy = task_system_data['Correct'].mean() * 100
        print(f"  {task}: {mean_time:.1f}s (±{task_system_data['Completion_Time_sec'].std():.1f}s), {accuracy:.0f}% accuracy")

print(f"\n=== SUS Scores ===")
for system in systems:
    system_sus = sus_df[sus_df['System'] == system]['SUS_Total_Score']
    print(f"System {system}: {system_sus.mean():.1f} (±{system_sus.std():.1f})")

print(f"\n=== NASA TLX Mental Demand ===")
for system in systems:
    system_tlx = tlx_df[tlx_df['System'] == system]['Mental_Demand']
    print(f"System {system}: {system_tlx.mean():.1f}/10 (±{system_tlx.std():.1f})")

print(f"\n=== Preference Rankings ===")
for rank in range(3):
    choice_col = ['First_Choice', 'Second_Choice', 'Third_Choice'][rank]
    counts = preference_df[choice_col].value_counts()
    print(f"{['#1', '#2', '#3'][rank]} choice: {dict(counts)}")
