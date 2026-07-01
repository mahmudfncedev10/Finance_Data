import torch
import torch.nn as nn
import sqlite3
import numpy as np
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🚀 Training engine locked onto device: {device}")

class PipelinePredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.input_layer = nn.Linear(2, 8)
        self.hidden_layer = nn.Linear(8, 4)
        self.output_layer = nn.Linear(4, 1)

    def forward(self, x):
        x = torch.relu(self.input_layer(x))
        x = torch.relu(self.hidden_layer(x))
        return torch.sigmoid(self.output_layer(x))
        
def generate_mock_crm_data(num_leads=1000):
    
    deal_values = np.random.uniform(1.0, 15.0, (num_leads, 1))
    domain_types = np.random.randint(0, 2, (num_leads, 1))
    X_data = np.hstack((deal_values, domain_types))
    Y_labels = np.zeros((num_leads, 1))
    for i in range(num_leads):
        if X_data[i, 0] >= 7.5 and X_data[i, 1] == 1:
            Y_labels[i] = 1.0 
        else:
            Y_labels[i] = np.random.choice([0.0, 1.0], p=[0.85, 0.15])
            X_tensor = torch.tensor(X_data, dtype=torch.float32)
            Y_tensor = torch.tensor(Y_labels, dtype=torch.float32)
            return X_tensor, Y_tensor 


# --- OUTSIDE THE FUNCTION (No Indentation) ---

# 1. Initialize our neural network architecture and push the entire model onto the GPU VRAM
model = PipelinePredictor().to(device)

# 2. Set up our training tracking tools (Loss function and the Optimizer)
criterion = nn.BCELoss() 
optimizer = torch.optim.Adam(model.parameters(), lr=0.01) 

# 3. Generate our training data arrays
X_train, Y_train = generate_mock_crm_data()

# 4. Ship the data arrays directly onto your RTX 5060 GPU memory space
X_train = X_train.to(device)
Y_train = Y_train.to(device)

print("\n🏋️ Starting Neural Network Optimization Loop...")
print("============================================================")

# 5. Run the actual optimization training cycle for 200 iterations
for epoch in range(200):
    predictions = model(X_train)
    loss = criterion(predictions, Y_train)
    
    optimizer.zero_grad() 
    loss.backward()       
    optimizer.step()      
    
    if (epoch + 1) % 20 == 0:
        print(f"Epoch [{epoch+1}/200] -> Current Error Loss: {loss.item():.4f}")

print("============================================================")
print("🎯 Training Complete! Your GPU has optimized the logic engine.")

# 6. Freeze the optimized weights matrix and export it to a file
model_save_path = "lead_score_model.pth"
torch.save(model.state_dict(), model_save_path)

print(f"💾 Structural brain file saved securely as: {model_save_path}")

