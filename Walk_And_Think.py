'''
developer:Dev_WAV
finish time:2024.11.17
function:A new string matching algorithm
'''

def analyse_obj_str(obj_str):
    '''统计目标字符串中的单个字符及其位置
    Count individual characters in the target string and their positions'''
    position_dict={}
    for i in range(len(obj_str)):
        if obj_str[i] not in position_dict:
            position_dict[obj_str[i]]=[i]
        else:
            position_dict[obj_str[i]].append(i)
     
    return position_dict

def Walk_And_Think(sample_str,obj_str):
    '''从sample_str中寻找obj_str,返回obj_str首字符在sample_str中的索引
    Find the index of the first character of obj_str in sample_str and return it.'''
    position_dict=analyse_obj_str(obj_str)
    steplen=len(obj_str)
    cursor=0
    issame=False
    answer=[]

    while cursor<=(len(sample_str)-1):
        cursor_char=sample_str[cursor]
        
        if cursor_char in position_dict:
            # 判断目标字符串中是否存在指针字符
            for i in position_dict[cursor_char]:
                # 依次判断指针字符在目标字符串中的不同位置而产生的不同情况
                j=0     # 重置j避免上次结果最本次结果的影响
                issame=True
                for j in range(steplen):
                    # 依次判断样品字符串相应位置是否匹配每个目标字符串中的各个字符
                    if j!=i:
                    # 跳过已经判断过的情况
                        if not (0 <= (cursor+(j-i)) <= (len(sample_str)-1)):
                            issame=False
                            break
                        if obj_str[j]==sample_str[cursor+(j-i)]:
                            # 判断字符是否相等
                            pass
                        else:
                            issame=False
                            break
                    else:
                        pass
                if issame:
                    answer.append(cursor-i)
        cursor+=steplen

    return answer
