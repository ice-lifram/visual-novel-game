# Summer Circuits Engine v1.0 Skeleton
import pygame, sys
from pathlib import Path
import dialogue

pygame.init()
WIDTH,HEIGHT=1280,720
FPS=60
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Summer Circuits")
clock=pygame.time.Clock()
WHITE=(255,255,255);BLACK=(0,0,0);BOX=(20,20,20)
ASSETS=Path("assets");BG=ASSETS/"backgrounds";PT=ASSETS/"portraits"
fn=pygame.font.SysFont("arial",28,True);ft=pygame.font.SysFont("arial",30);fT=pygame.font.SysFont("arial",56,True);fs=pygame.font.SysFont("arial",34)
def ph(sz,c): s=pygame.Surface(sz);s.fill(c);return s
cache_bg={};cache_pt={}
state={"bg":ph((WIDTH,HEIGHT),(60,70,90)),"l":None,"r":None}
def load(folder,name,size):
    if not name:return None
    cache=cache_bg if folder==BG else cache_pt
    if name in cache:return cache[name]
    p=folder/f"{name}.png"
    img=pygame.image.load(p.as_posix()).convert_alpha() if p.exists() else ph(size,(120,120,120))
    if img.get_size()!=size: img=pygame.transform.smoothscale(img,size)
    cache[name]=img;return img
def process():
    global idx
    while idx<len(scene):
        e=scene[idx]
        if e["type"]=="background": state["bg"]=load(BG,e["name"],(WIDTH,HEIGHT));idx+=1
        elif e["type"]=="portrait": state["l"]=load(PT,e.get("left"),(320,480));state["r"]=load(PT,e.get("right"),(320,480));idx+=1
        else: break
def wrap(t):
    out=[];cur=""
    for w in t.split():
        test=cur+w+" "
        if ft.size(test)[0]<1160: cur=test
        else: out.append(cur);cur=w+" "
    if cur: out.append(cur)
    return out
SCENES=[dialogue.chapter0,dialogue.chapter1]
si=0;scene=SCENES[0];idx=0;run=True;process()
while run:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: run=False
        elif ev.type==pygame.KEYDOWN and ev.key in (pygame.K_SPACE,pygame.K_RETURN):
            if idx<len(scene)-1: idx+=1;process()
            else:
                si+=1
                if si>=len(SCENES): run=False;break
                scene=SCENES[si];idx=0;process()
    screen.blit(state["bg"],(0,0))
    cur=scene[idx]
    if cur["type"]=="title":
        screen.fill(BLACK)
        screen.blit(fT.render(cur["title"],1,WHITE),(100,220))
        screen.blit(fs.render(cur["subtitle"],1,WHITE),(100,300))
    else:
        if state["l"]:screen.blit(state["l"],(40,140))
        if state["r"]:screen.blit(state["r"],(920,140))
        pygame.draw.rect(screen,BOX,(20,500,1240,190),border_radius=10)
        screen.blit(fn.render(cur["speaker"],1,WHITE),(45,515))
        y=560
        for line in wrap(cur["text"]):
            screen.blit(ft.render(line,1,WHITE),(45,y));y+=36
    pygame.display.flip();clock.tick(FPS)
pygame.quit();sys.exit()
