def rotate(width, height, raster):
    for j in range(0, width):
        target = width * height - 1 - j
        t_pos = target - (j * (height - 1))
        for l in range(1, height):
            pos = target - (l * width) - (j * (height - 1 - l))
            buffer = raster[pos]
            for idx in range(pos, t_pos):
                raster[idx] = raster[idx + 1]
            raster[t_pos] = buffer
    return raster


def fast_rot(width, height, raster):
    for j in range(0, width):
        for k in range(0, height):
            to = width * height - (height * j + k + 1)
            i = (width - j - 1) + width * k
            if i != to:
                while i > to:
                    i = width * (height - (i % height) - 1) + ((i - (i % height)) / height)
                buffer = raster[int(i)]
                raster[int(i)] = raster[int(to)]
                raster[int(to)] = buffer
    return raster


def draw(w, r):
    h = int(len(r)/w)
    for i in range(0, h):
        [print(str(a) + ' ' * (3 - len(str(a))), end='') for a in r[i * w:(i + 1) * w]]
        print()


if __name__ == '__main__':
    # from random import randint
    wi = 1
    hi = 9
    # bm = [randint(0, 10) for i in range(0, wi*hi)]
    bm = list(range(0, wi*hi))
    draw(wi, bm)
    print('===================================')
    draw(hi, fast_rot(wi, hi, bm))
