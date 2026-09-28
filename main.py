import sys 
from central_recursiva.excecoes import OperacaoInvalidaError, EntradaInvalidaError
from central_recursiva.processador import porcessar_operacao

def main():
    try:
      linha_q = sys.stdin.readline()
      if not linha_q
          return
      q = int(linha_q.strip())
    except ValueError:
      return

    for _ in range(q):
      linha = sys.stdin.readline()
      if not linha:
          break

      # Tratamento de exceções com try, except e finally
      try:
          resultado = processar_operacao(linha)
        print(resultado)
except OperacaoInvalidaError:
    print("ERRO: OperacaoInvalida")
except EntradaInvalidaError:
    print("ERRO: EntradaInvalida")
finally:
    # Executando ao final de cada iteração
    pass
if __nam__ == "__main__":
    main()
