from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

# plots the confusion matrix in a pretty plot
def plot_confusion_mat(ax, y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    ax.set_title(f'Confusion matrix with total accuracy at {accuracy_score(y_true, y_pred):0.3f}')
    
    cax = ax.matshow(cm,)
    labels =  list(range(len(cm)))
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.set_yticklabels(labels)
    
    for i in range(len(cm)):
        for j in range(len(cm)):
            text = ax.text(j, i, round(cm[i][j],0),
                           ha="center", va="center", color="w", size=16)
            
    ax.set_ylabel('true')
    ax.set_xlabel('predictions')