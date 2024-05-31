import pandas as pd

df = pd.read_excel('/root/Machine-Learning/UTS/dataset_ml.xlsx')

print(df.head(7))

print('\n--------------------------------------------\n')

rata_rata_datang = df['Datang'].mean()
print(f'a) Rata-rata Mahasiswa Datang: {rata_rata_datang}\n')

hari_terboros = df['Biaya'].idxmax()
print(f'b) Hari terboros: {df.loc[hari_terboros, "Hari"]} dengan biaya {df.loc[hari_terboros, "Biaya"]}\n')

hari_biaya_110k = df[df['Biaya'] > 110000]['Hari']
print(f'c) Hari dengan biaya lebih dari 110.000: {hari_biaya_110k.values}\n')

mahasiswa_rajin = df['Datang'].idxmax()
print(f'd) Mahasiswa yang paling banyak datang:\n{df.loc[mahasiswa_rajin, "Mahasiswa"]}\n')

mahasiswa_minggu = df[df['Hari'] == 'Minggu']['Mahasiswa']
print(f'e) Mahasiswa yang datang di hari Minggu:\n{mahasiswa_minggu.values}\n')

hari_biaya_tertinggi = df.loc[df['Biaya'].idxmax(), 'Hari']
hari_biaya_terendah = df.loc[df['Biaya'].idxmin(), 'Hari']
print(f'f) Hari dengan biaya tertinggi: {hari_biaya_tertinggi}, dan terendah: {hari_biaya_terendah}\n')

hari_ramai = df.loc[df['Datang'].idxmax(), 'Hari']
hari_sepi = df.loc[df['Datang'].idxmin(), 'Hari']
print(f'g) Hari ramai: {hari_ramai}, dan sepi: {hari_sepi}\n')
