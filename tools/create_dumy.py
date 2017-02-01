# from pathlib import Path
# import rstr
#
# # for i in range(10):
# #     print(rstr.xeger(r'[A-Z]{3}-\d{3}\.mp4'))
#
# # p = Path('./Done/test.txt')
# # p = Path('./Done/')
# # p.write_text('text')
# Path('../!Done').mkdir(parents=True, exist_ok=True)
# Path('../!Yet').mkdir(parents=True, exist_ok=True)
# for i in range(10):
#     Path('../!Done/', rstr.xeger(r'[A-Z]{3}-\d{3}\.mp4')).write_text('text')

from pathlib import Path

p = Path('../Yet')
for i in range(100, 104):
    new_p = p / 'team-{}.mp4'.format(i)
    new_p.write_text('123')
