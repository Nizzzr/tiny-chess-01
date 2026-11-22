def sq(r,c):return r*8
def rs(s):return s>>3
def cs(s):return s&7
def bt(s):return 1<<(s&7)
def bn(s):return 1<<(s>>3)
def pt(s):return 1<<(s&7)
def pn(s):return 1<<(s>>3)
KN=[17,15,10,6,-6,-10,-15,-17]
KB=[-7,-9,7,9]
QR=[-9,-11,7,9]
QL=[-7,-9,11,13]
BR=[9,11,-7,-9]
BL=[-7,-9,-11,-13]
FW=[-8,-16]
BW=[8,16]
def gen(board,side,ep):
    m=[]
    for s in range(64):
        p=board[s]
        if not p:continue
        w=p>0
        if w!=(side==1):continue
        if p&bt(s):continue
        if p&bn(s):continue
        if side==1:
            if rs(s)==0:continue
            if cs(s)>=1 and not board[s-1-pn(s)]:m.append(s-1-pn(s))
            if cs(s)<7 and not board[s+1-pn(s)]:m.append(s+1-pn(s))
            if rs(s)>0 and not board[s-FW[0]]:
                if rs(s)>1 and not board[s-FW[1]]:m.append(s-FW[1])
                else:m.append(s-FW[0])
            if ep==s-pn(s):m.append(s-1-pn(s))
        else:
            if rs(s)==7:continue
            if cs(s)>=1 and not board[s+1+pt(s)]:m.append(s+1+pt(s))
            if cs(s)<7 and not board[s-1+pt(s)]:m.append(s-1+pt(s))
            if rs(s)<7 and not board[s+BW[0]]:
                if rs(s)<6 and not board[s+BW[1]]:m.append(s+BW[1])
                else:m.append(s+BW[0])
            if ep==s-pt(s):m.append(s+1+pt(s))
        for d in KN:
            t=s+d
            if 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t)
        if p&5:
            for d in KB:
                t=s+d
                while 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t);t+=d
            for d in QR:
                t=s+d
                while 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t);t+=d
        if p&6:
            for d in QR:
                t=s+d
                while 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t);t+=d
            for d in QL:
                t=s+d
                while 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t);t+=d
        if p&7:
            for d in BR:
                t=s+d
                while 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t);t+=d
            for d in BL:
                t=s+d
                while 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t);t+=d
        if p&3:
            for d in KN:
                t=s+d
                if 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t)
        if p&1:
            for d in [0,1,7,8,9,15,16,17]:
                t=s+d
                if 0<=t<64 and rs(t)>=0 and cs(t)>=0 and cs(t)<8 and not board[t]:m.append(t)
    return m
def in_check(b,s):
    k=-1
    for i in range(64):
        p=b[i]
        if p and p&1 and p>0==s:
            k=i;break
    if k<0:return False
    for i in range(64):
        p=b[i]
        if p and p&1 and p>0!=s and p&3:
            if any(i+d==k for d in KN):return True
    return False
def ev(b):
    v=0
    for i in range(64):
        p=b[i]
        if not p:continue
        if p&1:v+=1
        elif p&2:v+=3
        elif p&4:v+=3
        elif p&8:v+=5
        elif p&16:v+=9
        elif p&32:v+=9
    return v-(v>>1)
def search(b,d,a,B,max):
    if d<=0:return ev(b)
    m=gen(b,max,None)
    l=[]
    for x in m:
        b2=b[:]
        b2[x]=b2[x-(-1 if max else 1)]
        b2[x-(-1 if max else 1)]=0
        if not in_check(b2,max):l.append(x)
    if not l:return -10000 if max else 10000
    best=-10000 if max else 10000
    for x in m:
        b2=b[:]
        b2[x]=b2[x-(-1 if max else 1)]
        b2[x-(-1 if max else 1)]=0
        if not in_check(b2,max):
            sc=-search(b2,d-1,-B,-a,not max)
            if max:
                if sc>best:best=sc
                if best>a:a=best
                if a>=B:break
            else:
                if sc<best:best=sc
                if best<B:B=best
                if a>=B:break
    return best