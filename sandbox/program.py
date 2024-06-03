"""
The Starship problem
Author: Brandi McPherson, brandimcpher@gmail.com
"""
import argparse

# CONSTANTS
# Rotation matrix for 90 degrees CCW [cos, -sin; sin, cos] and a constant "negative" val to flip to -90 deg rot matrix
_ROT_X = [0, -1]
_ROT_Y = [1, 0]
_NEG = -1
# Constant time unit
_TIME_UNIT = 1
# Constant velocity increment
_VEL_INC = 1

# Arg parser for CLI
parser = argparse.ArgumentParser(
    description="""Execute a series of maneuvers to move the FreeFlyer to its destination,
                                             which can be expressed as an [x,y] coordinate in a two-dimensional grid."""
)
parser.add_argument(
    "maneuvers",
    type=str,
    help="""A series of commands, as a string of any length. Commands may be defined with one of the following: L, R, 
    T, C, where L is a 90 deg CCW rotation, R is a 90 deg CW rotation, T fires the thrusters, and C cruises for one
            unit of time""",
)


class USSFreeFlyer:
    """
    Execute a series of maneuvers to move the FreeFlyer to its destination, which can be expressed as an [x,y]
    coordinate in a two-dimensional grid.
    """

    def __init__(self, maneuvers: str):
        """
        Constructor. Store commands and initial states.
        Args:
            maneuvers: A series of commands, as a string. Commands may be defined with one of the following: L, R, T, C,
            where L is a 90 deg CCW rotation, R is a 90 deg CW rotation, T fires the thrusters, and C cruises for one
            unit of time
        """
        # Store input maneuver commands and create registry of command executions
        self._input_commands = maneuvers
        self._CMD_REGISTRY = {
            "L": self._rotate_left,
            "R": self._rotate_right,
            "T": self._fire_thrusters,
            "C": self._cruise,
        }

        # Store starting states
        self._px, self._py = 0, 0
        self._vx, self._vy = 0, 0
        self._ox, self._oy = 1, 0

        # Begin commands for Starfleet's fastest starship, Freeflyer
        self._command_spacecraft()

    @property
    def position(self):
        """
        Easy access to position coords
        Returns:
            The spacecraft position
        """
        return self._px, self._py

    @property
    def velocity(self):
        """
        Easy access to velocity components
        Returns:
            The spacecraft velocity components
        """
        return self._vx, self._vy

    @property
    def orientation(self):
        """
        Easy access to pointing vector
        Returns:
            The spacecraft positing vector
        """
        return self._ox, self._oy

    def _rotate_left(self):
        """
        Rotate the FreeFlyer left (counter-clockwise) by 90 degrees. This command reorients the vehicle
        without changing its velocity vector. This action takes 1 unit of time, during which the FreeFlyer
        continues to cruise along its previous velocity vector.
        Returns:
            Executes cruise command and updates the pointing vector
        """
        # Cruise at previous velocity while rotation command occurs
        self._cruise()

        # Compute updated orientation x1, y1 = [rotation matrix] * [x,y] where rotation matrix is [cos -sin; sin cos]
        update_ox = _ROT_X[0] * self._ox + _ROT_X[1] * self._oy
        update_oy = _ROT_Y[0] * self._ox + _ROT_Y[1] * self._oy

        # Store updated orientation
        self._ox = update_ox
        self._oy = update_oy

    def _rotate_right(self):
        """
        Rotate the FreeFlyer right (clockwise) by 90 degrees. This command reorients the vehicle
        without changing its velocity vector. This action takes 1 unit of time, during which the FreeFlyer
        continues to cruise along its previous velocity vector.
        Returns:
            Executes cruise command and updates the pointing vector
        """
        # Cruise at previous velocity while rotation takes place
        self._cruise()

        # Compute updated orientation x1, y1 = [rotation matrix] * [x,y] where rotation matrix is [cos sin; -sin cos]
        update_ox = _NEG * _ROT_X[0] * self._ox + _NEG * _ROT_X[1] * self._oy
        update_oy = _NEG * _ROT_Y[0] * self._ox + _NEG * _ROT_Y[1] * self._oy

        # Store updated orientation
        self._ox = update_ox
        self._oy = update_oy

    def _fire_thrusters(self):
        """
        Fire thrusters. This is an instantaneous acceleration that increases the FreeFlyer's velocity by 1
        unit of velocity in the direction the FreeFlyer is facing. This action occurs immediately and then
        the FreeFlyer "cruises" for 1 unit of time.
        Returns:
            Updates the velocity vector and executes cruise commands
        """
        # Increment the velocity in the appropriate direction for a time unit
        self._vx += _VEL_INC * self._ox
        self._vy += _VEL_INC * self._oy

        # Cruise at new velocity
        self._cruise()

    def _cruise(self):
        """
        Cruise. The FreeFlyer cruises for 1 unit of time, during which its position updates based on its
        velocity.
        Returns:
            Updates the position coordinates
        """
        # Update the x, y position with pos = vel * time
        self._px += self._vx * _TIME_UNIT
        self._py += self._vy * _TIME_UNIT

    def _command_spacecraft(self):
        """
        Executes the given commands and prints final states to console
        Returns:
            printed final position, velocity, and orientation
        """
        # Loop though commands in sequence. Catch any incorrect commands
        for command in self._input_commands:
            # Pull command from registry and execute
            try:
                self._CMD_REGISTRY[command]()
            except KeyError:
                print(
                    f"Invalid command '{command}'. Please use one of the following: L, R, T, C"
                )
                return

        # Print out final states
        print(f"[{self._px}, {self._py}]")
        print(f"[{self._vx}, {self._vy}]")
        print(f"[{self._ox}, {self._oy}]")


# CLI
if __name__ == "__main__":
    inputs = parser.parse_args()
    output = USSFreeFlyer(inputs.maneuvers)
