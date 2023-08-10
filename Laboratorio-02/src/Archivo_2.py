import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import psutil

### CUANTOS RECURSOS CONSUME EL PROGRAMA ###
def get_resource_info(code_to_measure):
    resources_save_data = get_resource_usage(code_to_measure=code_to_measure)
    print(f"Tiempo de CPU: {resources_save_data['tiempo_cpu']} segundos")
    print(f"Uso de memoria virtual: {resources_save_data['memoria_virtual']} MB")
    print(f"Uso de memoria residente: {resources_save_data['memoria_residente']} MB")
    print(f"Porcentaje de uso de CPU: {resources_save_data['%_cpu']} %")

def get_resource_usage(code_to_measure):
    process = psutil.Process()
    #get cpu status before running the code
    cpu_percent = psutil.cpu_percent()
    start_time = time.time()
    code_to_measure()
    end_time = time.time()
    end_cpu_percent = psutil.cpu_percent() 
    cpu_percent = end_cpu_percent - cpu_percent
    cpu_percent = cpu_percent / psutil.cpu_count()
    
    return {
        'tiempo_cpu': end_time - start_time,
        'memoria_virtual': process.memory_info().vms / (1024 * 1024),  # Convertir a MB
        'memoria_residente': process.memory_info().rss / (1024 * 1024),  # Convertir a MB
        '%_cpu': cpu_percent # Porcentaje de uso de CPU
    }



'''  PROGRAMA 1  '''
def mi_programa_1():

    #Extraer lineas y separarlas por espacio
    f = open('UNI_CORR_500_07.txt', 'r')
    
    crd = []
    coordenadas =[]
    for line in f.readlines():
        extraer = line[0:29]
        aux = extraer.split()
        crd.append(aux)
    f.close()


    #Identificar las coordenadas y agregarlas a las listas requeridas más adelante
    for n in range (4, len(crd)):
        ListAux = crd[n]
        a = []
        X = ListAux[2]
        Y = ListAux[3]
        Z = ListAux[4]
   
        #agregar las coordenadas X, Y y Z a una lista auxiliar a (PARTE 1)
        a.append(float(X))
        a.append(float(Y))
        a.append(float(Z))
        #agregar la lista auxiliar a como sublista (PARTE 1)
        coordenadas.append(a)
        
        
    #Coordenadas X,Y que mas se repiten
    FrecuenciasXY = {tuple(coord[0:2]): 0 for coord in (coordenadas)}

    for coord in coordenadas:
        coordenadaXY = tuple(coord[0:2])
        FrecuenciasXY[coordenadaXY]+=1
    

    ix = 320
    iy = 480
    mx = (640-ix)/9
    my = (0-iy)/5
    Xpixel = []
    Ypixel = []

    
    #Conversion coordenada metro a pixel
    def Conversion(CoordenadaM):
        Xmetro, Ymetro = CoordenadaM
        Xpixel = int(mx * Xmetro + ix)
        Ypixel = int(my * Ymetro + iy)
        return Xpixel , Ypixel


    #Diccionario frecuencia de posiciones en pixel
    FrecuenciaPixel = {(ValX, ValY): 0 for ValX in range(641)for ValY in range (481)}


    #Pasar metro a pixel en el diccionario
    for coordenada, frecuencia in FrecuenciasXY.items():
        CoordenadaPixel = Conversion(coordenada)
        Xpixel.append(CoordenadaPixel[0])
        Ypixel.append(CoordenadaPixel[1])
        #print(f'La coordenada metrica: {coordenada} pasa a pixel {CoordenadaPixel}' )
        FrecuenciaPixel[CoordenadaPixel] = frecuencia
    print('')


    #Coordenadas X, Y que mas se repiten en pixel
    max_FrecuPixelXY = max(FrecuenciaPixel.values())
    XYPixel_mas_repetida = [CordXY for CordXY, frecuenciaXY in FrecuenciaPixel.items() if frecuenciaXY == max_FrecuPixelXY]
    

    ### GRAFICAR MAPA DE CALOR ###

    bins = 50

    heatmap, xedges, yedges = np.histogram2d(Xpixel, Ypixel, bins=bins)

    heatmap = heatmap.T

    x_extent = [0, 640]
    y_extent = [480, 0]

    plt.imshow(heatmap, extent=[x_extent[0], x_extent[1], y_extent[0], y_extent[1]], cmap='plasma')
    plt.colorbar(label='Frecuencia')
    plt.title('Frecuencia de peatones (Histograma 2D)', loc='center', fontdict = {'fontsize':14,'fontweight':'bold','color':'indigo'})
    plt.xlabel('Coordenada X', fontdict={'fontsize':8})
    plt.ylabel('Coordenada Y', fontdict={'fontsize':8})
    

if __name__ == "__main__":
    print('|' + '*'*85 + '|')
    print('Los recursos utilizados por el programa 1 son con el data set "UNI_CORR_500_07.txt": ')
    get_resource_info(mi_programa_1)
plt.show()

print('')





''' PROGRAMA 2 '''
def mi_programa_2():

    archivo_txt ="UNI_CORR_500_07.txt"
    data_frame = pd.read_csv(archivo_txt, delimiter="\t", skiprows = 3)
    
    
    plt.hist2d(data_frame['X'], data_frame['Y'], bins=(50, 50), cmap=plt.cm.plasma)
    plt.colorbar(label='Frecuencia')
    plt.title('Frecuencia de peatones (Histograma 2D)', loc='center', fontdict = {'fontsize':14,'fontweight':'bold','color':'indigo'})
    plt.xlabel('Coordenada X', fontdict={'fontsize':8})
    plt.ylabel('Coordenada Y', fontdict={'fontsize':8})

if __name__ == "__main__":
    print('|' + '*'*85 + '|')
    print('Los recursos utilizados por el programa 2 son con el data set "UNI_CORR_500_07.txt": ')
    print('')
    get_resource_info(mi_programa_2)
    print('|' + '*'*85 + '|')
plt.show()