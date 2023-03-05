#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import fileinput
import os

# Determinamos el número de serie del próximo enrutador
openfile = open('Mikrotik_backuper.sh')
readfile = openfile.read()
pattern = 'router\\d+'
all_router = re.findall(pattern, readfile)
numbers = list(map(lambda x: x[6:], all_router))
tru_numbers = list(set(list(map(int, numbers))))
a = str(max(tru_numbers) + 1)
openfile.close()
# Aquí es donde se reciben los datos
ipset = str(input('Enter Ip ->: '))
ippasswd = str(input('Enter password ->: '))
ipname = str(input('Enter router name ->: '))
# Luego viene la plantilla, que se pasa al script principal
tamplate_stat = str('=$(netcat -w3 -z ' + '$IP' + a + ' $PRT && echo success || echo fail)')
tamplate_name = '  router' + a + '\n' + '# NEWNAME'
tamplate_variable = (
                            'IP' +
                            a +
                            "='" +
                            ipset +
                            "'"
                    ) + \
                    '\r' + \
                    (
                            'PASS' +
                            a +
                            "='" +
                            ippasswd +
                            "'"
                    ) + \
                    '\r' + \
                    (
                            'NAME' +
                            a +
                            "='" +
                            ipname +
                            "'"
                    ) + \
                    '\r' + \
                    (
                            'status' +
                            a +
                            tamplate_stat
                    ) + \
                    '\r' + \
                    )
                            '#'
                    ) + \
                    '\r' +\
                    (
                            '#NEWVARIABLE'
                    )
tamplate_func = (
                        'function router' + a + ' {' + '\r'
                ) + \
                (
                        'echo "  ___________________________________________________' + ' \r'
                ) + \
                (
                        '  Start $IP' + a + ' ($NAME' + a + ')..."' + '\r'
                ) + \
                (
                        'if [ $status' + a + ' = $gg ]' + '\r'
                ) + \
                (
                        'then' + '\r'
                ) + \
                (
                        '  echo "' + '\r'
                ) + \
                (
                        '  Status $IP' + a + ' - OK, create backup:' + '\r'
                ) + \
                (
                        '  "' + '\r'
                ) + \
                (
                        '  sshpass -p $PASS' + a + ' ssh -T -p $PRT $LGIN@$IP' + a + ' << EOF' + '\r'
                ) + \
                (
                        'export file=$IP' + a + '$NAME' + a + '\r'
                ) + \
                (
                        'system backup save name=$IP' + a + '$NAME' + a + '\r'
                ) + \
                (
                        'quit' + '\r'
                ) + \
                (
                        'EOF' + '\r'
                ) + \
                (
                        'echo "' + '\r'
                ) + \
                (
                        "  Lockal save backup's..." + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'sshpass -p $PASS' + a + ' scp -P $PRT ' + '$LGIN@$IP' + a + '":/$IP' + a + '$NAME' + a + '.rsc" $DIR' + '\r'
                ) + \
                (
                        'sshpass -p $PASS' + a + ' scp -P $PRT $LGIN@$IP' + a + '":/$IP' + a + '$NAME' + a + '.backup"' + ' $DIR' + '\r'
                ) + \
                (
                        'echo "' + '\r'
                ) + \
                (
                        '  Limpiando el directorio del enrutador...' + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'sshpass -p $PASS' + a + ' ssh -T -p $PRT $LGIN@$IP' + a + ' << EOF' + '\r'
                ) + \
                (
                        'file remove "$IP' + a + '$NAME' + a + '.rsc"' + '\r'
                ) + \
                (
                        'file remove "$IP' + a + '$NAME' + a + '.backup"' + '\r'
                ) + \
                (
                        'quit' + '\r'
                ) + \
                (
                        'EOF' + '\r'
                ) + \
                (
                        'echo "' + '\r'
                ) + \
                (
                        '$IP' + a + ' END' + '\r'
                ) + \
                (
                        '  ___________________________________________________' + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'else' + '\r'
                ) + \
                (
                        '  echo "' + '\r'
                ) + \
                (
                        '  ...................................................' + '\r'
                ) + \
                (
                        '  ERROR $IP' + a + ' ($NAME' + a + '),' + '\r'
                ) + \
                (
                        "  la copia de seguridad no puede crear y guardar" + '\r'
                ) + \
                (
                        '  ...................................................' + '\r'
                ) + \
                (
                        '  ___________________________________________________' + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'fi' + '\r'
                ) + \
                (
                        '}' + '\r'
                ) + \
                (
                    '#' + '\r'
                ) + \
                (
                    '#NEWFUNK'
                )
# El siguiente código en realidad cambia el script principal ('.backup' se agrega al archivo original)
with fileinput.FileInput('Mikrotik_backuper.sh', inplace=True, backup='.backup') as file:
    for line in file:
        line = line.rstrip()
        print(tamplate_variable if line == '#NEWVARIABLE' else line)
with fileinput.FileInput('Mikrotik_backuper.sh', inplace=True, backup='.backup2') as file:
    for line in file:
        line = line.rstrip()
        print(tamplate_func if line == '#NEWFUNK' else line)
os.unlink('Mikrotik_backuper.sh' + '.backup2')
with fileinput.FileInput('Mikrotik_backuper.sh', inplace=True, backup='.backup3') as file:
    for line in file:
        line = line.rstrip()
        print(tamplate_name if line == '# NEWNAME' else line)
os.unlink('Mikrotik_backuper.sh' + '.backup3')
