# ==============================================================================
# Aula 03: Estruturas de Dados para IA (Listas, Dicionários e Loops)
# ==============================================================================

# 1. Uma LISTA simples de tecnologias para o seu currículo
stack_ia = ["Python", "Git & GitHub", "VS Code"]

# Adicionando uma nova tecnologia à lista (método .append)
stack_ia.append("FastAPI")
stack_ia.append("Modelos de Linguagem (LLMs)")

print("=== MINHA STACK DE TECNOLOGIAS EM IA ===")
# O loop 'for' percorre cada item da lista automaticamente
for indice, tec in enumerate(stack_ia, start=1):
    print(f"{indice}. {tec}")

print("-" * 50)

# 2. Simulador de Histórico de Conversa com uma IA (Lista de Dicionários)
print("=== SIMULADOR DE CHAT / MEMÓRIA DE IA ===\n")

historico_chat = [
    {"autor": "Sistema", "mensagem": "Agente de Carreira em IA inicializado."},
    {"autor": "Bruno", "mensagem": "Quero entrar no mercado de trabalho em IA."},
    {"autor": "Tutor IA", "mensagem": "Excelente! Vamos focar em projetos práticos no GitHub."}
]

# Permitindo que você envie uma nova mensagem pelo teclado!
sua_mensagem = input("Digite sua próxima pergunta para o Tutor: ")

# Adicionamos a sua nova mensagem ao histórico
historico_chat.append({"autor": "Bruno", "mensagem": sua_mensagem})

print("\n--- HISTÓRICO COMPLETO DA CONVERSA ---")
for item in historico_chat:
    print(f"[{item['autor']}]: {item['mensagem']}")

print("-" * 50)
print(f"Total de mensagens armazenadas na memória: {len(historico_chat)}")
