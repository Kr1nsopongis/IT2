import keyboard

startVerdi = 12

plassVerdi = {
    "1" : ["VN","-"],
    "2" : ["MN","-"],
    "3" : ["HN","-"],
    "11" : ["VM","-"],
    "12" : ["MM","_"],
    "13" : ["HM","-"],
    "21" : ["HO","-"],
    "22" : ["MO","-"],
    "23" : ["VO","-"],
}
print("Velkommen til tik tak toe!")
print(f"Spillebrettet:\n{plassVerdi['23'][1]} {plassVerdi['22'][1]} {plassVerdi['21'][1]}\n{plassVerdi['13'][1]} {plassVerdi['12'][1]} {plassVerdi['11'][1]}\n{plassVerdi['3'][1]} {plassVerdi['2'][1]} {plassVerdi['1'][1]}")

while True:
    if keyboard.is_pressed("left arrow"):
        startVerdi = startVerdi -1
    if keyboard.is_pressed("left arrow"):
    if keyboard.is_pressed("left arrow"):
    if keyboard.is_pressed("left arrow"):
