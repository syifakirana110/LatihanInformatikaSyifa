import streamlit as st

st.title("Selamat Datang di Web Informatika")
st.write(
    "ngoding seru bersama Syifa Kirana"
)
st.image ("99f90fc29f3e7b35c70820491a5bbc35.jpg")


st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
    
