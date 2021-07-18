#-*coding:UTF-8*-
import os
yugao=[
'you-get https://www.bilibili.com/bangumi/play/ep401373',
'you-get https://www.bilibili.com/bangumi/play/ep402324',
'you-get https://www.bilibili.com/bangumi/play/ep402595',
'you-get https://www.bilibili.com/bangumi/play/ep402890',
'you-get https://www.bilibili.com/bangumi/play/ep403640',
'you-get https://www.bilibili.com/bangumi/play/ep404051',
'you-get https://www.bilibili.com/bangumi/play/ep406332',
'you-get https://www.bilibili.com/bangumi/play/ep407352',
'you-get https://www.bilibili.com/bangumi/play/ep407618',
'you-get https://www.bilibili.com/bangumi/play/ep408115',
'you-get https://www.bilibili.com/bangumi/play/ep408712',
'you-get https://www.bilibili.com/bangumi/play/ep409911'
]
huaxu=[
'you-get https://www.bilibili.com/bangumi/play/ep411187',
'you-get https://www.bilibili.com/bangumi/play/ep411221',
'you-get https://www.bilibili.com/bangumi/play/ep408855',
'you-get https://www.bilibili.com/bangumi/play/ep405175',
'you-get https://www.bilibili.com/bangumi/play/ep405124',
'you-get https://www.bilibili.com/bangumi/play/ep402059',
'you-get https://www.bilibili.com/bangumi/play/ep400126',
'you-get https://www.bilibili.com/bangumi/play/ep400868',
'you-get https://www.bilibili.com/bangumi/play/ep402557',
'you-get https://www.bilibili.com/bangumi/play/ep402556',
'you-get https://www.bilibili.com/bangumi/play/ep400634',
'you-get https://www.bilibili.com/bangumi/play/ep399837',
'you-get https://www.bilibili.com/bangumi/play/ep399829',
'you-get https://www.bilibili.com/bangumi/play/ep399688',
'you-get https://www.bilibili.com/bangumi/play/ep394035',
'you-get https://www.bilibili.com/bangumi/play/ep364442',
'you-get https://www.bilibili.com/bangumi/play/ep401554'
]
os.system('pip install you-get')
os.system('you-get https://www.bilibili.com/bangumi/play/ep402337 --playlist')
for i in yugao:
    os.system(i)
for i in huaxu:
    os.system(i)