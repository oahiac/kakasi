from pykakasi import kakasi

kakasi = kakasi()
kakasi.setMode('J', 'H')  # J(Kanji) to H(Hiragana)
conv = kakasi.getConverter()
a=[]
for line in open("kanji.txt"):
	a.append(line.strip()+'\t\t\t\t\t'+conv.do(line)+'\n')
f=open('final.txt','a',encoding='utf-8')
f.writelines(a)
f.close()