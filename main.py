import os
import ssl
import time
from dotenv import load_dotenv
from crewai import Crew, Process
import markdown
from xhtml2pdf import pisa

def convertir_en_pdf(contenu_md: str, nom_fichier: str):
    """Convertit le contenu Markdown en PDF (Version 100% Python pour Windows)"""
    try:
        # 1. Convertir Markdown en HTML
        html_content = markdown.markdown(contenu_md, extensions=['tables', 'fenced_code'])
        
        # 2. Ajouter un style CSS compatible avec xhtml2pdf
        html_styled = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; color: #333; }}
                h1 {{ color: #1E88E5; border-bottom: 2px solid #1E88E5; padding-bottom: 10px; font-size: 24px; }}
                h2 {{ color: #333; margin-top: 30px; font-size: 18px; }}
                h3 {{ color: #555; font-size: 16px; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; font-size: 12px; }}
                th {{ background-color: #f2f2f2; color: #1E88E5; }}
                code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; font-family: monospace; }}
                a {{ color: #1E88E5; text-decoration: none; }}
            </style>
        </head>
        <body>{html_content}</body>
        </html>
        """
        
        # 3. Générer le PDF
        nom_pdf = nom_fichier.replace('.md', '.pdf')
        with open(nom_pdf, "w+b") as result_file:
            pisa_status = pisa.CreatePDF(html_styled, dest=result_file)
            
        if pisa_status.err:
            raise Exception("Erreur lors de la création du PDF par pisa")
            
        return nom_pdf
        
    except Exception as e:
        print(f"⚠️ Conversion PDF échouée (mais le .md est OK) : {e}")
        return None

# 🛡️ CONTOURNER L'INTERCEPTION SSL DE KASPERSKY
ssl._create_default_https_context = ssl._create_unverified_context

# 1. Charger les variables d'environnement
load_dotenv()

# 2. Configuration FORCÉE pour OpenRouter via LiteLLM
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "openrouter/auto"

# 3. Importer les agents et tâches
from agents.researcher import researcher
from agents.analyst import analyst
from agents.strategist import strategist
from agents.writer import writer
from tasks.tasks import create_tasks

def run_rapport_with_retry(topic: str, max_retries: int = 3):
    """Génère un rapport stratégique avec retry automatique en cas d'erreur réseau"""
    
    print(f"\n{'='*70}")
    print(f"📊 GÉNÉRATION DE RAPPORT STRATÉGIQUE")
    print(f"Sujet : {topic}")
    print(f"{'='*70}\n")
    
    # Créer les tâches
    tasks = create_tasks(topic)
    
    # Créer le Crew (équipe d'agents)
    crew = Crew(
        agents=[researcher, analyst, strategist, writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        max_rpm=5
    )
    
    # Retry mechanism
    for attempt in range(1, max_retries + 1):
        print(f"\n⏳ Tentative {attempt}/{max_retries}...\n")
        
        try:
            result = crew.kickoff()
            
            # ✅ Créer le dossier outputs et sauvegarder le Markdown
            os.makedirs("outputs", exist_ok=True)
            rapport_filename = f"outputs/rapport_{topic.replace(' ', '_').replace(':', '').lower()[:30]}.md"
            
            with open(rapport_filename, "w", encoding="utf-8") as f:
                f.write(str(result))
            
            # ✅ NOUVEAU : Convertir en PDF avec xhtml2pdf
            try:
                pdf_filename = convertir_en_pdf(str(result), rapport_filename)
                if pdf_filename:
                    print(f"📄 PDF sauvegardé avec succès : {pdf_filename}")
            except Exception as e:
                print(f"⚠️ Conversion PDF échouée (mais le .md est OK) : {e}")
            
            print(f"\n{'='*70}")
            print(f"✅ RAPPORT GÉNÉRÉ AVEC SUCCÈS !")
            print(f"📁 Fichiers sauvegardés dans le dossier 'outputs/'")
            print(f"{'='*70}\n")
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            print(f"\n❌ Erreur lors de la tentative {attempt} : {error_msg[:200]}")
            
            if attempt < max_retries:
                print(f"⏰ Attente de 5 secondes avant la prochaine tentative...")
                time.sleep(5)
            else:
                print(f"\n{'='*70}")
                print(f"❌ ÉCHEC APRÈS {max_retries} TENTATIVES")
                print(f"💡 Astuce : Mets Kaspersky en pause pendant 15 minutes et réessaie.")
                print(f"{'='*70}\n")
                return None

if __name__ == "__main__":
    print("=== Agent Multi-Agents de Rapport Stratégique ===")
    print("Agents : Researcher → Analyst → Strategist → Writer\n")
    
    exemples = [
        "Le marché des AI Agents en 2026",
        "Analyse concurrentielle de Notion vs Coda",
        "Opportunités de l'IA dans le e-commerce en Europe"
    ]
    
    print("Sujets suggérés :")
    for i, ex in enumerate(exemples, 1):
        print(f"  {i}. {ex}")
    print(f"  4. Sujet personnalisé\n")
    
    choix = input("Ton choix (1-4) : ").strip()
    
    if choix == "1":
        topic = exemples[0]
    elif choix == "2":
        topic = exemples[1]
    elif choix == "3":
        topic = exemples[2]
    else:
        topic = input("Entre ton sujet : ")
    
    if topic:
        run_rapport_with_retry(topic, max_retries=3)