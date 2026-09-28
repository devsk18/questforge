# QuestForge
QuestForge - a level-based challenge where you'll build a real, turn-based RPG battle engine.

# Level 0: Environment & Project Skeleton
Created project structure 
```
/questforge
    /domain         # core logic for the engine
    /infra          # tools & infra required
    /patterns       # design patterns 
    /tests          # test cases for the codebase
    main.py         # entrypoint
```

# Level 1: Classes & Objects
Added `Character` class with it's attributes and methods. A character can attack, heal and describe itself. It will have a name, health, max_health, attack_power for now.

# Level 2: Encapsulation
Added access specifiers, setters and getters to hide the properties from external access and mutations.

# Level 3: Inheritance 
Concept added to extend the features of Character class to it's subclasses which help us to form new characters without duplicating base code.