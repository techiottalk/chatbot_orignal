import wolframalpha as wa

inp = input("QUESTION: ")
app_id = "YRRQ8V-P93VL22LR2"
client = wa.Client(app_id)
res=client.query(inp)
answer=next(res.results).text
print(answer)




