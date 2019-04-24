class Polyomino:
    def __init__(self, coords):
        coords=set(coords)
        self.n=len(coords)
        minx = min({x[0] for x in coords})
        miny = min({x[1] for x in coords})
        self.coords={(x[0]-minx,x[1]-miny) for x in coords}
    def __eq__(self,other):
        return self.coords == other.coords
    def rotate(self, n):#n is no of quarterturns
        n%=4
        if n==0:   return Polyomino(self.coords)
        elif n==1: return Polyomino({(-x[1],x[0]) for x in self.coords})
        elif n==2: return Polyomino({(-x[0],-x[1]) for x in self.coords})
        elif n==3: return Polyomino({(x[1],-x[0]) for x in self.coords})
    def reflect(self):
        return Polyomino({(x[0],-x[1]) for x in self.coords})
    def __hash__(self):
        return hash(tuple(sorted(self.coords)))
    def orientations(self):
        S={self,self.rotate(1),self.rotate(2),self.rotate(3)}
        S2={x.reflect() for x in S}
        return S.union(S2)
    def __repr__(self):
        return 'Polyomino'+repr(self.coords)
    def __str__(self):
        maxx=max({x[0] for x in self.coords})
        maxy=max({x[1] for x in self.coords})
        string=''
        for y in range(0,maxy+1):
            for x in range(0,maxx+1):
                string+='█' if (x,y) in self.coords else ' '
            string+='\n'
        return string
    def translate(self,diff): #returns coords_list
        xDiff,yDiff = diff
        return {(x[0]+xDiff,x[1]+yDiff) for x in self.coords}
    def __contains__(self,other): #doesn't include orientations
        for ori in other.orientations():
            fixedPoint=list(ori.coords)[0]
            for p in self.coords:
                otherCoords=ori.translate((p[0]-fixedPoint[0],p[1]-fixedPoint[1]))
                if all([x in self.coords for x in otherCoords]):
                    return True
        return False
    def __ne__(self,other):
        return hash(self)!=hash(other)
    def __lt__(self,other):
        return hash(self)<hash(other)
    def __lt__(self,other):
        return hash(self)>hash(other)
    def __le__(self,other):
        return hash(self)<=hash(other)
    def __ge__(self,other):
        return hash(self)>=hash(other)
    def getAll(n):
        if n<0: return None
        if n==0: return set()
        if n==1:
            return {Polyomino({(0,0)})}
        else:
            allPoly = set()
            oldRes = Polyomino.getAll(n-1)
            for poly in oldRes:
                coords = poly.coords
                for p in coords:
                    for i in [(-1,0),(0,1),(1,0),(0,-1)]:
                        newCoords = coords.union({(p[0]+i[0],p[1]+i[1])})
                        if len(newCoords)==n:
                            newPoly=Polyomino(newCoords)
                            allPoly.add(sorted(newPoly.orientations())[0])
            return allPoly
