import wolframalpha as wa
import wikipedia as wiki
while True:
       inp = input("QUESTION: ")

       try:
           #wolframalpha
           app_id = "YRRQ8V-P93VL22LR2"
           client = wa.Client(app_id)
           res = client.query(inp)
           answer = next(res.results).text
           print(answer)

       except:
               print(wiki.summary(inp))