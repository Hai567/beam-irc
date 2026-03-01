import torch
import torch.nn as nn

class LateFusionModel(nn.Module):
    def __init__(self, lstm_input_dim, mlp_input_dim, hidden_dim=64, num_classes=1):
        super(LateFusionModel, self).__init__()
        
        # LSTM 
        self.lstm_branch = nn.LSTM(
            input_size=lstm_input_dim, 
            hidden_size=hidden_dim, 
            batch_first=True,
            num_layers=2,
            dropout=0.2
        )
        
        #  MLP
        self.mlp_branch = nn.Sequential(
            nn.Linear(mlp_input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )
        
        # Fusion Layer - Combine features from 2 heads
        # Input = hidden_dim (từ LSTM) + hidden_dim/2 (từ MLP)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim + (hidden_dim // 2), 32),
            nn.ReLU(),
            nn.Linear(32, num_classes) 
        )

    def forward(self, x_sequence, x_static):
        # 1. LSTM head
        lstm_out, (h_n, c_n) = self.lstm_branch(x_sequence)
        # Get the hidden state of the last layer (h_n[-1])
        feat_seq = h_n[-1] 
        
        # 2. MLP head
        feat_static = self.mlp_branch(x_static)
        
        # 3. Concatenate (Late Fusion)
        combined_features = torch.cat((feat_seq, feat_static), dim=1)
        
        # 4. Final classification
        output = self.classifier(combined_features)
        return output