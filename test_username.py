from selenium import webdriver
import pytest

# daftar username dan password yang akan diuji
Kunci = [
    ("khaideman99","12345"),        #username benar, password salah
    ("khaideman66","Happy123@"),    #username salah, password benar
    ("khaideman99","Happy123@")     #username benar, password benar
]

# inisialisasi driver untuk browser Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# dekorator untuk mengindikasikan bahwa fungsi ini adalah sebuah pytest
@pytest.mark.parametrize('a,b',Kunci)
def test_login(a,b):

    # membuka halaman login
    driver.get("https://demoqa.com/login")

    # mencari elemen input username dan memasukkan nilai a
    username_elem = driver.find_element("id","userName")
    username_elem.send_keys(a)

    # mencari elemen input password dan memasukkan nilai b
    password_elem = driver.find_element("id","password")
    password_elem.send_keys(b)

    # mencari elemen tombol login dan mengkliknya
    login_elem = driver.find_element("id","login")
    login_elem.click()

    # mencoba mencari pesan error jika username atau password salah
    try:
        invalidtext = driver.find_element("id","name").text
        assert invalidtext == "Invalid username or password!"

    # jika pesan error tidak ditemukan, mencari teks header halaman profil sebagai indikator login sukses
    except:
        success_text = driver.find_element("class name", "main-header").text
        assert success_text == "Profile"
        print("Sukses Login")
