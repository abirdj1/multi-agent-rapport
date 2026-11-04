from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from ddgs import DDGS

class DuckDuckGoSearchInput(BaseModel):
    query: str = Field(description="La requête de recherche à effectuer sur internet")

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Recherche des informations récentes sur internet via DuckDuckGo."
    args_schema: type[BaseModel] = DuckDuckGoSearchInput

    def _run(self, query: str) -> str:
        try:
            with DDGS() as ddgs:
                resultats = list(ddgs.text(query, max_results=8))
            if not resultats:
                return "Aucun résultat trouvé."
            texte = f"Résultats de recherche pour '{query}' :\n\n"
            for i, res in enumerate(resultats, 1):
                texte += f"{i}. {res['title']}\n   {res['body'][:200]}...\n   Lien : {res['href']}\n\n"
            return texte
        except Exception as e:
            return f"Erreur lors de la recherche : {str(e)}"

search_tool = DuckDuckGoSearchTool()