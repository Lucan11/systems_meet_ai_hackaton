from __future__ import annotations

import torch
from torch import nn


class ImprovedMLP(nn.Module):
    """Small MLP used by the Task 1 starter baseline."""

    def __init__(
            self,
            layers: list[int] = [9, 32, 32, 2],
    ) -> None:
        super().__init__()

        model_layers = []
        last_layer_idx = len(layers) - 1 - 1
        for layer_idx in range(len(layers) - 1):
            model_layers.append(nn.Linear(layers[layer_idx], layers[layer_idx + 1]))

            if layer_idx < last_layer_idx:
                model_layers.append(nn.LayerNorm(layers[layer_idx + 1]))
                model_layers.append(nn.ReLU())

        model_layers.append(nn.Sigmoid())
        self.net = nn.Sequential(*model_layers)
        # print(self.net)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)
