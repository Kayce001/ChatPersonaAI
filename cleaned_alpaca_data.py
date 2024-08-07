import json
import re

# 读取输入数据
input_file = 'alpaca_data.json'
with open(input_file, 'r', encoding='utf-8') as f:
    alpaca_data = json.load(f)

# 移除output字段中的角色标记
for entry in alpaca_data:
    output_text = entry['output']
    # 使用正则表达式删除角色标记
    cleaned_output = re.sub(r'角色[AB]:\s*', '', output_text)
    entry['output'] = cleaned_output

# 输出数据
output_file = 'cleaned_alpaca_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(alpaca_data, f, ensure_ascii=False, indent=2)

print(f"数据已成功清理并保存到 {output_file}")
