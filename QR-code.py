import QRgen as gt

"""
Voor het maken van de QR code moeten de volgende gegevens bekend zijn verdieping, bouwnummer en webaders tussen " "
    Het webadres is de voledige titel van de website met tekst achter de .com/ 
    het webadres moet gekopierd worden van de pagina met desbeterfende tekening die geconforteerd moet worden in een QR code
    Deze moeten als volgt ingevoer worden (zie hieronder)
gt.QRread(Verdiepingsnummer,Bouwnummer,Webadres)
    Onder deze infotekst staat een voorbeeldcode die werkt.
    Speel deze code af en speel volgens DE QRgen.py code af.
    Dit genereerd de QR code van de desbetrefende appartement
"""

gt.QRread(3, 3.02, "https://web.edcontrols.com/#/projects/com_edcontrols_073ae146-3fa9-4f9b-aa78-12cd7f8abdb5/tickets?view=map&aggs_type=map&sort=last-modified&sort_dir=desc&aggs_value=946840a2e1a683be4f12bed0e66fd9d7&aggs_type=map&groupId=6089ea3378a17e863f7593d4c438cc50&mapId=946840a2e1a683be4f12bed0e66fd9d7")
