import subprocess
from langchain_ollama import OllamaLLM
import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="SMARDOS - Ruang Konsultasi", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded" # Memaksa sidebar terbuka saat pertama kali load
)

# --- 2. ADVANCED CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;800&display=swap');
    
    .stApp { background-color: #f8fafc; }
    html, body, [class*="st-"] { font-family: 'Nunito', sans-serif; }

    /* Memastikan Sidebar terlihat jelas */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Styling Tombol Navigasi di Sidebar */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        text-align: left;
        padding: 10px 15px;
    }

    /* Chat Styling */
    [data-testid="stChatMessage"] {
        border-radius: 15px;
        padding: 1.2rem;
        margin-bottom: 0.8rem;
    }

    /* Header Styling */
    .main-header {
        background: white;
        padding: 1rem 2rem;
        border-bottom: 2px solid #2563eb;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIC FUNCTIONS ---
@st.cache_data(ttl=300)
def get_available_models():
    try:
        result = subprocess.run(["ollama", "list"], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.strip().split("\n")
        return [line.split()[0] for line in lines[1:]]
    except: return []

def generate_smardos_response(user_input, model_name):
    llm = OllamaLLM(model=model_name, temperature=0.7)
    system_instructions = (
        "Kamu adalah SMARDOS (Smart Asisten Dosen). "
        "Gunakan Bahasa Indonesia yang sopan dan akademis."
    )
    full_prompt = f"System: {system_instructions}\nUser: {user_input}"
    return llm.invoke(full_prompt)

# --- 4. SIDEBAR (NAVIGASI & SETTING) ---
with st.sidebar:
    # Logo & Nama
    st.markdown("<h1 style='color: #1e3a8a; font-size: 24px; font-weight: 800;'>🎓 SMARDOS</h1>", unsafe_allow_html=True)
    st.caption("v2.5 - Your Smart Academic Partner")
    
    st.markdown("---")
    
    # Menu Navigasi dengan Icon
    st.subheader("📌 Navigasi")
    if st.button("🏠 Kembali ke Beranda"):
        # st.switch_page("home.py") # Pastikan file home.py ada
        st.info("Fitur pindah halaman aktif jika file home.py tersedia.")
        
    st.markdown("---")
    
    # Pengaturan Model
    st.subheader("⚙️ Panel Kontrol AI")
    available_models = get_available_models()
    if available_models:
        selected_model = st.selectbox("Pilih Model Ollama:", available_models)
        st.success(f"Model: **{selected_model}** aktif.")
    else:
        selected_model = None
        st.error("⚠️ Model tidak ditemukan. Pastikan Ollama menyala.")

    st.markdown("---")
    
    # Aksi Cepat
    if st.button("🗑️ Bersihkan Riwayat Chat"):
        st.session_state.messages = []
        st.rerun()

# --- 5. MAIN CONTENT AREA ---
# Header
st.markdown(f"""
    <div class="main-header">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 24px;">💬</span>
            <h3 style="margin: 0; color: #1e3a8a;">Konsultasi Akademik</h3>
        </div>
        <div style="background: #eff6ff; padding: 5px 15px; border-radius: 20px; color: #2563eb; font-weight: bold; font-size: 12px;">
            STATUS: ONLINE
        </div>
    </div>
    """, unsafe_allow_html=True)

# Inisialisasi Chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya **SMARDOS**. Gunakan sidebar di sebelah kiri untuk mengatur model AI atau kembali ke menu utama. Apa yang ingin Anda diskusikan hari ini?"}
    ]

# Tampilkan Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🎓" if message["role"]=="assistant" else "👤"):
        st.markdown(message["content"])

# Input Chat
if selected_model:
    if prompt := st.chat_input("Tanyakan sesuatu pada SMARDOS..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🎓"):
            with st.spinner("Sedang berpikir..."):
                try:
                    response = generate_smardos_response(prompt, selected_model)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Terjadi kesalahan teknis: {str(e)}")
else:
    st.warning("Silakan jalankan Ollama dan pilih model di sidebar untuk mulai bertanya.")

# Footer
st.markdown("<div style='text-align: center; color: #94a3b8; font-size: 12px; margin-top: 50px;'>SMARDOS Local Intelligence</div>", unsafe_allow_html=True)