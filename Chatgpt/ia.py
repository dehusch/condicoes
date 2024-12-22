from transformers import pipeline

# Carrega um modelo de linguagem local
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# Interação no terminal
while True:
    pergunta = input("Digite sua pergunta (ou 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        break
    resposta = chatbot(pergunta, max_length=100, do_sample=True)
    print("Resposta:", resposta[0]["generated_text"])
