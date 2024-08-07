
input_file = 'E:\\data\\LCCC-base-split\\LCCC-base_valid.json'

import json

input_file = 'E:\\data\\LCCC-base-split\\LCCC-base_valid.json'

# 读取输入数据
with open(input_file, 'r', encoding='utf-8') as f:
    input_data = json.load(f)

# 转换为Alpaca数据格式
alpaca_data = []
for conversation in input_data:
    for i in range(1, len(conversation)):
        # 构建上下文对话
        context = []
        for j in range(i):
            role = "角色A" if j % 2 == 0 else "角色B"
            context.append(f"{role}: {conversation[j]}")
        input_text = "\n".join(context)
        
        # 当前输出
        role = "角色A" if i % 2 == 0 else "角色B"
        output_text = f"{role}: {conversation[i]}"
        
        entry = {
            "instruction": "继续对话",
            "input": input_text,
            "output": output_text,
            "system": "",  # 保持为空
            "history": []  # 保持为空
        }
        alpaca_data.append(entry)

# 输出数据
output_file = 'alpaca_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(alpaca_data, f, ensure_ascii=False, indent=2)

print(f"数据已成功转换并保存到 {output_file}")


