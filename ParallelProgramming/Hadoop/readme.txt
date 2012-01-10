На моей host-машине с Ubuntu 11.04:
1. Поставил в VirtualBox Ubuntu Server 11.10 (user:password30).
2. Настроил в Ubuntu Server 11.10 PXE Boot Server (DHCP, TFTP, NFS).
   http://www.serenux.com/2010/05/howto-setup-your-own-pxe-boot-server-using-ubuntu-server/
   http://www.serenux.com/2010/05/howto-get-an-ubuntu-live-cd-to-boot-off-a-pxe-server/
   http://blogs.sourceallies.com/2010/02/ubuntu-live-network-boot-using-pxe/
   PXELinux from here: http://archive.ubuntu.com/ubuntu/dists/oneiric/main/installer-amd64/current/images/netboot/netboot.tar.gz
3. Собрал из Ubuntu Mini Remix <http://www.ubuntu-mini-remix.org/> 11.04 с 
   помощью Ubuntu Customization Kit <http://uck.sourceforge.net/> 
   модифицированный Live образ Ubuntu, подходящий для сетевой раздачи и 
   выполняющий необходимые операции по копированию с сервера скриптов 
   инициализации и их запуска.
4. Настроил Hadoop на Ubuntu Server и раздал его на всех клиентов, 
   загружающихся с live дистрибутива.

Сценарий использования: 
1) прийти в лабораторию СПбГПУ;
2) подключить ноутбук с Ubuntu Server, вытащенным наружу через bridget adaptor;
3) перезагрузить каждый компьютер лаборатории и включить на нём загрузку по 
   сети в BIOS.
4) ??? 
   (машины загружаются и регистрируются на сервере; на сервере инициируется
   запуск служб Hadoop для всех подключенных компьютеров; запускается решение 
   задачи на развёрнутом кластере)
5) PROFIT

Возникшие проблемы:
1. На машинах в лаборатории СПбГПУ от 512 до 768 МБ оперативной памяти, чего 
   недостаточно для загрузки Live образа полностью в память. Пришлось 
   загружаться по NFS, что, к моему удивлению, не замедлило работу кластера в 
   целом (использовалось 8 компьютеров лаборатории).
2. Для хранения файлов HDFS я использовал первый раздел жесткого диска рабочей 
   машины, на котором есть хотя бы 10 ГБ свободного места. Такой раздел, 
   естественно, имел NTFS. Мне не удалось запустить HDFS на NTFS --- Hadoop 
   постоянно ругался на неправильные права файлов (естественно, они не 
   поддерживаются драйвером NTFS), опция игнорирования прав в настройках не 
   помогла.
