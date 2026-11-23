"""Scénario pédagogique fictif de décision médicale partagée.

Les arguments et attaques ci-dessous sont des hypothèses de modélisation.
Ils ne constituent ni des données cliniques ni une recommandation thérapeutique.
"""

from argumentation import VAF

# Chaque argument reçoit un identifiant stable, un texte explicatif et une valeur.
# La séparation texte / identifiant / valeur facilite l'affichage et la discussion.
ARGUMENT_TEXT = {
    "A1": "Le traitement A présente une efficacité supérieure.",
    "A2": "Le traitement B est mieux toléré au quotidien.",
    "A3": "Le traitement A expose à davantage d'effets indésirables.",
    "A4": "Le traitement B présente une efficacité moindre.",
}

# Fonction eta : argument -> valeur qu'il promeut.
ARGUMENT_VALUES = {
    "A1": "efficacite",
    "A2": "qualite_de_vie",
    "A3": "securite",
    "A4": "efficacite",
}

# Relation d'attaque initiale R. Ces liens sont des choix de modélisation
# illustratifs à discuter et justifier avec le binôme / l'enseignant.
ATTACKS = {
    ("A1", "A2"),  # A1 conteste l'avantage de tolérance avancé par A2.
    ("A2", "A1"),  # A2 conteste un choix fondé uniquement sur l'efficacité.
    ("A3", "A1"),  # A3 met en cause le traitement A sur le plan de la sécurité.
    ("A4", "A2"),  # A4 nuance l'avantage attribué au traitement B.
}

# L'ordre va de la valeur la plus importante pour l'audience à la moins importante.
# Ce sont des profils illustratifs, pas des préférences mesurées chez des patients.
AUDIENCES = {
    "Priorité à l'efficacité": [
        "efficacite", "securite", "qualite_de_vie"
    ],
    "Priorité à la qualité de vie": [
        "qualite_de_vie", "securite", "efficacite"
    ],
    "Priorité à la sécurité": [
        "securite", "qualite_de_vie", "efficacite"
    ],
}


def build_vaf():
    """Construit le VAF commun aux audiences."""
    return VAF(
        args=ARGUMENT_TEXT.keys(),
        attacks=ATTACKS,
        values=ARGUMENT_VALUES,
    )
