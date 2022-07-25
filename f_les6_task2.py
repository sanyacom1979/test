import json
# функция пополнения словаря вопрос-ответ
def to_dict_q_a(numb, qw, v_an, an, dict):
    dict[numb] = {qw + " (" + ", ".join(v_an) + ")" : an}
    return dict

# функция пополнения словаря правильных ответов

def to_dict_ra(numb, an, dict):
    dict[numb] = an
    return dict

# функция записи в файл формата json
def to_json(dict, js):
    with open(js, mode = "w", encoding = "utf-8") as f_js:
        json.dump(dict, f_js, ensure_ascii = False)


# функция чтения из файла формата json
def from_json(js):
    with open(js, encoding = "utf-8") as f_js:
        dict = json.load(f_js)
    return dict


# функция подсчета результатов викторины
def vict_result(qw_dict, an_dict):
    cnt = 0
    for vq1, va in zip(qw_dict.values(), an_dict.values()):
        for vq2 in vq1.values():
            if vq2 == va:
                cnt += 1
    return cnt
