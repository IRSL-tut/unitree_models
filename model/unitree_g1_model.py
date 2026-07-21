import os
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

class UnitreeG1Base(ru.ImportedRobotModel):
    def __init__(self, robot=None, item=True, world=False, **kwargs):
        super().__init__(robot=robot, item=item, world=world, **kwargs)

    def _init_ending(self, **kwargs): ## override
        self._off_z = -0.035
        self._off_x = 0.035
        self.registerEndEffector('lleg', ## end-effector
                                 'left_ankle_roll_link', ## tip-link
                                 tip_link_to_eef = coordinates(fv(self._off_x, 0, self._off_z)),
                                 joint_tuples = (('left_hip_pitch_joint',  'hip-p'),
                                                 ('left_hip_roll_joint',   'hip-r'),
                                                 ('left_hip_yaw_joint',    'hip-y'),
                                                 ('left_knee_joint',       'knee-p'),
                                                 ('left_ankle_pitch_joint','ankle-p'),
                                                 ('left_ankle_roll_joint', 'ankle-r'),
                                                 )
                                 )
        self.registerEndEffector('rleg', ## end-effector
                                 'right_ankle_roll_link', ## tip-link
                                 tip_link_to_eef = coordinates(fv(self._off_x, 0, self._off_z)),
                                 joint_tuples = (('right_hip_pitch_joint',  'hip-p'),
                                                 ('right_hip_roll_joint',   'hip-r'),
                                                 ('right_hip_yaw_joint',    'hip-y'),
                                                 ('right_knee_joint',       'knee-p'),
                                                 ('right_ankle_pitch_joint','ankle-p'),
                                                 ('right_ankle_roll_joint', 'ankle-r'),
                                                 )
                                 )

        self.registerNamedPose('default', ## CoM = 0, 0, xxx
                               [-0.5046941624051353, 0, 0, 0.9994336176391199, -0.4947393502417313, 0,
                                -0.5046941624051353, 0, 0, 0.9994336176391199, -0.4947393502417313, 0,
                                0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,],
                               ru.make_coordinates( {'pos': [0.0, 0.0, 0.713926 ]} )
                               )

class UnitreeG1Simple29dof(UnitreeG1Base):
    pass

class UnitreeG129dof(UnitreeG1Base):
    pass

class UnitreeG1Simple23dof(UnitreeG1Base):
    pass

class UnitreeG123dof(UnitreeG1Base):
    pass

### settings of model_file
UnitreeG1Simple29dof.model_file = f'{os.path.dirname(__file__)}/simple_unitree_g1_29dof_mode_15.body'
UnitreeG129dof.model_file = f'{os.path.dirname(__file__)}/unitree_ros/robots/g1_description/g1_29dof_mode_15.urdf'
#class UnitreeG1Simple23dof.model_file = f'{os.path.dirname(__file__)}/simple_unitree_g1_29dof_mode_15.body'
#class UnitreeG123dof.model_file = f'{os.path.dirname(__file__)}/simple_unitree_g1_29dof_mode_15.body'

### robot_class:
robot_class = UnitreeG1Simple29dof

_robot_type_map = {
    "G1Simple29dof" : UnitreeG1Simple29dof,
    "G129dof"       : UnitreeG129dof,
}
### makeRobot(robot=None, **kwargs):
def makeRobot(robot=None, item=True, world=True, **kwargs):
    return robot_class(robot, item=item, world=world, **kwargs)

def makeUnitreeRobot(robot_type_name=None, item=True, world=True, **kwargs):
    if robot_type_name in _robot_type_map:
        cls = _robot_type_map[robot_type_name]
        return cls(item=item, world=world, **kwargs)
    else:
        print(f'robot_type_name should be in {_robot_type_map.keys()}')
