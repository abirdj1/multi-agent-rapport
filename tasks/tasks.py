from crewai import Task
from agents.researcher import researcher
from agents.analyst import analyst
from agents.strategist import strategist
from agents.writer import writer

def create_tasks(topic: str):
    # Tâche 1 : Recherche (Prompt très court pour économiser les tokens)
    research_task = Task(
        description=f"Fais une recherche internet courte sur : '{topic}'. Trouve 3 faits clés.",
        expected_output="Liste de 3 faits clés avec sources.",
        agent=researcher
    )
    
    # Tâche 2 : Analyse
    analysis_task = Task(
        description=f"Analyse ces 3 faits et trouve 1 tendance majeure.",
        expected_output="1 paragraphe d'analyse concise.",
        agent=analyst
    )
    
    # Tâche 3 : Stratégie
    strategy_task = Task(
        description=f"Donne 1 opportunité et 1 risque basés sur l'analyse.",
        expected_output="2 points courts : 1 opportunité, 1 risque.",
        agent=strategist
    )
    
       # Tâche 4 : Rédaction du rapport final COMPLET
    writing_task = Task(
        description=f"""Rédige un RAPPORT STRATÉGIQUE COMPLET et PROFESSIONNEL en français sur '{topic}'.
        
        Tu DOIS impérativement suivre cette structure en 9 sections :
        1. **Titre** (Accrocheur et professionnel)
        2. **Résumé Exécutif** (3-4 phrases max, les points clés pour un dirigeant)
        3. **Introduction / Contexte** (Pourquoi ce sujet est critique maintenant)
        4. **Principales Conclusions** (Key Insights - 3 à 5 points avec puces)
        5. **Analyse Détaillée** (Structurée en sous-sections : Marché, Technologie, Adoption)
        6. **Opportunités Stratégiques** (Avec estimation du potentiel/ROI)
        7. **Risques & Points de Vigilance** (Avec niveau de criticité : Haut/Moyen/Bas)
        8. **Recommandations Actionnables** (Court, moyen et long terme)
        9. **Sources** (Liste des liens cliquables mentionnés)
        
        Ton ton doit être celui d'un partenaire de cabinet de conseil : factuel, orienté décision, sans jargon inutile, avec une mise en forme Markdown impeccable (gras, listes, titres).""",
        expected_output="Un rapport stratégique complet d'au moins 800 mots, rigoureusement structuré en 9 sections, prêt à être présenté à un comité de direction.",
        agent=writer
    )
    
    return [research_task, analysis_task, strategy_task, writing_task]