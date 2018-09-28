#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#need install RaspberryJuice plugins (Spigot/Bukkit)
from mcpi.minecraft import Minecraft
import time

serverip='192.168.1.113'
accountid='mc_usersname' 

mc = Minecraft.create(serverip)

class mic:
    x=0
    y=0
    z=0
    u=1
    def playerid(self,n):
        self.u=mc.getPlayerEntityId(n)
        #print "Account ID:"
        #print self.u

    def playerpostion(self):
        x,y,z=mc.entity.getPos(self.u)
        self.x=x
        self.y=y
        self.z=z
        #print x,y,z

    def getblockinfo(self,x,y,z):
        p=mc.getBlockWithData(x,y,z)
        return p

 

    def find_item1(self,item):
        result=0
        strs=""
        block=mc.getBlocks(self.x+5,self.y+5,self.z+5,self.x-5,self.y-5,self.z-5)
        block=set(block)
        for y in block:
            if item.get(y)!= None:
                strs=strs+" "+item.get(y)
                result =1
             
            if result==1:
                mc.postToChat(strs)
                return strs
            else:
                return "None"
   
                


m=mic()
m.playerid(accountid)
m.playerpostion()

ores={14:"黃金",15:"鐵礦",16:"煤碳",56:"鑽石",21:"青金石",129:"綠寶石"}
find_result=m.find_item1(ores)
if find_result=="None":
    print "什麼都沒有"
else:
    print "發現了:"+find_result
                
