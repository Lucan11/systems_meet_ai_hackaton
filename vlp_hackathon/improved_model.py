from __future__ import annotations

import torch
from torch import nn


class ImprovedMLP(nn.Module):
    """Small MLP used by the Task 1 starter baseline."""

    def __init__(self, input_features: int = 9) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_features, 32),
            nn.LayerNorm(32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.LayerNorm(32),
            nn.ReLU(),
            nn.Linear(32, 2),
            nn.LayerNorm(2),
            nn.Sigmoid(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)
