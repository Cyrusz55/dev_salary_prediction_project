"""

"""
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score)
import matplotlib.pyplot as plt
from pathlib import Path
def evaluate_model(y_true, y_pred, title: str = "Model evaluation")->dict:
    """
    Compute and print regression metrics.
    Return a dict of metric name > value
    :param y_true:
    :param y_pred:
    :param title:
    :return:
    """
    print(f"--- {title} ---")
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"R²: {r2:.4f}")

    return {"mae": mae, "mse": mse, "r2": r2}


def plot_predictions(y_true, y_pred, save_path: str=None):
    """Plot actual vs prediced.
    Plot for residuals.
    """
    fig, axes = plt.subplots(1, 2, figsize = (14, 5))

    # plot 1 - actual vs predicted.
    axes[0].scatter(y_true, y_pred, alpha=0.5, s = 10, color = 'steelblue')
    lim = float(max(y_true.max(), y_pred.max())) * 1.05
    axes[0].plot([0, lim], [0, lim], 'r--', linewidth = 1.5, label='perfect prediction')
    axes[0].set_xlabel("Actual salary (USD)")
    axes[0].set_ylabel("Predicted salary (USD)")
    axes[0].set_title("Actual vs predicted salary")
    axes[0].legend()

    # plot 2 -  residuals.
    residuals = y_true - y_pred
    axes[1].hist(residuals, bins = 60, color = 'coral', edgecolor='white')
    axes[1].axvline(0, color = 'black', linestyle = '--', linewidth = 1.5)
    axes[1].set_xlabel("Residual (Actual - Predicted)")
    axes[1].set_ylabel('Count')
    axes[1].set_title('Residual distribution')

    plt.suptitle('Model evaluation', fontweight = 'bold')
    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"Plot saved to {save_path}")
    plt.show()



def print_observations(metrics: dict):
    """
    Print observations based on model metrics.
    :param metrics:
    :return:
    """
    mae = metrics['mae']
    r2 = metrics['r2']
    print("Observations\n")
    print(f"MAE of ${mae} means our model's average prediction is off by ${mae:,.1f} from the actual salary")
    if r2 > 0.7:
        print(f"r2 score of {r2:.3f} is strong - the model explains {r2 * 100}% of the variance in salary")
    elif r2> 0.5:
        print(f"r2 score of {r2:.3f} is moderate - there is still variance the model cannot capture (expected for salary data)")
    else:
        print(f"r2 of {r2:.3f} is relatively low. This is common for salary predictions as many factors are unmeasured")

        