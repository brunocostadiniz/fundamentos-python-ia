# ==============================================================================
# Simulador de Prontidão para o Mercado de IA
# ==============================================================================

print("=== BEM-VINDO AO DIAGNÓSTICO DE CARREIRA EM IA ===")
print("Vamos calcular seu plano até o primeiro estágio!\n")

# 1. Entrada de dados do usuário (com conversão para números)
nome = input("Qual é o seu nome? ")
semestre = int(input("Qual semestre você está cursando (número)? "))
meses_ate_estagio = int(input("Em quantos meses você quer estar estagiando? "))
horas_por_dia = float(input("Quantas horas por dia você pode dedicar aos estudos? "))

# 2. Fazendo os cálculos (Matemática aplicada)
# Consideramos 30 dias por mês
total_dias = meses_ate_estagio * 30
total_horas_acumuladas = total_dias * horas_por_dia

# 3. Exibindo o Relatório de Diagnóstico
print("\n" + "=" * 50)
print(f"📊 RELATÓRIO INDIVIDUAL: {nome.upper()}")
print(f"Semestre Atual: {semestre}º")
print(f"Prazo planejado: {meses_ate_estagio} meses ({total_dias} dias)")
print(f"Horas totais de estudo prático: {total_horas_acumuladas:.0f} horas")
print("=" * 50)

# 4. Avaliação de Mercado (Lógica Condicional com if / elif / else)
if total_horas_acumuladas >= 250:
    print("🚀 Nível de Preparação: EXCELENTE!")
    print("Com essa carga horária, você consegue dominar Python, APIs e ter 3 projetos completos no GitHub.")
elif total_horas_acumuladas >= 150:
    print("⚡ Nível de Preparação: BOM!")
    print("Ritmo suficiente para disputar vagas de estágio, focando nos projetos essenciais.")
else:
    print("⚠️ Nível de Preparação: ATENÇÃO!")
    print("Carga horária apertada. Recomendamos estender o prazo ou focar 100% no portfólio prático.")

print("=" * 50)