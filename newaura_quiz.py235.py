import streamlit as st
st.title("whats your aesthetic?")
st.write("a mini vibe quiz") 
st.write("made by [your avishi]") 

st.write("---") 

answer = st.radio( 
    "which city are you?",
    [ "newyork","london","paris","mumbai","bangalore","amsterdam"]
)
st.write("you picked:", answer)

st.write("---")

answer2 = st.radio(" what is your style?",
                   ["boho", "minimalist", "old money", "street wear", "modest but classy", "whimsical", "gothic", "cottagecore", "90s"]

)
st.write("you picked:", answer2)

st.write("---")

answer3 =st.radio ("who's style do you resonate with the most?",
                   ["hailey biber (very newyork typeshi)",
                     "komal pandey (very desi with a twist)",
                     "kendal jenner(very street style)",
                     "gigi hadid(very classy and chic)" ,
                     "sabrina carpenter(very whimisicaland cute)",
                     "emma chamberlain(very 90s and vintage vibes)",
                     "taylor swift(very old money and cottagecore vibes)",
                     "aishwarya rai(very classy but desi 90s y2k vibes)"
                     ]
                    )

st.write("you picked:", answer3)

st.write("---")

answer4 = st.radio("what do you think you resonate with the most?",
                   ["clean girl(productive,ambitious,organised but fun)",
                    "girlblogger(lipgloss is a must and loves watching old barbie movies)",
                    "femme fatale(manchild is the first song on her playlist,conquers effortlessly with her strength)", 
                     "it girl (ignores drama has her own thing and loves independence)",
                     "messy girl (embraces imperfection but very sweet and fun)"
                     ])

st.write("you picked:", answer4)

st.write("---")

answer5= st.radio("which vibe do you give off the most?(the vibe does not depend upon your birthday month so you can be anyone of these)",
                  ["october girl (loves fall, pumpkin spice lattes and cozy sweatwears and coffee ,brown and furr vibes)",
                   " july girl(love summer, beach, sun , water, bikinis and fun vives)",
                   "august girl (love rain and sun at the same time, loves  cozy and rainy vibes, loves to read books and watch netflix)",
                   "april girl(loves spring, flowers and loves pastel colours and soft vibes)",
                   "december girl(loves winter,snow ,love watching christmas and 90s movies, loves cozy wives and warm drinks)",
                   "jan,feb girl(loves winter , studious vibes,loves to read and is a introvert but loves to be around friends and family)",
                   "september girl(love friends and loves to party and have fun loves to host parties and is a extrovert , and lowkey enjoys drama and gossip)"
                   ])


st.write("you pickes:",answer5)

points ={
    "The Downtown minimalist":0,
    "The Romantic Girlblogger":0,
    "The poison Ivy energy":0,
    "The rainy day artisocrat":0
}


if "newyork" in answer or "london" in answer:
    points["The Downtown minimalist"] = points["The Downtown minimalist"] + 1
if "paris" in answer or "amsterdam" in answer:
    points["The Romantic Girlblogger"] = points["The Romantic Girlblogger"] + 1
if "mumbai" in answer:
    points["The poison Ivy energy"] = points["The poison Ivy energy"] + 1
if "bangalore" in answer:
    points["The rainy day artisocrat"] = points["The rainy day artisocrat"] + 1

if "minimalist" in answer2 or "street wear" in answer2:
    points["The Downtown minimalist"] = points["The Downtown minimalist"] + 1
if "boho" in answer2 or "whimsical" in answer2:
    points["The Romantic Girlblogger"] = points["The Romantic Girlblogger"] + 1
if "gothic" in answer2 or "90s" in answer2:
    points["The poison Ivy energy"] = points["The poison Ivy energy"] + 1
if "old money" in answer2 or "modest" in answer2 or "cottagecore" in answer2:
    points["The rainy day artisocrat"] = points["The rainy day artisocrat"] + 1

if "hailey" in answer3 or "kendal" in answer3:
    points["The Downtown minimalist"] = points["The Downtown minimalist"] + 1
if "komal" in answer3 or "sabrina" in answer3:
    points["The Romantic Girlblogger"] = points["The Romantic Girlblogger"] + 1
if "emma" in answer3 or "taylor" in answer3:
    points["The poison Ivy energy"] = points["The poison Ivy energy"] + 1
if "gigi" in answer3 or "aishwarya" in answer3:
    points["The rainy day artisocrat"] = points["The rainy day artisocrat"] +1

if"clean" in answer4:
    points["The Downtown minimalist"] = points["The Downtown minimalist"] +1
if"girlblogger" in answer4:
    points["The Romantic Girlblogger"] = ["The Romantic Girlblogger"]+1
if"femme fatale" in answer4 or "it girl" in answer4:
    points["The poison Ivy energy"] = points["The poison Ivy energy"]+1
if"messy girl" in answer4:
    points["The rainy day artisocrat"] = points["The rainy day artisocrat"] +1

if"jan,feb girl" in answer5 or "december girl" in answer5:
   points["The Downtown minimalist"]= points["The Downtown minimalist"]+1
if"april girl" in answer5:
    points["The Romantic Girlblogger"] = points["The Romantic Girlblogger"] +1
if"july girl" in answer5 or  "september girl" in answer5 :
    points["The poison Ivy energy"] = points["The poison Ivy energy"]+1
if"october girl" in answer5 or  "august girl" in answer5:
    points["The rainy day artisocrat"] = points["The rainy day artisocrat"]+1

#st.write(points)

winner = max(points, key=points.get)
if st.button("reveal my aesthetic ✨"):
    st.subheader("your aesthetic is...")
    st.success(winner)

    # Pl--------------------------ay snow animation only when user clicks the reveal button
    st.snow()

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at center,
        #FFFFFF 0%,
        #FFEEF4 30%,
        #FBC4D8 55%,
        #EE7BA6 78%,
        #C9366F 100%);
}
</style>
""", unsafe_allow_html=True)






