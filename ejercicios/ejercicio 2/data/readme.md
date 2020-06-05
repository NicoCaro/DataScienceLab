# Descripción de datos

**I. Variables explicativas:**  


A. Datos del cliente bancario:

1. **age**: segmentos de edad (catégorica y creciente).
2. **job**: tipo de trabajo (categórica: admin., obrero, emprendedor, empleado doméstico, gerencia, jubilado, cuenta propia, servicios, estudiante, técnico, desempleado, desconocido)
3. **marital**: estado civil (categórica: divorciado, casado, soltero, desconocido; nota: divorciado significa divorciado o viudo)
4. **education**: (categórica: primaria, secundaria, terciaria y desconocida)
5. **default**: ¿tiene crédito en incumplimiento? (binaria)
6. **housing**: tiene préstamo de vivienda? (binaria)
7. **loan**: tiene préstamo personal? (binaria)
8. **balance**: equilibrio del individuo.
    
B. Relacionado con el último contacto de la campaña actual:

9. **contact**: tipo de comunicación de contacto (categórica: celular, teléfono)
10. **month**: último mes del año de contacto (categórica: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
11. **day_of_week**: día de la semana del último contacto  (categórica)
12. **duration**: duración del último contacto, en segundos (numérico). Nota importante: este atributo afecta en gran medida el objetivo de salida (por ejemplo, si duración = 0, entonces y = 'no').
13. **campaign**: número de contactos realizados durante esta campaña y para este cliente (numérico, incluye el último contacto)

C. Otros atributos:

14. **pdays**: número de días que pasaron después de que el cliente fue contactado por última vez desde una campaña anterior (numérico; 0 significa que el cliente no fue contactado previamente)
15. **previous**: número de contactos realizados antes de esta campaña y para este cliente (numérico)
16. **poutcome**: resultado de la campaña de marketing anterior (categórica: fracaso, inexistente, éxito)

**II. Variable objetivo:**
17. **deposit**: ¿el cliente ha suscrito un depósito a plazo luego de la llamada? (binaria)