#Fateme Molaei Jahromi
#40216341070006

import numpy as np

class CDPR:
    def __init__(self, base_positions, platform_positions):
        """
        Initialize the CDPR with the positions of the base and platform attachment points.

        :param base_positions: 3D coordinates of the base attachment points (6x3 array)
        :param platform_positions: 3D coordinates of the platform attachment points (6x3 array)
        """
        self.base_positions = np.array(base_positions)
        self.platform_positions = np.array(platform_positions)

    def forward_kinematics(self, cable_lengths):
        """
        Calculate the platform position and orientation given the cable lengths.

        :param cable_lengths: Lengths of the cables (6-element array)
        :return: Platform position and orientation (x, y, z, roll, pitch, yaw)
        """
        # This is a placeholder function. Actual implementation would require solving a nonlinear system of equations.
        raise NotImplementedError("Forward kinematics is not implemented.")

    def inverse_kinematics(self, position, orientation):
        """
        Calculate the cable lengths given the platform position and orientation.

        :param position: Desired platform position (x, y, z)
        :param orientation: Desired platform orientation (roll, pitch, yaw)
        :return: Lengths of the cables (6-element array)
        """
        # Create the rotation matrix from roll, pitch, and yaw
        roll, pitch, yaw = orientation
        R_x = np.array([[1, 0, 0],
                        [0, np.cos(roll), -np.sin(roll)],
                        [0, np.sin(roll), np.cos(roll)]])
        
        R_y = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                        [0, 1, 0],
                        [-np.sin(pitch), 0, np.cos(pitch)]])
        
        R_z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                        [np.sin(yaw), np.cos(yaw), 0],
                        [0, 0, 1]])
        
        R = np.dot(R_z, np.dot(R_y, R_x))

        # Calculate the positions of the platform attachment points in the global frame
        platform_global_positions = np.dot(self.platform_positions, R.T) + position

        # Calculate the cable lengths
        cable_lengths = np.linalg.norm(platform_global_positions - self.base_positions, axis=1)
        return cable_lengths

# Example usage:
base_positions = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1]
]

platform_positions = [
    [-0.1, -0.1, 0],
    [0.1, -0.1, 0],
    [-0.1, 0.1, 0],
    [0.1, 0.1, 0],
    [-0.1, -0.1, 0.2],
    [0.1, -0.1, 0.2]
]

cdpr = CDPR(base_positions, platform_positions)

position = [0.5, 0.5, 0.5]
orientation = [0.1, 0.2, 0.3]  # roll, pitch, yaw in radians

cable_lengths = cdpr.inverse_kinematics(position, orientation)
print("Cable Lengths:", cable_lengths)
