import streamlit as st
import pandas as pd
import numpy as np

# set title;
st.title('Deniz Pinar...')
st.subheader('welcome to my app')


# set image;
from PIL import Image
image = Image.open('x.jpg')
st.image(image,use_column_width=True)

# write text;
st.write('hey body...')
st.text('___'*100)
# write markdown;
st.markdown('this is a markdown')

# write success message;
st.success('basardin dostum!')

# write information text;
st.info('once EDA yapmalisin!!!')

# write warning message;
st.warning('burada dikkatli ol!')

# write error message;
st.error('string beklerken integer deger verdin!!!')

st.text('___'*100)
# write help text;
st.help(list)


st.text('___'*100)


# creating and displaying a df;
dict_ = {'Age':[16,18,22,26],
        'Education':['High_School','University','Master','Doctor'],
        'Skills':['python','sql','c','knime']}
df = pd.DataFrame(dict_)
st.dataframe(df)

st.text('___'*100)


# plot line chart;
chart_data = pd.DataFrame(np.random.randn(10,4),columns = ['x','y','z','t'])
st.line_chart(chart_data)

st.text('___'*100)


# plot area chart;
st.area_chart(chart_data)

st.text('___'*100)


# plot bar chart;
st.bar_chart(chart_data)

st.text('___'*100)


# plot matplotlib charts;
import matplotlib.pyplot as plt

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)
#bar_label st'de calismiyor
fig.tight_layout()

st.pyplot(fig)

st.text('___'*100)


# creating buttons;
if st.button("streamlit'te matplotlib grafigi cizilebilir mi?"):
    st.write('evet cizilebilir')
else: st.write('cevabi merak ediyorsan butona tikla')

st.text('___'*100)


# creating checkbox;
if st.checkbox('Show/Hide'):
    st.text('showing the widget')

st.text('___'*100)


# creating radio button;
status = st.radio("Select Gender: ", ('Male','Female'))
if status == 'Male':
    st.success('Male')
else: st.success('Female')


st.text('___'*100)


# creating selection box;
hobbies = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
st.write('Your hobby is: ', hobbies)


st.text('___'*100)



# creating multi selection box;
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies')


st.text('___'*100)


# creating text inputs;
name = st.text_input('Enter your name','Type here...')
if st.button('Submit'):
    result = name.title()
    st.success(result)


st.text('___'*100)


# creating slider;
level = st.slider('Select the level',1,5)
st.text('Selected: {}'.format(level))
# for slider interval;
level1 = st.slider('Select the level',1,10,(2,5))
st.text('You selected range between: {}'.format(level1))


st.text('___'*100)


# creating number input;
number = st.number_input('Enter a number')
st.text('you selected number: {}'.format(number))


st.text('___'*100)


# upload file;
file_ = st.file_uploader('choose a csv file', type='csv')
if file_ is not None:
    data = pd.read_csv(file_)
    st.write(data)
    st.success('succesfully uploaded')
else: st.markdown('Please upload a valid file!')


st.text('___'*100)


# creating color picker;
color = st.color_picker('Pick your preferred color', '#00f900')
st.write('This color is {}'.format(color))


st.text('___'*100)


# creating sidebar;
sidebar_ = st.sidebar.selectbox("hobby: ",
                     ['Dancing', 'Reading', 'Sports'])
st.write('Your hobby is: ', hobbies)


st.balloons()
# st.map(df) ile harita uzerinde nokta grafigi cizebilirsin
