import streamlit as st
from streamlit import session_state as ss
import base64

if 'hello' not in ss:
    ss['hello'] = False    
if 'riddle_answered' not in ss:
    ss['riddle_answered'] = False
if 'riddle_correct' not in ss:
    ss['riddle_correct'] = False
if 'button1' not in ss:
    ss['button1'] = False
if 'button2' not in ss:
    ss['button2'] = False
if 'slider' not in ss:
    ss['slider'] = False

file_ = open("hello_there.gif", "rb")
contents = file_.read()
hello_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("clapping.gif", "rb")
contents = file_.read()
clapping_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("you_lose.gif", "rb")
contents = file_.read()
you_lose_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("cat.gif", "rb")
contents = file_.read()
cat_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("laughing.gif", "rb")
contents = file_.read()
laughing_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("no.gif", "rb")
contents = file_.read()
no_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("shrug.gif", "rb")
contents = file_.read()
shrug_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("thank_you.gif", "rb")
contents = file_.read()
thank_you_url = base64.b64encode(contents).decode("utf-8")
file_.close()

def switch_hello():
    if ss.hello:
        ss.hello = False
    else:
        ss.hello = True
        
def check_riddle():
    ss.riddle_answered = True
    if ss.riddle_input == 'w' or ss.riddle_input == 'W':
        ss['riddle_correct'] = True
    else:
        ss['riddle_correct'] = False
        
def button1():
    if ss.button1:
        ss.button1 = False
    else:
        ss.button1 = True
        
def button2():
    if ss.button2:
        ss.button2 = False
    else:
        ss.button2 = True
        
def slider_switch():
    ss.slider = True
    
def slider_check():
    if ss.slider_input <= 2:
        st.markdown(
            f'<img src="data:image/gif;base64,{laughing_url}" alt="laughing gif">',
            unsafe_allow_html=True,
        )
    elif  ss.slider_input > 2 and ss.slider_input < 8:
        st.markdown(
            f'<img src="data:image/gif;base64,{shrug_url}" alt="shrug gif">',
            unsafe_allow_html=True,
        )
    elif ss.slider_input >= 8:
        st.markdown(
            f'<img src="data:image/gif;base64,{thank_you_url}" alt="thank you gif">',
            unsafe_allow_html=True,
        )

def render_main_page():        
    st.title("Welcome to streamlit!!")

    st.write('Try a few of the interactive buttons below to explore this page')

    st.write('click the hello button below.')

    st.button("Hello",on_click=switch_hello)

    if ss.hello:
        st.markdown(
            f'<img src="data:image/gif;base64,{hello_url}" alt="hello_there gif">',
            unsafe_allow_html=True,
        )

    st.title('Here is a riddle for you . . .')
    st.text_input('What\'s at the end of a rainbow?', key='riddle_input' , on_change=check_riddle)

    if ss.riddle_answered and ss.riddle_correct:
        st.write("That is correct! Good job.")
        st.markdown(
            f'<img src="data:image/gif;base64,{clapping_url}" alt="clapping gif">',
            unsafe_allow_html=True,
        )

    elif ss.riddle_answered and not ss.riddle_correct:
        st.write("Wrong! The answer is 'W' ;)")
        st.markdown(
            f'<img src="data:image/gif;base64,{you_lose_url}" alt="you lose gif">',
            unsafe_allow_html=True,
        )

    st.title("Here are two buttons in separate columns. Try one . . .")

    col1, col2 = st.columns(2)
    with col1:
        st.button("Mystery Button 1", on_click=button1)
        if ss.button1:
            st.write("Here is a gif of a cat . . . click the button again to make it disappear")
            st.markdown(
                f'<img src="data:image/gif;base64,{cat_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )

    with col2:
        st.button("Mystery Button 2", on_click=button2)

    st.slider("Please rate my app on a scale of 1 - 10. Be honest.", min_value=0, max_value=10, key='slider_input', on_change=slider_switch)
    if ss.slider:
        slider_check()

    st.title("The End")

def render_alt_page():
    
    st.title("This is a different Page!")
    st.write("This page is a dead end . . . click \'back\' to return.")
    st.button("BACK",on_click=button2)
    st.markdown(
            f'<img src="data:image/gif;base64,{no_url}" alt="no gif">',
            unsafe_allow_html=True,
        )
    
def main():    
    if not ss.button2:
        render_main_page()
    else:
        render_alt_page()
    
if __name__ == '__main__':
    main()
