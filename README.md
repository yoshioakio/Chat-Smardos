# 🎓 SMARDOS - Smart Asisten Dosen 🤖✨

**SMARDOS (Smart Asisten Dosen)** adalah platform konsultasi akademik berbasis AI yang dirancang khusus untuk mahasiswa dan peneliti. Berfungsi sebagai **asisten digital 24/7**, SMARDOS membantu membedah materi perkuliahan, teori ilmiah, hingga metodologi penelitian dengan dukungan referensi jurnal yang tervalidasi.

![home.png](home.png)

---

## 🚀 Fitur Unggulan

- **⚡ Academic-Only Guardrails:** AI telah diprogram untuk hanya merespons topik terkait mata kuliah dan dunia akademik.
- **📖 Jurnalized References:** Setiap jawaban teknis dilengkapi dengan referensi jurnal ilmiah asli dan tautan valid (DOI/Google Scholar).
- **🎯 Struktur Jawaban Sistematis:** Penjelasan disusun secara metodologis (Definisi -> Pembahasan -> Implementasi -> Referensi).
- **💻 Local Privacy:** Menggunakan teknologi _Ollama_ untuk memastikan data percakapan tetap aman di lingkungan lokal.

![chat.png](chat.png)

## 🛠️ Spesifikasi Sistem & Batasan

Untuk menjaga kualitas bimbingan, SMARDOS memiliki batasan operasional:

- **Topik Khusus:** Hanya menjawab seputar mata kuliah (Teknik, Sosial, Hukum, dll).
- **Anti-Halusinasi:** Jika topik tidak ditemukan di database akademik, AI akan menyarankan pencarian manual ke portal jurnal resmi.
- **Output Formal:** Menggunakan gaya bahasa asisten dosen yang sopan dan edukatif.

## 📦 Cara Instalasi Lokal

1.  Pastikan [Ollama](https://ollama.ai/) sudah terinstal dan berjalan.
2.  Clone repositori ini : `https://github.com/yoshioakio/Chat-Smardos.git`
3.  Instal dependensi: `pip install -r requirements.txt`
4.  Jalankan aplikasi: `streamlit run home.py`

---

## 🔗 Akses Publik

Jelajahi ekosistem SMARDOS secara langsung melalui tautan berikut:
👉 [**smardos.streamlit.app**](https://smardos.streamlit.app/)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://smardos.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
