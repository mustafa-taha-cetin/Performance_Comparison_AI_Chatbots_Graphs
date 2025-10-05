import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1: Define the data
# You can change these scores based on your own testing
data = {
    'AI_Model': ['ChatGPT', 'Claude', 'Gemini'],
    'Speed': [9, 8.4, 5.6],
    'Accuracy': [8.6, 9, 8.8],
    'Clarity': [8.2, 8.6, 7.6],
    'Helpfulness': [7.4, 8.6, 8.8]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Calculate average scores
df['Average'] = df[['Speed', 'Accuracy', 'Clarity', 'Helpfulness']].mean(axis=1)

print("=" * 60)
print("AI CHATBOT PERFORMANCE COMPARISON")
print("=" * 60)
print("\nData Table:")
print(df.to_string(index=False))
print("\n" + "=" * 60)

# Step 4: Create bar chart for all categories
def create_bar_chart():
    categories = ['Speed', 'Accuracy', 'Clarity', 'Helpfulness']
    x_position = np.arange(len(categories))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    chatgpt_scores = df[df['AI_Model'] == 'ChatGPT'][categories].values[0]
    claude_scores = df[df['AI_Model'] == 'Claude'][categories].values[0]
    gemini_scores = df[df['AI_Model'] == 'Gemini'][categories].values[0]
    
    bar1 = ax.bar(x_position - width, chatgpt_scores, width, label='ChatGPT', color='#10b981')
    bar2 = ax.bar(x_position, claude_scores, width, label='Claude', color='#8b5cf6')
    bar3 = ax.bar(x_position + width, gemini_scores, width, label='Gemini', color='#3b82f6')
    
    ax.set_xlabel('Categories', fontsize=12, fontweight='bold')
    ax.set_ylabel('Score (out of 10)', fontsize=12, fontweight='bold')
    ax.set_title('AI Chatbot Performance by Category', fontsize=14, fontweight='bold')
    ax.set_xticks(x_position)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.set_ylim(0, 10)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')
    print("\n✓ Bar chart saved as 'bar_chart.png'")
    plt.show()

# Step 5: Create average comparison chart
def create_average_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#10b981', '#8b5cf6', '#3b82f6']
    bars = ax.bar(df['AI_Model'], df['Average'], color=colors, edgecolor='black', linewidth=1.5)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_xlabel('AI Model', fontsize=12, fontweight='bold')
    ax.set_ylabel('Average Score (out of 10)', fontsize=12, fontweight='bold')
    ax.set_title('Overall Average Performance Comparison', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 10)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('average_chart.png', dpi=300, bbox_inches='tight')
    print("✓ Average chart saved as 'average_chart.png'")
    plt.show()

# Step 6: Create radar chart
def create_radar_chart():
    categories = ['Speed', 'Accuracy', 'Clarity', 'Helpfulness']
    num_categories = len(categories)
    
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    for index, row in df.iterrows():
        values = row[['Speed', 'Accuracy', 'Clarity', 'Helpfulness']].tolist()
        values += values[:1]
        
        if row['AI_Model'] == 'ChatGPT':
            color = '#10b981'
        elif row['AI_Model'] == 'Claude':
            color = '#8b5cf6'
        else:
            color = '#3b82f6'
        
        ax.plot(angles, values, 'o-', linewidth=2, label=row['AI_Model'], color=color)
        ax.fill(angles, values, alpha=0.15, color=color)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_title('AI Performance Radar Chart', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    ax.grid(True)
    
    plt.tight_layout()
    plt.savefig('radar_chart.png', dpi=300, bbox_inches='tight')
    print("✓ Radar chart saved as 'radar_chart.png'")
    plt.show()

# Step 7: Export to Excel
def export_to_excel():
    with pd.ExcelWriter('ai_comparison_results.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Results', index=False)
    print("\n✓ Data exported to 'ai_comparison_results.xlsx'")

# Step 8: Print summary statistics
def print_summary():
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    
    best_speed = df.loc[df['Speed'].idxmax(), 'AI_Model']
    best_accuracy = df.loc[df['Accuracy'].idxmax(), 'AI_Model']
    best_clarity = df.loc[df['Clarity'].idxmax(), 'AI_Model']
    best_helpfulness = df.loc[df['Helpfulness'].idxmax(), 'AI_Model']
    best_overall = df.loc[df['Average'].idxmax(), 'AI_Model']
    
    print(f"\nBest in Speed: {best_speed}")
    print(f"Best in Accuracy: {best_accuracy}")
    print(f"Best in Clarity: {best_clarity}")
    print(f"Best in Helpfulness: {best_helpfulness}")
    print(f"\nOverall Winner: {best_overall}")
    print("=" * 60)

# Main execution
if __name__ == "__main__":
    create_bar_chart()
    create_average_chart()
    create_radar_chart()
    export_to_excel()
    print_summary()
    
    print("\n✓ All tasks completed successfully!")
    print("  Files created:")
    print("  - bar_chart.png")
    print("  - average_chart.png")
    print("  - radar_chart.png")
    print("  - ai_comparison_results.xlsx")