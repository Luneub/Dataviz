import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import json
import altair as alt


def load_data():
    data = pd.read_csv(r'C:\Users\Ludwig\Downloads\temperature-quotidienne-regionale.csv',sep=';')
    return data

data = load_data()

# Écrire  application Streamlit ici
st.title('Mon Application etude de données météo Streamlit')

# Création de la barre latérale pour les menus déroulants
st.sidebar.title('Menu')
section = st.sidebar.radio('Sélectionnez la section', ['Introduction', 'Généralités', 'Température max par région', 
                                                       'Cycles mensuels','Variabilité climatique','Anomalies de température',
                                                      'Jours de gel', 'Jours de canicule','Conclusion'])
if section == 'Introduction':
    st.header('Variations des température dans chaque région française: Comprendre les tendances climatiques depuis 2016')
    st.write("""
    Analyse des Données Météorologiques : Comprendre les Tendances Climatiques

    L'étude et l'analyse des données météorologiques sont cruciales pour mieux comprendre les changements climatiques qui affectent
    notre planète. Les données météorologiques fournissent un trésor d'informations sur les conditions atmosphériques passées, 
    présentes et futures, permettant ainsi aux chercheurs, scientifiques et planificateurs de prendre des décisions éclairées en 
    matière de climat, de météorologie et d'environnement.
    Dans le cadre de ce projet, nous explorerons un ensemble de données météorologiques exhaustif qui couvre une période 
    significative et qui comprend plusieurs attributs clés. Ces données, collectées avec soin, nous permettront 
    d'entreprendre une analyse approfondie des tendances climatiques dans différentes régions. 
    Comprendre ces tendances est essentiel pour anticiper les événements météorologiques extrêmes, 
    évaluer les impacts potentiels sur l'environnement, et contribuer aux efforts visant à atténuer les changements climatiques.
    
    Composition des Données

    Les données météorologiques que nous analyserons comprennent les éléments suivants :

    - ID : Un identifiant unique pour chaque enregistrement, permettant de suivre et d'organiser les données.
    - Date : La date de l'enregistrement, qui nous permettra de reconstituer les tendances météorologiques au fil du temps.
    - Code INSEE de la Région : Un code INSEE spécifique à chaque région, nous permettant d'associer les données à des régions 
    géographiques spécifiques.
    - Région : Le nom de la région géographique associée à chaque enregistrement.
    - Température Minimale (Tmin) : La température minimale enregistrée pendant la journée, mesurée en degrés Celsius.
    - Température Maximale (Tmax) : La température maximale enregistrée pendant la journée, également mesurée en degrés Celsius.
    - Température Moyenne (Tmoy) : La température moyenne calculée à partir des valeurs de Tmin et Tmax.

    Objectifs du Projet

    L'objectif principal de ce projet est de conduire une analyse approfondie de ces données pour :

    - Identifier les tendances climatiques à long terme dans différentes régions.
    - Étudier les variations saisonnières et les cycles climatiques.
    - Évaluer les extrêmes climatiques, tels que les vagues de chaleur et les périodes de froid intense.

    Dans les sections suivantes de ce projet, nous explorerons ces données en utilisant des techniques d'analyse de données, 
    de visualisation et de modélisation. Notre objectif ultime est de contribuer à une compréhension plus profonde des phénomènes 
    climatiques qui façonnent notre planète et d'encourager des actions positives pour protéger notre environnement.
    """)

elif section == 'Généralités':
    # Extraction de l'année à partir de la colonne "date"
    data['Année'] = pd.to_datetime(data['date']).dt.year
    # Calcul de la moyenne de Tmoy par année et par région
    mean_tmin_by_year_region = data.groupby(['Année', 'region'])['tmin'].mean().reset_index()
    st.header('Généralités')
    # Analyse de l'évolution de Tmoy au fil du temps
    st.subheader('Comparaison de la température moyennes depuis 2016 pour chaque région')
    # Utilisation de la palette de couleurs de seaborn
    palette = sns.color_palette('Set2', n_colors=len(mean_tmin_by_year_region))

    # Création de l'histogramme avec des couleurs uniques pour chaque région
    fig, ax = plt.subplots(figsize=(12, 6))  # Définir la taille de la figure
    ax.bar(mean_tmin_by_year_region['region'], mean_tmin_by_year_region['tmin'], color=palette)
    ax.set_xlabel('Région')
    ax.set_ylabel('Moyenne de Tmin')
    ax.set_title('Moyenne de Tmin par Région')
    ax.tick_params(axis='x', rotation=80, labelsize=12)  # Pour faire pivoter les étiquettes des régions si nécessaire
    
    # Affichage de l'histogramme dans Streamlit
    st.pyplot(fig)
    
    #texte
    st.write("""Cet histogramme nous permet de visualiser la moyenne des températures minimales de chaques régions depuis 2016.
             Cela nous permet d'observer que les régions francaises les plus froides sont le Grand Est (Alsace, Loraine,...),
             l'Auvergne-Rhône-Alpes (Cantal, Ardèche,...), la Bourgogne-Franche-Compté (Jura, Yonne,...), les Hauts-de-France (Aisne, Oise,...)
             ainsi que la Normandie (Calvados, Orne,...).""")
    
    #HISTOGRAME 2
    
    # Extraction de l'année à partir de la colonne "date"
    data['Année'] = pd.to_datetime(data['date']).dt.year
    # Calcul de la moyenne de Tmoy par année et par région
    mean_tmoy_by_year_region = data.groupby(['Année', 'region'])['tmoy'].mean().reset_index()
    
      # Utilisation de la palette de couleurs de seaborn
    palette = sns.color_palette('Set2', n_colors=len(mean_tmoy_by_year_region))

    # Création de l'histogramme avec des couleurs uniques pour chaque région
    fig, ax = plt.subplots(figsize=(12, 6))  # Définir la taille de la figure
    ax.bar(mean_tmoy_by_year_region['region'], mean_tmoy_by_year_region['tmoy'], color=palette)
    ax.set_xlabel('Région')
    ax.set_ylabel('Moyenne de Tmoy')
    ax.set_title('Moyenne de Tmoy par Région')
    ax.tick_params(axis='x', rotation=80, labelsize=12)  # Pour faire pivoter les étiquettes des régions si nécessaire
    
    # Affichage de l'histogramme dans Streamlit
    st.pyplot(fig)
    
    #texte
    st.write("""Ce segond histogramme nous permet de visualiser la moyenne des températures moyennes de chaques régions depuis 2016.
             Cela nous permet d'observer que les régions francaises les plus agréable à vivre en fonction des préférences de chacun.
             On peut voir que malgré certaines régions exceptionnelles, la plupart se situent aux alentour des 15°C de moyenne et les résultats
             sont assez homogènes.""")
    
    # Histogramme 3
    # Extraction de l'année à partir de la colonne "date"
    data['Année'] = pd.to_datetime(data['date']).dt.year
    # Calcul de la moyenne de tmax par année et par région
    mean_tmax_by_year_region = data.groupby(['Année', 'region'])['tmax'].mean().reset_index()
    
    # Utilisation de la palette de couleurs de seaborn
    palette = sns.color_palette('Set2', n_colors=len(mean_tmax_by_year_region))

    # Création de l'histogramme avec des couleurs uniques pour chaque région
    fig, ax = plt.subplots(figsize=(12, 6))  # Définir la taille de la figure
    ax.bar(mean_tmax_by_year_region['region'], mean_tmax_by_year_region['tmax'], color=palette)
    ax.set_xlabel('Région')
    ax.set_ylabel('Moyenne de Tmax')
    ax.set_title('Moyenne de Tmin par Région')
    ax.tick_params(axis='x', rotation=80, labelsize=12)  # Pour faire pivoter les étiquettes des régions si nécessaire
    
    # Affichage de l'histogramme dans Streamlit
    st.pyplot(fig)
    
    #texte
    st.write("""Cet histogramme nous permet de visualiser la moyenne des températures maximales de chaques régions depuis 2016.
             Cela nous permet d'observer que les régions francaises les plus chaudes sont la Corse,
             l'Occitanie (Hérault, Lot, Lozère,...) et la région Provence-Alpes-Côte d'Azur (Bouches-du-Rhône, Var, 
             Vaucluse,...) avec des moyennes maximales au-dessus de 20°C.""")
    
    
elif section == 'Température max par région':
    st.header('Températures maximales par régions ')
    # Filtrage des données pour les années à partir de 2016
    data = data[pd.to_datetime(data['date']).dt.year >= 2016]
    # Agrégation des données par année et par région en calculant la moyenne de Tmax
    data = data.groupby(['region', pd.to_datetime(data['date']).dt.year])['tmax'].mean().reset_index()

    # Création du graphique interactif avec Plotly Express
    fig = px.line(data, x='date', y='tmax', color='region',
              labels={'tmax': 'Température Maximale (Tmax)', 'date': 'Année'},
              title='Évolution de la Température Maximale par Région depuis 2016')

    # Configuration de la légende pour afficher les noms des régions
    fig.update_layout(legend_title_text='Région')

    # Affichage du graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Ce graphique est extrêmement intéressant à analyser. En effet on remarque que les températures maximales ont évolué 
    de la même facon dans toutes les régions. Entre 2016 et 2020, l'augmentation de la température était assez 
    minime dans toutes les régions.
    Cependant les températures maximales ont brusquement chutées lors des années 2020 et 2021. 
    On peut supposer que cette brusque diminution est liée à la pandémie mondiale qui a causé l'arret complet des 
    activité et des émissions dans la quasi-totalité du globe.
    De plus, on remarque qu'à la fin de la pandémie, les températures ont augmentées de facon exponentielle en surpassant 
    ce qu'on aurait pu prévoir avant la pandémie mondiale.
    Ce graphique confirme aussi que comme le veut la logique, les régions les plus au Sud ont des températures plus élevées.""")
    
    
    
    
elif section == 'Cycles mensuels':
    st.header('Cycles mensuels')
    # Filtrage des données pour la région Île-de-France
    idf_data = data[data['region'] == 'Île-de-France']

    # Conversion de la colonne 'date' en format datetime
    idf_data['date'] = pd.to_datetime(idf_data['date'])

    # Échantillonnage des données mensuellement en prenant la moyenne
    idf_data_resampled = idf_data.resample('M', on='date').mean().reset_index()


    # Création du graphique interactif avec Plotly Express
    fig = px.line(idf_data_resampled, x='date', y=['tmin', 'tmax', 'tmoy'],
              labels={'value': 'Température (°C)', 'variable': 'Type de Température', 'date': 'Date'},
              title='Évolution des Températures en Île-de-France (Échantillonnage Mensuel)',
              color_discrete_sequence=['blue', 'red', 'green'],  # Couleurs de courbes différentes
              )

    # Configuration de la légende pour afficher les noms des types de température
    fig.update_layout(legend_title_text='Type de Température')

    # Affichage du graphique interactif dans Streamlit
    st.plotly_chart(fig)
    st.write("""Ce graphique nous permet d'analyser les cycles annuels de température dans la région Ile-d-France.
    On peut remarquer comme mentionner dans la partie précédente, que les températures ont globalement chutées lors de la période du Covid.
    Si on met de côté cette période, on remarque que les températures minimales et maximales ont augmenté dans la région parisienne.
    Cepenant la température moyenne ne semble pas augmenté. On peut alors supposer que malgré une légère augmentation des températures minimales,
    il semble y avoir plus de jours à temperature résonnables que de jours de forte chaleurs.\n""")
    
    ##2
    # Filtrage des données pour la région Pays de la Loire
    pdl_data = data[data['region'] == 'Pays de la Loire']

    # Conversion de la colonne 'date' en format datetime
    pdl_data['date'] = pd.to_datetime(pdl_data['date'])

    # Échantillonnage des données mensuellement en prenant la moyenne
    pdl_data_resampled = pdl_data.resample('M', on='date').mean().reset_index()


    # Création du graphique interactif avec Plotly Express
    fig = px.line(pdl_data_resampled, x='date', y=['tmin', 'tmax', 'tmoy'],
              labels={'value': 'Température (°C)', 'variable': 'Type de Température', 'date': 'Date'},
              title='Évolution des Températures en Pays de la Loire (Échantillonnage Mensuel)',
              color_discrete_sequence=['blue', 'red', 'green'],  # Couleurs de courbes différentes
              )

    # Configuration de la légende pour afficher les noms des types de température
    fig.update_layout(legend_title_text='Type de Température')


    # Affichage du graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""L'analyse des cycles pour la régions Pays de la Loire semble confirmer l'hypothèseénoncé précedemment.
    En effet, on observe à nouveau que les moyennes des températures maximales et minimales augmentent legerment alors que 
    les températures moyennes ne semblent pas augmenter significativement.""")
    
elif section=='Variabilité climatique':
    st.header('Variabilité climatique')
    
    
    # Utilisation de barres obliques inverses doubles pour échapper aux caractères \
    image_path = "varcli.png"


    # Afficher l'image
    st.image(image_path, caption='', use_column_width=True)
    
    st.write("""La "variabilité climatique" est une mesure de la dispersion ou de la variation des 
    températures quotidiennes dans une région donnée sur une période de temps spécifique. Plus l'écart type est élevé, 
    plus les températures quotidiennes dans cette région sont variables et fluctuent fréquemment. 
    En d'autres termes, une variabilité climatique élevée signifie que la région connaît des fluctuations importantes 
    de température, ce qui peut indiquer des variations saisonnières ou des conditions climatiques instables. Dans notre cas, les régions Grand Est et Centre-Val de Loire ont une variabilité climatique assez importante. Ce sont donc 
     des régions où il peut être difficile de prévoir le temps mais aussi de gérer les ressources agricoles à cause des trop grandes 
     variations de température.
    """)
    
elif section=='Anomalies de température':
    st.header('Anomalies de temperature')
    # Sélection la région 
    region_selectionnee = 'Corse'

    # Filtrer les données pour la région sélectionnée
    region_data = data[data['region'] == region_selectionnee]

    # Calcul des anomalies de température
    long_term_mean_temp = region_data['tmoy'].mean()
    region_data['anomalies_temperature'] = region_data['tmoy'] - long_term_mean_temp

    # Création du graphique de dispersion interactif représentant les anomalies de température
    fig = px.scatter(region_data, x='date', y='anomalies_temperature', 
                 title=f'Anomalies de Température pour la Région {region_selectionnee}',
                 labels={'date': 'Date', 'anomalies_temperature': 'Anomalies de Température (°C)'})

    # Affichage du graphique interactif dans Streamlit
    st.plotly_chart(fig)
        
    st.write("""Les anomalies de température sont un indicateur essentiel pour évaluer les variations climatiques 
        dans une région donnée. Cet attribut mesure les écarts de température quotidienne par rapport à une moyenne à long 
        terme, permettant ainsi de détecter les tendances climatiques inhabituelles. L'intérêt majeur de cette mesure réside 
        dans sa capacité à mettre en lumière les changements climatiques significatifs, tels que les épisodes de chaleur 
        extrême, les vagues de froid ou les variations saisonnières inhabituelles. En examinant les anomalies de température, 
        les chercheurs, les scientifiques et les décideurs peuvent mieux comprendre les phénomènes climatiques locaux, 
        anticiper les risques environnementaux et adapter les stratégies d'atténuation des changements climatiques. 
        Cette mesure fournit également des informations cruciales pour évaluer les impacts potentiels sur la santé publique, 
        l'agriculture, la gestion de l'eau et d'autres secteurs clés, contribuant ainsi à la prise de décisions éclairées 
        en matière de gestion du climat.
        Dans notre cas on observe certains pics de chaleur (juillet 2019,...) ou de froid(fevrier 2018,...) qui ne sont pas constants
        au cours des années.

""")
    
    
    # Sélectionnez la région que vous souhaitez analyser (par exemple, 'Île-de-France')
    region_selectionnee = 'Île-de-France'

    # Filtrer les données pour la région sélectionnée
    region_data = data[data['region'] == region_selectionnee]

    # Calcul des anomalies de température (écart par rapport à la température moyenne à long terme)
    long_term_mean_temp = region_data['tmoy'].mean()
    region_data['anomalies_temperature'] = region_data['tmoy'] - long_term_mean_temp

    # Création du graphique de dispersion interactif représentant les anomalies de température
    fig = px.scatter(region_data, x='date', y='anomalies_temperature', 
             title=f'Anomalies de Température pour la Région {region_selectionnee}',
             labels={'date': 'Date', 'anomalies_temperature': 'Anomalies de Température (°C)'})

    # Affichage du graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Si on compare ce second graphique avec le premier, on remarque que l'amplitude des anomalies de température est plus 
    importante que pour la Corse. De plus, les valeurs aberrantes sont beaucoup plus nombreuses que pour la Corse.
    On peut donc on conclure que l'Ile de France est une région avec une amplitude de température annuelles ainsi que des 
    variations de temperature plus importante que la region Corse. """)

    
elif section=='Jours de gel':
    st.header('Jours de gel')
    
    # Filtrer les données pour l'année 2016
    data_2016 = data[data['date'].str.startswith('2016')]

    # Compter le nombre de jours de gel (Tmin < 0°C) pour chaque région en 2016
    data_2016['gel_days'] = (data_2016['tmin'] < 0).astype(int)
    gel_days_by_region = data_2016.groupby('region')['gel_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Plotly  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(gel_days_by_region, x='region', y='gel_days',
         title='Nombre de Jours de Gel par Région en 2016',
         labels={'gel_days': 'Nombre de Jours de Gel', 'region': 'Région'},
         color='region',  # Utilisation de la région comme paramètre de couleur
         color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""L'histogramme interactif ci-dessus met en évidence le nombre de jours de gel enregistrés dans différentes régions de France au cours de l'année 2016. Les jours de gel sont définis comme des journées où la température minimale est inférieure à 0°C. Cette analyse revêt une importance particulière pour plusieurs raisons clés :

Impact sur l'agriculture : Les jours de gel peuvent avoir des conséquences significatives sur l'agriculture, en particulier dans les régions où les cultures sont sensibles au froid. Comprendre la fréquence de ces jours est essentiel pour les agriculteurs et les planificateurs agricoles.

Évaluation des risques : La connaissance des jours de gel est cruciale pour l'évaluation des risques. Les autorités locales et les gestionnaires des infrastructures, notamment dans le secteur de l'énergie et du transport, doivent anticiper les effets potentiels du gel sur les routes, les réseaux électriques et d'autres infrastructures.

Impacts sur la santé : Les vagues de froid et les jours de gel sont associés à des risques accrus pour la santé publique. L'analyse des jours de gel est importante pour la planification des services de santé, en particulier dans les régions où les températures hivernales sont extrêmement basses.

Données climatiques à long terme : Cette analyse contribue également à la compréhension des tendances climatiques à long terme. Les variations dans le nombre de jours de gel peuvent offrir des indications sur les changements climatiques régionaux.
""")
    
    #2019
    # Filtrer les données pour l'année 2019
    data_2019 = data[data['date'].str.startswith('2019')]

    # Compter le nombre de jours de gel (Tmin < 0°C) pour chaque région en 2019
    data_2019['gel_days'] = (data_2019['tmin'] < 0).astype(int)
    gel_days_by_region = data_2019.groupby('region')['gel_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Plotly  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(gel_days_by_region, x='region', y='gel_days',
             title='Nombre de Jours de Gel par Région en 2019',
             labels={'gel_days': 'Nombre de Jours de Gel', 'region': 'Région'},
             color='region',  # Utilisation de la région comme paramètre de couleur
             color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Ce second graphique nous permet d'analyser l'évolution du nombre de jours de gel dans toute les régions francaises.
    On remarque que la Corse reste la region possédant le moins de jours de gel de France. Par ailleurs ce nombre semble avoir 
    évoluer de facon significative dans certaines régions. Par exemple, le nombre de jours de gel a significativement 
    augmenté en Auvergne Rhône-Alpes passant de 51 en 2016 à 62 en 2019.""")
    
    #2021
    
    
    # Filtrer les données pour l'année 2021
    data_2021 = data[data['date'].str.startswith('2021')]

    # Compter le nombre de jours de gel (Tmin < 0°C) pour chaque région en 2021
    data_2021['gel_days'] = (data_2021['tmin'] < 0).astype(int)
    gel_days_by_region = data_2021.groupby('region')['gel_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Plotly  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(gel_days_by_region, x='region', y='gel_days',
             title='Nombre de Jours de Gel par Région en 2021',
             labels={'gel_days': 'Nombre de Jours de Gel', 'region': 'Région'},
             color='region',  # Utilisation de la région comme paramètre de couleur
             color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Ce graphique nous permet de constater que le nombre de jours de gels à généralement augmenté dans toutes
    les régions. Nous pouvons prendre le nombre de jours de gel en Normandie qui est passé de 21 en 2019 à 33 en 2021. 
    On peut relier cela à l'hypothèse que nous avions énoncés précedement : Les températures semblent avoir diminués
    dans toute la france lors de l'année du Covid.""")
    
    #2023
    # Filtrer les données pour l'année 2023
    data_2023 = data[data['date'].str.startswith('2023')]

    # Compter le nombre de jours de gel (Tmin < 0°C) pour chaque région en 2023
    data_2023['gel_days'] = (data_2023['tmin'] < 0).astype(int)
    gel_days_by_region = data_2023.groupby('region')['gel_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Plotly  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(gel_days_by_region, x='region', y='gel_days',
             title='Nombre de Jours de Gel par Région en 2023',
             labels={'gel_days': 'Nombre de Jours de Gel', 'region': 'Région'},
             color='region',  # Utilisation de la région comme paramètre de couleur
             color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Ce dernier histogramme semble comfirmer l'hypothese d'un réchauffement global suite à la reprise d'activité
    après la pandémie mondiale.
    En effet, le nombre de jours de gel en 2023 à significativement diminué entre 2021 et 2023.
    Par exemple, le nombre de jours de gel dans le Grand Est est passé de 62 en 2021 à seulement 33 en 2023.
    Ce qui représente quasiment une baisse de 45%.""")
    
    
elif section=='Jours de canicule':
    st.header('Jours de canicules')
    
    # Filtrer les données pour l'année 2016
    data_2016 = data[data['date'].str.startswith('2016')]

    # Compter le nombre de jours de canicule (Tmax > 30°C) pour chaque région en 2016
    data_2016['canicule_days'] = (data_2016['tmax'] > 30).astype(int)
    canicule_days_by_region = data_2016.groupby('region')['canicule_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Set1  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(canicule_days_by_region, x='region', y='canicule_days',
             title='Nombre de Jours de Canicule par Région en 2016',
             labels={'canicule_days': 'Nombre de Jours de Canicule', 'region': 'Région'},
             color='region',  # Utilisation de la région comme paramètre de couleur
             color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""L'histogramme interactif ci-dessus présente le nombre de jours de canicule pour chaque région de France en 2016. La canicule est définie comme une période pendant laquelle la température maximale (Tmax) dépasse 30°C. Cette visualisation est pertinente pour plusieurs raisons essentielles :

Santé Publique et Préparation aux Risques Climatiques : En mettant en évidence les régions où les jours de canicule sont plus fréquents, ce graphique peut aider les autorités de santé publique et les responsables de la gestion des risques climatiques à se préparer aux vagues de chaleur. Il est essentiel de protéger la population contre les effets néfastes de la chaleur excessive.

Adaptation au Changement Climatique : Le changement climatique entraîne une augmentation de la fréquence et de l'intensité des vagues de chaleur. Cette visualisation permet de suivre les régions les plus touchées et peut aider à orienter les mesures d'adaptation nécessaires, comme la mise en place de systèmes de refroidissement, de plans d'urgence et de sensibilisation.

Consommation d'Énergie et Besoins en Électricité : Les vagues de chaleur ont tendance à augmenter la demande d'électricité en raison de l'utilisation généralisée de la climatisation. En identifiant les régions sujettes aux canicules, les services d'électricité peuvent mieux anticiper les besoins en énergie et prévenir les pannes éventuelles.

Compréhension des Modèles Climatiques Locaux : En observant les variations régionales du nombre de jours de canicule, les chercheurs peuvent affiner leurs modèles climatiques locaux pour mieux prédire les événements futurs. Cette compréhension approfondie est essentielle pour des projections climatiques plus précises.

Impact sur l'Agriculture et l'Écologie : Les vagues de chaleur peuvent avoir un impact significatif sur l'agriculture et l'écosystème local. Cette visualisation peut aider les agriculteurs et les écologistes à mieux comprendre les défis et à prendre des mesures d'atténuation.
""")
    
    #2019
    
    # Filtrer les données pour l'année 2019
    data_2019 = data[data['date'].str.startswith('2019')]

    # Compter le nombre de jours de canicule (Tmax > 30°C) pour chaque région en 2019
    data_2019['canicule_days'] = (data_2019['tmax'] > 30).astype(int)
    canicule_days_by_region = data_2019.groupby('region')['canicule_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Set1  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(canicule_days_by_region, x='region', y='canicule_days',
             title='Nombre de Jours de Canicule par Région en 2019',
             labels={'canicule_days': 'Nombre de Jours de Canicule', 'region': 'Région'},
             color='region',  # Utilisation de la région comme paramètre de couleur
             color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Ce second graphique nous permet de constater que le nombres de jours caniculaires à considérablement augmenté dans 
    presque toutes les régions francaises entre 2016 et 2019.
    Nous pouvons prendre comme exemple la région Centre-Val-de-Loire qui est passé de 20 jours de fortes chaleurs en 2016
    à 30 jours en 2019. 
    Cela semble confirmer l'hypothèse de l'augmentation de la température globale avant la crise mondiale.""")
    
    #2021
    
    # Filtrer les données pour l'année 2021
    data_2021 = data[data['date'].str.startswith('2021')]

    # Compter le nombre de jours de canicule (Tmax > 30°C) pour chaque région en 2021
    data_2021['canicule_days'] = (data_2021['tmax'] > 30).astype(int)
    canicule_days_by_region = data_2021.groupby('region')['canicule_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Set1  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(canicule_days_by_region, x='region', y='canicule_days',
             title='Nombre de Jours de Canicule par Région en 2021',
             labels={'canicule_days': 'Nombre de Jours de Canicule', 'region': 'Région'},
             color='region',  # Utilisation de la région comme paramètre de couleur
             color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Cet histogramme pour l'année 2021 semble assez surprenant au premier abord, mais il vient en réalité renforcer
    notre hypothèse de rafraichssiment globale des températures lors de la période du Covid19.
    En effet on observe que la cantité de jours de canicule à drastiquement diminué pour chaque région entre les années 
    2019 et 2021. Nous pouvons prendre comme exemple la Normandie et les Hauts de France qui n'ont pas eu un seul jour de canicule 
    ou encore la région Ile-de-France qui est passé de 20 jours de fortes chaleurs à seulement 5 en 2021.""")
    
    #2023
    
    # Filtrer les données pour l'année 2023
    data_2023 = data[data['date'].str.startswith('2023')]

    # Compter le nombre de jours de canicule (Tmax > 30°C) pour chaque région en 2023
    data_2023['canicule_days'] = (data_2023['tmax'] > 30).astype(int)
    canicule_days_by_region = data_2023.groupby('region')['canicule_days'].sum().reset_index()

    # Sélectionner une séquence de couleurs
    colors = px.colors.qualitative.Set1  # Séquence de couleurs de Plotly

    # Créer un graphique interactif avec Plotly Express en utilisant différentes couleurs pour chaque région
    fig = px.bar(canicule_days_by_region, x='region', y='canicule_days',
             title='Nombre de Jours de Canicule par Région en 2023',
             labels={'canicule_days': 'Nombre de Jours de Canicule', 'region': 'Région'},
             color='region',  # Utilisation de la région comme paramètre de couleur
             color_discrete_sequence=colors)  # Séquence de couleurs différentes

    # Afficher le graphique interactif dans Streamlit
    st.plotly_chart(fig)
    
    st.write("""Tout comme pour les jours de gel, on peut voir que les quantités de nombre de jours caniculaire n'ont 
    rien à voir avec les données des précedentes années.
    En effet, la reprise de l'activité mondiale semble être responsable de cette hausse drastique de nombre de jours de forte
    chaleur.
    Nous pouvons prendre comme exemple la région Occitanie qui a vu son nombre de jours de canicule doublé entre 2021 et 2023,
    passant de 21 à 42. Ou encore la région Bourgogne-Franche-Comté qui est passé de 11 jours de fortes chaleur en 2021 
    à 29 en 2023.""")
    
elif section=='Conclusion':
    st.header('Conclusion')
    st.write("""L'analyse de données météorologiques révèle des informations cruciales sur les tendances climatiques, les variations régionales et les impacts potentiels sur divers secteurs. Les différents graphiques et histogrammes produits dans ce projet apportent des éclairages importants sur les températures minimales, maximales et moyennes dans les régions françaises depuis 2016.

L'analyse des températures minimales met en évidence les régions les plus froides de France, notamment le Grand Est, l'Auvergne-Rhône-Alpes, la Bourgogne-Franche-Comté, les Hauts-de-France et la Normandie. En revanche, les températures maximales indiquent les régions les plus chaudes, telles que la Corse, l'Occitanie et la région Provence-Alpes-Côte d'Azur. Les données montrent également une évolution intéressante, avec une diminution brusque des températures maximales en 2020 et 2021, suivie d'une augmentation significative après la pandémie mondiale.

Les cycles annuels de température mettent en évidence des variations saisonnières dans les régions Ile-de-France et Pays de la Loire, avec une tendance à l'augmentation des températures minimales et maximales.

L'analyse de la variabilité climatique suggère que les régions Grand Est et Centre-Val de Loire connaissent des fluctuations importantes de température, ce qui peut poser des défis pour la planification et la gestion des ressources.

Les anomalies de température sont essentielles pour détecter les variations climatiques inhabituelles. Les pics de chaleur ou de froid observés, notamment en juillet 2019, soulignent l'importance de cette mesure pour comprendre les phénomènes climatiques locaux.

L'analyse des jours de gel est pertinente pour l'agriculture, la santé publique et l'évaluation des risques, tout en contribuant à la compréhension des tendances climatiques à long terme. Les données suggèrent une augmentation du nombre de jours de gel dans plusieurs régions.

La fréquence des jours de canicule est essentielle pour la santé publique, l'adaptation au changement climatique, la gestion de l'énergie et l'impact sur l'agriculture et l'écologie. Les résultats révèlent une augmentation du nombre de jours de canicule entre 2016 et 2019, une diminution en 2021 liée à la pandémie mondiale, puis une augmentation significative en 2023 après la reprise de l'activité mondiale.

En résumé, cette analyse de données météorologiques offre un aperçu détaillé des températures en France depuis 2016 et des variations climatiques qui ont eu lieu au cours de cette période. Ces informations sont essentielles pour la planification, la prise de décision et l'adaptation aux changements climatiques, tout en démontrant l'impact significatif des événements mondiaux sur les tendances locales.
    
    """)
