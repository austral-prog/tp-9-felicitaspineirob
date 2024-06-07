
def create_inventory(items):
    result=dict()
    for item in items:
        result[item]=items.count(item)
    return result


def add_items(inventory, items):
    for item in items:
        if item in inventory:
              inventory[item]+=1
        else:
         inventory[item]=1
    return(result)


def decrement_items(inventory, items):
    for item in inventory:
        if inventory[item]>1:
            inventory[item]-=1
        else: 
            inventory[item]=0 
    return inventory
    

def remove_item(inventory, item):
    if item in inventory.keys():
        del inventory[item]
    return inventory 


def list_inventory(inventory):
list=[]
for item in inventory.items(): 
    if item[1]>0
    list+=[item]
return list
