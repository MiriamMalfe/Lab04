import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self):
        txtIn=replaceChars(self._view.txtIn.value.lower())
        words =txtIn.split()  #splitta il mio testo in  ingresso e me lo mette in una lista

        txtIn.value = ""    #azzero valore di txtIn così se dopo mi serve vuoto ce l'ho pronto

        modality = self._view.getRicerca()
        language = self._view.getLanguage().lower
        paroleErrate = " - "  #stringa che verrà stampata con dentro le parole errate

        match modality:   #controllo in che modalità sono
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

#posso farlo anche nel model
def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text