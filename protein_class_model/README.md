# Description
This model is a neural network designed for protein classification. Here's a breakdown of its components and functionality:

NOTE: Because of limits in calculation (no GPU) capacity I had to adjust several parameters, to trained the model.

# Hyperparameters
Early Stopping: This callback monitors the validation accuracy during training and stops the training process if the accuracy stops improving after a certain number of epochs (defined by the patience parameter).
Optimizer: Adam optimizer with a learning rate of 0.001, which is used to update the weights of the neural network during training.

# Model Architecture
Embedding Layer: This layer is responsible for converting integer-encoded vocabulary indices into dense vectors of fixed size (embedding_dim). It's essential for representing words in a continuous vector space, capturing semantic relationships between words.
LSTM Layer: Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) architecture designed to capture long-term dependencies in sequential data. It has 25 units (or cells) and is set to return sequences, meaning it processes the input sequences and returns the hidden state for each time step.
Flatten Layer: This layer flattens the output from the LSTM layer into a one-dimensional vector, which is then passed to the subsequent dense layers.
Dense Layers:
  -The first Dense layer has 100 units and uses the sigmoid activation function. Sigmoid is often used for classification tasks or when the output of each unit needs to be interpreted as a probability.
  -The second Dense layer has 10 units and uses the softmax activation function. Softmax is commonly used for multi-class classification tasks, as it converts the output into probabilities across multiple classes.

# Compilation
Loss Function: Categorical crossentropy, suitable for multi-class classification tasks where the target labels are one-hot encoded.
Optimizer: Adam optimizer with a learning rate of 0.001, as specified earlier.
Metrics: Accuracy is used as the evaluation metric to measure the model's performance during training and validation.
