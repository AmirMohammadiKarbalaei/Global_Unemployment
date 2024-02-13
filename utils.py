import matplotlib.pyplot as plt
import seaborn as sns

def plot(data, title: str, xlabel: str, ylabel: str, legend: str = None, legend_location: str = 'upper left', grid: bool = False):
    sns.set_style("whitegrid")
    
    fig, ax = plt.subplots(figsize=(10, 6))  
    sns.lineplot(data=data, marker='o', ax=ax, palette="Set2", linewidth=3)
    ax.set_title(title, fontsize=16, fontweight='bold')  
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14) 
    
    if legend:
        ax.legend(title=legend, bbox_to_anchor=(1.05, 1), loc=legend_location, fontsize=12)
    
    ax.grid(grid)
    
    plt.tight_layout()
    return fig, ax
    