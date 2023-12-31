<p align="center">
  <img src="https://github.com/RsGoksel/Genetic-Algorithm-Solutions/assets/80707238/140575ea-004d-40ad-83d4-a4f658048b71" width="500px"/>
</p>

In this work, the approach to solving games with Genetic Algorithms consists of three main classes.

  * Brain (Neural Network)
  * Agent 
  * Environment

    ![gif](https://github.com/RsGoksel/Genetic-Algorithm-Solutions/assets/80707238/8c45d988-f181-4b77-bdee-664117e08cf9)


## Brain and Agent
    
   Brain class has Weights, Layers, Activation Functions. Consider it Neural Network. 
   Gathered informations attachs to first layer of brain and eventually a prediction is obtained.

   Agent class has on the other hand has Brain class initially, also has variables which depends on the game, like movement settings, skill and limitations etc.  
    
- ! The depth of an artificial neural network (ANN) is important and may depend on the complexity of your problem. Choose a depth suitable for your problem.
  
![Brain-Agent](https://github.com/RsGoksel/Genetic-Algorithm-Solutions/blob/main/Game_Solutions/FlappyBird_Genetic/assets/Brain.png)

## Crossover

Crossover mechanism depends on the problem. There are Uniform Crossover, One-Point Crossover, Two-Point Crossover etc.
Generally in these game solutions uniform crossover has been used. 

*Uniform crossover involves selecting only one genome simultaneously from two different members.

![Crossover](https://github.com/RsGoksel/Genetic-Algorithms-Solutions/assets/80707238/cd154469-0566-4f05-87a4-deb9f59601ad)


When round is over, Died agents are fetched and chosen based on their own fitness values. Good ones (considering fitness function) are chosen and applied crossover. Pairs of weights from two parents are selected based on a probability coefficient and used to produce a new child agent, which may exhibit an improved fitness function.

________________________________________________________________________________________________

## Depiction of the approach


Every agent on the screen has own unique neural network. On another speech, during the initialization step of population creation, each agent is assigned unique weights.
In every generation or round, Best agents (considering their own fitness value) are chosen from all died agents and applied crossover. 

<img src="https://github.com/RsGoksel/Genetic-Algorithm-Solutions/assets/80707238/8bd79c28-238c-4109-98cf-ba573bd5059a" width="300" alt="Population">

The first step in the process is the creation of a population of agents. Each agent in this initial population is given a distinct set of neural network weights, resulting in a diverse starting point.

<img src="https://github.com/RsGoksel/Genetic-Algorithm-Solutions/blob/main/Game_Solutions/FlappyBird_Genetic/assets/Flap.png" width="600" alt="Population">


In every generation or round, Best agents (considering their own fitness value) are chosen from all died agents and applied crossover. 
Crossover process involves combining the neural network weights of two or more agents to create new agents (concept of genetic recombination)

<img src="https://github.com/RsGoksel/Genetic-Algorithm-Solutions/blob/main/Game_Solutions/FlappyBird_Genetic/assets/Neuro.png" width="600" alt="Population">

___________________________________________________________________________________________________________


2 external library required. Numpy and Pygame. You can install them with these

```bash
    pip install numpy
    pip install pygame
```
or
```bash
    pip install -r requirements.txt
```







