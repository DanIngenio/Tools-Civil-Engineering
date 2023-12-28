# Herramienta para representar derivas de un edifico 

###################################################################
# 1. Importar Librerias 
import numpy as np
import matplotlib.pyplot as plt

###################################################################
# 2. Importar Derivas del Edificio
Dxe=[0.001606,0.002606,0.003513,0.003939,0.004412,0.004688,0.004381,0.003267,8.3E-05,5.1E-05,4.8E-05,0]
Dxe=np.array(Dxe)*0.6

Dye=[0.001563,0.002635,0.003629,0.004139,0.004668,0.004976,0.004651,0.003396,6.3E-05,3.7E-05,3.6E-05,0]
Dye=np.array(Dye)*0.6

Niveles=[35,31.8,28.6,25.4,22.2,19,15.8,12.6,9,6,3,0]
Niveles=np.array(Niveles)

R=8
Dxi=0.75*R*Dxe*100
Dyi=0.75*R*Dye*100

Dmax=2
###################################################################
# 3. Crear Grafica 

fig = plt.figure(constrained_layout = True,figsize=(10,6))
gs = fig.add_gridspec(1, 2)

ax1 = fig.add_subplot(gs[:,0:1])
ax1.plot(Dxi,Niveles, color='blue',ls = "-.",lw=2,label=str(max(Dxi.round(1))) +' %')
ax1.scatter(Dxi,Niveles, marker='o',color='blue')
ax1.axvline(x=Dmax, ymin=0, ymax=1,label='2.0 %',color='black',ls = "--",lw=2)

ax1.set_title('Deriva Inelástica Dir_x', color='black', fontsize=16)
ax1.set_ylabel('Altura [m]', color='black', fontsize=12)
ax1.set_xlabel('Drift[%]', color='black', fontsize=12)
ax1.legend()
ax1.grid(alpha=0.5)



ax2 = fig.add_subplot(gs[:,1:2])
ax2.plot(Dyi,Niveles, color='red',ls = "-.",lw=2,label=str(max(Dyi.round(1))) +' %')
ax2.scatter(Dyi,Niveles, marker='o',color='red')
ax2.axvline(x=Dmax, ymin=0, ymax=1,label='2.0 %',color='black',ls = "--",lw=2)

ax2.set_title('Deriva Inelástica Dir_y', color='black', fontsize=16)
ax2.set_ylabel('Altura [m]', color='black', fontsize=12)
ax2.set_xlabel('Drift[%]', color='black', fontsize=12)
ax2.legend()
ax2.grid(alpha=0.5)

plt.savefig("Derivas_ED01.jpg",dpi=1080) # Guardar en formato de imagen
plt.show()
