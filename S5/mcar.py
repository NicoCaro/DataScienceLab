'''
Implementacion del test de Little para verificar si un dataset posee informacion
faltante segun el mecanismo MCAR.

Autor: Nicolas Caro

Observacion: Es una mala practica sobre-comentar codigo, en este modulo se 
hace esto de manera explicita por fines didacticos.
'''

import scipy.stats as stats
import numpy as np

def little_mcar(data):
    '''Impementacion del test MCAR de Little.
    
    Separa cada columna en grupos, segun el patron de perdida de
    informacion, para cada grupo calcula la media de informacion 
    completa (requiere hipotesis de normalidad en las columnas).
    Calcula la matriz de covarianza para las variables por 
    agrupacion con informacion completa. Finalemte calcula
    el estadistico (chi-cuadrado) de test y entrega su valor,
    los grados de libertad y el valor p.
    
    Args:
    -----
    data: Pandas DataFrame
        Un dataframe con valores faltantes
    
    Returns:
    --------
    
    d_2 : float
         Valor del estadisitico de prueba.
    
    deg_f: int
        Grados de libertad,
    
    p_value: float
        Valor p asociado al estadistico y grados de libertad.
    '''

    # Se copia el dataframe para evitar problemas de mutabilidad
    df = data.copy()

    # Se calcula el numero de variables en el dataset
    n_var = df.shape[1]

    # Se calcula la matriz indicadora de informacion faltante
    R = 1 * df.isnull()
    
    '''
    A cada patron de informacion faltante se asgina una llave, 
    por ejemplo, si el patron es del tipo:
    
    1 0 0 0 0 
    
    se asgina la llave 
    
    (1,0,0,0,0)
    
    De esta forma se diferencian patrones de perdida de informacion.
    posteriormente se generan grupos por columna basandose en esas
    llaves.
    '''

    R['signature'] = R.apply(tuple, axis=1)

    # Media: Implementar su estimador de maxima verosimilitud
    gmean = df.mean()

    # Covarianza del dataset: ignora valores faltantes
    gcov = df.cov()

    # propaga las llaves al dataset procesado
    df['signature'] = R['signature']

    # Se identifican los patrones unicos
    R.drop_duplicates(inplace=True)

    # Se asgina un codigo (int) a cada patron unico
    n_patterns = len(R)
    R['patterns'] = np.arange(n_patterns)

    # Se Genera un mapping del tipo llave -> codigo
    to_map = R[['signature', 'patterns']].values
    mapping = dict(to_map)

    # Se aplica el mapping para propagar codigos al dataset procesado
    df['patterns'] = df['signature'].map(mapping)

    # Agrupacion por patrones
    grouped = df.groupby('patterns')

    # Medias de cada columna por patron
    mu_j = grouped.mean()

    # Vector de cantidad de elementos por patron
    N_j = grouped['signature'].count()

    # Se elimina la llave, se mantienen solo los codigos
    df.drop('signature', axis=1, inplace=True)

    # Se obtienen subdatasets asociados a cada patron
    groups = (grouped.get_group(i) for i in range(n_patterns))

    # Se limpian eliminando la columna patterns y los valores faltantes
    groups = map(lambda x: x.dropna(axis=1), groups)
    groups = map(lambda x: x.drop('patterns', axis=1), groups)
    
    '''
    Con la agrupacion anterior se obtienen las variables 
    con informacion completa por patron
    '''
    
    full_info_vars = [g.columns for g in groups]

    #Se calculan las covarianzas de informacion completa por patron
    covs = (gcov.loc[var, var] for var in full_info_vars)

    # Se inveierten las covarianzas de manera eficiente
    inverter = lambda cov: np.linalg.solve(cov, np.identity(cov.shape[1]))
    sigma_inv = tuple(map(inverter, covs))

    # Se obtienen las medias con informacion completa por variable
    means_diff = mu_j - gmean
    means_diff = [means_diff.loc[n].dropna() for n in means_diff.index]

    # Se calcula (mu_j - mu_j^{ML}).T Sigma^{-1} (mu_j - mu_j^{ML})
    weights= map(lambda x: (x[0].T @ x[1]) @ x[2],
                       zip(means_diff, sigma_inv, means_diff))
    
    weights = np.array(tuple(weights))

    # Se obtienen los valores de interes (se calcula la suma)
    chi_stat = N_j.dot(weights) # estadistico d^2
    deg_f = N_j.sum() - n_var # grados de libertad

    p_value = 1 - stats.chi2.cdf(chi_stat,deg_f)

    return {'chi_stat': chi_stat, 'deg_f': deg_f, 'p_value': p_value}