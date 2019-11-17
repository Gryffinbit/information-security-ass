print 'This is a maze.'
print 'Python is so easy.'
print 'Plz Input The Shortest Way:'
maze = '##########' \
       '#S#@@@@@@#' \
       '#@#@####@#' \
       '#@#@@@@#@#' \
       '#@####@#@#' \
       '#@@@@@@#@#' \
       '########@#' \
       '#E######@#' \
       '#@@@@@@@@#' \
       '##########'
way = raw_input()
len = len(way)
p = 11
for i in way:
    if i == '&':
        p -= 10
    if i == '$':
        p += 10
    if i == '6':
        p -= 1
    if i == '3':
        p += 1
    if maze[p] == '#':
        print 'Your way is wrong'
        exit(0)
        break
    if maze[p] == '@':
        continue
    if maze[p] == 'E':
        print 'You do it,your flag is Syc\\{+Your Input+\\}.'
        exit(0)
        continue