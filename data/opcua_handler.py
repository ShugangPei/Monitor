import time
from opcua import Client
from opcua.ua import UaStatusCodeError, Variant, VariantType
from data.plc_variables import PLC_URL, USERNAME, PASSWORD, VARIABLES

class OPCUAHandler:
    def __init__(self):
        self.client = None
        self.nodes = {}

    def connect(self):
        self.cleanup_sessions()
        self.client = Client(PLC_URL)
        self.client.set_user(USERNAME)
        self.client.set_password(PASSWORD)
        self.client.connect_timeout = 5
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.client.connect()
                for var_name, info in VARIABLES.items():
                    self.nodes[var_name] = self.client.get_node(info["node"])
                return True
            except UaStatusCodeError:
                time.sleep(1)
                if attempt == max_retries - 1:
                    return False
            except Exception:
                return False

    def cleanup_sessions(self):
        try:
            if self.client:
                self.client.disconnect()
            temp_client = Client(PLC_URL)
            temp_client.set_user(USERNAME)
            temp_client.set_password(PASSWORD)
            temp_client.connect_timeout = 5
            temp_client.connect()
            temp_client.disconnect()
        except Exception:
            pass

    def read_values(self):
        values = {}
        try:
            for var_name, node in self.nodes.items():
                try:
                    values[var_name] = node.get_value()
                except Exception:
                    values[var_name] = "N/A"
            return values
        except Exception:
            return {}

    def write_value(self, var_name, value):
        try:
            node = self.nodes[var_name]
            var_type = VARIABLES[var_name]["type"]
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
            return True, f"{var_name} 已设置为 {value}"
        except Exception as e:
            return False, f"写入失败: {e}"

    def disconnect(self):
        if self.client:
            try:
                self.client.disconnect()
                self.cleanup_sessions()
            except Exception:
                pass
            finally:
                self.client = None
                self.nodes = {}