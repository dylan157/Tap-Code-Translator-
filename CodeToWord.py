#!/usr/bin/env python 
import re
print "CodeToWord 2.0"
print ""

def Master():
    print "############################## vvvvvv"
    Input = raw_input("Enter text or code for translating -")

    def CodeToWordNAV(InputIn):
        
        def CodeToWord(In): # converts code to letters
                    def Start_code_to_word(Code):
                        
                            print ""


                            ###input code
                            Code_input = Code

                            ###convert code to list
                        
                            Code_list = re.sub(" ", " ",  Code_input).split()
                        
                            #print Code_list
                            print ""
                            ###looks for code and creates a new string
                            def Code_to_word(mist):
                                    Processed_code = ""
                                    for Numbers in mist:        
                                            if "11" in Numbers:
                                                Processed_code = Processed_code + "a"
                                            if "12" in Numbers:
                                                Processed_code = Processed_code + "b"
                                            if "13" in Numbers:
                                                Processed_code = Processed_code + "c"
                                            if "14" in Numbers:
                                                Processed_code = Processed_code + "d"
                                            if "15" in Numbers:
                                                Processed_code = Processed_code + "e"
                                            if "21" in Numbers:
                                                Processed_code = Processed_code + "f"
                                            if "22" in Numbers:
                                                Processed_code = Processed_code + "g"
                                            if "23" in Numbers:
                                                Processed_code = Processed_code + "h"
                                            if "24" in Numbers:
                                                Processed_code = Processed_code + "i"
                                            if "25" in Numbers:
                                                Processed_code = Processed_code + "j"
                                            if "31" in Numbers:
                                                Processed_code = Processed_code + "l"    
                                            if "32" in Numbers:
                                                Processed_code = Processed_code + "m"
                                            if "33" in Numbers:
                                                Processed_code = Processed_code + "n"
                                            if "34" in Numbers:
                                                Processed_code = Processed_code + "o"
                                            if "35" in Numbers:
                                                Processed_code = Processed_code + "p"
                                            if "41" in Numbers:
                                                Processed_code = Processed_code + "q"
                                            if "42" in Numbers:
                                                Processed_code = Processed_code + "r"
                                            if "43" in Numbers:
                                                Processed_code = Processed_code + "s"
                                            if "44" in Numbers:
                                                Processed_code = Processed_code + "t"
                                            if "45" in Numbers:
                                                Processed_code = Processed_code + "u"
                                            if "51" in Numbers:
                                                Processed_code = Processed_code + "v"
                                            if "52" in Numbers:
                                                Processed_code = Processed_code + "w"
                                            if "53" in Numbers:
                                                Processed_code = Processed_code + "x"
                                            if "54" in Numbers:
                                                Processed_code = Processed_code + "y"
                                            if "55" in Numbers:
                                                Processed_code = Processed_code + "z"
                                            if "0" in Numbers:
                                                Processed_code = Processed_code + " "
                                            if "66" in Numbers:
                                                Processed_code = Processed_code + "k"
                                            if "?" in Numbers:
                                                Processed_code = Processed_code + "?"

                                    if len(Processed_code) > 0:
                                            return Processed_code
                                    else:
                                        Processed_code = "EMPTY" 
                                        return Processed_code


                            print "Text = " + Code_to_word(Code_list)
                            print ""
                            print "############################## ^^^^^"
                    Start_code_to_word(In)    

        def WordToCode(In): #Converts letters to code
                    def Start_word_to_code(Word):
                            debug = False
                            Text_Input = Word
                            if "d3bug" in Text_Input:
                                debug = True
                                Text_Input = re.sub("d3bug ","",Text_Input,count=1)

                            #Split_words makes each word in Text_input a single list item
                            Split_words = re.sub(" ", " ",  Text_Input).split()


                            #This loop adds "0" to the end of each word in Split_words. "0" represents a space when traslated.
                            Words_Plus_0 = []
                            for x in Split_words:
                                    Words_Plus_0.append (x + "0")


                            #This loop connects all the text back to a single word. (EG. ['hello0', 'there0'] --> 'hello0there0' )
                            Rejoint_words = ""
                            for x in Words_Plus_0:
                                    Rejoint_words = Rejoint_words + x


                            #lowers text to avoid unreadable capital letters
                            Lowered_Rejoint_words = Rejoint_words.lower()

                        
                            #Spaced_Characters adds spaced between each letter. (EG. "hello0" --> "h e l l o 0")                                               
                            Spaced_Characters = (" ".join(Lowered_Rejoint_words))

                        
                            #Spaced_Characters_List makes each letter a single list item. (EG. h i 0 --> ['h', 'i', '0'])
                            Spaced_Characters_List = re.sub(" ", " ",  Spaced_Characters).split()

                        

                            print ""

                            if debug == True: #Debug block
                                print ""
                                print "DEBUG V-V-V"
                                print Split_words
                                print Words_Plus_0
                                print Rejoint_words
                                print Lowered_Rejoint_words
                                print Spaced_Characters
                                print Spaced_Characters_List
                                print "DEBUG ^-^-^"
                                print ""

                            L2c = {
                                'a': '11 ',
                                'b': '12 ',
                                'c': '13 ',
                                'd': '14 ',
                                'e': '15 ',
                                'f': '21 ',
                                'g': '22 ',
                                'h': '23 ',
                                'i': '24 ',
                                'j': '25 ',
                                'l': '31 ',
                                'm': '32 ',
                                'n': '33 ',
                                'o': '34 ',
                                'p': '35 ',
                                'q': '41 ',
                                'r': '42 ',
                                's': '43 ',
                                't': '44 ',
                                'u': '45 ',
                                'v': '51 ',
                                'w': '52 ',
                                'x': '53 ',
                                'y': '54 ',
                                'z': '55 ',
                                '?': '? ',
                                '0': '0 '
                                }


                            #This function looks at each letter in Spaced_Characters_list and creates a string with the converted code.
                            def Word_To_Code(Spaced_Characters_List):
                                W2C_Result = ""
                                for x in Spaced_Characters_List:
                                    if x in L2c:
                                        W2C_Result = W2C_Result + L2c[x]
                                    else:
                                        W2C_Result = W2C_Result + "?"

                                if len(W2C_Result) > 0:       
                                    return W2C_Result



                            TrancelateWordToCode = Word_To_Code(Spaced_Characters_List)
                            print "Code = " + str(TrancelateWordToCode) 
                            print "############################## ^^^^^"
                    Start_word_to_code(In)    
     
        def CodeOrWord(text):
            Split_words = re.sub(" ", " ",  text[:50]).split()
            CodeContents = ["11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55", "66", "?"]
            StrWords = ""
            for items in Split_words[:100]:
                StrWords += items
            #print StrWords + " DEBUG STRWORDS"
            regex = re.compile('[a-z]')
            length = regex.findall(StrWords) 


            if  len(length) > (len(StrWords)  / 2):
                print ""                
                print "Translating word to code"
                WordToCode(text)
            else:
                print "Translating code to word"
                CodeToWord(text)
    
        def Restart():
                    print ""
                    again = raw_input("again? (y,n)")
                    print ""
                    if again == "y":
                            Master()
                    elif again == "n":
                         print "Bye!"   
                    else:
                        Restart()
                         



        CodeOrWord(InputIn)
        Restart()
    CodeToWordNAV(Input)
Master()


