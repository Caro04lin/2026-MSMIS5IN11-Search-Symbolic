"""Point d'entrée : comparaison Dung / VAF sur le même cas fictif."""

from argumentation import AF, af_from_audience, summarize
from medical_case import ARGUMENT_TEXT, ATTACKS, AUDIENCES, build_vaf


def format_extensions(extensions):
    """Affiche les extensions sous une forme stable et lisible."""
    return [
        "{" + ", ".join(sorted(extension)) + "}"
        for extension in extensions
    ]


def display_summary(label, af):
    print(f"\n{label}")
    for semantics, extensions in summarize(af).items():
        print(f"  {semantics:12s}: {format_extensions(extensions)}")


if __name__ == "__main__":
    print("F2 — Argumentation à valeurs pour la décision médicale partagée")
    print("Cas fictif : deux options thérapeutiques\n")

    print("Arguments :")
    for arg_id, description in ARGUMENT_TEXT.items():
        print(f"  {arg_id} ({arg_id}): {description}")

    print("\nAttaques initiales :", sorted(ATTACKS))

    # Baseline Dung : toutes les attaques initiales sont considérées comme réussies.
    baseline = AF(ARGUMENT_TEXT.keys(), ATTACKS)
    display_summary("1) Référence Dung — sans préférences de valeurs", baseline)

    # VAF : mêmes arguments et attaques, mais les attaques sont filtrées selon l'audience.
    vaf = build_vaf()
    print("\nVAF :", vaf)

    for label, audience in AUDIENCES.items():
        audience_af = af_from_audience(vaf, audience)
        print(f"\n2) {label}")
        print("  Ordre de préférence :", " > ".join(audience))
        print("  Attaques qui réussissent :", sorted(audience_af.attacks))
        display_summary("  Sémantiques sur l'AF filtré", audience_af)
