import streamlit as st
import os
import sys
import glob

# Ajouter le dossier courant au path pour pouvoir importer main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import run_rapport_with_retry

st.set_page_config(page_title="Agent Rapport Stratégique", page_icon="📊", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🤖 Agent Multi-Agents de Rapport Stratégique</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Researcher → Analyst → Strategist → Writer</p>", unsafe_allow_html=True)

st.sidebar.title("💡 Sujets suggérés")
sujets = [
    "Le marché des AI Agents en 2026",
    "Analyse concurrentielle de Notion vs Coda",
    "Opportunités de l'IA dans le e-commerce en Europe"
]
for sujet in sujets:
    if st.sidebar.button(sujet):
        st.session_state['topic'] = sujet

st.markdown("### 📝 Quel sujet souhaitez-vous analyser ?")
topic = st.text_input("Entrez votre sujet ici :", value=st.session_state.get('topic', ''), placeholder="Ex: L'impact de l'IA sur la cybersécurité")

if st.button(" Générer le Rapport Stratégique", type="primary", use_container_width=True):
    if not topic:
        st.warning("⚠️ Veuillez entrer un sujet avant de lancer la génération.")
    else:
        with st.spinner("⏳ Les 4 agents travaillent actuellement... Cela peut prendre 1 à 3 minutes."):
            result = run_rapport_with_retry(topic, max_retries=3)
            
            if result:
                st.success("✅ Rapport généré avec succès !")
                
                # ✅ CORRECTION : Utiliser glob pour trouver les fichiers avec le chemin complet
                output_dir = "outputs"
                md_files = glob.glob(os.path.join(output_dir, "*.md"))
                
                if md_files:
                    # Trouver le fichier le plus récent avec le chemin complet
                    latest_file_path = max(md_files, key=os.path.getctime)
                    latest_file = os.path.basename(latest_file_path)
                    
                    # Lire le contenu du rapport
                    with open(latest_file_path, "r", encoding="utf-8") as f:
                        report_content = f.read()
                    
                    st.markdown("---")
                    st.subheader(" Aperçu du Rapport")
                    st.markdown(report_content)
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Bouton de téléchargement Markdown
                        with open(latest_file_path, "rb") as f:
                            st.download_button(
                                label="📥 Télécharger (.md)",
                                data=f,
                                file_name=latest_file,
                                mime="text/markdown",
                                use_container_width=True
                            )
                    
                    with col2:
                        # Bouton de téléchargement PDF
                        pdf_file = latest_file.replace('.md', '.pdf')
                        pdf_path = os.path.join(output_dir, pdf_file)
                        
                        if os.path.exists(pdf_path):
                            with open(pdf_path, "rb") as f_pdf:
                                st.download_button(
                                    label="📥 Télécharger (.pdf)",
                                    data=f_pdf,
                                    file_name=pdf_file,
                                    mime="application/pdf",
                                    use_container_width=True
                                )
                        else:
                            st.info("⚠️ PDF non généré (voir logs terminal)")
                else:
                    st.error("❌ Aucun fichier de rapport trouvé dans le dossier outputs/")
            else:
                st.error("❌ Échec de la génération. Vérifiez votre connexion ou réessayez.")