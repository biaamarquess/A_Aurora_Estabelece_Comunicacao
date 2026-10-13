"""
Projeto: Sistema de Comunicação Interplanetária da Colônia (SCIC)
Instituição / Contexto: Atividade Integradora - Aurora Siger (2026)
Descrição: Código principal contendo a manipulação com Pandas/NumPy,
cálculo de erros numéricos e eletricidade, modelo preditivo com scikit-learn,
Heap para alertas críticos e Trie para buscas indexadas por prefixo.
"""

import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =====================================================================
# 1. ESTRUTURA DE DADOS: HEAP (FILA DE PRIORIDADE PARA ALERTAS)
# =====================================================================

class AlertaHeap:
    """Implementação de Min-Heap para priorização de alertas críticos da colônia."""
    def __init__(self):
        self.heap = []

    def _pai(self, i):
        return (i - 1) // 2

    def _esq(self, i):
        return 2 * i + 1

    def _dir(self, i):
        return 2 * i + 2

    def inserir(self, prioridade, modulo, mensagem):
        no = (prioridade, modulo, mensagem)
        self.heap.append(no)
        self._subir(len(self.heap) - 1)

    def _subir(self, i):
        pai = self._pai(i)
        while i > 0 and self.heap[i][0] < self.heap[pai][0]:
            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            i = pai
            pai = self._pai(i)

    def extrair_mais_urgente(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return raiz

    def _descer(self, i):
        menor = i
        esq = self._esq(i)
        dir_idx = self._dir(i)

        if esq < len(self.heap) and self.heap[esq][0] < self.heap[menor][0]:
            menor = esq
        if dir_idx < len(self.heap) and self.heap[dir_idx][0] < self.heap[menor][0]:
            menor = dir_idx

        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._descer(menor)

    def esta_vazio(self):
        return len(self.heap) == 0


# =====================================================================
# 2. ESTRUTURA DE DADOS: TRIE (BUSCA INDEXADA POR PREFIXO)
# =====================================================================

class NoTrie:
    """Nó unitário para a árvore Trie."""
    def __init__(self):
        self.filhos = {}
        self.fim_de_palavra = False
        self.dados_associados = set()


class TrieBuscaColonia:
    """Árvore Trie para recuperação rápida de registros por prefixo textual ou código."""
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra, referencia):
        atual = self.raiz
        palavra_lower = str(palavra).lower()
        for char in palavra_lower:
            if char not in atual.filhos:
                atual.filhos[char] = NoTrie()
            atual = atual.filhos[char]
        atual.fim_de_palavra = True
        atual.dados_associados.add(referencia)

    def _coletar_todos(self, no, resultados):
        if no.fim_de_palavra:
            resultados.update(no.dados_associados)
        for proximo in no.filhos.values():
            self._coletar_todos(proximo, resultados)

    def buscar_por_prefixo(self, prefixo):
        atual = self.raiz
        prefixo_lower = str(prefixo).lower()
        for char in prefixo_lower:
            if char not in atual.filhos:
                return []
            atual = atual.filhos[char]
        resultados = set()
        self._coletar_todos(atual, resultados)
        return list(resultados)


# =====================================================================
# 3. FUNÇÕES DE PROCESSAMENTO E SIMULAÇÃO DO SISTEMA
# =====================================================================

def carregar_dados():
    caminho = 'dados_aurora_siger.csv'
    if not os.path.exists(caminho):
        print("[ERRO] Arquivo de dados não encontrado. Certifique-se de manter o CSV na pasta.")
        return None
    return pd.read_csv(caminho)


def calcular_indicadores_e_erros(df):
    """Calcula erros numéricos e potência elétrica básica (Lei de Ohm / Potência)."""
    df['erro_absoluto_ms'] = np.abs(df['latencia_observada_ms'] - df['latencia_prevista_ms'])
    df['erro_relativo_%'] = (df['erro_absoluto_ms'] / df['latencia_observada_ms']) * 100
    df['potencia_watts'] = df['tensao_v'] * df['corrente_a']
    return df


def executar_modelo_previsao(df):
    """Executa modelo de regressão simples utilizando scikit-learn e calcula métricas."""
    X = df[['potencia_watts']]
    y = df['latencia_observada_ms']
    
    modelo = LinearRegression()
    modelo.fit(X, y)
    y_pred = modelo.predict(X)
    
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_pred)
    
    return modelo, y_pred, {'MAE': mae, 'MSE': mse, 'RMSE': rmse, 'R2': r2}


# =====================================================================
# 4. MENU DE EXECUÇÃO PRINCIPAL NO TERMINAL
# =====================================================================

def main():
    df = carregar_dados()
    if df is None:
        return

    df = calcular_indicadores_e_erros(df)

    # Inicialização da Fila de Prioridade (Heap) para Alertas
    heap_alertas = AlertaHeap()
    for _, row in df.iterrows():
        if row['status_operacional'] == 'alerta':
            heap_alertas.inserir(int(row['nivel_prioridade']), str(row['nome_modulo']), str(row['mensagem_alerta']))

    # Inicialização da Árvore Trie para Buscas por Prefixo
    trie = TrieBuscaColonia()
    for _, row in df.iterrows():
        trie.inserir(row['nome_modulo'], f"Módulo: {row['nome_modulo']} (Tipo: {row['tipo_modulo']})")
        trie.inserir(row['codigo_dispositivo'], f"Sensor ID: {row['codigo_dispositivo']} - {row['nome_modulo']}")

    while True:
        print("\n=======================================================")
        print("  SCIC - SISTEMA DE COMUNICAÇÃO INTERPLANETÁRIA (AURORA)")
        print("=======================================================")
        print("1. Carregar e consultar dados operacionais e indicadores")
        print("2. Exibir análise de erros numéricos e eletricidade básica")
        print("3. Executar modelo de previsão e avaliar métricas (MAE, MSE, RMSE, R²)")
        print("4. Priorizar alertas críticos (Heap / Fila de Prioridade)")
        print("5. Realizar busca indexada por prefixo (Trie)")
        print("6. Sair do sistema")

        opcao = input("\nSelecione a opção desejada (1-6): ").strip()

        if opcao == '1':
            print("\n--- REGISTROS OPERACIONAIS DA COLÔNIA ---")
            print(df[['nome_modulo', 'tipo_modulo', 'latencia_observada_ms', 'status_operacional', 'ciclo_registro']].to_string(index=False))

        elif opcao == '2':
            print("\n--- ERROS NUMÉRICOS E POTÊNCIA ELÉTRICA ---")
            print(df[['nome_modulo', 'latencia_observada_ms', 'latencia_prevista_ms', 'erro_absoluto_ms', 'erro_relativo_%', 'potencia_watts']].to_string(index=False))
            print("\n[Nota]: Discrepâncias decimais derivam de arredondamentos em ponto flutuante.")

        elif opcao == '3':
            _, _, metricas = executar_modelo_previsao(df)
            print("\n--- PERFORMANCE DO MODELO PREDITIVO ---")
            for k, v in metricas.items():
                print(f" > {k}: {v:.4f}")
            print("\n[Interpretação]: A comparação entre MAE e RMSE indica estabilidade dos resíduos.")

        elif opcao == '4':
            print("\n--- GERENCIAMENTO DE ALERTAS CRÍTICOS (HEAP) ---")
            if heap_alertas.esta_vazio():
                print("Nenhum alerta crítico ativo na fila.")
            else:
                urgente = heap_alertas.extrair_mais_urgente()
                print(f" [ALERTA MAIS URGENTE]")
                print(f" - Módulo: {urgente[1]}")
                print(f" - Prioridade: {urgente[0]}")
                print(f" - Mensagem: {urgente[2]}")

        elif opcao == '5':
            prefixo = input("\Digite o prefixo para busca (ex: 'agri', '0x2', 'hab'): ").strip()
            resultados = t = trie.buscar_por_prefixo(prefixo)
            print(f"\n--- RESULTADOS DA BUSCA POR PREFIXO '{prefixo}' ---")
            if resultados:
                for r in resultados:
                    print(f"  -> {r}")
            else:
                print("Nenhum registro encontrado para este prefixo.")

        elif opcao == '6':
            print("\nEncerrando o SCIC. Conexão com a Aurora Siger finalizada com segurança.")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 1 e 6.")

if __name__ == "__main__":
    main()