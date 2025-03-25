import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self):
        txtIn=replaceChars(self._view.txtIn.value.lower())
        words =txtIn.split()

        txtIn.value = ""

        modality = self._view.getRicerca()
        language = self._view.getLanguage().lower
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                tempo = t2-t1
                self._view.txtOut.controls.append(ft.Text(paroleErrate))
                self._view.txtOut.controls.append(ft.Text(f"tempo impiegato: {tempo}"))
                self._view.page.update()

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                tempo = t2 - t1
                self._view.txtOut.controls.append(ft.Text(paroleErrate))
                self._view.txtOut.controls.append(ft.Text(f"tempo impiegato: {tempo}"))
                self._view.page.update()

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                tempo = t2 - t1
                self._view.txtOut.controls.append(ft.Text(paroleErrate))
                self._view.txtOut.controls.append(ft.Text(f"tempo impiegato: {tempo}"))
                self._view.page.update()
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text