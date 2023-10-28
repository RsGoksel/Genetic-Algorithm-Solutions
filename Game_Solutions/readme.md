
In this repository, approach of solving the games with Genetic Algorithms has 3 main classes. 

  * Brain (Neural Network)
  * Agent 
  * Environment

## Environment
    Environment is the class of game screen which controlls all variable and gives visible output. It has 4 methods. 
    
![Env](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/d56c01f5-df97-4136-815e-ac4a884155c5)


## Brain and Agent
 Every ANN and agent variables may change considering the differents problems but they have kinda similar approachs.
    weights, layers, activation functions for brain
    iterating or moving mechanism, fitness function and decision. Final layer has to be number of decisions. For example if you're moving 4 dimension to move,
    than use 4 layer at final layer.

- ! The depth of an artificial neural network (ANN) is significant and may depend on the complexity of your problem.
![Brain-Agent](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/1390930e-e344-4f51-a232-e4d1c2fcc988)



## Crossover

And the backbone of genetic algorithms. Crossover mechanism has to be set and written according to the solution of the problem. Like Uniform Crossover, One-Point Crossover, Two-Point Crossover etc. 
![Crossover](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/cd154469-0566-4f05-87a4-deb9f59601ad)



When round is over, died agents are fetched and choosen by their own fitness values. The bests are chosen and being crossover. Every weights of 2 parents are chosen by probability coefficient and produces new child which may close to better fitness function

________________________________________________________________________________________________

## Depiction of the approach

![Sn1 (1)](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/dbcf6463-9a61-4353-906c-9f3d06c3013b)

Every agent on the screen has own unique neural network. On another speech, during the initialization step of population creation, each agent is assigned unique weights.

![sn2](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/43b64dad-6954-445f-b06c-ed4ba7b3f9c8)

In every generation or round, best agents (considering their own fitness value) are chosen from all died agents and apply crossover. 

![sn3](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/3086e107-0d84-4e4e-a286-5b4867d32740)

 2 external library required for the games. Numpy and Pygame. You can install them as
```bash
    pip install numpy
    pip install pygame
```
or
```bash
    pip install -r requirements.txt
```







