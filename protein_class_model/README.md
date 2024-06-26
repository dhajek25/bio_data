# Description
This model is a neural network designed for protein classification. See **protein_class.ipynb**. <br>

NOTE: Because of limits in calculation capacity (no GPU) I had to adjust several parameters, to trained the model.

Here's a breakdown of its components and functionality:

# Hyperparameters
Early Stopping: This callback monitors the validation accuracy during training and stops the training process if the accuracy stops improving after a certain number of epochs (defined by the patience parameter). <br>

Optimizer: Adam optimizer with a learning rate of 0.001, which is used to update the weights of the neural network during training. <br>

# Model Architecture
Embedding Layer: This layer is responsible for converting integer-encoded vocabulary indices into dense vectors of fixed size (embedding_dim). It's essential for representing words in a continuous vector space, capturing semantic relationships between words. <br>

LSTM Layer: Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) architecture designed to capture long-term dependencies in sequential data. It has 25 units (or cells) and is set to return sequences, meaning it processes the input sequences and returns the hidden state for each time step. <br>

Flatten Layer: This layer flattens the output from the LSTM layer into a one-dimensional vector, which is then passed to the subsequent dense layers. <br>

Dense Layers: <br>
  -The first Dense layer has 100 units and uses the sigmoid activation function. Sigmoid is often used for classification tasks or when the output of each unit needs to be interpreted as a probability. <br>
  -The second Dense layer has 10 units and uses the softmax activation function. Softmax is commonly used for multi-class classification tasks, as it converts the output into probabilities across multiple classes. <br>

# Compilation
Loss Function: Categorical crossentropy, suitable for multi-class classification tasks where the target labels are one-hot encoded. <br>

Optimizer: Adam optimizer with a learning rate of 0.001, as specified earlier. <br>

Metrics: Accuracy is used as the evaluation metric to measure the model's performance during training and validation. <br>

# Model Summary
![image](https://github.com/dhajek25/bio_data/assets/79058813/2d031660-4890-42b2-a037-eba3bbf78b30)

# Evaluation Metrics
Train accuracy = 93.75% <br>
Validation accuracy = 87.17%

# Evaluate Model
![image](https://github.com/dhajek25/bio_data/assets/79058813/9434cdd4-fc46-4861-910b-18ade3ae4cf5)

# Credits and References
During the process of model devolopment I followed these sources: <br>
https://www.kaggle.com/code/srajpara/protein-classification-rnn-lstm-v-1 <br>
https://www.kaggle.com/code/danofer/deep-protein-sequence-family-classification/notebook
