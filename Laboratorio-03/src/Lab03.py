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


def calculo_velocidad(grupo):
    distancia = np.sqrt((grupo['X'].diff(periods = 1))**2 + (grupo['Y'].diff(periods = 1))**2)
    tiempo = 1/25
    grupo['velocidad'] = distancia / tiempo
    return grupo





''' ARCHIVO 1 '''
def mi_programa_1():

    archivo_txt_01 ="UNI_CORR_500_01.txt"
    data_frame_01 = pd.read_csv(archivo_txt_01, delimiter="\t", skiprows = 3)

    grupo_01 = data_frame_01.groupby('# PersID', group_keys=False)
    df_vel_01 = grupo_01.apply(calculo_velocidad)
    #print(df_vel_01)

    #df_vel_01.to_csv(f"velocidades_01.csv", index=False, sep='\t')


    promedio_por_ID_01 = df_vel_01.groupby('# PersID')['velocidad'].mean()
    #print(promedio_por_ID_01)




    # Crear un histograma
    plt.hist(promedio_por_ID_01, bins=10, edgecolor='salmon', color='pink') 
    plt.xlabel('Promedio velocidad')
    plt.ylabel('Frecuencia')
    plt.title('Histograma UNI_CORR_500_01', loc='center', fontdict = {'fontsize':14,'fontweight':'bold','color':'black'})
    #plt.show() 

 
    # Crear Gráfico Caja Bigotes 10° Id
    data_sinNaN_01 = df_vel_01.dropna(subset=['velocidad'])

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.boxplot([data_sinNaN_01.loc[data_sinNaN_01['# PersID'] == i, 'velocidad']
                   for i in range(1, 11)])
    ax.set_xlabel('Id del Peatón')
    ax.set_ylabel('Velocidades')
    ax.set_title('Diagrama de Caja para 10 Peatones UNI_CORR_500_01')
    plt.xticks(range(1, 11), rotation=45)
    #plt.show() 

if __name__ == "__main__":
    print('|' + '*'*85 + '|')
    print('Los recursos utilizados por el programa 1 son con el data set "UNI_CORR_500_01.txt": ')
    get_resource_info(mi_programa_1)
    







''' ARCHIVO 2 '''
def mi_programa_2():

    archivo_txt_07 ="UNI_CORR_500_07.txt"
    data_frame_07 = pd.read_csv(archivo_txt_07, delimiter="\t", skiprows = 3)


    grupo_07 = data_frame_07.groupby('# PersID', group_keys=False)
    df_vel_07 = grupo_07.apply(calculo_velocidad)
    #print(df_vel_07)

    #df_vel_07.to_csv(f"velocidades_07.csv", index=False, sep='\t')

    promedio_por_ID_07 = df_vel_07.groupby('# PersID')['velocidad'].mean()
    #print(promedio_por_ID_07)


    # Crear un histograma

    plt.hist(promedio_por_ID_07, bins=10, edgecolor='teal', color='lightblue')  
    plt.xlabel('Promedio velocidad')
    plt.ylabel('Frecuencia')
    plt.title('Histograma UNI_CORR_500_07', loc='center', fontdict = {'fontsize':14,'fontweight':'bold','color':'black'})
    #plt.show()


    
    # Crear el gráfico de caja para los 10 primeros IDs
    data_sinNaN_07 = df_vel_07.dropna(subset=['velocidad'])

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.boxplot([data_sinNaN_07.loc[data_sinNaN_07['# PersID'] == i, 'velocidad']
               for i in range(1, 11)])
    ax.set_xlabel('Id del Peatón')
    ax.set_ylabel('Velocidades')
    ax.set_title('Diagrama de Caja para 10 Peatones UNI_CORR_500_07')
    plt.xticks(range(1, 11), rotation=45)
    #plt.show()

if __name__ == "__main__":
    print('|' + '*'*85 + '|')
    print('Los recursos utilizados por el programa 2 son con el data set "UNI_CORR_500_07.txt": ')
    print('')
    get_resource_info(mi_programa_2)
    print('|' + '*'*85 + '|')