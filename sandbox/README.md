# USSFreeFlyer
Contents:
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
   1. [I/O](#io)
   2. [Running the program](#running-the-program)
4. [Tests](#tests)

## Description
The `USSFreeFlyer` Python program executes a series of maneuvers to move the USS FreeFlyer to its destination, which can be expressed as an 
`[x,y]` coordinate in a two-dimensional grid. Your starship can process the following commands:

`L`:
Rotate the FreeFlyer left (counter-clockwise) by 90 degrees. This command reorients the vehicle
without changing its velocity vector. This action takes 1 unit of time, during which the FreeFlyer
continues to cruise along its previous velocity vector.

`R`:
Rotate the FreeFlyer right (clockwise) by 90 degrees. This command reorients the vehicle
without changing its velocity vector. This action takes 1 unit of time, during which the FreeFlyer
continues to cruise along its previous velocity vector.

`T`:
Fire thrusters. This is an instantaneous acceleration that increases the FreeFlyer's velocity by 1
unit of velocity in the direction the FreeFlyer is facing. This action occurs immediately and then
the FreeFlyer "cruises" for 1 unit of time.

`C`:
Cruise. The FreeFlyer cruises for 1 unit of time, during which its position updates based on its
velocity.

## Installation

`USSFreeFlyer` requires a standard Python installation but no additional packages or libraries. 

## Usage
### I/O
`USSFreeFlyer` takes in a series of commands of any length using the above definitions (LRTC). After the final 
maneuver in the series is completed, the final position, velocity, and orientation are output to the console. 

Example inputs: 
1. TLLT: FreeFlyer thrusts in the positive x-direction, turns around and thrusts in the negative x-direction, causing it
to stop.
2. TLLTRTRRCCCT: FreeFlyer moves in the positive x-direction 3 units and then in the
positive y-direction by 6 units. Note that the FreeFlyer cruises towards
the end of the maneuver plan before stopping.
3. LTLLTTRRT: FreeFlyer moves in the position y-direction, turns around, and returns to
the origin

Example outputs (TLLT):
```powershell
[3, 0]
[0, 0]
[-1, 0]
```
Example outputs (TLLTRTRRCCCT):
```powershell
[3, 6]
[0, 0]
[0, -1]
```
Example outputs (LTLLTTRRT):
```powershell
[0, 0]
[0, 0]
[0, 1]
```

### Running the program
For command-line interface (Windows PowerShell), navigate to the directory containing `program.py` and execute the 
following command:
```powershell
python .\program.py TLLT
```

As a Python script:

```python
from program import USSFreeFlyer

# Add maneuvers 
commands = "TLLT"
free_flyer = USSFreeFlyer(commands)

# Access properties 
pos_x, pos_y = free_flyer.position
vel_x, vel_y = free_flyer.velocity
o_x, o_y = free_flyer.orientation
```

## Tests
Unit and case tests are included in `test_freeflyer.py` for quick validation and examples. This program was 
tested with Python 3.12 on Windows 11.



