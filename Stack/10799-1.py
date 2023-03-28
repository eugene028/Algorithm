wood = list(input())
answer = 0
st = []

for i in range(len(wood)):
    if wood[i] == '(':
        st.append('(')

    else:
        if wood[i-1] == '(':
            st.pop()
            answer += len(st)

        else:
            st.pop()
            answer += 1

print(answer)