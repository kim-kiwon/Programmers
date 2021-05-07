new_id = "abcdefghijklmn.p"

def solution(new_id):
    new_id = new_id.lower()
    new_id = list(new_id)
    can = ['-', '_', '.']
    for i in range(len(new_id)):
        if new_id[i].isdigit(): continue
        if new_id[i].isalpha(): continue
        if new_id[i] in can:
            continue
        else:
            new_id[i] = " "
    temp = ""
    for i in new_id:
        if i != ' ':
            temp += i
    new_id = temp
    new_id.replace(" ", "")

    new_id = list(new_id)
    flag = 0
    for i in range(len(new_id)):
        if new_id[i] != '.': flag = 0; continue;
        if flag == 0 and new_id[i] == '.': flag = 1; continue;
        if flag == 1 and new_id[i] == '.': new_id[i] = " "
    temp = ""
    for i in new_id:
        if i != ' ':
            temp += i
    new_id = temp

    new_id = list(new_id)
    if len(new_id) >= 1 and new_id[0] == '.': new_id = new_id[1:]
    if len(new_id) >= 2 and new_id[-1] == '.': new_id = new_id[:-1]
    new_id = "".join(new_id)

    if new_id == "": new_id = "a"

    if len(new_id) >= 16:
        new_id = list(new_id)
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:-1]
        new_id = "".join(new_id)

    while len(new_id) < 3:
        val = new_id[-1]
        new_id += val
    return new_id

print(solution(new_id))