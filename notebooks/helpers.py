from pathlib import Path
import csv
import sys

import numpy as np
import matplotlib.pyplot as plt
import torch


def init(SEED = 42, gpu: bool = False, task: int = 1):
    ROOT = Path.cwd().resolve().parent if Path.cwd().name == "notebooks" else Path.cwd().resolve()
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    np.random.seed(SEED)
    torch.manual_seed(SEED)
    print("PyTorch:", torch.__version__)

    # Make sure to run on CPU
    if not gpu:
        import os
        os.environ['CUDA_VISIBLE_DEVICES'] = ''

    if task == 1:
        TRAIN_CSV = ROOT / "data" / "train_clean_3x3_1cm.csv"
        VALIDATION_CSV = ROOT / "data" / "validation_clean_3x3_1cm.csv"
        COLUMNS = ["led_0", "led_2", "led_4", "led_12", "led_14", "led_16", "led_24", "led_26", "led_28"]
    else:
        TRAIN_CSV = ROOT / "data" / "train_clean_6x6_8cm.csv"
        VALIDATION_CSV = ROOT / "data" / "validation_clean_6x6_8cm.csv"
        COLUMNS = ["led_0", "led_1", "led_2", "led_3", "led_4", "led_5",
                         "led_6", "led_7", "led_8", "led_9", "led_10", "led_11",
                         "led_12", "led_13", "led_14", "led_15", "led_16", "led_17",
                         "led_18", "led_19", "led_20", "led_21", "led_22", "led_23",
                         "led_24", "led_25", "led_26", "led_27", "led_28", "led_29",
                         "led_30", "led_31", "led_32", "led_33", "led_34", "led_35"]

    def load_task1_csv(path):
        rows = []
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                rows.append([float(row["x"]), float(row["y"]), *[float(row[c]) for c in COLUMNS]])
        arr = np.asarray(rows, dtype=np.float32)
        return arr[:, 2:], arr[:, :2] / 10.0

    X_train_raw, y_train_cm = load_task1_csv(TRAIN_CSV)
    X_val_raw, y_val_cm = load_task1_csv(VALIDATION_CSV)

    print("Training rows:", len(X_train_raw))
    print("Validation rows:", len(X_val_raw))
    print("Input shape:", X_train_raw.shape)
    print("Target x range (cm):", y_train_cm[:, 0].min(), "to", y_train_cm[:, 0].max())
    print("Target y range (cm):", y_train_cm[:, 1].min(), "to", y_train_cm[:, 1].max())

    print("Using split files:")
    print("  train:", TRAIN_CSV.name, len(X_train_raw), "rows")
    print("  validation:", VALIDATION_CSV.name, len(X_val_raw), "rows")

    return X_train_raw, y_train_cm, X_val_raw, y_val_cm

def preprocess_data(
        X_train_raw: np.ndarray,
        y_train_cm: np.ndarray,
        X_val_raw: np.ndarray,
        y_val_cm: np.ndarray,
        plot: bool = False
):
    rss_scale = max(float(np.max(np.abs(X_train_raw))), 1e-8)
    X_train = X_train_raw / rss_scale
    X_val = X_val_raw / rss_scale

    target_min_cm = y_train_cm.min(axis=0)
    target_range_cm = np.maximum(y_train_cm.max(axis=0) - target_min_cm, 1e-8)
    y_train = (y_train_cm - target_min_cm) / target_range_cm
    y_val = (y_val_cm - target_min_cm) / target_range_cm

    print("RSS scale:", rss_scale)
    print("Target min cm:", target_min_cm)
    print("Target range cm:", target_range_cm)

    if plot:
        plt.figure(figsize=(6, 4))
        plt.hist(X_train[:, 0], bins=50)
        plt.xlabel("Normalized RSS")
        plt.ylabel("Samples")
        plt.title("Task 1 baseline: first selected LED")
        plt.show()
    return X_train, y_train, X_val, y_val, target_min_cm, target_range_cm
