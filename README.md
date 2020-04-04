# BB
Bouncing Balls in a box that don't interact with each other.

## REQUIREMENTS
I used Anaconda3 and therefore Python3.X. To run the python script you will need the __random, numpy, math, and matplotlib__ packages. These are included with the Anaconda distribution.

## DIRECTORIES
### SCRIPTS
Containes the __bouncing_balls.py__ python script.

### MOVIES
Containes an animated __bouncing_balls.gif__ file included as an example of what the code is outputing.

## OPTIONS
There are two integration options avialable: leapfrog and Yoshida. The leapfrog is a standard 2nd order scheme. In the game engine community the Verlet method may be a more ubiquitous choice but I'm a rebel like that. The Yoshida scheme is a 4th order scheme. It is certainly overkill for this application but, again, I'm a rebel like that. The code has a variety of other parameters that can be changed to meet your individual fancy and preferences. The number of balls can be changed from 1 to at least 10,000. However, at 10,000 the screen is so full of balls its rediculous. The code uses random variables for the initial conditions of the balls. Therefore, the initial x,y positons and velocities can be changed to suite your interests as well. If you don't like red balls you can easily change to whatever color makes you the happiest! I considered a rainbow option but time and all...

Last, but certainly not least, the code will animate a plot out of the box. If you would like to make a movie different than included in the /movie directory simply comment out the two lines marked in the Python file and your good-to-go!

## OS: Windows
```powershell
>python.exe bouncing_balls.py
```

## OS: Linux
```bash
>python bouncing_balls.py
```

## OS: macOS
TBD
