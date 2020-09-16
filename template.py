import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader


class CustomSet(Dataset):
    def __init__(self, size=10000):
        self.size = size
        self.X = np.random.rand(self.size, 1)
        self.Y = self.X ** 2

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        return {'x': torch.tensor(self.X[i], dtype=torch.float),
                'y': torch.tensor(self.Y[i], dtype=torch.float)}


class Net(nn.Module):
    def __init__(self, N_HIDDEN=20):
        super(Net, self).__init__()
        self.N_HIDDEN = N_HIDDEN
        # layer
        self.fc1 = nn.Linear(1, N_HIDDEN)
        self.fc2 = nn.Linear(N_HIDDEN, 1)

    def forward(self, x):
        x = F.sigmoid(F.relu(self.fc1(x)))
        x = self.fc2(x)
        return x


def run():
    # dataset and dataloader
    customset = CustomSet()
    dataloader = DataLoader(dataset=customset, batch_size=32, shuffle=True, num_workers=1)
    # network and configurations
    net = Net()
    criterion = nn.MSELoss()
    optimizer = optim.SGD(lr=0.1, params=net.parameters(), momentum=0)
    for epoch in range(1000):
        for data in dataloader:
            x = data['x']
            y = data['y']
            predict_y = net(x)
            # zero grad
            optimizer.zero_grad()
            # update
            loss = criterion(predict_y, y)
            loss.backward()
            optimizer.step()
        print('\n epoch: %i | loss: %.5f' % (epoch, loss.item()))
        print(y.detach().numpy().tolist())
        print(predict_y.detach().numpy().tolist())


if __name__ == '__main__':
    run()
