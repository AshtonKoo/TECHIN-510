import streamlit as st

st.set_page_config(
    page_title="Mingxi Gu",
    page_icon="👾",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
) 

col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![](https://avatars.githubusercontent.com/u/148400739?s=400&u=a498aa94022d59d124533e733e4004e95366cc1a&v=4)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://avatars.githubusercontent.com/u/148400739?s=400&u=a498aa94022d59d124533e733e4004e95366cc1a&v=4')
with col2:
    st.markdown(
        """
    # Mingxi Gu (He/Him)
                
    Student at [GIX](https://gix.uw.edu/)
    """
    )

st.markdown(
    """
# Education

- [University of Arizona](https://www.arizona.edu/)
- [University of Washington](https://www.washington.edu/)

# Work Experience

- [Resume](https://www.gumingxi.com/resume)

# Interesting Projects

- [Project 1](https://www.gumingxi.com/future-of-mobility-zin-content)
- [Project 2](https://www.gumingxi.com/internet-archive-content)
- [Project 3](https://www.gumingxi.com/xinshan-content)
- [Project 4](https://www.gumingxi.com/the-vera-project-content)
"""
)

st.markdown(
    """
# Pictures
""")
col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/148400739?s=400&u=a498aa94022d59d124533e733e4004e95366cc1a&v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )

col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/148400739?s=400&u=a498aa94022d59d124533e733e4004e95366cc1a&v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href=" " target="_blank">Streamlit</a ><br 'style= top:3px;'>
with < img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a ></p >
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
