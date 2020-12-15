# Projet de visualisation de donnée Métagénomique. 
Réalisé par Johana Galvis et Marie Martelat.<br/>


### Présentation Projet 

En utilisant les données issus de la publication "Microbial Biogeography of Public Restroom Surfaces" de Flores et al., nous voulons montrer les possibilités
qu’offfent les packages Python pour la visualization de données dans le contexte de la métagénomique.<br/>
Nous avions à notre disposition une table de comptage de 14 échantillons.<br/>
Les échantillons ont été collectés sur différentes surface de toilette. Surface touché par les mains (door_in, faucet_handle, toilet_flush_handle) par les
pieds (sink_floor, toilet_floor) ou en contacte directe avec la partie posterieur du corp(toilet_seat).<br/>
Il peut être intéressant d’essayer de visualiser une différence de composition bactérienne dans ces différents type d’echantillons.<br/><br/>
Le poster finale de ce projet est présent dans le dépot sous le nom PosterVDV.pdf . <br/>
Les différentes figures réalisées sont localisées dans le dossier plots, qui contient des figures statics et dynamiques (html).


### Aide à l'exécution

Pour premmettre la visualisation des différentes figures présentes dans le fichier Jupyter (VdbFinalProject.ipynb) il est nécessaire d'importer ces différents packages : 
pandas, os, numpy, matplotlib, plotly, seaborn, sklearn et scipy.

Les deux premières cellules du fichier doivent obligatoirement être lancer avant d'effectuer une des figures des autres cellules du fichiers. Car en effet ces deux premières cellules contiennent les récupérations de données et méthodes nécessaire pour créer les figures.