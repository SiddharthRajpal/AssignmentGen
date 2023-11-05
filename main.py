from fpdf import FPDF
import streamlit as st
import openai
openai.api_key = st.secrets["DB_API"]

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(model=model,messages=messages,temperature=0.1,)
    return response.choices[0].message["content"]

response = ""
def generate():
    print(f'make a assignment on {topic} for class {grade} {board} of {questions} {length} length questions that is {level}, do not give any foreword, {special}')
    return get_completion(prompt=f'Make a assignment on {topic} for class {grade} {board} of {questions} {length} length questions that is {level} in difficulty, do not give any foreword, {special}')

#Layout
st.title("Assignment Generator")
board = st.selectbox("Your Board",("ICSE","CBSE","IGSCE","ISC"))
grade = st.selectbox("Your Class",("1",'2','3','4','5','6','7','8','9','10','11','12'))
length = st.selectbox("Question Length",("Short","Long"))
topic = st.text_input("Your Topic")
questions = st.number_input("Number of Questions", min_value=1,max_value=10)
special = st.text_input("Special Requirements")
level = st.selectbox("Level",("Very Easy","Easy","Moderate","Hard"))
logo = st.file_uploader("Upload Institution Logo",type=['png','jpg'])
button = st.button("Generate", on_click= None)

if(button==True):
    with st.spinner('Generating...'):
        response = generate()
        pdf = FPDF(unit="mm",orientation="portrait")
        st.markdown(f"""
<style>
#output{{
    background-color: white; 
    border-radius: 8px; 
    color: rgb(14, 17, 23);
    padding: 10px;
    margin-bottom: 12px;
}}
</style>
<div id="output">
<p>
{response}
</p>
</div>""",unsafe_allow_html = True)

        pdf.set_top_margin(40)
        pdf.add_page()

        # pdf.add_font("roboto",style='',fname="fonts/WorkSans-VariableFont_wght.ttf",uni=True)
        pdf.set_font('helvetica','',14)
        w = 50
        if logo != None:
            pdf.image(logo,x=105-(w/2),y=10,w=w)

        pdf.write(10, response)
        pdf.output('testPdf.pdf')
        with open('testPdf.pdf', 'rb') as f:
            st.download_button('Download PDF', f, file_name=f'Class{grade}Assignment{topic}.pdf')
        
