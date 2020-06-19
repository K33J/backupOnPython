# import os
# import time

# source = ['"/home/user/Pictures/testPng"']

# direction = '/home/user/Documents'

# target = direction + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# zipCommand = "zip -qr {0} {1}" . format(target, ' '.join(source))

# if os.system(zipCommand) == 0:
#     print('Backup created succesfully! in ', target)
# else:
#     print('Error backup create..')
##################################################################################################

##################################################################################################
import os
import time

source = ['"/home/user/Pictures/wall"', '/home/user/Pictures/prof']

direction = '/home/user/Documents'

today = direction + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.tar'

comment = input('Put your commentary --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.tar'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.tar'

if not os.path.exists(today):
    os.mkdir(today)
    print("Directory has created succesfull!..", today)

tarCommand = "tar cvf {0} {1}" . format(target, ' '.join(source))

if os.system(tarCommand) == 0:
    print('Backup created succesfully! in ', target)
else:
    print('Error backup create..')












