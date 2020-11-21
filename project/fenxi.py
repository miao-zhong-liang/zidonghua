import json
def get_json_value_by_key(in_json, target_key, results=[]):
    if isinstance(in_json, dict):  # 如果输入数据的格式为dict
        for key in in_json.keys():  # 循环获取key
            data = in_json[key]
            get_json_value_by_key(data, target_key, results=results)  # 回归当前key对于的value

            if key == target_key:  # 如果当前key与目标key相同就将当前key的value添加到输出列表
                results.append(data)

    elif isinstance(in_json, list) or isinstance(in_json, tuple):  # 如果输入数据格式为list或者tuple
        for data in in_json:  # 循环当前列表
            get_json_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素

    return results
 
with open('1.json','r') as f:
    data=json.load(f)
data2=data
# 调用查找
ancestors=get_json_value_by_key(data,'ancestors')
print(ancestors)
print('------------------')
a=get_json_value_by_key(data2,'bounds')
print(a)