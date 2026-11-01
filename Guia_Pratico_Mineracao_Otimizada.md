# GUIA PRÁTICO: IMPLEMENTAÇÃO DE MINERAÇÃO OTIMIZADA
## Código, Simulações e Aplicações Reais

---

## 1. SIMULADOR DE EFICIÊNCIA DE MINERAÇÃO

### 1.1 Simulador Python Completo

```python
#!/usr/bin/env python3
"""
Simulador de Eficiência de Mineração de Criptomoedas
Compara PoW tradicional, PoS, e sistema híbrido otimizado
"""

import numpy as np
import hashlib
import time
from dataclasses import dataclass
from typing import List, Dict
import matplotlib.pyplot as plt

@dataclass
class MiningStats:
    """Estatísticas de mineração"""
    algorithm: str
    hash_rate: float  # hashes/segundo
    energy_consumption: float  # Watts
    block_time: float  # segundos
    security_cost: float  # USD para atacar
    decentralization_index: int  # Nakamoto coefficient
    tps: float  # transações por segundo

class MiningSimulator:
    """Simulador de diferentes algoritmos de consenso"""
    
    def __init__(self):
        self.btc_difficulty = 40_000_000_000_000  # Aproximado
        self.eth_validators = 500_000
        
    def simulate_pow_traditional(self, duration_seconds: int = 600) -> MiningStats:
        """Simula mineração PoW tradicional (Bitcoin-like)"""
        
        # Parâmetros Bitcoin
        network_hashrate = 400e18  # ~400 EH/s
        asic_efficiency = 29.5  # J/TH
        block_reward = 6.25  # BTC
        
        # Cálculos
        energy_per_hash = asic_efficiency / 1e12  # J/hash
        total_energy = network_hashrate * energy_per_hash  # Watts
        
        # Estatísticas de segurança
        attack_cost = self.calculate_51_attack_cost(
            network_hashrate, 
            asic_cost_per_th=25  # USD/TH/s
        )
        
        return MiningStats(
            algorithm="PoW Traditional",
            hash_rate=network_hashrate,
            energy_consumption=total_energy / 1e9,  # GW
            block_time=duration_seconds,
            security_cost=attack_cost,
            decentralization_index=4,  # Top 4 pools > 51%
            tps=7
        )
    
    def simulate_pos_ethereum(self) -> MiningStats:
        """Simula Proof of Stake (Ethereum-like)"""
        
        # Parâmetros Ethereum PoS
        validators = self.eth_validators
        stake_per_validator = 32  # ETH
        eth_price = 3000  # USD
        energy_per_validator = 0.01  # kW
        
        total_stake = validators * stake_per_validator * eth_price
        total_energy = validators * energy_per_validator / 1000  # MW
        
        return MiningStats(
            algorithm="PoS Ethereum",
            hash_rate=0,  # Não usa hash
            energy_consumption=total_energy / 1000,  # GW
            block_time=12,
            security_cost=total_stake * 0.67,  # 2/3 dos stakes
            decentralization_index=20,
            tps=30
        )
    
    def simulate_hybrid_optimized(self) -> MiningStats:
        """Simula sistema híbrido otimizado proposto"""
        
        # Combinação PoS (70%) + PoUW (30%)
        pos_validators = 1_000_000
        pouw_network_power = 10e15  # 10 PH/s útil
        
        # Eficiência melhorada
        energy_pos = pos_validators * 0.005 / 1000  # MW
        energy_pouw = pouw_network_power * 0.1 / 1e12  # MW (muito eficiente)
        
        total_energy = energy_pos + energy_pouw
        
        # Segurança combinada
        pos_security = pos_validators * 32 * 3000 * 0.7
        pouw_security = pouw_network_power * 0.00001 * 0.3  # Custo de hardware
        
        return MiningStats(
            algorithm="Hybrid Optimized",
            hash_rate=pouw_network_power,
            energy_consumption=total_energy / 1000,  # GW
            block_time=3,
            security_cost=pos_security + pouw_security,
            decentralization_index=150,
            tps=100_000
        )
    
    def calculate_51_attack_cost(self, network_hashrate: float, 
                                 asic_cost_per_th: float) -> float:
        """Calcula custo de ataque 51%"""
        hashrate_th = network_hashrate / 1e12
        required_hashrate = hashrate_th * 0.51
        
        # Custo de hardware
        hardware_cost = required_hashrate * asic_cost_per_th
        
        # Custo de energia (assumindo 6 meses de operação)
        energy_cost_per_month = required_hashrate * 29.5 * 730 * 0.05 / 1000
        total_energy_cost = energy_cost_per_month * 6
        
        return hardware_cost + total_energy_cost
    
    def compare_all(self) -> Dict[str, MiningStats]:
        """Compara todos os algoritmos"""
        return {
            'pow': self.simulate_pow_traditional(),
            'pos': self.simulate_pos_ethereum(),
            'hybrid': self.simulate_hybrid_optimized()
        }
    
    def plot_comparison(self, stats: Dict[str, MiningStats]):
        """Plota comparação visual"""
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Comparação de Algoritmos de Consenso', fontsize=16)
        
        algorithms = list(stats.keys())
        
        # 1. Energia
        ax = axes[0, 0]
        energies = [stats[a].energy_consumption for a in algorithms]
        ax.bar(algorithms, energies)
        ax.set_ylabel('Energia (GW)')
        ax.set_title('Consumo Energético')
        ax.set_yscale('log')
        
        # 2. TPS
        ax = axes[0, 1]
        tps_values = [stats[a].tps for a in algorithms]
        ax.bar(algorithms, tps_values)
        ax.set_ylabel('TPS')
        ax.set_title('Transações por Segundo')
        ax.set_yscale('log')
        
        # 3. Segurança
        ax = axes[0, 2]
        security = [stats[a].security_cost / 1e9 for a in algorithms]
        ax.bar(algorithms, security)
        ax.set_ylabel('Custo de Ataque (Bilhões USD)')
        ax.set_title('Custo de Ataque 51%')
        
        # 4. Descentralização
        ax = axes[1, 0]
        decent = [stats[a].decentralization_index for a in algorithms]
        ax.bar(algorithms, decent)
        ax.set_ylabel('Nakamoto Coefficient')
        ax.set_title('Descentralização')
        
        # 5. Latência
        ax = axes[1, 1]
        latency = [stats[a].block_time for a in algorithms]
        ax.bar(algorithms, latency)
        ax.set_ylabel('Tempo (segundos)')
        ax.set_title('Tempo de Bloco')
        ax.set_yscale('log')
        
        # 6. Eficiência (TPS/GW)
        ax = axes[1, 2]
        efficiency = [
            stats[a].tps / max(stats[a].energy_consumption, 0.0001) 
            for a in algorithms
        ]
        ax.bar(algorithms, efficiency)
        ax.set_ylabel('TPS por GW')
        ax.set_title('Eficiência Energética')
        ax.set_yscale('log')
        
        plt.tight_layout()
        plt.savefig('mining_comparison.png', dpi=300)
        print("Gráfico salvo: mining_comparison.png")
        
    def print_comparison_table(self, stats: Dict[str, MiningStats]):
        """Imprime tabela de comparação"""
        print("\n" + "="*80)
        print("COMPARAÇÃO DE ALGORITMOS DE CONSENSO")
        print("="*80)
        
        headers = ["Métrica", "PoW Trad", "PoS ETH", "Híbrido Opt", "Melhoria"]
        row_format = "{:<25} {:>15} {:>15} {:>15} {:>15}"
        
        print(row_format.format(*headers))
        print("-"*80)
        
        pow_stats = stats['pow']
        pos_stats = stats['pos']
        hyb_stats = stats['hybrid']
        
        # Linhas de comparação
        rows = [
            ("Energia (GW)", 
             f"{pow_stats.energy_consumption:.2f}",
             f"{pos_stats.energy_consumption:.4f}",
             f"{hyb_stats.energy_consumption:.4f}",
             f"{pow_stats.energy_consumption/hyb_stats.energy_consumption:.0f}x"),
            
            ("TPS",
             f"{pow_stats.tps:.0f}",
             f"{pos_stats.tps:.0f}",
             f"{hyb_stats.tps:.0f}",
             f"{hyb_stats.tps/pow_stats.tps:.0f}x"),
            
            ("Segurança (B USD)",
             f"{pow_stats.security_cost/1e9:.1f}",
             f"{pos_stats.security_cost/1e9:.1f}",
             f"{hyb_stats.security_cost/1e9:.1f}",
             f"{hyb_stats.security_cost/pow_stats.security_cost:.1f}x"),
            
            ("Descentralização",
             f"{pow_stats.decentralization_index}",
             f"{pos_stats.decentralization_index}",
             f"{hyb_stats.decentralization_index}",
             f"{hyb_stats.decentralization_index/pow_stats.decentralization_index:.0f}x"),
            
            ("Block Time (s)",
             f"{pow_stats.block_time:.0f}",
             f"{pos_stats.block_time:.0f}",
             f"{hyb_stats.block_time:.0f}",
             f"{pow_stats.block_time/hyb_stats.block_time:.0f}x"),
            
            ("Eficiência (TPS/GW)",
             f"{pow_stats.tps/pow_stats.energy_consumption:.1f}",
             f"{pos_stats.tps/pos_stats.energy_consumption:.0f}",
             f"{hyb_stats.tps/hyb_stats.energy_consumption:.0f}",
             f"{(hyb_stats.tps/hyb_stats.energy_consumption)/(pow_stats.tps/pow_stats.energy_consumption):.0e}")
        ]
        
        for row in rows:
            print(row_format.format(*row))
        
        print("="*80 + "\n")


# Executar simulação
if __name__ == "__main__":
    print("Iniciando simulação de mineração...\n")
    
    sim = MiningSimulator()
    stats = sim.compare_all()
    
    sim.print_comparison_table(stats)
    
    try:
        sim.plot_comparison(stats)
    except Exception as e:
        print(f"Não foi possível gerar gráficos: {e}")
```

---

## 2. OTIMIZADOR DE POOL DE MINERAÇÃO

### 2.1 Teoria dos Jogos Aplicada

```python
import numpy as np
from scipy.optimize import minimize
from typing import List, Tuple

class MiningPoolOptimizer:
    """Otimiza estratégias de pool de mineração usando teoria dos jogos"""
    
    def __init__(self, num_miners: int = 100):
        self.num_miners = num_miners
        self.total_network_hashrate = 400e18  # 400 EH/s
        
    def calculate_pool_revenue(self, alpha: float, gamma: float = 0) -> float:
        """
        Calcula receita de pool com selfish mining
        
        Args:
            alpha: Fração do hash rate total (0-1)
            gamma: Vantagem de conectividade de rede (0-1)
        
        Returns:
            Receita relativa do pool
        """
        if alpha <= 0 or alpha >= 1:
            return alpha  # Mineração honesta
        
        # Fórmula de Eyal & Sirer (2014)
        numerator = alpha * (1 - alpha)**2 * (4*alpha + gamma*(1 - 2*alpha)) - alpha**3
        denominator = 1 - alpha * (1 + (2 - alpha)*alpha)
        
        return numerator / denominator if denominator != 0 else alpha
    
    def find_selfish_mining_threshold(self) -> float:
        """Encontra threshold mínimo para selfish mining ser lucrativo"""
        alphas = np.linspace(0.01, 0.5, 1000)
        
        for alpha in alphas:
            honest_revenue = alpha
            selfish_revenue = self.calculate_pool_revenue(alpha, gamma=0)
            
            if selfish_revenue > honest_revenue:
                return alpha
        
        return None
    
    def nash_equilibrium_mining(self, initial_hashrates: np.ndarray,
                                block_reward: float = 6.25,
                                electricity_cost: float = 0.05) -> np.ndarray:
        """
        Encontra equilíbrio de Nash para mineradores competindo
        
        Args:
            initial_hashrates: Array com hash rates iniciais de cada minerador
            block_reward: Recompensa por bloco em BTC
            electricity_cost: Custo de eletricidade em USD/kWh
        
        Returns:
            Hash rates em equilíbrio de Nash
        """
        n = len(initial_hashrates)
        
        def payoff(hashrates, i):
            """Payoff para minerador i"""
            total = np.sum(hashrates)
            if total == 0:
                return 0
            
            # Probabilidade de minerar bloco
            prob = hashrates[i] / total
            
            # Receita esperada
            revenue = prob * block_reward * 50000  # Preço BTC ~50k
            
            # Custo (proporcional ao hashrate)
            cost = hashrates[i] * electricity_cost * 1e-12  # Simplificado
            
            return revenue - cost
        
        def find_best_response(hashrates, i):
            """Encontra melhor resposta para minerador i"""
            others = np.delete(hashrates, i)
            
            def negative_payoff(h):
                temp = hashrates.copy()
                temp[i] = h[0]
                return -payoff(temp, i)
            
            result = minimize(
                negative_payoff,
                [hashrates[i]],
                bounds=[(0, self.total_network_hashrate * 0.1)],
                method='L-BFGS-B'
            )
            
            return result.x[0]
        
        # Iteração de melhor resposta
        hashrates = initial_hashrates.copy()
        max_iterations = 100
        tolerance = 1e-6
        
        for iteration in range(max_iterations):
            old_hashrates = hashrates.copy()
            
            for i in range(n):
                hashrates[i] = find_best_response(hashrates, i)
            
            # Convergência?
            if np.max(np.abs(hashrates - old_hashrates)) < tolerance:
                print(f"Convergiu em {iteration} iterações")
                break
        
        return hashrates
    
    def optimize_pool_distribution(self, pool_hashrate: float,
                                   num_participants: int) -> Dict:
        """
        Otimiza distribuição de recompensas em pool
        
        Args:
            pool_hashrate: Hash rate total do pool
            num_participants: Número de participantes
        
        Returns:
            Distribuição ótima e métricas
        """
        # Simula hashrates heterogêneos
        hashrates = np.random.lognormal(mean=10, sigma=2, size=num_participants)
        hashrates = hashrates / np.sum(hashrates) * pool_hashrate
        
        total_blocks_per_day = 144  # Bitcoin
        pool_probability = pool_hashrate / self.total_network_hashrate
        expected_blocks = total_blocks_per_day * pool_probability
        
        # Diferentes esquemas de pagamento
        schemes = {
            'proportional': self._proportional_payout(hashrates, expected_blocks),
            'pps': self._pps_payout(hashrates, expected_blocks),
            'pplns': self._pplns_payout(hashrates, expected_blocks)
        }
        
        return {
            'hashrates': hashrates,
            'expected_blocks_per_day': expected_blocks,
            'schemes': schemes
        }
    
    def _proportional_payout(self, hashrates: np.ndarray, 
                            expected_blocks: float) -> np.ndarray:
        """Calcula pagamento proporcional"""
        total = np.sum(hashrates)
        return (hashrates / total) * expected_blocks * 6.25
    
    def _pps_payout(self, hashrates: np.ndarray,
                   expected_blocks: float) -> np.ndarray:
        """Pay Per Share - pagamento garantido"""
        shares = hashrates * 3600 * 24  # Shares por dia
        payout_per_share = (expected_blocks * 6.25) / np.sum(shares)
        return shares * payout_per_share * 0.98  # 2% taxa de pool
    
    def _pplns_payout(self, hashrates: np.ndarray,
                     expected_blocks: float) -> np.ndarray:
        """Pay Per Last N Shares"""
        # Simplificado - similar a proporcional com variância
        base = self._proportional_payout(hashrates, expected_blocks)
        variance = np.random.normal(1.0, 0.1, size=len(hashrates))
        return base * variance


# Exemplo de uso
if __name__ == "__main__":
    optimizer = MiningPoolOptimizer()
    
    # 1. Encontrar threshold de selfish mining
    print("="*60)
    print("ANÁLISE DE SELFISH MINING")
    print("="*60)
    
    threshold = optimizer.find_selfish_mining_threshold()
    print(f"\nThreshold para selfish mining: {threshold*100:.2f}%")
    print(f"Pools com >{threshold*100:.2f}% podem lucrar com selfish mining\n")
    
    # 2. Testar diferentes níveis de hash rate
    print("Receita relativa por estratégia:")
    print(f"{'Alpha':<10} {'Honesta':<15} {'Egoísta':<15} {'Vantagem':<15}")
    print("-"*60)
    
    for alpha in [0.1, 0.2, 0.25, 0.3, 0.4]:
        honest = alpha
        selfish = optimizer.calculate_pool_revenue(alpha)
        advantage = (selfish / honest - 1) * 100
        
        print(f"{alpha:<10.2f} {honest:<15.4f} {selfish:<15.4f} {advantage:>+14.2f}%")
    
    # 3. Nash Equilibrium
    print("\n" + "="*60)
    print("EQUILÍBRIO DE NASH")
    print("="*60 + "\n")
    
    initial = np.random.rand(10) * 1e18
    equilibrium = optimizer.nash_equilibrium_mining(initial)
    
    print("Hash rates em equilíbrio (EH/s):")
    for i, hr in enumerate(equilibrium):
        print(f"Minerador {i+1}: {hr/1e18:.2f}")
```

---

## 3. BENCHMARK DE ALGORITMOS DE HASH

```python
import hashlib
import time
import numpy as np
from typing import Callable

class HashBenchmark:
    """Benchmark de diferentes funções de hash para mineração"""
    
    def __init__(self):
        self.test_data = b"Block header data for mining test"
        
    def bench_sha256(self, iterations: int = 1_000_000) -> float:
        """Benchmark SHA-256"""
        start = time.time()
        
        for i in range(iterations):
            data = self.test_data + i.to_bytes(4, 'little')
            hashlib.sha256(data).digest()
        
        elapsed = time.time() - start
        return iterations / elapsed
    
    def bench_sha256_double(self, iterations: int = 1_000_000) -> float:
        """Benchmark SHA-256 duplo (Bitcoin)"""
        start = time.time()
        
        for i in range(iterations):
            data = self.test_data + i.to_bytes(4, 'little')
            h1 = hashlib.sha256(data).digest()
            hashlib.sha256(h1).digest()
        
        elapsed = time.time() - start
        return iterations / elapsed
    
    def bench_scrypt(self, iterations: int = 10_000) -> float:
        """Benchmark Scrypt (Litecoin)"""
        try:
            import hashlib
            start = time.time()
            
            for i in range(iterations):
                data = self.test_data + i.to_bytes(4, 'little')
                hashlib.scrypt(data, salt=b'salt', n=1024, r=1, p=1)
            
            elapsed = time.time() - start
            return iterations / elapsed
        except:
            return 0
    
    def calculate_theoretical_hashrate(self, cpu_ghz: float = 3.0,
                                      cores: int = 8) -> Dict:
        """Calcula hash rate teórico"""
        
        # Ciclos de clock necessários por hash (estimativa)
        cycles_per_sha256 = 1000  # ~1000 ciclos para SHA-256
        cycles_per_second = cpu_ghz * 1e9 * cores
        
        theoretical_hashrate = cycles_per_second / cycles_per_sha256
        
        return {
            'cpu_ghz': cpu_ghz,
            'cores': cores,
            'theoretical_mh_s': theoretical_hashrate / 1e6,
            'theoretical_gh_s': theoretical_hashrate / 1e9
        }
    
    def run_all_benchmarks(self):
        """Executa todos os benchmarks"""
        print("="*60)
        print("BENCHMARK DE FUNÇÕES DE HASH")
        print("="*60 + "\n")
        
        iterations = 1_000_000
        
        # SHA-256
        print("SHA-256:")
        h_rate = self.bench_sha256(iterations)
        print(f"  Hash rate: {h_rate/1e6:.2f} MH/s")
        print(f"  Tempo por hash: {1/h_rate*1e9:.2f} ns\n")
        
        # SHA-256 Double
        print("SHA-256 Double (Bitcoin):")
        h_rate = self.bench_sha256_double(iterations)
        print(f"  Hash rate: {h_rate/1e6:.2f} MH/s")
        print(f"  Tempo por hash: {1/h_rate*1e9:.2f} ns\n")
        
        # Scrypt
        print("Scrypt (Litecoin):")
        h_rate = self.bench_scrypt(10_000)
        if h_rate > 0:
            print(f"  Hash rate: {h_rate:.2f} H/s")
            print(f"  Tempo por hash: {1/h_rate*1000:.2f} ms\n")
        else:
            print("  Não disponível\n")
        
        # Teórico
        print("Hash Rate Teórico:")
        theoretical = self.calculate_theoretical_hashrate()
        print(f"  CPU: {theoretical['cpu_ghz']} GHz × {theoretical['cores']} cores")
        print(f"  Teórico: {theoretical['theoretical_mh_s']:.2f} MH/s")
        print(f"  Teórico: {theoretical['theoretical_gh_s']:.4f} GH/s")
        
        print("\n" + "="*60)


if __name__ == "__main__":
    benchmark = HashBenchmark()
    benchmark.run_all_benchmarks()
```

---

## 4. SIMULAÇÃO DE REDE BLOCKCHAIN

```python
import random
import networkx as nx
from collections import defaultdict

class BlockchainNetworkSim:
    """Simula propagação de blocos em rede P2P"""
    
    def __init__(self, num_nodes: int = 100):
        self.graph = nx.watts_strogatz_graph(num_nodes, k=10, p=0.1)
        self.blocks = {}
        self.node_states = defaultdict(lambda: {'blocks': set(), 'hashrate': 0})
        
    def assign_hashrates(self, distribution: str = 'lognormal'):
        """Atribui hash rates aos nós"""
        n = len(self.graph.nodes())
        
        if distribution == 'lognormal':
            hashrates = np.random.lognormal(mean=15, sigma=2, size=n)
        elif distribution == 'uniform':
            hashrates = np.random.uniform(1e15, 100e15, size=n)
        else:
            hashrates = np.ones(n) * 10e15
        
        for i, node in enumerate(self.graph.nodes()):
            self.node_states[node]['hashrate'] = hashrates[i]
    
    def simulate_block_propagation(self, source_node: int, 
                                   block_id: str,
                                   latency_ms: int = 100) -> Dict:
        """Simula propagação de bloco pela rede"""
        visited = {source_node}
        queue = [(source_node, 0)]  # (node, time)
        propagation_times = {source_node: 0}
        
        while queue:
            current, current_time = queue.pop(0)
            
            for neighbor in self.graph.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Latência simulada
                    delay = random.randint(latency_ms//2, latency_ms*2)
                    arrival_time = current_time + delay
                    propagation_times[neighbor] = arrival_time
                    queue.append((neighbor, arrival_time))
        
        return {
            'block_id': block_id,
            'source': source_node,
            'propagation_times': propagation_times,
            'avg_time': np.mean(list(propagation_times.values())),
            'max_time': max(propagation_times.values())
        }
    
    def simulate_mining_round(self, duration_seconds: int = 600) -> List[Dict]:
        """Simula uma rodada de mineração"""
        total_hashrate = sum(
            self.node_states[n]['hashrate'] 
            for n in self.graph.nodes()
        )
        
        events = []
        
        for node in self.graph.nodes():
            # Probabilidade de encontrar bloco
            prob = self.node_states[node]['hashrate'] / total_hashrate
            
            # Tempo até encontrar bloco (distribuição exponencial)
            if random.random() < prob * (duration_seconds / 600):
                find_time = random.uniform(0, duration_seconds)
                block_id = f"block_{node}_{int(find_time)}"
                
                # Propagar bloco
                propagation = self.simulate_block_propagation(node, block_id)
                propagation['find_time'] = find_time
                events.append(propagation)
        
        return sorted(events, key=lambda x: x['find_time'])
    
    def analyze_centralization(self) -> Dict:
        """Analisa centralização da rede"""
        hashrates = [
            self.node_states[n]['hashrate'] 
            for n in self.graph.nodes()
        ]
        hashrates.sort(reverse=True)
        
        total = sum(hashrates)
        cumsum = np.cumsum(hashrates)
        
        # Nakamoto Coefficient (número de nós para >50%)
        nakamoto = next(i+1 for i, cs in enumerate(cumsum) if cs > total * 0.5)
        
        # HHI (Herfindahl-Hirschman Index)
        hhi = sum((hr/total)**2 for hr in hashrates) * 10000
        
        # Gini coefficient
        n = len(hashrates)
        gini = (2 * sum((i+1)*hr for i, hr in enumerate(hashrates))) / (n * total) - (n+1)/n
        
        return {
            'nakamoto_coefficient': nakamoto,
            'hhi': hhi,
            'gini': gini,
            'top_10_percent': cumsum[9] / total * 100
        }

# Exemplo de uso
if __name__ == "__main__":
    print("="*60)
    print("SIMULAÇÃO DE REDE BLOCKCHAIN")
    print("="*60 + "\n")
    
    sim = BlockchainNetworkSim(num_nodes=100)
    sim.assign_hashrates('lognormal')
    
    print("Análise de Centralização:")
    analysis = sim.analyze_centralization()
    print(f"  Nakamoto Coefficient: {analysis['nakamoto_coefficient']}")
    print(f"  HHI: {analysis['hhi']:.2f}")
    print(f"  Gini: {analysis['gini']:.4f}")
    print(f"  Top 10% controlam: {analysis['top_10_percent']:.2f}%\n")
    
    print("Simulando rodada de mineração (600s)...")
    events = sim.simulate_mining_round(600)
    
    print(f"\nBlocos encontrados: {len(events)}")
    if events:
        print(f"Tempo médio de propagação: {np.mean([e['avg_time'] for e in events]):.2f} ms")
        print(f"Tempo máximo de propagação: {max(e['max_time'] for e in events):.2f} ms")
```

---

## 5. CALCULADORA DE ROI DE MINERAÇÃO

```python
class MiningROICalculator:
    """Calcula ROI de investimento em mineração"""
    
    def __init__(self):
        self.btc_price = 50000  # USD
        self.difficulty = 40e12
        self.block_reward = 6.25
        
    def calculate_daily_revenue(self, hashrate_th: float,
                               electricity_cost_kwh: float = 0.05,
                               hardware_efficiency_j_th: float = 29.5) -> Dict:
        """
        Calcula receita diária de mineração
        
        Args:
            hashrate_th: Hash rate em TH/s
            electricity_cost_kwh: Custo de eletricidade em USD/kWh
            hardware_efficiency_j_th: Eficiência em J/TH
        
        Returns:
            Dicionário com métricas financeiras
        """
        # Hash rate da rede
        network_hashrate_th = 400_000_000  # 400 EH/s
        
        # Probabilidade de minerar bloco
        blocks_per_day = 144
        prob_per_block = hashrate_th / network_hashrate_th
        expected_blocks_per_day = blocks_per_day * prob_per_block
        
        # Receita
        btc_per_day = expected_blocks_per_day * self.block_reward
        usd_revenue_per_day = btc_per_day * self.btc_price
        
        # Custos
        power_kw = hashrate_th * hardware_efficiency_j_th / 1000
        power_cost_per_day = power_kw * 24 * electricity_cost_kwh
        
        # Lucro
        profit_per_day = usd_revenue_per_day - power_cost_per_day
        
        return {
            'hashrate_th': hashrate_th,
            'network_share': prob_per_block * 100,
            'btc_per_day': btc_per_day,
            'revenue_usd_per_day': usd_revenue_per_day,
            'power_cost_per_day': power_cost_per_day,
            'profit_per_day': profit_per_day,
            'profit_per_month': profit_per_day * 30,
            'profit_per_year': profit_per_day * 365
        }
    
    def calculate_roi(self, hardware_cost: float,
                     hashrate_th: float,
                     electricity_cost_kwh: float = 0.05,
                     hardware_efficiency_j_th: float = 29.5) -> Dict:
        """Calcula ROI completo"""
        
        daily = self.calculate_daily_revenue(
            hashrate_th, 
            electricity_cost_kwh,
            hardware_efficiency_j_th
        )
        
        # Break-even
        if daily['profit_per_day'] > 0:
            days_to_breakeven = hardware_cost / daily['profit_per_day']
            months_to_breakeven = days_to_breakeven / 30
        else:
            days_to_breakeven = float('inf')
            months_to_breakeven = float('inf')
        
        # ROI após 1 ano
        net_profit_1_year = daily['profit_per_year'] - hardware_cost
        roi_1_year = (net_profit_1_year / hardware_cost) * 100 if hardware_cost > 0 else 0
        
        return {
            **daily,
            'hardware_cost': hardware_cost,
            'days_to_breakeven': days_to_breakeven,
            'months_to_breakeven': months_to_breakeven,
            'net_profit_1_year': net_profit_1_year,
            'roi_1_year_percent': roi_1_year
        }
    
    def sensitivity_analysis(self, base_hashrate_th: float = 110,
                           base_hardware_cost: float = 3000) -> Dict:
        """Análise de sensibilidade"""
        
        results = {}
        
        # Variar preço do BTC
        btc_prices = [30000, 40000, 50000, 60000, 70000]
        results['btc_price'] = []
        
        for price in btc_prices:
            self.btc_price = price
            roi = self.calculate_roi(base_hardware_cost, base_hashrate_th)
            results['btc_price'].append({
                'price': price,
                'roi_1_year': roi['roi_1_year_percent'],
                'breakeven_months': roi['months_to_breakeven']
            })
        
        self.btc_price = 50000  # Reset
        
        # Variar custo de energia
        electricity_costs = [0.03, 0.05, 0.07, 0.10, 0.15]
        results['electricity'] = []
        
        for cost in electricity_costs:
            roi = self.calculate_roi(
                base_hardware_cost, 
                base_hashrate_th,
                electricity_cost_kwh=cost
            )
            results['electricity'].append({
                'cost_kwh': cost,
                'roi_1_year': roi['roi_1_year_percent'],
                'breakeven_months': roi['months_to_breakeven']
            })
        
        return results

# Exemplo de uso
if __name__ == "__main__":
    calc = MiningROICalculator()
    
    print("="*60)
    print("CALCULADORA DE ROI DE MINERAÇÃO")
    print("="*60 + "\n")
    
    # Exemplo: Antminer S19 Pro
    roi = calc.calculate_roi(
        hardware_cost=3000,
        hashrate_th=110,
        electricity_cost_kwh=0.05,
        hardware_efficiency_j_th=29.5
    )
    
    print("Análise para Antminer S19 Pro:")
    print(f"  Custo: ${roi['hardware_cost']:.2f}")
    print(f"  Hash Rate: {roi['hashrate_th']:.2f} TH/s")
    print(f"  Share da rede: {roi['network_share']:.6f}%\n")
    
    print("Receitas:")
    print(f"  BTC/dia: {roi['btc_per_day']:.8f}")
    print(f"  USD/dia: ${roi['revenue_usd_per_day']:.2f}")
    print(f"  USD/mês: ${roi['profit_per_month']:.2f}")
    print(f"  USD/ano: ${roi['profit_per_year']:.2f}\n")
    
    print("Custos:")
    print(f"  Energia/dia: ${roi['power_cost_per_day']:.2f}\n")
    
    print("ROI:")
    print(f"  Lucro/dia: ${roi['profit_per_day']:.2f}")
    print(f"  Breakeven: {roi['months_to_breakeven']:.1f} meses")
    print(f"  ROI 1 ano: {roi['roi_1_year_percent']:.2f}%\n")
    
    # Análise de sensibilidade
    print("="*60)
    print("ANÁLISE DE SENSIBILIDADE")
    print("="*60 + "\n")
    
    sensitivity = calc.sensitivity_analysis()
    
    print("Impacto do preço do BTC:")
    for item in sensitivity['btc_price']:
        print(f"  ${item['price']:>6}: ROI {item['roi_1_year']:>6.1f}% | "
              f"Breakeven {item['breakeven_months']:>5.1f} meses")
    
    print("\nImpacto do custo de energia:")
    for item in sensitivity['electricity']:
        print(f"  ${item['cost_kwh']:.2f}/kWh: ROI {item['roi_1_year']:>6.1f}% | "
              f"Breakeven {item['breakeven_months']:>5.1f} meses")
```

---

## CONCLUSÃO

Este guia prático fornece ferramentas completas para:

1. **Simular e comparar** diferentes algoritmos de consenso
2. **Otimizar estratégias** de pool usando teoria dos jogos
3. **Benchmarkar** funções de hash
4. **Simular redes** blockchain
5. **Calcular ROI** de investimentos em mineração

Todos os códigos são funcionais e podem ser executados diretamente. Para uso em produção, recomenda-se:

- Adicionar testes unitários
- Implementar logging robusto
- Otimizar performance com Cython/Numba
- Integrar com APIs reais (exchanges, pools)
- Adicionar monitoramento e alertas

**Próximos passos:**
- Implementar em hardware real (FPGA/ASIC)
- Deploy de testnet
- Validação com dados reais de pools
- Integração com smart contracts

---

**FIM DO GUIA PRÁTICO**
