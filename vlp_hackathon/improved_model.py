from __future__ import annotations

import torch
from torch import nn


class ImprovedMLP(nn.Module):
    """Small MLP used by the Task 1 starter baseline."""

    def __init__(
            self,
            layers: list[int] = [9, 32, 32, 2],
            activation: str = "relu",
            last_act: str = "",
            layer_norm: bool = True
    ) -> None:
        super().__init__()

        layer_map = {
            "relu": nn.ReLU,
            "tanh": nn.Tanh,
            "sigmoid": nn.Sigmoid,
            "": nn.Identity,
            "none": nn.Identity
        }

        activation = activation.lower()
        self.act = layer_map[activation]
        self.last_act = layer_map[last_act]

        model_layers = []
        last_layer_idx = len(layers) - 1 - 1
        for layer_idx in range(len(layers) - 1):
            model_layers.append(nn.Linear(layers[layer_idx], layers[layer_idx + 1]))

            if layer_idx < last_layer_idx:
                if layer_norm:
                    model_layers.append(nn.LayerNorm(layers[layer_idx + 1]))
                model_layers.append(self.act())

        model_layers.append(self.last_act())
        self.net = nn.Sequential(*model_layers)
        print(self.net)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class Task1Model(ImprovedMLP):

    def __init__(self):
        super().__init__(
            layers=[9, 113, 90, 93],
            activation="relu",
            last_act="tanh"
        )


