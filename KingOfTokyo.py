#------------King of Tokyo--------------------------#
#------------Importe--------------------------------#
import random
from dicts import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#------------GUI------------------------------------#
#------------Root-Fenster---------------------------#
window = tk.Tk()
window.title("King of Tokyo")
window.iconbitmap("claw.ico")
window.geometry("895x900")
window.resizable(False, False)
background = ImageTk.PhotoImage(Image.open("board.png"))
back_label = tk.Label(window, image=background)
back_label.place(x=0,y=0, relwidth=1, relheight=1)
#------------Die Felder-----------------------------#
#Aktiver Spieler
active_lbl = tk.Label(window)
active_lbl.grid(column=0, row=0, columnspan=4, sticky= 'we')
# Spieler 1 Feld:
ply1_frm = tk.LabelFrame(window, padx=10, pady=10, width=180, text="Spieler 1", bg="#F69814")
ply1_frm.grid(column=0, row=1,padx=16,pady=10)
ply1_frm.columnconfigure(1,weight=1,minsize=100)
#Spieler 2 Feld
ply2_frm = tk.LabelFrame(window, padx=10, pady=10, text="Spieler 2", bg="#F69814")
ply2_frm.grid(column=1, row=1,padx=16,pady=10)
ply2_frm.columnconfigure(1,weight=1,minsize=100)
#Spieler 3 Feld
ply3_frm = tk.LabelFrame(window, padx=10, pady=10, text="Spieler 3", bg="#F69814")
ply3_frm.grid(column=2, row=1,padx=16,pady=10)
ply3_frm.columnconfigure(1,weight=1,minsize=100)
# Spieler 4 Feld
ply4_frm = tk.LabelFrame(window, padx=10, pady=10, text="Spieler 4", bg="#F69814")
ply4_frm.grid(column=3, row=1,padx=16,pady=10)
ply4_frm.columnconfigure(1,weight=1, minsize=100)
#Spieler 1 Inhalt
ply1_name_lbl=tk.Label(ply1_frm)
ply1_health_lbl=tk.Label(ply1_frm)
ply1_energy_lbl=tk.Label(ply1_frm)
ply1_points_lbl=tk.Label(ply1_frm)
#Spieler 2 Inhalt
ply2_name_lbl=tk.Label(ply2_frm)
ply2_health_lbl=tk.Label(ply2_frm)
ply2_energy_lbl=tk.Label(ply2_frm)
ply2_points_lbl=tk.Label(ply2_frm)
#Spieler 3 Inhalt
ply3_name_lbl=tk.Label(ply3_frm)
ply3_health_lbl=tk.Label(ply3_frm)
ply3_energy_lbl=tk.Label(ply3_frm)
ply3_points_lbl=tk.Label(ply3_frm)
#Spieler 4 Inhalt:
ply4_name_lbl=tk.Label(ply4_frm)
ply4_health_lbl=tk.Label(ply4_frm)
ply4_energy_lbl=tk.Label(ply4_frm)
ply4_points_lbl=tk.Label(ply4_frm)
#Spieler in Tokyo
tokyo_lbl = tk.Label(window)
tokyo_lbl.grid(column=0, row=2, columnspan=4, sticky= 'we')
#Würfelfeld
die_frm = tk.LabelFrame(window,bg='#F69814', text="Würfelfeld")
die_frm.grid(column=1, row=3, columnspan=2, sticky= 'we',padx=13,pady=10)
die_frm.columnconfigure(0,weight=2)
#Würfelfeldinhalt
check01=tk.IntVar()
check02=tk.IntVar()
check03=tk.IntVar()
check04=tk.IntVar()
check05=tk.IntVar()
check06=tk.IntVar()
check07=tk.IntVar()
check08=tk.IntVar()
rolls_left = tk.Label(die_frm)
die01 = tk.Checkbutton(die_frm)
die02 = tk.Checkbutton(die_frm)
die03 = tk.Checkbutton(die_frm)
die04 = tk.Checkbutton(die_frm)
die05 = tk.Checkbutton(die_frm)
die06 = tk.Checkbutton(die_frm)
die07 = tk.Checkbutton(die_frm)
die08 = tk.Checkbutton(die_frm)
die_keep_btn = tk.Button(die_frm)
die_end_btn = tk.Button(die_frm)
#Powerkarten Feld
powercard_frm = tk.Frame(window,bg='#F69814',padx=15,pady=10)
powercard_frm.grid(column=0,row=4,columnspan=4,padx=15,pady=10)
powercard_frm.columnconfigure(0,weight=2)
powercard_frm.rowconfigure(1,weight=0,)
#Powerkarten Inhalt
power_var= tk.StringVar()
card01_check = tk.Radiobutton(powercard_frm)
card01_text = tk.Label(powercard_frm)
card01_cost = tk.Label(powercard_frm)
card02_check = tk.Radiobutton(powercard_frm)
card02_text = tk.Label(powercard_frm)
card02_cost = tk.Label(powercard_frm)
card03_check = tk.Radiobutton(powercard_frm)
card03_text = tk.Label(powercard_frm)
card03_cost = tk.Label(powercard_frm)
buy_card = tk.Button(powercard_frm)
end_buy_card = tk.Button(powercard_frm)
reset_card = tk.Button(powercard_frm)
#Spielernamen Feld
name_frm = tk.Frame(window,bg='#F69814',padx=13,pady=10)
name_frm.grid(column=0,row=0,columnspan=2, sticky="we")
name_frm.columnconfigure(0,weight=0)
name_frm.rowconfigure(1,weight=0,)
#Spielernamen Inhalt
name_lbl = tk.Label(name_frm)
name_ent = tk.Entry(name_frm)
name_btn = tk.Button(name_frm)
player_name = tk.StringVar(name_frm)
#------------Globale Werte--------------------------#
# Variablen
tokyo = 0
tick=0
now_playing = 0
key_now = 0
name_now = ""
die_now = 0
throws_now = 0
throws_taken = 0
#Listen & Dicts:
dice_picture = { 
    1 : "Du hast eine 1!", 
    2 : "Du hast eine 2!", 
    3 : "Du hast eine 3!", 
    4 : "Du hast ein Herz!",
    5 : "Du hast einen Blitz!",
    6 : "Du hast eine Tatze!",}
card_deck = power_cards # Kartenstapel als Dict
card_list = list(card_deck) #Kartenstapel als Liste
cards_used = []
players = {}
players_list = list(players)
tokyo_player = []
die_saved=[]
player_sequence = []
names = []
turnorder = []
store=[]
final_die=[]
player_now ={}
#------------Die Logik------------------------------#

#------------Programme------------------------------#
def dice_roll (dice_am):
    """Die angegebene Anzahl an Würfeln werfen.\n 
    Zu geben: wie viele Würfel?"""
    dice = []
    while dice_am >=1: 
        dice.append(random.randint(1,6))
        dice_am -= 1
    return dice
def dice_throw(number):
    """Den Würfelwerten ihre Spielbezeichnung geben.\n 
    Zu geben: Liste der Würfelergebnisse"""
    pictures = []
    for dice in number:
        pictures.append(dice_picture[dice])
    return pictures
def power_add(name,player):
    """Die gekaufte Powerkarte dem Spieler hinzufügen.\n
    Zu geben: Kartenname & welcher Spieler"""
    if name == "Säure Angriff":
        player["dmg"] += 1
        tk.messagebox.showinfo("Neue Power!","Deine Angriffe sind nun noch gefährlicher!")
    elif name == "Außerirdische Macht":
        player["energybonus"] +=1
        tk.messagebox.showinfo("Neue Power!","Die Außerirdische Macht steht dir bei!")
    elif name == "Alpha Monster":
        player["alpha"]=True
        tk.messagebox.showinfo("Neue Power!","Du bist nun das Alpha-Monster!")
    elif name == "Hochhaus":
        player["points"] += 3
        tk.messagebox.showinfo("Neue Power!",f"Du hast nun {player['points']} Siegpunkte")
    elif name == "Plattenpanzer":
        player["def"] += 1
        tk.messagebox.showinfo("Neue Power!","Du trägst nun eine Rüstung!")
    elif name == "Pendlerzug":
        player["points"] += 2
        tk.messagebox.showinfo("Neue Power!",f"Du hast nun {player['points']} Siegpunkte")
    elif name == "Komplette Zerstörung":
        player["destroy"] = True
        tk.messagebox.showinfo("Neue Power!","Du hast nun die Macht der Zerstörung!")
    elif name == "Kiosk":
        player["points"] += 1
        tk.messagebox.showinfo("Neue Power!",f"Du hast nun {player['points']} Siegpunkte")
    elif name == "Schlagzeile":
        player["headline"] = True
        tk.messagebox.showinfo("Neue Power!","Deine Taten werden von den Medien mehr beachtet!")
    elif name == "Sprung aus großer Höhe":
        global tokyo
        player["points"] += 2
        tokyo = player["turnorder"]
        gui_tokyo(tokyo)
        tk.messagebox.showinfo("Neue Power!","Du springst nach Tokyo!")
    elif name == "Aufladen":
        player["energy"] += 9
        tk.messagebox.showinfo("Neue Power!",f"Energie durchströmt deinen Körper! Du hast wieder {player['energy']} Energie.")
    elif name == "Kraftwerk":
        player["powerplant"] = True
        tk.messagebox.showinfo("Neue Power!","Die Energie in dir bebt!")
    elif name == "Evakuierungsbefehl":
        tk.messagebox.showinfo("Neue Power!","Die Stadt wird evakuiert!")
        for monster in players:
            if monster != player:
                players[monster]["points"] -= 5
                if players[monster]["points"] < 0:
                    players[monster]["points"] = 0
                tk.messagebox.showinfo("Aktivierung",f"{players[monster]['name']} findet keine Opfer mehr! Neuer Siegpunktestand= {players[monster]['points']}.")
    elif name == "Rückschlag!":
        tk.messagebox.showinfo("Neue Power!","Tokyo wehrt sich!")
        for monster in players:
            if monster != player:
                players[monster]["points"] -= 5
                if players[monster]["points"] < 0:
                    players[monster]["points"] = 0
                tk.messagebox.showinfo("Aktivierung",f"{players[monster]['name']} wird getroffen! Neuer Siegpunktestand= {players[monster]['points']}.")
    elif name == "Noch größer!":
        player["max_health"] = 12
        player["health"] += 2
        tk.messagebox.showinfo("Neue Power!","Du bist gewaltig gewachsen!")
    elif name == "Zweiter Kopf":
        player["die"] += 1
        tk.messagebox.showinfo("Neue Power!","Zwei Köpfe sind besser als einer!")
    elif name == "Mehr Arme":
        player["die"] += 1
        tk.messagebox.showinfo("Neue Power!","Mehr Arme bedeutet mehr Möglichkeiten!")
    elif name == "Feuerball":
        tk.messagebox.showinfo("Neue Power!","Dein Feuerball mäht sich durch die Gegner!")
        for monster in players:
            if monster != player:
                players[monster]["health"] -= 2
                if players[monster]['health'] <= 0:
                    tk.messagebox.showinfo("Besiegt!",f"{players[monster]['name']} hat keine Lebenspunkte mehr und somit raus!")
                    if players[monster]["name"] == tokyo:
                        tokyo = 0
                        del players [monster]
                else:
                    tk.messagebox.showinfo("Aktivierung",f"{monster['name']} wird schwer getroffen! Neue Lebenspunkte= {monster['health']}.")
    elif name == "Blutrausch":
        player["rage"]=True
        tk.messagebox.showinfo("Neue Power!","Du bist im Blutrausch!")
    elif name == "Freund der Kinder":
        player["child"] = True
        tk.messagebox.showinfo("Neue Power!","Du bist das Lieblingsmonster der Kinder!")
    elif name == "Bergwerk":
        tk.messagebox.showinfo("Neue Power!","Das Bergwerk wird zerstört!")
        player["points"] += 2
        for monster in player_sequence:
            if monster != player_now:
                players[monster]["health"] -= 3
                if players[monster]['health'] <= 0:
                    tk.messagebox.showinfo("Besiegt!",f"{players[monster]['name']} hat keine Lebenspunkte mehr und somit raus!")
                    if players[monster]["name"] == tokyo:
                        tokyo = 0
                    del players [monster]
                else:
                    tk.messagebox.showinfo("NAktivierung",f"{players[monster]['name']} wird von Steinen getroffen! Neue Lebenspunkte= {players[monster]['health']}.")
    elif name == "Gigantisches Gehirn":
        player["throws"] += 1
        tk.messagebox.showinfo("Neue Power!","Du kannst nun schneller denken und so besser planen!")
    elif name == "Heilung":
        player["health"] += 2
        if player["health"] > player["max_health"]:
            player["health"] = player["max_health"]
        tk.messagebox.showinfo("Neue Power!",f"Du fühlst dich besser! Aktuelle Lebenspunkte: {player['health']}.")
    elif name == "Kannibale":
        player["canibalism"] = True
        tk.messagebox.showinfo("Neue Power!","Du verspürst die Lust nach Monsterfleisch!")
    elif name == "Regeneration":
        player["regen"] = True
        tk.messagebox.showinfo("Neue Power!","Deine Heilkräfte sind bewundernswert!")
    elif name == "Solarenergie":
        player["solar"]=True
        tk.messagebox.showinfo("Neue Power!","Du nutzt nun die Energie der Sonne!")
    elif name == "Panzer Weitwurf":
        player["tank"]=True
        tk.messagebox.showinfo("Neue Power!","Du findest gefallen daran die Waffen der Menschen zu 'benutzen'!")
    elif name == "Die Armee kommt!":
        player_now["points"] += 2
        player_now["health"] -= 2
        tk.messagebox.showinfo("Neue Power!","Du vernichtest die Armee, aber nocht komplett ohne Spuren an deinen Körper!")
    else:
        print("DAS IST MÜLL!!!!!!!")
    if card_deck[name][2] == "stay":
        player["powers"] += f"{name}\n"
    update_players(player_num)
def draw_card():
    """Neue Karte wird gezogen.\n
    Zu geben: -"""
    global cards_used
    if len(cards_used) >= len(card_list)-3:
        cards_used = []
    card_drawn= random.choice(card_list)
    if card_drawn in cards_used:                  
        card_drawn = draw_card()
        cards_used.append(card_drawn)
        return card_drawn
    else:
        cards_used.append(card_drawn)
        return card_drawn
def turn_order(player_count):
    """Die Spielerreihenfolge festlegen.\n
    Zu geben: Anzahl der Spieler"""
    turnorder = []
    while len(turnorder) != player_count:
        order = random.randint(1,player_count)
        if order not in turnorder:
            turnorder.append(order)
    return turnorder
def add_health(dice,active_player):
    """Im Würfelergebniss nach möglicher Heilung schauen und anwenden.\n
    Zu geben:Würfelergebniss, welcher Spieler"""
    heart = 0
    for num in dice:
        if num == 4:
            heart +=1
    return heart
def add_energy(dice,active_player):
    """Füge erwürfelte Energie hinzu.\n
    Zu geben: Würfelergebniss, welcher Spieler"""
    energy = 0
    for num in dice:
        if num == 5:
            energy +=1
    return energy
def add_dmg(dice,active_player):
    """Wie viel Schaden wurde erzeugt.\n
    Zu geben: Würfelergebniss, welcher Spieler"""
    hit = 0
    for num in dice:
        if num == 6:
            hit +=1
    hit += active_player["dmg"]
    return hit        
def add_points(dice,active_player):
    """Gewonnene Siegpunkte errechnen.\n
    Zu geben: Würfelergebniss, welcher Spieler"""
    point = 0
    one = []
    two = []
    three = []
    for num in dice:
        if num == 1:
            one.append("1")
        elif num == 2:
            two.append("1")
        elif num == 3:
            three.append("1")
        else:
            continue
    if len(one)>=3:
        point += (len(one)-2)
    elif len(two)>=3:
        point += (len(two)-1)
    elif len(three)>=3:
        point += len(three)
    return point
def buy_power(which_power,energy_player):
    """Kaufe eine Powerkarte vom Slot und lege eine neue aus.\n
    Zu geben: Welche Karte, welcher Spieler"""
    global slot1, slot2, slot3
    card = card_deck[which_power][1]
    #Fähigkeiten aktivieren
    if player_now["energybonus"] > 0:
        card -= player_now["energybonus"]
    #Genug Energie?
    if card <= player_now["energy"]:
        #Fähigkeiten aktivieren
        if player_now["headline"]:
            player_now["points"] += 1
            tk.messagebox.showinfo("Aktivierung",f"Du zierst alle Titelseiten! Du hast nun {player_now['points']} Siegpunkte.")
            if player_now["points"] >= 20:
                tk.messagebox.showinfo("The winner is you!",f"Glückwunsch! {name_now} ist der King of Tokio mit {player_now['points']} Siegpunkten!\nDanke fürs spielen!")
                quit()
        player_now["energy"] -= card
        tk.messagebox.showinfo("Gekauft",f"Du hast {which_power} gekauft! Restenergie = {player_now['energy']}.")
        power_add(which_power ,player_now)
        #Neue Karte auslegen
        if slot1 == which_power:
            slot1 = draw_card()
            update_players(player_num)    
            buy_powers_gui()
        elif slot2 == which_power:
            slot2 = draw_card()
            update_players(player_num)    
            buy_powers_gui()
        else:
            slot3 = draw_card()
            update_players(player_num)    
            buy_powers_gui()
    else:
        tk.messagebox.showerror("Fehler!","Du hast zu wenig Energie.")
    update_players(player_num)
    #Zurück zum Kaufbildschirm    
    buy_powers_gui()    
def attack(reciver,damage):
    """Schaden für einen Spieler berechnen bei einem Angriff.\n
    Zu geben: Welcher Spieler, Höhe Schaden"""
    global tokyo
    #Schaden verteilen
    players[reciver]["health"]-=damage
    #Fähigkeiten aktivieren
    players[reciver]["health"]+=players[reciver]["def"]
    if players[reciver]["def"] > 0:
        tk.messagebox.showinfo("Aktivierung/Schaden",f"{players[reciver]['name']} hat 1 Schaden abgewehrt und nun noch {players[reciver]['health']} Lebenspunkte!")
    else:
        tk.messagebox.showinfo("Schaden",f"{players[reciver]['name']} hat {damage} Schaden erlitten und nun noch {players[reciver]['health']} Lebenspunkte!")
    if players[reciver]['health'] > 0 and reciver == tokyo_player:
        update_players(player_num)
        leave = ""
        leave = leave_tokyo()
        if leave == 1:
            tokyo = 0
            tk.messagebox.showinfo("Tokyo","Tokyo ist nun wieder unbesetzt!")
        else:
            tk.messagebox.showinfo("Tokyo",f"Tokyo bleibt in der Hand von {tokyo}!")
    if players[reciver]['health'] <= 0:
        tk.messagebox.showinfo("Besiegt!",f"{players[reciver]['name']} hat keine Lebenspunkte mehr und somit raus!")
        if players[reciver]["name"] == tokyo:
            tokyo = 0
            tk.messagebox.showinfo("Tokyo","Tokyo ist unbesetzt!")
        player_sequence.remove(reciver)
def draw_new_cards():
    """Alle drei Karten neu auslegen.\n
    Zu geben:-"""
    global slot1
    global slot2
    global slot3
    slot1 = draw_card()
    slot2 = draw_card()
    slot3 = draw_card()
#------------Programme-GUI--------------------------#
def update_players(player_num):
    """GUI:Spielerboxen aktualisieren\n
    zu geben: Wie viele Spieler."""
    global ply1_name_lbl, ply1_health_lbl, ply1_energy_lbl, ply1_points_lbl, ply2_name_lbl, ply2_health_lbl, ply2_energy_lbl, ply2_points_lbl, ply3_name_lbl, ply3_health_lbl, ply3_energy_lbl, ply3_points_lbl, ply4_name_lbl, ply4_health_lbl, ply4_energy_lbl, ply4_points_lbl
    #Alte Einträge entfernen:
    #Spieler 1 Inhalt
    ply1_name_lbl.destroy()
    ply1_health_lbl.destroy()
    ply1_energy_lbl.destroy()
    ply1_points_lbl.destroy()
    #Spieler 2 Inhalt
    ply2_name_lbl.destroy()
    ply2_health_lbl.destroy()
    ply2_energy_lbl.destroy()
    ply2_points_lbl.destroy()
    #Spieler 3 Inhalt
    ply3_name_lbl.destroy()
    ply3_health_lbl.destroy()
    ply3_energy_lbl.destroy()
    ply3_points_lbl.destroy()
    #Spieler 4 Inhalt:
    ply4_name_lbl.destroy()
    ply4_health_lbl.destroy()
    ply4_energy_lbl.destroy()
    ply4_points_lbl.destroy()
    #Neue Einträge
    #Spieler 1 Inhalt
    ply1_name_lbl=tk.Label(ply1_frm, text=f"Name:\n{players[1]['name']}", bg="#F69814",anchor="w")
    ply1_name_lbl.grid(column=0, row=0,sticky="n")
    ply1_health_lbl=tk.Label(ply1_frm, text=f"Leben:\n\n{players[1]['health']}", bg="#F69814",anchor="w")
    ply1_health_lbl.grid(column=0, row=1,sticky="n")
    ply1_energy_lbl=tk.Label(ply1_frm, text=f"Energie:\n{players[1]['energy']}", bg="#F69814",anchor="w")
    ply1_energy_lbl.grid(column=0, row=2,sticky="n")
    ply1_points_lbl=tk.Label(ply1_frm, text=f"Siegpunkte:\n{players[1]['points']}", bg="#F69814",anchor="w")
    ply1_points_lbl.grid(column=0, row=3,sticky="n")
    # ply1_powers_lbl=tk.Label(ply1_frm, text=f"Powerkarten:\n{players[1]['powers']}", bg="#F69814",anchor="w")
    # ply1_powers_lbl.grid(column=0, row=4,sticky="n")
    #Spieler 2 Inhalt
    ply2_name_lbl=tk.Label(ply2_frm, text=f"Name:\n{players[2]['name']}", bg="#F69814",anchor="w")
    ply2_name_lbl.grid(column=0, row=0,)
    ply2_health_lbl=tk.Label(ply2_frm, text=f"Leben:\n\n{players[2]['health']}", bg="#F69814",anchor="w")
    ply2_health_lbl.grid(column=0, row=1,)
    ply2_energy_lbl=tk.Label(ply2_frm, text=f"Energie:\n{players[2]['energy']}", bg="#F69814",anchor="w")
    ply2_energy_lbl.grid(column=0, row=2,)
    ply2_points_lbl=tk.Label(ply2_frm, text=f"Siegpunkte:\n{players[2]['points']}", bg="#F69814",anchor="w")
    ply2_points_lbl.grid(column=0, row=3,)
    # ply2_powers_lbl=tk.Label(ply2_frm, text=f"Powerkarten:\n{players[2]['powers']}", bg="#F69814",anchor="w")
    # ply2_powers_lbl.grid(column=0, row=4,)
    if player_num == 3 or player_num-1 == 3:
    #Spieler 3 Inhalt:
        ply3_name_lbl=tk.Label(ply3_frm, text=f"Name:\n{players[3]['name']}", bg="#F69814",anchor="w")
        ply3_name_lbl.grid(column=0, row=0)
        ply3_health_lbl=tk.Label(ply3_frm, text=f"Leben:\n\n{players[3]['health']}", bg="#F69814",anchor="w")
        ply3_health_lbl.grid(column=0, row=1)
        ply3_energy_lbl=tk.Label(ply3_frm, text=f"Energie:\n{players[3]['energy']}", bg="#F69814",anchor="w")
        ply3_energy_lbl.grid(column=0, row=2)
        ply3_points_lbl=tk.Label(ply3_frm, text=f"Siegpunkte:\n{players[3]['points']}", bg="#F69814",anchor="w")
        ply3_points_lbl.grid(column=0, row=3)
        # ply3_powers_lbl=tk.Label(ply3_frm, text=f"Powerkarten:\n{players[3]['powers']}", bg="#F69814",anchor="w")
        # ply3_powers_lbl.grid(column=0, row=4)
    else:
        ply3_name_lbl=tk.Label(ply3_frm, text=f"Name:\n---", bg="#F69814",anchor="w")
        ply3_name_lbl.grid(column=0, row=0)
        ply3_health_lbl=tk.Label(ply3_frm, text=f"Leben:\n\n---", bg="#F69814",anchor="w")
        ply3_health_lbl.grid(column=0, row=1)
        ply3_energy_lbl=tk.Label(ply3_frm, text=f"Energie:\n---", bg="#F69814",anchor="w")
        ply3_energy_lbl.grid(column=0, row=2)
        ply3_points_lbl=tk.Label(ply3_frm, text=f"Siegpunkte:\n---", bg="#F69814",anchor="w")
        ply3_points_lbl.grid(column=0, row=3)
        # ply3_powers_lbl=tk.Label(ply3_frm, text=f"Powerkarten:\n---", bg="#F69814",anchor="w")
        # ply3_powers_lbl.grid(column=0, row=4)
    if  player_num == 4:
        #Spieler 4 Inhalt:
        ply4_name_lbl=tk.Label(ply4_frm, text=f"Name:\n{players[4]['name']}", bg="#F69814",anchor="w")
        ply4_name_lbl.grid(column=0, row=0, sticky="n")
        ply4_health_lbl=tk.Label(ply4_frm, text=f"Leben:\n\n{players[4]['health']}", bg="#F69814",anchor="w")
        ply4_health_lbl.grid(column=0, row=1)
        ply4_energy_lbl=tk.Label(ply4_frm, text=f"Energie:\n{players[4]['energy']}", bg="#F69814",anchor="w")
        ply4_energy_lbl.grid(column=0, row=2)
        ply4_points_lbl=tk.Label(ply4_frm, text=f"Siegpunkte:\n{players[4]['points']}", bg="#F69814",anchor="w")
        ply4_points_lbl.grid(column=0, row=3)
        # ply4_powers_lbl=tk.Label(ply4_frm, text=f"Powerkarten:\n{players[4]['powers']}", bg="#F69814",anchor="w")
        # ply4_powers_lbl.grid(column=0, row=4)
    else:
        ply4_name_lbl=tk.Label(ply4_frm, text=f"Name:\n---", bg="#F69814",anchor="w")
        ply4_name_lbl.grid(column=0, row=0, sticky="n")
        ply4_health_lbl=tk.Label(ply4_frm, text=f"Leben:\n\n---", bg="#F69814",anchor="w")
        ply4_health_lbl.grid(column=0, row=1)
        ply4_energy_lbl=tk.Label(ply4_frm, text=f"Energie:\n---", bg="#F69814",anchor="w")
        ply4_energy_lbl.grid(column=0, row=2)
        ply4_points_lbl=tk.Label(ply4_frm, text=f"Siegpunkte:\n---", bg="#F69814",anchor="w")
        ply4_points_lbl.grid(column=0, row=3)
        # ply4_powers_lbl=tk.Label(ply4_frm, text=f"Powerkarten:\n---", bg="#F69814",anchor="w")
        # ply4_powers_lbl.grid(column=0, row=4)
def gui_active_player(name):
    """GUI:Zeigt den aktiven Spieler an.\n
    Zu geben: Welcher Spieler."""
    global active_lbl
    active_lbl.destroy()
    active_lbl = tk.Label(window,text=f"Du bist dran, {name}!", anchor="center", bg="#F69814")
    active_lbl.grid(column=0, row=0, columnspan=4, sticky= 'we')
def gui_tokyo(new_tokyo_player):
    """GUI: Zeigt den aktuellen Spieler in Tokyo an.\n
    Zu geben: Neuer Spieler in Tokyo."""
    global tokyo_lbl
    tokyo_lbl.destroy()
    tokyo_lbl = tk.Label(window,text=f"Aktuell in Tokyo: {new_tokyo_player}!", anchor="center", bg="#F69814")
    tokyo_lbl.grid(column=0, row=2, columnspan=4, sticky= 'we')
def leave_tokyo():
    """GUI: Pop-Up bei Schaden in Tokyo, ob der Spieler in Tokyo bleiben möchte.\n
    Zu geben:-"""
    global tokyo
    stay_or_go = messagebox.askyesno(f"{tokyo} wurde angegriffen!",f"Möchte {tokyo} Tokyo verlassen?")
    return stay_or_go 
def draw_new_cards_gui():
    """GUI Die ersten 3 Powerkarten auslegen\n
    Zu geben:-"""
    draw_new_cards()
    example_name = tk.Label(powercard_frm, text="Name",bg="#F69814",anchor="w")
    example_name.grid(column=1, row=0, sticky="nw")
    example_text = tk.Label(powercard_frm, text="Beschreibung",bg="#F69814",anchor="w")
    example_text.grid(column=1, row=1, sticky="nw")
    example_cost = tk.Label(powercard_frm, text="Kosten",bg="#F69814",anchor="w")
    example_cost.grid(column=0, row=0, sticky="nw")
    card01_check = tk.Radiobutton(powercard_frm, text=slot1, variable=power_var, value= slot1,bg="#F69814",anchor="w")
    card01_check.grid(column=1, row=2, sticky="nw")
    card01_text = tk.Label(powercard_frm, text=card_deck[slot1][0],bg="#F69814",anchor="w")
    card01_text.grid(column=1, row=3, sticky="nw")
    card01_cost = tk.Label(powercard_frm, text=card_deck[slot1][1],bg="#F69814",anchor="w")
    card01_cost.grid(column=0, row=2, sticky="nw")
    card02_check = tk.Radiobutton(powercard_frm, text=slot2, variable=power_var, value=slot2,bg="#F69814",anchor="w")
    card02_check.grid(column=1, row=4, sticky="nw")
    card02_text = tk.Label(powercard_frm, text=card_deck[slot2][0],bg="#F69814",anchor="w")
    card02_text.grid(column=1, row=5, sticky="nw")
    card02_cost = tk.Label(powercard_frm, text=card_deck[slot2][1],bg="#F69814",anchor="w")
    card02_cost.grid(column=0, row=4, sticky="nw")
    card03_check = tk.Radiobutton(powercard_frm, text=slot3, variable=power_var, value= slot3,bg="#F69814",anchor="w")
    card03_check.grid(column=1, row=6, sticky="nw")
    card03_text = tk.Label(powercard_frm, text=card_deck[slot3][0],bg="#F69814",anchor="w")
    card03_text.grid(column=1, row=7, sticky="nw")
    card03_cost = tk.Label(powercard_frm, text=card_deck[slot3][1],bg="#F69814",anchor="w")
    card03_cost.grid(column=0, row=6, sticky="nw")
#------------Spielflächen und Ablauf----------------#
def get_name():
    """GUI/BTN. Spielernamen festlegen, Dopplungen und leere Namen ausfiltern\n
    Zu geben:-"""
    global names, player_num, turnorder, name_ent, tick, player_name
    #Reihenfolge festlegen
    while len(turnorder) != player_num:
        order = random.randint(1,player_num)
        if order not in turnorder:
            turnorder.append(order)
    #Namen kontrollieren
    player_name = (str(player_name.get()))
    if player_name == "" or player_name in names:
        tk.messagebox.showerror("Fehler","Dieser Name ist schon vergeben oder nicht möglich, bitte wähle einen anderen!")
        name_ent.destroy()
        player_name = tk.StringVar()
        name_ent = tk.Entry(name_frm, textvariable=player_name)
        name_ent.grid(column=0, row=1,)
        player_name.set(tk.StringVar())
    else:
        #Spieler erstellen 
        names.append(player_name)
        player_name = {"name":player_name, "points":0, "energy":0, "max_health":10, "health":10, "powers":"", "die": 6, "throws": 3, "dmg": 0, "def": 0, "turnorder": turnorder[tick], "energybonus":0, 
            "alpha":False, "headline":False, "destroy":False, "powerplant":False, "rage":False, "child":False, "canibalism":False, "regen":False, "solar":False, "tank":False, }
        key = player_name["turnorder"]
        players[key] = player_name
        tick += 1
        player_sequence.append(tick)
        name_ent.destroy()
        player_name = tk.StringVar()
        name_ent = tk.Entry(name_frm, textvariable=player_name)
        name_ent.grid(column=0, row=1,)
        player_name.set(tk.StringVar())
        #Wenn fertig, alle GUI Elemente entfernen
        if tick == player_num:
            name_frm.destroy()
            draw_new_cards_gui()
            round_start()
def round_start():
    """GUI Vorbereitung der Runde, Spielphase 1\n
    Zu geben:-"""
    global now_playing, player_now, key_now, name_now, die_now, throws_now, throws_taken, store, final_die 
    update_players(player_num)
    #Start der Runde, alle Variablen zurücksetzen bzw. aktualisieren
    now_playing = 0
    now_playing = 0
    player_now ={}
    key_now = 0
    name_now = ""
    die_now = 0
    throws_now = 0
    throws_taken = 0
    store=[]
    final_die=[]
    now_playing = player_sequence.pop(0)
    player_now = players[now_playing]
    key_now = player_now["turnorder"]
    name_now = player_now["name"]
    die_now = player_now["die"]
    throws_now = player_now["throws"]
    gui_active_player(name_now)
    tk.messagebox.showinfo("Neuer Spieler",f"Du bist dran, {name_now}!")
    throw_die()
def throw_die():
    """GUI Würfel anzeigen und ggf. gespeicherte Würfel mit anzeigen, Spielphase 2\n
    Zu geben:-"""
    global throws_taken, final_die, check01, check02, check03, check04, check05, check06, check07, check08
    global die_keep_btn
    #Werte zurücksetzten
    check01=tk.IntVar()
    check02=tk.IntVar()
    check03=tk.IntVar()
    check04=tk.IntVar()
    check05=tk.IntVar()
    check06=tk.IntVar()
    check07=tk.IntVar()
    check08=tk.IntVar()
    #Würfe mitzählen
    throws_taken +=1
    roll=dice_roll(die_now-len(store))
    dice_value=dice_throw(roll+store)
    #Auswahl erstellen
    die_checkbox(roll+store,dice_value,now_playing)
    #Buttons erstellen
    die_keep_btn = tk.Button(die_frm,text="Noch mal werfen", command=btn_die_save)
    die_keep_btn.grid(column=1, row=7, sticky="nw")
    die_end_btn = tk.Button(die_frm,text="Alle Würfel behalten", command= lambda: btn_die_end(die_end_btn, die_keep_btn))
    die_end_btn.grid(column=1, row=8, sticky="w")
    final_die=roll+store
    #Wenn alle Würfe verbraucht sind, nicht mehr nachwürfeln
    if throws_now == throws_taken:
        die_keep_btn.destroy()
def die_checkbox(int_of_die_in_order,value_of_die_in_order,player):
    """GUI Checkboxen mit Werten anzeigen\n
    Zu geben: Zahlen in Reihenfolge, Bilder in Reihenfolge, Welcher Spieler"""
    global die01, die02, die03, die04, die05, die06, die07, die08, rolls_left
    #Werte zurückstezen, um Dopplungen zu verhindern
    rolls_left.destroy()
    die01.destroy()
    die02.destroy()
    die03.destroy()
    die04.destroy()
    die05.destroy()
    die06.destroy()
    #Auswahlbildschirm aufbauen
    rolls_left = tk.Label(die_frm,text=f"Du hast noch {throws_now-throws_taken} Würfe!", anchor="w", bg="#F69814")
    rolls_left.grid(column=0, row=0, sticky="nw")
    die01 = tk.Checkbutton(die_frm, text=value_of_die_in_order[0], anchor="w", bg="#F69814", variable=check01, onvalue=int_of_die_in_order[0],)
    die01.grid(column=0, row=1, sticky="nw")
    die02 = tk.Checkbutton(die_frm, text=value_of_die_in_order[1], anchor="w", bg="#F69814", variable=check02, onvalue=int_of_die_in_order[1],)
    die02.grid(column=0, row=2, sticky="nw")
    die03 = tk.Checkbutton(die_frm, text=value_of_die_in_order[2], anchor="w", bg="#F69814", variable=check03, onvalue=int_of_die_in_order[2],)
    die03.grid(column=0, row=3, sticky="nw")
    die04 = tk.Checkbutton(die_frm, text=value_of_die_in_order[3], anchor="w", bg="#F69814", variable=check04, onvalue=int_of_die_in_order[3],)
    die04.grid(column=0, row=4, sticky="nw")
    die05 = tk.Checkbutton(die_frm, text=value_of_die_in_order[4], anchor="w", bg="#F69814", variable=check05, onvalue=int_of_die_in_order[4],)
    die05.grid(column=0, row=5, sticky="nw")
    die06 = tk.Checkbutton(die_frm, text=value_of_die_in_order[5], anchor="w", bg="#F69814", variable=check06, onvalue=int_of_die_in_order[5],)
    die06.grid(column=0, row=6, sticky="nw")
    #Fähigkeiten aktivieren
    if players[player]["die"] == 7 or players[player]["die"]>6:
        die07.destroy()
        die07 = tk.Checkbutton(die_frm, text=value_of_die_in_order[6], anchor="w", bg="#F69814", variable=check07, onvalue=int_of_die_in_order[6],)
        die07.grid(column=0, row=7, sticky="nw")
    if players[player]["die"] == 8:
        die08.destroy()
        die08 = tk.Checkbutton(die_frm, text=value_of_die_in_order[7], anchor="w", bg="#F69814", variable=check08, onvalue=int_of_die_in_order[7],)
        die08.grid(column=0, row=8, sticky="nw")
def btn_die_save():
    """GUI/BTN: Die Checkbox Der Würfel auswerten\n
    Zu geben:-"""
    global die_now
    global store
    global die_frm
    keepers=[]
    if check01.get() != 0:
        keepers.append(check01.get())
    if check02.get() != 0:
        keepers.append(check02.get())
    if check03.get() != 0:
        keepers.append(check03.get())
    if check04.get() != 0:
        keepers.append(check04.get())
    if check05.get() != 0:
        keepers.append(check05.get())
    if check06.get() != 0:
        keepers.append(check06.get())
    if die_now == 7 or die_now>6:
        if check07.get() != 42:
            keepers.append(check07.get())
        die07.destroy()
    if die_now == 8:
        if check08.get() != 42:
            keepers.append(check08.get())
        die07.destroy() 
    die_frm.destroy()
    die_frm = tk.LabelFrame(window,bg='#F69814', text="Würfelfeld")
    die_frm.grid(column=1, row=3, columnspan=2, sticky= 'we',padx=13,pady=10)
    die_frm.columnconfigure(0,weight=2)      
    store=keepers
    throw_die()
def btn_die_end(button, save_button):
    """GUI Würfel auswerten, Spielphase 3.\n
    Zu geben: gedrückter Button, anderer Button im Würfelfeld"""
    global tokyo, tokyo_player, die_end_btn
    button.destroy()
    save_button.destroy()
    #Würfel verarbeiten
    health0 = add_health(final_die,player_now) #Leben
    energy0 = add_energy(final_die,player_now) #Energie
    dmg0 = add_dmg(final_die,player_now)       #Schaden
    points0 = add_points(final_die,player_now) #Siegpunkte
    #Fähigkeiten aktivieren
    if player_now["destroy"]:
        if 1 in final_die and 2 in final_die  and 3 in final_die  and 4 in final_die  and 5 in final_die  and 6 in final_die:
            player_now["points"] += 9
            tk.messagebox.showinfo("Aktivierung",f"Totale Zerstörung! Du hast nun {player_now['points']} Siegpunkte.")
    if player_now["child"]:
        if energy0 > 0:
            energy0 += 1
            tk.messagebox.showinfo("Aktivierung","Die Kinder lieben dich und schenken dir Ihre Kraft!")
    update_players(player_num)
    #Ergebnisse verteilen:
    #Leben
    if health0 > 0:
        #Fähigkeiten aktivieren
        if player_now["regen"]:
            health0 += 1
            tk.messagebox.showinfo("Aktivierung","Deine Kräfte haben die Heilung verstärkt!")
        #Check ob Heilung und wie viel    
        if tokyo == name_now:
            tk.messagebox.showinfo("Heilung","Du bist in Tokyo und kannst dich nicht heilen.")
        elif player_now["max_health"] == player_now["health"]:
            tk.messagebox.showinfo("Heilung","Du hast schon volle Lebenspunkte.")
        else:
            player_now["health"] += health0
            if player_now["health"] > player_now["max_health"]:
                player_now["health"] = player_now["max_health"]
            tk.messagebox.showinfo("Heilung",f"Du hast dich geheilt! Du hast nun {player_now['health']} Lebenspunkte!")
        update_players(player_num)
    #Energie
    if energy0 > 0:
        player_now["energy"] += energy0
        tk.messagebox.showinfo("Energie",f"Du hast nun {player_now['energy']} Energie!")
    update_players(player_num)
    #Siegpunkte
    if points0 > 0:
        player_now["points"] += points0
        tk.messagebox.showinfo("Siegpunkte",f"Du hast nun {player_now['points']} Siegpunkte!")
        if player_now["points"] >= 20:
            tk.messagebox.showinfo("The winner is you!",f"Glückwunsch! {name_now} ist der King of Tokio mit {player_now['points']} Siegpunkten!\nDanke fürs spielen!")
            quit()
        update_players(player_num)
    #Schaden verteilen:
    if dmg0 > 0:
        #Fähigkeiten aktivieren
        if player_now["alpha"]:
            player_now["points"] += 1
            tk.messagebox.showinfo("Aktivierung",f"Du bist das Alpha Monster! Du bekommst 1 Siegpunkt und hast nun {player_now['points']} Siegpunkte!")
            if player_now["points"] >= 20:
                tk.messagebox.showinfo("The winner is you!",f"Glückwunsch! {name_now} ist der King of Tokio mit {player_now['points']} Siegpunkten!\nDanke fürs spielen!")
                quit()
            update_players(player_num)
        if player_now["tank"] and dmg0 >= 3:
            player_now["points"] += 2
            tk.messagebox.showinfo("Aktivierung",f"Und schon wieder fliegen Panzer durch die Luft! Du bekommst 2 Siegpunkte und hast nun {player_now['points']} Siegpunkte!")
            if player_now["points"] >= 20:
                tk.messagebox.showinfo("The winner is you!",f"Glückwunsch! {name_now} ist der King of Tokio mit {player_now['points']} Siegpunkten!\nDanke fürs spielen!")
                quit()
            update_players(player_num)
        if player_now["canibalism"]:
            if player_now["health"] < player_now["max_health"]:
                player_now["health"] += 1
                tk.messagebox.showinfo("Aktivierung",f"Du nährst dich an deinen Gegnern! Du hast dich geheilt und hast nun {player_now['health']} Lebenspunkte!")
                update_players(player_num) 
            else:
                tk.messagebox.showinfo("Aktivierung","Du nährst dich an deinen Gegnern! Aber du hast schon volles Leben.")
        #Schaden auswerten und bestimmen wer Schaden bekommt
        if tokyo == 0:
            tk.messagebox.showinfo("Angriff",f"Als erster Spieler kannst du keinen Schaden verteilen.")
        elif tokyo == name_now:
            for dmg_target in player_sequence:
                attack(dmg_target,dmg0)
                update_players(player_num)
                gui_tokyo(tokyo)
        elif tokyo != name_now:
            attack(tokyo_player,dmg0)
            update_players(player_num)
            gui_tokyo(tokyo)
        if len(player_sequence) < 1:
            tk.messagebox.showinfo("The winner is you!",f"{name_now} ist das letzte Monster, niemand kann dich aufhalten!\n\nHerzlichen Glückwunsch {name_now}, Du bist der King of Tokyo!!!")
            quit()
    #Geht es nach Tokyo oder gibt es Punkte:
    #Tokyo leer
    if tokyo == 0:
        tokyo = name_now
        tokyo_player = now_playing
        gui_tokyo(tokyo)
        player_now["points"]+=1
        tk.messagebox.showinfo("Tokyo",f"{name_now} hat Tokyo eingenommen!\n{name_now} hat nun {player_now['points']} Siegpunkte!")
        update_players(player_num)
        if player_now["points"] >= 20:
            tk.messagebox.showinfo("The winner is you!",f"{name_now} ist unaufhaltbar und hat genug Siegpunkte gesammelt!\n\nHerzlichen Glückwunsch {name_now}, Du bist der King of Tokyo!!!")
            quit()
    #Tokyo von Spieler besetzt
    elif tokyo == name_now:
        player_now["points"]+=2
        tk.messagebox.showinfo("Tokyo",f"{name_now} tobt weiterhin in Tokyo und hat nun {player_now['points']} Siegpunkte!")
        update_players(player_num)
        if player_now["points"] >= 20:
            tk.messagebox.showinfo("The winner is you!",f"{name_now} ist unaufhaltbar und hat genug Siegpunkte gesammelt!\n\nHerzlichen Glückwunsch {name_now}, Du bist der King of Tokyo!!!")
            quit()
    buy_powers_gui()
def buy_powers_gui():
    """GUI Powerkarten kaufen, Spielphase 4.\n
    Zu geben:-"""
    global powercard_frm
    #Frame zerstören, um dopplungen zu vermeiden
    powercard_frm.destroy()
    #Frame mit aktuellen Werten aufbauen
    powercard_frm = tk.Frame(window,bg='#F69814',padx=13,pady=10)
    powercard_frm.grid(column=0,row=4,columnspan=4,padx=13,pady=10)
    powercard_frm.columnconfigure(0,weight=2)
    powercard_frm.rowconfigure(1,weight=0,)
    example_name = tk.Label(powercard_frm, text="Name",bg="#F69814",anchor="w")
    example_name.grid(column=1, row=0, sticky="nw")
    example_text = tk.Label(powercard_frm, text="Beschreibung",bg="#F69814",anchor="w")
    example_text.grid(column=1, row=1, sticky="nw")
    example_cost = tk.Label(powercard_frm, text="Kosten",bg="#F69814",anchor="w")
    example_cost.grid(column=0, row=0, sticky="nw")
    card01_check = tk.Radiobutton(powercard_frm, text=slot1, variable=power_var, value= slot1,bg="#F69814",anchor="w")
    card01_check.grid(column=1, row=2, sticky="nw")
    card01_text = tk.Label(powercard_frm, text=card_deck[slot1][0],bg="#F69814",anchor="w")
    card01_text.grid(column=1, row=3, sticky="nw")
    card01_cost = tk.Label(powercard_frm, text=card_deck[slot1][1],bg="#F69814",anchor="w")
    card01_cost.grid(column=0, row=2, sticky="nw")
    card02_check = tk.Radiobutton(powercard_frm, text=slot2, variable=power_var, value=slot2,bg="#F69814",anchor="w")
    card02_check.grid(column=1, row=4, sticky="nw")
    card02_text = tk.Label(powercard_frm, text=card_deck[slot2][0],bg="#F69814",anchor="w")
    card02_text.grid(column=1, row=5, sticky="nw")
    card02_cost = tk.Label(powercard_frm, text=card_deck[slot2][1],bg="#F69814",anchor="w")
    card02_cost.grid(column=0, row=4, sticky="nw")
    card03_check = tk.Radiobutton(powercard_frm, text=slot3, variable=power_var, value= slot3,bg="#F69814",anchor="w")
    card03_check.grid(column=1, row=6, sticky="nw")
    card03_text = tk.Label(powercard_frm, text=card_deck[slot3][0],bg="#F69814",anchor="w")
    card03_text.grid(column=1, row=7, sticky="nw")
    card03_cost = tk.Label(powercard_frm, text=card_deck[slot3][1],bg="#F69814",anchor="w")
    card03_cost.grid(column=0, row=6, sticky="nw")
    #Buttons erstellen
    buy_card = tk.Button(powercard_frm, text="Kaufen", command= lambda: buy_power(power_var.get(),player_now["energy"]))
    end_buy_card = tk.Button(powercard_frm, text="Beenden", command= lambda: end_shopping(end_buy_card, reset_card, buy_card))
    end_buy_card.grid(column=1, row=8, sticky="nw")
    reset_card = tk.Button(powercard_frm, text="Für 2 Energie neue Karten", command= lambda: new_cards_buy(player_now))
    #Wenn zu wenig Energie, bleiben die Buttons weg
    if player_now["energy"] >= 2:
        buy_card.grid(column=0, row=8, sticky="nw")
        reset_card.grid(column=0, row=9, sticky="nw")
    #Fähigkeiten aktivieren
    if player_now["energybonus"] > 0:
        tk.messagebox.showinfo("Aktivierung","Kosten für dich je 1 Energie weniger")
def new_cards_buy(player):
    """Alle Karten auswechseln\n
    Zu geben: Aktiver Spieler"""
    player["energy"] -= 2
    draw_new_cards()
    update_players(player_num)
    buy_powers_gui()
def end_shopping(btn1, btn2, btn3):
    """GUI Runde beenden, Spielphase 5.\n
    Zu geben: Die drei Buttons im Powerkarten Frame"""
    #Buttons entfernen
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    #Fähigkeiten aktivieren
    if player_now["powerplant"]:
        if player_now["energy"] >= 6:
            bonus = int(player_now["energy"]/6)
            player_now["points"] += bonus
            tk.messagebox.showinfo("Aktivierung",f"Du bist voller Energie! Neue Siegpunkte: {player_now['points']}!")
            update_players(player_num)
    if player_now["solar"]:
        if player_now["energy"] == 0:
            player_now["energy"] += 1
            tk.messagebox.showinfo("Aktivierung","Die Sonne schenkt dir Energie!")
            update_players(player_num)
    if len(player_sequence) == 0:
        tk.messagebox.showinfo("Thw winner is you!",f"Du hast alle anderen Spieler besiegt! {name_now} ist King of Tokyo!")
        quit()
    elif player_now["points"] >= 20:
        tk.messagebox.showinfo("The winner is you!",f"{name_now} hat die Macht an dich gerissen! Du bist King of Tokyo!")
        quit()
    #Nächsten Spieler festlegen    
    if player_now["rage"]:
        player_sequence.insert(0,player_now["turnorder"])
        player_now["rage"]=False
        tk.messagebox.showinfo("Aktivierung","Du bist im Blutrausch und machst direkt weiter!")
    else:    
        player_sequence.append(now_playing)
    #Erneuter Start bei Spielphase 1
    round_start()
#-----------Spielstart------------------------------#
#Einleitung und Spielerzahl festlegen:
manual = tk.messagebox.askquestion("King of Tokyo","Möchtest du die Spielregeln lesen?")
if manual == "yes":
    tk.messagebox.showinfo("King of Tokyo,","""    Ziel des Spieles ist es entweder als erster 20 Siegpunkte zu erreichen oder alle anderen Monster zu besiegen.
    Zu Beginn des Spieles startet jeder mit 10 Lebenspunkten, Lebenspunktlimit von 10, 0 Energie und 0 Siegpunkten.
    Außerdem beginnt jeder mit 6 Würfeln und der Möglichkeit, bis zu 3-mal neu zu würfeln. 
    Ihr habt pro Runde die Möglichkeit zu würfeln, zu Beginn immer mit 6 Würfeln und 3 Versuchen.
    Nach jedem Wurf könnt ihr Würfel zurücklegen, welche ihr behalten wollt, um nur die Restlichen neu zu würfeln.
    Wollt ihr alle Würfel neu würfeln, einfach bei 'welche Würfel willst du speichern' keine Zahl eingeben.
    Wenn euch euer Ergebnis gefällt oder alle Versuche verbraucht sind wird ausgewertet. 
    1, 2 & 3 geben euch Siegpunkte, wenn ich mindestens 3 gleiche Zahlen habt. 
    111 = 1 Siegpunkt
    222 = 2 Siegpunkte
    333 = 3 Siegpunkte
    Für jede weitere gleiche Zahl bekommt ihr noch mal einen Siegpunkt extra! z. B:
    1111 = 2 Siegpunkte (1 Siegpunkt für '111' + 1 Siegpunkt für die zusätzliche 1)
    2222 = 3 Siegpunkte (2 Siegpunkte für '222' + 1 Siegpunkt für die zusätzliche 2)
    111111 = 4 Siegpunkte (1 Siegpunkt für '111' + 3 Siegpunkte für die drei zusätzlichen 1)
    Energie gibt euch pro erwürfelter Energie 1 Energiepunkt, welcher euch bleibt, bis ihr ihn ausgebt, für z. B. Powerkarten.
    Herzen heilen euch pro gewürfeltem Herz um 1 Lebenspunkt, aber nicht über eure maximalen Lebenspunkte.
    Du kannst dich nicht durch Würfel heilen, wenn du in Tokyo bist!
    Tatzen fügen anderen Spielern Schaden zu, je nachdem, wo ihr steht.
    Wenn du in Tokyo bist, fügst du allen anderen Monstern gleichzeitig Schaden zu.
    Wenn du nicht in Tokyo bist, fügst du nur dem Monster in Tokyo Schaden zu.
    Das Monster in Tokyo darf, nachdem es Schaden bekommen hat, entscheiden, ob es Tokyo verlassen möchte.
    Sollte es Tokyo verlassen, geht der Spieler, welcher den Schaden ausgeteilt hat, als neues Monster nach Tokyo.
    Aber warum sollte man nach Tokyo wollen?
    Die Vorteile:
    - Wenn du Tokyo betrittst, bekommst du direkt 1 Siegpunkt.
    - Solltest du dich zu Beginn deiner Runde schon in Tokyo befinden, bekommst du sogar 2 Siegpunkte.
    - Du kannst alle anderen Monster angreifen.
    Die Nachteile:
    - Du kannst dich nicht mit Würfeln heilen.
    - Alle anderen Spieler greifen nur dich an.
    Du siehst Tokyo ist Fluch und Segen zugleich, besonders, da du es nur verlassen kannst, nachdem du Schaden bekommen hast.
    Aber das kannst du auch zu deinem Vorteil nutzen, wie wirst du nach einigen Runden selbst herausfinden.
    Kommen wir nun zu den Powerkarten:
    Diese kannst du am Ende deines Zuges für Energiepunkte kaufen. Es stehen immer 3 Karten zur Verfügung.
    Falls dir keine der Karten gefällt, gibt es auch die Möglichkeit, für 2 Energiepunkte neue Karten auszulegen.
    Energiekarten haben alle möglichen Eigenschaften, ob sie dir nun direkt Siegpunkte oder Lebenspunkte geben, dein maximales Leben erhöhen. 
    Oder dir sogar mehr Würfel geben, mit Powerkarten kannst du das Spiel zu deinen Gunsten wenden und dir einen Vorteil verschaffen.
    Sollte ein Monster alle Lebenspunkte verlieren, ist es aus dem Spiel und die restlichen Spieler machen weiter.
    Wenn ein Monster mindestens 20 Siegpunkte hat, endet das Spiel sofort, und dieses Monster hat gewonnen.
    Solltest du noch weitere Fragen haben: Per Onlinesuche oder im Dateiordner findet sich die offizielle Anleitung des King of Tokyo.
    Und nun viel Spaß mit dem Spiel!
    """)
how_many = tk.messagebox.askquestion("Starte das Spiel", "Seid ihr mehr als zwei Spieler?")
if how_many == "yes":
    how_many = tk.messagebox.askquestion("Starte das Spiel", "Seid ihr mehr als drei Spieler?")
    if how_many == "yes":
        player_num = 4
    else:
        player_num =3
else:
    player_num =2
#Das erste Fenster zur Eingabe der Namen
name_lbl = tk.Label(name_frm, text="Gebt nun nacheinander den Namen eures Monsters ein:", bg="#F69814")
name_lbl.grid(column=0, row=0,)
player_name = tk.StringVar(name_frm)
name_ent = tk.Entry(name_frm, textvariable=player_name)
name_ent.grid(column=0, row=1,)
name_btn = tk.Button(name_frm, text="Bestätigen", command=get_name)
name_btn.grid(column=0, row=2,)

stay_open = input() #Terminal Input um das Fenster offen zu halten
window = tk.Tk()
tk.Tk.update(window)