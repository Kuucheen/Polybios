from sty import fg
import os, sys
if sys.platform == "win32":
    os.system('color')

end = False
while end == False:
        print(f"""{fg(33)} ____  _____  __   _  _  ____  ____  _____  ___ 
{fg(69)}(  _ \(  _  )(  ) ( \/ )(  _ \(_  _)(  _  )/ __)
{fg(105)} )___/ )(_)(  )(__ \  /  ) _ < _)(_  )(_)( \__ \ 
{fg(177)}(__)  (_____)(____)(__) (____/(____)(_____)(___/""")
        
        print(f"\n\n{fg(177)}You are using the automated version of PolyBios rn if you want to use the manual version dm Kuchen#2472\n")

        inp = input(f"{fg(212)}Text/Encrypted: ")

        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '?', '.', '+', '-', '*', '#']
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        temp = inp.replace(" ", "")
        temp = temp.lower()
        temp = list(temp)
        
        if temp[0] in abc:
                abc = 'abcdefghijklmnopqrstuvwxyz!?.+-*#'
                enc = ['11', '12', '13', '14', '15', '16', '21', '22', '23', '24', '25', '26', '31', '32', '33', '34', '35', '36', '41', '42', '43', '44', '45', '46', '51', '52', '53', '54', '55', '56', '61', '62', '63', '64', '65', '66']
                inp = inp.lower()
                inp = inp.replace(" ", "")
                inp = list(inp)
                print("Detected: Normal Text\n")
                for i in inp:
                        x = abc.find(i)
                        print(enc[x], end=" ")
        elif temp[0] in num:
                enc = '11..12..13..14..15..16..21..22..23..24..25..26..31..32..33..34..35..36..41..42..43..44..45..46..51..52..53..54..55..56..61..62..63..64..65..66'
                abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '?', '.', '+', '-', '*', '#']
                inp = inp.split(" ")
                print("Detected: Encrypted Text\n")
                for i in inp:
                        x = enc.find(i)
                        print(abc[x//4], end=" ")
        else:
                print("\nCouldnt detect any encryption or you used more unicode characters than supported")

        print(f"{fg(206)}\n\n          REPEAT\n[1] Yes           [2] No")
        temp = input("")
        os.system("cls")
        if temp != "1":
                end = True


 
