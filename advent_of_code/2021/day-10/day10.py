def get_input() -> list:
    with open(r'input.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list

def partOne(chars):
    l_char = ('(','{','[','<')
    match = {'(':')', '{':'}', '[':']', '<':'>'}
    wrong = []
    scores = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    for line in chars:
        c_stack = []
        for ch in line:
            if ch in l_char:
                c_stack.append(ch)
            else:
                if len(c_stack)>0:
                    if not (match[c_stack.pop()] == ch):
                        wrong.append(ch)
                        break
    for i in scores:
        score += scores[i] * wrong.count(i)
    return score

def partTwo(chars):
    l_char = ('(','{','[','<')
    match = {'(':')', '{':'}', '[':']', '<':'>'}
    scores = {'(':1, '[':2, '{':3, '<':4}
    score_list = []
    for line in chars:
        c_stack=[]
        for ch in line:
            if ch in l_char:
                c_stack.append(ch)
            else:
                if len(c_stack)>0:
                    if not (match[c_stack.pop()] == ch):
                        c_stack=[]
                        break
        score = 0
        for i in reversed(c_stack):
            score = (score * 5) + scores[i]
        if score > 0:
            score_list.append(score)
    score_list = sorted(score_list)
    return score_list[int(len(score_list)/2)]

def main():
    dims = get_input()
    print(f"The answer to part 1 is {partOne(dims)}")
    print(f"The answer to part 2 is {partTwo(dims)}")

if __name__ == '__main__':
    main()