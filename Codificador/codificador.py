#Abrir archivo
import  numpy as np
import scipy.io
import binascii


def codificador(path):
     f = open(path, "r")
     vk = f.read()
     f.close()
     #Leemos el archivo
     vt = []
     bkt=[]
     bft=''
     #Separamos los elementos en la lista vk
     for k in range(len(vk)):
         vt.append(vk[k])
     #Pasar cada elemento a binario y lo almacenamos en bkt
     for k in range(len(vt)):
         bkt.append(  bin(int.from_bytes(vt[k].encode(), 'big')) )
         bkt[k]= bkt[k].replace('0b','')
     #Verificamos que todos los elementos en bkt tengan el mismo largo
     for k in range(len(bkt)):
         if(int(len(bkt[k])) < 8):
             while(int(len(bkt[k])) < 8):
                 bkt[k]='0'+bkt[k]
     #Unimos los elementos en una misma linea
     for k in range(len(bkt)):
          bft +=bkt[k]
     return bft

#Decodificador
def decodificador(bft):
     bfr = bft
     bkr= []
     vr=[]
     out =''
     #Separamos bfr en espacios de 8 bits
     for k in range(0,len(bfr),8):
         bkr.append(bfr[k:k+8]) 
     #Convertimos cada elemento de bkr a su codigo ascii
     for k in range(len(bkr)):
         vr.append(chr(int(bkr[k], 2)))  
     #Juntamos todo en una misma cadena
     for k in range(len(vr)):
         out+=str(vr[k])

     return(out)





