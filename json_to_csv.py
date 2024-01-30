import json
import csv
import os

def json_to_csv(json_file, csv_file_edge, csv_file_node):
    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_edge), exist_ok=True)
    os.makedirs(os.path.dirname(csv_file_node), exist_ok=True)

    # 解析 JSON 数据
    with open(json_file, 'r') as file:
        tot_tree_json = json.load(file)

    # CSV 文件的标题行
    edge_headers = ['Source', 'Target', 'last_formula', 'operator']
    node_headers = ['id', 'node_id', 'step', 'value']

    # 创建 CSV 边文件
    with open(csv_file_edge, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(edge_headers)
        # 写入每行数据
        for node_content, state in tot_tree_json['nodes'].items():
            if state['step'] == 0:
                row = ['null', node_content, '', '']
            else:
                row = [state['parent'], node_content, state['last_formula'], state['operator']]
            writer.writerow(row)

    # 创建 CSV 点文件
    with open(csv_file_node, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(node_headers)
        # 写入每行数据
        for node_content, state in tot_tree_json['nodes'].items():
            row = [node_content, state['node_id'], state['step'], state['value']]
            writer.writerow(row)

def get_all_file_names(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names

if __name__ == '__main__':
    # 将 JSON 转换为 CSV
    JSON_files = get_all_file_names('./CJL_Logs/Json')
    for file in JSON_files:
        name = ''.join(file.split('.')[:-1])
        json_file = f'./CJL_Logs/Json/{file}'
        csv_file_edge = f'./CJL_Logs/csv/{name}/edge.csv'
        csv_file_node = f'./CJL_Logs/csv/{name}/node.csv'
        json_to_csv(json_file, csv_file_edge, csv_file_node)