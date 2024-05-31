from ggplot import ggplot, aes, geom_bar, theme, element_text, labs
import pandas as pd

fakultas = ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"]
jumlah_mahasiswa = [260, 28, 284, 465, 735]
akreditasi = ["A", "A", "B", "A", "A"]

info_mahasiswa = pd.DataFrame({'fakultas': fakultas, 'jumlah_mahasiswa': jumlah_mahasiswa, 'akreditasi': akreditasi})

gambar = ggplot(info_mahasiswa, aes(x='fakultas', y='jumlah_mahasiswa', fill='fakultas')) + \
    geom_bar(stat='identity', width=1) + \
    theme(axis_text_x=element_text(angle=45, hjust=1)) + \
    labs(x='Fakultas', y='Jumlah Mahasiswa', title='Jumlah Mahasiswa per Fakultas')

print(gambar)
