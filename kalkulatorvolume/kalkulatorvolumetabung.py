import streamlit as st
import math

def kalkulator_volume_tabung_streamlit():
    """
    Kalkulator volume tabung dengan metode pendekatan discovery learning menggunakan Streamlit.
    Output angka dibulatkan menjadi bilangan bulat.
    """
    st.title("Kalkulator Volume Tabung (Discovery Learning)")
    st.write("---")

    st.write("Hai! Mari kita hitung volume tabung bersama-sama.")
    st.write("Sebelum itu, tahukah kamu apa itu tabung?")
    st.info("💡 Bayangkan sebuah kaleng susu atau pipa. Itu adalah contoh **tabung**.")
    st.write("Tabung memiliki dua bagian utama: **alas** (lingkaran) dan **tinggi**.")

    st.write("---")
    st.subheader("Langkah 1: Memahami Luas Alas")
    st.write("Nah, mari kita pikirkan tentang alasnya.")
    st.write("Alas tabung berbentuk lingkaran. Bagaimana kita menghitung **luas sebuah lingkaran**?")
    st.write("Ingat rumus luas lingkaran? Itu melibatkan '**pi**' (sekitar 3.14) dan **jari-jari**.")
    st.markdown("Luas Lingkaran = $\\pi \\times \\text{jari-jari} \\times \\text{jari-jari}$")
    st.markdown("Atau, Luas Lingkaran = $\\pi r^2$")

    st.write("---")
    st.subheader("Langkah 2: Masukkan Nilai Tabung")

    # Input Jari-jari - diatur untuk menerima bilangan bulat
    jari_jari = st.number_input("Masukkan panjang **jari-jari** alas tabung (misal: cm)", min_value=0, value=1, step=1, format="%d")
    if jari_jari <= 0 and st.session_state.get('jari_jari_set', False):
        st.warning("Jari-jari harus lebih besar dari nol.")
        return

    # Input Tinggi - diatur untuk menerima bilangan bulat
    tinggi = st.number_input("Masukkan **tinggi** tabung (dalam satuan yang sama dengan jari-jari)", min_value=0, value=1, step=1, format="%d")
    if tinggi <= 0 and st.session_state.get('tinggi_set', False):
        st.warning("Tinggi harus lebih besar dari nol.")
        return

    # Perbarui session state setelah input valid
    if jari_jari > 0:
        st.session_state['jari_jari_set'] = True
    if tinggi > 0:
        st.session_state['tinggi_set'] = True

    st.write(f"Oke, kita punya **jari-jari**: `{jari_jari}` dan **tinggi**: `{tinggi}`")

    st.write("---")
    st.subheader("Langkah 3: Perhitungan")

    # Tombol hitung akan memicu perhitungan hanya jika semua input valid
    if jari_jari > 0 and tinggi > 0:
        if st.button("Hitung Volume!"):
            # Menghitung luas alas
            st.write("### Menghitung Luas Alas Tabung")
            luas_alas = math.pi * (jari_jari ** 2)
            st.write(f"Menggunakan rumus **Luas Lingkaran** = $\\pi \\times r^2$")
            # Output luas alas dibulatkan ke bilangan bulat terdekat
            st.success(f"Luas Alas = `{math.pi:.4f}` * `{jari_jari}`^2 = `{round(luas_alas)}` satuan persegi.")

            st.write("### Menghitung Volume Tabung")
            st.write("Bayangkan luas alas itu seperti '**tumpukan**' koin.")
            st.write("Jika kita menumpuk '**luas alas**' itu setinggi '**tinggi**' tabung, kita akan mendapatkan volumenya!")
            st.markdown("Jadi, **Volume Tabung** = **Luas Alas** $\\times$ **Tinggi**")

            volume = luas_alas * tinggi
            # Output volume dibulatkan ke bilangan bulat terdekat
            st.success(f"Volume Tabung = `{round(luas_alas)}` * `{tinggi}` = `{round(volume)}` satuan kubik.")

            st.balloons()
            st.write("---")
            st.subheader("Selamat!")
            st.write("Anda telah berhasil menghitung volume tabung.")
            st.write(f"Dengan jari-jari **{jari_jari}** dan tinggi **{tinggi}**,")
            # Output volume akhir dibulatkan ke bilangan bulat terdekat
            st.success(f"Volume tabung adalah: **{round(volume)}** satuan kubik.")
    else:
        st.warning("Silakan masukkan nilai jari-jari dan tinggi yang valid (lebih dari nol) untuk memulai perhitungan.")


if __name__ == "__main__":
    # Inisialisasi session state jika belum ada
    if 'jari_jari_set' not in st.session_state:
        st.session_state['jari_jari_set'] = False
    if 'tinggi_set' not in st.session_state:
        st.session_state['tinggi_set'] = False

    kalkulator_volume_tabung_streamlit()
