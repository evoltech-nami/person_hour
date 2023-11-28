import streamlit as st
import datetime
import pandas as pd

st.set_page_config(
    page_title='システムソリューション課　工数管理',
    layout='wide',
    initial_sidebar_state='expanded')
    
today=datetime.date.today()
name_item=['','鈴木','河内','杉浦','片山','奈美']

##サイドバー##

input_name =st.sidebar.selectbox('名前',name_item)
input_date=st.sidebar.date_input("作業日",today)
st.sidebar.write('')
st.sidebar.write('売上のない業務')
input_item_1=st.sidebar.selectbox('項目',['管理','社内会議','教育・学習','進捗報告','その他(掃除等)'])
input_time_1=st.sidebar.number_input('作業時間',step=1.0)
df =pd.DataFrame({"name":[input_name],"date":[input_date.strftime('%Y/%m/%d')],'item':[input_item_1],'time':[input_time_1]})
if st.sidebar.button('入力(売上なし)',use_container_width=True):
    df.to_csv('output.csv',index=False,encoding='utf-8',mode='a',header=False)

st.sidebar.write('売上のある業務')
input_customer=st.sidebar.selectbox('お客様',['','TOKAI様','朝日電装様','アマノ様','ヤマハ様'])
input_no=st.sidebar.text_input('業務No.(見積No.)')
input_item_2=st.sidebar.selectbox('項目',['管理','設計','製造','テスト','評価業務','打ち合わせ','その他'])
input_time_2=st.sidebar.number_input('作業時間2',step=1.0)
df =pd.DataFrame({"name":[input_name],"date":[input_date.strftime('%Y/%m/%d')],'customer':[input_customer],'no':[str(input_no)],'item':[input_item_2],'time':[input_time_2]})
if st.sidebar.button('入力(売上あり)',use_container_width=True):
        df.to_csv('output2.csv',index=False,encoding='utf-8',mode='a',header=False)
##サイドバー##        
    
    

col1,col2,col3,col4= st.columns(4)
with col1:
    st.image('evoltech.png')
with col2:
    st.subheader('工数管理')
with col3:
    filter_date=st.date_input("作業日:")
with col4:
    filter_name=st.selectbox('名前:',name_item,index=name_item.index(input_name))


st.write('売上のない業務')         
df=pd.read_csv('output.csv')
if filter_name=='':
    st.dataframe(df,width=500)
else:
    st.dataframe(df[df['name']==filter_name],width=500)


st.write('売上のある業務')
df=pd.read_csv('output2.csv')
if filter_name=='':
    st.dataframe(df,width=800)
else:
    st.dataframe(df[df['name']==filter_name],width=800)
             