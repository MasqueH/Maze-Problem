m =[ [0,1,0,0,0,1,1,0,0,0,1,1,1,1,1],
     [1,0,0,0,1,1,0,1,1,1,0,0,1,1,1],
     [0,1,1,0,0,0,0,1,1,1,1,0,0,1,1],
     [1,1,0,1,1,1,1,0,1,1,0,1,1,0,0],
     [1,1,0,1,0,0,1,0,1,1,1,1,1,1,1],
     [0,0,1,1,0,1,1,1,0,1,0,0,1,0,1],
     [0,0,1,1,0,1,1,1,0,1,0,0,1,0,1],
     [0,1,1,1,1,0,0,1,1,1,1,1,1,1,1],
     [0,0,1,1,0,1,1,0,1,1,1,1,1,0,1],
     [1,1,0,0,0,1,1,0,1,1,0,0,0,0,0],
     [0,0,1,1,1,1,1,0,0,0,1,1,1,1,0],
     [0,1,0,0,1,1,1,1,1,0,1,1,1,1,0]];


class cell:
    def __init__(self,x,y):
        self.x,self.y=x,y
        if self.x>=0 and self.x<len(m) and self.y>=0 and self.y<len(m[-1]): self.value=m[self.x][self.y]
        else: self.value=1 
        self.direction=0
    def newnextcell(self):
        ds=((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
        i,j = ds[self.direction]
        self.direction += 1
        return cell(self.x+i,self.y+j)
stack=[cell(0,0)]

while(stack):
    curcell=stack[-1]
    if (curcell.x,curcell.y)==(len(m)-1,len(m[-1])-1): print([(c.x,c.y) for c in stack]);break
    elif curcell.direction < 8:
        nn=curcell.newnextcell()
        if nn.value==0 and (nn.x,nn.y) not in [(c.x,c.y) for c in stack]: stack.append(nn)
    else: stack.pop()