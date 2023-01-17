import sys, random, time

try:
    import bext
except ImportError:
    print('Ten program wymaga modułu bext,')
    print('który możesz zainstalować według instrukcji ze strony')
    print('https://pypi.org/project/Bext/.')
    sys.exit()

width, height = bext.size()
width -= 1

numberOfLogos = 5
pauseAmount = 0.2
colors = ['red', 'green', 'yellow','blue', 'cyan', 'white']
UpRight = 'ur'
UpLeft = 'ul'
DownRight = 'dr'
DownLeft = 'dl'
directions = (UpRight, UpLeft, DownRight, DownLeft)
color = 'color'
x = 'x'
y = 'y'
dir = 'direction'

def main():
    bext.clear()

    logos = []
    for i in range(numberOfLogos):
        logos.append({color: random.choice(colors),
                      x: random.randint(1,width -4),
                      y: random.randint(1, height -4),
                      dir: random.choice(directions)})
        if logos[-1][x] % 2 == 1:
            logos[-1][x] -= 1

    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[x], logo[y])
            print(' ', end='')

            originalDirection = logo[dir]
            if logo[x] == 0 and logo[y] == 0:
                logo[dir] = DownRight
                cornerBounces += 1
            elif logo[x] == 0 and logo[y] == height -1:
                logo[dir] = UpRight
                cornerBounces += 1
            elif logo[x] == width - 3 and logo[y] == 0:
                logo[dir] = DownLeft
                cornerBounces += 1
            elif logo[x] == width - 3 and logo[y] == height - 1:
                logo[dir] = UpLeft
                cornerBounces += 1

            elif logo[x] == 0 and logo[dir] == UpLeft:
                logo[dir] = UpRight
            elif logo[x] == 0 and logo[dir] == DownLeft:
                logo[dir] = DownRight
            elif logo[x] == width - 3 and logo[dir] == UpRight:
                logo[dir] = UpLeft
            elif logo[x] == width - 3 and logo[dir] == DownRight:
                logo[dir] = DownLeft

            elif logo[y] == 0 and logo[dir] == UpLeft:
                logo[dir] = DownLeft
            elif logo[y] == 0 and logo[dir] == UpRight:
                logo[dir] = DownRight
            elif logo[y] == height - 1 and logo[dir] == DownLeft:
                logo[dir] = UpLeft
            elif logo[y] == height - 1 and logo[dir] == DownRight:
                logo[dir] = UpRight

            if logo[dir] != originalDirection:
                logo[color] = random.choice(colors)

            if logo[dir] == UpRight:
                logo[x] += 2
                logo[y] -= 1
            elif logo[dir] == UpLeft:
                logo[x] -= 2
                logo[y] -= 1
            elif logo[dir] == DownRight:
                logo[x] += 2
                logo[y] += 1
            elif logo[dir] == DownLeft:
                logo[x] -= 2
                logo[y] += 1

        bext.goto(5, 0)
        bext.fg('white')
        print('Odbicie od rogu:', cornerBounces, end='')

        for logo in logos:
            bext.goto(logo[x], logo[y])
            bext.fg(logo[color])
            print('DVD', end='')

        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(pauseAmount)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Animacja logo DVD')
        sys.exit()
