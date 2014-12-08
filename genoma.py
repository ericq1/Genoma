import re
genoma = open("RF00059_vs_UTR_Todas_sp_unicas","r")
dtt = open("UTR_Todas_sp_unicas_linea.txt","r")

print("Analizando los archivos, espere un momento")

dt = re.compile('\d\d[.]\d')
lista = re.compile('[a-zA-Z][a-zA-Z][a-zA-Z][-][a-zA-Z][a-zA-Z][a-zA-Z][^ ]*')
mt = []
for line in genoma:
    score = re.findall(dt,line)
    datos = (re.findall(lista,line))
    if len(score) > 0:
        if float(score[0]) >= 35.8:
            if len(datos) >0:
                for x in mt:
                    if x == []:
                        mt.remove(x)
                mt.append(datos[0])
wlistos = list(set(mt))
documento = open("documento.txt", "w")
secuenncia = []
for i in dtt:
    secuenncia.append(i)
for ident in wlistos:
    siguiente = False
    for seq in secuenncia:
        if siguiente:
            documento.write(ident+ ", " + seq)
            siguiente = False
            break
        if ident in seq:
            siguiente = True
genoma.close()
dtt.close()
input("Datos guardados satisfactoriamente en documento.txt")
