import os
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

class UnitreeG1Base(ru.ImportedRobotModel):
    def __init__(self, robot=None, item=True, world=False, **kwargs):
        super().__init__(robot=robot, item=item, world=world, **kwargs)

    def _init_ending(self, **kwargs): ## override
        self._off_z = -0.035
        self._off_x = 0.035
        self._hand_off_x = 0.1
        self._hand_off_y = 0.035
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
        self.registerEndEffector('larm', ## end-effector
                                 'left_wrist_yaw_link', ## tip-link
                                 tip_link_to_eef = coordinates(fv(self._hand_off_x, - self._hand_off_y, 0)),
                                 joint_tuples = (('left_shoulder_pitch_joint', 'shoulder-p'),
                                                 ('left_shoulder_roll_joint',  'shoulder-r'),
                                                 ('left_shoulder_yaw_joint',   'shoulder-y'),
                                                 ('left_elbow_joint',          'elbow-p'),
                                                 ('left_wrist_roll_joint',     'wrist-r'),## yaw
                                                 ('left_wrist_pitch_joint',    'wrist-p'),
                                                 ('left_wrist_yaw_joint',      'wrist-y'),## roll
                                                 )
                                 )
        self.registerEndEffector('rarm', ## end-effector
                                 'right_wrist_yaw_link', ## tip-link
                                 tip_link_to_eef = coordinates(fv(self._hand_off_x, self._hand_off_y, 0)),
                                 joint_tuples = (('right_shoulder_pitch_joint', 'shoulder-p'),
                                                 ('right_shoulder_roll_joint',  'shoulder-r'),
                                                 ('right_shoulder_yaw_joint',   'shoulder-y'),
                                                 ('right_elbow_joint',          'elbow-p'),
                                                 ('right_wrist_roll_joint',     'wrist-r'),## yaw
                                                 ('right_wrist_pitch_joint',    'wrist-p'),
                                                 ('right_wrist_yaw_joint',      'wrist-y'),## roll
                                                 )
                                 )
        self.registerEndEffector('torso', ## end-effector (this is just used as joint group)
                                 'torso_link', ## tip-link
                                 #tip_link_to_eef = coordinates(fv(self._off_x, 0, self._off_z)),
                                 joint_tuples = (('waist_yaw_joint',   'waist-y'),
                                                 ('waist_roll_joint',  'waist-r'),
                                                 ('waist_pitch_joint', 'waist-p'),
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

class UnitreeG129dofSimple(UnitreeG1Base):
    pass

class UnitreeG129dof(UnitreeG1Base):
    pass

## TODO
class UnitreeG129dofDex3Simple(UnitreeG1Base):
    pass

class UnitreeG129dofDex3(UnitreeG1Base):
    pass

#class UnitreeG1Simple23dof(UnitreeG1Base):
#    pass

#class UnitreeG123dof(UnitreeG1Base):
#    pass


### settings of model_file
UnitreeG129dofSimple.model_file = f'{os.path.dirname(__file__)}/simple_unitree_g1_29dof_mode_15.body'
UnitreeG129dof.model_file = f'{os.path.dirname(__file__)}/unitree_ros/robots/g1_description/g1_29dof_mode_15.urdf'
UnitreeG129dofDex3Simple.model_file = f'{os.path.dirname(__file__)}/simple_unitree_g1_29dof_mode_15.body'
UnitreeG129dofDex3.model_file = f'{os.path.dirname(__file__)}/unitree_ros/robots/g1_description/g1_29dof_mode_15.urdf'
#class UnitreeG1Simple23dof.model_file = f'{os.path.dirname(__file__)}/simple_unitree_g1_29dof_mode_15.body'
#class UnitreeG123dof.model_file = f'{os.path.dirname(__file__)}/simple_unitree_g1_29dof_mode_15.body'

### robot_class:
#robot_class = UnitreeG129dofSimple
robot_class = UnitreeG129dof

_robot_type_map = {
    "G129dofSimple" : UnitreeG129dofSimple,
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
