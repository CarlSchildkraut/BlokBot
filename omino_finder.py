import pygame
from polyomino import Polyomino


#1:red
#2:blue
#3:yellow
#4:red
color_hash={(195,195,195):0,(237,28,36):1,(63,72,204):2,(255,242,0):3,(47,215,97):4}

def interpret_image(file_loc):
    try:
        surface = pygame.image.load(file_loc)
        x,y=surface.get_size()
        assert x%30==y%30==5
        m,n=(x-5)//30,(y-5)//30
        colors=[]
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(color_hash[tuple(surface.get_at((30*j+14,30*i+14)))[:3]])
            colors.append(row)
        return colors
    except ValueError:
        print("Error -- image could not be read.")
        return []

def partition_into_disconnected(coords_list):
    if len(coords_list)==0: return []
    parts=[]
    p=coords_list[0]
    S={p}
    n=1
    while True:
        T=set()
        for s in S:
            x,y=s
            T.add((x,y))
            if (x+1,y) in coords_list: T.add((x+1,y))
            if (x-1,y) in coords_list: T.add((x-1,y))
            if (x,y+1) in coords_list: T.add((x,y+1))
            if (x,y-1) in coords_list: T.add((x,y-1))
        m=len(T)
        if m==n:
            break
        n=m
        S=T
    return [list(S)]+partition_into_disconnected([p for p in coords_list if p not in S])

def get_ominos(color_list):
    H={}
    for i in range(1,5):
        coords=[]
        for y in range(len(color_list)):
            for x in range(len(color_list[0])):
                if color_list[y][x]==i:
                    coords.append((x,y))
        pieces = partition_into_disconnected(coords)
        ominos = [Polyomino(p) for p in pieces]
        for p in ominos:
            print(i)
            print(p)

colors=interpret_image('exboard.png')

get_ominos(colors)
    
