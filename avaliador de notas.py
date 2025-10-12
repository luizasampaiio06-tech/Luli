import streamlit as st

st.write("Alô mundo")
st.header("Bem-vindo ao site mais novo da Luli! ")
st.write("Só preencha abaixo com alguns dados para conhecê-lo melhor. 😁")

nome = st.text_input("Qual é o seu nome?")
if nome:
    st.write(f"Olá, {nome}! Fico muito animado  por você estar aqui! 😊")
def avaliar_nota(nota):
    if nota < 6:
        return "Ruim"
    elif nota < 8:
        return "Boa"
    else:
        return "Excelente"

def main():
    print("=== Avaliador de Notas ===")
    notas = []

    while True:
        entrada = input("Digite uma nota (ou 'sair' para finalizar): ")
        if entrada.lower() == 'sair':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    print("\n=== Resultado da Avaliação ===")
    for i, nota in enumerate(notas):
        print(f"Nota {i+1}: {nota} → {avaliar_nota(nota)}")


