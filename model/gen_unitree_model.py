# export PYTHONPATH=/choreonoid_ws/src/irsl_python_lib:$PYTHONPATH
# git clone https://github.com/unitreerobotics/unitree_ros
# exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

#
# generate body from list
#
import irsl_cnoid.robot_graph.robot_graph as mrg

if True:
    exec(open('link.py').read()) ## load lst and devlist
    #gg = mrg.RobotTree.generate_from_list(lst, add_root=True)
    gg = mrg.RobotTree.generate_from_list(lst, add_root=False)
    gg.update_coords()
    #
    gg.add_geometries_for_joints(scale=0.14)
    gg.add_geometries_for_links(scale=0.16)
rtb = mrg.RobotTreeBuilder(); rtb.buildRobotFromTree(gg)
rtb.addDeviceFromMap(devlist)
rtb.exportBody('simple_unitree_g1_29dof_mode_15.body', modelName='UnitreeG1')
rtb.viewInfo()

#
# make link-list
#
import irsl_cnoid.robot_graph.robot_graph as mrg

robot = RobotModel.loadModelItem('unitree_ros/robots/g1_description/g1_29dof_mode_15.urdf')

gg = mrg.RobotTree.generate_from_body(robot.robot)
gg.update_coords()
lst=gg.make_list()

print(lst)
## add additional geometries to list

#
# simplify body
#
exec(open('simplify_body.py').read())
bd = iu.loadRobot('simple_unitree_g1_29dof_mode_15.body')
simplifyBody(bd)
iu.exportBody('/tmp/hoge.body', bd)
rb = RobotBuilder('/tmp/hoge.body')
rb.viewInfo()

## check model
import unitree_g1_model
robot = unitree_g1_model.makeUnitreeRobot('G1Simple29dof')
urdf = unitree_g1_model.makeUnitreeRobot('G129dof')

su = set(urdf.linkNames)
sr = set(robot.linkNames)
su.difference(sr)
sr.difference(su)

for n in su.intersection(sr):
    res = ru.equalLink(robot.link(n), urdf.link(n), eps=1e-4)
    if not res:
        print(n)
