---
layout: post
title:  "Шпаргалка по установке OpenBSD"
date:   2021-01-23 10:00:00 +0000
categories: OpenBSD
---
## Предисловие
Пора уже написать шпаргалку по установке OpenBSD. Раскатывать её приходится только со свежим релизом, а к тому времени всё уже забывается.

OpenBSD 6.7 я буду ставить на стационарный компьютер, выполняющий роль билд-машины. Компьютер подключен проводом к домашней сети, в которой есть dhcp-сервер (на роутере). Домен в сети не поднят.

## Загрузка и установка
Скачать OpenBSD следует с [сайта OpenBSD][1].

Образ записать на флешку. Настроить на компьютере загрузку с флешки. Загрузиться с флешки и начать установку.

## Примечания к установке

Ниже будут приведены два блока, в первом - краткий листинг с вариантами, во втором - полный листинг, но без учёта особенностей моей системы. В квадратный скобках в конце каждой строки написан вариант по-умолчанию, который будет выбран при нажатии enter. 

### Краткий вариант

В кратком варианте, жирным шрифтом, указаны варианты выбранные при конфигурирования моей системы.

Choose your keyboard layout ('?' or 'L' for list) [default] **default**

System hostname? (short form, e.g. 'foo') **my_comp_name**

Which network interface do you wish to configure? (or 'done') [fxp0] **fxp0**

IPv4 address for fxp0 (or 'dhcp' or 'none') [dhcp] **dhcp**

IPv6 address for fxp0 (or 'autoconf' or 'none') [none] **none**

Which network interface do you wish to configure? (or 'done') [done] **done**

DNS domain name? (e.g. 'example.com') [my.domain] **my.domain**

Password for root account? (whill note echo) _

Password for root account? (again) _

Start sshd(8) by default? [yes] **yes**

Do you expect to run the X Window System? [yes] **no**

Change the default console to com8? [no] **no**

Setup a user? (enter a lower-case loginname, or 'no') [no] **user1**

Full name for user user1? [user1] **User User**

Password for user user1? (whill note echo) _

Password for user user1? (again) _

Allow root ssh login? (yes, no, prohibit-password) [no] **no**

What timezone are you in? ('?' for list) [Asia/Yekaterinburg] **Asia/Yekaterinburg**

Which disk is the root disk? ('?' for details) [wd0] **wd0**

Use (W)hole disk MBR, whole disk (G)PT, (O)penBSD area or (E)dit? [OpenBSD] **W**

Use (A)uto layout, (E)dit auto layout, or create (C)ustom layout? [a] **A**

Location of sets? (disk http nfs or 'done') [http] **http**

HTTP proxy URL? (e.g. `'http://proxy:8080'`, or 'none') [none] **none**

HTTP Server? (hostname, list#, 'done' or '?') **cdn.openbsd.org**

Set name(s)? (or 'about' or 'done') [done] **done**

Location of sets? (disk http nfs or 'done') [done] **done**

Exit to (S)hell, (H)alt or (R)eboot? [reboot] **H**

### Полный вариант

В полном варианте я постарался отразить весь необходимый листинг, который был в этот момент на экране. 

```

Welcome to the OpenBSD/amd64 6.7 installation program.
(I)nstall, (U)pgrade, (A)utoinstall or (S)hell? I

Choose your keyboard layout ('?' or 'L' for list) [default]

System hostname? (short form, e.g. 'foo') my_comp_name

Which network interface do you wish to configure? (or 'done') [fxp0]
IPv4 address for fxp0 (or 'dhcp' or 'none') [dhcp] dhcp
fxp0: 192.168.0.14 lease accepted from 192.168.0.1 (e4:cb:11:97:c9:30)
IPv6 address for fxp0 (or 'autoconf' or 'none') [none] none
Availble network interface are: fxp0 nfe0 vlan0.
Which network interface do you wish to configure? (or 'done') [done]
DNS domain name? (e.g. 'example.com') [my.domain] my.domain
Using DNS nameservers at 192.168.0.1

Password for root account? (whill note echo) _
Password for root account? (again)
Start sshd(8) by default? [yes]
Do you expect to run the X Window System? [yes] no
Change the default console to com8? [no]
Setup a user? (enter a lower-case loginname, or 'no') [no] user1
Full name for user user1? [user1] User User
Password for user user1? (whill note echo) _
Password for user user1? (again) _
Allow root ssh login? (yes, no, prohibit-password) [no]
What timezone are you in? ('?' for list) [Asia/Yekaterinburg]

Availble disks are: wd0 sd0.
Which disk is the root disk? ('?' for details) [wd0]

Use (W)hole disk MBR, whole disk (G)PT, (O)penBSD area or (E)dit? [OpenBSD] W

Use (A)uto layout, (E)dit auto layout, or create (C)ustom layout? [a] A
Let's install the sets!

Location of sets? (disk http nfs or 'done') [http]
HTTP proxy URL? (e.g. 'http://proxy:8080', or 'none') [none]
HTTP Server? (hostname, list#, 'done' or '?') cdn.openbsd.org
Server directory? [pub/OpenBSD/6.7/amd64] pub/OpenBSD/6.7/amd64

Set name(s)? (or 'about' or 'done') [done]

Location of sets? (disk http nfs or 'done') [done]
Saving configuration files... done.
Making all device nodes... done.
Multiprocessor machine: using bsd.mp instead of bsd.
Relinking to create unique kernel... done.

CONGRATULATION! Your OpenBSD install has been successfully completed!

When you login to your new system the first time, please read your mail
using the 'mail' command.

Exit to (S)hell, (H)alt or (R)eboot? [reboot] H
syncing disk... done

The operation system ha halted.
Please press any key to reboot.
```

Дальше остаётся извлечь флешку и включить загрузку с жёсткого диска.

## Пояснения к установке OpenBSD
В ходе установки был создан пользователь, кроме root, и отключена возможность подключаться под root по ssh. Это минимальные правила безопасности, которые стоит соблюдать. Следует выдать пользователю возможность повышения привелегий sudo/visudo (в идеале на конкретные операции), и не работать под root. Обычные рабочие операции root не требуют.

[1]: https://www.openbsd.org/faq/faq4.html#Download