import time
from typing import Dict, Any, Tuple

from opcua import Client
from opcua.ua import UaStatusCodeError, Variant, VariantType

from data.plc_variables import PLC_URL, USERNAME, PASSWORD, VARIABLES


class OPCUAHandler:
    def __init__(self):
        self.client = None
        self.nodes: Dict[str, Any] = {}
        self.connected = False
        self.last_error = ""

    def connect(self) -> bool:
        self.disconnect()
        self.client = Client(PLC_URL)
        self.client.set_user(USERNAME)
        self.client.set_password(PASSWORD)
        self.client.connect_timeout = 5

        for _ in range(3):
            try:
                self.client.connect()
                self.nodes = {
                    var_name: self.client.get_node(info["node"])
                    for var_name, info in VARIABLES.items()
                }
                self.connected = True
                self.last_error = ""
                return True
            except Exception as exc:
                self.last_error = str(exc)
                time.sleep(1)

        self.connected = False
        return False

    def read_values(self) -> Dict[str, Any]:
        if not self.connected:
            return {}

        values: Dict[str, Any] = {}
        try:
            for var_name, node in self.nodes.items():
                try:
                    values[var_name] = node.get_value()
                except Exception:
                    values[var_name] = None
            return values
        except Exception as exc:
            self.last_error = str(exc)
            self.connected = False
            return {}

    def write_value(self, var_name: str, value: Any) -> Tuple[bool, str]:
        if var_name not in self.nodes:
            return False, f"变量不存在: {var_name}"

        node = self.nodes[var_name]
        var_type = VARIABLES[var_name]["type"]

        try:
            if var_type == "Boolean":
                node.set_value(Variant(bool(value), VariantType.Boolean))
            elif var_type in ["Float", "REAL"]:
                node.set_value(Variant(float(value), VariantType.Float))
            elif var_type == "Int16":
                node.set_value(Variant(int(value), VariantType.Int16))
            elif var_type == "Int32":
                node.set_value(Variant(int(value), VariantType.Int32))
            elif var_type == "UInt16":
                node.set_value(Variant(int(value), VariantType.UInt16))
            else:
                node.set_value(value)
            return True, f"{var_name} 已设置为 {value}"
        except UaStatusCodeError as exc:
            if "BadWriteNotSupported" in str(exc):
                try:
                    current = node.get_value()
                    if var_type in ["Float", "REAL"]:
                        ok = abs(float(current) - float(value)) < 1e-5
                    else:
                        ok = current == value
                    if ok:
                        return True, f"{var_name} 写入已生效（服务端返回不支持写入）"
                    return False, f"写入失败，期望: {value}，实际: {current}"
                except Exception as verify_exc:
                    return False, f"写入失败，且无法验证结果: {verify_exc}"
            return False, f"写入失败: {exc}"
        except Exception as exc:
            return False, f"写入错误: {exc}"

    def disconnect(self) -> None:
        if self.client is not None:
            try:
                self.client.disconnect()
            except Exception:
                pass
        self.client = None
        self.nodes = {}
        self.connected = False
