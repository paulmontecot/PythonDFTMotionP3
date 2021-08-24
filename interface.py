import streamlit as st
import pandas as pd
import base64
import MathUtilities
import getFeaturesWindows
import emoji

st.set_page_config(
    # Can be "centered" or "wide". In the future also "dashboard", etc.
    layout="wide",
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    # String or None. Strings get appended with "• Streamlit".
    page_title="Features Extraction Interface \U0001F58A",
    page_icon="Features Extraction Interface",  # String, anything supported by st.image, or None.
)

#app

st.title("Features Extraction Interface \U0001F58A")
st.markdown("**Fill the differents items then click on generate**")
st.subheader('User ID')
user_id = st.text_input("")
st.sidebar.subheader("Data type")
datatype = st.sidebar.selectbox("",('accX','accY','accZ'))
st.subheader('Please Upload Data \U00002B07')
uploaded_file = st.file_uploader("")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    dataframe.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']
    st.write(dataframe)
    Data = dataframe[datatype]
    dataframe['norme'] = MathUtilities.norme(dataframe)
    norme = dataframe['norme']
    Xfinaldata, Yfinaldata = getFeaturesWindows.getFeaturesWindows(Data, 1)
    dffinaldata = pd.DataFrame(Xfinaldata)
    #dffinaldata.columns = ['DC', 'energy', 'entropyDFT', 'Deviation','contact','pressure']
    dffinaldata.columns = ['DC', 'energy', 'entropyDFT', 'Deviation']
else:
    dffinaldata = pd.DataFrame()

st.subheader('BHK Score')
BHK_score = st.text_input(" ")
st.subheader('Handedness')
handed = st.selectbox(
'',
('Left Handed', 'Right Handed'))
st.subheader('Level of constraint')
constraint = st.selectbox("",('1','2','3','4','5','6','7','8','9','10'))
st.subheader('Constraint type')
finger = st.checkbox("finger")
wrist = st.checkbox("wrist")
elbow = st.checkbox("elbow")
shoulder = st.checkbox("shoulder")
st.subheader('Frame Resolution')
int_val = st.number_input('', min_value=1, max_value=10, value=5, step=1)

def get_dataBHK():
    return[]
def get_dataglobal():
    return[]
mean = dffinaldata.mean(axis=1)
median = dffinaldata.median(axis=1)
standard_deviation = dffinaldata.std(axis=1)
variance = dffinaldata.var(axis=1)
df_BHK = pd.DataFrame()
df_Global = pd.DataFrame()

if finger == False:
    finger = "\U0001F534"
elif finger == True:
    finger = "\U0001F7E2"

if wrist == False:
    wrist = "\U0001F534"
elif wrist == True:
    wirst = "\U0001F7E2"

if elbow == False:
    elbow = "\U0001F534"
elif elbow == True:
    elbow = "\U0001F7E2"

if shoulder == False:
    shoulder = "\U0001F534"
elif shoulder == True:
    shoulder = "\U0001F7E2"

if st.button('GENERATE'):
    dataBHK = {"BHK score": BHK_score, "handedness": handed, "Constraint": constraint,"finger": finger, "wrist":wrist,"elbow":elbow,"shoulder":shoulder}
    dataglobal = {"Mean": mean, "Median": median, "standard deviation": standard_deviation, "variance": variance}
    df_BHK = pd.DataFrame.from_records([dataBHK])
    df_Global = pd.DataFrame.from_records(dataglobal)
    df_Frames = dffinaldata

    st.dataframe(df_BHK)
    st.dataframe(df_Global)
    st.dataframe(df_Frames)



    df_final = pd.concat([df_BHK, df_Global, df_Frames], axis=0)

if st.button('Download'):
    csv = dffinaldata.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    st.markdown('### **⬇️ Download output CSV File **')
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as ".csv")'
    st.markdown(href, unsafe_allow_html=True)
