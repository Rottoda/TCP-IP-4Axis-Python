
import threading
from dobot_api import DobotApiDashboard, DobotApi, DobotApiMove, MyType
from time import sleep
import numpy as np

PARAMS=0
def connect_robot():
    try:
        ip = "192.168.1.6"
        dashboard_p = 29999
        move_p = 30003
        feed_p = 30004
        print("연결 중입니다...")
        dashboard = DobotApiDashboard(ip, dashboard_p)
        move = DobotApiMove(ip, move_p)
        feed = DobotApi(ip, feed_p)
        print(">.<연결성공>!<")
        return dashboard, move, feed
    except Exception as e:
        print(":(연결실패:(")
        raise e

if __name__ == '__main__':
    dashboard, move, feed = connect_robot()
   
    """
    ************************************
    ************************************
        if PARAMS  조건부 컴파일 지시에 매개변수가 있는가?
            0  지시문에 매개변수가 없습니다
            1  지시문에 매개변수가 포함되어 있습니다
            
        다음 지시를 포함하는 예제：
            EnableRobot
            DisableRobot
            DO
            AccJ
            SetArmOrientation
            RunScript
            PositiveSolution
            InverseSolution
            ModbusCreate
            GetHoldRegs
            DOGroup
            MovL
            MovLIO
            MoveJog
            Circle
    """
    
    """
    ************************************
    ************************************
     * 지시:EnableRobot
     * 성능:로봇 작동 허용
    """
    if PARAMS:
      dashboard.EnableRobot()    #인자 없음
    else:
       load=0.1
       centerX=100.1
       centerY=0.1
       centerZ=0.1
       dashboard.EnableRobot(load)    #하나의 인자
       
       dashboard.EnableRobot(load, centerX, centerY, centerZ)    #4개 인자
  
    """
    ************************************
    ************************************
     * 指令：DisableRobotexit
     * 功能：下使能机器人
    """
    dashboard.DisableRobot()    #인자 없음
     
     
    """
    ************************************
    ************************************
     * 指令： DO
     * 功能：设置数字输出端口状态（队列指令）
    """
    index=1
    status=1
    dashboard.DO(index,status)  
     
     
    """
     *******************************
     *******************************
     * 指令： AccJ
     * 功能：设置关节加速度比例。该指令仅对MovJ、MovJIO、MovJR、 JointMovJ指令有效
    """
    index=1
    dashboard.AccJ(index)  
     
     
    """
     ******************************
     ******************************
     * 指令： SetArmOrientation
     * 功能：设置手系指令。
    """
    if PARAMS:
        LorR=1
        dashboard.SetArmOrientation(LorR)    #하나의 인자
    else:
        LorR=1
        UorD=1
        ForN=1
        Config=1
        # orientation = f"{LorR},{UorD},{ForN},{Config}"
        # dashboard.SetArmOrientation(orientation)
        dashboard.SetArmOrientation(LorR, UorD, ForN, Config)    #4개의 매개변수
    
    
    """
    ************************************
    ************************************
     * 指令： RunScript
     * 功能：运行lua脚本。
    """
    name="luaname"
    dashboard.RunScript(name)  
     
    """
    ************************************
    ************************************
     * 指令： PositiveSolution
     * 功能：正解。（给定机器人各关节的角度，计算出机器人末端的空间位置）
    """
    J1=0.1
    J2=0.1
    J3=0.1
    J4=0.1
    User=1
    Tool=1
    dashboard.PositiveSolution(J1, J2, J3, J4,User, Tool)    #하나의 인자

     
    """
    ************************************
    ************************************
     * 指令： InverseSolution
     * 功能：逆解。（已知机器人末端的位置和姿态，计算机器人各关节的角度值）
    """  
    if PARAMS:
        J1=0.1
        J2=0.1
        J3=0.1
        J4=0.1
        User=1
        Tool=1
        dashboard.InverseSolution(J1, J2, J3, J4,User, Tool)    #하나의 인자
    else:
        J1=0.1
        J2=0.1
        J3=0.1
        J4=0.1
        User=1
        Tool=1
        isJointNear=1
        JointNear="JointNear"
        dashboard.InverseSolution(J1, J2, J3, J4,User, Tool,isJointNear, JointNear)  
        
    """
    ************************************
    ************************************
     * 指令： ModbusCreate
     * 功能：创建modbus主站
    """
    if PARAMS:
        ip="192.168.1.6"
        port=29999
        slave_id=1
        dashboard.ModbusCreate(ip, port, slave_id)    #3개의 인자
    else:
        ip="192.168.1.6"
        port=29999
        slave_id=1
        isRTU=1
        dashboard.ModbusCreate(ip, port, slave_id, isRTU)    #4개의 인자
     
     
    """
    ************************************
    ************************************
     * 指令： GetHoldRegs
     * 功能：读保持寄存器。
       """
    if PARAMS:
        index=1
        addr=1
        count=1
        dashboard.GetHoldRegs(index, addr, count)    #3개의 인자
    else:
        index=1
        addr=1
        count=1
        valType="valType"
        dashboard.GetHoldRegs(index, addr, count, valType)    #4개의 인자    
     
    """
    ************************************
    ************************************
     * 指令： DOGroup
     * 功能：设置输出组端口状态  (最大支持64个参数)
    """
    if PARAMS:
        index=1
        value=1
        dashboard.DOGroup(index, value)    #2个参数
    else:
        index=1
        value=1
        index2=1
        value2=1
        index32=1
        value32=1
        dashboard.DOGroup(index, value, index2, value2, index32, value32)    # 64개 인자 (일부 인자는 생략됨)
     
     
    """
    ************************************
    ************************************
     * 지령： MovL
     * 기능: 포인트 투 포인트(PtP) 이동, 목표 위치는 데카르트 좌표계 기준 점입니다
    """
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        move.MovL(x, y, z, r)    #선택 가능한 매개변수가 없습니다
    else:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        userparam="User=1"
        toolparam="Tool=1"
        speedlparam="SpeedL=1"
        acclparam="AccL=1"
        cpparam="CP=1" 
        move.MovL(x, y, z, r,userparam)    #设置user      可选参数顺序可换
        move.MovL(x, y, z, r,userparam, toolparam)    #设置user tool
        move.MovL(x, y, z, r,userparam, toolparam, speedlparam,)    #设置 user  tool  speedl 
        move.MovL(x, y, z, r,userparam, toolparam, speedlparam, acclparam)    #设置user  user  tool  speedl accl
        move.MovL(x, y, z, r,userparam, toolparam, speedlparam, acclparam, cpparam)    #设置 user  tool  speedl accl cp
     
     
    """
    ************************************
    ************************************
    * 指令： Arc
    * 功能：：从当前位置以圆弧插补方式移动至笛卡尔坐标系下的目标位置。
 	该指令需结合其他运动指令确定圆弧起始点。
    """
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        x2=1.0
        y2=1.0
        z2=1.0
        r2=1.0
        move.Arc(x, y, z, r,x2, y2, z2, r2)    #无可选参数
    else:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        x2=1.0
        y2=1.0
        z2=1.0
        r2=1.0
        userparam="User=1"
        toolparam="Tool=1"
        speedlparam="SpeedL=1"
        acclparam="AccL=1"
        cpparam="CP=1" 
        move.Arc(x, y, z, r,x2, y2, z2, r2,cpparam,userparam,speedlparam, toolparam, speedlparam, acclparam)    # user tool 顺序不固定可换
 
 
    """
    ************************************
    ************************************
     * 指令： MovLIO
     * 功能：在直线运动时并行设置数字输出端口状态，目标点位为笛卡尔点位。
    """
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        Mode=1
        Distance=1
        Index=1
        Status=1
        move.MovLIO(x, y, z, r, Mode, Distance, Index, Status)    #无可选参数
    else:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        Mode=1
        Distance=1
        Index=1
        Status=1
        userparam="User=1"
        toolparam="Tool=1"
        speedlparam="SpeedL=1"
        acclparam="AccL=1"
        cpparam="CP=1" 
        move.MovLIO(x, y, z, r,Mode, Distance, Index, Status,cpparam,userparam,speedlparam, toolparam, speedlparam, acclparam)    # user tool 顺序不固定可换    
     
    """
    ************************************
    ************************************
     * 指令： MoveJog
     * 功能：点动运动，不固定距离运动
    """
    if PARAMS:
        axisID=""
        move.MoveJog(axisID)           
    else:
        axisID="j1+"
        CoordType="CoordType=0"
        userparam="User=0"
        toolparam="Tool=0"
        move.MoveJog(axisID, CoordType, userparam, toolparam)    

    ##    发MoveJog()停止命令控制机器人停止运动
    move.MoveJog()
    
    
    """
    ************************************
    ************************************
     * 指令： Circle
     * 功能：整圆运动，仅对笛卡尔点位生效。
    """   
    if PARAMS:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        count=1
        move.Circle(x, y, z, r,count)           
    else:
        x=1.0
        y=1.0
        z=1.0
        r=1.0
        count=1
        userparam="User=0"
        toolparam="Tool=0"
        speedlparam="SpeedL=R"
        acclparam="AccL=R"
        move.Circle(x, y, z, r,count, userparam, toolparam, speedlparam, acclparam)       