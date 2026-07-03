import streamlit as st

st.title("🎉 我的第一个 Streamlit 应用")
st.write("Hello, World! 这是 Streamlit 的魔法！")

# 加个滑块
age = st.slider("你多大？", 0, 100, 25)
st.write("你选择了:", age)

# 加个按钮
if st.button("点击我！"):
    st.balloons()