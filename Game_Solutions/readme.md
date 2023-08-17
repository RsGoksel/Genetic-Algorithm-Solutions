In this repository, approach of solving the games with Genetic Algorithms has 3 main classes. 

  * Brain
  * Agent
  * Environment

## Environment
    Environment is the class of game screen which controlls all variable and gives visible output. It has 4 methods. 
    
![image](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/bb33d07d-73a1-48e6-bd5e-09b1ce385411)

## Brain and Agent
 Every ANN and agent variables may change considering the differents problems but they have kinda similar approachs.
    weights, layers, activation functions for brain
    iterating or moving mechanism, fitness function and decision. Final layer has to be number of decisions. For example if you're moving 4 dimension to move,
    than use 4 layer at final layer.

- ! The depth of an artificial neural network (ANN) is significant and may depend on the complexity of your problem.

![image](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/03365794-600e-425f-8207-5bf52f0dc703)

## Crossover

And the backbone of genetic algorithms. Crossover mechanism has to be set and written according to the solution of the problem. Like Uniform Crossover, One-Point Crossover, Two-Point Crossover etc. 

![image](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/2c908828-c028-4cf0-9b77-da1c51d4886c)

When round is over, died agents are fetched and choosen by their own fitness values. The bests are chosen and being crossover. Every weights of 2 parents are chosen by probability coefficient and produces new child which may close to better fitness function

  
