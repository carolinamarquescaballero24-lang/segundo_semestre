for curso in range(1,5):
    asistieron=0
    falta=0
    print(f"--CURSO--{curso}")
    for estudiante in range(1,7):
         asistencia =int(input(f"Estudiante {estudiante} :"))
         if asistencia ==1:
             asistieron=asistieron+1
         else:
             falta=falta+1
    print(f"Asistieron {asistieron} faltaron {falta}")