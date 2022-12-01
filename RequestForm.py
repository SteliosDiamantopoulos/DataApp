import streamlit as st
import pandas as pd
from datetime import datetime as dt
import os
from io import StringIO 
import shutil
departments =['Mysteris','SupplyChain','Field Engineerer','Data Managment','HR','Callibration','other Choice']
list_registered=['Stelios','Ariff']
supported_files = ['xlsx','pdf','png']

def new_tytle (projectNO,publisher,departments,date,ftype):
    new_tytle = (projectNO + '_' + publisher + '_' + departments + '_' + date.strftime("%d/%m/%Y") + '.' + ftype)
    return new_tytle

def projectNO_check(projectNO):
    return(projectNO.isnumeric())

def publisher_check(name):
    
    if name in list_registered :
        return (True)
    else :
        st.warning('Unkown publisher name', icon="⚠️")
        return (False)

def save_uploadedfile(uploadedfile,projectNO,publisher,departments,date,ftype):
    new_name = new_tytle(projectNO,publisher,departments,date,ftype)
    with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to tempDir".format(uploadedfile.name))
    
def department_check(department):
    return(True)
    # if department == 'other Choice':
    #     flag=False
    #     newdepartment = st.text_input('newDepartment',flag)    
    #     departments.append(newdepartment)
    #     return (False)
    # else:
    #     return(True)

def fyleType_check(ftype):
    if ftype in supported_files :
        return (True)
    else :
        st.warning('This extansion is not supported', icon="⚠️")
        return (False)


def form_check(projectNO,publisher,department,date,ftype):
    check = False
    if projectNO_check(projectNO) & publisher_check(publisher) & department_check(department) &date_check(date) % fyleType_check(ftype) :
        check = True
    return(check)

def date_check(date):
    if date < dt.today().date():
        st.warning('Wrong Date Entry', icon="⚠️")
        return (False)
    else :
        return(True)

with st.form('Sharing Form'):#,clear_on_submit=True
    st.title('Sharing Form')


    st.title('PublistInformation')

    projectNO = st.text_input('ProjectNo')
    
    publisher = st.text_input('PublisherName')

    departments = st.selectbox('Departments',departments)

    date = st.date_input('EntryDate')

    ftype = st.selectbox ('File type',supported_files)

    #st.write(date,dt.today().date())
    importance = st.selectbox('Priority',('High','Medium','Low'))

    description = st.text_input('Description')

   

    st.title('Instuctions for Renaming Shared Folders')

    #Extra file naming information 


   

    newFolderName = st.text_input('Rename Folders Before Submitting',new_tytle(projectNO,publisher,departments,date,ftype))


    submitted = st.form_submit_button("Submit")


    if submitted and form_check(projectNO,publisher,departments,date,ftype) == True:
        st.write('Submitted name : ',new_tytle(projectNO,publisher,departments,date,ftype))
    else:
        pass

    

    uploaded_file = st.file_uploader("Choose a file")
    publish = st.form_submit_button('Publish')            
    if publish :
        if uploaded_file is not None:
            st.write(uploaded_file)
            save_uploadedfile(uploaded_file,projectNO,publisher,departments,date,ftype)
            st.write(uploaded_file.name)


    a_path = "C:\\Users\\stdia\\Desktop\\StreamLit\\WebSite"
    a_folder = "memory"
    a_file = str(new_tytle(projectNO,publisher,departments,date,ftype))

    joined_path = os.path.join(a_path, a_folder, a_file)
    startPath = "C:\\Users\\stdia\\Desktop\\StreamLit\\WebSite\\tempDir\\tf16400962_win322.xlsx"
       
    os.rename(startPath,joined_path)



       



  
