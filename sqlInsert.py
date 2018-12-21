#Nick Soetaert


'''
insert into Move
values
('00000', 1, 'e4', 'e5');
---

---
[Event "Live Chess"]
[Site "Chess.com"]
[Date "2018.12.01"]
[White "CanIUndoThatMove"]
[Black "gedebuk123"]
[Result "0-1"]
[ECO "B57"]
[WhiteElo "1368"]
[BlackElo "1359"]
[TimeControl "300"]
[EndTime "13:56:55 PST"]
[Termination "gedebuk123 won on time"]
[CurrentPosition "8/8/4K3/5p2/5k2/8/8/8 w - - 0 64"]

1.e4 c5 2.Bc4 d6 3.Nc3 Nc6 4.Nf3 Nf6 5.d4 cxd4 6.Nxd4 a6 7.b3 e6 8.Bb2 Be7 9.Qd2 O-O 10.O-O-O Qc7 11.f4 b5 12.Bd3 Bb7 13.Nf3 Nb4 14.e5 Nxd3+ 15.Qxd3 dxe5 16.fxe5 Rfd8 17.Qe2 Ng4 18.h3 Bxf3 19.gxf3 Nxe5 20.Nxb5 Rxd1+ 21.Rxd1 axb5 22.Qxe5 Qxe5 23.Bxe5 Rxa2 24.Rd7 Bg5+ 25.Kb1 Ra8 26.Rb7 h6 27.Rxb5 Kh7 28.c4 Kg6 29.c5 f6 30.Bd6 Rc8 31.b4 Kf7 32.Rb7+ Ke8 33.Rb8 Rxb8 34.Bxb8 Kd7 35.b5 Kc8 36.Bd6 f5 37.Kc2 Bd8 38.Kd3 Kb7 39.Be5 g6 40.Kc4 Be7 41.Bd6 Bd8 42.c6+ Kb6 43.Bc5+ Kc7 44.Bd4 Kb8 45.Kc5 Kc7 46.b6+ Kb8 47.c7+ Bxc7 48.bxc7+ Kxc7 49.Bf6 Kd7 50.Kd4 Kd6 51.Ke3 g5 52.f4 gxf4+ 53.Kxf4 Kd5 54.h4 Kd6 55.Bg7 Ke7 56.Bxh6 Kf6 57.Bg5+ Kg6 58.Bd8 Kh5 59.Bc7 Kxh4 60.Ke5 Kh5 61.Kxe6 Kg5 62.Bd6 Kg4 63.Bf4 Kxf4  0-1
'''

filename = input("Please enter filename, without the .pgn: ")
gameid = input("Please enter 5-digit game ID: ")

filename += ".pgn"

moveNum = ""
whiteMove = ""
blackMove = ""


file = open(filename, "r")
tempFile = open("temp", "w+")


#Get rid of first 15 lines of header
x = 0
for line in file:
    if (x >= 14):
        tempFile.write(line)
    x = x+1

file.close()
tempFile.close()


finalFile = open("cleanGame" + gameid, "w+")
tempFile = open("temp", "r")

l = tempFile.readlines()
s = "".join(l)

i = 0

while(i < len(s)):

    if((whiteMove != "") and (blackMove != "") and (moveNum != "")):
        finalFile.write("insert into Move\nvalues\n(\'" + str(gameid) + "\', " + str(moveNum) + ", \'" + str(whiteMove) + "\', \'" + str(blackMove) + "\');\n\n")
        whiteMove = ""
        blackMove = ""
        moveNum = ""

    if((s[i] == "0") or (s[i] == "1")
    or (s[i] == "2") or (s[i] == "3") 
    or (s[i] == "4") or (s[i] == "5") 
    or (s[i] == "6") or (s[i] == "7") 
    or (s[i] == "8") or (s[i] == "9")):

        moveNum += s[i]
        i+=1

    elif(s[i] == "."):

        i+=1
        #readyToPrint = True;

    else:
        while((i < len(s)) and (s[i] != " ")):
            whiteMove += s[i]
            i += 1

        #whitespace after move
        i+=1

        while((i < len(s)) and (s[i] != " ")):
            blackMove += s[i]
            i+=1

        #whitespace after move
        i+=1

        if (i == len(s)):
            break


finalFile.close()
