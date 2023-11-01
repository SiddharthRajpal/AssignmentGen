# AssignmentGen
An innovative app powered by RNN and Keras, tailoring personalized assignments for diverse educational levels and grades, fostering interactive and adaptive learning experiences.

## Trailer
Watch our Trailer here :- [Trailer Link]


## Our Model
Below is the summary of our RNN model which we have made using python and keras.

### Model for RNN


| Layer (type)                  | Output Shape             | Param      |
|-------------------------------|--------------------------|------------|
| embedding (Embedding)               | multiple     | 16896            |
|  gru (GRU)  |               | multiple     | 3938304          |
|  dense (Dense)                      | multiple     | 67650            |


 The architecture consists of three layers: an Embedding layer, a GRU (Gated Recurrent Unit) layer, and a Dense (fully connected) layer.

## Embedding Layer:

Type: Embedding
Output Shape: Multiple
Parameters: 16896
Explanation: The Embedding layer is the first layer in the network. It is used for converting sequences of integers (representing words or tokens) into dense vectors of fixed size. The output shape is not specified here but depends on the input data.
GRU Layer:

## Type: GRU
Output Shape: Multiple
Parameters: 3938304
Explanation: The GRU layer is a type of recurrent neural network (RNN) layer. GRU is capable of capturing long-range dependencies in sequential data. It processes input sequences and maintains an internal state, allowing it to capture patterns and relationships across the input data. The output shape is not specified here but depends on the input data.
Dense Layer:

## Type: Dense
Output Shape: Multiple
Parameters: 67650
Explanation: The Dense layer is a standard fully connected neural network layer. It performs a linear operation on the input data and applies an activation function to produce the output. In this context, it is likely used to map the GRU layer's output to the desired output format, which could represent different levels and grades for generated assignments.
This architecture is suitable for tasks where sequential input data, such as text or time series data, needs to be processed, and the model needs to capture complex patterns and relationships within the data. The specific shapes and parameters depend on the input data dimensions and the problem being solved. Developers can use this architecture as a starting point and customize it based on their specific requirements and datasets.





## Usage
Our Site is hosted at this link :- [ Site Link ]
