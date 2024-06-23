import torch
from torch import nn


class Sofmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        exp_x = self._get_exp_x(x)
        return exp_x / torch.sum(exp_x)

    def _get_exp_x(self, x: torch.Tensor) -> torch.Tensor:
        return torch.exp(x)


class SofmaxStable(Sofmax):
    def __init__(self):
        super().__init__()

    def _get_exp_x(self, x: torch.Tensor) -> torch.Tensor:
        max_x = torch.max(x)
        return super()._get_exp_x(x - max_x)


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    print(f"Input data: {data}")
    softmax = Sofmax()
    softmax_stable = SofmaxStable()

    print(f"Softmax output: {softmax(data)}")
    print(f"Softmax stable output: {softmax_stable(data)}")
