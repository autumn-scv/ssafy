alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PW_info = 'CZWVZJWLCCFWLGJREUUFNEJ'

pw_result = ''

for i in range(len(PW_info)):
    for j in range(len(alpa)):
        if PW_info[i] == alpa[j]:
            idx = (j + 9) if j + 9 <= 25 else (j + 9 - 26)
            print(idx)
            pw_result += alpa[idx]
            break

print(pw_result)