# Notion vs Coda : anatomie d'une concurrence déjà terminée — et là où se déplace réellement la ligne de front

---

## 1. Résumé Exécutif

La question « Notion vs Coda » n'a plus d'objet concurrentiel : **Coda a été absorbé par Grammarly en janvier 2025** (annonce du 17 décembre 2024), la société mère s'est renommée **Superhuman** en novembre 2025, et Coda est devenu **« Superhuman Docs »** — Coda n'existe plus comme acteur indépendant. Le rapport de force était déjà scellé bien avant : **Notion ≈ 100 M d'utilisateurs et ~52 % de part de marché contre ~50 000 équipes et 0,27 % pour Coda**, soit un rapport d'échelle supérieur à 50 sur la part de marché et de l'ordre de 1 à 10 sur le revenu. Le véritable enseignement n'est pas là : **un modèle de tarification est le thermomètre du pouvoir de marché, pas son levier** — Notion facture la couverture (par siège) parce qu'il est devenu le standard ; Coda facturait la création (per Doc Maker) parce qu'il ne pouvait pas imposer la couverture. La ligne de front se déplace désormais de « siège vs créateur » vers **« IA bundlée vs IA à l'usage »**, terrain sur lequel Microsoft, Google et Atlassian peuvent inclure l'IA dans des sièges déjà payés — c'est là que se situe le risque n°1 pour tout DSI.

---

## 2. Introduction / Contexte

**Pourquoi ce sujet est critique maintenant.** Trois événements rapprochés ont transformé une comparaison d'outils en décision d'architecture patrimoniale :

1. **Le 13 mai 2025**, Notion a **supprimé son add-on IA facturé 10 $/utilisateur/mois** et l'a **intégré au plan Business** — un mouvement de *bundling* qui augmente mécaniquement le ticket moyen par siège.
2. **Le 5 novembre 2025**, Grammarly s'est renommée **Superhuman**, regroupant Grammarly, Coda et Superhuman Mail ; **le 8 juillet 2026**, Coda est devenu **Superhuman Docs**, toutes les fonctionnalités étant conservées.
3. **Fin 2025**, Notion affiche un **ARR estimé à ~600 M$** (contre ~500 M$ en septembre 2025) sur une **base utilisateurs plate à 100 M depuis août 2024** — soit **+20 % de revenu sans croissance de base**.

Ce dernier point est le cœur du sujet : la croissance du marché ne se fait plus par acquisition d'utilisateurs mais par **extraction d'ARPU sur une base installée captive**. Toute organisation qui achète aujourd'hui un workspace collaboratif n'achète pas un outil, elle **entre dans un modèle de monétisation dont elle doit anticiper la trajectoire tarifaire**. C'est l'objet de ce rapport.

---

## 3. Principales Conclusions

- **🔴 La concurrence est close, pas arbitrée.** Coda n'est plus un concurrent de Notion mais une brique documentaire d'une suite AI-native dominée par un acteur 300× plus grand en valorisation (Grammarly : 13 Md$, 40 M d'utilisateurs actifs quotidiens). Le concurrent pertinent en 2026 est **Microsoft Loop/SharePoint, Google Workspace, Atlassian (Confluence + Rovo) et Superhuman Docs**.
- **🟠 L'avantage tarifaire de Coda est réel, non monétisable, mais transférable.** Le modèle « per Doc Maker » (éditeurs et lecteurs gratuits) reste structurellement **~93 % moins cher** sur un déploiement à forte proportion de lecteurs — avantage désormais porté par Superhuman, pas détruit.
- **🟠 La divergence tarifaire est un symptôme, pas une stratégie.** La capacité de Notion à augmenter son ARPU sans churn est un **indicateur de pouvoir de marché**, directement corrélé à sa distribution (100 M d'utilisateurs, ~52 % de part de marché).
- **🟡 Le risque dominant n'est pas le lock-in fournisseur, c'est la commoditisation de l'IA.** Les suites intégrées peuvent inclure l'IA dans des sièges déjà payés : la prime tarifaire payée aujourd'hui pour de l'IA « bundlée » est un **coût irréversible adossé à un avantage éphémère**.
- **🟡 La qualité de la donnée exige de la prudence.** Les chiffres de revenu proviennent de sources tierces non auditées et les prix Coda divergent selon les sources secondaires : ce rapport est un **outil de cadrage décisionnel**, pas un business case validé.

---

## 4. Analyse Détaillée

### 4.1 Marché — Un rapport d'échelle de 1 à 200, à lire avec méthode

| Indicateur | Notion | Coda | Écart |
|---|---|---|---|
| Utilisateurs / équipes | **~100 M** (août 2024, source primaire) | **> 50 000 équipes** | ×2 000 |
| Clients payants | **~4 M** | n.d. | — |
| Revenu | **~600 M$ ARR** (déc. 2025) | **~41,1 M$/an** (est. oct. 2024) | ~×10–15 |
| Part de marché | **52,12 %** (« collaborative workspaces ») | **0,27 %** (« team collaboration ») | ~×190 |
| Valorisation | **10–11 Md$** (≈18,3× le revenu) | non divulguée (acquisition) | — |

**Lecture.** Notion a franchi les 100 M d'utilisateurs en août 2024, milestone officialisé par le CEO **Ivan Zhao** dans le billet *« 100 Million of You »* — la donnée la plus solide de cette analyse. Coda revendique **plus de 50 000 équipes** (Figma, DoorDash, Square, The New York Times) pour un revenu estimé à **~41,1 M$**, à traiter comme un ordre de grandeur non audité.

⚠️ **Réserve méthodologique importante :** le rapport de 1 à 200 **surestime l'écart réel** — les segments 6sense ne sont pas comparables (« collaborative workspaces » vs « team collaboration », face à 193 concurrents référencés). Le **sens et l'ordre de grandeur (facteur > 50) tiennent**, mais le chiffre exact ne doit pas être cité sans cette nuance. Par ailleurs, un article secondaire (TechnoTrenz) avance 20 M d'utilisateurs fin 2024 : cette divergence s'explique vraisemblablement par une confusion entre **utilisateurs enregistrés cumulés** et **utilisateurs actifs**. Le chiffre à retenir est celui de la source primaire : **100 M**, à lire comme des comptes enregistrés cumulés.

### 4.2 Technologie & Tarification — Deux philosophies opposées de captation de valeur

**Notion — monétiser la couverture (per seat).** Grille publique : **Free (0 $)**, **Plus (10 $/membre/mois en annuel, 12 $ en mensuel)**, **Business (20 $/membre/mois en annuel, 24 $ en mensuel)**, **Enterprise sur devis**. Chaque membre actif génère un coût. Depuis le **13 mai 2025**, l'IA est **incluse dans le plan Business** (add-on à 10 $/siège supprimé) : le ticket moyen par siège augmente et le prix est **réaligné sur la valeur perçue de l'IA**.

**Coda / Superhuman Docs — monétiser la création (per Doc Maker).** Grille : **Free (0 $)**, **Pro (~10 $/Doc Maker/mois)**, **Business (~30–40 $/Doc Maker/mois)**, **Enterprise sur devis**, avec des **crédits IA facturés à la consommation**. Seuls les créateurs/gestionnaires paient ; **éditeurs et lecteurs sont gratuits**.

**Lecture concurrentielle.** Notion monétise la **couverture**, Coda la **création**. Sur 500 personnes avec 20 créateurs, Coda est structurellement moins cher ; au-delà de ~40 % de créateurs, **l'écart s'annule**. C'est le principal — et le seul — levier de différenciation prix de Coda.

⚠️ **Réserve :** les sources secondaires **divergent sur les prix Coda** (Pro à 10 $ ou 15 $ ; Business à 30 $ ou 40 $). Les montants doivent être présentés avec la mention « environ » et **revérifiés sur coda.io/pricing avant toute modélisation de coût**.

### 4.3 Adoption — La séquence causale, et l'insight non évident

Les trois faits ne sont pas trois observations indépendantes mais **une seule séquence causale** :

> **Déficit de distribution (fait n°2) → divergence tarifaire subie (fait n°1) → absorption (fait n°3).**

Le point de bascule est le **13 mai 2025** : en supprimant l'add-on IA pour le bundler dans Business, Notion réalise **un acte qu'un challenger ne peut pas se permettre** — augmenter le ticket moyen sans craindre le churn, parce que la base est captive et que l'IA est devenue non-substituable. La corrélation est vérifiable : **base plate à 100 M depuis août 2024, ARR de ~500 M$ à ~600 M$ en trois mois** — la croissance est désormais **tirée par l'ARPU, non par le volume**.

Symétriquement, le « per Doc Maker » de Coda est un **avantage de coût réel mais non monétisable** : à 0,27 % de part de marché, l'innovation tarifaire ne compense pas l'absence de canal. Grammarly/Superhuman n'achète pas un concurrent, il achète **une brique documentaire** — confirmé par le rebranding en Superhuman Docs avec conservation intégrale des fonctionnalités.

**L'insight que la lecture « Notion vs Coda » masque :** un modèle de pricing **révèle** le pouvoir de marché, il ne le crée pas. Et Superhuman, en conservant les **crédits IA à la consommation**, reconduit l'opposition bundling/usage **à un niveau supérieur** — préparant le vrai combat de 2026-2027.

---

## 5. Opportunités Stratégiques

### ✅ Opportunité n°1 — Arbitrer le modèle de facturation sur les déploiements à forte proportion de lecteurs *(quick win, 0–90 jours)*

**Le levier.** L'écart tarifaire structurel est **immédiatement capturable** sur les périmètres « opérationnels » : beaucoup de consultation, peu de production.

| Scénario : 500 utilisateurs, 20 créateurs | Coût annualisé |
|---|---|
| Notion Business (20 $/siège/mois en annuel) | ≈ **120 k$/an** |
| Coda/Superhuman Docs Business (~35 $/Doc Maker/mois) | ≈ **8,4 k$/an** |
| **Delta** | **≈ 110 k$/an, soit −93 %** |

**Potentiel estimé :** ~110 k$/an par déploiement de 500 personnes, soit **−40 % minimum de coût par utilisateur actif annuel** sur les périmètres re-platformés. Sur un parc de 3 000 sièges, le potentiel dépasse **600 k$/an**.

⚠️ *Réserve : chiffrage en ordre de grandeur, destiné à cadrer la décision, non un business case validé.*

### ✅ Opportunité n°2 — Négocier en position de force la clause IA *(0–6 mois)*

Notion a un **intérêt économique objectif** à augmenter ses prix par siège (croissance tirée par l'ARPU). Négocier un ***price lock* 24 mois, IA incluse sans surcoût**, avant la prochaine renégociation, capte la valeur d'un rapport de force qui ne durera pas.

### ✅ Opportunité n°3 — Utiliser Superhuman Docs comme levier de négociation, pas comme cible de migration *(6–18 mois)*

Le modèle « per Doc Maker » est un **argument de négociation crédible** face à Notion, même sans intention de migrer. **ROI :** compression tarifaire obtenue par effet de concurrence, sans coût de migration.

---

## 6. Risques & Points de Vigilance

| Risque | Mécanisme | Criticité |
|---|---|---|
| **Compression de valeur par le bundling IA des suites intégrées** | Microsoft (Loop/SharePoint), Google Workspace, Atlassian (Confluence + Rovo) incluent l'IA dans des sièges **déjà payés et déjà déployés** : ils n'ont pas à gagner la décision sur la valeur de l'IA, ils la **rendent gratuite par effet de bord**. | 🔴 **HAUT** — probabilité ~70 %, horizon 6–18 mois |
| **Prime tarifaire irréversible** | Toute prime payée aujourd'hui pour de l'IA « bundlée » est un **coût adossé à un avantage qui se commoditisera**. | 🔴 **HAUT** |
| **Lock-in par les primitives IA propriétaires** | Automatisations métier écrites dans les primitives IA du workspace → sortie non portable. | 🟠 **MOYEN** |
| **Qualité de la donnée décisionnelle** | ARR Notion et revenu Coda issus de sources tierces (GetLatka, multiples.vc), **non auditées** ; prix Coda divergents ; « 75 % du Fortune 500 » non rattaché à une publication officielle Notion. | 🟠 **MOYEN** |
| **Confusion d'acteurs (homonymes)** | **Coda Payments** (monétisation digitale) et **Coda Octopus** n'ont **aucun lien** avec Coda.io. | 🟡 **BAS** |

**Mitigations concrètes :**
1. **Clause de *price lock* 24 mois** sur le tarif par siège, IA incluse sans surcoût, interdisant toute hausse liée à l'IA.
2. **Découpler le siège de l'IA** dans l'architecture cible : aucune automatisation métier écrite dans les primitives IA propriétaires — **préserver la portabilité vers un LLM externe**.
3. **Test de substituabilité à 12 mois** sur un périmètre pilote. **Seuil d'alerte : > 20 jours-homme de migration ⇒ lock-in excessif, stopper l'extension du périmètre.**

---

## 7. Recommandations Actionnables

### 🔵 Court terme (0–90 jours) — *Financer la sécurité par l'économie*
- **Lancer sous 60 jours un *pricing audit*** sur les 3 espaces collaboratifs les plus peuplés (mesure du **ratio créateurs/lecteurs réel via les logs**).
- **Renégocier ou re-platformer sous 90 jours** les espaces dont le ratio créateurs/lecteurs est **< 20 %**.
- **KPI de succès : −40 % minimum de coût par utilisateur actif annuel** sur les périmètres re-platformés.
- **Condition d'arrêt :** ne re-platformer que les périmètres à faible intensité de création — au-delà de **~40 % de créateurs**, l'écart s'annule et le coût de migration détruit le ROI.

### 🟠 Moyen terme (3–12 mois) — *Verrouiller le contrat et l'architecture*
- **Insérer la clause de *price lock* 24 mois** au prochain avenant.
- **Documenter la carte de dépendance** (documents, automatisations, permissions) de chaque workspace : base du test de substituabilité.
- **Revérifier les grilles officielles** (notion.com/pricing, coda.io/pricing) et **dater explicitement** toute donnée de marché avant publication interne.

### 🟢 Long terme (12–24 mois) — *Anticiper le déplacement de la ligne de front*
- **Réexaminer le portefeuille** sur le nouvel axe **« IA bundlée vs IA à l'usage »** plutôt que sur l'axe obsolète « siège vs créateur ».
- **Benchmarker les suites intégrées** (Microsoft, Google, Atlassian) sur le coût marginal réel de l'IA, siège déjà payé.
- **Arbitrer annuellement** : la substituabilité technique et contractuelle est désormais le seul critère durable de choix de plateforme.

> **Ce qu'il faut retenir :** l'opportunité est **tactique et immédiate** (~110 k$/an sur 500 personnes) ; le risque est **structurel et progressif**. Le premier finance le second — **engagez l'audit tarifaire pour financer la clause de *price lock***.

---

## 8. Sources

**Notion — sources primaires et données de marché**
- Notion, *Pricing* — https://www.notion.com/pricing
- Notion, *100 Million of You* (Ivan Zhao, août 2024) — https://www.notion.com/blog/100-million-of-you
- Relais LinkedIn du billet — https://www.linkedin.com/pulse/100m-you-ivan-zhao-ylzbf

**Notion — tarification et IA (sources secondaires)**
- *Notion Pricing Pivot Audit* — https://danian.co/articles/post/notion-pricing-pivot-audit
- *Notion AI pricing* — https://www.usagepricing.com/blueprint/notion-ai
- AppStackInsider, *Notion pricing explained* — https://appstackinsider.com/insights/notion-pricing-explained/

**Notion — métriques et valorisation**
- https://taptwicedigital.com/stats/notion
- https://sqmagazine.co.uk/notion-statistics/
- https://axis-intelligence.com/notion-statistics/
- https://getlatka.com/companies/notion
- https://multiples.vc/private-comps/notion

**Parts de marché (6sense)**
- https://technographics.6sense.com/collaborative-workspaces/notion-market-share
- https://6sense.com/tech/team-collaboration/coda-market-share
- https://6sense.com/tech/collaborative-workspaces

**Coda — tarification et coûts**
- https://saasflags.com/products/coda/pricing
- https://comparedge.com/tools/coda/cost-guide
- https://www.usagepricing.com/blueprint/coda
- https://thedigitalprojectmanager.com/tools/coda-pricing/
- https://costbench.com/software/project-management/coda/
- https://multiples.vc/private-comps/coda-us

**Acquisition par Grammarly — sources primaires**
- https://www.grammarly.com/blog/company/grammarly-to-acquire-coda/
- https://www.businesswire.com/news/home/20241217547105/en/AI-Leader-Grammarly-to-Acquire-Coda-Bring-on-New-CEO
- https://coda.io/blog/about-coda/grammarly-acquires-coda

**Acquisition — presse**
- https://techcrunch.com/2024/12/17/grammarly-acquires-productivity-startup-coda-brings-on-new-ceo/
- https://siliconangle.com/2024/12/17/grammarly-acquires-coda-takes-co-founder-mehrotra-new-ceo/

**Rebranding Superhuman / Superhuman Docs**
- https://www.grammarly.com/blog/company/announcing-company-rebrand-to-superhuman/
- https://blog.superhuman.com/introducing-superhuman-docs/
- https://help.superhuman.com/hc/en-us/articles/46210093285773-What-s-changing-Coda-becomes-Superhuman-Docs
- https://seedtable.com/exits/coda-io

---

### ⚠️ Précautions méthodologiques à signaler au comité

1. **Prix Coda** — divergences entre sources secondaires (Pro 10 $ vs 15 $ ; Business 30 $ vs 40 $) → revérifier sur la grille officielle avant toute modélisation.
2. **Notion AI** — l'add-on à 10 $/utilisateur/mois a été **supprimé le 13 mai 2025** ; ne pas utiliser de grilles tarifaires antérieures à cette date.
3. **« 75 % du Fortune 500 »** — non rattaché à une publication officielle Notion → présenter comme « estimation diffusée par des sources secondaires ».
4. **Homonymes à exclure** — **Coda Payments** et **Coda Octopus** n'ont aucun lien avec **Coda.io**.
5. **Revenus** — les ARR de Notion et le revenu de Coda proviennent de sources tierces (GetLatka, multiples.vc), non de communications financières auditées → **ordres de grandeur uniquement**.
6. **Montant de l'acquisition Grammarly/Coda** — jamais rendu public → toute estimation circulant sur le web est **spéculative**.