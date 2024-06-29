import yaml
import os


# def read_yaml(file_path):
#     with open(file_path, "r", encoding='utf-8') as file:
#         data = yaml.safe_load(file)
#     return data


def read_yaml(file_path):
    # 获取当前脚本文件所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接 YAML 文件的路径
    yaml_file_path = os.path.join(current_dir, "..", "case_data", file_path)

    with open(yaml_file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
        return data