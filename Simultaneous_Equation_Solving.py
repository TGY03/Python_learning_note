import streamlit as st
from sympy.solvers import solve
from sympy import symbols
from sympy.core import sympify

x, y, z = symbols('x y z')

# st.header('聯立方程式求解')
st.markdown('# 聯立方程式求解')

expr1 = st.text_area('請輸入聯立方程式：', 'x+y=8\nx-y=2\n2*y+z=13')

if st.button('求解'):
    equations_clean=[]
    equations = expr1.split('\n')
    if len(equations)>0:
        for i in range(len(equations)):
            if equations[i] == '':
                continue
            arr = equations[i].split('=')
            if len(arr) == 2:
                equations[i] = arr[0] + '-(' + arr[1] + ')'
            equations_clean.append(equations[i])
        print(equations_clean)
    
    ans = solve(equations_clean)
    print(ans)
    st.write(f'結果:{ans}')
