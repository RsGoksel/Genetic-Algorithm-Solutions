GAME SOLUTIONS with GENETIC ALGORITHMS

In this work, the approach to solving games with Genetic Algorithms consists of three main classes.

  * Brain (Neural Network)
  * Agent 
  * Environment

## Environment
    Environment class has game Settings. Involves Initial variables, Methods, and configurations.
    
![Env](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/d56c01f5-df97-4136-815e-ac4a884155c5)


## Brain and Agent
    
   Brain class has Weights, Layers, Activation Functions. Consider it Neural Network. 
   Gathered informations attachs to first layer of brain and eventually a prediction is obtained.

   Agent class has on the other hand has Brain class initially, also has variables which depends on the game, like movement settings, skill and limitations etc.  
    
- ! The depth of an artificial neural network (ANN) is important and may depend on the complexity of your problem. Choose a depth suitable for your problem.
  
![Brain-Agent](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/1390930e-e344-4f51-a232-e4d1c2fcc988)

## Crossover

Crossover mechanism depends on the problem. There are Uniform Crossover, One-Point Crossover, Two-Point Crossover etc.
Generally in these game solutions uniform crossover has been used. 

*Uniform crossover involves selecting only one genome simultaneously from two different members.

![Crossover](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/cd154469-0566-4f05-87a4-deb9f59601ad)



When round is over, Died agents are fetched and chosen based on their own fitness values. Good ones (considering fitness function) are chosen and applied crossover. Pairs of weights from two parents are selected based on a probability coefficient and used to produce a new child agent, which may exhibit an improved fitness function.

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







