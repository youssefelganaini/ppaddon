import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")


openai.api_key = OPENAI_KEY

# prompt = """
#     -----

#     Deine Aufgabe: Überprüfung einer PowerPoint-Präsentation auf Qualität und Konsistenz

#     Ziel: Sicherstellen, dass die Präsentation keine Rechtschreib- und Grammatikfehler enthält und dass der Text konsequent und einheitlich formuliert ist.

#     Details:
#     Rechtschreibung und Grammatik: Überprüfe jede Folie und die darauf befindlichen Textboxen sorgfältig auf Rechtschreib- und Grammatikfehler.
#     Einheitlichkeit: Stelle sicher, dass in zusammenhängenden Textpassagen oder Bullet-Points ein konsistenter Formulierungsstil verwendet wird. Identifiziere Stellen, an denen der Stil inkonsistent oder wechselhaft erscheint. Achte zudem auf eine einheitliche und konsistente Nutzung von Grammatikzeichen- und formen. Bspw. sollen auf einer Folie entweder alle Bullet Points, oder keiner, mit einem Punkte beendet werden. Zudem sollen alle zusammenhängenden Bullet Points im gleichen Stil (z.B. Nominalstil) geschrieben werden.
#     Abkürzungen: Achte darauf, ob Abkürzungen verwendet werden, die nicht erklärt werden. Jede Abkürzung sollte bei ihrer ersten Verwendung erklärt werden.
#     Hinweis: Beachte keine Fehler mit einem Bindestrich, da diese Verwendet werden, um ein Wort über mehrere Teil zu erstrecken.Außerdem sollst du nicht auf Ziffern im Text achten, da diese als Fußnoten verwendet werden.
#     Ausgabe: Erstelle eine Tabelle, in der du die Fehler für jede Folie nummeriert aufgeführt werden. Zu jedem Fehler sollte ein Verbesserungsvorschlag angegeben werden."""


def send_gpt(message_gpt):

    message_gpt += """
        ---
        
        Das ist eine wichtige Präsentation, die ich gerade für einen relevanten Kunden mit hohen Anforderungen erstelle.
        In der Präsentation dürfen keine Fehler vorkommen. Überprüfe daher jede Folie sorgfältig auf Rechtschreib- und Grammatikfehler.
        Zudem ist es wichtig, dass die einzelnen Text einheitlich formuliert sind. Auch wenn mehrere Bullet-Points inhaltich klar ist, soll zudem garantiert sein, dass diese stilitisch ganz einheitlich formuliert sind.
        Achte zudem darauf, dass keine Abkürzungen verwendet werden, die nicht durch Ziffern in Form von Fußnoten näher erklärt werden.
        Bindestriche kannst du vernachlässigen, da diese den Zweck haben, ein Wort über mehrere Zeilen zu erstrecken und somit keine ungewollten Fehler sind.
        Erstelle eine Tabelle, in der du die Fehler für jede Folie nummeriert aufgeführt werden. Zu jedem Fehler sollte ein Verbesserungsvorschlag angegeben werden.
        Falls du inkonsistene Formulierung gefunden hast, gibt unbedingt Beispiele dafür und Vorschläge, wie du es verbessern würdest.
        """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=1024,
        messages=[{"role": "user", "content": message_gpt}],
    )

    return response
