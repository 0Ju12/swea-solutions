for tc in range(1, 11):
    N = int(input())
    text = input()

    stack = []

    pair = { ')': '(', ']': '[', '}': '{', '>': '<'}

    result = 1

    for ch in text:
        if ch in '([{<':
            stack.append(ch)

        else:
            if not stack:
                result = 0
                break

            if stack[-1] != pair[ch]:
                result = 0
                break

            stack.pop()

    if stack:
        result = 0

    print(f"#{tc} {result}")


    #
#     T = 10
# pair = {
#     ')': '(',
#     '}': '{',
#     ']': '[',
#     '>': '<',
# }
# open_brackets = set(['(', '[', '{', '<'])
 
# for tc in range(1, T+1):
#     input()
#     brackets = input()
 
#     answer = 1
#     brackets_stack = []
#     for bracket in brackets:
#         if bracket in open_brackets:
#             brackets_stack.append(bracket)
#             continue
         
#         if pair[bracket] != brackets_stack[-1]:
#             answer = 0
#             break
 
#         brackets_stack.pop()
     
#     print(f'#{tc} {answer}')
