'''
A megadott halmazok alapján a program értékelje ki, és az eredményt jelenítse meg a képernyőn
az alábbiakat vizsgálva:
- hány olyan étel van, amit mind a két gyerek szeret, és melyek ezek,
- melyek azok az ételek, amiket Peti szeret, de Kriszti nem,
- melyek azok az ételek, melyeket csak egyikük szeret!
'''
Peti_kedvencei = {'halászlé', 'bécsi szelet', 'bukta', 'rakott krumpli', 'almás rétes' }
Kriszti_kedvencei = {'borsóleves', 'bécsi szelet', 'túrós tészta', 'lecsó', 'almás rétes' }

print(f'{len(Peti_kedvencei & Kriszti_kedvencei)} db olyan étel van, amit mind a két gyerek szeret.')
print(Peti_kedvencei & Kriszti_kedvencei)
print('\n')
print(f'{len(Peti_kedvencei - Kriszti_kedvencei)} db olyan étel van, amiket Peti szeret, de Kriszti nem.')
print(Peti_kedvencei - Kriszti_kedvencei)
print('\n')
print(f'{len((Peti_kedvencei | Kriszti_kedvencei) - (Peti_kedvencei & Kriszti_kedvencei))} db olyan étel van, melyeket csak egyikük szeret!.')
print((Peti_kedvencei | Kriszti_kedvencei) - (Peti_kedvencei & Kriszti_kedvencei))
print('\n')
