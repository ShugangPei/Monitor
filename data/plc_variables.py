# PLC 连接信息
PLC_URL = "opc.tcp://192.168.1.10:4840"
USERNAME = "admin"
PASSWORD = "admin"


VARIABLES = {
    # CNC控制（14 个）
    "CNCStatus": {"node": "ns=2;s=Application.GVL_HMI.CNCStatus", "type": "Int16", "comment": "CNC状态", "writable": False},
    "CNCSourceNo": {"node": "ns=2;s=Application.GVL_HMI.CNCSourceNo", "type": "Int32", "comment": "CNC运行行号", "writable": False},
    "CNCwm": {"node": "ns=2;s=Application.GVL_HMI.CNCwm", "type": "UInt16", "comment": "CNC切割参数号", "writable": False},
    "CNCiLastSwitch": {"node": "ns=2;s=Application.GVL_HMI.CNCiLastSwitch", "type": "Int16", "comment": "CNC最终开关号", "writable": False},
    "CNC_MODE": {"node": "ns=2;s=Application.GVL_HMI.CNC_MODE", "type": "Boolean", "comment": "CNC模式", "writable": True},
    "CNC_Manual": {"node": "ns=2;s=Application.GVL_HMI.CNC_Manual", "type": "Boolean", "comment": "手动模式(非CNC)", "writable": True},
    "CNC_Ready": {"node": "ns=2;s=Application.GVL_HMI.CNC_Ready", "type": "Boolean", "comment": "CNC准备", "writable": True},
    "CNC_Start": {"node": "ns=2;s=Application.GVL_HMI.CNC_Start", "type": "Boolean", "comment": "CNC启动", "writable": True},
    "CNC_WKStop": {"node": "ns=2;s=Application.GVL_HMI.CNC_WKStop", "type": "Boolean", "comment": "CNC确认步", "writable": True},
    "CNC_Read1": {"node": "ns=2;s=Application.GVL_HMI.CNC_Read1", "type": "Boolean", "comment": "CNC读文件", "writable": True},
    "XY_HOME": {"node": "ns=2;s=Application.GVL_HMI.XY_HOME", "type": "Boolean", "comment": "XY回零", "writable": True},
    "CNC_Pause": {"node": "ns=2;s=Application.GVL_HMI.CNC_Pause", "type": "Boolean", "comment": "CNC暂停", "writable": True},
    "CNC_Stop": {"node": "ns=2;s=Application.GVL_HMI.CNC_Stop", "type": "Boolean", "comment": "CNC停止", "writable": True},
    "CNC_Resst": {"node": "ns=2;s=Application.GVL_HMI.CNC_Resst", "type": "Boolean", "comment": "CNC复位", "writable": True},
    # X轴（16 个）
    "X_POWER": {"node": "ns=2;s=Application.GVL_HMI.X_POWER", "type": "Boolean", "comment": "X轴使能", "writable": True},
    "X_REST": {"node": "ns=2;s=Application.GVL_HMI.X_REST", "type": "Boolean", "comment": "X轴复位", "writable": True},
    "X_Stop": {"node": "ns=2;s=Application.GVL_HMI.X_Stop", "type": "Boolean", "comment": "X轴停止", "writable": True},
    "X_JogNeg": {"node": "ns=2;s=Application.GVL_HMI.X_JogNeg", "type": "Boolean", "comment": "X轴正转", "writable": True},
    "X_Jogrev": {"node": "ns=2;s=Application.GVL_HMI.X_Jogrev", "type": "Boolean", "comment": "X轴反转", "writable": True},
    "X_MoveAbs": {"node": "ns=2;s=Application.GVL_HMI.X_MoveAbs", "type": "Boolean", "comment": "X轴定位", "writable": True},
    "X_HOME": {"node": "ns=2;s=Application.GVL_HMI.X_HOME", "type": "Boolean", "comment": "X轴回原点", "writable": True},
    "X_PosNow": {"node": "ns=2;s=Application.GVL_HMI.X_PosNow", "type": "REAL", "comment": "X轴当前位置", "writable": False},
    "X_MoveVel": {"node": "ns=2;s=Application.GVL_HMI.X_MoveVel", "type": "REAL", "comment": "X轴速度", "writable": True},
    "X_MoveABSPos": {"node": "ns=2;s=Application.GVL_HMI.X_MoveABSPos", "type": "REAL", "comment": "X轴定位位置", "writable": True},
    "X_MoveRelaDist": {"node": "ns=2;s=Application.GVL_HMI.X_MoveRelaDist", "type": "REAL", "comment": "X轴相对位移值", "writable": True},
    "X_Moveacc": {"node": "ns=2;s=Application.GVL_HMI.X_Moveacc", "type": "REAL", "comment": "X轴加速", "writable": True},
    "X_Movedec": {"node": "ns=2;s=Application.GVL_HMI.X_Movedec", "type": "REAL", "comment": "X轴减速", "writable": True},
    "X_Stopdec": {"node": "ns=2;s=Application.GVL_HMI.X_Stopdec", "type": "REAL", "comment": "X轴急停减速", "writable": True},
    "X_MoveRela_done": {"node": "ns=2;s=Application.GVL_HMI.X_MoveRela_done", "type": "Boolean", "comment": "X轴相对运动完成", "writable": False},
    "X_MoveAbs_done": {"node": "ns=2;s=Application.GVL_HMI.X_MoveAbs_done", "type": "Boolean", "comment": "X轴定位完成", "writable": False},
    # Y轴（16 个）
    "Y_POWER": {"node": "ns=2;s=Application.GVL_HMI.Y_POWER", "type": "Boolean", "comment": "Y轴使能", "writable": True},
    "Y_REST": {"node": "ns=2;s=Application.GVL_HMI.Y_REST", "type": "Boolean", "comment": "Y轴复位", "writable": True},
    "Y_Stop": {"node": "ns=2;s=Application.GVL_HMI.Y_Stop", "type": "Boolean", "comment": "Y轴停止", "writable": True},
    "Y_JogNeg": {"node": "ns=2;s=Application.GVL_HMI.Y_JogNeg", "type": "Boolean", "comment": "Y轴正转", "writable": True},
    "Y_Jogrev": {"node": "ns=2;s=Application.GVL_HMI.Y_Jogrev", "type": "Boolean", "comment": "Y轴反转", "writable": True},
    "Y_MoveAbs": {"node": "ns=2;s=Application.GVL_HMI.Y_MoveAbs", "type": "Boolean", "comment": "Y轴定位", "writable": True},
    "Y_HOME": {"node": "ns=2;s=Application.GVL_HMI.Y_HOME", "type": "Boolean", "comment": "Y轴回原点", "writable": True},
    "Y_PosNow": {"node": "ns=2;s=Application.GVL_HMI.Y_PosNow", "type": "REAL", "comment": "Y轴当前位置", "writable": False},
    "Y_MoveVel": {"node": "ns=2;s=Application.GVL_HMI.Y_MoveVel", "type": "REAL", "comment": "Y轴速度", "writable": True},
    "Y_MoveABSPos": {"node": "ns=2;s=Application.GVL_HMI.Y_MoveABSPos", "type": "REAL", "comment": "Y轴定位位置", "writable": True},
    "Y_MoveRelaDist": {"node": "ns=2;s=Application.GVL_HMI.Y_MoveRelaDist", "type": "REAL", "comment": "Y轴相对位移值", "writable": True},
    "Y_Moveacc": {"node": "ns=2;s=Application.GVL_HMI.Y_Moveacc", "type": "REAL", "comment": "Y轴加速", "writable": True},
    "Y_Movedec": {"node": "ns=2;s=Application.GVL_HMI.Y_Movedec", "type": "REAL", "comment": "Y轴减速", "writable": True},
    "Y_Stopdec": {"node": "ns=2;s=Application.GVL_HMI.Y_Stopdec", "type": "REAL", "comment": "Y轴急停减速", "writable": True},
    "Y_MoveRela_done": {"node": "ns=2;s=Application.GVL_HMI.Y_MoveRela_done", "type": "Boolean", "comment": "Y轴相对运动完成", "writable": False},
    "Y_MoveAbs_done": {"node": "ns=2;s=Application.GVL_HMI.Y_MoveAbs_done", "type": "Boolean", "comment": "Y轴定位完成", "writable": False},
    # A轴（16 个）
    "A_POWER": {"node": "ns=2;s=Application.GVL_HMI.A_POWER", "type": "Boolean", "comment": "A轴使能", "writable": True},
    "A_REST": {"node": "ns=2;s=Application.GVL_HMI.A_REST", "type": "Boolean", "comment": "A轴复位", "writable": True},
    "A_Stop": {"node": "ns=2;s=Application.GVL_HMI.A_Stop", "type": "Boolean", "comment": "A轴停止", "writable": True},
    "A_JogNeg": {"node": "ns=2;s=Application.GVL_HMI.A_JogNeg", "type": "Boolean", "comment": "A轴正转", "writable": True},
    "A_Jogrev": {"node": "ns=2;s=Application.GVL_HMI.A_Jogrev", "type": "Boolean", "comment": "A轴反转", "writable": True},
    "A_MoveAbs": {"node": "ns=2;s=Application.GVL_HMI.A_MoveAbs", "type": "Boolean", "comment": "A轴定位", "writable": True},
    "A_HOME": {"node": "ns=2;s=Application.GVL_HMI.A_HOME", "type": "Boolean", "comment": "A轴回原点", "writable": True},
    "A_PosNow": {"node": "ns=2;s=Application.GVL_HMI.A_PosNow", "type": "REAL", "comment": "A轴当前位置", "writable": False},
    "A_MoveVel": {"node": "ns=2;s=Application.GVL_HMI.A_MoveVel", "type": "REAL", "comment": "A轴速度", "writable": True},
    "A_MoveABSPos": {"node": "ns=2;s=Application.GVL_HMI.A_MoveABSPos", "type": "REAL", "comment": "A轴定位位置", "writable": True},
    "A_MoveRelaDist": {"node": "ns=2;s=Application.GVL_HMI.A_MoveRelaDist", "type": "REAL", "comment": "A轴相对位移值", "writable": True},
    "A_Moveacc": {"node": "ns=2;s=Application.GVL_HMI.A_Moveacc", "type": "REAL", "comment": "A轴加速", "writable": True},
    "A_Movedec": {"node": "ns=2;s=Application.GVL_HMI.A_Movedec", "type": "REAL", "comment": "A轴减速", "writable": True},
    "A_Stopdec": {"node": "ns=2;s=Application.GVL_HMI.A_Stopdec", "type": "REAL", "comment": "A轴急停减速", "writable": True},
    "A_MoveRela_done": {"node": "ns=2;s=Application.GVL_HMI.A_MoveRela_done", "type": "Boolean", "comment": "A轴相对运动完成", "writable": False},
    "A_MoveAbs_done": {"node": "ns=2;s=Application.GVL_HMI.A_MoveAbs_done", "type": "Boolean", "comment": "A轴定位完成", "writable": False},
    # B轴（16 个）
    "B_POWER": {"node": "ns=2;s=Application.GVL_HMI.B_POWER", "type": "Boolean", "comment": "B轴使能", "writable": True},
    "B_REST": {"node": "ns=2;s=Application.GVL_HMI.B_REST", "type": "Boolean", "comment": "B轴复位", "writable": True},
    "B_Stop": {"node": "ns=2;s=Application.GVL_HMI.B_Stop", "type": "Boolean", "comment": "B轴停止", "writable": True},
    "B_Jogrev": {"node": "ns=2;s=Application.GVL_HMI.B_Jogrev", "type": "Boolean", "comment": "B轴反转", "writable": True},
    "B_JogNeg": {"node": "ns=2;s=Application.GVL_HMI.B_JogNeg", "type": "Boolean", "comment": "B轴正转", "writable": True},
    "B_MoveAbs": {"node": "ns=2;s=Application.GVL_HMI.B_MoveAbs", "type": "Boolean", "comment": "B轴定位", "writable": True},
    "B_HOME": {"node": "ns=2;s=Application.GVL_HMI.B_HOME", "type": "Boolean", "comment": "B轴回原点", "writable": True},
    "B_PosNow": {"node": "ns=2;s=Application.GVL_HMI.B_PosNow", "type": "REAL", "comment": "B轴当前位置", "writable": False},
    "B_MoveVel": {"node": "ns=2;s=Application.GVL_HMI.B_MoveVel", "type": "REAL", "comment": "B轴速度", "writable": True},
    "B_MoveABSPos": {"node": "ns=2;s=Application.GVL_HMI.B_MoveABSPos", "type": "REAL", "comment": "B轴定位位置", "writable": True},
    "B_MoveRelaDist": {"node": "ns=2;s=Application.GVL_HMI.B_MoveRelaDist", "type": "REAL", "comment": "B轴相对位移值", "writable": True},
    "B_Moveacc": {"node": "ns=2;s=Application.GVL_HMI.B_Moveacc", "type": "REAL", "comment": "B轴加速", "writable": True},
    "B_Movedec": {"node": "ns=2;s=Application.GVL_HMI.B_Movedec", "type": "REAL", "comment": "B轴减速", "writable": True},
    "B_Stopdec": {"node": "ns=2;s=Application.GVL_HMI.B_Stopdec", "type": "REAL", "comment": "B轴急停减速", "writable": True},
    "B_MoveRela_done": {"node": "ns=2;s=Application.GVL_HMI.B_MoveRela_done", "type": "Boolean", "comment": "B轴相对运动完成", "writable": False},
    "B_MoveAbs_done": {"node": "ns=2;s=Application.GVL_HMI.B_MoveAbs_done", "type": "Boolean", "comment": "B轴定位完成", "writable": False},
    # Z轴（16 个）
    "Z_POWER": {"node": "ns=2;s=Application.GVL_HMI.Z_POWER", "type": "Boolean", "comment": "Z轴使能", "writable": True},
    "Z_REST": {"node": "ns=2;s=Application.GVL_HMI.Z_REST", "type": "Boolean", "comment": "Z轴复位", "writable": True},
    "Z_Stop": {"node": "ns=2;s=Application.GVL_HMI.Z_Stop", "type": "Boolean", "comment": "Z轴停止", "writable": True},
    "Z_Jogrev": {"node": "ns=2;s=Application.GVL_HMI.Z_Jogrev", "type": "Boolean", "comment": "Z轴反转", "writable": True},
    "Z_JogNeg": {"node": "ns=2;s=Application.GVL_HMI.Z_JogNeg", "type": "Boolean", "comment": "Z轴正转", "writable": True},
    "Z_MoveAbs": {"node": "ns=2;s=Application.GVL_HMI.Z_MoveAbs", "type": "Boolean", "comment": "Z轴定位", "writable": True},
    "Z_HOME": {"node": "ns=2;s=Application.GVL_HMI.Z_HOME", "type": "Boolean", "comment": "Z轴回原点", "writable": True},
    "Z_PosNow": {"node": "ns=2;s=Application.GVL_HMI.Z_PosNow", "type": "REAL", "comment": "Z轴当前位置", "writable": False},
    "Z_MoveVel": {"node": "ns=2;s=Application.GVL_HMI.Z_MoveVel", "type": "REAL", "comment": "Z轴速度", "writable": True},
    "Z_MoveABSPos": {"node": "ns=2;s=Application.GVL_HMI.Z_MoveABSPos", "type": "REAL", "comment": "Z轴定位位置", "writable": True},
    "Z_Moveacc": {"node": "ns=2;s=Application.GVL_HMI.Z_Moveacc", "type": "REAL", "comment": "Z轴加速", "writable": True},
    "Z_Movedec": {"node": "ns=2;s=Application.GVL_HMI.Z_Movedec", "type": "REAL", "comment": "Z轴减速", "writable": True},
    "Z_Stopdec": {"node": "ns=2;s=Application.GVL_HMI.Z_Stopdec", "type": "REAL", "comment": "Z轴急停减速", "writable": True},
    "Z_MoveRelaDist": {"node": "ns=2;s=Application.GVL_HMI.Z_MoveRelaDist", "type": "REAL", "comment": "Z轴相对位移值", "writable": True},
    "Z_MoveRela_done": {"node": "ns=2;s=Application.GVL_HMI.Z_MoveRela_done", "type": "Boolean", "comment": "Z轴相对运动完成", "writable": False},
    "Z_MoveAbs_done": {"node": "ns=2;s=Application.GVL_HMI.Z_MoveAbs_done", "type": "Boolean", "comment": "Z轴定位完成", "writable": False},
    # 密封测试（13 个）
    "CHAMBER_O2_OK_SEAL": {"node": "ns=2;s=Application.GVL_HMI.CHAMBER_O2_OK", "type": "Boolean", "comment": "氧含量OK", "writable": False},
    "AI_HP_O2_CONTENT_OUTPUT_SEAL": {"node": "ns=2;s=Application.GVL_HMI.AI_HP_O2_CONTENT_OUTPUT", "type": "Float", "comment": "高精度氧含量值", "writable": False},
    "AI_LP_O2_CONTENT_OUTPUT_SEAL": {"node": "ns=2;s=Application.GVL_HMI.AI_LP_O2_CONTENT_OUTPUT", "type": "Float", "comment": "低精度氧含量值", "writable": False},
    "AI_CHAMBER_PRESSURE_OUTPUT_SEAL": {"node": "ns=2;s=Application.GVL_HMI.AI_CHAMBER_PRESSURE_OUTPUT", "type": "REAL", "comment": "工作腔压力值", "writable": False},
    "AI_CHAMBER_O2_CONTENT_OUTPUT_SEAL": {"node": "ns=2;s=Application.GVL_HMI.AI_CHAMBER_O2_CONTENT_OUTPUT", "type": "REAL", "comment": "工作腔氧含量值(PPM)", "writable": False},
    "SOLENOID_VALVE_CONTROL_MODE": {"node": "ns=2;s=Application.GVL_HMI.SOLENOID_VALVE_CONTROL_MODE", "type": "Int16", "comment": "电磁阀控制模式", "writable": False},
    "MANUAL_TEST_MODE": {"node": "ns=2;s=Application.GVL_HMI.MANUAL_TEST_MODE", "type": "Boolean", "comment": "手动测试模式", "writable": True},
    "EXHAUST_VALVE_1_ENABLE_H_1": {"node": "ns=2;s=Application.GVL_HMI.EXHAUST_VALVE_1_ENABLE_H_1", "type": "Boolean", "comment": "排气阀1手动打开", "writable": True},
    "EXHAUST_VALVE_2_ENABLE_H_1": {"node": "ns=2;s=Application.GVL_HMI.EXHAUST_VALVE_2_ENABLE_H_1", "type": "Boolean", "comment": "排气阀2手动打开", "writable": True},
    "FAST_FLUX_VALVE_ENBLE_H_1": {"node": "ns=2;s=Application.GVL_HMI.FAST_FLUX_VALVE_ENBLE_H_1", "type": "Boolean", "comment": "快速气阀手动打开", "writable": True},
    "SLOW_FLUX_VALVE_ENBLE_H_1": {"node": "ns=2;s=Application.GVL_HMI.SLOW_FLUX_VALVE_ENBLE_H_1", "type": "Boolean", "comment": "慢速气阀手动打开", "writable": True},
    "AUTO_TEST_MODE": {"node": "ns=2;s=Application.GVL_HMI.AUTO_TEST_MODE", "type": "Boolean", "comment": "自动测试模式", "writable": True},
    "START_AIR_CLEAN": {"node": "ns=2;s=Application.GVL_HMI.START_AIR_CLEAN", "type": "Boolean", "comment": "自动洗气", "writable": True},
    # 激光和风机（10 个）
    "CHAMBER_O2_OK_LASER": {"node": "ns=2;s=Application.GVL_HMI.CHAMBER_O2_OK", "type": "Boolean", "comment": "氧含量OK", "writable": False},
    "AI_HP_O2_CONTENT_OUTPUT_LASER": {"node": "ns=2;s=Application.GVL_HMI.AI_HP_O2_CONTENT_OUTPUT", "type": "Float", "comment": "高精度氧含量值", "writable": False},
    "AI_LP_O2_CONTENT_OUTPUT_LASER": {"node": "ns=2;s=Application.GVL_HMI.AI_LP_O2_CONTENT_OUTPUT", "type": "Float", "comment": "低精度氧含量值", "writable": False},
    "AI_CHAMBER_O2_CONTENT_OUTPUT_LASER": {"node": "ns=2;s=Application.GVL_HMI.AI_CHAMBER_O2_CONTENT_OUTPUT", "type": "REAL", "comment": "工作腔氧含量值(PPM)", "writable": False},
    "AI_CHAMBER_PRESSURE_OUTPUT_LASER": {"node": "ns=2;s=Application.GVL_HMI.AI_CHAMBER_PRESSURE_OUTPUT", "type": "REAL", "comment": "工作腔压力值", "writable": False},
    "AI_FILTER_ELEMENT_PRESSURE_OUTPUT": {"node": "ns=2;s=Application.GVL_HMI.AI_FILTER_ELEMENT_PRESSURE_OUTPUT", "type": "REAL", "comment": "过滤系统风压反馈值(单位pa)", "writable": False},
    "AI_FILTER_ELEMENT_PRESSURE_SET_H": {"node": "ns=2;s=Application.GVL_HMI.AI_FILTER_ELEMENT_PRESSURE_SET_H", "type": "REAL", "comment": "过滤系统风压设定值", "writable": True},
    "DO_LASER_EXTERNAL_LIGHT_OUTPUT_H": {"node": "ns=2;s=Application.GVL_HMI.DO_LASER_EXTERNAL_LIGHT_OUTPUT_H", "type": "Boolean", "comment": "激光器光出使能", "writable": True},
    "RECIRCULATING_FAN_ON_H": {"node": "ns=2;s=Application.GVL_HMI.RECIRCULATING_FAN_ON_H", "type": "Boolean", "comment": "循环风机打开", "writable": True},
    "PRINT_SHIELD_TEST": {"node": "ns=2;s=Application.GVL_HMI.PRINT_SHIELD_TEST", "type": "Boolean", "comment": "屏蔽打印测试", "writable": True},
    # 工厂设置（6 个）
    "CNC_XygapVel": {"node": "ns=2;s=Application.GVL_HMI.CNC_XygapVel", "type": "REAL", "comment": "CNC速度", "writable": False},
    "CNC_XygapACC": {"node": "ns=2;s=Application.GVL_HMI.CNC_XygapACC", "type": "REAL", "comment": "CNC加速度", "writable": False},
    "CNC_XygapDEC": {"node": "ns=2;s=Application.GVL_HMI.CNC_XygapDEC", "type": "REAL", "comment": "CNC减速度", "writable": False},
    "CNCfDefaultVel": {"node": "ns=2;s=Application.GVL_HMI.CNCfDefaultVel", "type": "REAL", "comment": "CNC默认速度", "writable": False},
    "CNCfDefaultAccel": {"node": "ns=2;s=Application.GVL_HMI.CNCfDefaultAccel", "type": "REAL", "comment": "CNC默认加速度", "writable": False},
    "CNCfDefaultDecel": {"node": "ns=2;s=Application.GVL_HMI.CNCfDefaultDecel", "type": "REAL", "comment": "CNC默认减速度", "writable": False},
}

GROUPED_VARIABLES = {
    "CNC控制": [
        "CNCStatus", "CNCSourceNo", "CNCwm", "CNCiLastSwitch",
        "CNC_MODE", "CNC_Manual", "CNC_Ready", "CNC_Start", "CNC_WKStop", "CNC_Read1",
        "XY_HOME", "CNC_Pause", "CNC_Stop", "CNC_Resst"
    ],
    "X轴": [
        "X_PosNow", "X_MoveRela_done", "X_MoveAbs_done",
        "X_POWER", "X_REST", "X_Stop", "X_JogNeg", "X_Jogrev", "X_MoveAbs", "X_HOME",
        "X_MoveVel", "X_MoveABSPos", "X_MoveRelaDist", "X_Moveacc", "X_Movedec", "X_Stopdec"
    ],
    "Y轴": [
        "Y_PosNow", "Y_MoveRela_done", "Y_MoveAbs_done",
        "Y_POWER", "Y_REST", "Y_Stop", "Y_JogNeg", "Y_Jogrev", "Y_MoveAbs", "Y_HOME",
        "Y_MoveVel", "Y_MoveABSPos", "Y_MoveRelaDist", "Y_Moveacc", "Y_Movedec", "Y_Stopdec"
    ],
    "A轴": [
        "A_PosNow", "A_MoveRela_done", "A_MoveAbs_done",
        "A_POWER", "A_REST", "A_Stop", "A_JogNeg", "A_Jogrev", "A_MoveAbs", "A_HOME",
        "A_MoveVel", "A_MoveABSPos", "A_MoveRelaDist", "A_Moveacc", "A_Movedec", "A_Stopdec"
    ],
    "B轴": [
        "B_PosNow", "B_MoveRela_done", "B_MoveAbs_done",
        "B_POWER", "B_REST", "B_Stop", "B_Jogrev", "B_JogNeg", "B_MoveAbs", "B_HOME",
        "B_MoveVel", "B_MoveABSPos", "B_MoveRelaDist", "B_Moveacc", "B_Movedec", "B_Stopdec"
    ],
    "Z轴": [
        "Z_PosNow", "Z_MoveRela_done", "Z_MoveAbs_done",
        "Z_POWER", "Z_REST", "Z_Stop", "Z_Jogrev", "Z_JogNeg", "Z_MoveAbs", "Z_HOME",
        "Z_MoveVel", "Z_MoveABSPos", "Z_Moveacc", "Z_Movedec", "Z_Stopdec", "Z_MoveRelaDist"
    ],
    "密封测试": [
        "CHAMBER_O2_OK_SEAL", "AI_HP_O2_CONTENT_OUTPUT_SEAL", "AI_LP_O2_CONTENT_OUTPUT_SEAL",
        "AI_CHAMBER_PRESSURE_OUTPUT_SEAL", "AI_CHAMBER_O2_CONTENT_OUTPUT_SEAL", "SOLENOID_VALVE_CONTROL_MODE",
        "MANUAL_TEST_MODE", "EXHAUST_VALVE_1_ENABLE_H_1", "EXHAUST_VALVE_2_ENABLE_H_1",
        "FAST_FLUX_VALVE_ENBLE_H_1", "SLOW_FLUX_VALVE_ENBLE_H_1", "AUTO_TEST_MODE", "START_AIR_CLEAN"
    ],
    "激光和风机": [
        "CHAMBER_O2_OK_LASER", "AI_HP_O2_CONTENT_OUTPUT_LASER", "AI_LP_O2_CONTENT_OUTPUT_LASER",
        "AI_CHAMBER_O2_CONTENT_OUTPUT_LASER", "AI_CHAMBER_PRESSURE_OUTPUT_LASER",
        "AI_FILTER_ELEMENT_PRESSURE_OUTPUT", "DO_LASER_EXTERNAL_LIGHT_OUTPUT_H", "RECIRCULATING_FAN_ON_H",
        "PRINT_SHIELD_TEST", "AI_FILTER_ELEMENT_PRESSURE_SET_H"
    ],
    "工厂设置": [
        "CNC_XygapVel", "CNC_XygapACC", "CNC_XygapDEC",
        "CNCfDefaultVel", "CNCfDefaultAccel", "CNCfDefaultDecel"
    ]
}