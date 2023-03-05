#!/usr/bin/env bash
#
#
# Tenga en cuenta que para el correcto funcionamiento
# necesitará las utilidades que se encuentran aquí
#
#
DIR=                   # example: DIR=/home/user/backups/
LGIN=                  # example: LGIN=admin 
PRT=                   # example: PRT=22
#SHELF=                # example: SHELF=13
#
DATE=$(echo `date +%Y.%m.%d`)
exec 2>> $DIR$DATE".log"
gg=success
#
##### NO ELIMINAR COMENTARIOS EN EL BLOQUE DE ABAJO #####
#
# router0               
#
#NEWVARIABLE
#
#NEWFUNK
#
function startsaver {
# NEWNAME
}
#
startsaver >> $DIR$DATE.log
#
##### NO ELIMINAR COMENTARIOS EN EL BLOQUE ANTERIOR #####
#
#
#
##### ARCHIVO DE COPIAS DE SEGURIDAD Y ELIMINACIÓN DE VERSIONES ANTIGUAS #####
#
statsave=$(cat $DIR$DATE.log | grep "ERROR \| failed \| denied \| error \| Permission" && echo ERROR || echo success )
#
function archandel {
echo "

  _______________________________
  Se inició el archivado de las copias de seguridad recopiladas:"
if [ "$statsave" = "$gg" ]
  then
    zip -9 -j $DIR$DATE.zip $DIR*.backup $DIR*rsc
    rm $DIR*.backup $DIR*.rsc
#    echo "
#    search and delete old versions"
#    find "$DIR"2* -mtime +$SHELF -delete
    echo "
  Archiving done
  _______________________________"
  else
    echo "  ...............................
                ERROR
     no se reciben todas las copias de seguridad
              comprobar la corrección
              de los datos ingresados
                y leer el registro!
     ......................................"
    zip -9 -j $DIR$DATE"_brocken".zip $DIR*.backup $DIR*rsc
    rm $DIR*.backup $DIR*.rsc
    echo "  _______________________________"
fi
}
#
archandel >> $DIR$DATE.log
#####_____________________________________________#####
#
#
#
##### AJUSTES DE ALERTAS DE TELEGRAM #####
#TOKEN=
#IDCHAT=
#URL="https://api.telegram.org/bot$TOKEN/sendMessage"
##PROXYSOCKS=
##TGMESS="curl --silent --show-error --fail -k -G -o /dev/null -x socks5://${PROXYSOCKS} ${URL} -d chat_id=${IDCHAT} "
#TGMESS="curl --silent --show-error --fail -k -G -o /dev/null $URL -d chat_id=$IDCHAT "
#Function alerts
#function alert {
#  echo "  _______________________________
#  Se generan alertas"
#if [ "$statsave" = "$gg" ]
#  then
#    $TGMESS --data-urlencode "text=Creation of backups $DATE was successful"
#    echo "FIN
#  _______________________________"
#  else
#    $TGMESS --data-urlencode "text=An error occurred while creating backups, check the $DATE log"
#    echo "FIN
#  _______________________________"
#fi
#}
#####_________________________#####
#alert >> $DIR$DATE.log
