#Mrpi314 programming
#Modes: Windows, Crowpi2, or Simple.
mode='Windows'
if mode == 'Windows':
    import Python.UC37_Windows as UC37
elif mode == 'Crowpi2':
    import Python.UC37_full as UC37
elif mode == 'Simple':
    import Python.UC37_mini.py as UC37