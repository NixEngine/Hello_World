## Page 1

# RELATÓRIO TÉCNICO COMPLETO: ANDROID 16 (AOSP)

---

## Sumário Executivo

Total de Algoritmos/Estruturas/Protocolos Coletados: 679

Componentes do Android Pesquisados: 26

Pesquisadores Analisados: 20

---

## PARTE 1: COMPONENTES DO ANDROID 16 - CONTEÚDO TÉCNICO

---

### Componente 1: Kernel Linux Android 16 - Agendamento, Memória e IPC

Itens Técnicos Encontrados: 12

Conceitos-Chave: EEVDF, Tempo Virtual, Árvore de Busca Binária Aumentada, LMKD, Pontuação de Processo, cgroups, Binder IPC, Protocolo de Transação, binder_node, Ashmem, memfd

---

## Conteúdo Técnico do Kernel Linux no Android 16

Este documento apresenta o conteúdo técnico focado nos algoritmos, estruturas de dados, protocolos e arquitetura dos componentes do Kernel Linux utilizados no Android 16: Agendamento (EEVDF), Gerenciamento de Memória (LMKD), Driver Binder e Ashmem.

### 1. Agendamento de Tarefas (Scheduler)

No Android 16, o Completely Fair Scheduler (CFS) está sendo substituído pelo Earliest Eligible Virtual Deadline First (EEVDF) [1].

#### 1.1. Algoritmo EEVDF

O EEVDF é um algoritmo de agendamento que visa a distribuição equitativa do tempo de CPU entre todas as tarefas executáveis com a mesma prioridade [2].

O conceito central do EEVDF é o **Tempo Virtual** (virtual time) [3]. Cada tarefa mantém um relógio virtual que avança a uma taxa baseada em seu peso (prioridade). O agendador seleciona a tarefa com o menor tempo virtual elegível para execução.

O algoritmo EEVDF pode ser resumido pela regra de seleção:

Selecionar a tarefa $T$ com o menor $v_{runtime}$ elegível, onde $v_{runtime}$ é o tempo virtual de execução da tarefa.

#### 1.2. Estrutura de Dados

A estrutura de dados principal utilizada pelo EEVDF para gerenciar as tarefas é uma **Árvore de Busca Binária Aumentada** (Augmented Binary Search Tree) [4].

---


## Page 2

Esta estrutura permite as seguintes operações eficientes:

*   **Inserção** (insert_req): Adicionar uma nova tarefa executável.
*   **Exclusão** (delete_req): Remover uma tarefa (por exemplo, quando ela termina ou entra em estado de espera).
*   **Seleção** (pick_next_task): Selecionar a tarefa com o menor $v_{runtime}$ (o nó mais à esquerda da árvore).

# 2. Gerenciamento de Memória (LMKD)

O Low Memory Killer Daemon (LMKD) é um processo de espaço de usuário que monitora o estado da memória e reage à alta pressão de memória, eliminando processos para liberar recursos [5].

## 2.1. Mecanismo de Seleção de Vítimas

O LMKD emprega um mecanismo de seleção de vítimas mais sofisticado e proativo do que o tradicional OOM Killer do Linux. O algoritmo de seleção de vítimas é baseado em três pilares:

1.  **Pontuação de Processo** (oom_score_adj): Cada processo Android recebe uma pontuação ajustável (oom_score_adj) que reflete sua importância. Processos com pontuações mais altas (menos importantes, como aplicativos em cache) são os primeiros candidatos à eliminação.
2.  **Grupos de Controle** (cgroups): O LMKD utiliza cgroups para monitorar e gerenciar grupos de tarefas. Isso permite que o daemon receba sinais de pressão de memória por grupo e aplique políticas de eliminação de forma granular [6].
3.  **Sinais de Pressão de Memória**: O LMKD reage a sinais de pressão de memória do kernel, agindo antes que o sistema atinja um estado crítico e instável [7].

## 2.2. Arquitetura

O LMKD opera como um daemon de espaço de usuário que se comunica com o kernel para obter informações sobre a pressão de memória e executar a eliminação de processos.

# 3. Driver Binder (IPC)

O Binder é o principal mecanismo de Inter-Process Communication (IPC) no Android, implementado através de um Driver Binder no kernel [8].

## 3.1. Protocolo de Transação

O protocolo Binder é baseado em transações e segue um modelo Cliente-Servidor.

*   **Cliente:** Faz uma chamada de função remota (Remote Procedure Call - RPC).
*   **Driver Binder (Kernel):** Roteia a transação do cliente para o processo servidor correspondente.
*   **Servidor:** Executa a função e retorna o resultado.

O protocolo garante a passagem de descritores de arquivo e objetos Binder entre processos, mantendo a segurança e a identidade do chamador [9].

## 3.2. Estruturas de Dados do Kernel

O Driver Binder no kernel utiliza estruturas de dados específicas para rastrear as conexões e transações:

---


## Page 3

<table>
  <thead>
    <tr>
      <th>Estrutura de Dados</th>
      <th>Função</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>binder_node</b></td>
      <td>Representa um objeto Binder real no processo servidor. Cada serviço exportado tem um binder_node associado.</td>
    </tr>
    <tr>
      <td><b>binder_ref</b></td>
      <td>Representa uma referência a um binder_node no processo cliente. É a representação local do objeto remoto.</td>
    </tr>
    <tr>
      <td><b>binder_proc</b></td>
      <td>Representa um processo que está usando o Binder. Contém informações sobre os binder_node e binder_ref pertencentes a esse processo.</td>
    </tr>
    <tr>
      <td><b>binder_transaction</b></td>
      <td>Estrutura temporária que encapsula os dados e metadados de uma chamada IPC em trânsito.</td>
    </tr>
  </tbody>
</table>

# 4. Ashmem (Memória Compartilhada Android)

O Ashmem (Android Shared Memory) é um mecanismo de memória compartilhada anônima que permite que processos compartilhem grandes regiões de memória de forma eficiente [10].

## 4.1. Mecanismo e Arquitetura

O Ashmem é implementado como um driver de kernel que cria regiões de memória compartilhada que podem ser referenciadas por **descritores de arquivo** ( fds ) [11].

Uma característica crucial do Ashmem é sua capacidade de **descartar páginas de memória** sob pressão de memória. Se o sistema estiver com pouca memória, o kernel pode liberar as páginas de uma região Ashmem, desde que a região não esteja “bloqueada” pelo processo. O processo que acessa a região descartada receberá uma falha de página, e o kernel tentará realocar a memória [12].

## 4.2. Transição para memfd

O Android está em um processo de transição para substituir o Ashmem pelo mecanismo memfd do kernel Linux, que oferece funcionalidade semelhante e está na **mainline** do kernel [13].

A interface de nível de API, ASharedMemory , foi atualizada para suportar o uso de memfd , facilitando a migração para o AOSP [14].

---

## Referências

[1] Kernel release notes | Android Open Source Project ([https://source.android.com/docs/core/architecture/kernel/release-notes](https://source.android.com/docs/core/architecture/kernel/release-notes))
[2] EEVDF Scheduler ([https://docs.kernel.org/scheduler/sched-eevdf.html](https://docs.kernel.org/scheduler/sched-eevdf.html)) [3] Discussion 5: Starvation, EEVDF ([https://cs162.org/static/dis/5.pdf](https://cs162.org/static/dis/5.pdf)) [4] Linux 核 心 設 計 : Scheduler(5): EEVDF Scheduler/1 ([https://hackmd.io/@sysprog/Hka7Kzeap/%2FSyG4t5u1a](https://hackmd.io/@sysprog/Hka7Kzeap/%2FSyG4t5u1a)) [5] Low memory killer daemon | Android Open Source Project ([https://source.android.com/docs/core/perf/lmkd](https://source.android.com/docs/core/perf/lmkd)) [6] How Android’s Low Memory Killer keeps devices responsive ([https://www.linkedin.com/posts/vikseln_android-aosp-lowmemorykiller-activity-7370913027136716801-6o1Z](https://www.linkedin.com/posts/vikseln_android-aosp-lowmemorykiller-activity-7370913027136716801-6o1Z)) [7] what’s the differences between Android LMK and Linux OOM ([https://stackoverflow.com/questions/46468604/whats-the-differences-between-android-lmk-and-linux-oom](https://stackoverflow.com/questions/46468604/whats-the-differences-between-android-lmk-and-linux-oom)) [8] Binder overview | Android Open Source Project ([https://source.android.com/docs/core/architecture/ipc/binder-overview](https://source.android.com/docs/core/architecture/ipc/binder-overview)) [9] Binder Internals - Android Offensive Security Blog ([https://androidoffsec.withgoogle.com/posts/binder-internals/](https://androidoffsec.withgoogle.com/posts/binder-internals/)) [10] Advanced Algorithmic Architectures in Android and Kotlin ([https://medium.com/@riyaspullurofficial/advanced-algorithmic-architectures-in-android-and-kotlin-c49a7666aecf](https://medium.com/@riyaspullurofficial/advanced-algorithmic-architectures-in-android-and-kotlin-c49a7666aecf)) [11] Shared Memory : the fastest way to share data between ... ([https://www.linkedin.com/pulse/shared-memory-fastest-way-share-data-between-android-stefano-santilli](https://www.linkedin.com/pulse/shared-memory-fastest-way-share-data-between-android-stefano-santilli)) [12] Android ashmem - Rust for Linux ([https://rust-for-linux.com/android-%60ashmem%60](https://rust-for-linux.com/android-%60ashmem%60)) [13] Transitioning Android from ashmem to memfd ([https://lpc.events/event/19/contributions/2117/attachments/1727/3782/LPC%202025_%20Transitioning%20Android%20from%20ashmem%20to%20memfd](https://lpc.events/event/19/contributions/2117/attachments/1727/3782/LPC%202025_%20Transitioning%20Android%20from%20ashmem%20to%20memfd)) [14] Harness: Transparent and Lightweight Protection of Vehicle Control on Untrusted Android Automotive Operating System ([https://www.usenix.org/conference/usenixsecurity25/presentation/gong-haochen](https://www.usenix.org/conference/usenixsecurity25/presentation/gong-haochen))

---


## Page 4

# Componente 2: HAL Hardware Abstraction Layer - HIDL, AIDL, passthrough mode, binderized mode

**Itens Técnicos Encontrados:** 14

**Conceitos-Chave:** Binder IPC, AIDL, HIDL, Binderized HAL, Passthrough Mode, Stable AIDL, Parcelable, ParcelableHolder, SEPolicy, VTS, VINTF Manifest, setInheritRt, fd, handle, @VintfStability, hidl2aidl

# Arquitetura de Abstração de Hardware (HAL) no Android 16 (AOSP)

O componente central desta análise é a **Arquitetura de Abstração de Hardware (HAL)** do Android, com foco na transição de **HIDL para AIDL** e o protocolo de comunicação **Binder IPC**.

## Protocolos de Comunicação e Arquitetura

### 1. Binder Inter-Process Communication (IPC)

O **Binder** é o protocolo de comunicação fundamental no Android, servindo como o mecanismo de passagem de mensagens que permite a comunicação entre processos (IPC). Ele é a base para a arquitetura **Binderized HAL**, onde os serviços HAL rodam em um processo separado do Framework do Android.

*   **Mecanismo:** Passagem de mensagens entre processos.
*   **Algoritmo de Threading:** O AIDL não inicia automaticamente *thread pools* para objetos Binder. O gerenciamento de threads deve ser iniciado manualmente.
*   **Prioridade em Tempo Real:** A função `setInheritRt` deve ser invocada no objeto *binder* para habilitar a herança de prioridade em tempo real, um mecanismo crucial para garantir o desempenho de hardware sensível ao tempo.

### 2. AIDL (Android Interface Definition Language)

O **AIDL** é a linguagem de definição de interface (IDL) preferencial e estável para HALs a partir do Android 11, mantendo-se como o padrão no Android 16.

*   **Protocolo:** Exclusivamente **Binder IPC** (Binderized HAL).
*   **Estabilidade:** O **Stable AIDL** é obrigatório para comunicação entre as partições *system.img* (Framework) e *vendor.img* (Hardware). A estabilidade é garantida pela anotação `@VintfStability` e pela declaração `stability: "vintf"` no `aidl_interface`.
*   **Versionamento:** Adota o versionamento *in-place*, permitindo a adição de métodos ao final das interfaces ou campos a parcelables sem quebrar a compatibilidade. Não utiliza o conceito de *major versions* para incompatibilidade.
*   **Tipos Primitivos:** Utiliza o tipo `fd` (File Descriptor) para representar descritores de arquivo, em contraste com o `handle` do HIDL.
*   **Tratamento de Erros:** Utiliza o tipo Status embutido e exceções para tratamento de erros, um avanço em relação aos erros não verificados do HIDL.

### 3. HIDL (Hardware Interface Definition Language)

O **HIDL** é a IDL legada, introduzida no Projeto Treble (Android 8) e agora descontinuada em favor do AIDL.

*   **Modos de Operação:**
    *   **Binderized Mode:** Comunicação via Binder IPC.

---


## Page 5

*   **Passthrough Mode:** Chamadas diretas *in-process*, permitindo que HALs legados (anteriores ao Android 8) fossem usados. Este modo não é suportado por HALs baseados em AIDL.
*   **Ferramenta de Transição:** A ferramenta `hidl2aidl` é utilizada para converter interfaces HIDL (.hal) para AIDL (.aidl), facilitando a migração.

# Estruturas de Dados e APIs

## 1. Estruturas de Dados

*   **Parcelable:** Estrutura de dados para serialização e desserialização de objetos, essencial para a transmissão de dados via Binder IPC.
*   **ParcelableHolder:** Uma estrutura de dados que encapsula um Parcelable, permitindo que fornecedores estendam Parcelables definidos pelo AOSP com dados específicos do fabricante sem modificar a interface original.

## 2. APIs de Extensão do Binder

O mecanismo de extensão permite modificar a funcionalidade de um HAL existente ou adicionar novas capacidades.

<table>
<thead>
<tr>
<th>Linguagem</th>
<th>API para Definir Extensão</th>
<th>API para Obter Extensão</th>
</tr>
</thead>
<tbody>
<tr>
<td>NDK</td>
<td>AIBinder_setExtension</td>
<td>AIBinder_getExtension</td>
</tr>
<tr>
<td>Java</td>
<td>android.os.Binder.setExtension</td>
<td>android.os.IBinder.getExtension</td>
</tr>
<tr>
<td>C++</td>
<td>android::Binder::setExtension</td>
<td>android::IBinder::getExtension</td>
</tr>
<tr>
<td>Rust</td>
<td>binder::Binder::set_extension</td>
<td>binder::IBinder::get_extension</td>
</tr>
</tbody>
</table>

# Arquitetura de Segurança e Validação

## 1. SEPolicy (SELinux Policy)

O SELinux é usado para aplicar políticas de segurança. Para HALs AIDL, o SEPolicy define o controle de acesso e a comunicação entre o cliente e o servidor HAL.

*   **Atributos:** `hal_foo_client` e `hal_foo_server` definem os domínios de segurança para o cliente e o servidor HAL.
*   **Regras:** Regras como `binder_call` e `binder_use` controlam o fluxo de comunicação IPC.

## 2. VTS (Vendor Test Suite)

O VTS é um conjunto de testes de integração que verifica a implementação e o comportamento esperado de cada HAL, garantindo a compatibilidade com o Framework do Android.

## 3. VINTF Manifest

O VINTF Manifest é um arquivo de metadados que lista os HALs instalados e esperados no dispositivo, sendo um componente chave na arquitetura Treble e na validação de integridade das camadas HAL.

# Resumo dos Conceitos Técnicos

Os conceitos técnicos centrais são: Binder IPC, AIDL, HIDL, Binderized HAL, Passthrough Mode, Stable AIDL, Parcelable, ParcelableHolder, SEPolicy, VTS, e VINTF Manifest.

---


## Page 6

# Componente 3: Binder IPC

**Itens Técnicos Encontrados:** 12

**Conceitos-Chave:** Binder Transaction Protocol, Parcel, Binder Objects, Death Notification, AIDL Compiler, binder_transaction, binder_buffer, BpBinder, BBinder, Stub, Proxy

# Detalhes Técnicos do Binder IPC no Kernel Linux

## Protocolo de Transação (Binder Transactions)

Mensagens trocadas com o Binder são chamadas de **transações Binder**. Elas podem transportar dados simples (como inteiros) e estruturas mais complexas, como descritores de arquivo, buffers de memória ou referências (fortes/fracas) a objetos.

## Estruturas de Dados Chave no Kernel

1.  **binder_transaction**: Estrutura principal que encapsula a transação.
2.  **binder_buffer**: Buffer de memória alocado pelo kernel para armazenar os dados da transação (o Parcel serializado).
3.  **binder_node**: Representa o objeto de serviço no processo servidor.
4.  **binder_ref**: Representa a referência do cliente ao binder_node no processo servidor.

## Fluxo de Transação (Protocolo)

O fluxo de transação envolve a chamada de sistema `ioctl` no dispositivo `/dev/binder` (ou `/dev/vndbinder`, `/dev/hwbinder`).

1.  **Userland (Cliente)**: O código do cliente chama `transact()`. O Parcel é preparado (serialização) e o `ioctl` com o comando `BINDER_WRITE_READ` é invocado.
2.  **Kernel (Driver Binder)**:
    *   O driver recebe a transação.
    *   **Tradução de Objetos**: O kernel percorre o buffer do Parcel em busca de **Objetos Binder** (`binder_object_header`).
    *   **Mapeamento de Referências**: Se um objeto for uma referência local (`BINDER_TYPE_BINDER`), o kernel o traduz para uma referência remota (`BINDER_TYPE_HANDLE`) para o processo de destino, e vice-versa.
    *   **Alocação de Buffer**: O kernel aloca um `binder_buffer` no espaço de endereçamento do processo alvo.
    *   **Cópia de Dados**: O conteúdo do Parcel (dados e offsets) é copiado para o `binder_buffer` no processo alvo.
    *   **Notificação**: O kernel notifica o processo alvo (servidor) que há uma transação pendente.
3.  **Userland (Servidor)**: Um thread do pool de threads do Binder no servidor recebe a notificação, desempacota o Parcel (dessorialização) e executa o método de serviço.
4.  **Resposta**: O resultado é empacotado em um Parcel de resposta e o fluxo se inverte.

## Estrutura de Dados Parcel

O Parcel é o mecanismo de serialização do Android, otimizado para IPC local.

*   Não é um mecanismo de serialização de propósito geral (não deve ser usado para armazenamento em disco ou rede).
*   Contém dados brutos e uma lista de offsets para objetos Binder (como referências a outros serviços ou descritores de arquivo).
*   **Marshalling/Unmarshalling**: O processo de serialização/dessorialização é chamado de *parceling* (marshalling) e *unparceling* (unmarshalling).

---


## Page 7

# Objetos Binder (Tipos)

Estruturas que representam referências a objetos ou recursos que precisam de tradução pelo kernel:

<table>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BINDER_TYPE_BINDER</td>
      <td>Referência forte a um objeto local (servidor).</td>
    </tr>
    <tr>
      <td>BINDER_TYPE_WEAK_BINDER</td>
      <td>Referência fraca a um objeto local (servidor).</td>
    </tr>
    <tr>
      <td>BINDER_TYPE_HANDLE</td>
      <td>Referência forte a um objeto remoto (cliente).</td>
    </tr>
    <tr>
      <td>BINDER_TYPE_WEAK_HANDLE</td>
      <td>Referência fraca a um objeto remoto (cliente).</td>
    </tr>
    <tr>
      <td>BINDER_TYPE_FD</td>
      <td>Descritor de arquivo que precisa ser duplicado no processo alvo.</td>
    </tr>
    <tr>
      <td>BINDER_TYPE_PTR</td>
      <td>Ponteiro para um buffer de dados (usado em hwbinder).</td>
    </tr>
  </tbody>
</table>

# Notificação de Morte (Death Notification)

**Protocolo/Mecanismo:** Permite que um cliente ( BpBinder ) seja notificado quando o processo do servidor ( BBinder ) ao qual ele se refere morre.

1. **Registro:** O cliente registra um DeathRecipient (receptor de morte) no IBinder remoto (o BpBinder).
2. **Kernel:** O driver Binder rastreia essa relação.
3. **Notificação:** Se o processo do servidor for encerrado, o driver Binder envia uma notificação para o cliente, que executa o método binderDied() do DeathRecipient.

# Compilador AIDL (Android Interface Definition Language)

**Algoritmo/Arquitetura:** O AIDL é uma IDL (Interface Definition Language) que define a interface de programação para IPC.

1. **Entrada:** Arquivo .aidl (define a interface, métodos e tipos de dados).
2. **Processamento:** O compilador AIDL (parte do sistema de build) gera código em linguagens específicas (Java, C++, NDK, Rust).
3. **Saída (Classes Geradas):**
   * **Interface:** Define os métodos da interface.
   * **Stub (Servidor):** Classe abstrata que o servidor implementa. Contém o método onTransact() que recebe o Parcel de entrada, desserializa os dados e chama a implementação do método real.
   * **Proxy (Cliente):** Classe que o cliente usa. Contém o método transact() que serializa os dados no Parcel e invoca o IPC via driver Binder.

**Função do Compilador:** Automatizar o marshalling e unmarshalling (serialização e desserialização) dos dados entre os processos, garantindo que o protocolo de transação seja seguido.

# Android 16 (AOSP) - Mudanças

Embora a pesquisa inicial não tenha revelado mudanças técnicas fundamentais no protocolo Binder para o Android 16, as referências indicam que:

* O AOSP está migrando para a referência android-latest-release em vez de aosp-main (a partir de Março de 2025).
* Houve uma mudança para o tamanho de página de 16KB (começando por volta do Android 15), o que pode ter implicações no gerenciamento de memória do driver Binder, mas o protocolo central permanece o mesmo.

---


## Page 8

# Componente 4: SELinux Android

**Itens Técnicos Encontrados:** 10

**Conceitos-Chave:** Type Enforcement (TE), Contexto de Segurança, Policy Compilation, Common Intermediate Language (CIL), Multi-Category Security (MCS), Atributos, Mapeamento de Política, sepolicy

A implementação do **SELinux (Security-Enhanced Linux)** no Android é um sistema de **Controle de Acesso Obrigatório (MAC)**, fundamental para o *sandboxing* de aplicativos e a proteção de dados. Ele é construído sobre a estrutura **Linux Security Module (LSM)** e utiliza primariamente o componente **Type Enforcement (TE)** [1].

## Estruturas de Dados e Algoritmos de Controle de Acesso

O mecanismo de controle de acesso é baseado em **Contextos de Segurança** (ou *labels*), que são a estrutura de dados central. Um contexto de segurança segue o formato: `user:role:type:sensitivity[:categories]` [1].

*   **Tipo (Type/Domain):** O campo mais crucial. Define o domínio SELinux para processos (sujeitos) e o rótulo para objetos (alvos) como arquivos, *sockets* e serviços Binder [1].
*   **Atributos (Attributes):** Estruturas de dados que agrupam múltiplos tipos, simplificando a escrita de regras de política (ex: `appdomain` agrupa `untrusted_app` e `isolated_app`) [1].

O **algoritmo** de decisão de acesso é implementado através de **Regras de Política** no formato: `allow source target:class permissions;` [1]

<table>
<thead>
<tr>
<th>Elemento</th>
<th>Descrição Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>source</code></td>
<td>O tipo (ou atributo) do sujeito (domínio do processo) que solicita o acesso.</td>
</tr>
<tr>
<td><code>target</code></td>
<td>O tipo (ou atributo) do objeto que está sendo acessado.</td>
</tr>
<tr>
<td><code>class</code></td>
<td>A classe do objeto (ex: `file`, `socket`, `binder`).</td>
</tr>
<tr>
<td><code>permissions</code></td>
<td>A operação permitida (ex: `read`, `write`, `transfer`).</td>
</tr>
</tbody>
</table>

A política opera sob o princípio **default-deny**, onde qualquer acesso não explicitamente permitido por uma regra resulta em uma negação (AVC denial) [3].

## Multi-Category Security (MCS) e Isolamento

O Android utiliza o campo **categories** do contexto de segurança para implementar o **Multi-Category Security (MCS)**, um mecanismo de isolamento de dados [1].

*   **Estrutura de Categorias:** O campo categories utiliza um subconjunto de c0 a c1023 [1].
*   **Algoritmo de Isolamento:** As categorias são dinamicamente alocadas a processos de aplicativos e seus dados correspondentes (`/data/data` e outros) [1] [3]. Este mecanismo garante que:
    1.  Dados de um aplicativo sejam isolados do acesso por outros aplicativos (App Sandboxing) [1].
    2.  Dados sejam isolados entre diferentes usuários físicos do dispositivo [1]. A política SELinux contém regras que exigem a correspondência de categorias para acesso, reforçando o princípio do menor privilégio.

## Arquitetura e Compilação da Política (Policy Compilation)

A política SELinux do Android (sepolicy) é modularizada para permitir atualizações independentes da plataforma e do fornecedor (vendor) [2].

*   **Linguagem de Política:** A maioria das políticas é definida usando a Kernel Policy Language (*.te files), com exceções para o Common Intermediate Language (CIL) [1] [2].
*   **Estrutura Modular (Android 8.0+):**
    *   Platform Public sepolicy: Define a API estável (tipos e atributos) para a política do fornecedor [2].

---


## Page 9

*   **Platform Private sepolicy:** Contém detalhes de implementação interna da plataforma [2].
*   **Vendor sepolicy:** Política específica do dispositivo [2].

*   **Processo de Compilação:**
    1.  Os arquivos de política ( *.te , *_contexts ) são convertidos para o formato **CIL** [2].
    2.  As políticas CIL (Platform Public, Platform Private, Vendor) são combinadas [2].
    3.  Um **arquivo de mapeamento** ( mapping file ) é criado para vincular os atributos da política pública da plataforma com os tipos concretos da política do fornecedor, garantindo a compatibilidade entre versões [2].
    4.  O conjunto final de políticas CIL é compilado em um **arquivo de política binária** ( sepolicy ) que é carregado no kernel [2].

*   **Otimização de Inicialização:** O Android utiliza uma política **pré-compilada** ( precompiled_sepolicy ) armazenada nas partições /vendor ou /odm . O processo init verifica hashes SHA256 dos arquivos CIL de entrada para determinar se a política pré-compilada pode ser carregada diretamente, economizando o tempo de compilação em tempo de execução [2].

## APIs e Estruturas de Associação de Contexto

A associação de tipos a objetos é gerenciada por estruturas de dados de contexto lidas por processos-chave do sistema [3]:

<table>
<thead>
<tr>
<th>Estrutura de Dados (Arquivo)</th>
<th>Objeto Associado</th>
<th>Processo Leitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>file_contexts</td>
<td>Caminhos de arquivos</td>
<td>Vários componentes userspace, restorecon</td>
</tr>
<tr>
<td>property_contexts</td>
<td>Propriedades do sistema Android</td>
<td>init</td>
</tr>
<tr>
<td>service_contexts</td>
<td>Serviços Binder</td>
<td>servicemanager</td>
</tr>
<tr>
<td>seapp_contexts</td>
<td>Processos de aplicativos e diretórios /data/data</td>
<td>zygote, installd</td>
</tr>
</tbody>
</table>

[1] SELinux concepts | Android Open Source Project. [2] Build SELinux policy | Android Open Source Project. [3] Implement SELinux | Android Open Source Project.

---

## Componente 5: Init System - Init.rc syntax, property service, ueventd, bootchart

Itens Técnicos Encontrados: 10

Conceitos-Chave: Android Init Language, Actions, Services, Triggers, Property Service IPC, ueventd kernel socket, ueventd devnode creation, bootchart I/O profiling, APEX versioned RC files

## Conteúdo Técnico: Init System (Android 16 AOSP)

O sistema Init do Android, composto por init , ueventd , property service e a ferramenta bootchart , é o primeiro processo em espaço de usuário e o pilar da inicialização do sistema operacional. O conteúdo técnico a seguir foca na arquitetura, protocolos, estruturas de dados e algoritmos desses componentes.

### 1. Sintaxe Init.rc (Android Init Language)

A Android Init Language é um formato de arquivo de configuração estruturado em linhas, utilizado pelo processo init para definir a sequência de inicialização e o gerenciamento de serviços.

#### 1.1. Estrutura e Arquitetura

A linguagem é composta por cinco classes principais de declarações [1]:

1.  **Actions:** Sequências nomeadas de comandos que são executadas quando um trigger correspondente é satisfeito.
2.  **Commands:** Funções internas executadas sequencialmente dentro de uma Action.

---


## Page 10

3. **Services**: Programas que o `init` inicia e, opcionalmente, reinicia quando terminam.
4. **Options**: Modificadores que afetam como e quando um Service é executado.
5. **Imports**: Mecanismo para incluir outros arquivos de configuração `.rc`.

**Arquitetura de Configuração (APEX Versioning)**: A partir do Android T (e aplicável ao Android 16), o `init` suporta arquivos `.rc` versionados dentro de módulos **APEX** (Android Pony EXpress) para garantir a compatibilidade com diferentes SDKs. O padrão de nomenclatura é `init.#rc`, onde `#` é o primeiro SDK onde o arquivo é aceito. O `init` aplica a regra de seleção que escolhe o maior valor `.rc` que não exceda o SDK do sistema em execução [1].

## 1.2. Algoritmos e Mecanismos de Execução

*   **Mecanismo de Enfileiramento de Actions**: Quando um trigger ocorre, a Action correspondente é adicionada à cauda de uma fila de execução (to-be-executed queue). As Actions são desenfileiradas e seus Commands são executados sequencialmente. O `init` intercala a execução de Commands com outras atividades (criação/destruição de dispositivos, configuração de propriedades, reinício de processos) [1].
*   **Triggers**:
    *   **Event Triggers**: Formato simples `<event>` (ex: early-init, boot). Satisfeitos quando o `init` atinge o estágio correspondente.
    *   **Property Triggers**: Formato `property:<name>=<value>`. Satisfeitos quando a propriedade do sistema `<name>` assume o valor `<value>`. Múltiplos triggers podem ser combinados com o operador lógico `&&` [1].

## 1.3. APIs (Comandos Internos)

O `init` expõe uma vasta API de comandos internos, incluindo:

<table>
<thead>
<tr>
<th>Categoria</th>
<th>Comando (Exemplos)</th>
<th>Função Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td>Controle de Serviço</td>
<td><code>start &lt;service&gt;</code>, <code>stop &lt;service&gt;</code>, <code>restart &lt;service&gt;</code>, <code>class_start &lt;class&gt;</code></td>
<td>Gerenciamento do ciclo de vida de processos em espaço de usuário.</td>
</tr>
<tr>
<td>Sistema de Arquivos</td>
<td><code>mount &lt;type&gt; &lt;device&gt; &lt;dir&gt;</code>, <code>umount &lt;path&gt;</code>, <code>mkdir &lt;path&gt;</code>, <code>chmod &lt;mode&gt; &lt;path&gt;</code>, <code>chown &lt;owner&gt; &lt;group&gt; &lt;path&gt;</code></td>
<td>Configuração e montagem de partições, criação de diretórios e ajuste de permissões.</td>
</tr>
<tr>
<td>Propriedades</td>
<td><code>setprop &lt;name&gt; &lt;value&gt;</code>, <code>wait_for_prop &lt;name&gt; &lt;value&gt;</code></td>
<td>Leitura e escrita de propriedades do sistema.</td>
</tr>
<tr>
<td>Execução</td>
<td><code>exec -- &lt;command&gt;</code>, <code>exec_start &lt;service&gt;</code>, <code>exec_background - - &lt;command&gt;</code></td>
<td>Execução de programas externos, com ou sem bloqueio da sequência de comandos do init .</td>
</tr>
<tr>
<td>SELinux</td>
<td><code>restorecon &lt;path&gt;</code>, <code>restorecon_recursive &lt;path&gt;</code></td>
<td>Restauração do contexto de segurança SELinux em arquivos e diretórios.</td>
</tr>
</tbody>
</table>

## 2. Property Service

O Property Service é o mecanismo central para o compartilhamento de informações de configuração e estado entre processos no Android.

### 2.1. Protocolo e Arquitetura

*   **IPC (Inter-Process Communication)**: O serviço é implementado para permitir que processos leiam e escrevam propriedades do sistema (pares chave-valor) [3].
*   **Controle de Serviço via Propriedades**: O `init` expõe um protocolo de controle através de propriedades que começam com `ctl.` , como `ctl.start`, `ctl.stop`, `ctl.restart`, e `ctl.interface_start`. A escrita de um valor nessas propriedades desencadeia o comando correspondente no `init` [1].
*   **Assincronia**: A opção `ro.property_service.async_persist_writes` (se true ) permite que as escritas de propriedades persistentes ( persist. ) e não persistentes ocorram de forma assíncrona, sem ordem definida [1].

---


## Page 11

# 2.2. Estruturas de Dados

As propriedades são armazenadas em memória e acessíveis por meio de APIs de leitura e escrita. O estado de um serviço é refletido na propriedade `init.svc.<name>` (valores: stopped, stopping, running, restarting) [1].

# 3. ueventd

O ueventd é um daemon que gerencia a criação de nós de dispositivo em `/dev`, a configuração de permissões em `/sys` e o carregamento de firmware, operando com base em eventos do kernel.

## 3.1. Protocolo e Algoritmo

*   **Protocolo de Comunicação:** O ueventd opera escutando os sockets uevent do kernel [2]. O kernel envia mensagens uevent sempre que um dispositivo é adicionado ou removido [4].
*   **Algoritmo de Criação de Nós (`/dev`):**
    1.  Recebe um uevent (ex: add, remove).
    2.  Cria/deleta o nó em `/dev` com base no uevent DEVPATH.
    3.  Aplica o contexto de segurança SELinux (SELabel) e permissões (modo, usuário, grupo) [2].
    4.  **Path Matching:** Usa a função fnmatch (com ou sem a flag FNM_PATHNAME) para corresponder o caminho do dispositivo com as regras definidas no ueventd.rc [2].
*   **Gerenciamento de Firmware:** O ueventd serve requisições de firmware, buscando o arquivo correspondente ao uevent FIRMWARE em diretórios pré-definidos (`firmware_directories`) e em `/apex/*/etc/firmware` [2].

# 4. bootchart

O bootchart é uma ferramenta de diagnóstico de desempenho focada na inicialização do sistema.

## 4.1. Algoritmo de Profiling

*   **Mecanismo:** Fornece o detalhamento de carga de CPU e I/O de todos os processos durante a inicialização [1].
*   **Ativação:** É ativado pela existência do arquivo `/data/bootchart/enabled` ou pela opção `-bootchart timeout` no emulador [1].
*   **Comandos:** Os comandos bootchart start e bootchart stop são usados no init.rc para delimitar o período de coleta de dados [1].
*   **Análise:** O script compare-bootcharts.py é uma ferramenta de análise que compara os tempos de início/fim de processos selecionados entre dois bootcharts (em milissegundos), auxiliando na identificação de regressões de desempenho [1].

---

## Referências

[1] init/README.md - platform/system/core - Git at Google. Android Open Source Project. URL: https://android.googlesource.com/platform/system/core/+/master/init/README.md
[2] Ueventd - platform/system/core - Git at Google. Android Open Source Project. URL: https://android.googlesource.com/platform/system/core/+/master/init/README.ueventd.md
[3] property_service.cpp - platform/system/core - Git at Google. Android Open Source Project. URL: https://android.googlesource.com/platform/system/core/+/refs/heads/main/init/property_service.cpp
[4] kernel - How does udev/uevent work? Stack Exchange. URL: https://unix.stackexchange.com/questions/550037/how-does-udev-uevent-work

---

## Componente 6: Native Libraries - Bionic libc, libcutils, liblog, libhardware

Itens Técnicos Encontrados: 27

---


## Page 12

**Conceitos-Chave:** Scudo Hardened Allocator, fdsan Ownership Tagging, Arm MTE, Logd Protocol, qtaguid Socket Tagging, hw_module_t, hw_device_t, Dynamic Linker, ELF TLS, _FORTIFY_SOURCE

# Conteúdo Técnico: Native Libraries (Bionic libc, libcutils, liblog, libhardware)

Este documento detalha os principais aspectos técnicos (arquitetura, algoritmos, estruturas de dados, protocolos e APIs) das bibliotecas nativas do Android 16 (AOSP): Bionic libc, libcutils, liblog e libhardware.

## 1. Bionic libc (C Library, Math Library, and Dynamic Linker)

A Bionic é a implementação da biblioteca C padrão do Android, otimizada para ambientes móveis, com foco em segurança e eficiência de recursos.

### Arquitetura

A Bionic é estruturalmente dividida em:

*   **libc**: Implementação das chamadas de sistema (syscall wrappers) e funções padrão C (POSIX/BSD/Linux).
*   **libm**: Biblioteca matemática.
*   **libdl**: Biblioteca de interface do linker dinâmico, contendo stubs que são substituídos em tempo de execução pelo próprio linker.
*   **Dynamic Linker**: Componente responsável pelo carregamento e linkagem dinâmica de bibliotecas.

### Algoritmos e Mecanismos de Segurança

#### 1.1. Alocador de Memória Nativo (Native Allocator)

O alocador padrão é o **Scudo Hardened Allocator**, projetado para mitigar vulnerabilidades de segurança como *use-after-free* e *buffer overflows*.

*   **APIs de Controle:**
    *   `malloc_disable` / `malloc_enable`: Usadas para pausar/retomar threads de alocação, garantindo a consistência durante a iteração de alocação (usado por `libmemunreachable` ).
    *   `malloc_iterate`: Enumera todas as alocações ativas.
*   **Extensões `mallopt`:**
    *   `M_DECAY_TIME`: Controla o atraso na purga e liberação de memória não utilizada de volta ao kernel (para reduzir o Resident Set Size - RSS).
    *   `M_PURGE`: Força a purga e liberação imediata de memória.

#### 1.2. File Descriptor Sanitizer (fdsan)

Mecanismo de segurança que detecta o manuseio incorreto de descritores de arquivo (*use-after-close* e *double-close*).

*   **Algoritmo:** Ownership Tagging (Aplicação de Tag de Propriedade).
*   **Estrutura de Dados:** Uma tag de fechamento de 64 bits, onde 8 bits definem o tipo de proprietário ( enum `android_fdan_owner_type`) e 56 bits definem um valor identificador único do objeto proprietário. A detecção de erro ocorre se um descritor é fechado com uma tag incorreta ou sem tag.

#### 1.3. Memory Tagging Extension (MTE)

Integração com o MTE da Arm para detecção de acessos inválidos à memória.

---


## Page 13

*   **Mecanismos:**
    *   **Heap Tagging:** Implementado no Scudo, atualizando tags em `malloc` e `free`.
    *   **Stack Tagging:** Implementado via instrumentation pass do LLVM (AArch64StackTagging) para definir tags de acordo com o tempo de vida dos objetos na pilha.
*   **Protocolo de Inicialização:** O linker (`ld`) adiciona seções dinâmicas e notas ELF específicas (`--android-memtag-mode`) que são lidas pela função `__libc_init_mte` da libc para configurar o nível de MTE no kernel via `prctl`.

# 2. liblog (Sistema de Logging)

A liblog fornece a interface para o sistema de logging do Android, comunicando-se com o daemon `logd` via sockets.

## Protocolo de Comunicação (liblog -> logd)

A comunicação é baseada em uma estrutura binária que encapsula o cabeçalho e o payload.

## Estruturas de Dados do Protocolo

*   **android_log_header_t**: Contém `uint8_t id` (buffer de log), `uint16_t tid` (Thread ID) e `log_time realtime` (timestamp).
*   **log_time**: Estrutura de 64 bits para timestamp, dividida em `uint32_t tv_sec` (segundos) e `uint32_t tv_nsec` (nanosegundos).
*   **Payload string**: Usado para logs de texto (main, system, etc.), contendo `char prio` (prioridade), `char tag[]` (string nula-terminada) e `char message[]` (string nula-terminada).
*   **Payload binary (Event Logs)**: Usado para logs de eventos (events, security), começando com `android_event_header_t` (int32_t tag do evento) seguido por estruturas de dados tipadas para o payload (e.g., `android_event_int_t`, `android_event_string_t`).

# 3. libcutils (Utilitários C)

A libcutils é uma biblioteca de utilidades de baixo nível que fornece funcionalidades comuns para ferramentas e bibliotecas do Android.

## Protocolo e Mecanismo de Rede

*   **qtaguid Socket Tagging**: Implementa a funcionalidade de socket tagging para contabilidade de tráfego de rede (Network Traffic Accounting).
*   **Protocolo de Comunicação com o Kernel**: O mecanismo utiliza a interface do kernel `/proc/net/xt_qtaguid/ctrl` para associar uma tag (que inclui UID, PID e classe de tráfego) a um socket, permitindo o rastreamento de uso de dados por aplicativo.
*   **APIs**: Funções como `set_socket_tag` e `get_socket_tag`.

## Outras APIs

*   **APIs de Política de Agendamento**: Funções para manipular a política de agendamento de threads (`sched_policy.c`), permitindo que processos definam prioridades de execução.

# 4. libhardware (Hardware Abstraction Layer Legado)

A libhardware define a interface para o HAL legado do Android, que é baseado em módulos dinamicamente carregáveis.

---


## Page 14

# Arquitetura e Estruturas de Dados

A arquitetura é baseada em módulos (`.so`) que exportam símbolos específicos.

*   **Estrutura do Módulo (`hw_module_t`):**
    *   Estrutura base que todo módulo HAL deve exportar através do símbolo `HAL_MODULE_INFO_SYM`.
    *   Campos chave incluem `tag` (`HARDWARE_MODULE_TAG`), `module_api_version`, `hal_api_version`, `id`, `name`, `author` e um ponteiro para a estrutura de métodos (`hw_module_methods_t`).
*   **Estrutura do Dispositivo (`hw_device_t`):**
    *   Estrutura base para um dispositivo específico fornecido pelo módulo.
    *   Inclui `tag` (`HARDWARE_DEVICE_TAG`), `version` (específica do módulo) e um ponteiro para a função `close`.

# Protocolo de Carregamento de Módulos

*   **API de Carregamento:** `int hw_get_module(const char *id, const struct hw_module_t **module)`.
*   **Algoritmo de Carregamento:** A função resolve o `id` do módulo para um caminho de arquivo (`/system/lib/hw/<id>.default.so`), usa `dlopen` para carregar o arquivo e busca o símbolo `HAL_MODULE_INFO_SYM` para obter a estrutura `hw_module_t`.

---

# Resumo Técnico

<table>
  <thead>
    <tr>
      <th>Componente</th>
      <th>Algoritmos/Mecanismos</th>
      <th>Estruturas de Dados</th>
      <th>Protocolos/APIs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bionic libc</td>
      <td>Scudo Hardened Allocator, fdsan Ownership Tagging, Arm MTE (Heap/Stack Tagging), _FORTIFY_SOURCE</td>
      <td>Tag de Fechamento (64-bit), Seções/Notas ELF (MTE)</td>
      <td>malloc/mallopt Extensions (M_DECAY_TIME, M_PURGE), __libc_init_mte, Wrappers de Syscall</td>
    </tr>
    <tr>
      <td>liblog</td>
      <td>Comunicação via Socket</td>
      <td>android_log_header_t, log_time, Estruturas de Log de Eventos (android_event_*_t)</td>
      <td>Logd Protocol (Binário/String)</td>
    </tr>
    <tr>
      <td>libutils</td>
      <td>qtaguid Socket Tagging, APIs de Política de Agendamento</td>
      <td>N/A (Funções de utilidade)</td>
      <td>/proc/net/xt_qtaguid/ctrl Interface, set_socket_tag / get_socket_tag</td>
    </tr>
    <tr>
      <td>libhardware</td>
      <td>Algoritmo de Carregamento de Módulos (dlopen/dlsym)</td>
      <td>hw_module_t, hw_device_t</td>
      <td>hw_get_module, HAL_MODULE_INFO_SYM (Símbolo de Exportação)</td>
    </tr>
  </tbody>
</table>

---

# Componente 7: ART Android Runtime

**Itens Técnicos Encontrados:** 15

**Conceitos-Chave:** Generational Concurrent Mark-Compact (CMC) GC, Concurrent Copying (CC) GC, RegionTLAB, RosAlloc, Read-Barrier, AOT Compilation, JIT Compilation, Profile-Guided Optimization (PGO), dex2oat, .vdex, .odex, .art, Generational GC Strategy

# ART Android Runtime: Compilação e Gerenciamento de Memória no Android 16 (AOSP)

O Android Runtime (ART) no Android 16 mantém e aprimora a arquitetura de execução híbrida (Ahead-Of-Time/Just-In-Time/Interpretação) e introduz um novo algoritmo de Garbage Collection (GC) para otimizar o desempenho e a eficiência energética.

---


## Page 15

# 1. Arquitetura de Compilação (AOT e JIT)

O ART utiliza uma abordagem de compilação em múltiplas etapas, guiada por perfis de execução (Profile-Guided Optimization - PGO), para equilibrar o tempo de instalação, o uso de espaço em disco e o desempenho em tempo de execução [1].

## 1.1. Processo de Compilação Híbrida

O fluxo de compilação e otimização no ART é o seguinte [1]:

1. **Instalação Inicial (AOT com Perfil Cloud):** Na instalação de um aplicativo, o compilador AOT (dex2oat) utiliza um perfil de metadados (.dm file) distribuído pela Play Store (perfil *cloud*). Os métodos listados neste perfil são compilados AOT. Se o perfil *cloud* não estiver disponível, nenhuma compilação AOT é realizada.
2. **Execução Inicial (Interpretação e JIT):** Nas primeiras execuções, métodos não compilados AOT são interpretados. Métodos executados com frequência (*hot methods*) são compilados JIT. O ART gera um perfil de execução local e o combina com o perfil *cloud* (se existir).
3. **Otimização em Background (Daemon de Compilação):** Quando o dispositivo está ocioso e carregando, um *daemon* de compilação re-compila o aplicativo usando o perfil combinado, resultando em mais código AOT compilado.

## 1.2. Artefatos de Compilação

O compilador dex2oat gera artefatos de compilação que são carregados pelo runtime (libart.so) [1]:

<table>
<thead>
<tr>
<th>Artefato</th>
<th>Descrição Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td>.vdex</td>
<td>Contém metadados para acelerar a verificação e, em alguns casos, o código DEX não comprimido.</td>
</tr>
<tr>
<td>.odex</td>
<td>Contém o código AOT compilado para os métodos no APK.</td>
</tr>
<tr>
<td>.art</td>
<td>Contém representações internas do ART de strings e classes listadas no APK, usadas para acelerar o startup do aplicativo.</td>
</tr>
</tbody>
</table>

## 1.3. Filtros do Compilador (APIs de Configuração)

Os filtros do compilador controlam como o ART compila o código DEX e são passados como opções para o dex2oat [1]:

<table>
<thead>
<tr>
<th>Filtro</th>
<th>Algoritmo de Compilação</th>
</tr>
</thead>
<tbody>
<tr>
<td>verify</td>
<td>Executa apenas a verificação do código DEX (sem compilação AOT).</td>
</tr>
<tr>
<td>speed</td>
<td>Executa a verificação do código DEX e compila AOT todos os métodos.</td>
</tr>
<tr>
<td>speed-profile</td>
<td>Executa a verificação do código DEX, compila AOT apenas os métodos listados no perfil e otimiza o carregamento de classes listadas no perfil.</td>
</tr>
</tbody>
</table>

A compilação AOT de bibliotecas e aplicativos pré-instalados durante a construção da imagem do sistema é chamada de **Dexpreopt**. A configuração é controlada por variáveis de build como PRODUCT_DEX_PREOPT_DEFAULT_COMPILER_FILTER e PRODUCT_SYSTEM_SERVER_COMPILER_FILTER [1].

# 2. Algoritmos e Estruturas de Dados de Garbage Collection (GC)

O Android 16 QPR2 introduz uma melhoria significativa no gerenciamento de memória com um novo coletor de lixo [2].

## 2.1. Generational Concurrent Mark-Compact (CMC) GC

O Generational Concurrent Mark-Compact (CMC) Garbage Collector é a principal novidade no ART do Android 16 QPR2 [2]. Este algoritmo é uma evolução do GC padrão (Concurrent Copying) e foca a coleta em objetos recém-alocados (geração jovem), resultando em menor uso de CPU e maior eficiência de bateria [2].

## 2.2. GC Padrão (Concurrent Copying - CC)

O GC padrão do ART, desde o Android 8, é o **Concurrent Copying (CC)**, que se tornou **Generational** a partir do Android 10 [3].

---


## Page 16

# Componente 7: Garbage Collection - Generational GC, CMS, ART

## 2.1. Garbage Collection (GC) - Generational GC

O ART utiliza o Garbage Collection (GC) de geração jovem (young GC) e geração completa (full-heap GC) [3]:

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Descrição e Algoritmo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Algoritmo</td>
      <td><b>Generational GC</b>. O GC realiza coletas da geração jovem (young GC) até que o throughput (calculado por bytes liberados/segundo de duração do GC) caia abaixo da média do throughput das coletas de heap completo (full-heap GC). Nesse ponto, ele alterna para um full-heap GC [3].</td>
    </tr>
  </tbody>
</table>

## 2.2. Garbage Collection (GC) - CMS

O ART ainda suporta o **Concurrent Mark Sweep (CMS)**, que utiliza um alocador diferente e compactação adiada [3]:

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Descrição e Algoritmo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Algoritmo</td>
      <td><b>Concurrent Mark Sweep</b> (Marcação e Varredura Concorrente). A compactação é evitada até que o aplicativo vá para o background ou quando uma falha de alocação ocorre devido à fragmentação [3].</td>
    </tr>
  </tbody>
</table>

## 2.3. GC Alternativo (Concurrent Mark Sweep - CMS)

O ART ainda suporta o **Concurrent Mark Sweep (CMS)**, que utiliza um alocador diferente e compactação adiada [3]:

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Descrição e Algoritmo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Algoritmo</td>
      <td><b>Concurrent Mark Sweep</b> (Marcação e Varredura Concorrente). A compactação é evitada até que o aplicativo vá para o background ou quando uma falha de alocação ocorre devido à fragmentação [3].</td>
    </tr>
  </tbody>
</table>

## 2.4. APIs e Comandos de Depuração

O ART fornece mecanismos para depuração e análise de desempenho do GC [3]:

*   **API de Configuração:** A variável de ambiente `ART_USE_READ_BARRIER` (valor padrão `true` para CC) pode ser alterada para selecionar o tipo de GC em tempo de build [3].
*   **Comando de Depuração:** O comando `adb shell kill -s QUIT PID` envia o sinal SIGQUIT para um aplicativo em execução, forçando-o a despejar informações de desempenho do GC, incluindo histogramas de fases e pausas, no arquivo `/data/anr/` [3].

---

## Referências

[1] Configure ART | Android Open Source Project. URL: https://source.android.com/docs/core/runtime/configure
[2] Android 16 QPR2 is Released. Android Developers Blog. URL: https://android-developers.googleblog.com/2025/12/android-16-qpr2-is-released.html
[3] Debug ART garbage collection | Android Open Source Project. URL: https://source.android.com/docs/core/runtime/gc-debug

---

# Componente 8: Dalvik Bytecode - DEX format, instruction set, optimization, verification

Itens Técnicos Encontrados: 14

**Conceitos-Chave:** DEX Format, LEB128, Conjunto de Instruções Dalvik/ART, Máquina de Registros, Verificador de Bytecode, dexopt, dex2oat, Filtros de Compilação ART

O componente **Dalvik Bytecode** e seu formato executável **DEX** (Dalvik Executable) são fundamentais para a execução de aplicações no Android Runtime (ART) do Android 16 (AOSP). O foco técnico reside na estrutura de dados do arquivo DEX, no conjunto de instruções da máquina de registros e nos algoritmos de verificação e otimização.

---


## Page 17

# 1. Formato de Arquivo DEX (Estruturas de Dados e Formato de Arquivo)

O arquivo `.dex` é uma estrutura de dados que contém um conjunto de definições de classe e dados adjuntos. Sua arquitetura é projetada para ser eficiente em termos de memória e I/O, permitindo o mapeamento de memória (mmap) e o compartilhamento de dados entre processos.

## Estrutura de Dados Principal

O layout do arquivo DEX é composto por uma sequência de seções, sendo as principais:

*   **header_item**: Contém metadados do arquivo, incluindo a *checksum* e *signature* (SHA-1) para verificação de integridade, e *offsets* para as outras seções. Inclui a constante mágica `DEX_FILE_MAGIC` (ex: `dex\n039\0` para a versão 039).
*   **Tabelas de Identificadores**: Listas ordenadas e indexadas que atuam como *pools* de constantes:
    *   `string_ids`: Identificadores para todas as *strings* usadas.
    *   `type_ids`: Identificadores para todos os tipos (classes, arrays, primitivos).
    *   `proto_ids`: Identificadores para protótipos de métodos (tipos de retorno e argumentos).
    *   `field_ids`: Identificadores para campos.
    *   `method_ids`: Identificadores para métodos.
*   **class_defs**: Lista de definições de classe, ordenadas de forma que superclasses e interfaces apareçam antes das classes que as referenciam.
*   **data**: Área de dados que armazena estruturas de suporte, como listas de tipos (`type_list`), dados de código (`code_item`), e dados de anotação.

## Codificação de Dados (LEB128)

O formato DEX utiliza a codificação **LEB128** (*Little-Endian Base 128*) para quantidades inteiras de comprimento variável (variável-length), otimizando o espaço.

*   **sleb128**: LEB128 assinado.
*   **uleb128**: LEB128 não assinado.
*   **uleb128p1**: LEB128 não assinado para representar um valor assinado mais um, permitindo que o valor `-1` (ou `0xfffffffffff`) seja codificado em um único *byte*.

# 2. Conjunto de Instruções (Arquitetura)

O Dalvik/ART utiliza um modelo de **Máquina de Registros** (*Register-based machine*), em contraste com a máquina de pilha do Java Virtual Machine (JVM).

## Modelo de Máquina e Convenções

*   **Registros**: A máquina é baseada em registros de 32 bits (`v0` a `v65535`). Pares de registros adjacentes são usados para valores de 64 bits (como `long` e `double`).
*   **Unidade de Armazenamento**: O fluxo de instruções é composto por quantidades não assinadas de 16 bits.
*   **Convenções de Chamada**: Os argumentos de um método são passados para os últimos `N` registros do *frame* de invocação. Métodos de instância recebem uma referência `this` como primeiro argumento.

## Formatos de Instrução

As instruções são codificadas em diversos formatos para otimizar o tamanho do bytecode, com o formato sendo indicado por um sufixo (ex: `10x`, `22x`). O formato define o número de unidades de 16 bits e a disposição dos campos (opcode, registradores, literais, offsets).

---


## Page 18

<table>
  <thead>
    <tr>
      <th>Formato</th>
      <th>Unidades (16-bit)</th>
      <th>Exemplo de Sintaxe</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10x</td>
      <td>1</td>
      <td>nop</td>
      <td>Sem operandos.</td>
    </tr>
    <tr>
      <td>12x</td>
      <td>1</td>
      <td>move vA, vB</td>
      <td>4 bits para A e B.</td>
    </tr>
    <tr>
      <td>22x</td>
      <td>2</td>
      <td>move/from16 vAA, vBBBB</td>
      <td>8 bits para AA, 16 bits para BBBB.</td>
    </tr>
    <tr>
      <td>35c</td>
      <td>3</td>
      <td>invoke-virtual {vC, vD, vE, vF, vG}, meth@BBBB</td>
      <td>Chamada de método com até 5 argumentos.</td>
    </tr>
    <tr>
      <td>30t</td>
      <td>3</td>
      <td>goto/32 +AAAAAAAA</td>
      <td>Salto de 32 bits.</td>
    </tr>
  </tbody>
</table>

## 3. Verificação e Otimização (Algoritmos e Processos)

O Android Runtime (ART) utiliza o compilador **dex2oat** para processar o bytecode DEX. Este processo envolve verificação e otimização *Ahead-of-Time* (AOT) ou *Profile-Guided* (PGO).

### Verificação de Bytecode

O Verificador de Bytecode Dalvik (e subsequentemente o ART Verifier) realiza uma análise de fluxo de dados (*Data Flow Analysis*) para garantir a segurança de tipos e a integridade do código.

*   **Garantias:** Assegura que o código não viola a segurança de tipos, que os registros são usados corretamente e que o fluxo de controle é válido.
*   **Diferenças Chave:** Não verifica o tamanho da pilha de operandos (pois não há pilha) e impõe restrições mais rigorosas de segurança de tipos em larguras inteiras sub-32 bits.
*   **Verificação Diferida:** Para erros de acesso (ex: *IllegalAccessException*), o verificador pode substituir a instrução problemática por um opcode “always throw” em uma cópia modificável do método, adiando o erro para o momento da execução.

### Otimização ART/dex2oat

O dex2oat é a ferramenta de compilação que transforma o bytecode DEX em código de máquina nativo (ODEX/VDEX/ART).

### Filtros de Compilação (ART): Controlam o nível de otimização aplicado:

*   **speed-profile**: Otimiza apenas o código que foi executado com frequência (baseado em perfis de uso), oferecendo um equilíbrio entre velocidade e espaço em disco. É o filtro padrão no Android 16.
*   **speed**: Compila o máximo de código possível, priorizando a velocidade de execução.
*   **everything-profile**: Similar ao speed-profile, mas com otimizações mais agressivas.
*   **everything**: Compila todo o código, ignorando perfis.

### Otimizações Específicas (Passes de Otimização):

*   **Resolução Simbólica:** Substituição de referências simbólicas por valores diretos:
    *   Chamadas de métodos virtuais: Substituição do índice do método pelo índice da *vtable* (*vtable index*).
    *   Acesso a campos de instância: Substituição do índice do campo pelo offset de *byte*.
*   **Inlining:** Substituição de chamadas de métodos de alto volume (ex: `String.length()` ) por implementações nativas diretas.
*   **Poda de Métodos (**Method Pruning**): Remoção de métodos vazios ou ineficientes (ex: `Object.<init>` ).
*   **Pré-computação de Dados:** Adição de dados pré-calculados (ex: tabelas *hash* para pesquisa de nome de classe) ao arquivo DEX otimizado para economizar tempo de inicialização e memória.

O processo de otimização é crucial para o desempenho do Android, garantindo que o bytecode seja pré-verificado e otimizado antes da execução, minimizando o uso de memória total do sistema através do compartilhamento de dados de classe entre múltiplos processos.

---


## Page 19

# Componente 9: Zygote - Process forking, preloading classes, socket activation

**Itens Técnicos Encontrados:** 12

**Conceitos-Chave:** Copy-on-Write (CoW), ZygoteInit.main(), ZygoteServer, Unix Domain Socket, USAP (Unspecialized App Processes), Preload Classes, Preload Resources, fork() syscall, PID, cgroup, ART/Dalvik VM, File Descriptor Hygiene

## Conteúdo Técnico: Zygote - Process forking, preloading classes, socket activation (Android 16 AOSP)

O **Zygote** é um processo fundamental na arquitetura do Android, atuando como o progenitor de todos os processos de aplicativos e de alguns processos de sistema (como o `system_server`). Sua função principal é otimizar o tempo de inicialização de aplicativos e o uso de memória através de três mecanismos técnicos centrais: *process forking*, *preloading classes* e *socket activation* [1] [2].

### 1. Arquitetura e Inicialização

O Zygote é iniciado pelo *init daemon* do Android durante a sequência de *boot*. O ponto de entrada do Zygote é o binário nativo `app_process` (escrito em C++), que executa o método estático `ZygoteInit.main()` (implementado em Java) [3].

### Estruturas de Dados e APIs

*   **ZygoteInit.java**: Contém a lógica de inicialização e o *preloading*.
*   **ZygoteServer.java**: Implementa a estrutura de servidor de socket para aguardar comandos.
*   **ZygoteConnection.java**: Gerencia a conexão individual com o cliente (geralmente o `system_server`).
*   **ZygoteState**: Estrutura que mantém o estado do Zygote, incluindo o status do *preloading* e a conexão com o socket.

### 2. Process Forking (Criação de Processos)

O mecanismo de criação de processos do Zygote é baseado na chamada de sistema `fork()` do Linux, aproveitando o princípio de *Copy-on-Write (CoW)* [4].

### Algoritmo de Forking

1.  O `system_server` (ou outro cliente) envia um comando de criação de processo para o Zygote via *Unix Domain Socket*.
2.  O Zygote (processo pai) executa a chamada de sistema `fork()` [5].
3.  O kernel cria um novo processo (filho) que compartilha as páginas de memória do Zygote pai, incluindo o *heap* da **ART/Dalvik VM** e as classes pré-carregadas.
4.  O processo filho (o novo aplicativo) executa código específico para se diferenciar do pai, incluindo:
    *   **Alteração de Identificadores**: O processo filho altera seu **PID** (Process ID), **UID** (User ID) e **GID** (Group ID) para corresponder ao aplicativo que está sendo iniciado.
    *   **Limpeza de Descritores de Arquivo**: O Zygote aplica um algoritmo de **File Descriptor Hygiene** (Higiene de Descritores de Arquivo). Descritores de arquivo abertos no Zygote que não estão em uma *allowlist* são redirecionados para `/dev/null` usando a chamada de sistema `dup` para evitar acesso não intencional a recursos do sistema pelo processo filho [1].
5.  O processo filho inicia a execução do código do aplicativo.

### Estrutura de Dados: Copy-on-Write (CoW)

O CoW é uma técnica de gerenciamento de memória onde o processo filho compartilha as páginas de memória do pai. A cópia física da página só ocorre quando o processo filho tenta escrever nela, garantindo que a memória pré-carregada seja compartilhada de forma eficiente e apenas as modificações sejam alocadas separadamente.

---


## Page 20

# 3. Preloading Classes e Recursos

O Zygote pré-carrega classes e recursos essenciais do framework Android antes de entrar em seu loop de escuta, garantindo que cada novo processo de aplicativo já tenha essas estruturas em memória [6].

## Algoritmo de Preloading

O *preloading* é realizado dentro do método `ZygoteInit.main()` através de chamadas como `preloadClasses()` e `preloadResources()` [6].

1.  **preloadClasses()**: Carrega classes do frameworkAndroid (ex: `android.app.*`, `android.view.*`) e as inicializa.
2.  **preloadResources()**: Carrega recursos do sistema (imagens, layouts, strings) e os armazena em estruturas de dados compartilhadas.
3.  **preloadDexCaches()**: Preenche os caches de dex com classes, campos e métodos trazidos pelo preloading.

## Estruturas de Dados

*   **DexCache**: Estrutura de dados interna da ART (Android Runtime) que armazena informações sobre classes e métodos carregados, otimizando o acesso.
*   **Memória Compartilhada**: As classes e recursos pré-carregados residem em regiões de memória que são compartilhadas entre o Zygote e todos os processos filhos via CoW.

# 4. Socket Activation e Protocolo de Comunicação

O Zygote atua como um servidor que escuta comandos de criação de processos através de um Unix Domain Socket [7].

## Protocolo de Comunicação

*   **Localização do Socket**: O Zygote escuta em um stream socket localizado em `/dev/socket/zygote` (ou similar, dependendo da configuração) [8].
*   **Comando**: O cliente (geralmente o `system_server`) envia um comando de texto via socket. O comando inclui parâmetros como o nome da classe principal a ser executada, o UID/GID do processo, e as capacidades de segurança (SELinux, cgroups) [1].
*   **Estrutura de Dados (Comando)**: O comando é tipicamente uma lista de strings separadas por null ou por um delimitador, que o Zygote analisa para configurar o novo processo.
*   **Resposta**: Após o forking e a configuração, o Zygote envia o PID do novo processo de volta ao cliente via socket.

## Algoritmo de Escuta

O ZygoteServer executa um loop de escuta:

1.  **runSelectLoopMode()**: O Zygote entra em um loop infinito, aguardando conexões de clientes no Unix Domain Socket.
2.  **select()**: Utiliza a chamada de sistema select() para monitorar o socket de escuta e quaisquer conexões de clientes ativas.
3.  **handleNewConnection()**: Quando uma nova conexão é detectada, um novo thread ou objeto ZygoteConnection é criado para gerenciar a comunicação.
4.  **runOnce()**: O ZygoteConnection lê o comando, executa o forking e envia a resposta.

## USAP (Unspecialized App Processes) Pool

A partir de versões mais recentes do Android (incluindo o Android 16), o Zygote pode manter um pool de processos pré-forkados e não especializados (USAP) para reduzir ainda mais a latência de inicialização de aplicativos [1].

*   **Algoritmo USAP**: O Zygote pré-forka processos USAP e os mantém em um pool. Quando um aplicativo é solicitado, o `system_server` se conecta a um USAP disponível via socket, e o USAP é “especializado” (alteração de PID, cgroup, etc.) para o aplicativo, eliminando a necessidade de um fork() síncrono [1].

---


## Page 21

[1] About the Zygote processes | Android Open Source Project. source.android.com. [2] Android Zygote Internals and Its Effects on Performance. proandroiddev.com. [3] Android Boot Process Part 2: From Zygote to SystemServer. linkedin.com. [4] What the Zygote!?. Android OS boot process explained. medium.com. [5] core/java/com/android/internal/os/ZygoteInit.java. android.googlesource.com. [6] Zygote preloading vs boot.art loading. stackoverflow.com. [7] Zygote runs as a daemon and accepts commands on a UNIX stream socket at /dev/socket/zygote. rtx.meta.security. [8] core/java/com/android/internal/os/ZygoteServer.java. android.googlesource.com.

---

# Componente 10: JNI Java Native Interface - Method signatures, reference types, local/global refs

Itens Técnicos Encontrados: 22

**Conceitos-Chave:** Assinaturas de Tipo JNI, jobject, jclass, jarray, jfieldID, jmethodID, jvalue, Referências Locais, Referências Globais, Tabela de Referências Locais, PushLocalFrame, PopLocalFrame, NewGlobalRef, DeleteGlobalRef, IsSameObject, UTF-8 Modificado

O **Java Native Interface (JNI)** é a interface de programação que permite que código Java em execução na Java Virtual Machine (JVM) ou no Android Runtime (ART) interaja com código nativo (C/C++). O foco técnico reside na representação de tipos de dados, assinaturas de métodos e no gerenciamento de referências de objetos.

## 1. Assinaturas de Tipo (Type Signatures)

O JNI utiliza a representação de assinaturas de tipo da Java Virtual Machine para identificar tipos primitivos, classes e métodos. Esta é uma estrutura de dados fundamental para a resolução de métodos e campos em tempo de execução.

<table>
<thead>
<tr>
<th>Assinatura de Tipo</th>
<th>Tipo Java</th>
<th>Tipo Nativo JNI</th>
<th>Descrição</th>
</tr>
</thead>
<tbody>
<tr>
<td>z</td>
<td>boolean</td>
<td>jboolean</td>
<td>Tipo primitivo de 8 bits sem sinal.</td>
</tr>
<tr>
<td>B</td>
<td>byte</td>
<td>jbyte</td>
<td>Tipo primitivo de 8 bits com sinal.</td>
</tr>
<tr>
<td>C</td>
<td>char</td>
<td>jchar</td>
<td>Tipo primitivo de 16 bits sem sinal.</td>
</tr>
<tr>
<td>S</td>
<td>short</td>
<td>jshort</td>
<td>Tipo primitivo de 16 bits com sinal.</td>
</tr>
<tr>
<td>I</td>
<td>int</td>
<td>jint</td>
<td>Tipo primitivo de 32 bits com sinal.</td>
</tr>
<tr>
<td>J</td>
<td>long</td>
<td>jlong</td>
<td>Tipo primitivo de 64 bits com sinal.</td>
</tr>
<tr>
<td>F</td>
<td>float</td>
<td>jfloat</td>
<td>Tipo primitivo de 32 bits.</td>
</tr>
<tr>
<td>D</td>
<td>double</td>
<td>jdouble</td>
<td>Tipo primitivo de 64 bits.</td>
</tr>
<tr>
<td>L fully-qualified-class ;</td>
<td>fully-qualified-class</td>
<td>jobject (ou subtipo)</td>
<td>Referência a uma classe.</td>
</tr>
<tr>
<td>[ type</td>
<td>type[]</td>
<td>jarray (ou subtipo)</td>
<td>Array de um tipo.</td>
</tr>
<tr>
<td>( arg-types ) ret-type</td>
<td>Tipo de método</td>
<td>N/A</td>
<td>Define os tipos de argumentos e o tipo de retorno.</td>
</tr>
</tbody>
</table>

**Exemplo de Assinatura de Método:** O método Java long f (int n, String s, int[] arr) possui a seguinte assinatura de tipo: (ILjava/lang/String;[I)J.

## 2. Estruturas de Dados de Referência e IDs

O JNI define tipos opacos para referências de objetos e identificadores de membros, garantindo a interoperabilidade entre a JVM/ART e o código nativo.

---


## Page 22

# 2.1. Tipos de Referência ( jobject Hierarchy )

Todos os tipos de referência JNI herdam de jobject. Em C, são definidos como o mesmo tipo ( typedef jobject jclass; ), mas em C++, são usadas classes dummy para impor a relação de subtipagem:

*   jobject : Tipo base para todas as referências de objetos Java.
*   jclass : Referência a objetos java.lang.Class.
*   jstring : Referência a objetos java.lang.String.
*   jarray : Tipo base para arrays, com subtipos como jobjectArray , jintArray , etc.
*   jthrowable : Referência a objetos java.lang.Throwable.

# 2.2. IDs de Campo e Método

Os identificadores de campo e método são ponteiros opacos em C, usados para acessar membros de classes sem a necessidade de pesquisa repetida por nome e assinatura.

*   jfieldID : Identificador opaco para campos de instância ou estáticos.
*   jmethodID : Identificador opaco para métodos de instância ou estáticos.

# 2.3. União de Argumentos ( jvalue )

A união jvalue é uma estrutura de dados usada para passar argumentos para métodos e construtores de forma unificada, especialmente em chamadas de API como CallMethodA .

```c
typedef union jvalue {
    jboolean z;
    jbyte b;
    jchar c;
    jshort s;
    jint i;
    jlong j;
    jfloat f;
    jdouble d;
    jobject l; /* para tipos de referência */
} jvalue;
```

# 3. Gerenciamento de Referências (Algoritmos e APIs)

O JNI define um protocolo rigoroso para o gerenciamento de referências para evitar vazamentos de memória e garantir que o Coletor de Lixo (GC) possa liberar objetos Java.

## 3.1. Referências Locais ( Local References )

*   **Estrutura de Dados:** No Android (AOSP/ART), as referências locais são gerenciadas por uma Tabela de Referências Locais (Local Reference Table), que é tipicamente implementada como uma tabela hash ou um array por thread.
*   **Protocolo:** Referências locais são válidas apenas durante a execução do método nativo que as criou. O ART/JVM as libera automaticamente quando o método nativo retorna.
*   **API de Liberação Explícita:** DeleteLocalRef( JNIEnv* env, jobject localRef ) : Usada para liberar referências locais manualmente em loops longos ou ao lidar com objetos grandes, prevenindo o estouro da Tabela de Referências Locais (que no Android pode ter um limite de 512 ou mais entradas).
*   **API de Frame Local:** PushLocalFrame( JNIEnv* env, jint capacity ) e PopLocalFrame( JNIEnv* env, jobject result ) : Permitem que o código nativo crie um novo frame de referência local, liberando todas as referências criadas dentro dele ao chamar PopLocalFrame , exceto o objeto de resultado retornado. Isso é um mecanismo de gerenciamento de pilha de referências.

---


## Page 23

# 3.2. Referências Globais (Global References)

*   **Protocolo:** Referências globais permanecem válidas até serem explicitamente liberadas. Elas impedem que o objeto Java referenciado seja coletado pelo GC.
*   **API de Criação:** `NewGlobalRef(JNIEnv* env, jobject localRef)`: Promove uma referência local (ou outra global) a uma referência global.
*   **API de Liberação:** `DeleteGlobalRef(JNIEnv* env, jobject globalRef)`: Libera a referência global, permitindo que o objeto seja coletado se não houver outras referências fortes.

# 3.3. Algoritmo de Comparação de Objetos

*   **API:** `IsSameObject(JNIEnv* env, jobject ref1, jobject ref2)`: Este é o único método correto para verificar se duas referências JNI (locais ou globais) apontam para o mesmo objeto Java.
*   **Motivação:** No código nativo, o valor de um jobject (o ponteiro) não é garantido ser constante ou único entre invocações, e referências diferentes (local e global) para o mesmo objeto terão valores de ponteiro diferentes. Portanto, a comparação direta com `==` é proibida.

# 4. Protocolo de Codificação de String

*   **Formato:** Modified UTF-8 (UTF-8 Modificado): O JNI usa este formato para representar strings.
*   **Algoritmo de Codificação:**
    *   Caracteres `\u0001` a `\u007F` são representados por 1 byte (`0xxxxxxx`).
    *   O caractere nulo (`\u0000`) e caracteres `\u0080` a `\u07FF` são representados por 2 bytes.
    *   Caracteres `\u0800` a `\uFFFF` são representados por 3 bytes.
    *   Caracteres suplementares (acima de U+FFFF) são codificados separadamente como dois surrogate code units UTF-16, resultando em 6 bytes (dois blocos de 3 bytes).
*   **Propriedade Chave:** O formato Modified UTF-8 garante que nunca haverá nulos embutidos (`\0`) dentro da string codificada, pois o caractere nulo é codificado em 2 bytes.

# 5. Arquitetura Específica do Android (AOSP/ART)

A implementação JNI no Android é fornecida pelo **Android Runtime (ART)**.

*   **Implementação de Referências Locais:** O ART implementa as referências locais usando uma `IndirectReferenceTable` por thread, que mapeia os valores opacos de jobject para os objetos reais na heap Java.
*   **Limite de Referências Locais:** O NDK adverte que a implementação é obrigada a reservar slots para apenas 16 referências locais, embora o limite real no ART seja tipicamente maior (ex: 512). A alocação excessiva sem liberação manual (`DeleteLocalRef` ou `PopLocalFrame`) leva ao erro “JNI local ref table overflow”.
*   **OOtimização de Chamadas Nativas:** O Android introduziu anotações como `@FastNative` e `@CriticalNative` para otimizar chamadas JNI, reduzindo a sobrecarga da transição entre o código Java e o código nativo, especialmente para métodos que não acessam objetos Java ou que usam apenas tipos primitivos.
*   **Ferramentas de Análise:** O Android Studio (Memory Profiler) fornece a **JNI Heap View** para inspecionar referências globais JNI criadas e liberadas, auxiliando na depuração de vazamentos de referência global.

---

# Componente 11: NDK Native Development Kit - CMake, ndk-build, ABI compatibility

**Itens Técnicos Encontrados:** 9

**Conceitos-Chave:** 16KB Page Alignment, ELF p_align, NDK ABI Forward Compatibility, Graph-based ABI Analysis, Strongly Connected Components (SCC), DWARF, STG, CMake ANDROID_ABI, ndk-build APP_ABI

---


## Page 24

# 1. Arquitetura e Protocolos de Compatibilidade ABI

A Compatibilidade ABI (Application Binary Interface) no Android NDK é regida pelo princípio de **compatibilidade forward** [1]. Isso significa que binários nativos (.so files) compilados com uma versão mais antiga do NDK devem continuar funcionando em novas versões do Android (como o Android 16). A compatibilidade reversa não é garantida.

*   **APIs e Estruturas de Dados:** O NDK define um conjunto de **Platform APIs** que, uma vez expostas, tornam-se parte da ABI estável e devem ser mantidas compatíveis em versões futuras [1].
*   **Análise de Equivalência ABI (Algoritmo e Estrutura de Dados):** Para garantir a estabilidade da ABI, o AOSP utiliza uma abordagem de análise ABI baseada em grafos [2].
    *   **Estrutura de Dados:** A ABI é modelada como um **grafo** (ABI graph). Estruturas como **DWARF** (Debugging With Arbitrary Record Formats) e **STG** (Symbol Table Graph) são fundamentais para a representação e análise do grafo [2].
    *   **Algoritmos:** O processo de análise de equivalência de grafos ABI utiliza **algoritmos de grafos** avançados, incluindo:
        *   **SCC (Strongly Connected Components) finder:** Utilizado em algoritmos recursivos cientes de ciclos para analisar a estrutura do grafo ABI [2].
        *   **Algoritmo de Equivalência de Grafos:** Fundamentado em princípios matemáticos sólidos para determinar a equivalência entre diferentes ABIs [2].

# 2. Alinhamento de Memória e Estruturas de Dados (Contexto Android 16)

A migração para o tamanho de página de 16KB (em vez do tradicional 4KB) no Android 16 (ou versões recentes) impõe uma restrição técnica de alinhamento para bibliotecas nativas não compactadas [3].

*   **Estrutura de Dados e Protocolo:** O alinhamento é um requisito para as bibliotecas compartilhadas (.so files) e é verificado no cabeçalho do formato de arquivo **ELF (Executable and Linkable Format)**.
*   **Algoritmo/Verificação:** A ferramenta **readelf** (parte do NDK) é usada para inspecionar o valor do campo p_align nos cabeçalhos do programa ELF.
    *   **Alinhamento de 16KB (Requerido):** p_align = 0x4000 (16384 bytes).
    *   **Alinhamento de 4KB (Antigo):** p_align = 0x1000 (4096 bytes).
*   **Build Systems (CMake e ndk-build):** Versões recentes do NDK (r28+) e do Android Gradle Plugin (AGP 8.3.0+) automatizam esse alinhamento para projetos que utilizam CMake ou ndk-build [3].

# 3. Mapeamento de Variáveis do Sistema de Build

Os sistemas de build **CMake** e **ndk-build** utilizam variáveis específicas para definir a ABI alvo, que se mapeiam para as arquiteturas suportadas pelo Android (ex: arm64-v8a , armeabi-v7a , x86_64 , x86 ):

<table>
<thead>
<tr>
<th>Sistema de Build</th>
<th>Variável/Opção</th>
<th>Função</th>
</tr>
</thead>
<tbody>
<tr>
<td>ndk-build</td>
<td>APP_ABI</td>
<td>Variável no Application.mk que especifica a lista de ABIs alvo.</td>
</tr>
<tr>
<td>CMake</td>
<td>ANDROID_ABI</td>
<td>Opção de toolchain que especifica a ABI alvo, correspondendo diretamente ao APP_ABI do ndk-build [4].</td>
</tr>
</tbody>
</table>

Referências: [1] Platform APIs. https://android.googlesource.com/platform/ndk/+/ndk-release-r19/docs/PlatformApis.md [2] Graph-based ABI analysis for fun and profit. https://lpc.events/event/17/contributions/1618/attachments/1190/2446/Graph-based%20ABI%20analysis%20for%20fun%20and%20profit.pdf [3] Android’s 16KB Page Size Migration: Everything You Need to Know November 2025. https://medium.com/@venkatraman230/androids-16kb-page-size-migration-everything-you-need-to-know-november-2025-b5c3ccbd2a7a [4] CMake toolchain file and other scripts for the Android NDK. https://github.com/taka-no-me/android-cmake

---


## Page 25

# Componente 12: System Server - Service Manager, Ciclo de Vida de Serviços e Watchdog

**Itens Técnicos Encontrados:** 11

**Conceitos-Chave:** Binder IPC, Service Manager, SystemServer.java, HandlerChecker, Watchdog, startBootstrapServices, startCoreServices, startOtherServices, Looper, ANR

# System Server - Service Manager, Ciclo de Vida de Serviços e Watchdog (AOSP Android 16)

O System Server é o processo central e monolítico do Android (executado como `system_server`) que hospeda a maioria dos serviços essenciais do sistema. Sua arquitetura é baseada em um único processo Java que utiliza o mecanismo de Inter-Process Communication (IPC) **Binder** para expor seus serviços a outros processos de aplicação e nativos.

## 1. Arquitetura e Protocolo do Service Manager

O Service Manager (também conhecido como *Context Manager* do Binder) é um componente fundamental da arquitetura IPC do Android.

### Protocolo: Binder IPC

O Service Manager atua como o ponto de registro central para todos os serviços baseados em Binder.

*   **Estrutura de Dados/Protocolo:** O Service Manager é o único processo que possui a permissão de registrar serviços no *driver* do Binder (`/dev/binder`). Ele mantém um mapeamento de *strings* de nomes de serviços para *handles* de Binder (referências a objetos remotos).
*   **APIs Principais:**
    *   `addService(String name, IBinder service)`: Usada pelo System Server e outros processos privilegiados para registrar um novo serviço.
    *   `getService(String name)`: Usada por clientes (aplicações, outros serviços) para obter o *handle* do Binder para um serviço registrado.
*   **Arquitetura:** O Service Manager é implementado como um processo nativo separado (`/system/bin/servicemanager`) que é iniciado pelo *init* no *boot* do sistema. Ele é o primeiro serviço a ser registrado no *driver* Binder, recebendo o *handle* `0`.

## 2. Ciclo de Vida dos Serviços do Sistema (System Server)

O ciclo de vida dos serviços é gerenciado pela classe `SystemServer.java`, que executa o algoritmo de inicialização em fases estritas para garantir a ordem correta das dependências.

### Algoritmo de Inicialização (Método run() em SystemServer.java)

A inicialização dos serviços segue uma sequência estrita de três fases, executadas na *thread* principal do System Server (*Looper*):

1.  `startBootstrapServices()` : Inicializa os serviços mais críticos e de baixo nível, que não dependem de outros serviços.
    *   Exemplos: Installer , ActivityManagerService (AMS), PowerManagerService , PackageManagerService (PMS).
    *   **Estrutura de Dados:** Após a inicialização, o AMS é o primeiro a chamar `ActivityManagerService.setSystemProcess()`, estabelecendo o processo `system_server` como o processo do sistema.

---


## Page 26

2. `startCoreServices()`: Inicializa serviços que dependem dos serviços bootstrap e são essenciais para a funcionalidade básica do sistema.
    * Exemplos: BatteryService, UsageStatsService.

3. `startOtherServices()`: Inicializa a maioria dos serviços restantes, que podem ter dependências mais complexas.
    * Exemplos: WindowManagerService, InputManagerService, MediaRouterService.

* **Arquitetura:** Todos os serviços são executados na thread principal do System Server ou em threads auxiliares dedicadas (como DisplayThread, IoThread, FgThread), mas são gerenciados e registrados via ServiceManager.addService().

# 3. Mecanismo Watchdog

O **Watchdog** é um mecanismo de monitoramento de threads dentro do System Server, projetado para detectar e recuperar-se de deadlocks ou hangs prolongados na thread principal ou em threads críticas.

## Algoritmo de Monitoramento

O Watchdog opera em um loop de monitoramento periódico:

1. **Estrutura de Dados:** O Watchdog mantém uma lista de threads críticas a serem monitoradas, armazenadas em uma ArrayList<HandlerCheckerAndTimeout>. Cada HandlerChecker na lista é associado a um Looper de uma thread específica (ex: thread principal, thread de display, thread de animation).
2. **Protocolo de Ping:** A thread do Watchdog envia uma mensagem vazia (um “ping”) para o Handler de cada thread monitorada.
3. **Timeout:** O tempo limite padrão (DEFAULT_TIMEOUT) é de **60 segundos** (60.000 ms). Se a mensagem não for processada e retornar ao Watchdog dentro desse período, a thread é considerada hung (travada).
4. **Estados:** O HandlerChecker utiliza estados para rastrear o progresso: COMPLETED (0), WAITING (1), WAITED_UNTIL_PRE_WATCHDOG (2), e OVERDUE (3).
5. **Ação de Falha:** Se um timeout for detectado (OVERDUE), o Watchdog:
    * Coleta stack traces de todas as threads Java e de processos nativos de interesse (definidos em NATIVE_STACKS_OF_INTEREST).
    * Gera um relatório de erro (ANR - Application Not Responding) no Dropbox.
    * Protocolo de Reinicialização: Chama o IPowerManager.reboot() para forçar a reinicialização do sistema, garantindo a recuperação do deadlock.

## Monitoramento de Binder

* **Estrutura de Dados/Protocolo:** O BinderThreadMonitor é um monitor especial que utiliza a API Binder.blockUntilThreadAvailable(). Este método bloqueia até que uma thread do pool de threads Binder esteja disponível para processar chamadas IPC. Se o pool estiver exausto ou travado, o monitor falha, contribuindo para o timeout do Watchdog.

# Componente 13: Activity Manager - Activity lifecycle, task affinity, launch modes, back stack

Itens Técnicos Encontrados: 11

Conceitos-Chave: ActivityRecord, TaskRecord, Back Stack LIFO, Binder IPC, IActivityManager, Launch Modes, Task Affinity, updateOomAdjLocked

O gerenciamento de atividades no Android é centralizado no **ActivityManagerService (AMS)**, um serviço de sistema executado no processo system_server. O AMS é responsável por manter o estado do sistema, gerenciar o ciclo de vida das atividades, e controlar a alocação de recursos, utilizando um conjunto de estruturas de dados e protocolos de comunicação bem definidos [4].

---


## Page 27

# Estruturas de Dados Centrais

O AMS modela a hierarquia de atividades e tarefas usando duas estruturas de dados principais, que representam a arquitetura da Back Stack:

1.  **TaskRecord**: Representa uma Task (Tarefa), que é uma coleção de atividades que o usuário interage para realizar uma tarefa.

    *   **Estrutura:** É essencialmente um contêiner que mantém uma lista de instâncias de ActivityRecord ( final ArrayList<ActivityRecord> mActivities ) [2].
    *   **Campos Chave:**
        *   final int taskId: Identificador único da tarefa.
        *   final String affinity: O nome de afinidade da tarefa, usado para reparenting e para determinar onde uma nova atividade deve ser lançada.
        *   Intent intent : O Intent original que iniciou a tarefa.
        *   int numActivities : Número atual de atividades na tarefa.
        *   boolean rootWasReset : Indica se o Intent na raiz da tarefa tinha a flag FLAG_ACTIVITY_RESET_TASK_IF_NEEDED [2].

2.  **ActivityRecord**: Representa uma instância específica de uma Activity no sistema.

    *   **Estrutura:** Contém todos os metadados e o estado de execução de uma atividade.
    *   **Campos Chave:**
        *   TaskRecord task : Referência à tarefa à qual esta atividade pertence.
        *   final IApplicationToken.Stub appToken : O token Binder que identifica a atividade no Window Manager.
        *   ActivityState state : O estado atual do ciclo de vida da atividade (e.g., INITIALIZING , RESUMED , PAUSED , STOPPED , FINISHING ).
        *   long startTime , long pauseTime : Timestamps usados para rastrear o ciclo de vida e o desempenho.
        *   Bundle icicle : O último estado salvo da atividade ( onSaveInstanceState ) [3].

# Algoritmo da Back Stack e Ciclo de Vida

A Back Stack opera sob o princípio LIFO (Last-In, First-Out). Quando uma nova atividade é iniciada, ela é empilhada ( pushed ) no topo da pilha. Quando o usuário pressiona o botão “Voltar” , a atividade atual é desempilhada ( popped ) e destruída, e a atividade anterior é retomada [1].

# Mecanismos de Lançamento (Launch Modes)

Os Launch Modes definem o algoritmo de como uma nova instância de atividade é associada a uma tarefa, controlando a criação e reutilização de instâncias [1]:

---


## Page 28

<table>
  <thead>
    <tr>
      <th>Modo de Lançamento</th>
      <th>Algoritmo de Ação</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>standard</td>
      <td>Cria uma nova instância da atividade e a empilha na tarefa do chamador. Múltiplas instâncias são permitidas.</td>
    </tr>
    <tr>
      <td>singleTop</td>
      <td>Se uma instância já existir no topo da pilha, o sistema a reutiliza, chamando onNewIntent(). Caso contrário, cria uma nova instância.</td>
    </tr>
    <tr>
      <td>singleTask</td>
      <td>O sistema procura uma tarefa existente com a mesma afinidade. Se encontrar, traz a tarefa para o primeiro plano e destrói todas as atividades acima da instância existente, chamando onNewIntent() na instância reutilizada. Se não encontrar, cria uma nova tarefa e a atividade se torna a raiz.</td>
    </tr>
    <tr>
      <td>singleInstance</td>
      <td>Comportamento idêntico a singleTask, mas a atividade é sempre o único membro de sua tarefa. Qualquer atividade subsequente iniciada por ela é aberta em uma tarefa separada.</td>
    </tr>
    <tr>
      <td>singleInstancePerTask</td>
      <td>A atividade só pode ser a atividade raiz de uma tarefa. Pode haver múltiplas instâncias em diferentes tarefas, mas apenas uma por tarefa.</td>
    </tr>
  </tbody>
</table>

## Protocolo de Comunicação e Gerenciamento de Processos

1. **Protocolo Binder IPC**: O protocolo de comunicação interprocessual (IPC) de alto desempenho do Android é o **Binder**. A comunicação entre os aplicativos (clientes) e o AMS (servidor) é realizada através da interface **IActivityManager**, definida em AIDL (Android Interface Definition Language). O Binder permite que métodos em objetos remotos (como o AMS) sejam chamados como se fossem locais, utilizando um mecanismo de **transação** e o objeto **Parcel** para serialização/desserialização de dados [5].

2. **Algoritmo de Ajuste OOM**: O AMS implementa o método **updateOomAdjLocked()** para gerenciar a memória e a prioridade dos processos. Este algoritmo calcula e atribui um **OOM (Out-Of-Memory) adjustment score** a cada processo em execução. Processos com pontuações mais baixas têm maior prioridade e são menos propensos a serem eliminados pelo *Low Memory Killer* do kernel Linux. O algoritmo considera o estado das atividades (**ActivityRecord.state**), a visibilidade e a importância do processo para o usuário (e.g., processo em primeiro plano, serviço em execução) para determinar a pontuação [4] [6].

---

## Referências

[1] Tasks and the back stack | App architecture - Android Developers. [2] services/java/com/android/server/am/TaskRecord.java - platform/frameworks/base - Git at Google. [3] services/core/java/com/android/server/am/ActivityRecord.java - platform/frameworks/base - Git at Google. [4] Mastering ActivityManagerService: Unlocking the Hidden ... - LinkedIn. [5] Use binder IPC | Android Open Source Project. [6] Personalized optimization for android smartphones - ACM Digital Library.

---

## Componente 14: Package Manager - APK parsing, signature verification, permissions, dexopt

### Itens Técnicos Encontrados: 16

### Conceitos-Chave:
APK Signature Scheme v3.1, Rotação de Chaves, SDK Version Targeting, PackageParser, PackageManagerService, ART Service, dexopt, dex2oat, Zygote Sandboxing, Permissões de Assinatura

### Conteúdo Técnico: Package Manager (Parsing, Assinatura, Permissões, Dexopt)

O gerenciamento de pacotes no Android, centrado no **PackageManagerService** (PMS), é um componente crítico do sistema que lida com a instalação, desinstalação e consulta de aplicações. O processo envolve uma arquitetura complexa, estruturas de dados específicas e protocolos criptográficos para garantir a integridade e a segurança do sistema.

### 1. Arquitetura e Parsing de APK

O processo de instalação de um APK é iniciado pelo PMS, que delega a tarefa de parsing ao **PackageParser**.

---


## Page 29

# Estruturas de Dados e Algoritmos de Parsing

O código-fonte principal para o parsing de pacotes reside em frameworks/base/core/java/android/content/pm/PackageParser.java no AOSP.

*   **Estrutura de Dados Principal:** A classe PackageParser.Package é a estrutura de dados central que armazena todos os metadados extraídos do APK, incluindo o AndroidManifest.xml, recursos, certificados de assinatura e informações de código.
*   **Processo de Parsing:** O método parsePackage (ou suas variantes) é o algoritmo de parsing que lê o arquivo APK (que é um arquivo ZIP) e extrai o AndroidManifest.xml (um arquivo binário XML) e outros componentes. O parsing do manifesto é um processo de desserialização binária que popula a estrutura PackageParser.Package.
*   **Protocolo de Comunicação:** O PMS se comunica com o daemon de baixo nível installd (localizado em cmds/installld no AOSP) via Binder IPC para operações de sistema de arquivos, como criação de diretórios de dados e movimentação de arquivos.

## 2. Verificação de Assinatura (Signature Verification)

A verificação de assinatura é um protocolo de segurança essencial que garante a autenticidade e a integridade do APK.

### Protocolos de Assinatura

O Android 16 (visando SDK 33+ e superior) utiliza primariamente o **APK Signature Scheme v3.1**, que é uma evolução do v3.

<table>
<thead>
<tr>
<th>Esquema</th>
<th>Versão Android</th>
<th>Localização da Assinatura</th>
<th>Algoritmos Criptográficos</th>
<th>Estrutura de Dados Chave</th>
</tr>
</thead>
<tbody>
<tr>
<td>v3.1</td>
<td>13+ (e Android 16)</td>
<td>APK Signing Block (ID novo)</td>
<td>RSASSA-PKCS1-v1_5, SHA-256/512 (para digest)</td>
<td>SDK Version Targeting, Proof-of-Rotation (PoR)</td>
</tr>
<tr>
<td>v3</td>
<td>9+</td>
<td>APK Signing Block (ID: 0xf05368c0 )</td>
<td>RSASSA-PKCS1-v1_5, ECDSA, DSA</td>
<td>Proof-of-Rotation (PoR)</td>
</tr>
<tr>
<td>v2</td>
<td>7+</td>
<td>APK Signing Block</td>
<td>RSASSA-PKCS1-v1_5, ECDSA, DSA</td>
<td>Merkle Tree (para integridade)</td>
</tr>
<tr>
<td>v1</td>
<td>Todas</td>
<td>META-INF/</td>
<td>Assinatura de arquivos JAR</td>
<td>Arquivos MANIFEST.MF, CERT.SF, CERT.RSA</td>
</tr>
</tbody>
</table>

### Mecanismo de Rotação de Chaves (Key Rotation)

O v3.1 introduz o conceito de **SDK Version Targeting** para a rotação de chaves.

*   **Estrutura PoR:** O **Proof-of-Rotation (PoR)** é uma estrutura de dados dentro do bloco de assinatura que armazena a **linhagem de assinatura** (lineage) do aplicativo. Cada entrada na linhagem contém o certificado de assinatura anterior e um atestado de que o novo certificado pode assinar atualizações para o certificado anterior.
*   **Comportamento v3.1:** O v3.1 usa um **novo Block ID** no APK Signing Block. Dispositivos Android 13+ (incluindo Android 16) reconhecem este ID e usam o *rotated signer* (assinante rotacionado) contido nele. Dispositivos mais antigos ignoram o bloco v3.1 e usam o *original signer* (assinante original) no bloco v3, garantindo compatibilidade.
*   **Algoritmo de Verificação:** A biblioteca apksig (AOSP) é responsável por gerar e verificar essas assinaturas. O processo de verificação envolve a computação de um digest (usando algoritmos de hash como SHA-256 ou SHA-512) de partes específicas do APK e a validação da assinatura criptográfica (usando RSASSA-PKCS1-v1_5 ou outros) contra esse digest.

## 3. Gerenciamento de Permissões

O PackageManager é o árbitro central do modelo de permissões do Android.

*   **Tipos de Permissão:**
    *   Normal: Concedidas automaticamente na instalação.
    *   Dangerous: Requerem runtime permission check e diálogo de consentimento do usuário.

---


## Page 30

*   **Signature:** Concedidas apenas se o aplicativo solicitante for assinado com a mesma chave do aplicativo que define a permissão (ou a chave da plataforma). O PMS valida essas permissões durante o parsing e a instalação.
*   **Mecanismo de Sandboxing:** O sistema impõe o isolamento de aplicativos usando o **Zygote Sandboxing**. Cada aplicativo é executado em seu próprio processo Linux com um **UID (User ID)** e **GID (Group ID)** exclusivos, limitando o acesso aos recursos do sistema de arquivos e IPC. O PMS é responsável por mapear as permissões declaradas no manifesto para os GIDs do Linux.

## 4. Dexopt e ART (Android Runtime)

**Dexopt** (otimização de código Dalvik Executable) é o processo de compilação Ahead-Of-Time (AOT) ou Just-In-Time (JIT) de código de aplicativo para otimizar o desempenho.

### Mudanças no Android 16

No Android 16, o processo de dexopt foi otimizado para reduzir o tempo de inatividade do aplicativo durante as atualizações.

*   **ART Service:** A partir do Android 14, a implementação de dexopt no PackageManager foi substituída pelo **ART Service**. O ART Service é um componente do sistema que gerencia a compilação e otimização de código.
*   **Otimização de Instalação:** O Android 16 move a execução de dexopt ou **dex2oat** (o compilador AOT do ART) para uma fase anterior do processo de instalação. Isso permite que a otimização ocorra enquanto o aplicativo ainda está sendo baixado ou em uma fase onde o aplicativo não está em uso, minimizando o tempo em que o aplicativo fica “unrunnable” (inutilizável) após a atualização.
*   **Dexpreopt:** A otimização de código para bibliotecas e aplicativos pré-instalados é realizada durante a construção da imagem do sistema, em um processo chamado **dexpreopt**.

---

### Elementos Técnicos Encontrados:

1.  **Protocolos de Assinatura:** APK Signature Scheme v1, v2, v3, v3.1, v4.
2.  **Estruturas de Dados:** PackageParser .Package , APK Signing Block, v3.1 Block ID, Proof-of-Rotation (PoR) structure, SigningInfo.
3.  **Algoritmos Criptográficos:** RSASSA-PKCS1-v1_5, SHA-256, SHA-512.
4.  **Componentes de Arquitetura/Processos:** PackageManagerService (PMS), PackageParser, installd daemon, ART Service, dex2oat compiler, Zygote Sandboxing, Binder IPC.
5.  **Conceitos:** SDK Version Targeting, Key Rotation Lineage, Dexpreopt.

---

### Componente 15: Window Manager - Display metrics, window tokens, input dispatch, animations

**Itens Técnicos Encontrados:** 14

**Conceitos-Chave:** InputChannel, BufferQueue, SurfaceControl, Window Token, InputDispatcher, VSync, WindowMetrics, Predictive Back Gesture

---

### Conteúdo Técnico: Window Manager no Android 16 (AOSP)

O Window Manager (WM) no Android, implementado principalmente pelo **WindowManagerService** no **system_server**, é o componente central responsável por gerenciar o ciclo de vida, a aparência e a interação de todas as janelas na tela. Sua arquitetura é baseada em uma comunicação interprocessual (IPC) complexa e estruturas de dados bem definidas para coordenar com outros serviços críticos, como o **InputFlinger** e o **SurfaceFlinger**.

---


## Page 31

# 1. Arquitetura e Protocolo de Input Dispatch

O subsistema de *input dispatch* é responsável por rotear eventos de entrada (toque, teclado, etc.) do hardware para a janela de aplicação correta.

## Estruturas de Dados e Protocolos

<table>
  <thead>
    <tr>
      <th>Estrutura/Protocolo</th>
      <th>Tipo</th>
      <th>Função Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>InputChannel</td>
      <td>Estrutura de Dados / IPC</td>
      <td>Um canal de comunicação baseado em socketpair (socket Unix) que liga o InputDispatcher (no system_server) ao InputEventReceiver (no processo da aplicação). É a via de transporte para eventos de input.</td>
    </tr>
    <tr>
      <td>socketpair</td>
      <td>Protocolo IPC</td>
      <td>Mecanismo de comunicação de baixo nível (Unix domain socket) que serve como o canal de transporte subjacente para o InputChannel.</td>
    </tr>
    <tr>
      <td>Window Token</td>
      <td>Estrutura de Dados (Binder)</td>
      <td>Objeto Binder que representa a identidade e o ciclo de vida de uma janela ou um grupo de janelas. Usado pelo WindowManagerService para rastrear e gerenciar a hierarquia e o foco das janelas.</td>
    </tr>
  </tbody>
</table>

## Algoritmo de Roteamento ( InputDispatcher )

O InputDispatcher é o algoritmo central de roteamento de eventos. Ele utiliza um Looper para escutar os descritores de arquivo dos InputChannels.

1.  **Fluxo de Eventos:** O evento de input segue o caminho: Hardware → Driver → /dev/input/eventXX → EventHub → InputReader → InputDispatcher → InputChannel (IPC) → InputEventReceiver (App).
2.  **Gerenciamento de Ciclo de Vida:** O InputDispatcher envia eventos via InputChannel::sendMessage e espera por um sinal FINISHED do lado da aplicação para confirmar o processamento do evento, gerenciando o ciclo de vida do evento de input.
3.  **Timeout:** O WindowManagerService define um timeout de input dispatching (e.g., DEFAULT_INPUT_DISPATCHING_TIMEOUT_NANOS) para detectar e relatar Application Not Responding (ANR) se uma janela não processar o evento a tempo.

# 2. Gráficos, Display Metrics e Animações

O Window Manager coordena com o SurfaceFlinger para a composição gráfica e gerencia as métricas de exibição.

## Protocolo de Comunicação Gráfica (WM - SurfaceFlinger)

<table>
  <thead>
    <tr>
      <th>Estrutura/Protocolo</th>
      <th>Tipo</th>
      <th>Função Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BufferQueue</td>
      <td>Protocolo IPC (Binder)</td>
      <td>Permite a transferência de buffers gráficos (conteúdo da janela) do aplicativo (produtor) para o SurfaceFlinger (consumidor).</td>
    </tr>
    <tr>
      <td>SurfaceControl</td>
      <td>Estrutura de Dados</td>
      <td>Contém os metadados da camada (z-order, transformações, opacidade, display frame) que o WindowManager usa para manipular a aparência da janela.</td>
    </tr>
    <tr>
      <td>ASurfaceControl</td>
      <td>API / Estrutura de Dados</td>
      <td>Combina Surface e SurfaceControl em um pacote de transação para o SurfaceFlinger, permitindo atualizações atômicas e mais eficientes (a partir do Android 10).</td>
    </tr>
    <tr>
      <td>VSync</td>
      <td>Protocolo de Sincronização</td>
      <td>Sinal de tempo enviado pelo display para o SurfaceFlinger, indicando o momento seguro para aceitar novos buffers e iniciar a composição, minimizando o tearing.</td>
    </tr>
  </tbody>
</table>

---


## Page 32

# Algoritmos e APIs de Métricas e Animação

1.  **WindowMetrics**: Estrutura de dados que fornece as métricas da janela atual, incluindo a área de exibição disponível para o aplicativo, crucial para layouts adaptativos.
2.  **DisplayMetrics**: Estrutura de dados que armazena informações gerais sobre o display (densidade, largura/altura em pixels), usadas para cálculos de layout e recursos.
3.  **Window Size Classes**: Algoritmo de categorização (e.g., Compact, Medium, Expanded) que usa a largura e altura disponíveis da janela para guiar o design de layouts responsivos.
4.  **NATIVE_WINDOW_TRANSFORM_HINT**: Algoritmo/Hint de Otimização. Uma dica em ANativeWindow que representa a transformação mais provável (e.g., rotação) que o SurfaceFlinger aplicará. Drivers GL podem usar isso para pré-transformar o buffer, economizando energia.
5.  **Predictive Back Gesture (Android 16)**: Algoritmo de Animação. Usa a API OnBackPressedCallback para fornecer uma animação de retorno preditiva (e.g., back-to-home, cross-activity), onde o sistema operacional orquestra a animação antes da conclusão do gesto, melhorando a fluidez da experiência do usuário.

# Resumo da Arquitetura

O WindowManagerService atua como o ponto de controle central, gerenciando a hierarquia de janelas, calculando as regiões de input e as métricas de exibição (WindowMetrics), e fornecendo metadados (SurfaceControl) e buffers (BufferQueue) para o SurfaceFlinger para composição final. O InputDispatcher opera em paralelo, usando canais IPC (InputChannel via socketpair) para entregar eventos de input diretamente às janelas de aplicação corretas.

# Quantificação Técnica

O conteúdo técnico extraído inclui 14 itens principais, categorizados da seguinte forma:

<table>
<thead>
<tr>
<th>Categoria</th>
<th>Itens Técnicos</th>
</tr>
</thead>
<tbody>
<tr>
<td>Algoritmos/Mecanismos</td>
<td>5 (Input Dispatcher, VSync, NATIVE_WINDOW_TRANSFORM_HINT, Window Size Classes, Predictive Back Gesture)</td>
</tr>
<tr>
<td>Estruturas de Dados</td>
<td>6 (InputChannel, Window Token, SurfaceControl, ASurfaceControl, WindowMetrics, DisplayMetrics)</td>
</tr>
<tr>
<td>Protocolos/APIs</td>
<td>3 (socketpair, BufferQueue, OnBackPressedCallback)</td>
</tr>
<tr>
<td>Total Aproximado</td>
<td>14</td>
</tr>
</tbody>
</table>

# Componente 16: Content Providers

**Itens Técnicos Encontrados:** 13

**Conceitos-Chave:** URI Matching, Trie, Protocolo IPC Binder, IContentProvider, ContentProviderNative, ContentProviderProxy, Parcel, BulkCursorDescriptor, CRUD, Batch Operations, ContentObserver, Padrão Observer

# Content Providers (Android 16 - AOSP)

O Content Provider é um componente fundamental da arquitetura Android para gerenciar o acesso a um conjunto estruturado de dados, atuando como uma camada de abstração e um mecanismo de comunicação interprocessual (IPC) seguro.

---


## Page 33

# 1. URI Matching (UriMatcher)

O mecanismo de correspondência de URI é essencial para rotear as requisições de dados para as funções apropriadas do Content Provider.

## Estrutura de Dados e Algoritmo

A classe UriMatcher implementa um algoritmo de correspondência de padrões baseado em uma estrutura de dados em árvore (Trie).

*   **Estrutura de Dados:** A correspondência é realizada através de uma lista aninhada de objetos UriMatcher (internamente referidos como node s), onde cada nó representa um segmento da URI. A lista de filhos (mChildren) de um nó armazena os próximos segmentos possíveis.
*   **Algoritmo de Correspondência** (match(Uri uri)):
    1.  A URI de entrada é segmentada em autoridade e segmentos de caminho (uri.getAuthority() e uri.getPathSegments() ).
    2.  O algoritmo itera sobre cada segmento (começando pela autoridade).
    3.  Para cada segmento, ele percorre a lista de filhos (mChildren) do nó atual.
    4.  A correspondência é feita com base no tipo de segmento (mWhich):
        *   EXACT : Corresponde a uma string literal (n.mText.equals(u)).
        *   NUMBER : Corresponde a um segmento que consiste apenas em dígitos (algoritmo de validação de string numérica).
        *   TEXT : Corresponde a qualquer string (curinga * ).
    5.  Se um nó correspondente for encontrado, ele se torna o novo nó atual (node = n), e o processo continua para o próximo segmento.
    6.  Se nenhum nó correspondente for encontrado para um segmento, a correspondência falha, retornando NO_MATCH (-1).
    7.  O valor de retorno é o código inteiro (mCode ) associado ao nó final correspondente.

# 2. Protocolo de Comunicação Interprocessual (IPC)

A comunicação entre o ContentResolver (cliente) e o ContentProvider (servidor) é realizada através do mecanismo Binder do Android.

## Arquitetura

*   IContentProvider : Interface AIDL (Android Interface Definition Language) que define os métodos remotos (query, insert, update, delete, bulkInsert, applyBatch, etc.).
*   ContentProviderNative : Implementação do lado do servidor (Content Provider) que estende Binder e implementa IContentProvider . Ele recebe as chamadas do Binder e as despacha para os métodos concretos do ContentProvider .
*   ContentProviderProxy : Implementação do lado do cliente (ContentResolver ) que implementa IContentProvider . Ele empacota os argumentos em um objeto Parcel e usa o método transact( ) do Binder para enviar a chamada ao processo remoto.

## Estruturas de Dados e Protocolo

*   Parcel : Estrutura de dados serializável usada para empacotar (marshalling) e desempacotar (unmarshalling) os dados e argumentos das chamadas de método através do Binder.
*   BulkCursorToCursorAdaptor : Estrutura de dados usada para transferir grandes volumes de dados (como resultados de query ) de forma eficiente. O ContentProviderProxy.query() usa essa classe para receber um BulkCursorDescriptor (que contém um IBinder para o cursor remoto) e adaptá-lo para um Cursor local.

---


## Page 34

* Transação Binder: As operações CRUD são mapeadas para códigos de transação ( QUERY_TRANSACTION, INSERT_TRANSACTION, etc.) que são passados ao método `transact()` do Binder.

# 3. Operações CRUD e Batch

As operações de manipulação de dados são definidas pelos métodos abstratos da classe ContentProvider:

* CRUD (Create, Read, Update, Delete):
    * insert(Uri uri, ContentValues values)
    * query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder)
    * update(Uri uri, ContentValues values, String selection, String[] selectionArgs)
    * delete(Uri uri, String selection, String[] selectionArgs)

* Batch Operations ( applyBatch ):
    * applyBatch(ArrayList<ContentProviderOperation> operations): Permite a execução de múltiplas operações (insert, update, delete) em uma única transação IPC.
    * Estrutura de Dados: A classe ContentProviderOperation encapsula uma única operação de dados, incluindo a URI, o tipo de operação (e.g., TYPE_INSERT ), e os valores ( contentValues ). A lista de operações é serializada via Parcel e enviada ao Content Provider, que as executa atomicamente (se suportado).

# 4. Mecanismo de Observers (ContentObserver)

O mecanismo de notificação de alteração de dados segue o padrão **Observer**.

## Estrutura e Protocolo

* ContentObserver : Classe abstrata que deve ser estendida para receber notificações de alteração de conteúdo. Ele é registrado no ContentResolver através do método `registerContentObserver(Uri uri, boolean notifyForDescendants, ContentObserver observer)`.
* ContentObservable : Estrutura de dados interna (semelhante a um ArrayList de ContentObserver s) que gerencia a lista de observadores registrados para uma URI.
* Notificação ( ContentResolver.notifyChange() ):
    1. O ContentProvider chama getContext().getContentResolver().notifyChange(uri, observer) após uma alteração de dados (insert, update, delete).
    2. O ContentResolver (que está no processo do cliente) usa o Binder para notificar o ContentService (no processo do sistema).
    3. O ContentService mantém um registro global de todos os ContentObserver s e suas URLs.
    4. O ContentService despacha a notificação de volta para os ContentResolver s registrados nos processos dos aplicativos afetados.
    5. O ContentResolver localiza o ContentObserver e chama o método dispatchChange().
* Algoritmo de Despacho ( dispatchChange() ): Se um Handler foi fornecido ao construtor do ContentObserver , a chamada para onChange() é postada na fila de mensagens do Handler (execução assíncrona na thread principal). Caso contrário, onChange() é invocado imediatamente na thread de notificação.

# 5. APIs e Classes Chave

* android.content.ContentProvider : Classe base para o provedor de dados.
* android.content.ContentResolver : Classe cliente para interagir com o provedor.
* android.net.Uri : Estrutura de dados para identificar o recurso.

---


## Page 35

*   `android.content.UriMatcher` : Algoritmo de roteamento de URI.
*   `android.content.ContentValues` : Estrutura de dados para pares chave-valor (coluna-valor) em operações de inserção/atualização.
*   `android.database.Cursor` : Estrutura de dados para resultados de consulta (linhas e colunas).
*   `android.database.ContentObserver` : Classe base para o padrão Observer.
*   `android.content.ContentProviderOperation` : Estrutura de dados para operações em lote.
*   `android.os.Binder / android.os.IBinder / android.os.Parcel` : Classes e interfaces do protocolo IPC.

---

# Componente 17: Broadcast Receivers - Intent filters, ordered broadcasts, sticky broadcasts

**Itens Técnicos Encontrados:** 13

**Conceitos-Chave:** Intent Filter Matching Algorithm, Ordered Broadcast Protocol, BroadcastQueue, android:priority, Sticky Broadcast Deprecation, Intent Data Matching

## Conteúdo Técnico: Broadcast Receivers no Android 16 (AOSP)

O subsistema de Broadcast Receivers no Android 16 é um componente fundamental da arquitetura de comunicação inter-componentes, operando sob o padrão de design **Publish-Subscribe** [1]. A gestão centralizada e a entrega de broadcasts são realizadas pelo **ActivityManagerService (AMS)**, que utiliza a estrutura de dados **BroadcastQueue** no processo do servidor do sistema para gerenciar a fila de broadcasts pendentes [2].

### 1. Algoritmo de Correspondência de Intent Filter

O mecanismo de **Intent Filter** é o algoritmo central para determinar quais BroadcastReceiver devem receber um determinado Intent. Para que um filtro corresponda a um Intent, três condições devem ser satisfeitas simultaneamente: Ação, Categoria e Dados [3].

#### 1.1. Estrutura de Dados Interna

A classe IntentFilter armazena as ações, categorias, tipos de dados (MIME), esquemas, autoridades e caminhos internamente, tipicamente utilizando estruturas como ArrayList ou ArraySet para permitir múltiplos valores para cada atributo [3].

#### 1.2. Regras de Correspondência (Método match() )

O algoritmo de correspondência é executado sequencialmente, com cada componente do Intent sendo validado contra o filtro:

---


## Page 36

<table>
  <thead>
    <tr>
      <th>Componente</th>
      <th>Regra de Correspondência</th>
      <th>Observações Técnicas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ação</td>
      <td>Corresponde se qualquer valor de ação no filtro for igual à ação do Intent . Se o filtro não especificar ações, só corresponde a Intents sem ação.</td>
      <td>O método matchAction() verifica a igualdade da string.</td>
    </tr>
    <tr>
      <td>Categoria</td>
      <td>Corresponde se todas as categorias presentes no Intent estiverem presentes no filtro.</td>
      <td>O método matchCategories() exige que o conjunto de categorias do Intent seja um subconjunto do filtro.</td>
    </tr>
    <tr>
      <td>Dados (Data)</td>
      <td>Corresponde se o Tipo MIME e a URI de Dados (Esquema + Autoridade + Caminho) corresponderem.</td>
      <td>A correspondência de dados é a mais complexa e é dividida em sub-regras.</td>
    </tr>
    <tr>
      <td>Tipo MIME</td>
      <td>Corresponde se qualquer tipo MIME no filtro corresponder ao tipo MIME do Intent .</td>
      <td>A correspondência é case-sensitive. Suporta wildcard (*) para o sub-tipo (e.g., audio/*) [3].</td>
    </tr>
    <tr>
      <td>Esquema</td>
      <td>Corresponde se qualquer esquema no filtro for igual ao esquema da URI de Dados do Intent .</td>
      <td>A correspondência é case-sensitive [3].</td>
    </tr>
    <tr>
      <td>Autoridade</td>
      <td>Corresponde se qualquer autoridade no filtro corresponder à autoridade da URI de Dados, e um esquema tiver sido correspondido.</td>
      <td>A autoridade é composta por host e porta (host:port). A correspondência é case-sensitive [3].</td>
    </tr>
    <tr>
      <td>Caminho</td>
      <td>Corresponde se qualquer caminho no filtro corresponder ao caminho da URI de Dados, e tanto um esquema quanto uma autoridade tiverem sido correspondidos.</td>
      <td>Suporta correspondência literal, prefixo e glob (padrão) [3].</td>
    </tr>
  </tbody>
</table>

## 2. Protocolo de Ordered Broadcasts

Ordered Broadcasts são um protocolo de comunicação onde os Intents são entregues a um receptor por vez, permitindo que cada receptor influencie o fluxo da entrega [4].

### 2.1. Mecanismo de Prioridade e Entrega Sequencial

1.  **Fila de Prioridade:** O AMS coleta todos os BroadcastReceiverers que correspondem ao Intent e os ordena com base no valor de **prioridade** definido pelo atributo android:priority no AndroidManifest.xml ou via IntentFilter.setPriority() [4].
2.  **Entrega:** A entrega é sequencial, começando pelo receptor de maior prioridade.
3.  **Controle de Fluxo (APIs):** Cada receptor pode:
    *   Chamar setResultData(), setResultCode() ou setResultExtras() para passar dados de resultado ao próximo receptor na sequência.
    *   Chamar abortBroadcast() para interromper a propagação do Intent, impedindo que receptores de menor prioridade o recebam [4].

### 2.2. Mudança Arquitetural no Android 16

No Android 16, a garantia da ordem de entrega baseada em prioridade foi restringida. A ordem de entrega usando android:priority **não é garantida** entre diferentes processos. A prioridade é respeitada apenas dentro do **mesmo processo de aplicação** [1]. Esta mudança visa otimizar a saúde geral do sistema, priorizando a entrega rápida em detrimento da ordem estrita entre processos.

## 3. Sticky Broadcasts (Depreciação e Arquitetura de Cache)

O mecanismo de Sticky Broadcasts foi **depreciado** desde o Android 5.0 (API 21) devido a falhas de segurança inerentes ao seu design [5].

---


## Page 37

# 3.1. Arquitetura de Cache

Um *sticky broadcast* é um Intent especial cujo objeto permanece armazenado em um cache do sistema após a conclusão da transmissão [5]. O sistema pode retransmitir esse Intent em cache para receptores que se registrem posteriormente, permitindo que eles acessem o último valor transmitido.

# 3.2. Falhas de Segurança (Protocolo)

As falhas de segurança decorrem do protocolo de acesso e permissão:

*   **Acesso Irrestrito:** O Intent em cache não pode ser restrito por permissões e é acessível por qualquer aplicativo [5].
*   **Modificação de Dados:** Um invasor pode trivialmente sobrescrever os dados extras (*Extra Data*) do Intent no cache, que será então retransmitido para outros receptores legítimos [5].
*   **Permissão Trivial:** A permissão `android.permission.BROADCAST_STICKY` era concedida automaticamente na instalação, permitindo que qualquer aplicativo enviisse broadcasts sticky [5].

# 3.3. Mitigação Técnica

A recomendação técnica é evitar o uso de *sticky broadcasts* e, em vez disso, utilizar mecanismos de gerenciamento de estado como LiveData (que implementa o Observer Pattern) ou um banco de dados local para armazenar o último valor e notificar os componentes interessados [5].

---

## Referências

[1] Broadcasts overview. Android Developers. Disponível em: https://developer.android.com/develop/background-work/background-tasks/broadcasts
[2] BroadcastQueue.java. Android Code Search. Disponível em: https://cs.android.com/android/platform/superproject/+/master:frameworks/base/services/core/java/com/android/server/am/BroadcastQueue.java
[3] core/java/android/content/IntentFilter.java. Android Open Source Project. Disponível em: https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/content/IntentFilter.java
[4] Context.SendOrderedBroadcast Method (Android.Content). Microsoft Learn. Disponível em: https://learn.microsoft.com/en-us/dotnet/api/android.content.context.sendorderedbroadcast?view=net-android-35.0
[5] Sticky Broadcasts. Android Developers. Disponível em: https://developer.android.com/privacy-and-security/risks/sticky-broadcast

---

# Componente 18: Services - Bound, Started, Foreground, JobScheduler (Android 16/AOSP)

Itens Técnicos Encontrados: 10

Conceitos-Chave: Binder IPC, Scatter-Gather, Real-time Priority Inheritance, ServiceRecord, ActivityManagerService, JobScheduler Quota Optimization Algorithm, App Standby Bucket, AIDL, HIDL, getPendingJobReasons

## Services do Android (Bound, Started, Foreground, JobScheduler) - Conteúdo Técnico AOSP/Android 16

---

### 1. Protocolo e Arquitetura de Comunicação Interprocessos (IPC)

A comunicação entre Services (especialmente Bound Services) e o sistema (ActivityManagerService, JobSchedulerService) é fundamentalmente baseada no protocolo **Binder IPC** [1].

---


## Page 38

# 1.1. Protocolo Binder IPC

O Binder é um mecanismo de comunicação interprocessos (IPC) do Android, implementado como um driver no kernel Linux. Ele facilita a comunicação de *message passing* entre processos, utilizando memória compartilhada para otimizar a transferência de dados.

*   **Otimização Scatter-Gather:** A partir do Android 8, o driver Binder utiliza a otimização *scatter-gather* para reduzir a cópia de dados de três para uma. Em vez de serializar os dados em um *Parcel* e copiá-los três vezes (processo chamador -> kernel -> processo alvo -> desserialização), os dados são mantidos em seu layout de memória original e copiados diretamente para o processo alvo, onde são lidos sem uma cópia adicional [1].
*   **Gerenciamento de Prioridade em Tempo Real:** O driver Binder implementa *Real-time priority inheritance* (Herança de Prioridade em Tempo Real). Se um thread em tempo real faz uma chamada Binder, o thread que trata essa chamada no processo alvo também é elevado para a prioridade em tempo real. Isso é crucial para evitar latência (*jank*) em operações sensíveis ao tempo [1].
*   **Domínios Binder:** A arquitetura separa os contextos de comunicação em diferentes nós de dispositivo, isolando o tráfego:
    *   `/dev/binder`: IPC entre processos de *framework* e aplicativos (AIDL).
    *   `/dev/hwbinder`: IPC entre *framework/vendor* (HIDL).
    *   `/dev/vndbinder`: IPC entre processos de *vendor* (AIDL) [1].

# 2. Arquitetura de Gerenciamento de Services

O ciclo de vida e a execução de todos os Services são gerenciados centralmente pelo **ActivityManagerService** (**AMS**), que reside no processo `system_server`.

*   **Estrutura de Dados ServiceRecord:** O AMS utiliza a estrutura de dados **ServiceRecord** para manter o estado, as informações de *binding* e o ciclo de vida de cada Service em execução. Esta estrutura é a representação interna do Service no lado do sistema [2].
*   **Fluxo de Comunicação:** A chamada para iniciar, parar ou *bind* a um Service (e.g., `Context.startService()`, `Context.bindService()` ) é uma transação Binder que é enviada ao AMS. O AMS, por sua vez, gerencia o processo da aplicação e invoca os métodos de *callback* do Service (e.g., `onCreate()`, `onStartCommand()`, `onBind()` ) [2].

# 3. Algoritmos e APIs do JobScheduler no Android 16

O Android 16 introduz otimizações significativas no gerenciamento de *jobs* em segundo plano, focando em um algoritmo de alocação de quota mais dinâmico e transparente [3].

## 3.1. Algoritmo de Otimização de Quota do JobScheduler

O algoritmo de agendamento e execução de *jobs* foi ajustado para alocar a quota de tempo de execução (*runtime quota*) de *jobs* regulares e acelerados (*expedited jobs*) com base em fatores dinâmicos:

1.  **App Standby Bucket:** O *bucket* de *standby* do aplicativo (e.g., *Active*, *Working Set*, *Frequent*, *Rare*) é o principal fator. *Buckets* mais ativos recebem uma quota de tempo de execução mais generosa [3].
2.  **Visibilidade do Aplicativo:** *Jobs* iniciados enquanto o aplicativo está visível para o usuário, mas que continuam após o aplicativo se tornar invisível, aderem à quota de tempo de execução do *job* [3].
3.  **Serviços em Primeiro Plano Concorrentes:** *Jobs* que estão sendo executados simultaneamente com um *Foreground Service* também aderem à quota de tempo de execução do *job*, reforçando a restrição de recursos em segundo plano [3].

## 3.2. APIs de Introspecção do JobScheduler

Para auxiliar na depuração e compreensão do algoritmo de agendamento, o Android 16 introduz novas APIs que expõem o estado interno do agendador:

---


## Page 39

* JobScheduler#getPendingJobReasons(int jobId): Retorna uma lista de razões pelas quais um job específico está pendente e não em execução. As razões incluem restrições explícitas definidas pelo desenvolvedor e restrições implícitas definidas pelo sistema (e.g., quota esgotada, restrições de rede/bateria) [3].
* JobScheduler#getPendingJobReasonsHistory(int jobId): Retorna uma lista das mudanças de restrição mais recentes para o job, permitindo uma análise histórica do agendamento [3].

Essas APIs utilizam uma estrutura de dados interna (e.g., PendingJobReasonsInfo) para encapsular o código da razão e o estado do job [3].

---

## Referências

[1] Use binder IPC. Android Open Source Project. URL: https://source.android.com/docs/core/architecture/hidl/binder-ipc
[2] ActivityManagerService. Android Open Source Project. URL: https://android.googlesource.com/platform/frameworks/base/+/4f868ed/services/core/java/com/android/server/am/ActivityMana
[3] The Second Developer Preview of Android 16. Android Developers Blog. URL: https://android-developers.googleblog.com/2024/12/second-developer-preview-android16.html

---

## Componente 19: Jetpack Compose Runtime (Recomposition, State, Side Effects)

Itens Técnicos Encontrados: 10

**Conceitos-Chave:** SlotTable, Gap Buffer, Recomposer, Snapshot System, Multiversion Concurrency Control (MVCC), SnapshotMutationPolicy, Dirty Flags, Composition, Recomposition Scopes, SideEffect, LaunchedEffect, remember

## Conteúdo Técnico: Jetpack Compose Runtime (Recomposition, State, Side Effects)

Este documento foca exclusivamente nos aspectos técnicos internos do Jetpack Compose Runtime, incluindo algoritmos, estruturas de dados, protocolos e arquitetura, conforme solicitado, com ênfase nos mecanismos de **Recomposition**, **remember**, **Side Effects** e **Modifiers**.

### 1. Arquitetura e Componentes Principais

A arquitetura do Compose Runtime é baseada em três pilares principais que orquestram o ciclo de vida da UI:

1. **Composition (Composição)**: A execução inicial das funções @Composable para construir a descrição da UI.
2. **Recomposition (Recomposição)**: A reexecução seletiva das funções @Composable quando o estado que elas leem muda.
3. **Runtime**: O ambiente que gerencia o estado, a composição e a aplicação das mudanças na árvore de UI.

### 1.1. O Recomposer

O Recomposer atua como o orquestrador central do ciclo de vida do Compose.

*   **Função**: Rastreia as dependências de estado e agenda a recomposição para os composables marcados como dirty (sujos) quando um MutableState é alterado [1].
*   **Algoritmo de Identificação de Dirty Composables**: O Recomposer mantém um mapeamento de qual estado é lido por qual escopo de composição. Quando uma mutação de estado ocorre, o Recomposer utiliza esse mapeamento para identificar e marcar os escopos de composição afetados (o que é frequentemente referido como “dirty flags” ou “bits de mudança”) para reexecução [2]. A otimização de skipping (salto) é aplicada pelo compilador, que insere verificações de

---


## Page 40

estabilidade ( $composer . changed(value) ) no bytecode para evitar a reexecução de *composables* cujos parâmetros não mudaram [3].

# 2. Estruturas de Dados Fundamentais

## 2.1. SlotTable (Tabela de Slots)

A SlotTable é a estrutura de dados interna primária do Compose Runtime, responsável por armazenar a descrição da UI e o estado associado.

*   **Estrutura:** É uma estrutura de dados baseada no conceito de **Gap Buffer** (Buffer de Lacuna) [4].
*   **Gap Buffer (Algoritmo):** O Gap Buffer é um algoritmo de estrutura de dados otimizado para inserções e exclusões rápidas em um ponto específico de uma sequência.
    *   A SlotTable é implementada como um array plano (ou lista) que contém uma lacuna (gap) móvel.
    *   **Otimização:** A inserção ou exclusão de elementos (slots) na posição da lacuna é uma operação de tempo constante **O(1)**. Isso é crucial para a recomposição, onde a UI é frequentemente modificada (elementos adicionados, removidos ou reordenados) em um local específico da árvore [4].
    *   **Movimentação da Lacuna:** A movimentação da lacuna para um novo ponto de inserção/exclusão é uma operação **O(n)**, mas é amortizada, pois a maioria das mutações ocorre no mesmo local [4].
*   **Conteúdo:** A SlotTable armazena:
    *   Valores memorizados (do remember ).
    *   Referências a nós da UI (elementos da árvore).
    *   Informações de agrupamento e escopo de composição.

## 2.2. Snapshot System (Sistema de Snapshot)

O Snapshot System é o mecanismo de concorrência e gerenciamento de estado do Compose, implementando um protocolo de Multiversion Concurrency Control (MVCC) [5].

*   **Protocolo MVCC:** Permite que a leitura do estado (durante a composição) ocorra sem bloqueio, enquanto as mutações (escritas) são isoladas e aplicadas atomicamente.
    *   **Leitura Consistente:** A UI (thread de composição) sempre lê uma visão coerente e imutável do estado (um snapshot).
    *   **Mutação Isolada:** As alterações de estado são feitas em um snapshot privado.
    *   **Aplicação Atômica:** A aplicação do snapshot (o commit) verifica conflitos de escrita. Se não houver conflitos, a alteração é aplicada ao estado global e notifica o Recomposer [5].
*   **SnapshotMutationPolicy (Protocolo de Mutação):** Define como o sistema lida com a mutação e a fusão de alterações de estado [6].
    *   `structuralEqualityPolicy()`: Usa a igualdade estrutural (equals()) para determinar se o valor realmente mudou, evitando recomposições desnecessárias.
    *   `neverEqualPolicy()`: Sempre força a notificação de mudança, garantindo a recomposição.
    *   `referentialEqualityPolicy()`: Usa a igualdade de referência (padrão para mutableStateOf), notificando a mudança se a referência do objeto for alterada.

# 3. Side Effects (Efeitos Colaterais) e APIs

Os *Side Effects* são APIs que permitem a interação controlada entre o mundo declarativo do Compose e o mundo imperativo (I/O, corrotinas, listeners).

---


## Page 41

<table>
  <thead>
    <tr>
      <th>API de Side Effect</th>
      <th>Propósito Técnico</th>
      <th>Mecanismo de Execução</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>SideEffect</b></td>
      <td>Execução de código imperativo após a composição bem-sucedida.</td>
      <td>Executado no final da fase de <b>Composition</b> ou <b>Recomposition</b>, antes que a UI seja desenhada [7]. Não é reiniciado em caso de mudança de chave.</td>
    </tr>
    <tr>
      <td><b>LaunchedEffect</b></td>
      <td>Iniciar uma corrotina vinculada ao ciclo de vida do <i>composable</i>.</td>
      <td>Utiliza o <i>CouroutineScope</i> do <i>composable</i>. A corrotina é cancelada e reiniciada se a chave (key) mudar, seguindo o protocolo de concorrência de corrotinas [7].</td>
    </tr>
    <tr>
      <td><b>DisposableEffect</b></td>
      <td>Gerenciar recursos que precisam de limpeza (listeners, subscriptions).</td>
      <td>Requer um bloco <i>onDispose</i> que é executado quando o <i>composable</i> sai da composição ou quando a chave muda, garantindo a liberação de recursos [7].</td>
    </tr>
    <tr>
      <td><b>remember</b></td>
      <td>Memoização de valores através das recomposições.</td>
      <td>Armazena o valor na <i>SlotTable</i> no slot correspondente. O valor é recuperado na próxima recomposição, desde que a chave (key) não mude [8].</td>
    </tr>
    <tr>
      <td><b>derivedStateOf</b></td>
      <td>Otimização de cálculos caros dependentes de estado.</td>
      <td>Recalcula o valor apenas quando as dependências de estado lidas dentro de seu bloco mudam, e não em toda recomposição do <i>composable</i> pai [1].</td>
    </tr>
  </tbody>
</table>

# 4. Modifiers (Modificadores)

Os Modifiers são implementados como uma lista encadeada de objetos que aplicam transformações e comportamentos aos elementos da UI.

*   **Estrutura:** Modifier é uma interface que representa uma lista de elementos Modifier.Element. A aplicação de modificadores é a concatenação desses elementos em uma lista encadeada.
*   **Protocolo de Aplicação:** Os modificadores são processados em ordem. Durante as fases de <b>Measure</b> (Medição) e <b>Layout</b> (Disposição), os modificadores são iterados para calcular o tamanho e a posição do elemento, permitindo que cada modificador influencie o resultado do próximo [9].

# Referências

[1] Oktay Genç. *Decoding the Soul of the Compose Runtime: A Deep Anatomy of the Recomposer, Snapshot State, and Side-Effect Model*. Medium. [2] Amit Kalghatgi. *Recomposition in Jetpack Compose*. Medium. [3] blog.devgenius.io. *Smart Recomposition Demystified Jetpack Compose*. [4] Akshay Nandwana. *Understanding Gap Buffers in Jetpack Compose: The 60-Year-Old Algorithm Powering Modern Android UI*. ProAndroidDev. [5] abd409115011. *Concurrency Control in Jetpack Compose*. Medium. [6] Zach Klipp. *Introduction to the Compose Snapshot system*. blog.zachklipp.com. [7] Android Developers. *Side-effects in Compose*. [8] Sandeep Kella. *How remember in Jetpack Compose Saves You a Slot Internally*. Medium. [9] Android Developers. *Jetpack Compose phases*.

# Componente 20: View System - Measure/layout/draw, touch events, ViewGroup, custom views

**Itens Técnicos Encontrados:** 12

**Conceitos-Chave:** Árvore de Views, MeasureSpec, Algoritmo de Medição, Algoritmo de Layout, Algoritmo de Desenho, MotionEvent, Protocolo de Dispatch de Toque, onInterceptTouchEvent, onTouchEvent, requestLayout, invalidate

---


## Page 42

# Conteúdo Técnico: View System - Measure/Layout/Draw e Eventos de Toque (Android AOSP)

O View System do Android é a base para a interface do usuário, operando através de um pipeline de renderização e um protocolo de dispatch de eventos de toque. O foco técnico reside nos algoritmos de medição e layout, nas estruturas de dados que governam as restrições de tamanho e no protocolo de roteamento de eventos.

## 1. Pipeline de Renderização (Measure/Layout/Draw)

O processo de renderização de uma View e ViewGroup é um algoritmo de duas passagens, executado de forma recursiva em uma **Árvore de Views** (View Tree), iniciando pelo nó raiz.

### 1.1. Algoritmo de Medição (Measure Pass)

**Objetivo:** Determinar o *tamanho medido* (measured width e measured height) que cada View deseja ter, respeitando as restrições do pai.

**Estrutura de Dados:** MeasureSpec

Um MeasureSpec é um inteiro empacotado que contém um **Modo** e um **Tamanho** (size). É passado de pai para filho através do método `measure(int widthMeasureSpec, int heightMeasureSpec)`.

**Modos de Medição:**

*   MeasureSpec.EXACTLY : O pai impõe um tamanho exato. A View deve usar este tamanho. Ocorre quando `layout_width` ou `layout_height` são definidos com um valor fixo (ex: 100dp ) ou `match_parent` (se o pai tiver um tamanho fixo).
*   MeasureSpec.AT_MOST : O pai impõe um tamanho máximo. A View deve ser menor ou igual a este tamanho. Ocorre quando `layout_width` ou `layout_height` são definidos como `wrap_content` dentro de um pai com restrições.
*   MeasureSpec.UNSPECIFIED : O pai não impõe restrições. A View pode ser do tamanho que desejar. Ocorre raramente, tipicamente em ViewGroup s adaptáveis como ScrollView.

**API/Método Central:** `onMeasure(int widthMeasureSpec, int heightMeasureSpec)`

Implementado em View e ViewGroup para calcular o tamanho. Em ViewGroup , o método itera sobre os filhos, chamando `measure()` em cada um, e então calcula seu próprio tamanho com base nos tamanhos dos filhos e nas suas próprias restrições. O resultado final é armazenado via `setMeasuredDimension(int measuredWidth, int measuredHeight)`.

### 1.2. Algoritmo de Layout (Layout Pass)

**Objetivo:** Determinar a posição e o tamanho final de cada View dentro de seu pai.

**API/Método Central:** `onLayout(boolean changed, int left, int top, int right, int bottom)`

Chamado pelo pai após a passagem de medição. Em ViewGroup , o método usa os tamanhos medidos dos filhos para calcular as coordenadas de posicionamento (left, top, right, bottom) de cada filho. O ViewGroup chama o método `layout(int l, int t, int r, int b)` em cada filho para definir sua posição final.

### 1.3. Algoritmo de Desenho (Draw Pass)

**Objetivo:** Renderizar o conteúdo da View na tela.

**API/Método Central:** `onDraw(Canvas canvas)`

Chamado após o Layout Pass. A View usa o objeto canvas fornecido para desenhar seu conteúdo (texto, formas, bitmaps). O ciclo de desenho de uma ViewGroup inclui:

*   **onDraw()** - chamado por ViewGroup
    *   **onDrawChild()** - chamada por ViewGroup para cada filho
        *   **onPreDraw()** - método de cada View
            *   **onLayout()** - chamados por ViewGroup
                *   **onMeasure()** - chamado por ViewGroup
                    *   **onSizeChanged()** - chamada por ViewGroup
                        *   **onDraw()** - chamadas por ViewGroup
                            *   **onLayout()** - chamados por ViewGroup
                                *   **onMeasure()** - chamado por ViewGroup
                                    *   **onSizeChanged()** - chamada por ViewGroup
                                        *   **onDraw()** - chamadas por ViewGroup
                                            *   **onLayout()** - chamados por ViewGroup
                                                *   **onMeasure()** - chamado por ViewGroup
                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                        *   **onDraw()** - chamadas por ViewGroup
                                                            *   **onLayout()** - chamados por ViewGroup
                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado por ViewGroup
                                                                                                                                                                    *   **onSizeChanged()** - chamada por ViewGroup
                                                                                                                                                        *   **onDraw()** - chamadas por ViewGroup
                                                                                                                                                            *   **onLayout()** - chamados por ViewGroup
                                                                                                                                                                *   **onMeasure()** - chamado

---


## Page 43

1. Desenhar o próprio fundo.
2. Chamar `draw()` para cada filho.
3. Desenhar elementos de frente (foreground, barras de rolagem).

**Mecanismo de Atualização:** `requestLayout()` e `invalidate()`

*   `requestLayout()` : Inicia um novo ciclo completo de Measure e Layout (e Draw). Usado quando o tamanho ou posição da View pode mudar.
*   `invalidate()` : Inicia apenas o ciclo de Draw. Usado quando apenas a aparência da View muda, mas não seu tamanho ou posição.

# 2. Protocolo de Dispatch de Eventos de Toque

O tratamento de eventos de toque (representados pela estrutura de dados `MotionEvent`) segue um protocolo de roteamento top-down (dispatch) e consumo bottom-up.

## 2.1. Estrutura de Dados: MotionEvent

Contém dados sobre o evento de toque: coordenadas X/Y, tempo, e o tipo de ação (`ACTION_DOWN`, `ACTION_MOVE`, `ACTION_UP`, `ACTION_CANCEL`). O `ACTION_DOWN` é o ponto de partida de uma sequência de eventos de toque.

## 2.2. Algoritmo de Dispatch

O evento de toque começa na Activity e é passado para a ViewGroup raiz, que inicia o processo recursivo:

1.  **dispatchTouchEvent(MotionEvent ev)** : Método principal em View e ViewGroup. Se for uma ViewGroup, ele primeiro chama `onInterceptTouchEvent()`. Se `onInterceptTouchEvent()` retornar true, o evento é interceptado e a ViewGroup tenta consumi-lo em seu próprio `onTouchEvent()`. Se `onInterceptTouchEvent()` retornar false, o evento é passado para os filhos (em ordem inversa de Z, ou seja, o mais visível primeiro).
2.  **onInterceptTouchEvent(MotionEvent ev)** (Apenas em ViewGroup): Decide se a ViewGroup deve “roubar” o evento de toque de seus filhos. Se retornar true para um `ACTION_DOWN`, todos os eventos subsequentes daquela sequência (MOVE, UP) serão enviados diretamente para o `onTouchEvent` da ViewGroup .
3.  **onTouchEvent(MotionEvent ev)** (Em view e ViewGroup): Onde o evento é efetivamente consumido. Se retornar true, a View ou ViewGroup se torna o “alvo” do toque, e todos os eventos subsequentes da sequência serão enviados diretamente a ela, ignorando `onInterceptTouchEvent` e outros filhos.

**Protocolo de Consumo:**

*   O evento é considerado consumido se `onTouchEvent()` retornar true.
*   Se um `ACTION_DOWN` não for consumido por nenhuma View ou ViewGroup na árvore, todos os eventos subsequentes daquela sequência são descartados.
*   A ViewGroup pode impedir que seus pais interceptem eventos chamando `requestDisallowInterceptTouchEvent(true)` em seu pai.

---

# Componente 21: SurfaceFlinger - Buffer queues, vsync, composition, HWC

**Itens Técnicos Encontrados:** 15

**Conceitos-Chave:** BufferQueue, SurfaceControl, ASurfaceControl, Gralloc, VSync, Synchronization Fences, Hardware Composer HAL (HWC), Device Composition, GPU Fallback, Pre-rotation

---


## Page 44

# Conteúdo Técnico: SurfaceFlinger, Buffer Queues, VSync, Composition e HWC no Android AOSP

O **SurfaceFlinger** é o componente central da arquitetura gráfica do Android, atuando como o compositor de sistema responsável por aceitar *buffers* de dados gráficos de múltiplas fontes, compô-los em uma única imagem e enviá-la para o *display* [1]. Sua operação é intrinsecamente ligada ao **Hardware Composer HAL (HWC)**, ao sistema de gerenciamento de janelas (*WindowManager*) e a mecanismos de sincronização de baixo nível, como o VSync e os *Synchronization Fences* [2].

## 1. Estruturas de Dados e APIs de Comunicação

A comunicação de dados gráficos entre os aplicativos (*produtores*) e o SurfaceFlinger (*consumidor*) é orquestrada por estruturas de dados e APIs específicas, garantindo a transferência eficiente e sincronizada de *buffers* [1].

A estrutura de dados fundamental é o **BufferQueue**, que implementa o padrão produtor-consumidor para a transferência de *buffers* de dados gráficos. O lado do produtor é representado por um objeto **Surface**, que é onde a renderização do aplicativo (via Canvas API, OpenGL ES ou Vulkan) é direcionada. O resultado dessa renderização é armazenado em um *buffer* que é subsequentemente enfileirado para o SurfaceFlinger consumir [1].

O gerenciamento da camada de exibição é realizado através do **SurfaceControl**, uma estrutura que contém metadados cruciais, como o *frame* de exibição, a posição, as transformações geométricas e a ordem Z (*z-order*) da camada. O *WindowManager* utiliza o SurfaceControl para manipular a aparência da aplicação na tela e comunica esses metadados ao SurfaceFlinger [2].

A partir do Android 10, a API **ASurfaceControl** foi introduzida, combinando a *Surface* e o *SurfaceControl* em um pacote de transação unificado. As atualizações de camada são realizadas através de instâncias de **ASurfaceTransaction**, e o *feedback* sobre a apresentação é fornecido pela estrutura **ASurfaceTransactionStats**, que detalha o tempo de *latch* e os *fences* de aquisição [2]. A alocação de memória para esses *buffers* é gerenciada pelo **Gralloc** (Graphics Memory Allocator), uma HAL que fornece a interface para a alocação de memória gráfica específica do fornecedor [1].

## 2. Protocolos de Sincronização: VSync e Synchronization Fences

A sincronização temporal é crítica para evitar artefatos visuais como o *tearing* (rasgo de tela) e para otimizar o consumo de energia. Dois protocolos principais regem essa sincronização:

### VSync (Vertical Synchronization)

O VSync é um sinal de temporização gerado pelo *display* e transmitido ao SurfaceFlinger, indicando o início de um novo ciclo de varredura vertical [2].

> "Quando o display está entre atualizações, o display envia o sinal VSync para o SurfaceFlinger. O sinal VSync indica que ele pode atualizar o display sem tearing. Quando o SurfaceFlinger recebe o sinal VSync, ele percorre sua lista de camadas procurando por novos buffers." [2]

O algoritmo de VSync no SurfaceFlinger é reativo: ele acorda apenas uma vez por VSync. Se um novo *buffer* estiver disponível em uma BufferQueue , ele é adquirido (*latch*); caso contrário, o *buffer* adquirido anteriormente é reutilizado. O **HWC** é o componente de hardware responsável por gerar e enviar os eventos VSync para o SurfaceFlinger [3].

### Synchronization Fences

Os *Synchronization Fences* (ou *Sync Fences*) são um mecanismo de sincronização assíncrona que permite que o trabalho da CPU e da GPU prossiga de forma independente, bloqueando apenas quando há uma dependência real [3].

O protocolo envolve o aplicativo submeter um *buffer* produzido na GPU juntamente com um objeto *sync fence*. Este *fence* sinaliza o momento exato em que a GPU finalizou a escrita no *buffer*. O **HWC** utiliza esse protocolo para garantir que um *buffer* só seja exibido após a conclusão da escrita pela GPU, verificando se o *fence* sinalizou antes de exibir o *buffer* [3].

---


## Page 45

# 3. Algoritmos e Estratégias de Composição (HWC)

O Hardware Composer HAL (HWC) é uma camada de abstração de *hardware* que assume a maior parte da carga de composição, utilizando *hardware* especializado (como *overlays* e *blitters* 2D) para reduzir o uso da GPU e do OpenGL ES (GLES) [3].

O SurfaceFlinger e o HWC empregam um algoritmo de composição em múltiplas etapas, executado a cada VSync, se houver novo conteúdo:

<table>
  <thead>
    <tr>
      <th>Etapa</th>
      <th>Componente</th>
      <th>Ação Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>SurfaceFlinger</td>
      <td>Lida com transações e faz *latch* de novos *buffers* gráficos.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>SurfaceFlinger -> HWC</td>
      <td>Chama `validateDisplay()` para que o HWC examine o estado das camadas e determine a estratégia de composição.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>HWC -> SurfaceFlinger</td>
      <td>O HWC retorna as mudanças de tipo de composição (`getChangedCompositionTypes`).</td>
    </tr>
    <tr>
      <td>4</td>
      <td>SurfaceFlinger</td>
      <td>Chama `acceptDisplayChanges` para aceitar a estratégia do HWC.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>SurfaceFlinger</td>
      <td><b>Composição de Fallback (GPU):</b> Se o HWC marcar camadas para composição pelo cliente, o SurfaceFlinger as compõe usando a GPU e chama `setClientTarget` para entregar o resultado.</td>
    </tr>
    <tr>
      <td>6</td>
      <td>SurfaceFlinger -> HWC</td>
      <td>Chama `presentDisplay` para instruir o HWC a finalizar a composição e exibir o resultado final.</td>
    </tr>
  </tbody>
</table>

**Estratégias de Composição:**

*   **HWC (Device Composition):** O HWC compõe todas as camadas diretamente usando *hardware* dedicado. Esta é a estratégia preferencial por ser mais eficiente em termos de energia e desempenho [3].
*   **SurfaceFlinger (GPU Fallback / Client Composition):** Ocorre quando o HWC não pode lidar com a composição de certas camadas (por exemplo, devido a limitações de *hardware* ou em displays virtuais sem suporte HWC). O SurfaceFlinger utiliza a GPU para realizar a composição [3].

Um algoritmo de otimização notável é a **Pré-rotação (Pre-rotation)**. Para evitar que o HWC ou o SurfaceFlinger gastem poder de processamento com rotações, o Android fornece uma dica (`NATIVE_WINDOW_TRANSFORM_HINT`) via ANativeWindow. Os drivers GL podem usar essa dica para aplicar a transformação (rotação) ao *buffer* antes que ele chegue ao SurfaceFlinger, garantindo que o *buffer* já esteja corretamente orientado [2].

# 4. Arquitetura de Displays

O SurfaceFlinger suporta a arquitetura de múltiplos *displays* físicos (a partir do Android 10) e *displays* virtuais [3].

## Displays Virtuais

A composição para *displays* virtuais é similar à de *displays* físicos, mas o *output* é direcionado a um *buffer* **Galloc** em vez de diretamente para a tela. O HWC escreve o *output* neste *buffer*, fornece o *completion fence* e o envia a um consumidor (como um *video encoder* ou a GPU) [3].

Os modos de composição para *displays* virtuais definem o algoritmo de renderização:

<table>
  <thead>
    <tr>
      <th>Modo</th>
      <th>Algoritmo de Composição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GLES</td>
      <td>A GPU compõe todas as camadas, escrevendo diretamente no *buffer* de saída. O HWC não está envolvido na composição.</td>
    </tr>
    <tr>
      <td>MIXED</td>
      <td>A GPU compõe algumas camadas para o *framebuffer*, e o HWC compõe o *framebuffer* e as camadas restantes.</td>
    </tr>
    <tr>
      <td>HWC</td>
      <td>O HWC compõe todas as camadas, escrevendo diretamente no *buffer* de saída.</td>
    </tr>
  </tbody>
</table>

O formato de saída do *buffer* virtual depende do modo. No modo GLES, é tipicamente `RGBA_8888`. Nos modos MIXED e HWC, o formato pode ser `IMPLEMENTATION_DEFINED`, permitindo que o Galloc escolha o formato mais eficiente (ex: YCbCr para *video*

---


## Page 46

encoders) com base nas usage flags [3].

---

## Referências

[1] Graphics architecture | Android Open Source Project [2] SurfaceFlinger and WindowManager | Android Open Source Project [3] Implement Hardware Composer HAL | Android Open Source Project

---

## Componente 22: Skia Graphics - Canvas API, Path Operations, Shaders, Image Filters (Android 16 AOSP)

Itens Técnicos Encontrados: 13

Conceitos-Chave: SkCanvas, SkPath, SkPath::kMove_Verb, SkPath::kLine_Verb, SkPath::kQuad_Verb, SkPath::kConic_Verb, SkPath::kCubic_Verb, Path Fill Type, SkSL, SkRuntimeEffect, SkShader, SkColorFilter, SkBlender, Pipeline de Fragment Shader, Gerenciamento de Cores, Alpha Pré-multiplicado, Uniforms com layout(color)

---

## Conteúdo Técnico: Skia Graphics no Android 16 (AOSP)

O Skia Graphics Engine, componente central do sistema gráfico do Android, oferece uma arquitetura robusta para renderização 2D de alto desempenho. A implementação no Android 16 (AOSP) se baseia em APIs de baixo nível como **SkCanvas**, **SkPath** e o sistema de sombreamento **SkSL/SkRuntimeEffect**, que gerenciam a geometria, as operações de caminho, os shaders e os filtros de imagem.

### 1. Arquitetura da Canvas API (SkCanvas)

O **SkCanvas** é a principal API de desenho, atuando como o **contexto de desenho** que direciona a renderização para uma superfície (tela ou offscreen) e mantém uma **pilha de matrizes de transformação e clips** [1].

#### Estruturas de Dados e APIs Chave:

*   **SkCanvas**: Objeto central que armazena o estado gráfico (matriz de transformação e clip) e expõe as chamadas de desenho (draw calls).
*   **SkPaint**: Estrutura de dados que armazena os atributos de desenho (cor, largura do traço, estilo, antialiasing, shader, color filter, blend mode) e é passada explicitamente em cada draw call [1].
*   **Pilha de Matrizes e Clips**: O SkCanvas implementa os métodos save() e restore() para gerenciar uma pilha de estados de transformação e clipagem, permitindo transformações localizadas sem afetar o estado global.

### 2. Operações de Caminho (SkPath)

O **SkPath** é a estrutura de dados fundamental para representar geometrias 2D complexas, composta por uma ou mais **Contornos** (contours), que são sequências de segmentos conectados [2].

#### Estruturas de Dados e Algoritmos:

*   **Estrutura do SkPath**: Uma sequência de **Verbos** (Verbs) e **Pontos** (Points) que definem a geometria. O primeiro Verb em um Path é sempre SkPath::kMove_Verb, e cada kMove_Verb subsequente inicia um novo contour [2].
*   **Verbos de Caminho (Path Verbs)**:
    *   SkPath::kMove_Verb : Move o ponto atual, iniciando um novo contorno.
    *   SkPath::kLine_Verb : Desenha um segmento de linha reta.

---


## Page 47

*   `SkPath::kQuad_Verb`: Desenha uma curva de Bézier quadrática (um ponto de controle).
*   `SkPath::kConic_Verb`: Desenha uma curva cônica (um ponto de controle e um peso `Path_Conic_Weight`).
*   `SkPath::kCubic_Verb`: Desenha uma curva de Bézier cúbica (dois pontos de controle).
*   `SkPath::kClose_Verb`: Fecha o contorno, conectando o último ponto ao primeiro [2].

*   **Path Fill Type**: Algoritmo que determina como as áreas sobrepostas dos contornos são preenchidas (ex: `winding`, `EvenOdd`), definindo se formam preenchimentos ou buracos [2].
*   **Path Ops**: Operações booleanas de caminho (união, interseção, diferença, XOR) que são implementadas por algoritmos de geometria computacional para combinar geometrias complexas.

# 3. Shaders e Filtros de Imagem (SkSL e SkRuntimeEffect)

O Skia utiliza o **SkSL** (Skia Shading Language), uma linguagem de sombreamento de alto nível similar ao GLSL, para criar shaders e filtros de imagem dinâmicos [3].

## Arquitetura e Protocolos:

*   **SkSL**: Linguagem de sombreamento que é compilada em tempo de execução para o código de fragment shader do GPU backend (como Vulkan no Android 16) [3].
*   **SkRuntimeEffect**: Objeto C++ que encapsula o código SkSL e é usado para criar instâncias de SkShader, SkColorFilter e SkBlender com comportamento definido pelo código SkSL [3].
*   **Pipeline de Fragment Shader**: O Skia compila dinamicamente um único fragment shader de GPU que integra todas as etapas de renderização, incluindo:
    1. Avaliação de antialiasing e clipagem.
    2. Lógica do SkShader (que pode ser uma árvore de shaders, incluindo outros SkRuntimeEffect s).
    3. Lógica do SkColorFilter .
    4. Código de SkBlendMode (blending).
    5. Conversão de espaço de cores [3].
*   **Gerenciamento de Cores**: O Skia aplica automaticamente a conversão de espaço de cores (ex: sRGB para Rec. 2020) para a maioria das entradas.
    *   **Uniforms com layout(color)** : Variáveis uniformes no SkSL que são explicitamente marcadas para receber a conversão de espaço de cores, garantindo consistência de cor independentemente do espaço de cor de destino [3].
    *   `toLinearSrgb()` / `fromLinearSrgb()`: Funções intrínsecas do SkSL para conversão entre o espaço de cor de trabalho e o espaço linear sRGB, essencial para cálculos de iluminação fisicamente corretos [3].
*   **Alpha Pré-multiplicado (Premultiplied Alpha)**: O Skia opera consistentemente com cores pré-multiplicadas ( `[R*A, G*A, B*A, A]`) em sua pipeline de shader, o que é crucial para o algoritmo de *blending source-over* (`GL_ONE`, `GL_ONE_MINUS_SRC_ALPHA`) [3].
*   **Raw Image Shaders**: API (`SkImage::makeRawShader`) para criar shaders a partir de imagens que contêm dados não-cor (ex: mapas de normais), ignorando a conversão de espaço de cores e a pré-multiplicação de alpha [3].

---


## Page 48

# 4. Resumo dos Componentes Técnicos

<table>
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Componente Técnico</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>APIs/Estruturas</td>
      <td>SkCanvas</td>
      <td>Contexto de desenho, gerencia a pilha de matrizes e clips.</td>
    </tr>
    <tr>
      <td>Estruturas de Dados</td>
      <td>SkPaint</td>
      <td>Armazena atributos de desenho (cor, estilo, shaders).</td>
    </tr>
    <tr>
      <td>Estruturas de Dados</td>
      <td>SkPath</td>
      <td>Representação de geometria 2D como sequência de Verbos e Pontos.</td>
    </tr>
    <tr>
      <td>Algoritmos</td>
      <td>Path Fill Type (Winding/EvenOdd)</td>
      <td>Algoritmo de preenchimento de contornos.</td>
    </tr>
    <tr>
      <td>Algoritmos</td>
      <td>Path Ops (Booleano)</td>
      <td>Algoritmos de geometria computacional para união/interseção de caminhos.</td>
    </tr>
    <tr>
      <td>Linguagem/API</td>
      <td>SkSL (Skia Shading Language)</td>
      <td>Linguagem de sombreamento de alto nível.</td>
    </tr>
    <tr>
      <td>API/Estrutura</td>
      <td>SkRuntimeEffect</td>
      <td>Objeto C++ que encapsula e compila código SkSL.</td>
    </tr>
    <tr>
      <td>Arquitetura</td>
      <td>Pipeline de Fragment Shader Dinâmico</td>
      <td>Algoritmo de compilação que gera um único shader de GPU a partir de uma árvore de efeitos.</td>
    </tr>
    <tr>
      <td>Protocolo/Backend</td>
      <td>Vulkan Backend</td>
      <td>Implementação do Skia para renderização via API Vulkan.</td>
    </tr>
    <tr>
      <td>Algoritmos</td>
      <td>Gerenciamento de Cores (Conversão)</td>
      <td>Algoritmos de transformação de cores entre espaços (ex: sRGB para Rec. 2020).</td>
    </tr>
    <tr>
      <td>Algoritmos</td>
      <td>Alpha Pré-multiplicado</td>
      <td>Algoritmo de blending source-over baseado em cores pré-multiplicadas.</td>
    </tr>
    <tr>
      <td>APIs</td>
      <td>SkPath::kMove_Verb, kLine_Verb, kQuad_Verb, kConic_Verb, kCubic_Verb</td>
      <td>Verbos que definem a estrutura de dados e a geometria do caminho.</td>
    </tr>
    <tr>
      <td>APIs</td>
      <td>SkImage::makeRawShader</td>
      <td>API para criação de shaders que ignoram o gerenciamento de cores.</td>
    </tr>
  </tbody>
</table>

Referências [1] SkCanvas Overview. Skia Documentation. [2] SkPath Overview. Skia Documentation. [3] SkSL & Runtime Effects. Skia Documentation.

---

# Componente 23: Vulkan OpenGL ES - Command buffers, pipelines, descriptor sets, SPIR-V

Itens Técnicos Encontrados: 15

**Conceitos-Chave:** Vulkan Loader, Driver, SPIR-V, VkCommandBuffer, VkPipeline, VkDescriptorSet, WSI, Gralloc, AHardwareBuffer, VkSwapchainKHR, VkPipelineCache, VkDeviceMemory, VkBuffer, VkImage, VkShaderModule

O componente **Vulkan/OpenGL ES** no contexto do Android 16 (AOSP) é fundamental para a arquitetura gráfica de baixo nível, visando a redução do *overhead* da CPU e o acesso direto ao hardware da GPU [1] [2]. A arquitetura se baseia em uma interação estrita entre o **Vulkan Loader** (fornecido pelo Android) e o **Vulkan Driver** (fornecido pelo SoC/IHV) [2].

## Arquitetura e Protocolos

O **Vulkan Loader** ( libvulkan.so ) é o ponto de entrada da API Vulkan para as aplicações. Ele gerencia o carregamento e o *dispatch* das chamadas para o **Vulkan Driver** específico do hardware [3].

1.  **Protocolo de Interface do Driver (ICD):** O Loader interage com o Driver através de um protocolo de interface de driver instalável (ICD). O Driver é descoberto via HAL (Hardware Abstraction Layer), buscando módulos em caminhos como /vendor/lib[64]/hw/vulkan.<ro.hardware.vulkan>.so [3].

---


## Page 49

2. **WSI (Window System Integration):** A integração com o sistema de janelas do Android é tratada por extensões Vulkan específicas, como `VK_KHR_surface`, `VK_KHR_swapchain` e, crucialmente, `VK_KHR_android_surface` [3].

3. **Protocolo de Buffer Nativo:** A extensão `VK_ANDROID_native_buffer` é utilizada para a comunicação entre o Vulkan e o sistema de buffers do Android, permitindo que o driver utilize *handles* de buffers nativos (`AHardwareBuffer`) para alocação de memória e criação de imagens de *swapchain* [3] [4].

## Estruturas de Dados e Objetos Vulkan

Os objetos Vulkan são representados por *handles* (identificadores) que, internamente no Loader do AOSP, são mapeados para estruturas de dados que contêm informações de *dispatch* e estado.

### 1. Command Buffers ( VkCommandBuffer )

O `VkCommandBuffer` é a estrutura de dados central para o registro de comandos da GPU.

*   **Estrutura Lógica:** Existem dois níveis: *primary* (pode executar *secondary*) e *secondary* (não pode ser submetido diretamente a uma fila) [5].
*   **Alocação:** São alocados a partir de um *pool* de comandos (`VkCommandPool`) [5].
*   **Uso no AOSP:** O arquivo `vulkan/api/vulkan.api` no AOSP define o `VkCommandBuffer` como um *handle* despachável (`@dispatchHandle type u64 VkCommandBuffer`), indicando que o Loader mantém uma tabela de *dispatch* associada a ele [6].

### 2. Pipelines ( VkPipeline )

O `VkPipeline` é um objeto imutável que encapsula o estado completo da GPU para uma operação de desenho ou computação.

*   **Estrutura de Criação:** A criação de um *pipeline* gráfico envolve a estrutura `VkGraphicsPipelineCreateInfo`, que inclui arrays de `VkPipelineShaderStageCreateInfo` (para estágios de *shader*), `VkPipelineVertexInputStateCreateInfo`, `VkPipelineInputAssemblyCreateInfo`, entre outros [7].
*   **Cache:** O Vulkan suporta o uso de `VkPipelineCache` para reutilizar *pipelines* criados anteriormente, o que é uma otimização crítica para o desempenho em dispositivos móveis [8].
*   **Estrutura Interna (AOSP Loader):** O `VkPipeline` é definido como um *handle* não despachável (`@nonDispatchHandle type u64 VkPipeline`) [6].

### 3. Descriptor Sets ( VkDescriptorSet )

Os *Descriptor Sets* são a forma como os *shaders* acessam recursos como *buffers* (`VkBuffer`), imagens (`VkImage`) e *samplers* (`VkSampler`).

*   **Alocação:** São alocados a partir de um *pool* de descritores (`VkDescriptorPool`) [9].
*   **Layout:** O layout de um *descriptor set* é definido por `VkDescriptorSetLayout`, que especifica os tipos de recursos e os estágios de *shader* que os utilizarão [9].
*   **Estrutura Interna (AOSP Loader):** O `VkDescriptorSet` é um *handle* não despachável (`@nonDispatchHandle type u64 VkDescriptorSet`) [6].

### 4. SPIR-V (Standard Portable Intermediate Representation)

SPIR-V é a linguagem intermediária binária utilizada pelo Vulkan para representar *shaders* [1].

*   **Formato de Arquivo:** O SPIR-V é um formato binário que encapsula o código do *shader* e metadados.
*   **Processamento no AOSP:** O AOSP utiliza o projeto **SPIRV-Tools** (disponível em `platform/external/deqp-deps/SPIRV-Tools`) para processamento, incluindo montagem, desmontagem e otimização de módulos SPIR-V [10].
*   **Reflexão:** Bibliotecas como **SPIRV-Cross** são comumente usadas para reflexão (extração de metadados) e tradução de SPIR-V para outras linguagens de *shader* (como GLSL ou HLSL), embora a integração direta no AOSP para uso em tempo de execução do driver não seja explicitamente detalhada como uma estrutura de dados primária do Loader [11]. O objeto Vulkan que contém o código SPIR-V é o `VkShaderModule` (`@nonDispatchHandle type u64 VkShaderModule`) [6].

---


## Page 50

# Estruturas de Dados Internas do Loader (Exemplo)

O arquivo `vulkan/api/vulkan.api` no AOSP define classes internas (`@internal class`) que representam a abstração de objetos Vulkan dentro do Loader, como:

<table>
  <thead>
    <tr>
      <th>Estrutura Interna</th>
      <th>Membros Chave</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>@internal class<br>BufferObject</td>
      <td>VkDevice device, VkDeviceMemory memory,<br>VkDeviceSize memoryOffset</td>
      <td>Abstração de um buffer Vulkan, ligando-o ao dispositivo, memória alocada e offset [6].</td>
    </tr>
    <tr>
      <td>@internal class<br>BufferViewObject</td>
      <td>VkDevice device, VkBuffer buffer, VkFormat format, VkDeviceSize offset, VkDeviceSize range</td>
      <td>Abstração de uma view de buffer, especificando o buffer subjacente, formato e região de memória [6].</td>
    </tr>
  </tbody>
</table>

# Referências

[1] Vulkan | Android Open Source Project [2] Graphics architecture | Android Open Source Project [3] Implement Vulkan | Android Open Source Project [4] Native Hardware Buffer - NDK - Android Developers [5] Command Buffers :: Vulkan Documentation Project [6] vulkan/api/vulkan.api - platform/frameworks/native - Git at Google [7] vkCreateGraphicsPipelines(3) - Khronos Registry [8] Pipeline Cache - Vulkan Documentation [9] Descriptor Sets [10] platform/external/deqp-deps/SPIRV-Tools - Git at Google [11] KhronosGroup/SPIRV-Cross

---

# Componente 24: Keystore - Key generation, attestation, hardware-backed keys, TEE

Itens Técnicos Encontrados: 15

**Conceitos-Chave:** Trusted Execution Environment (TEE), StrongBox, KeyMint HAL, AndroidKeyStore, keystore daemon, Binder API, keyblob, X.509, OID 1.3.6.1.4.1.11129.2.1.17, KeyGenParameterSpec, ECDSA, RSA, RFC 5280, hardwareEnforced, Marshalling/Unmarshalling

# Keystore: Geração de Chaves, Atestado e Hardware-Backed Keys no Android AOSP

O sistema **Keystore** do Android, no contexto do Android Open Source Project (AOSP), é um componente de segurança fundamental projetado para fornecer um contêiner seguro para chaves criptográficas. Sua arquitetura é construída para aproveitar componentes de hardware seguro, como o **Trusted Execution Environment (TEE)** ou **StrongBox**, garantindo que o material da chave permaneça protegido contra extração e manipulação pelo sistema operacional principal (Rich Execution Environment - REE) [1].

## Arquitetura e Componentes de Segurança

A arquitetura do Keystore é dividida em camadas que interagem para fornecer serviços criptográficos seguros. O sistema atua como uma ponte entre as APIs de alto nível do Android e o hardware seguro subjacente.

---


## Page 51

<table>
  <thead>
    <tr>
      <th>Componente</th>
      <th>Tipo</th>
      <th>Função Técnica</th>
      <th>Protocolo/API</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AndroidKeyStore</td>
      <td>API (Java)</td>
      <td>Implementação das APIs padrão Java Cryptography Architecture (JCA), com extensões específicas do Android, servindo como interface de alto nível para aplicativos.</td>
      <td>JCA, KeyGenParameterSpec</td>
    </tr>
    <tr>
      <td>keystore daemon</td>
      <td>Serviço (Sistema)</td>
      <td>Gerencia o acesso ao Keystore, armazena os keyblobs criptografados e encaminha requisições criptográficas para a camada HAL.</td>
      <td>Binder API</td>
    </tr>
    <tr>
      <td>KeyMint HAL</td>
      <td>Hardware Abstraction Layer</td>
      <td>API de baixo nível (sucessora do Keymaster) que delega operações criptográficas sensíveis a um Trusted Application (TA) no TEE.</td>
      <td>KeyMint API</td>
    </tr>
    <tr>
      <td>TEE / StrongBox</td>
      <td>Hardware Seguro</td>
      <td>Executa operações criptográficas seguras (geração, uso, atestado) em um ambiente isolado, garantindo a integridade e a confidencialidade do material da chave.</td>
      <td>Protocolo de Marshalling/Unmarshalling (KeyMint/TA)</td>
    </tr>
  </tbody>
</table>

O keystore daemon armazena o material secreto da chave em uma estrutura de dados conhecida como **keyblob**. Este **keyblob** é criptografado de tal forma que o *daemon* pode armazená-lo, mas não pode usá-lo ou revelá-lo, sendo o uso restrito ao TEE/StrongBox [1].

## Geração de Chaves e Algoritmos

A geração de chaves é controlada pela API AndroidKeyStore, que utiliza a classe **KeyGenParameterSpec** para definir os parâmetros da chave, incluindo seu propósito (**KeyPurpose**: :SIGN, **KeyPurpose**: :VERIFY), validade (**Tag**: :ACTIVE_DATETIME, **Tag**: :USAGE_EXPIRE_DATETIME) e, crucialmente, se a chave deve ser *hardware-backed* [1].

O KeyMint HAL suporta um conjunto básico de primitivas criptográficas, permitindo a implementação de protocolos que utilizam chaves com controle de acesso e suporte de hardware. Os algoritmos de assinatura e criptografia suportados incluem **ECDSA** (para chaves EC) e **RSA** (para chaves RSA), que são utilizados tanto para as chaves geradas quanto para as chaves de atestado [2].

## Protocolo de Atestado de Chaves

O **Atestado de Chaves (Key Attestation)** é um protocolo de segurança que permite a um aplicativo ou serviço remoto verificar de forma robusta as propriedades de um par de chaves assimétricas, incluindo se ele é suportado por hardware seguro e quais restrições de uso lhe foram impostas [2].

O atestado é fornecido na forma de um certificado X.509 padrão, conforme definido pela RFC 5280, que inclui uma extensão crítica de atestado.

## Estrutura de Dados do Certificado de Atestado

O certificado X.509 de atestado possui campos fixos e variáveis, garantindo a conformidade e a rastreabilidade.

---


## Page 52

<table>
  <thead>
    <tr>
      <th>Campo do Certificado (RFC 5280)</th>
      <th>Valor Técnico</th>
      <th>Estrutura de Dados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>version</td>
      <td>INTEGER 2 (Certificado v3)</td>
      <td>TBSCertificate SEQUENCE</td>
    </tr>
    <tr>
      <td>serialNumber</td>
      <td>INTEGER 1 (Valor fixo)</td>
      <td>TBSCertificate SEQUENCE</td>
    </tr>
    <tr>
      <td>subject</td>
      <td>CN = “Android Keystore Key” (Valor fixo)</td>
      <td>TBSCertificate SEQUENCE</td>
    </tr>
    <tr>
      <td>signatureAlgorithm</td>
      <td>Identificador do algoritmo (ECDSA ou RSA) usado para assinar a chave.</td>
      <td>Certificado</td>
    </tr>
    <tr>
      <td>validity</td>
      <td>SEQUENCE de duas datas: Tag::ACTIVE_DATETIME e Tag::USAGE_EXPIRE_DATETIME .</td>
      <td>TBSCertificate SEQUENCE</td>
    </tr>
    <tr>
      <td>Extensão de Atestado</td>
      <td>OID: 1.3.6.1.4.1.11129.2.1.17</td>
      <td>OCTET_STRING contendo uma SEQUENCE DER-codificada.</td>
    </tr>
  </tbody>
</table>

A extensão de atestado é o componente mais crítico, pois contém informações detalhadas sobre o par de chaves atestado e o estado do dispositivo no momento da geração da chave. Dentro desta extensão, o campo hardwareEnforced é preenchido exclusivamente pelo TEE/StrongBox. Este mecanismo garante que as propriedades de segurança da chave (como restrições de uso) são impostas pelo hardware seguro, e não podem ser falsificadas pelo sistema operacional principal [2].

O certificado é assinado por uma **chave de atestado** certificada, que pode ser diferente da chave atestada. O método **attestKey** é uma operação de chave pública que pode ser invocada a qualquer momento, independentemente das restrições de autorização da chave atestada [2].

---

## Referências

[1] Hardware-backed Keystore. Android Open Source Project. Disponível em: https://source.android.com/docs/security/features/keystore .
[2] Key and ID attestation. Android Open Source Project. Disponível em: https://source.android.com/docs/security/features/keystore/attestation .

---

## Componente 25: Permissions Android - Runtime permissions, permission groups, special permissions

Itens Técnicos Encontrados: 13

Conceitos-Chave: NEARBY_WIFI_DEVICES, Local Network Protection (LNP), Permissões Granulares de Saúde, BODY_SENSORS, RESTRICT_LOCAL_NETWORK, PermissionController, Hard/Soft Restrictions, revokeSelfPermissionsOnKill

## Conteúdo Técnico: Permissions Android (Android 16 AOSP)

O modelo de permissões do Android 16 (API 36) mantém a arquitetura de permissões de tempo de execução (*runtime permissions*) introduzida no Android 6.0, mas implementa mudanças significativas em protocolos de acesso à rede e estruturas de dados para permissões sensíveis, como as de saúde. O foco técnico reside na arquitetura de aplicação de restrições e na granularidade das novas APIs de permissão.

### 1. Arquitetura de Aplicação de Permissões de Tempo de Execução

A arquitetura central de permissões de tempo de execução é mantida, distinguindo entre **Permissões Perigosas** (concedidas em *runtime* pelo usuário) e **Permissões Normais** (concedidas em *install-time* pelo sistema) [1].

---


## Page 53

# Estruturas e Protocolos de Controle

*   **Separação de Módulos (Android 10+):** O processo de instalação (Package Installer) é separado da concessão de permissões (Permission Controller), garantindo que a lógica de permissão seja centralizada e modularizada [1].
*   **Restrições Rígidas e Suaves (Hard and Soft Restrictions):** Permissões restritas devem ser allowlisted (incluídas em uma lista de permissões) pelo instalador (ex: Google Play Store) ou pelo sistema.
    *   **Restrições Rígidas:** Impedem a concessão de permissões não allowlisted.
    *   **Restrições Suaves:** O comportamento de permissões não allowlisted é definido pela documentação pública da permissão específica [1].
*   **API de Revogação Assíncrona (Android 13+):** A API Context.revokeSelfPermissionsOnKill() permite que um aplicativo revogue suas próprias permissões concedidas. O algoritmo de revogação é assíncrono e acionado quando é seguro, resultando no encerramento de todos os processos em execução no UID de chamada [1].
*   **APIs de Gerenciamento de Grupos:** O sistema utiliza PackageManager.getGroupOfPlatformPermission e PackageManager.getPlatformPermissionsForGroup para gerenciar a associação de permissões a grupos, embora a UI de configurações trate a revogação por grupo [1].

## 2. Local Network Protection (LNP) - Android 16

O projeto LNP introduz uma nova permissão de tempo de execução para proteger a privacidade do usuário, restringindo o acesso implícito à rede local [2].

### Nova Permissão e Estrutura

*   **Permissão de Tempo de Execução:** NEARBY_WIFI_DEVICES (requerida no manifest do aplicativo) [2].
*   **Mecanismo de Restrição (Algoritmo):** A restrição é implementada profundamente na pilha de rede (deep in the networking stack), aplicando-se a todas as APIs de rede (sockets nativos ou gerenciados, bibliotecas como Cronet e OkHttp) [2].
*   **Protocolos Afetados:** O tráfego para e de um endereço de rede local requer a permissão. Isso inclui:
    *   Conexões TCP de saída e entrada.
    *   Envio e recebimento de UDP (unicast, multicast, broadcast) [2].
    *   Resolução de serviços na rede local (ex: mDNS, SSDP) [2].
*   **Códigos de Erro:** Tentativas de acesso não autorizado resultam em erros de socket, como EPERM (Operation not permitted) ou ECONNABORTED [2].

### Definição Técnica de Rede Local (LAN)

A restrição é aplicada a endereços IP que se enquadram nas seguintes faixas, consideradas redes locais [2]:

---


## Page 54

<table>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Faixa de Endereço</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPv4</td>
      <td>169.254.0.0/16</td>
      <td>Link Local</td>
    </tr>
    <tr>
      <td>IPv4</td>
      <td>100.64.0.0/10</td>
      <td>CGNAT</td>
    </tr>
    <tr>
      <td>IPv4</td>
      <td>10.0.0.0/8</td>
      <td>RFC1918 (Privado Classe A)</td>
    </tr>
    <tr>
      <td>IPv4</td>
      <td>172.16.0.0/12</td>
      <td>RFC1918 (Privado Classe B)</td>
    </tr>
    <tr>
      <td>IPv4</td>
      <td>192.168.0.0/16</td>
      <td>RFC1918 (Privado Classe C)</td>
    </tr>
    <tr>
      <td>IPv4</td>
      <td>255.255.255.255</td>
      <td>Endereço de Broadcast</td>
    </tr>
    <tr>
      <td>IPv6</td>
      <td>Link-local</td>
      <td>Endereços de Link-local</td>
    </tr>
    <tr>
      <td>IPv6</td>
      <td>ff00::/8</td>
      <td>Endereços Multicast</td>
    </tr>
    <tr>
      <td>IPv6</td>
      <td>Rotas Conectadas Diretamente</td>
      <td>Rotas diretamente conectadas</td>
    </tr>
    <tr>
      <td>IPv6</td>
      <td>Redes Stub (ex: Thread)</td>
      <td>Redes Stub</td>
    </tr>
  </tbody>
</table>

# 3. Permissões Granulares de Saúde (Health and Fitness)

O Android 16 introduz uma migração de permissões amplas para um modelo mais granular para dados de saúde e fitness, alinhado com o Health Connect [3].

## Estrutura de Dados e APIs Afetadas

*   **Estrutura de Permissão:** Migração de BODY_SENSORS e BODY_SENSORS_BACKGROUND para permissões mais específicas sob o namespace android.permissions.health [3].
*   **Novas Permissões Granulares:**
    *   READ_HEART_RATE : Para monitoramento de frequência cardíaca (while-in-use) [3].
    *   READ_HEALTH_DATA_IN_BACKGROUND : Para acesso a sensores em segundo plano [3].
*   **APIs e Tipos de Serviço Afetados:**
    *   HEART_RATE_BPM (Health Services no Wear OS).
    *   Sensor.TYPE_HEART_RATE (Android Sensor Manager).
    *   FOREGROUND_SERVICE_TYPE_HEALTH (requer a permissão android.permission.health correspondente em vez de BODY_SENSORS ) [3].

## Referências

[1] Runtime permissions - Android Open Source Project. [2] Local network permission - Privacy - Android Developers. [3] Behavior changes: Apps targeting Android 16 or higher - Android Developers.

# Componente 26: Sandbox Android - UID isolation, SELinux contexts, seccomp filters

**Itens Técnicos Encontrados:** 9

**Conceitos-Chave:** UID isolation, SELinux, seccomp-bpf, Mandatory Access Control (MAC), Discretionary Access Control (DAC), Android ID (AID), Berkeley Packet Filter (BPF), SEPolicy, AID_USER_OFFSET

O Sandbox Android é a fundação da arquitetura de segurança do sistema operacional, implementando o princípio de **isolamento de processos e privilégio mínimo** através de uma combinação de mecanismos do kernel Linux e políticas de segurança

---


## Page 55

específicas do Android.

## 1. Isolamento de UID (User ID)

O isolamento de UID é o primitivo de segurança fundamental para o sandboxing de aplicativos no Android.

### Estruturas de Dados e Algoritmos

*   **UID Único por Aplicativo (DAC):** Cada aplicativo é executado com um **UID (User ID) UNIX** exclusivo, que é o principal de segurança para o aplicativo [1]. Isso simplifica a verificação de permissões e elimina a necessidade de verificações por PID (Process ID), que são mais suscetíveis a race conditions [1].
*   **Android ID (AID):** Para suportar múltiplos usuários e perfis em um único dispositivo, o Android utiliza o conceito de **Android ID (AID)**. O AID é uma combinação do UID do aplicativo e um offset do usuário do dispositivo.
    *   **Fórmula de Atribuição de UID:** O UID de um aplicativo é determinado dentro de um intervalo definido, relativo a um offset de usuário: $UID_{app} = AID_{USER_OFFSET} + UID_{base} onde AID{USER_OFFSET} é tipicamente 100000e UID{base} está no intervalo de 10000a19999(de AID{APP_START}a AID{APP_END})$ [1].
*   **Estrutura de Armazenamento de Permissões:** As permissões concedidas a um aplicativo são armazenadas em um local centralizado no sistema de arquivos, especificamente em `/data/system/packages.xml` [1].

## 2. Contextos SELinux (Mandatory Access Control - MAC)

O SELinux (Security-Enhanced Linux) implementa o **Controle de Acesso Obrigatório (MAC)**, que complementa o DAC do UID, fornecendo uma granularidade de isolamento mais fina, mesmo entre processos que compartilham o mesmo UID [1].

### Arquitetura e Protocolos

*   **Princípio Default-Deny:** O SELinux opera sob o princípio de **default-deny**, onde apenas ações explicitamente permitidas pela política são autorizadas [4].
*   **Estrutura da Política (SEPolicy):** A política SELinux (SEPolicy) não é monolítica. Ela é construída em tempo de inicialização a partir de diferentes partições (atualmente system e vendor ) [1]. Isso permite que as atualizações de política para componentes de plataforma e hardware sejam feitas de forma independente (mecanismo introduzido com o Project Treble) [1].
*   **Contextos SELinux:** São rótulos (tags) aplicados a processos e objetos (como arquivos, sockets, dispositivos) que definem o tipo de acesso permitido. A política SELinux é um conjunto de regras que governam as interações entre esses contextos.

## 3. Filtros seccomp (Secure Computing)

Os filtros seccomp (Secure Computing) fornecem uma camada adicional de defesa, limitando as chamadas de sistema (syscalls) que um processo pode executar, reduzindo drasticamente a superfície de ataque do kernel [3].

### Algoritmos e APIs

*   **Protocolo seccomp-bpf:** O Android utiliza o **seccomp-bpf** (seccomp com Berkeley Packet Filter) [3]. O BPF é um protocolo/linguagem de bytecode que permite que um processo defina um filtro para as chamadas de sistema recebidas [2].
*   **Estrutura do Filtro:** O filtro é expresso como um programa **BPF** [2]. Este programa é carregado no kernel e executado para cada chamada de sistema. O programa BPF decide se a chamada deve ser permitida, negada, ou se deve acionar um sinal (como SIGSYS) [2].
*   **API:** A API do kernel Linux utilizada para aplicar o filtro é a chamada de sistema `seccomp()` [2]. Desde o Android 8.0, todos os aplicativos são executados com um filtro seccomp-bpf que restringe as syscalls permitidas, fortalecendo a fronteira entre o aplicativo e o kernel [3].

---


## Page 56

<table>
  <thead>
    <tr>
      <th>Mecanismo</th>
      <th>Camada de Implementação</th>
      <th>Princípio Técnico</th>
      <th>Estrutura/Protocolo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>UID Isolation</td>
      <td>Kernel Linux (DAC)</td>
      <td>Isolamento de Processo</td>
      <td>AID (Android ID), AID_USER_OFFSET, /data/system/packages.xml</td>
    </tr>
    <tr>
      <td>SELinux Contexts</td>
      <td>Kernel Linux (MAC)</td>
      <td>Controle de Acesso Obrigatório</td>
      <td>SEPolicy (system/vendor), Default-deny</td>
    </tr>
    <tr>
      <td>seccomp filters</td>
      <td>Kernel Linux (Sandboxing)</td>
      <td>Restrição de Syscall</td>
      <td>seccomp-bpf, Berkeley Packet Filter (BPF)</td>
    </tr>
  </tbody>
</table>

## Referências

[1] The Android Platform Security Model (2023) [https://arxiv.org/html/1904.05572v3]
[2] Seccomp BPF (SECure COMPUTing with filters) [https://www.kernel.org/doc/html/v4.19/userspace-api/seccomp_filter.html]
[3] Application Sandbox | Android Open Source Project [https://source.android.com/docs/security/app-sandbox]
[4] Understanding SELinux in Android AOSP: Security at its ... [https://medium.com/@samirdubey/understanding-selinux-in-android-aosp-security-at-its-core-part-1-e398c79f8253]

---

# PARTE 2: PESQUISADORES E TEORIAS

## Pesquisador 1: Andy Rubin

**Itens Técnicos Encontrados:** 10

**Contribuições:** Máquina Virtual Dalvik, Arquitetura Baseada em Registradores, Formato DEX, Processo Zygote, Protocolo Binder, Copy-on-Write, Sandboxing de Aplicações

## Fundamentos Técnicos da Arquitetura Inicial do Android

A arquitetura inicial do Android, desenvolvida sob a liderança de Andy Rubin, foi fundamentalmente moldada pela necessidade de operar em dispositivos móveis com recursos severamente limitados, uma filosofia de design que impôs restrições técnicas específicas. O sistema operacional foi concebido para suportar velocidade de processador e RAM limitadas, ausência de espaço de troca (*no swap space*), operação alimentada por bateria e um ambiente de execução de aplicações isolado (*sandboxed*).

## Máquina Virtual Dalvik (DVM) e Arquitetura Baseada em Registradores

O componente central do *runtime* de aplicação inicial do Android foi a **Máquina Virtual Dalvik (DVM)**. Em contraste com a arquitetura baseada em pilha (*stack-based*) da Java Virtual Machine (JVM), a DVM foi projetada com uma **arquitetura baseada em registradores (*register-based*)**. Esta escolha arquitetônica é uma otimização técnica crítica para dispositivos com memória restrita, pois permite um consumo mínimo de memória para o *footprint* da VM.

A DVM opera sobre o **Kernel Linux**, utilizando-o para funcionalidades de sistema operacional de baixo nível, como *threading* e gerenciamento de memória. Um conceito fundamental de arquitetura de sistemas é que cada aplicação Android é executada em seu próprio processo, com sua própria instância da DVM, garantindo o isolamento e a estabilidade.

## Formato de Arquivo DEX (Dalvik Executable)

Para complementar a DVM, foi introduzido o formato de arquivo **Dalvik Executable (.dex)**. Este formato representa uma otimização técnica primária para uso de memória e compartilhamento de dados. Enquanto o código-fonte Java é compilado em arquivos *.class* (bytecode Java), a ferramenta *dx* é utilizada para converter esses arquivos em um único arquivo *.dex*.

---


## Page 57

A principal distinção técnica é que um arquivo .dex consolida múltiplas classes em uma única estrutura, ao contrário do formato .class que contém apenas uma. Essa consolidação e otimização de bytecode são cruciais para reduzir a sobrecarga de E/S (Entrada/Saída) e o consumo de memória em dispositivos móveis.

## Processo Zygote e Mecanismo Copy-on-Write

O **Processo Zygote** é um conceito de sistema operacional que serve como a raiz de todos os processos de sistema e de aplicação. Seu mecanismo técnico é um *forking* otimizado, projetado para acelerar o lançamento de aplicações.

Ao iniciar, o Zygote pré-carrega as classes e recursos essenciais do framework Android (incluindo a DVM/ART). Quando uma nova aplicação é solicitada, o Zygote realiza um *fork* de si mesmo. O processo filho resultante herda o espaço de endereçamento de memória pré-inicializado do Zygote. Este mecanismo explora o princípio do **Copy-on-Write (CoW)** do kernel Linux, permitindo que o novo processo compartilhe as páginas de memória do Zygote até que uma escrita seja necessária, resultando em um lançamento de aplicação significativamente mais rápido e eficiente em termos de memória.

## Protocolo Binder para Comunicação Interprocessos (IPC)

O **Protocolo Binder** é o mecanismo de Comunicação Interprocessos (IPC) de alto desempenho e baixa latência que atua como o espinha dorsal da arquitetura do Android. Implementado diretamente no kernel Linux, o Binder é mais eficiente do que os mecanismos IPC tradicionais do Linux (como *pipes* ou *sockets*).

O protocolo facilita chamadas de procedimento remoto (RPC) entre processos isolados, permitindo que componentes do sistema e aplicações se comuniquem de forma segura. A interface de comunicação é definida usando a **Android Interface Definition Language (AIDL)**, que garante uma comunicação type-safe e estruturada. A transferência de dados é realizada através de uma estrutura de dados de transação (*binder transaction data*), que é mapeada para a memória compartilhada, minimizando a cópia de dados entre os espaços de endereço do kernel e do usuário.

## Resumo dos Conceitos Técnicos

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Tipo</th>
      <th>Função Primária</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Máquina Virtual Dalvik (DVM)</td>
      <td>Arquitetura de Sistema</td>
      <td>Ambiente de execução otimizado para recursos limitados.</td>
    </tr>
    <tr>
      <td>Arquitetura Baseada em Registradores</td>
      <td>Algoritmo/Estrutura</td>
      <td>Otimização de VM para consumo mínimo de memória.</td>
    </tr>
    <tr>
      <td>Formato DEX</td>
      <td>Estrutura de Dados</td>
      <td>Formato de arquivo de bytecode consolidado e otimizado para E/S e memória.</td>
    </tr>
    <tr>
      <td>Processo Zygote</td>
      <td>Conceito de SO/Mecanismo</td>
      <td>Pré-carregamento de classes e *forking* otimizado para lançamento rápido de apps.</td>
    </tr>
    <tr>
      <td>Copy-on-Write (CoW)</td>
      <td>Conceito de SO/Algoritmo</td>
      <td>Mecanismo de compartilhamento de memória para eficiência no *forking* do Zygote.</td>
    </tr>
    <tr>
      <td>Protocolo Binder</td>
      <td>Protocolo/Arquitetura IPC</td>
      <td>Comunicação Interprocessos de alto desempenho e baixa latência.</td>
    </tr>
    <tr>
      <td>AIDL</td>
      <td>Protocolo/Linguagem de Definição</td>
      <td>Definição de interface type-safe para comunicação RPC via Binder.</td>
    </tr>
    <tr>
      <td>Sandboxing de Aplicações</td>
      <td>Conceito de SO/Segurança</td>
      <td>Isolamento de processos para segurança e estabilidade do sistema.</td>
    </tr>
    <tr>
      <td>Kernel Linux</td>
      <td>Arquitetura de Sistema/SO</td>
      <td>Base para *threading*, gerenciamento de memória e *drivers* de hardware.</td>
    </tr>
    <tr>
      <td>Gerenciamento de Memória (Low-level)</td>
      <td>Conceito de SO</td>
      <td>Uso do kernel Linux para lidar com a ausência de *swap* e RAM limitada.</td>
    </tr>
  </tbody>
</table>

---


## Page 58

# Pesquisador 2: Linus Torvalds

**Itens Técnicos Encontrados:** 15

**Contribuições:** Escalonador Round-Robin v0.01, Estrutura de Dados Array de Tarefas, Conceito Nice Value, Algoritmo Weighted Fair Queueing (WFQ), Estrutura Árvore Rubro-Negra (CFS), Conceito Virtual Runtime (vruntime), Estrutura vm_area_struct (VMA), Algoritmo Buddy System, Conceito Slab Allocator

## Conteúdo Técnico: Contribuições de Linus Torvalds ao Kernel Linux (Escalonamento e Gerenciamento de Memória)

O conteúdo técnico a seguir foca exclusivamente em algoritmos, estruturas de dados, protocolos e conceitos de sistemas operacionais, conforme solicitado.

### 1. Escalonamento de Processos (Scheduler)

#### 1.1. Escalonador Inicial (v0.01)

O escalonador original, implementado por Linus Torvalds na versão 0.01 do kernel Linux, era notavelmente simples e direto:

*   **Algoritmo:** Escalonamento *Round-Robin* (circular) simples.
*   **Estrutura de Dados:** Um array de tarefas (*task*) de tamanho fixo (máximo de 64 entradas), que servia como a fila de execução (*run queue*).
*   **Conceito de SO:** Time Slice (fatia de tempo) fixo de 150 milissegundos, monitorado por um *interval timer* que interrompia a CPU a cada 10 milissegundos.
*   **Algoritmo de Seleção:** O escalonador percorria a fila de execução em ordem reversa, selecionando o primeiro processo executável que ainda possuía um time slice positivo.
*   **Mecanismo de Reset:** Quando todos os processos executáveis esgotavam seu time slice, todos os time slices eram resetados. Processos executáveis recebiam 150ms. Processos em espera (*sleeping tasks*) recebiam um bônus de time slice (metade do time slice atual) para favorecer a interatividade.
*   **Conceito de SO:** Nice Value (valor de *nice*) implementado para modificar o time slice de uma tarefa, permitindo a priorização.

#### 1.2. Completely Fair Scheduler (CFS) - Conceitos Fundamentais

Embora o CFS tenha sido desenvolvido por Ingo Molnar, ele representa a arquitetura de escalonamento moderna do kernel Linux, que evoluiu a partir das bases estabelecidas por Torvalds e seus colaboradores. Os conceitos centrais são:

*   **Algoritmo:** Implementação de *Weighted Fair Queueing* (WFQ), que busca a justiça (*fairness*) na distribuição do tempo de CPU.
*   **Estrutura de Dados:** Árvore Rubro-Negra (*Red-Black Tree*) auto-balanceada, utilizada para manter a fila de execução (*run queue*). Esta estrutura garante que as operações de inserção e remoção de tarefas ocorram em tempo *O(log n)*.
*   **Estrutura de Dados:** Objeto *sched_entity* (entidade de escalonamento), que encapsula a tarefa e contém os dados de escalonamento.
*   **Conceito de SO:** Virtual Runtime (*vruntime*), um contador que rastreia o tempo de execução “ideal” de uma tarefa. O *vruntime* é incrementado pelo tempo de execução real, ponderado pelo peso da tarefa (derivado do valor de *nice*).
*   **Algoritmo de Seleção:** O processo a ser escalonado é sempre o nó mais à esquerda da Árvore Rubro-Negra, pois ele representa a tarefa com o menor *vruntime* (a mais “atrasada” ou a que recebeu menos tempo de CPU).

### 2. Gerenciamento de Memória (Memory Management)

O gerenciamento de memória no kernel Linux é baseado em conceitos de sistemas operacionais que Linus Torvalds implementou e aprimorou:

*   **Algoritmo:** Buddy System, que divide blocos de memória em partes iguais, permitindo a alocação de blocos menores.
*   **Estrutura de Dados:** Estrutura *vm_area_struct* (VMA), que representa uma área de memória virtual.
*   **Conceito de SO:** Slab Allocator, um mecanismo eficiente para alocar e liberar blocos de memória.
*   **Estrutura de Dados:** Estrutura *vm_area_struct* (VMA), que encapsula a tarefa e contém os dados de escalonamento.
*   **Conceito de SO:** Virtual Runtime (*vruntime*), um contador que rastreia o tempo de execução “ideal” de uma tarefa. O *vruntime* é incrementado pelo tempo de execução real, ponderado pelo peso da tarefa (derivado do valor de *nice*).
*   **Algoritmo de Seleção:** O processo a ser escalonado é sempre o nó mais à esquerda da Árvore Rubro-Negra, pois ele representa a tarefa com o menor *vruntime* (a mais “atrasada” ou a que recebeu menos tempo de CPU).

### 3. Outros Conceitos e Estruturas

*   **Conceito de SO:** Nice Value (valor de *nice*) implementado para modificar o time slice de uma tarefa, permitindo a priorização.
*   **Estrutura de Dados:** Estrutura *vm_area_struct* (VMA), que encapsula a tarefa e contém os dados de escalonamento.
*   **Conceito de SO:** Virtual Runtime (*vruntime*), um contador que rastreia o tempo de execução “ideal” de uma tarefa. O *vruntime* é incrementado pelo tempo de execução real, ponderado pelo peso da tarefa (derivado do valor de *nice*).
*   **Algoritmo de Seleção:** O processo a ser escalonado é sempre o nó mais à esquerda da Árvore Rubro-Negra, pois ele representa a tarefa com o menor *vruntime* (a mais “atrasada” ou a que recebeu menos tempo de CPU).

### 4. Conclusão

A contribuição de Linus Torvalds ao kernel Linux foi fundamental para o desenvolvimento de algoritmos, estruturas de dados, protocolos e conceitos de sistemas operacionais, especialmente no que diz respeito ao escalonamento de processos e gerenciamento de memória. Sua visão pioneira e constante busca pela eficiência e justiça no uso dos recursos computacionais continua sendo uma fonte de inspiração para pesquisadores e engenheiros de sistemas operacionais.

---


## Page 59

*   **Conceito de SO:** Memória Virtual e Paginação, onde o kernel gerencia a memória em unidades de páginas (tipicamente 4KB).
*   **Estrutura de Dados:** `vm_area_struct` (VMA), que descreve uma área contígua de memória virtual de um processo, incluindo direitos de acesso (leitura, escrita, execução) e operações associadas.
*   **Estrutura de Dados:** Page Frame Number (PFN), um número que identifica unicamente um page frame físico na memória RAM.
*   **Conceito de SO:** Page Fault (falha de página) e Demand Paging (Paginação sob Demanda), mecanismos para carregar páginas de memória no momento em que são acessadas.
*   **Algoritmo/Estrutura:** Buddy System (Sistema Buddy), um algoritmo de alocação de memória física que gerencia blocos de memória de tamanhos potências de dois para combater a fragmentação externa.
*   **Algoritmo/Estrutura:** Slab Allocator (Alocador Slab), um mecanismo de cache de objetos do kernel para alocação eficiente de estruturas de dados pequenas e frequentemente usadas (como `task_struct` ou `inode`), reduzindo a sobrecarga do Buddy System e a fragmentação interna.

## 3. Arquitetura de Sistemas

*   **Conceito de SO:** Processos e Threads Unificados: O kernel Linux trata processos e threads como entidades de escalonamento semelhantes, diferenciando-os apenas pelo grau de compartilhamento de recursos (código e/ou dados). Ambos são representados pela estrutura `task_struct`.
*   **Conceito de SO:** Kernel Monolítico, onde todos os serviços principais do sistema operacional (escalonador, gerenciamento de memória, drivers) residem no mesmo espaço de endereçamento, garantindo comunicação rápida, mas exigindo maior rigor no desenvolvimento.

---

## Pesquisador 3: Andrew Morton (Linux kernel maintainer)

**Itens Técnicos Encontrados:** 10

**Contribuições:** Reverse Mapping (rmap), pagevecs, MGLRU, mm tree, Page Replacement Policy

As contribuições técnicas de **Andrew Morton** para o kernel Linux, especialmente no subsistema de gerenciamento de memória (MM), concentram-se em algoritmos, estruturas de dados e conceitos de arquitetura de sistemas operacionais que visam aprimorar a escalabilidade, o desempenho e a estabilidade do kernel. Embora Morton seja primariamente um mantenedor e integrador, seu trabalho envolve a supervisão e o aprimoramento de implementações técnicas cruciais.

### Algoritmos e Estruturas de Dados

#### 1. Reverse Mapping (rmap)

O Reverse Mapping (rmap) é um conceito fundamental no gerenciamento de memória virtual do Linux, crucial para o processo de *page reclamation* (recuperação de páginas). O rmap resolve o problema de descobrir quais Page Table Entries (PTEs) apontam para uma determinada página física quando o kernel precisa desalocá-la ou movê-la.

*   **Conceito:** A capacidade de mapear uma página física de volta para todas as entradas de tabela de páginas virtuais que a referenciam.
*   **Estrutura de Dados:** O rmap utiliza estruturas de dados para manter uma lista de referências de mapeamento reverso para cada `struct page`. Isso permite que o kernel encontre e invalide eficientemente todas as referências virtuais a uma página física antes de desalocá-la.

#### 2. Pagevecs

O pagevec é uma otimização de estrutura de dados e algoritmo introduzida por Morton para reduzir a contenção de bloqueio (lock contention) em operações de página.

*   **Estrutura de Dados:** Um vetor (ou lista) de páginas (do tipo `struct page`) que permite que operações de gerenciamento de memória, como a liberação de páginas, sejam agrupadas e processadas em lote.

---


## Page 60

*   **Algoritmo:** Ao invés de adquirir e liberar um bloqueio para cada página individualmente, o kernel acumula páginas em um pagevec e processa o vetor inteiro de uma só vez, reduzindo drasticamente a sobrecarga de sincronização, especialmente em sistemas com múltiplos processadores e grandes quantidades de memória.

3. MGLRU (Multi-Generational Least Recently Used)

Embora o MGLRU tenha sido desenvolvido por outros colaboradores, sua integração e adoção foram supervisionadas por Morton como mantenedor do subsistema MM. O MGLRU é um algoritmo de substituição de páginas que visa melhorar a eficiência do LRU tradicional.

*   **Algoritmo:** Substitui o mecanismo de lista LRU de duas camadas por um sistema de múltiplas gerações. Páginas são classificadas em diferentes gerações com base em seu uso recente, permitindo que o kernel tome decisões mais informadas sobre quais páginas descartar.
*   **Conceito:** O MGLRU melhora o desempenho de sistemas com memória limitada e reduz a sobrecarga de varredura (scan overhead) do gerenciador de memória.

**Conceitos de Arquitetura de Sistemas Operacionais**

4. mm tree (Árvore de Desenvolvimento de Memória)

A mm tree (ou -mm tree ) é o repositório de patches mantido por Andrew Morton.

*   **Arquitetura de Sistemas:** Representa um estágio de teste e integração de patches de gerenciamento de memória antes de serem mesclados na linha principal do kernel (mainline).
*   **Conceito:** Serve como um ambiente de teste para patches instáveis ou em desenvolvimento, permitindo que o código seja amplamente testado e revisado por outros desenvolvedores antes de ser considerado estável o suficiente para Linus Torvalds.

5. Otimizações de Memória em Grande Escala

O trabalho de Morton frequentemente aborda a escalabilidade do gerenciamento de memória para máquinas com grandes quantidades de RAM.

*   **Conceito:** Otimizações em estruturas de controle do kernel para garantir que o aumento da memória física não resulte em um crescimento desproporcional das estruturas de dados internas do kernel, como as que gerenciam as **Huge Pages** (Páginas Enormes) e o **Slab Allocator** (alocador de objetos do kernel).

6. Estruturas de Gerenciamento de Páginas

O trabalho de manutenção de Morton envolve a constante otimização das estruturas de dados centrais do gerenciamento de memória.

*   **Estrutura de Dados:** `struct page`: A estrutura central que descreve cada página física de memória. As otimizações em seu tamanho e nos metadados que ela armazena são cruciais para a eficiência do kernel.
*   **Conceito:** Alocação de Memória Contígua: Correções e aprimoramentos nos mecanismos que garantem a alocação de blocos de memória fisicamente contíguos, essenciais para buffers de hardware e certas estruturas de dados do kernel.

Em resumo, o foco técnico do trabalho de Andrew Morton está na implementação prática e na otimização de **algoritmos de substituição de páginas**, na eficiência de **estruturas de mapeamento reverso** e na arquitetura de desenvolvimento que garante a estabilidade e a escalabilidade do subsistema de gerenciamento de memória do kernel Linux.

---

**Pesquisador 4: Ingo Molnar**

**Itens Técnicos Encontrados:** 9

**Contribuições:** Completely Fair Scheduler (CFS), Virtual Runtime (vruntime), Árvore Rubro-Negra (rbtree) para runqueues, PREEMPT_RT, Mutexes de Tempo Real (RT Mutexes), Herança de Prioridade (PI), Interrupções Threaded

---


## Page 61

# Conteúdo Técnico do Trabalho de Ingo Molnar

O trabalho de Ingo Molnar no kernel Linux abrange contribuições fundamentais para o escalonamento de processos e a capacidade de tempo real do sistema operacional, com foco no **Completely Fair Scheduler (CFS)** e no *patchset PREEMPT_RT* (Real-Time Preemption).

## Completely Fair Scheduler (CFS)

O CFS é o escalonador padrão para tarefas de propósito geral (*SCHED_OTHER*, *SCHED_BATCH*, *SCHED_IDLE*) no kernel Linux, implementando o conceito de **Fair Queuing** adaptado para escalonamento de processos.

### Algoritmos e Conceitos de Sistemas Operacionais

1.  **Modelo de CPU Multitarefa Ideal:** O CFS modela uma “CPU multitarefa ideal e precisa” (*Ideal, precise multi-tasking CPU*), onde cada tarefa recebe uma fatia de tempo de CPU proporcional ao seu peso (*nice value*), executando em paralelo a uma velocidade de $1/N$, onde $N$ é o número de tarefas executáveis.
2.  **Algoritmo de Escalonamento:** O CFS utiliza uma variação do algoritmo **Fair Queuing**, que busca garantir que o tempo de execução virtual (*vruntime*) de todas as tarefas seja mantido o mais próximo possível, promovendo uma distribuição justa do tempo de CPU.
3.  **Conceito de Virtual Runtime (*vruntime*):** É o tempo de execução real de uma tarefa normalizado pelo peso total das tarefas executáveis. É o principal conceito de justiça no CFS. O valor é rastreado pelo campo `p->se.vruntime` (em nanosegundos) na estrutura de dados da tarefa.
4.  **Fórmula de Atualização do *vruntime*:** O *vruntime* de uma tarefa é atualizado após sua execução pela seguinte relação: $vruntime \leftarrow vruntime + \Delta t \times \frac{nice_0_weight}{task_weight} \text{Onde}\Delta t \text{é o tempo real gastado na CPU}, nice_0_weight é o peso de uma tarefa com 'nice' 0 (padrão), etask_weight$ é o peso da tarefa atual (derivado do seu *nice value*). Tarefas com prioridade mais baixa (maior *nice value*, menor *task_weight*) têm seu *vruntime* aumentado mais rapidamente, forçando-as a ceder a CPU mais cedo.
5.  **Granularidade de Escalonamento (*sched_min_granularity_ns*):** Define o tempo mínimo que uma tarefa deve rodar antes de ser preemptada, minimizando a sobrecarga de *context switches*.
6.  **Latência de Escalonamento (*sched_latency_ns*):** O tempo máximo que uma tarefa deve esperar para rodar. É a granularidade mínima multiplicada pelo número de tarefas.

### Estruturas de Dados e Arquitetura

1.  **Árvore Rubro-Negra (Red-Black Tree - rbtree):** A principal estrutura de dados do CFS. As tarefas executáveis são armazenadas em uma *rbtree* ordenada pelo seu *vruntime*. A *rbtree* é uma árvore binária de busca auto-balanceada, garantindo que a tarefa com o menor *vruntime* (a próxima a ser executada) seja encontrada em tempo $O(\log N)$, onde $N$ é o número de tarefas executáveis.
2.  **Classes de Escalonamento (Scheduling Classes):** O CFS é implementado como uma classe de escalonamento (*fair_sched_class*), parte de uma arquitetura modular que permite que diferentes políticas de escalonamento (como CFS, Real-Time e Deadline) coexistam e sejam gerenciadas pelo núcleo do escalonador.

## PREEMPT_RT (Real-Time Preemption)

O *patchset PREEMPT_RT* transforma o kernel Linux em um kernel totalmente preemptivo e de tempo real, minimizando seções não-preemptíveis e garantindo latências previsíveis.

### Protocolos e Conceitos de Sistemas Operacionais

1.  **Protocolo de Herança de Prioridade (Priority Inheritance - PI):** Um protocolo de sincronização crucial para sistemas de tempo real. Ele resolve o problema de **inversão de prioridade** ao fazer com que uma tarefa de baixa prioridade que detém um recurso necessário por uma tarefa de alta prioridade herde temporariamente a prioridade da tarefa de alta prioridade.
2.  **Mutexes de Tempo Real (RT Mutexes):** A maioria dos *spinlocks* do kernel são substituídos por *mutexes* que suportam o protocolo PI. O *rt_mutex* é a estrutura de dados central para esta conversão.

---


## Page 62

3. **Spinlocks “Dorminhocos” (Sleeping Spinlocks):** No PREEMPT_RT, a maioria dos *spinlocks* são convertidos em *mutexes* de tempo real (*rt_mutex_base*), fazendo com que as tarefas que tentam adquirir um *spinlock* ocupado durmam (*sleep*) em vez de girar (*busy-wait*), o que permite a preempção.

4. **Interrupções Threaded (Threaded Interrupts):** A maioria dos *handlers* de interrupção são convertidos em *threads* de kernel de tempo real. Isso permite que o código do *handler* seja preemptível e sujeito ao escalonamento por prioridade, reduzindo a latência de interrupção.

5. **Conversão de Softirqs e Tasklets:** Mecanismos de adiamento de trabalho como *softirqs* e *tasklets* são convertidos em *threads* de kernel de tempo real para garantir que sejam preemptíveis e não bloqueiem tarefas de maior prioridade.

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Tipo</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Completely Fair Scheduler (CFS)</td>
      <td>Algoritmo/Arquitetura</td>
      <td>Escalonador de processos baseado em *Fair Queuing* e no modelo de CPU ideal.</td>
    </tr>
    <tr>
      <td>Virtual Runtime (vruntime)</td>
      <td>Conceito de SO</td>
      <td>Métrica de tempo de execução normalizada, usada como chave de ordenação para tarefas.</td>
    </tr>
    <tr>
      <td>Árvore Rubro-Negra (rbtree)</td>
      <td>Estrutura de Dados</td>
      <td>Estrutura auto-balanceada usada para armazenar e ordenar tarefas executáveis por vruntime em $O(\log N)$.</td>
    </tr>
    <tr>
      <td>PREEMPT_RT</td>
      <td>Arquitetura/Conceito de SO</td>
      <td>*Patchset* que torna o kernel Linux totalmente preemptível e de tempo real.</td>
    </tr>
    <tr>
      <td>Herança de Prioridade (PI)</td>
      <td>Protocolo</td>
      <td>Mecanismo de sincronização para evitar a inversão de prioridade em *mutexes* de tempo real.</td>
    </tr>
    <tr>
      <td>Mutexes de Tempo Real (rt_mutex)</td>
      <td>Estrutura de Dados/Conceito de SO</td>
      <td>Substituição de *spinlocks* por *mutexes* que suportam PI, permitindo que tarefas durmam em vez de girar.</td>
    </tr>
    <tr>
      <td>Interrupções Threaded</td>
      <td>Arquitetura/Conceito de SO</td>
      <td>Conversão de *handlers* de interrupção em *threads* de kernel preemptíveis.</td>
    </tr>
    <tr>
      <td>Classes de Escalonamento</td>
      <td>Arquitetura</td>
      <td>Estrutura modular que permite a coexistência de diferentes políticas de escalonamento (CFS, RT, Deadline).</td>
    </tr>
    <tr>
      <td>Fórmula de vruntime</td>
      <td>Algoritmo/Fórmula</td>
      <td>Relação matemática para calcular o tempo de execução virtual com base no peso da tarefa.</td>
    </tr>
  </tbody>
</table>

---

## Pesquisador 5: Peter Zijlstra

Itens Técnicos Encontrados: 9

Contribuições: EEVDF Scheduler, Adaptive Spin, RCU Boost, Preemptible RCU, Lockdep DAG Validation

## Contribuições Técnicas de Peter Zijlstra (Scheduler, Locking, RCU)

O trabalho de Peter Zijlstra no kernel Linux é focado em otimizações de escalonamento, sincronização e tempo real, introduzindo ou aprimorando algoritmos, estruturas de dados e conceitos de sistemas operacionais.

### 1. Escalonador (Scheduler)

#### 1.1. Earliest Eligible Virtual Deadline First (EEVDF)

O EEVDF é um algoritmo de escalonamento que substituiu o Completely Fair Scheduler (CFS) como o escalonador padrão no kernel Linux (a partir da versão 6.6). O objetivo principal é garantir uma distribuição de tempo de CPU mais justa e previsível, especialmente em cargas de trabalho mistas.

---


## Page 63

# Algoritmo e Conceitos:

*   **Virtual Runtime (vruntime):** O EEVDF, assim como o CFS, utiliza o conceito de *vruntime*, que acumula o tempo de execução de uma tarefa, escalado pelo seu peso (prioridade).
*   **Deadline Virtual:** O EEVDF introduz o conceito de um *deadline* virtual para cada tarefa, que é calculado com base no seu *vruntime* e no tempo de fatia alocado.
*   **Elegibilidade:** Uma tarefa se torna *elegível* para execução quando seu *vruntime* atinge um certo limite, garantindo que tarefas que receberam menos tempo de CPU sejam priorizadas.
*   **Seleção de Tarefa:** O algoritmo seleciona a tarefa *elegível* com o menor *deadline* virtual. Isso garante que as tarefas que estão mais “atrasadas” em relação ao seu tempo de CPU justo sejam executadas primeiro.

# Estrutura de Dados:

*   **Árvore Red-Black (rbtree):** O EEVDF mantém as tarefas executáveis em uma árvore Red-Black balanceada. Esta estrutura de dados permite operações de inserção, remoção e busca da tarefa com o menor *vruntime* (ou menor *deadline* virtual) em tempo logarítmico ($O(\log n)$), onde $n$ é o número de tarefas.

## 1.2. RT Balancer

Conceito de balanceamento de carga para tarefas de tempo real (FIFO/RR) em sistemas SMP (Symmetric Multiprocessing), garantindo que a invariante de tempo real seja mantida em múltiplos CPUs, respeitando *cpusets* e domínios raiz.

# 2. Sincronização (Locking)

## 2.1. Adaptive Spin (Giro Adaptativo)

### Algoritmo e Conceito:

*   **Otimização de Mutexes:** Introduzido para otimizar a aquisição de mutexes (exclusão mútua) em ambientes multi-core.
*   **Mecanismo:** Em vez de imediatamente colocar a tarefa em espera (dormir) quando um mutex está ocupado, a tarefa entra em um *loop de giro* (spinlock) por um curto período.
*   **Condição de Giro:** O giro só ocorre se o proprietário do mutex estiver atualmente em execução em outro CPU. Se o proprietário estiver bloqueado ou não estiver em execução, o giro é inútil e a tarefa é colocada para dormir (bloqueio).
*   **Benefício:** Evita a sobrecarga de uma troca de contexto (context switch) se o bloqueio for liberado rapidamente, melhorando a latência e o desempenho.

## 2.2. Lockdep (Validação de Grafo de Dependência de Bloqueio)

### Conceito de Sistema Operacional:

*   **Validação de DAG (Directed Acyclic Graph):** O lockdep é uma ferramenta de depuração em tempo de execução que rastreia as dependências de bloqueio.
*   **Objetivo:** Valida se o grafo de dependência de bloqueio (DAG) é acíclico, prevenindo **deadlocks** (impasses) ao garantir que os bloqueios sejam sempre adquiridos na mesma ordem.
*   **Estrutura de Dados:** Utiliza **classes de bloqueio** (baseadas no local de inicialização do bloqueio) e um grafo para mapear as ordens de aquisição.

# 3. RCU (Read-Copy Update)

## 3.1. Preemptible RCU

### Conceito de Sistema Operacional:

---


## Page 64

*   **Contexto:** O RCU tradicional depende da desativação de preempção ( `preempt_disable` ) para definir seções críticas de leitura.
*   **Preemptible RCU:** Modifica o RCU para funcionar em kernels com preempção total (como o `PREEMPT_RT`), onde a desativação de preempção não é suficiente para garantir a seção crítica de leitura.
*   **Mecanismo:** A seção crítica de leitura é definida por um par de chamadas de função que rastreiam o estado da tarefa, permitindo que o escalonador ainda possa preempcionar a tarefa, mas garantindo que a seção crítica seja contabilizada para o período de graça (grace period).

## 3.2. RCU Boost

### Algoritmo e Conceito:

*   **Problema:** Em sistemas de tempo real, uma tarefa de alta prioridade pode ser bloqueada indefinidamente esperando que uma seção crítica de RCU termine, se o leitor de RCU estiver em um CPU com prioridade mais baixa (inversão de prioridade).
*   **Mecanismo:** O RCU Boost é uma forma de herança de prioridade aplicada ao RCU. Quando uma tarefa de alta prioridade precisa esperar por um período de graça do RCU, as tarefas que estão atualmente em uma seção crítica de RCU (os leitores) podem ter sua prioridade temporariamente elevada (boost) para que o período de graça termine mais rapidamente.
*   **Implementação:** Força um período de graça usando `krcupreemptd` e aumenta a prioridade de todas as seções de leitura durante a sincronização (`sync_rcu()`).

## Tabela de Conteúdo Técnico

<table>
<thead>
<tr>
<th>Categoria</th>
<th>Conceito/Algoritmo/Estrutura</th>
<th>Descrição Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td>Escalonamento</td>
<td>EEVDF (Earliest Eligible Virtual Deadline First)</td>
<td>Algoritmo de escalonamento justo que utiliza <code>vruntime</code> e <code>deadline virtual</code> para seleção de tarefas elegíveis.</td>
</tr>
<tr>
<td>Estrutura de Dados</td>
<td>Árvore Red-Black (rbtree)</td>
<td>Estrutura de dados balanceada utilizada pelo EEVDF para manter as tarefas executáveis ordenadas pelo <code>vruntime</code> ou <code>deadline virtual</code>.</td>
</tr>
<tr>
<td>Escalonamento</td>
<td>Virtual Runtime (<code>vruntime</code>)</td>
<td>Métrica que acumula o tempo de execução de uma tarefa, escalado pelo peso de prioridade, para medir a justiça do escalonamento.</td>
</tr>
<tr>
<td>Sincronização</td>
<td>Adaptive Spin</td>
<td>Técnica de otimização de mutex onde a tarefa gira (spinlock) apenas se o proprietário do bloqueio estiver em execução, evitando troca de contexto desnecessária.</td>
</tr>
<tr>
<td>Sincronização</td>
<td>Lockdep DAG Validation</td>
<td>Conceito de sistema operacional que rastreia e valida o grafo de dependência de bloqueio para garantir que seja acíclico, prevenindo deadlocks.</td>
</tr>
<tr>
<td>RCU</td>
<td>RCU Boost</td>
<td>Mecanismo de herança de prioridade para RCU, elevando a prioridade dos leitores de RCU para evitar inversão de prioridade em sistemas de tempo real.</td>
</tr>
<tr>
<td>RCU</td>
<td>Preemptible RCU</td>
<td>Adaptação do RCU para kernels com preempção total, onde a seção crítica de leitura é definida por rastreamento de estado em vez de desativação de preempção.</td>
</tr>
<tr>
<td>Sincronização</td>
<td>Priority Inheritance (PI)</td>
<td>Conceito de SO aplicado em mutexes e RCU Boost para resolver a inversão de prioridade, elevando a prioridade de um proprietário de recurso.</td>
</tr>
<tr>
<td>Escalonamento</td>
<td>RT Balancer</td>
<td>Algoritmo de balanceamento de carga para tarefas de tempo real (FIFO/RR) em SMP, respeitando cpusets.</td>
</tr>
</tbody>
</table>

## Pesquisador 6: Paul E. McKenney

Itens Técnicos Encontrados: 17

---


## Page 65

Contribuições: RCU (Read-Copy-Update), Período de Graça, Tree RCU, Ordenação de Memória, Barreiras de Memória (smp_mb, smp_rmb, smp_wmb)

# Conteúdo Técnico: RCU e Ordenação de Memória (Paul McKenney)

## 1. RCU (Read-Copy-Update)

O Read-Copy-Update (RCU) é um mecanismo de sincronização de sistemas operacionais que permite acesso concorrente de múltiplos leitores a estruturas de dados compartilhadas, com latência mínima para as operações de leitura. O RCU é fundamentalmente um algoritmo de sincronização sem bloqueio para leitores (lock-free for readers).

### 1.1. Algoritmo RCU (Conceito Central)

O algoritmo RCU baseia-se na imutabilidade da estrutura de dados durante a leitura e em um processo de atualização em duas fases:

1.  **Fase de Cópia e Atualização (Copy and Update):** O escritor (updater) cria uma cópia da estrutura de dados a ser modificada. A modificação é realizada na cópia.
2.  **Fase de Publicação (Publish):** O escritor usa uma operação atômica (e.g., `rcu_assign_pointer()` ) para substituir o ponteiro da estrutura de dados antiga pela nova. Leitores subsequentes verão a nova estrutura.
3.  **Fase de Espera pelo Período de Graça (Wait for Grace Period):** O escritor espera por um **Período de Graça (Grace Period - GP)**.
4.  **Fase de Reclamação (Reclamation):** Após o GP, o escritor garante que todos os leitores que estavam ativos antes da Fase de Publicação terminaram suas seções críticas e, portanto, não estão mais acessando a estrutura de dados antiga. A memória da estrutura antiga é então liberada (`kfree_rcu()` ).

### 1.2. Estrutura de Dados e Conceitos de SO

*   **Seção Crítica de Leitura RCU (RCU Read-Side Critical Section):** Uma região de código delimitada por `rcu_read_lock()` e `rcu_read_unlock()`. Em implementações como o RCU-sched, esta seção é definida por qualquer região de código onde a preempção está desabilitada.
*   **Período de Graça (Grace Period - GP):** Um intervalo de tempo que é garantido se estender além do ponto de término de todas as Seções Críticas de Leitura RCU que estavam ativas no início do GP. O GP é o mecanismo que permite a reutilização segura da memória (safe deferred reclamation).
*   **Estado Quiescente (Quiescent State - QS):** Um ponto no tempo em que um leitor RCU (CPU ou thread) não está em uma Seção Crítica de Leitura RCU. O término de um GP é declarado quando um QS foi observado em todas as CPUs.

## 2. Arquitetura Tree RCU

O Tree RCU é a arquitetura escalável do RCU implementada no kernel Linux, projetada para sistemas com grande número de CPUs.

### 2.1. Estrutura de Dados rcu_node

A escalabilidade é alcançada através de uma estrutura de dados hierárquica de nós, onde o elemento central é a estrutura `rcu_node`.

*   **Estrutura Hierárquica:** As CPUs são agrupadas em uma árvore de nós (`rcu_node`), reduzindo a sobrecarga de comunicação e sincronização de O(N) para O(log N) em relação ao número de CPUs.

---


## Page 66

* Campo ->lock : O campo ->lock dentro da estrutura rcu_node é o principal bloco de construção para a ordenação de memória do Período de Graça.

## 2.2. Protocolo de Ordenação de Memória do Período de Graça

O Tree RCU utiliza uma rede de seções críticas baseadas em locks e barreiras de memória para fornecer garantias de ordenação.

*   **Garantia de Ordenação:** Qualquer acesso que ocorra após o final de um GP é garantido de ver os efeitos de todos os acessos que ocorreram antes do início daquele GP dentro das Seções Críticas de Leitura RCU.
*   **Uso de Locks e Barreiras:** As funções de aquisição de lock (raw_spin_lock_rcu_node(), etc.) invocam smp_mb__after_unlock_lock() imediatamente após a aquisição bem-sucedida do lock. Este mecanismo garante que um acesso anterior a uma liberação de lock será visto por todas as CPUs como ocorrendo antes de um acesso posterior a uma aquisição de lock subsequente, formando uma cadeia de ordenação que cobre toda a infraestrutura RCU.

## 3. Ordenação de Memória (Memory Ordering)

O trabalho de McKenney sobre ordenação de memória aborda a necessidade de impor uma ordem de execução em sistemas multiprocessados (SMP) devido às otimizações de reordenação de acessos à memória realizadas por compiladores e CPUs.

### 3.1. Conceitos de SO e Arquitetura

*   **Reordenação de Acessos:** CPUs modernas reordenam operações de memória (leitura/escrita) para otimizar o desempenho, explorando o paralelismo de hardware (e.g., bancos de cache independentes).
*   **Modelos de Consistência de Memória:**
    *   **Consistência Sequencial (Sequential Consistency):** Todas as operações ocorrem na ordem especificada pelo código, e a visão de todos os CPUs é consistente com uma ordem global combinada. (Raramente implementada em hardware de alto desempenho).
    *   **Consistência Fraca (Weak Consistency):** Permite reordenações arbitrárias, limitadas apenas por instruções explícitas de barreira de memória.
    *   **Consistência de Processo (Process Consistency - x86):** As escritas de um dado CPU são vistas em ordem por todos os CPUs.

### 3.2. Algoritmos: Barreiras de Memória (Memory Barriers)

As barreiras de memória são instruções de CPU que impõem uma ordenação parcial percebida sobre as operações de memória em ambos os lados da barreira.

*   **smp_mb() (Memory Barrier):** Uma barreira completa que impede a reordenação de operações de leitura (loads) e escrita (stores) que a precedem com operações que a sucedem.
*   **smp_rmb() (Read Memory Barrier):** Impede a reordenação de operações de leitura que a precedem com operações de leitura que a sucedem.
*   **smp_wmb() (Write Memory Barrier):** Impede a reordenação de operações de escrita que a precedem com operações de escrita que a sucedem.
*   **smp_mb__after_unlock_lock():** Uma barreira de memória especializada usada em primitivas de sincronização (como locks RCU) para garantir que acessos antes de uma liberação de lock sejam visíveis antes de acessos após uma aquisição de lock subsequente.

### 3.3. Estruturas de Dados (Implícitas)

*   **Ponteiros Protegidos por RCU:** Ponteiros para estruturas de dados que são lidos usando rcu_dereference() e escritos usando rcu_assign_pointer().
*   **Operações Atômicas:** Funções como atomic_add_return() são usadas para garantir ordenação forte em transições de estado (e.g., entrada/saída de estado ocioso), pois são operações de leitura-modificação-escrita.

---


## Page 67

* Estruturas de Sincronização: Primitivas de sincronização de alto nível (spinlocks, semáforos) que encapsulam as barreiras de memória necessárias.

Referências: [1] McKenney, P. E. (2017). *A Tour Through TREE_RCU’s Grace-Period Memory Ordering*. The Linux Kernel documentation. [2] McKenney, P. E. (2005). *Memory Ordering in Modern Microprocessors, Part I*. ACM Queue. [3] McKenney, P. E. (2010). *Memory Barriers: a Hardware View for Software Hackers*. [4] McKenney, P. E. (2007). *What is RCU, Fundamentally?*. PDXScholar.

---

## Pesquisador 7: Dianne Hackborn

Itens Técnicos Encontrados: 25

Contribuições: Mecanismo Binder IPC, Arquitetura de Gerenciamento de Atividades e Tarefas, Estruturas de Dados de Gerenciamento de Janelas

## Conteúdo Técnico do Trabalho de Dianne Hackborn: Binder, Activity Manager e Window Manager

O trabalho de Dianne Hackborn na arquitetura do Android é fundamental, especialmente no desenvolvimento do mecanismo de Inter-Process Communication (IPC) **Binder** e na definição das estruturas de gerenciamento de componentes e janelas, como o **Activity Manager** e o **Window Manager**. A análise a seguir foca exclusivamente nos conceitos técnicos, arquitetura de sistemas, estruturas de dados, protocolos e algoritmos subjacentes.

### 1. O Mecanismo Binder (Protocolo e Arquitetura)

O Binder é um mecanismo de RPC (Remote Procedure Call) leve otimizado para o ambiente móvel do Android, sendo um dos pilares da arquitetura do sistema operacional [1]. Sua concepção, baseada no projeto OpenBinder, foi liderada por Hackborn e é crucial para a comunicação entre os processos do *System Server* e os processos de aplicação [2].

#### Protocolo e Conceitos de SO

O Binder opera como um **driver no kernel** do Linux, facilitando a comunicação entre processos que, por princípio de **isolamento de dados** e segurança, possuem espaços de endereço separados.

*   **Comunicação Síncrona**: O protocolo Binder suporta chamadas síncronas entre processos, o que simplifica a lógica de programação de serviços.
*   **Memória Compartilhada** (*ashmem*): Para transferências de dados de alto desempenho, o Binder utiliza a **memória compartilhada anônima** (*ashmem*) para mapear buffers de dados diretamente entre os espaços de endereço do processo remetente e do processo destinatário, minimizando a cópia de dados (zero-copy) [1].
*   **Pool de Threads por Processo**: Cada processo de aplicação que atua como servidor Binder mantém um **pool de threads** dedicado para processar requisições de IPC recebidas, garantindo que as chamadas de serviço não bloqueiem a thread principal da aplicação.
*   **AIDL (Android Interface Definition Language)**: É a linguagem de definição de interface que formaliza o protocolo de comunicação, permitindo que o sistema gere automaticamente o código *stub* e *proxy* para a invocação de métodos remotos.

#### Estruturas de Dados do Kernel

O driver Binder mantém estruturas de dados essenciais para rastrear e gerenciar as referências de objetos entre processos:

---


## Page 68

<table>
  <thead>
    <tr>
      <th>Estrutura de Dados</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>binder_node</code></td>
      <td>Estrutura no kernel que representa um objeto Binder (o serviço real) no processo servidor. É o ponto de ancoragem para o serviço.</td>
    </tr>
    <tr>
      <td><code>binder_ref</code></td>
      <td>Estrutura no kernel que representa uma referência a um <code>binder_node</code> em um processo cliente. É o que o cliente usa para interagir com o serviço.</td>
    </tr>
    <tr>
      <td><code>Parcel</code></td>
      <td>O contêiner de dados fundamental para a transação Binder. É uma estrutura serializável otimizada para IPC, capaz de empacotar e desempacotar dados primitivos e referências a objetos Binder.</td>
    </tr>
  </tbody>
</table>

## Algoritmo de Contagem de Referência

O Binder implementa um algoritmo de **contagem de referência** no kernel para gerenciar o ciclo de vida dos objetos Binder. Este mecanismo garante que os objetos de serviço não sejam destruídos enquanto ainda houver referências ativas a eles em outros processos, prevenindo vazamentos de memória e falhas de comunicação [1].

## 2. Activity Manager (Arquitetura e Algoritmos)

O **Activity Manager Service (AMS)** é o serviço de sistema responsável por gerenciar o ciclo de vida dos componentes de aplicação, com foco nas Activities e na organização das tarefas.

### Estruturas de Gerenciamento de Componentes

O AMS utiliza estruturas de dados hierárquicas para manter o estado do sistema:

*   **ActivityRecord**: Estrutura de dados central que encapsula o estado completo de uma instância de Activity, incluindo sua configuração, estado de ciclo de vida (e.g., INITIALIZING, PAUSED, RESUMED), e flags de lançamento.
*   **TaskRecord**: Representa uma **Task (Tarefa)**, que é uma coleção de Activities. A estrutura contém uma lista ordenada de ActivityRecord (<code>ArrayList<ActivityRecord> mActivities</code>), gerenciando a afinidade da tarefa (affinity) e o modo de persistência.
*   **ActivityStack (ou TaskStack)**: Estrutura de dados do tipo **Pilha (Stack)** que armazena as Activities dentro de uma Task, implementando o comportamento LIFO (Last-In, First-Out) para a navegação de retorno (Back Stack) [3].

### Algoritmos de Gerenciamento de SO

*   **Algoritmo de Gerenciamento de Ciclo de Vida**: O AMS implementa um **algoritmo de máquina de estados** para controlar as transições de estado das Activities (e.g., onCreate(), onPause(), onResume()), garantindo a correta alocação e desalocação de recursos.
*   **Algoritmo de Empilhamento de Atividades**: A lógica de empilhamento é um algoritmo complexo que avalia as flags de intenção (e.g., FLAG_ACTIVITY_NEW_TASK, FLAG_ACTIVITY_CLEAR_TOP) e os modos de lançamento (e.g., LAUNCH_SINGLE_TASK) para determinar se uma nova Activity deve ser criada, reutilizada ou se a pilha de tarefas deve ser reordenada ou limpa.
*   **Gerenciamento de Processos e Memória**: O AMS atua como um **gerenciador de processos** de alto nível, utilizando o estado das Activities (e.g., foreground, background) para tomar decisões sobre a eliminação de processos (low-memory killer) e a alocação de recursos, um conceito essencial de **Gerenciamento de Memória** em sistemas operacionais móveis.

## 3. Window Manager (Arquitetura)

O **Window Manager Service (WMS)** é o serviço de sistema que interage com o *SurfaceFlinger* para gerenciar a apresentação visual das janelas.

*   **Criação de Superfícies**: O WMS é responsável por solicitar e gerenciar as **superfícies gráficas** (buffers de pixels) para cada janela de aplicação, que são então compostas pelo *SurfaceFlinger*.

---


## Page 69

*   **Estruturas de Janela:** O WMS utiliza estruturas como `WindowState` para representar cada janela individualmente e `WindowContainer` como uma classe base para contêineres hierárquicos de janelas, como `ActivityRecord` e `TaskRecord`, permitindo que o gerenciamento de janelas seja integrado ao gerenciamento de atividades.
*   **Algoritmo de Gerenciamento de Foco:** O WMS implementa um algoritmo para determinar qual janela deve receber os eventos de entrada (foco), essencial para a interação do usuário.
*   **Transições de Janela:** O WMS gerencia as animações e transições entre as janelas (e.g., abertura, fechamento, redimensionamento), utilizando estados de transição como `TRANSIT_CLOSE` e `TRANSIT_RELAUNCH`.

---

## Referências

[1] Huang, J. (2012). *Android Binder IPC Mechanism*. Southern Taiwan University of Technology. [2] Artenstein, N. (2014). *Man in the Binder: He Who Controls IPC, Controls the Droid*. Black Hat Europe. [3] Android Open Source Project. services/core/java/com/android/server/am/TaskRecord.java. Google Git.

---

## Pesquisador 8: Jeff Sharkey

**Itens Técnicos Encontrados:** 18

**Contribuições:** Scoped Storage, FUSE, MediaProvider como Handler FUSE, Modelo de Permissão Granular, ContentProvider.applyBatch, Storage Access Framework

## Conteúdo Técnico Extraído: Jeff Sharkey - Storage, Permissions, Scoped Storage

O trabalho de Jeff Sharkey, focado principalmente na introdução e evolução do **Scoped Storage** no Android (a partir do Android Q/10), representa uma mudança fundamental na **arquitetura de sistemas** e no **modelo de permissões** do sistema operacional, estendendo o princípio de **Application Sandboxing** para o armazenamento externo [1].

## Arquitetura de Sistemas e Conceitos de SO

### Scoped Storage e Modelo de Permissões

O **Scoped Storage** é um paradigma de armazenamento que visa proteger a privacidade e a segurança dos dados do usuário, limitando o acesso de aplicativos ao armazenamento externo [2].

O modelo de acesso é baseado em um **isolamento de dados** mais rigoroso, com as seguintes regras de acesso granular [2]:

*   **Acesso Próprio:** Aplicativos têm acesso de **leitura e escrita** aos seus próprios arquivos (diretórios específicos do pacote) sem a necessidade de permissões de armazenamento [2].
*   **Acesso a Mídia Compartilhada:**
    *   **Leitura:** Requer a permissão `READ_EXTERNAL_STORAGE` para acessar arquivos de mídia contribuídos por outros aplicativos [2].
    *   **Escrita:** A escrita em arquivos de mídia de outros aplicativos é permitida apenas com **consentimento direto do usuário** (com exceções para aplicativos de Galeria do Sistema e aqueles elegíveis para a permissão `MANAGE_EXTERNAL_STORAGE` - “All Files access”) [2].
*   **Acesso a Dados Privados:** Não há acesso de leitura ou escrita aos diretórios de dados externos de outros aplicativos (`android/data` e `android/obb`) [2].

### Filesystem in Userspace (FUSE)

A partir do Android 11, o sistema operacional suporta o **Filesystem in Userspace (FUSE)**, que é um componente crucial na arquitetura do Scoped Storage [2].

---


## Page 70

*   **Função do FUSE:** O FUSE permite que o módulo MediaProvider examine as operações de arquivo no espaço do usuário e controle o acesso aos arquivos com base em uma política de permitir, negar ou redigir (redact) o acesso [2].
*   **Implementação:** O Android 11 reintroduziu o FUSE usando uma implementação aprimorada da libfuse, que pode ser ajustada para resolver problemas de desempenho observados em versões anteriores [2].
*   **MediaProvider como Handler FUSE:** No Android 11+, o MediaProvider assume o papel de handler do sistema de arquivos (para FUSE) para o armazenamento externo. Isso garante a consistência entre o sistema de arquivos no armazenamento externo e o banco de dados do MediaProvider [2]. Como handler no espaço do usuário, o MediaProvider pode interceptar chamadas do kernel para garantir a segurança da privacidade nas operações de arquivo [2].
*   **Otimizações (FUSE Tuning):** O ajuste de desempenho do FUSE inclui [2]:
    *   **Bypass:** Ignorar o FUSE para os diretórios de armazenamento privado externo (Android/data e Android/obb).
    *   **Ajuste de Parâmetros:** Otimização de read-ahead e dirty ratios do sistema de arquivos FUSE.
    *   **Cache:** Uso de FUSE write-back cache.
    *   **IPC:** Caching de permissões para reduzir chamadas de IPC (Inter-Process Communication) para o system server [2].

## Protocolos e Estruturas de Dados

*   **MediaStore API:** Protocolo/API central para lidar com arquivos de mídia compartilhados. Define coleções específicas para tipos de mídia (Audio, Video, Images) e a coleção Downloads [1].
*   **ContentProvider.applyBatch():** API para realizar operações de arquivo em massa (bulk file operations) em uma única transação, otimizando a eficiência [1].
*   **Storage Access Framework (SAF):** Conjunto de APIs para interação com o seletor de arquivos do sistema [1]:
    *   ACTION_OPEN_DOCUMENT / ACTION_GET_CONTENT : Para abrir um seletor de arquivos [1].
    *   ACTION_OPEN_DOCUMENT_TREE : Para permitir que o usuário selecione uma subárvore de diretórios (directory subtree), tipicamente usado por aplicativos de gerenciamento de arquivos [1].
*   **DocumentsProvider:** Interface que permite que o sistema acesse arquivos de provedores de documentos instalados (soluções de armazenamento local ou em nuvem) [1].
*   **File Descriptor Passing:** Padrão de comunicação recomendado para código nativo (NDK), onde o código Java/Kotlin descobre o arquivo e passa o descriptor de arquivo associado para o código nativo [1].

## Contribuições Técnicas (Resumo)

O trabalho de Jeff Sharkey é central para a implementação do **Scoped Storage**, que envolve a reengenharia do subsistema de armazenamento do Android para maior segurança e privacidade, com a adoção do **FUSE** e a redefinição do papel do **MediaProvider** como um componente modular e handler do sistema de arquivos.

## Referências

[1] Jeff Sharkey, Seb Grubb. *Android Q Scoped Storage: Best Practices and Updates*. Android Developers Blog. 2019. [2] Android Open Source Project. *Scoped storage*. AOSP Documentation.

## Contagem de Conceitos

1.  Application Sandboxing (Princípio de SO)
2.  Scoped Storage (Paradigma de Armazenamento/Arquitetura)
3.  Modelo de Permissão Granular (Conceito de SO/Segurança)
4.  Filesystem in Userspace (FUSE) (Arquitetura/Protocolo de SO)
5.  MediaProvider como Handler FUSE (Arquitetura/Componente de SO)
6.  Política de Acesso (Allow, Deny, Redact) (Algoritmo/Conceito de SO)
7.  FUSE Bypass (Otimização de Arquitetura)

---


## Page 71

8. SDCardFS Deprecation (Arquitetura de SO)
9. FUSE Tuning (Algoritmo/Otimização)
10. FUSE write-back cache (Estrutura de Dados/Otimização)
11. Caching de Permissões (Estrutura de Dados/Otimização)
12. MediaStore API (Protocolo/API)
13. ContentProvider.applyBatch() (API/Algoritmo de Bulk Operation)
14. ACTION_OPEN_DOCUMENT (API/Protocolo SAF)
15. ACTION_OPEN_DOCUMENT_TREE (API/Protocolo SAF)
16. DocumentsProvider (Interface/Estrutura)
17. File Descriptor Passing (Protocolo de Comunicação)
18. Modular System Component (Mainline) (Arquitetura de SO)

Total de conceitos técnicos identificados: 18.

---

## Pesquisador 9: Chet Haase

Itens Técnicos Encontrados: 20

Contribuições: Framework de Animação de Propriedades, Arquitetura de Renderização Acelerada (RenderNode), Interpolação Linear (LERP), Sistema de Propriedades da View, AGSL e RuntimeShader

### Framework de Animação de Propriedades (Property Animation Framework)

O trabalho de Chet Haase no Android 3.0 (Honeycomb) introduziu o **Framework de Animação de Propriedades** (android.animation), uma mudança arquitetural significativa em relação ao sistema anterior (android.view.animation).

#### Conceitos e Estruturas de Dados

*   **Property Animation (Animação de Propriedades):** Conceito central que permite animar valores ao longo do tempo e atribuir esses valores a propriedades de objetos, não se limitando a objetos View ou a um conjunto fixo de transformações visuais.
*   **Animator:** Superclasse abstrata para as classes de animação.
*   **ValueAnimator:** O motor de temporização central do sistema. É responsável por calcular os valores animados (o “o quê” da animação).
    *   **Estrutura de Dados:** Utiliza valores de ponto flutuante (float) e inteiros (int) por padrão, mas é extensível.
    *   **Algoritmo de Interpolação:** Implementa a lógica de temporização (duração, repetição, atraso) e utiliza o conceito de interpolação para calcular valores intermediários.
*   **ObjectAnimator:** Subclasse de ValueAnimator que adiciona a capacidade de definir um objeto alvo e o nome de uma propriedade. É responsável por aplicar os valores calculados (o “onde” da animação) ao objeto alvo, invocando automaticamente os métodos setter(set<Property>) correspondentes.
    *   **Protocolo de Acesso:** Depende da existência de métodos públicos set<Property>(Type value) e, opcionalmente, get<Property>() no objeto alvo para funcionar.
*   **AnimatorSet:** Estrutura de dados para coreografar múltiplas animações, permitindo que sejam executadas em paralelo (with), sequencialmente (after), ou com atrasos específicos, através da classe auxiliar AnimatorSet.Builder.
*   **TypeEvaluator:** Interface (algoritmo/estrutura) que define como interpolar entre valores de tipos não-padrão (diferentes de float ou int).
    *   **Algoritmo Linear:** A implementação padrão para tipos complexos, como PointEvaluator, realiza uma interpolação linear (Linear Interpolation - LERP) entre os valores inicial e final, baseada na fração de tempo decorrido (fraction).
    *   **Fórmula LERP (implícita):** startFloat + fraction * (endFloat - startFloat)

---


## Page 72

*   **TimeInterpolator**: Interface que controla o comportamento de temporização não-linear da animação (e.g., aceleração e desaceleração). É um super-interface do Interpolator legado.

## Conceitos de Sistema Operacional e Arquitetura de UI

O trabalho de Haase e Guy na arquitetura de gráficos do Android revela os seguintes conceitos:

*   **Arquitetura de Renderização (Pipeline Gráfico):**
    *   **Skia**: Biblioteca 2D nativa (motor gráfico) usada pelo Android.
    *   **Modo Imediato (Immediate Mode)**: Modelo inicial de renderização onde comandos de desenho eram executados diretamente na Thread da UI.
    *   **Renderização Acelerada por Hardware (Android 3.0+)**: Mudança arquitetural onde os comandos de desenho são gravados em uma display list (hoje conhecida como RenderNode ) em vez de serem executados imediatamente. Essa lista é então executada pela GPU, liberando a Thread da UI.
    *   **RenderNode**: Estrutura de dados que armazena os comandos de desenho de uma View para serem reexecutados de forma eficiente pela GPU.
*   **Propriedades da View**: Adição de propriedades transformacionais à classe View para suportar a Animação de Propriedades, permitindo que a animação altere a localização e orientação física do objeto, e não apenas sua aparência visual.
    *   **Propriedades de Transformação**: translationX, translationY, rotation, rotationX, rotationY, scaleX, scaleY, pivotX, pivotY, x, y, alpha.
*   **Otimização de Memória**: Introdução de Hardware Bitmaps (Android 8.0), que residem apenas na memória da GPU para economizar RAM.
*   **Gráficos Programáveis**:
    *   **RenderEffect (Android 12/13)**: Conceito de aplicação de efeitos visuais (como blur) no pipeline de renderização.
    *   **RuntimeShader (Android 12/13)**: Permite a criação de shaders customizados em tempo de execução usando AGSL (Android Graphics Shading Language), oferecendo controle de baixo nível sobre a renderização.
*   **Estruturas de Dados de Caminho**: A biblioteca androidx.graphics:graphics-path introduziu o PathIterator, uma estrutura para inspecionar os dados de um caminho de desenho, permitindo manipulação e análise programática de formas vetoriais.
*   **Arquitetura de UI Moderna**: O trabalho visa uma futura API Canvas moderna, stateless (sem estado), e mais simples no AndroidX, contrastando com a API Paint legada, que é um “god object” stateful.

## Conceitos Encontrados:

1.  Property Animation
2.  Animator
3.  ValueAnimator
4.  ObjectAnimator
5.  AnimatorSet
6.  TypeEvaluator
7.  TimeInterpolator
8.  Interpolação Linear (LERP)
9.  Skia (Motor Gráfico)
10. Modo Imediato (Immediate Mode)
11. Renderização Acelerada por Hardware
12. RenderNode (Display List)
13. Propriedades de Transformação da View
14. Hardware Bitmaps

---


## Page 73

15. RenderEffect
16. RuntimeShader
17. AGSL (Android Graphics Shading Language)
18. PathIterator
19. Arquitetura Stateless (Objetivo de Design)
20. Protocolo Setter/Getter (para ObjectAnimator)

---

## Pesquisador 10: Romain Guy

Itens Técnicos Encontrados: 18

Contribuições: Pipeline 2D Acelerado por Hardware, Display Lists para cache de comandos, Otimização de Animação com Camadas de Hardware

---

## Conteúdo Técnico do Trabalho de Romain Guy: Sistema View, Aceleração de Hardware e Renderização no Android

---

## Arquitetura e Conceitos de Sistemas Operacionais

### Pipeline de Renderização 2D Acelerado por Hardware

A principal contribuição arquitetural é a introdução do **Pipeline 2D Acelerado por Hardware** no Android 3.0 (Honeycomb), que descarrega operações de desenho da CPU para a **GPU (Graphics Processing Unit)**, aproveitando o paralelismo inerente ao hardware gráfico.

### Modelo de Desenho (Drawing Model)

O novo modelo de desenho opera em três estágios fundamentais, que substituem o modelo de redesenho recursivo da hierarquia de Views:

1.  **Invalidate the hierarchy (Invalidar a hierarquia):** Marca a View como “suja” (dirty), sinalizando a necessidade de redesenho.
2.  **Record/update display lists (Gravar/atualizar listas de exibição):** O sistema registra as chamadas de desenho em uma estrutura de dados, a Display List.
3.  **Draw the display lists (Desenhar as listas de exibição):** A GPU executa os comandos armazenados na Display List.

### Componentes do Pipeline

*   **OpenGLRenderer:** Componente de arquitetura que atua como um tradutor, convertendo as chamadas de desenho do Canvas (API de desenho 2D do Android) em comandos OpenGL ES (protocolo gráfico) para execução na GPU.
*   **Composição:** O processo de combinar as camadas de diferentes Views para formar a imagem final na tela é realizado pelo **SurfaceFlinger** (componente de SO/arquitetura implícito no processo de renderização).

---


## Page 74

# Estruturas de Dados

## Display Lists

As **Display Lists** são estruturas de dados que armazenam uma sequência de comandos de desenho (Draw commands) de uma View.

*   **Otimização:** Ao invés de reexecutar o código Java de desenho da View, o sistema simplesmente reexecuta a Display List pré-gravada, o que é significativamente mais rápido, pois a execução ocorre em código nativo.

## Camadas de Hardware (Hardware Layers)

Uma **Hardware Layer** é uma estrutura de renderização que armazena o conteúdo de uma View em um framebuffer fora da tela, tipicamente uma textura OpenGL na memória da GPU.

*   **Tipos:**
    *   LAYER_TYPE_HARDWARE : Utiliza uma textura OpenGL.
    *   LAYER_TYPE_SOFTWARE : Utiliza um Bitmap na memória RAM.

# Algoritmos e Protocolos

## Otimização de Animação

Um algoritmo de otimização de animação utiliza as Camadas de Hardware para evitar o redesenho completo da View quando apenas propriedades como alpha, rotação ou escala são alteradas. O sistema insere comandos de manipulação de camada:

```java
SaveLayerAlpha(alpha_value)
DrawDisplayList(View)
Restore
```

Este algoritmo aplica a transformação (ex: transparência) à textura da camada sem precisar reexecutar os comandos de desenho complexos da View.

## Shaders GLSL

O pipeline de renderização acelerado utiliza **Shaders GLSL** (OpenGL Shading Language) para definir o comportamento de renderização na GPU.

### Exemplo de Vertex Shader (Text+gradient)

O código a seguir é um exemplo de um vertex shader que calcula coordenadas de textura e uma variável linear para gradientes, além de transformar a posição do vértice:

```glsl
attribute vec4 position;
attribute vec2 texCoords;
uniform mat4 transform;
uniform mat4 screenSpace;
varying vec2 outTexCoords;
varying vec2 linear;

void main(void) {
  outTexCoords = texCoords;
  linear = vec2((screenSpace * position).x, 0.5);
  gl_Position = transform * position;
}

---


## Page 75

# Restrições e Comportamentos (API)

O pipeline de hardware não suporta certas operações da API Canvas e Paint, indicando limitações na tradução de comandos 2D para OpenGL ES:

*   **Operações Não Suportadas (Canvas):** `clipPath`, `clipRegion`, `drawPicture`, `drawPoints`, `drawPosText`, `drawTextOnPath`, `drawVertices`.
*   **Operações Não Suportadas (Paint):** `setLinearText`, `setMaskFilter`, `setRasterizer`.
*   **Comportamento Alterado (clipRect):** Modos de recorte como XOR, Difference e ReverseDifference são ignorados.
*   **Restrições de ComposeShader:** Não pode conter dois shaders do mesmo tipo; não pode conter outro ComposeShader.

---

# Pesquisador 11: Chris Craik

**Itens Técnicos Encontrados:** 11

**Contribuições:** RenderThread, Display List (RenderNode), Algoritmo de Reordenação Sensível à Sobreposição, CanvasProperty, HWUI

O trabalho de Chris Craik no sistema de renderização do Android, notavelmente o **HWUI (Hardware UI)**, introduziu conceitos fundamentais de arquitetura de sistemas e estruturas de dados para otimizar o desempenho gráfico, com foco em animações fluidas e redução de *jank* (engasgos).

## Arquitetura e Conceitos de Sistemas Operacionais

O principal conceito de arquitetura introduzido é a separação de responsabilidades entre *threads* para garantir a fluidez da interface:

1.  **RenderThread (Conceito de SO/Arquitetura):**
    *   É um *thread* de processamento gerenciado pelo sistema, introduzido no Android Lollipop (API 21).
    *   **Função:** Offload (descarregamento) do trabalho de renderização da *Main UI Thread* (Thread Principal da Interface do Usuário).
    *   **Mecanismo:** O RenderThread é responsável pela otimização e despacho final dos comandos de desenho para a **GPU** (*Graphics Processing Unit*).
    *   **Vantagem:** Permite que animações e efeitos visuais (como translações, escalas, rotações e *alpha*) continuem a ser processados e atualizados de forma assíncrona, mesmo quando a UI Thread está ocupada com tarefas pesadas, garantindo o conceito de **animações livres de *jank***.

## Estruturas de Dados e Protocolos

O sistema de renderização é baseado em estruturas de dados que armazenam e otimizam as operações de desenho:

1.  **Display List / RenderNode (Estrutura de Dados):**
    *   É uma estrutura de dados interna (anteriormente *DisplayList*, agora encapsulada por *RenderNode*) que atua como um **gravador de macro** de operações de desenho.
    *   **Conteúdo:** Armazena uma sequência de comandos de desenho (*DisplayListOp*) e referências a recursos (como *bitmaps*, *paths*, *paints*).
    *   **Uso:** A UI Thread cria e modifica o *RenderNode*, e o RenderThread o reproduz (*replay*) para a GPU.
    *   **Otimização:** Permite que as operações de desenho sejam conhecidas antecipadamente e otimizadas (ex: agrupar todo o desenho de texto em uma única passagem) e re-executadas sem a necessidade de interação com a lógica de negócios do aplicativo.

2.  **CanvasProperty (Protocolo/Estrutura de Dados):**
    *   É um *wrapper* para valores (ex: *float*, *paint*) que permite que o *DisplayListCanvas* (a implementação do *Canvas* para aceleração de hardware) registre uma **referência** a um valor, em vez do valor direto.

---


## Page 76

*   **Função:** Permite que o valor seja alterado dinamicamente e assincronamente pelo RenderThread (via RenderNodeAnimator) sem a necessidade de recriar a Display List na UI Thread.

3. **Instruction Buffer (Estrutura de Dados):**
    *   Um buffer de instruções utilizado no algoritmo de reordenação para armazenar comandos de desenho antes de serem enviados ao GPC (Graphics Processing Component).

## Algoritmo de Reordenação Sensível à Sobreposição

O trabalho de Craik e Guy resultou na patente US9875519B2, que descreve um algoritmo para otimizar a ordem de execução das instruções de renderização, minimizando a troca de estado (shader switching) na GPU, sem comprometer a ordem visual correta (first-to-last drawing order).

### Algoritmo de Reordenação (Método 100 - Sorting):

1.  **Entrada:** Uma nova instrução de desenho ($I_A$) associada a uma porção da tela ($P_A$).
2.  **Busca:** O algoritmo busca no Instruction Buffer em ordem reversa (do final para o início).
3.  **Verificação de Sobreposição (Overlap Check):**
    *   Para uma instrução existente ($I_B$) no buffer com porção da tela ($P_B$): Se $P_A$ sobrepõe $P_B$, a posição de inserção de $I_A$ é determinada com base na posição de $I_B$ (preservando a ordem de desenho).
4.  **Verificação de Similaridade (Similarity Check):**
    *   Se não houver sobreposição, o algoritmo verifica se $I_A$ e $I_B$ são similares (ex: mesmo VOT - Visible Object Type).
    *   VOT (Visible Object Type): Conceito/Estrutura de Dados que classifica as instruções de desenho por tipo (ex: point type, line type, shape type, image type, text type).
    *   Se forem similares, a posição de inserção é determinada para agrupar $I_A$ perto de $I_B$, reduzindo a troca de shaders.
5.  **Inserção:** $I_A$ é inserida no Instruction Buffer na posição determinada.

### Algoritmo de Fusão (Método 150 - Merging):

1.  **Identificação:** Identificar uma instrução fusível (mergeable instruction) no buffer (ex: usando uma chave de fusão baseada no VOT).
2.  **Verificação de Sobreposição:** Buscar por sobreposição entre a porção da tela da nova instrução e as instruções no buffer até a posição da instrução fusível.
3.  **Fusão:** Se nenhuma sobreposição for encontrada, a nova instrução é fundida (merged) com a instrução fusível, substituindo-a por uma única instrução que executa ambas as operações.

---


## Page 77

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Tipo</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HWUI</td>
      <td>Arquitetura</td>
      <td>Motor de renderização do Android que utiliza aceleração de hardware (GPU).</td>
    </tr>
    <tr>
      <td>RenderThread</td>
      <td>Conceito de SO</td>
      <td>Thread de processamento assíncrono para offload de renderização da UI Thread.</td>
    </tr>
    <tr>
      <td>Display List / RenderNode</td>
      <td>Estrutura de Dados</td>
      <td>Lista de comandos de desenho gravados para otimização e reprodução na GPU.</td>
    </tr>
    <tr>
      <td>Instruction Buffer</td>
      <td>Estrutura de Dados</td>
      <td>Buffer de comandos de desenho para reordenação e fusão antes do GPC.</td>
    </tr>
    <tr>
      <td>Overlap-Aware Reordering</td>
      <td>Algoritmo</td>
      <td>Reordenação de instruções de desenho baseada em sobreposição de regiões para otimizar o uso de shaders e preservar a ordem visual.</td>
    </tr>
    <tr>
      <td>VOT (Visible Object Type)</td>
      <td>Conceito/Estrutura</td>
      <td>Classificação de instruções de desenho (point, line, shape, image, text) para determinar similaridade e agrupar operações.</td>
    </tr>
    <tr>
      <td>CanvasProperty</td>
      <td>Protocolo</td>
      <td>Wrapper para valores dinâmicos que permite a atualização de parâmetros de desenho pelo RenderThread.</td>
    </tr>
    <tr>
      <td>Instruction Merging</td>
      <td>Algoritmo</td>
      <td>Fusão de instruções de desenho similares e não sobrepostas em um único comando para reduzir o overhead por instrução.</td>
    </tr>
    <tr>
      <td>GPC (Graphics Processing Component)</td>
      <td>Arquitetura</td>
      <td>Componente de hardware (GPU) que executa as instruções de renderização.</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Algoritmo/Estrutura</th>
      <th>Detalhe Técnico</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Reordenação</td>
      <td>Busca reversa no Instruction Buffer com lógica condicional: IF overlap THEN preserve order ELSE IF Similar THEN group ELSE insert at End .</td>
    </tr>
    <tr>
      <td>Fusão</td>
      <td>Condição: IF NOT Overlap AND Similar THEN Merge Instructions .</td>
    </tr>
    <tr>
      <td>RenderThread</td>
      <td>Executa RenderNodeAnimator para atualizar CanvasProperty de forma assíncrona.</td>
    </tr>
    <tr>
      <td>Display List</td>
      <td>Armazena Vector<DisplayListOp*> e recursos ( Vector<const SkBitmap*> , Vector<const SkPaint*> , etc.).</td>
    </tr>
    <tr>
      <td>VOT</td>
      <td>Usado como Merging Key para hash lookup na busca por instruções fusíveis.</td>
    </tr>
  </tbody>
</table>

## Pesquisador 12: John Reck (Engenheiro de Software no Google)

**Itens Técnicos Encontrados:** 12

**Contribuições:** Gap Buffer, Slot Table, Recomposição O(1), Estabilidade Estrutural, State Hoisting

O trabalho de John Reck no Jetpack Compose e na UI declarativa está intrinsecamente ligado aos mecanismos internos de alto desempenho do runtime do Compose. A arquitetura técnica subjacente é construída sobre conceitos de estruturas de dados e algoritmos que garantem a eficiência da **Recomposição** (Recomposition), o processo de atualização da interface do usuário em resposta a mudanças de estado.

### Estruturas de Dados e Algoritmos

#### 1. Gap Buffer (Buffer de Lacuna)

O **Gap Buffer** é uma estrutura de dados fundamental, originária da década de 1960, que serve de base conceitual para a otimização de operações de inserção e deleção.

*   **Estrutura:** Um array contínuo com uma “lacuna” (gap) móvel.
*   **Algoritmo:** A inserção ou deleção de dados na posição da lacuna é uma operação de Complexidade de Tempo O(1). O movimento da lacuna para uma nova posição é uma operação de Complexidade de Tempo O(n), onde n é o número de elementos a serem movidos.

---


## Page 78

*   **Aplicação:** O Jetpack Compose utiliza o conceito de Gap Buffer internamente no componente TextField para manipulação eficiente de texto, onde a maioria das edições ocorre em torno do cursor.

## 2. Slot Table (Tabela de Slots)

A **Slot Table** é a estrutura de dados central do *runtime* do Jetpack Compose, análoga ao Gap Buffer, mas aplicada à árvore de elementos da UI (Composables).

*   **Estrutura:** Uma estrutura de dados que armazena os nós da árvore de UI e seus valores associados. Ela incorpora o princípio do Gap Buffer para otimizar as atualizações.
*   **Algoritmo:** Durante a Recomposição, o *runtime* move o “cursor” (a lacuna conceitual) na Slot Table para os *slots* que precisam ser atualizados. Isso permite que o *runtime* pule grandes seções da árvore de UI que não foram alteradas, resultando em uma Recomposição de **Complexidade de Tempo O(1)** para a maioria das atualizações de estado local.
*   **Conceito de Arquitetura:** A Slot Table é a base para a **Estabilidade Estrutural** (Structural Stability), onde a estrutura da árvore de UI deve ser mantida o mais constante possível para maximizar a eficiência do pulo de *slots* (skipping).

## Conceitos de Arquitetura e Otimização

### 3. Recomposição Otimizada

A Recomposição é o processo de chamar novamente as funções Composable para atualizar a UI. Sua otimização depende de:

*   **Estabilidade Estrutural:** A arquitetura do código deve evitar a mudança condicional da estrutura da árvore de UI (ex: usando AnimatedVisibility em vez de blocos `if` que alteram a composição).
*   **State Hoisting (Elevação de Estado):** O padrão de arquitetura que move o estado para o chamador do Composable, garantindo que apenas o Composable que depende do estado seja recomposto, e não seus filhos ou irmãos. Isso é um princípio do **Fluxo de Dados Unidirecional (UDF)**.
*   **derivedStateOf (Estado Derivado):** Uma função que permite que cálculos caros baseados em estado sejam armazenados em cache e só sejam reavaliados quando o estado subjacente mudar, evitando recomposições desnecessárias.

### 4. Chaves Estáveis (Stable Keys)

Em listas dinâmicas (como LazyColumn ou LazyRow), o uso de **Chaves Estáveis** é um algoritmo crucial:

*   **Algoritmo:** Ao fornecer uma chave única e estável (ex: `item.id`) para cada item da lista, o *runtime* do Compose pode identificar e rastrear com precisão quais itens foram adicionados, removidos ou movidos.
*   **Conceito de SO:** Isso se relaciona com a otimização de recursos, pois o *runtime* evita a reconstrução completa dos itens da lista, preservando o estado interno (como a posição de rolagem ou o estado de foco) dos elementos que não mudaram.

### 5. Batching de Mudanças (Batching Changes)

A arquitetura do Compose suporta o agrupamento de múltiplas mudanças de estado em uma única transação de Recomposição.

*   **Algoritmo:** Múltiplas chamadas de atualização de estado que ocorrem em rápida sucessão são processadas em lote, resultando em uma única Recomposição da UI.
*   **Impacto:** Reduz a sobrecarga de processamento e garante que a UI seja atualizada de forma atômica e eficiente, em vez de ser atualizada parcialmente várias vezes.

### 6. Evolução da Slot Table

O desenvolvimento futuro da arquitetura do Compose aponta para uma evolução da Slot Table para um sistema de **Tabela de Links Paginada (Paged “Link Table”)**.

*   **Estrutura:** Múltiplos Gap Buffers menores, interligados.
*   **Benefício:** Melhor eficiência de memória para árvores de UI muito grandes e maior facilidade para paralelizar as atualizações, mantendo os benefícios de desempenho O(1) da Slot Table original.
*   **Conceito de SO:** Isso reflete a otimização de memória e a busca por paralelismo em sistemas de alto desempenho.

---


## Page 79

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Tipo</th>
      <th>Complexidade/Princípio</th>
      <th>Aplicação no Compose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gap Buffer</td>
      <td>Estrutura de Dados/Algoritmo</td>
      <td>O(1) Inserção/Deleção local</td>
      <td>Otimização de TextField</td>
    </tr>
    <tr>
      <td>Slot Table</td>
      <td>Estrutura de Dados/Arquitetura</td>
      <td>O(1) Recomposição local</td>
      <td>Núcleo do runtime de UI</td>
    </tr>
    <tr>
      <td>Recomposição</td>
      <td>Algoritmo de Renderização</td>
      <td>Otimização de UI</td>
      <td>Atualização eficiente da tela</td>
    </tr>
    <tr>
      <td>Estabilidade Estrutural</td>
      <td>Princípio de Arquitetura</td>
      <td>Otimização de Skipping</td>
      <td>Maximiza o pulo de slots</td>
    </tr>
    <tr>
      <td>Chaves Estáveis</td>
      <td>Algoritmo de Lista</td>
      <td>Rastreamento de Elementos</td>
      <td>Otimização de LazyColumn/Row</td>
    </tr>
    <tr>
      <td>State Hoisting</td>
      <td>Padrão de Arquitetura</td>
      <td>Fluxo de Dados Unidirecional</td>
      <td>Gerenciamento de Estado</td>
    </tr>
    <tr>
      <td>Batching de Mudanças</td>
      <td>Algoritmo de Transação</td>
      <td>Agrupamento de Atualizações</td>
      <td>Redução de Recomposições</td>
    </tr>
    <tr>
      <td>Tabela de Links Paginada</td>
      <td>Estrutura de Dados (Futura)</td>
      <td>Paralelismo e Memória</td>
      <td>Evolução da Slot Table</td>
    </tr>
  </tbody>
</table>

---

## Pesquisador 13: Dennis Ritchie

**Itens Técnicos Encontrados:** 23

**Contribuições:** Linguagem C, Modelo de Ponteiros Tipados, Aritmética de Ponteiros, Operadores ++/–, Arquitetura Unix, Filosofia de Composição de Programas, Fluxos de Texto como Interface Universal

## Linguagem C (Dennis Ritchie)

### Tipos e Estruturas de Dados

1. **Evolução de Tipos:** Transição de uma linguagem “sem tipo” (BCPL/B, com um único tipo ‘word’ ou ‘cell’) para uma linguagem com estrutura de tipos, introduzindo int e char.
2. **Modelo de Ponteiros:**
   * Em BCPL/B, ponteiros eram índices inteiros em um array de palavras, exigindo conversão de escala em tempo de execução (word-addressed).
   * Em C, ponteiros se tornaram endereços de máquina endereçados por byte, eliminando a sobrecarga de escala em tempo de execução.
3. **Aritmética de Ponteiros Tipada:** A aritmética de ponteiros em C (ex: ponteiro + i) passou a depender do tipo de dado, escalando o valor i pelo tamanho do objeto apontado (ex: sizeof(tipo)).
4. **Tratamento de Arrays:** A regra crucial de C: um valor de tipo array, quando aparece em uma expressão, é convertido em um ponteiro para o primeiro objeto do array. Isso permitiu a composição de tipos mais complexos (como struct contendo arrays) sem a necessidade de armazenar o ponteiro base dentro da estrutura.
5. **Sintaxe de Declaração Analógica:** A sintaxe de declaração de variáveis reflete o uso em expressões (ex: int *pi; onde *pi é um int). Isso se aplica a ponteiros, arrays, funções e ponteiros para funções/arrays.
6. **Estruturas (Structs):** Introdução de tipos compostos (registros) que mapeiam de forma intuitiva para a memória da máquina, como em struct { int inumber; char name[14]; }.

### Algoritmos e Operadores

1. **Operadores de Atribuição Generalizada:** Introdução de operadores como +=, -=, etc. (originalmente x=+y em B, corrigido para x+=y em C).
2. **Operadores de Incremento/Decremento:** Criação dos operadores ++ e -- (prefixo e posfixo), que permitem a alteração do valor antes ou depois de sua avaliação.

---


## Page 80

# Arquitetura de Sistemas e Compilação

1.  **Linguagem de Implementação de Sistemas:** C foi concebida como uma linguagem de alto nível para escrever sistemas operacionais (como o Unix), competindo em velocidade e tamanho de código com a linguagem assembly.
2.  **Modelo de Compilação:** Transição do “threaded code” (código interpretado) do B para a geração de instruções de máquina PDP-11 diretamente pelo compilador C.
3.  **Compilação Separada:** Uso de um *linker* convencional para resolver nomes externos em arquivos compilados separadamente, em contraste com o mecanismo de “vetor global” do BCPL.

# Filosofia Unix (Dennis Ritchie e Colaboradores)

## Conceitos de Sistemas Operacionais e Arquitetura

1.  **Processo:** Noção explícita de um **processo** como um locus de controle (herdado do Multics).
2.  **Sistema de Arquivos:** Implementação de um **sistema de arquivos** em estrutura de **árvore**.
3.  **Shell como Programa de Nível de Usuário:** O interpretador de comandos (shell) é um programa de nível de usuário, não parte do kernel, facilitando sua substituição e extensão.
4.  **Acesso Generalizado a Dispositivos:** Tratamento de dispositivos de E/S de forma unificada, como arquivos.
5.  **Princípio da Modularidade e Composição:**
    *   DOTADIW (Do One Thing And Do It Well): Cada programa deve fazer uma coisa e fazê-la bem.
    *   Composição: O poder do sistema reside nas relações entre os programas, que são combinados para realizar tarefas complexas (em oposição a um design monolítico).
6.  **Protocolo de Interface Universal:** Uso de **fluxos de texto** (text streams) como interface universal entre programas.
7.  **Filtro:** O conceito de que cada programa deve ser um **filtro**, lendo de uma entrada padrão e escrevendo para uma saída padrão.
8.  **Mecanismos vs. Política:** Separação clara entre mecanismos (como fazer algo) e política (o que fazer), permitindo flexibilidade e customização.
9.  **Portabilidade:** Ênfase na portabilidade do código e do sistema operacional, em detrimento da otimização extrema para uma arquitetura específica.
10. **Desenvolvimento Iterativo:** Design e construção de software para ser testado rapidamente (prototipagem), com disposição para descartar e reconstruir partes desajeitadas.
11. **Minimalismo:** Ênfase na simplicidade e no minimalismo do código e da interface.
12. **Estrutura de Dados Simples:** Preferência por armazenar dados em **arquivos de texto simples** (flat text files) para facilitar a interoperabilidade.

# Pesquisador 14: Ken Thompson

**Itens Técnicos Encontrados:** 19

**Contribuições:** i-node, Fork/Exec/Pipe, Kernel Minimalista, Sistema de I/O Unificado, Buffer Cache, Algoritmo de Cache LRU, Prioridade de Espera

# Conteúdo Técnico do Trabalho de Ken Thompson (Unix)

O trabalho de Ken Thompson, em colaboração com Dennis Ritchie, no desenvolvimento do sistema operacional **Unix** introduziu uma série de conceitos, estruturas de dados e algoritmos que se tornaram a base da computação moderna. A análise técnica foca exclusivamente nos mecanismos internos do sistema, conforme detalhado nos artigos “The UNIX Time-Sharing System” e “UNIX Implementation” [1] [2].

---


## Page 81

# Arquitetura de Sistemas e Conceitos de SO

A arquitetura do Unix é definida por um **Kernel Minimalista** que implementa apenas o “denominador comum mínimo” de funcionalidades, delegando a maior parte das tarefas a programas de usuário [2]. Este design promove a simplicidade e a robustez.

O sistema adota o princípio de **Sistema de I/O Unificado**, onde todos os dispositivos de entrada/saída (disco, terminal, fita) são tratados como arquivos, simplificando drasticamente a interface do kernel e o desenvolvimento de **Drivers de Dispositivo** [1].

O **Shell** (interpretador de comandos) é implementado como um programa de usuário, e não como parte do kernel. Ele utiliza as chamadas de sistema fundamentais para orquestrar a execução de programas, incluindo **Redirecionamento de I/O** e o conceito de **Pipeline** [1].

# Gerenciamento de Processos

O modelo de gerenciamento de processos do Unix é baseado em um conjunto de chamadas de sistema que definem a criação e a execução de um **Processo**:

<table>
  <thead>
    <tr>
      <th>Chamada de Sistema</th>
      <th>Função Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fork</td>
      <td>Criação de processos. O processo filho é uma cópia exata do processo pai, incluindo o espaço de endereço e o estado do processo.</td>
    </tr>
    <tr>
      <td>Exec</td>
      <td>Substitui a imagem do processo atual por uma nova imagem de programa, permitindo que o processo filho execute um programa diferente.</td>
    </tr>
    <tr>
      <td>Pipe</td>
      <td>Mecanismo de Comunicação Interprocessos (IPC) que conecta a saída padrão de um processo à entrada padrão de outro, viabilizando o conceito de pipeline.</td>
    </tr>
    <tr>
      <td>Swapping</td>
      <td>Algoritmo de gerenciamento de memória que move processos inteiros entre a memória principal e o disco (área de swap) para otimizar o uso da memória [1].</td>
    </tr>
  </tbody>
</table>

# Estruturas de Dados de Processo

O kernel mantém estruturas de dados específicas para o gerenciamento de processos [2]:

1.  **Tabela de Processos (Process Table):** Uma entrada por processo, contendo informações necessárias quando o processo está inativo (nome, localização do segmento de texto, informações de agendamento).
2.  **Segmento de Sistema (System Segment/u-area):** Uma estrutura de dados de tamanho fixo que é trocada (swapped) com o processo. Contém dados necessários apenas quando o processo está ativo (registradores da CPU, descritores de arquivo abertos, stack para a fase de sistema).
3.  **Segmentos de Texto (Text Segments):** Segmentos de código *read-only* que são compartilhados entre múltiplos processos, gerenciados por uma **Tabela de Texto (Text Table)** para rastrear a contagem de compartilhamento e a localização na memória secundária.
4.  **Segmentos de Dados (Data Segments):** Segmentos *read-write* estritamente privados para cada processo, com duas fronteiras de crescimento (heap e stack).

# Sistema de Arquivos (File System)

O sistema de arquivos do Unix é hierárquico e implementado através de estruturas de dados e algoritmos específicos [1]:

## Estruturas de Dados

1.  **i-node (índice de nó):** A estrutura de dados central que descreve um arquivo. Contém metadados (tipo, proprietário, permissões, datas, tamanho) e, crucialmente, a **Lista de Endereços de Blocos de Disco**. Esta lista utiliza um esquema de

---


## Page 82

endereçamento multinível (direto, indireto, duplamente indireto e triplamente indireto) para permitir o acesso eficiente a arquivos de qualquer tamanho.

2. **Diretório**: Um arquivo ordinário que mapeia nomes de arquivo (14 caracteres) para números de i-node.
3. **Super Bloco**: Contém o estado do sistema de arquivos, incluindo o tamanho do sistema de arquivos e a lista de i-nodes livres.
4. **Buffer Cache**: Uma estrutura de cache para blocos de disco, essencial para o desempenho de I/O.

## Algoritmos e Protocolos

1.  **Algoritmo de Busca de Caminho (Pathname Search)**: Inicia no i-node do diretório raiz e percorre a hierarquia de diretórios, lendo as entradas de diretório para encontrar o i-node correspondente a cada componente do caminho.
2.  **Algoritmo de Alocação de Espaço em Disco**: Gerencia a alocação de blocos de dados a partir de uma lista de blocos livres mantida no Super Bloco.
3.  **Algoritmo de Cache de Buffer (LRU)**: O sistema de cache de buffer utiliza uma lista de blocos usados recentemente (LRU - Least Recently Used) para decidir quais blocos descartar quando um novo bloco precisa ser carregado do disco [2].
4.  **Prioridade de Espera (Wait Priority)**: Mecanismo de sincronização do kernel usado para controlar o acesso a recursos compartilhados, como o cache de buffer e a tabela de processos [2].

---

[1] D. M. Ritchie and K. Thompson, “The UNIX Time-Sharing System,” Communications of the ACM, vol. 17, no. 7, pp. 365–375, Jul. 1974. [2] K. Thompson, “UNIX Implementation,” The Bell System Technical Journal, vol. 57, no. 6, pp. 1931–1946, Jul.–Aug. 1978.

---

## Pesquisador 15: Butler W. Lampson

**Itens Técnicos Encontrados:** 25

**Contribuições:** Matriz de Acesso, Domínios de Proteção, Listas de Capacidades (C-lists), Listas de Controle de Acesso (ACLs), Serviço de Nomes Global, Arquitetura Hierárquica de Naming, Princípio do Mínimo Privilégio

## Conteúdo Técnico do Trabalho de Butler Lampson: Princípios de SO, Proteção e Nomenclatura

O conteúdo técnico a seguir é extraído dos trabalhos de Butler Lampson, notavelmente “Protection” (1971/1974) e “Designing a Global Name Service” (1986), focando em algoritmos, estruturas de dados, protocolos, arquitetura de sistemas e conceitos de sistemas operacionais (SO).

### I. Modelo Formal de Proteção (Matriz de Controle de Acesso)

O modelo de proteção é formalizado através de um Sistema de Objetos (*Object System*) que define o estado de proteção de um sistema.

---


## Page 83

# Estruturas e Conceitos Fundamentais

<table>
  <thead>
    <tr>
      <th>Conceito</th>
      <th>Estrutura/Tipo</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Objeto (X)</td>
      <td>Entidade do Sistema</td>
      <td>Qualquer recurso que precisa ser protegido (e.g., processos, domínios, arquivos, segmentos). Possui um **nome** com validade global (e.g., inteiro de 64 bits).</td>
    </tr>
    <tr>
      <td>Domínio (D)</td>
      <td>Entidade de Execução</td>
      <td>Entidade que possui acesso aos objetos (sujeito). Um domínio é definido pelo conjunto de direitos de acesso que possui em um dado momento. Domínios são também **objetos**.</td>
    </tr>
    <tr>
      <td>Matriz de Acesso (A)</td>
      <td>Matriz Abstrata</td>
      <td>Estrutura de dados abstrata onde as linhas são indexadas por **Domínios** e as colunas por **Objetos**. A entrada $A[d,x]$ contém o conjunto de **direitos de acesso** que o domínio $d$ tem sobre o objeto $x$.</td>
    </tr>
    <tr>
      <td>Direitos de Acesso</td>
      <td>Conjunto de Operações</td>
      <td>Operações permitidas sobre um objeto (e.g., read, write, execute, append, control).</td>
    </tr>
    <tr>
      <td>Domínio de Proteção</td>
      <td>Conceito de SO</td>
      <td>O conjunto de pares (objeto, direitos) acessíveis a um processo em um dado momento. É a base para a implementação do **Princípio do Mínimo Privilégio**.</td>
    </tr>
  </tbody>
</table>

# Estruturas de Dados para Implementação

O modelo abstrato da Matriz de Acesso pode ser implementado por diferentes estruturas de dados:

1.  **Listas de Capacidades (C-lists):**
    *   **Estrutura:** Armazenamento por linha (domínio). Cada domínio $d$ possui uma **lista de capacidades**.
    *   **Capacidade:** Par ordenado $(x,r)$, onde $x$ é o nome do objeto e $r$ é o conjunto de direitos. A capacidade atua como um **nome protegido** ou “ticket” que confere direitos.
    *   **Algoritmo de Acesso:** Para acessar o objeto $x$ com direito $r$, o sistema verifica se o domínio possui uma capacidade $(x,r')$ tal que $r \subseteq r'$. A integridade da capacidade deve ser garantida pelo **Kernel de Proteção**.

2.  **Listas de Controle de Acesso (ACLs):**
    *   **Estrutura:** Armazenamento por coluna (objeto). Cada objeto $x$ possui uma **Lista de Controle de Acesso**.
    *   **ACL:** Lista de pares ordenados $(d,r)$, onde $d$ é o nome do domínio e $r$ é o conjunto de direitos.
    *   **Algoritmo de Acesso:** Para acessar o objeto $x$ com direito $r$, o sistema verifica se a ACL de $x$ contém um par $(d,r')$ tal que $r \subseteq r'$.

3.  **Chaves de Proteção (Lock-and-Key):**
    *   **Estrutura:** Mecanismo de proteção de memória. Cada segmento (objeto) tem uma **chave** (lock) e cada processo (domínio) tem um conjunto de **chaves** (keys).
    *   **Algoritmo de Acesso:** O acesso é permitido se uma das chaves do processo corresponder à chave do segmento.

# Operações Primitivas (Algoritmos de Modificação)

O modelo define um conjunto de operações primitivas que modificam o estado de proteção (a Matriz de Acesso):

<table>
  <thead>
    <tr>
      <th>Operação</th>
      <th>Sintaxe</th>
      <th>Efeito na Matriz de Acesso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Entrar em Domínio</td>
      <td>enter(d1, d2)</td>
      <td>Muda o domínio de execução de $d1$ para $d2$.</td>
    </tr>
    <tr>
      <td>Adicionar Direito</td>
      <td>get(d, x, r)</td>
      <td>$A[d,x] := A[d,x] \cup \{r\}$</td>
    </tr>
    <tr>
      <td>Remover Direito</td>
      <td>put(d, x, r)</td>
      <td>$A[d,x] := A[d,x] - \{r\}$</td>
    </tr>
    <tr>
      <td>Criar Objeto</td>
      <td>create(x)</td>
      <td>Cria um novo objeto $x$ e um novo domínio $d$ com direitos de control sobre $x$.</td>
    </tr>
    <tr>
      <td>Destruir Objeto</td>
      <td>destroy(x)</td>
      <td>Remove o objeto $x$ e todos os direitos a ele associados.</td>
    </tr>
    <tr>
      <td>Transferir Direito</td>
      <td>transfer(d1, d2, x, r)</td>
      <td>Transfere o direito $r$ de $d1$ para $d2$ sobre $x$ (requer direito copy em $d1$).</td>
    </tr>
    <tr>
      <td>Restringir Direito</td>
      <td>limit(d, x, r)</td>
      <td>$A[d,x] := A[d,x] \cap \{r\}$</td>
    </tr>
  </tbody>
</table>

---


## Page 84

# II. Arquitetura e Estruturas de Nomenclatura (Naming)

O trabalho sobre Serviço de Nomes Global (Global Name Service) define uma arquitetura para mapeamento de nomes em sistemas distribuídos.

## Arquitetura Hierárquica e Estruturas de Dados

O serviço de nomes mapeia um **nome** de uma entidade para um conjunto de **propriedades rotuladas** (e.g., network address=...).

<table>
  <thead>
    <tr>
      <th>Estrutura/Conceito</th>
      <th>Tipo</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Serviço de Nomes Global</td>
      <td>Arquitetura de SO Distribuído</td>
      <td>Base para localização de recursos, endereçamento de e-mail e autenticação em larga escala (bilhões de nomes).</td>
    </tr>
    <tr>
      <td>Estrutura Hierárquica</td>
      <td>Arquitetura</td>
      <td>Método fundamental para acomodar Escalabilidade (Large Size) e Isolamento de Falhas (Fault Isolation).</td>
    </tr>
    <tr>
      <td>Diretório</td>
      <td>Estrutura de Dados</td>
      <td>Nó na árvore hierárquica, possui um Identificador de Diretório (DI) único.</td>
    </tr>
    <tr>
      <td>Referência de Diretório (DR)</td>
      <td>Estrutura de Dados</td>
      <td>Arco na árvore, consiste no DI do diretório filho.</td>
    </tr>
    <tr>
      <td>Nome Completo (FN)</td>
      <td>Protocolo de Nomenclatura</td>
      <td>Nome de caminho (path name) relativo a uma raiz (e.g., ANSI/DEC/SRC ).</td>
    </tr>
    <tr>
      <td>Árvore de Valores</td>
      <td>Estrutura de Dados</td>
      <td>Estrutura interna de um diretório, mapeando um Caminho (sequência de Rótulos) para um valor.</td>
    </tr>
    <tr>
      <td>Nó</td>
      <td>Estrutura de Dados</td>
      <td>Elemento da Árvore de Valores, carrega um Timestamp (TS) para sincronização e uma marca de presença/ausência.</td>
    </tr>
    <tr>
      <td>Links</td>
      <td>Estrutura de Dados</td>
      <td>Um valor de nome que é outro Nome Completo (FN), permitindo que diferentes caminhos levem ao mesmo recurso.</td>
    </tr>
  </tbody>
</table>

## Princípios de Arquitetura de Sistemas Distribuídos

O design do Serviço de Nomes é guiado por requisitos técnicos rigorosos:

*   **Alta Disponibilidade (High Availability):** O sistema deve continuar funcionando mesmo com falhas localizadas.
*   **Tolerância à Desconfiança (Tolerance of Mistrust):** O design deve funcionar em um ambiente onde nem todos os componentes são totalmente confiáveis.
*   **Replicação e Sincronização:** O nível administrativo lida com a distribuição e sincronização de cópias do banco de dados de nomes.
*   **Não-Determinismo:** O comportamento não-determinístico do serviço é precisamente especificado para permitir flexibilidade de implementação.

---


## Page 85

# III. Consolidação de Algoritmos, Estruturas e Conceitos

<table>
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Algoritmos/Protocolos</th>
      <th>Estruturas de Dados</th>
      <th>Conceitos de SO/Arquitetura</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Proteção</td>
      <td>Algoritmo de Acesso (C-list/ACL), Operações Primitivas (get, put, transfer, limit, create, destroy, enter).</td>
      <td>Matriz de Acesso (Abstrata), Lista de Capacidades (C-list), Capacidade, Lista de Controle de Acesso (ACL), Chaves de Proteção.</td>
      <td>Domínio de Proteção, Objeto, Princípio do Mínimo Privilégio, Kernel de Proteção.</td>
    </tr>
    <tr>
      <td>Nomenclatura</td>
      <td>Protocolo de Nomenclatura Hierárquica, Protocolo de Sincronização (via Timestamp).</td>
      <td>Serviço de Nomes Global, Diretório (com DI), Referência de Diretório (DR), Nome Completo (FN), Árvore de Valores (com Rótulos e TS), Links.</td>
      <td>Escalabilidade, Alta Disponibilidade, Isolamento de Falhas, Tolerância à Desconfiança.</td>
    </tr>
    <tr>
      <td>Intersecção</td>
      <td>Protocolo de Autenticação (baseado em Naming).</td>
      <td>Capacidade como Nome Protegido.</td>
      <td>Relação entre Naming e Protection.</td>
    </tr>
  </tbody>
</table>

## Pesquisador 16: Jerome H. Saltzer

Itens Técnicos Encontrados: 25

Contribuições: Princípio Ponta a Ponta, Princípios de Design de Segurança (Economia de Mecanismo, Mediação Completa, Design Aberto, Separação de Privilégios, Menor Privilégio, Mecanismos de Proteção, Aceitabilidade), Arquitetura de Proteção Baseada em Descritores, Listas de Controle de Acesso (ACLs), Sistemas de Capacidade (Capabilities)

## Conteúdo Técnico do Trabalho de Jerome H. Saltzer

O trabalho de Jerome H. Saltzer, notavelmente em “End-to-End Arguments in System Design” (com Reed e Clark) e “The Protection of Information in Computer Systems” (com Schroeder), estabelece conceitos fundamentais de **arquitetura de sistemas** e **conceitos de sistemas operacionais** (SO), com foco em proteção e confiabilidade.

### 1. Princípio Ponta a Ponta (End-to-End Argument)

O princípio ponta a ponta é um argumento de arquitetura de sistemas que sugere que as funções de controle de correção e integridade devem ser implementadas nas camadas mais altas (aplicação) do sistema, ou seja, nas “pontas” da comunicação.

*   **Conceito de Arquitetura:** O princípio argumenta que a função de correção (e.g., garantia de entrega, supressão de duplicatas, segurança) só pode ser implementada de forma **completa e correta** com o conhecimento e a ajuda da aplicação que está nas extremidades da comunicação.
*   **Implicação em Protocolos:** A implementação de mecanismos de confiabilidade em camadas inferiores (e.g., na rede) é vista como uma otimização de desempenho, e não como um requisito de correção.
*   **Exemplos de Aplicação (Conceitos de SO/Protocolos):**
    *   **Confiabilidade de Dados:** Um checksum de arquivo (aplicação) é necessário para garantir a transferência correta, independentemente da confiabilidade do protocolo de transporte (camada inferior).
    *   **Reconhecimento de Entrega (Delivery Acknowledgement):** O reconhecimento significativo deve ser gerado pela aplicação de destino (“Eu fiz”), e não pelo subsistema de comunicação (“Eu entreguei”).
    *   **Supressão de Mensagens Duplicadas:** A aplicação deve ser capaz de lidar com duplicatas (devido a retentativas de falha), mesmo que a rede tente suprimi-las, pois a aplicação pode gerar duplicatas lógicas.
    *   **Criptografia:** A criptografia ponta a ponta (aplicação) é necessária para autenticação e gerenciamento seguro de chaves, enquanto a criptografia de rede (camada inferior) serve apenas como uma “parede de fogo” de segurança.
    *   **Gerenciamento de Transações:** O uso de protocolos de **confirmação de duas fases (two-phase commit)** é um exemplo de protocolo ponta a ponta sofisticado para garantir a atomicidade de ações distribuídas.

---


## Page 86

# 2. Princípios de Design de Mecanismos de Proteção

O trabalho com Schroeder define um conjunto de princípios de **design de sistemas** para a criação e avaliação de **mecanismos de proteção** em sistemas operacionais.

<table>
  <thead>
    <tr>
      <th>Princípio</th>
      <th>Conceito Técnico</th>
      <th>Aplicação em Arquitetura/SO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Economia de Mecanismo (Economy of Mechanism)</td>
      <td>Manter o design de segurança o mais simples e pequeno possível.</td>
      <td>Reduz a probabilidade de erros de implementação e facilita a verificação de correção.</td>
    </tr>
    <tr>
      <td>Mediação Completa (Complete Mediation)</td>
      <td>Todos os acessos a todos os objetos devem ser verificados quanto à autoridade.</td>
      <td>Requisito fundamental para a implementação de um núcleo de segurança (security kernel).</td>
    </tr>
    <tr>
      <td>Design Aberto (Open Design)</td>
      <td>O mecanismo de proteção não deve depender do sigilo de seu design ou implementação.</td>
      <td>A segurança reside na chave ou senha, e não na obscuridade do algoritmo.</td>
    </tr>
    <tr>
      <td>Separação de Privilégios (Separation of Privilege)</td>
      <td>O acesso a um objeto deve depender de mais de uma condição (e.g., duas chaves).</td>
      <td>Aumenta a segurança ao exigir múltiplas autorizações para operações críticas.</td>
    </tr>
    <tr>
      <td>Menor Privilégio (Least Privilege)</td>
      <td>Cada processo ou usuário deve ter o conjunto mínimo de privilégios necessários para completar seu trabalho.</td>
      <td>Reduz o dano potencial em caso de comprometimento de um componente.</td>
    </tr>
    <tr>
      <td>Mecanismos de Proteção (Protection Mechanisms)</td>
      <td>Mecanismos de proteção devem ser aceitáveis (fáceis de usar) e validados (testados e verificados).</td>
      <td>Foco na usabilidade e na correção formal dos mecanismos de controle de acesso.</td>
    </tr>
    <tr>
      <td>Aceitabilidade (Acceptability)</td>
      <td>O mecanismo de proteção deve ser simples, fácil de usar e não interferir no trabalho do usuário.</td>
      <td>Um mecanismo complexo ou inconveniente será contornado pelos usuários.</td>
    </tr>
  </tbody>
</table>

# 3. Arquiteturas de Proteção (Estruturas de Dados e Conceitos de SO)

O artigo detalha as estruturas de dados e arquiteturas de SO usadas para implementar o controle de acesso.

*   Matriz de Acesso (Access Matrix):
    *   Estrutura: Linhas representam sujeitos (usuários, processos) e colunas representam objetos (arquivos, dispositivos). As entradas contêm o conjunto de direitos de acesso (leitura, escrita, execução).
*   Listas de Controle de Acesso (Access Control Lists - ACLs): Uma forma de implementar a Matriz de Acesso.
    *   Estrutura: Associada a cada objeto, uma lista de sujeitos e seus respectivos direitos.
    *   Conceito de SO: O sistema verifica a ACL do objeto para determinar se o sujeito tem permissão.
*   Sistemas de Capacidade (Capability Systems): Outra forma de implementar a Matriz de Acesso.
    *   Estrutura: Associada a cada sujeito, uma lista de capacidades (capabilities). Uma capacidade é um token que combina a identidade de um objeto com os direitos de acesso permitidos.
    *   Conceito de SO: A capacidade atua como um “bilhete” que o sujeito apresenta para acessar o objeto. A posse da capacidade confere o direito.
*   Arquitetura Baseada em Descritores (Descriptor-Based Protection): Um conceito de arquitetura de hardware e SO, como no sistema Multics.
    *   Estrutura: Uso de descritores (estruturas de dados) para gerenciar o endereçamento e a proteção da memória. Um descritor contém o endereço base, o limite e os bits de permissão (leitura/escrita/execução).
    *   Conceito de SO: Separação de endereçamento e proteção. O hardware usa o descritor para mapear endereços virtuais para físicos e, simultaneamente, verificar as permissões de acesso.
*   Domínios de Proteção (Protection Domains): Conceito de SO onde um conjunto de pares (objeto, direitos) define o ambiente de execução de um processo. A mudança de domínio é um mecanismo de controle de acesso.

Algoritmos/Protocolos Implícitos:

*   Protocolo de Confirmação de Duas Fases (Two-Phase Commit - 2PC): Protocolo de transação distribuída (mentcionado como um protocolo ponta a ponta sofisticado) para garantir que todos os participantes de uma transação distribuída concordem em confirmar ou abortar a operação.

---


## Page 87

*   **Algoritmos de Autenticação:** Uso de senhas e criptografia (como Diffie-Hellman) para verificar a identidade do usuário ou da mensagem.
*   **Algoritmos de Checksum:** Uso de redundância (checksums) para detecção de erros de bit.
*   **Protocolos de Retentativa (Retry Protocols):** Algoritmos de controle de fluxo e recuperação de falhas que operam em diferentes camadas (rede ou aplicação) para retransmitir dados perdidos ou corrompidos.
*   **Mecanismos de Autenticação:** Uso de chaves e identificadores para verificar a identidade do usuário.
*   **Mecanismos de Controle de Acesso:** Algoritmos de busca e comparação para verificar direitos em ACLs ou Capabilities.

**Estruturas de Dados:**

*   Matriz de Acesso (Conceitual)
*   Listas de Controle de Acesso (ACLs)
*   Capacidades (Capabilities)
*   Descritores de Segmento (Multics-like)
*   Checksums (para integridade de dados)
*   Números de Sequência (para ordenação e detecção de duplicatas)

---

## Pesquisador 17: David Wheeler

**Itens Técnicos Encontrados:** 10

**Contribuições:** Princípio da Indireção, Sub-rotina Fechada, Rotina Interpretativa, Algoritmo de Chamada e Retorno, Tabela de Páginas (Implícita)

## Conteúdo Técnico: Indireção e Memória Virtual no Trabalho de David Wheeler

### Conceitos de Sistemas Operacionais e Arquitetura

#### Princípio da Indireção

O princípio fundamental de indireção é a base para a solução de problemas complexos em ciência da computação, sendo a Memória Virtual uma de suas aplicações mais diretas. A indireção é a técnica de referenciar um valor ou recurso através de um intermediário (um nome, referência ou contêiner) em vez de acessar o valor diretamente.

#### Memória Virtual

A Memória Virtual é uma aplicação arquitetural do princípio da indireção, onde um endereço lógico (virtual) é mapeado para um endereço físico (real). Este mapeamento é realizado por uma estrutura de dados de tradução de endereços, como a Tabela de Páginas, e é um conceito essencial de Gerenciamento de Memória em Sistemas Operacionais.

#### Sub-rotina Fechada (Closed Sub-routine)

A invenção da sub-rotina fechada no EDSAC estabeleceu um conceito arquitetural de modularidade e reuso de código. Uma sub-rotina é uma entidade autocontida que permite a quebra do código em partes menores e testáveis, reduzindo a incidência de erros no programa principal.

---


## Page 88

# Rotina Interpretativa

A rotina interpretativa é um conceito de arquitetura de sistema onde uma sub-rotina é organizada para executar uma sequência de operações (‘ordens’) determinadas por um parâmetro de entrada. As ‘ordens’ são idênticas às da máquina, mas a rotina interpretativa retém o controle para fornecer informações extras sobre o curso do programa, funcionando como um mecanismo primitivo de depuração e rastreamento em tempo de execução.

# Algoritmos

## Algoritmo de Chamada e Retorno de Sub-rotina

O algoritmo de transferência de controle para a sub-rotina fechada envolve a seguinte sequência de operações:

1.  **Transferência de Controle:** O controle é transferido do programa principal para o endereço inicial da sub-rotina.
2.  **Execução:** A sub-rotina executa sua lógica de cálculo.
3.  **Retorno:** O controle é retornado ao ponto no programa principal imediatamente após a instrução de chamada. No EDSAC, este mecanismo era implementado por um arranjo que garantia o retorno ao endereço correto.

## Algoritmo de Tradução de Endereços (Sub-rotinas)

Para sub-rotinas armazenadas em uma **forma invariante** (como em uma biblioteca de fita de papel), um processo de tradução de endereços é necessário antes da execução. Este algoritmo aplica **regras fixas** para ajustar os endereços internos da sub-rotina ao seu novo local na memória principal, garantindo que a sub-rotina seja executável no conjunto de locais em que é usada.

## Algoritmo de Interpretação

O algoritmo da rotina interpretativa envolve a leitura sequencial de ‘ordens’ (parâmetros) e a execução da operação correspondente, que simula as instruções da máquina. Este processo é repetido a cada chamada da sub-rotina, permitindo a execução de código dinâmico ou a simulação de um conjunto de instruções.

# Estruturas de Dados

## Biblioteca de Sub-rotinas

Uma **estrutura de dados** para armazenar e gerenciar sub-rotinas reutilizáveis, inicialmente implementada como um conjunto de fitas de papel contendo o código em uma **forma invariante**.

## Tabela de Páginas/Endereços

Embora não detalhada explicitamente por Wheeler em seus trabalhos iniciais sobre sub-rotinas, a aplicação do princípio da indireção à Memória Virtual implica a existência de uma **Tabela de Páginas** (Page Table). Esta estrutura de dados é essencial para o mapeamento de endereços virtuais para endereços físicos, atuando como o intermediário (o “nível de indireção”) no sistema operacional.

## Pilha (Stack)

Apesar do EDSAC usar um mecanismo de retorno fixo, o conceito de sub-rotina é o precursor direto da estrutura de dados **Pilha (Stack)**, que é usada em arquiteturas modernas para gerenciar o empilhamento de chamadas de sub-rotinas e o armazenamento de endereços de retorno e variáveis locais.

# Pesquisador 18: Maurice Vincent Wilkes

Itens Técnicos Encontrados: 27

---


## Page 89

Contribuições: Microprogramação, Memória Escrava (Cache), Mapeamento Direto, Protocolo Write-Back, Algoritmo de Execução de Micro-instrução

# Conteúdo Técnico: Microprogramação e Memória Escrava (Cache) de Maurice Wilkes

O trabalho de Maurice Wilkes introduziu dois conceitos fundamentais na arquitetura de computadores e sistemas operacionais: a **Microprogramação** (1951) e a **Memória Escrava** (1965), precursora da memória cache.

## 1. Microprogramação (Micro-programming)

### Arquitetura de Sistemas e Estruturas de Dados

A microprogramação define a unidade de controle de um processador como um sistema baseado em memória, substituindo a lógica de estado finito (hardwired).

*   **Estrutura de Dados (Memória de Controle):** O microprograma é armazenado em uma Matriz de Diodos (ou memória de controle). A palavra de micro-instrução é dividida em campos:
    *   Campo de Controle (Control Field): Bits que geram sinais de controle (micro-operações).
    *   Campo de Endereço (Next Address Field): Endereço da próxima micro-instrução.
    *   Campo de Condição (Conditional Field): Bit para seleção condicional do próximo endereço.
*   **Arquitetura de Controle:** O sistema utiliza duas matrizes e registradores de controle:
    *   Matriz C (Control Matrix): Decodifica o Campo de Controle para gerar os sinais de controle (micro-operações).
    *   Matriz D (Next Micro-instruction Address Matrix): Gera o endereço da próxima micro-instrução.
    *   Registro de Controle I: Armazena o endereço da micro-instrução atual.

### Algoritmos

*   **Algoritmo de Execução de Micro-instrução (Ciclo):**
    1.  O endereço atual do Registro de Controle I é usado para buscar a micro-instrução na Matriz de Diodos.
    2.  A Matriz C executa as micro-operações (e.g., A -> C, Add C to A).
    3.  A Matriz D gera o endereço da próxima micro-instrução.
    4.  **Decisão Condicional (Conditional Branch):** Se o Campo de Condição estiver ativo, o endereço gerado pela Matriz D é modificado por um sinal de teste (e.g., overflow) antes de ser carregado no Registro de Controle I.
*   **Algoritmo de Mapeamento:** O código de operação (opcode) da instrução de máquina de nível superior é mapeado para o endereço inicial da sequência de micro-instruções que a implementa.

### Conceitos de Sistemas Operacionais

*   **Abstração de Hardware:** Cria uma camada de abstração entre o conjunto de instruções visível ao programador e o hardware físico.
*   **Emulação:** Permite que um processador implemente o conjunto de instruções de outro.

## 2. Memória Escrava (Slave Memory)

### Arquitetura de Sistemas e Estruturas de Dados

A Memória Escrava é o conceito original de memória cache, uma memória rápida e pequena que atua como um buffer para uma memória principal mais lenta e maior, buscando reduzir o tempo de acesso efetivo.

*   **Arquitetura de Sistema (Memória Hierárquica):** Consiste em uma Memória de Trabalho Rápida (Memória Escrava, e.g., 32K palavras, 1-µs) e uma Memória Principal Lenta (e.g., 1M palavras, 8-µs).

---


## Page 90

*   **Estrutura de Endereçamento (Mapeamento Direto Simples):** O endereço da memória principal r é mapeado para um registro da memória escrava usando a função **módulo:** r (mod N), onde N é o número de registros na memória escrava.
*   **Estrutura de Dados (Bits de Controle):**
    *   **Bits de Tag (Etiqueta):** Os bits mais significativos do endereço principal são armazenados para identificar qual bloco da memória principal está na memória escrava.
    *   **Bit de Presença/Válido (Tag 1):** Indica se a palavra na memória escrava é válida (1) ou se é necessário buscar na memória principal (0).
    *   **Bit Modificado/Sujo (Tag 2):** Indica se a palavra na memória escrava foi alterada (1) e precisa ser escrita de volta na memória principal.

## Algoritmos e Protocolos

*   **Algoritmo de Busca/Acesso (Hit/Miss):**
    1.  A memória escrava é acessada primeiro no endereço mapeado.
    2.  **Acerto (Hit):** Se o Bit de Presença for 1 e os Bits de Tag coincidirem, a operação é concluída na memória escrava.
    3.  **Falta (Miss):** Se o Bit de Presença for 0, a palavra é copiada da memória principal e o Bit de Presença é definido como 1.
*   **Protocolo de Escrita (Instruções):** Write-Through com Verificação. A palavra é atualizada na memória escrava e na memória principal.
*   **Protocolo de Escrita (Dados/Programas):** Write-Back na troca de contexto. Se a operação for uma escrita, o Bit Modificado é definido como 1.
*   **Algoritmo de Troca de Contexto (Supervisor Scan/Flush):**
    1.  O supervisor inicia uma varredura da memória escrava quando o **Registro Base** é alterado (troca de programa).
    2.  Para cada palavra com Bit de Presença = 1:
        *   Se Bit Modificado = 1, a palavra **deve** ser escrita de volta na memória principal (Write-Back).
        *   Os Bits de Tag são redefinidos para 0 após a varredura.

## Conceitos de Sistemas Operacionais

*   **Gerenciamento de Memória:** Uso de um **Registro Base** para endereçamento de blocos de programas (precursor da segmentação/paginação).
*   **Troca de Contexto:** O supervisor é o responsável por gerenciar o flush da memória escrava (cache) durante a troca de programas em sistemas de time-sharing.
*   **Algoritmo de Escalonamento:** O sistema é projetado para time-sharing on-line, onde programas são ativados por um algoritmo de escalonamento.

---

## Pesquisador 19: Edsger Wybe Dijkstra

Itens Técnicos Encontrados: 18

Contribuições: Semáforos (P e V), Exclusão Mútua, Algoritmo do Banqueiro, Arquitetura em Camadas, Memória Virtual Paginada

---


## Page 91

# Conteúdo Técnico do Trabalho de Edsger Dijkstra

## 1. Semáforos e Exclusão Mútua

### 1.1. Estrutura de Dados: Semáforo (S)

O semáforo é uma variável inteira não negativa utilizada para controle de acesso a recursos compartilhados (exclusão mútua) e sincronização de processos.

### 1.2. Algoritmos: Operações Primitivas (P e V)

As operações P e V (do holandês *Probeer* - testar, e *Verhoog* - aumentar) são as únicas operações atômicas permitidas em um semáforo.

#### Operação P (Wait/Down)

A operação P tenta diminuir o valor do semáforo. Se o valor resultante for negativo, o processo é bloqueado.

**Definição Formal (Pseudocódigo):**

```pseudocode
P(S):
    S := S - 1;
    if S < 0 then
        // Adiciona o processo à fila de espera do semáforo
        // Bloqueia o processo
```

#### Operação V (Signal/Up)

A operação V aumenta o valor do semáforo. Se o valor resultante for menor ou igual a zero, um processo bloqueado é acordado.

**Definição Formal (Pseudocódigo):**

```pseudocode
V(S):
    S := S + 1;
    if S <= 0 then
        // Remove um processo da fila de espera do semáforo
        // Acorda o processo
```

### 1.3. Conceito: Exclusão Mútua

A exclusão mútua é implementada usando um **semáforo binário** (também chamado de *mutex*), inicializado com o valor 1.

**Algoritmo de Exclusão Mútua:**

```pseudocode
begin
    integer mutex; // semáforo binário
    mutex := 1; // valor inicial 1 (livre)
    ...
process:
    begin
        P(mutex); // Entrada na Região Crítica (aguarda se mutex=0)
        // Região Crítica (código que acessa recurso compartilhado)
        V(mutex); // Saída da Região Crítica (libera o recurso)
        // Código não crítico
    end
end

---


## Page 92

# 2. Algoritmo do Banqueiro (Deadlock Avoidance)

O Algoritmo do Banqueiro é um algoritmo de alocação de recursos e prevenção de deadlock (impasse) que garante que o sistema permaneça em um estado seguro.

## 2.1. Estruturas de Dados

Seja n o número de processos e m o número de tipos de recursos.

<table>
  <thead>
    <tr>
      <th>Estrutura</th>
      <th>Tipo</th>
      <th>Dimensão</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Available</td>
      <td>Vetor (1-D)</td>
      <td>m</td>
      <td>Número de instâncias disponíveis de cada tipo de recurso.</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>Matriz (2-D)</td>
      <td>n × m</td>
      <td>Demanda máxima de recursos de cada processo. Max[i, j] é o máximo de instâncias do recurso R<sub>j</sub> que o processo P<sub>i</sub> pode solicitar.</td>
    </tr>
    <tr>
      <td>Allocation</td>
      <td>Matriz (2-D)</td>
      <td>n × m</td>
      <td>Número de instâncias de cada recurso atualmente alocadas a cada processo. Allocation[i, j] é o número de instâncias do recurso R<sub>j</sub> alocadas ao processo P<sub>i</sub>.</td>
    </tr>
    <tr>
      <td>Need</td>
      <td>Matriz (2-D)</td>
      <td>n × m</td>
      <td>Recursos restantes que cada processo ainda precisa. Need[i, j] = Max[i, j] – Allocation[i, j].</td>
    </tr>
  </tbody>
</table>

## 2.2. Algoritmo de Segurança (Safety Algorithm)

O algoritmo verifica se o sistema está em um estado seguro, ou seja, se existe uma sequência de execução de processos que permite que todos os processos concluam suas tarefas.

**Passos:**

1. **Inicialização:**
   * Work = Available (vetor de trabalho)
   * Finish[i] = false para todos os processos P<sub>i</sub>.

2. **Busca:** Encontrar um processo P<sub>i</sub> que satisfaça as seguintes condições:
   * Finish[i] = false
   * Need[i] ≤ Work (o processo pode ser atendido com os recursos disponíveis)

3. **Execução Simulada:** Se tal P<sub>i</sub> for encontrado:
   * Work = Work + Allocation[i] (simula a liberação dos recursos alocados a P<sub>i</sub>)
   * Finish[i] = true
   * Voltar ao Passo 2.

4. **Conclusão:** Se Finish[i] = true para todos os i, o sistema está em um estado seguro.

# 3. Arquitetura do Sistema THE Multiprogramming System

O sistema THE é notável por sua estrutura em camadas (layered structure), um conceito de arquitetura de sistemas operacionais.

## 3.1. Conceito: Estrutura em Camadas

A arquitetura é organizada em uma hierarquia de 6 níveis (Layer 0 a Layer 5), onde cada camada superior depende apenas das funcionalidades fornecidas pelas camadas inferiores.

---


## Page 93

# 3.2. Camadas e Abstrações

<table>
  <thead>
    <tr>
      <th>Camada (Layer)</th>
      <th>Abstração/Conceito de SO</th>
      <th>Funcionalidades Técnicas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Layer 0</td>
      <td>Alocação de Processador</td>
      <td>Gerenciamento de interrupções, context switching, **escalonamento** (*scheduler*) de processos (baseado em semáforos).</td>
    </tr>
    <tr>
      <td>Layer 1</td>
      <td>Alocação de Memória</td>
      <td>Implementação de **memória virtual paginada** baseada em software (sem hardware de MMU), gerenciamento de *backing store* (tambor magnético), algoritmo de substituição de página **LRU** (*Least Recently Used*).</td>
    </tr>
    <tr>
      <td>Layer 2</td>
      <td>Comunicação Console-Processo</td>
      <td>Gerenciamento da comunicação entre o sistema operacional e o console do operador.</td>
    </tr>
    <tr>
      <td>Layer 3</td>
      <td>Gerenciamento de I/O</td>
      <td>Gerenciamento de dispositivos de entrada/saída, incluindo **bufferização** de dados.</td>
    </tr>
    <tr>
      <td>Layer 4</td>
      <td>Programas do Usuário</td>
      <td>Processos de usuário (compilação, execução, impressão). Utiliza uma **fila de escalonamento baseada em prioridade**.</td>
    </tr>
    <tr>
      <td>Layer 5</td>
      <td>Usuário</td>
      <td>(Não implementada pelo sistema, representa a interface final).</td>
    </tr>
  </tbody>
</table>

# 3.3. Estruturas de Dados e Algoritmos Adicionais

*   **Memória Virtual Paginada (Software-based Paged Virtual Memory):** Implementada via *software* (compilador ALGOL modificado) que gera chamadas de sistema para garantir que a informação solicitada esteja na memória principal, realizando *swapping* (troca) se necessário.
*   **Algoritmo LRU (Least Recently Used):** Utilizado para o gerenciamento da memória virtual e substituição de páginas.
*   **Fila de Escalonamento (Priority-based Queue):** Utilizada no Layer 4 para gerenciar a execução dos programas do usuário, favorecendo processos recém-iniciados ou bloqueados por I/O.

---

## Pesquisador 20: Per Brinch Hansen

**Itens Técnicos Encontrados:** 11

**Contribuições:** Monitor Concept, Semântica Signal-and-Exit, Concurrent Pascal, Hierarquia de Direitos de Acesso

O trabalho de Per Brinch Hansen sobre Monitores e programação concorrente, notavelmente em seu artigo “*Concurrent Programming Concepts*” e na linguagem **Concurrent Pascal**, introduziu estruturas e protocolos fundamentais para a sincronização de processos em sistemas operacionais.

### Conceitos de Sistemas Operacionais e Protocolos

1.  **Monitor (Estrutura de Sincronização)** O Monitor é um conceito de estruturação de sistemas operacionais e um mecanismo de sincronização de alto nível. Ele encapsula **dados compartilhados** e as **proceduras** que operam sobre esses dados. O protocolo central do Monitor garante a **Exclusão Mútua** sobre os dados internos: em qualquer instante, no máximo um processo pode estar executando uma das procedimentos do Monitor.

2.  **Variáveis de Condição (Condition Variables)** São estruturas de dados internas ao Monitor, utilizadas para gerenciar a espera de processos por condições específicas. Um processo que encontra uma condição não satisfeita executa a operação `wait(c)`, que o suspende e o coloca em uma **fila de espera** associada à variável de condição `c`, liberando a exclusão mútua do Monitor.

3.  **Semântica Signal-and-Exit (Protocolo de Brinch Hansen)** A semântica original de Brinch Hansen para a operação `signal(c)` é conhecida como **Signal-and-Exit**. Quando um processo executa `signal(c)`:
    *   Um processo suspenso na fila de espera `c` é despertado.
    *   O processo sinalizador é obrigado a sair imediatamente do Monitor (exit), permitindo que o processo despertado entre no Monitor e continue sua execução. Este protocolo evita a complexidade do *transfer of control* e a necessidade de uma fila de urgência, simplificando a implementação em comparação com a semântica Signal-and-Wait de Hoare.

---


## Page 94

4. Arquitetura de Sistemas (Programação Estruturada Concorrente) O conceito de Monitor, juntamente com o tipo **Processo**, forma a base para a **Programação Estruturada Concorrente**. Essa arquitetura permite a construção de sistemas operacionais (como o Sistema Operacional SOLO) onde a sincronização é verificada em tempo de compilação, garantindo a ausência de deadlocks e race conditions relacionados à exclusão mútua.

## Estruturas de Dados em Concurrent Pascal

A linguagem Concurrent Pascal, desenvolvida por Brinch Hansen, implementa o conceito de Monitor através de três tipos de dados estruturados que definem a arquitetura do sistema:

1.  **Tipo Process (Process Type)** Define uma unidade de execução concorrente. Um processo é uma sequência de instruções que pode ser executada em paralelo com outros processos.
2.  **Tipo Monitor (Monitor Type)** Define uma estrutura de dados compartilhada e as operações sincronizadas sobre ela. O Monitor é composto por:
    *   **Dados Compartilhados**: Variáveis acessíveis apenas pelas procedimentos do Monitor.
    *   **Procedimentos de Monitor**: Operações que garantem exclusão mútua.
    *   **Variáveis de Condição**: Filas de espera para sincronização interna.
    *   **Operação Inicial**: Código executado uma única vez para inicializar os dados.
3.  **Tipo Classe (Class Type)** Define uma estrutura de dados com operações, similar ao Monitor, mas **sem exclusão mútua** e sem variáveis de condição. É usado para encapsular dados privados que não são compartilhados entre processos concorrentes, ou que são compartilhados de forma segura dentro de um Monitor.
4.  **Hierarquia de Direitos de Acesso** Concurrent Pascal impõe uma **hierarquia de acesso** estrita entre os tipos de dados:
    *   Um **Processo** pode acessar **Classes** e **Monitores**.
    *   Um **Monitor** pode acessar **Classes** e outros **Monitores** (desde que não haja chamadas circulares, para evitar deadlocks).
    *   Uma **Classe** só pode acessar outras **Classes**. Essa restrição de arquitetura é verificada pelo compilador, garantindo que a estrutura do sistema seja segura e hierárquica.

## Algoritmos e Implementação

A implementação do Monitor de Brinch Hansen, especialmente em Concurrent Pascal, utiliza mecanismos de baixo nível (como semáforos) para gerenciar as filas de entrada e as filas de condição, embora o programador use apenas as abstrações de alto nível (wait e signal). O algoritmo de controle de acesso ao Monitor envolve:

1.  **Fila de Entrada**: Uma fila de processos esperando para entrar no Monitor (garantindo exclusão mútua).
2.  **Fila de Condição**: Uma fila de processos esperando por uma condição específica (c.wait).
3.  **Algoritmo de Retomada**: O protocolo Signal-and-Exit garante que, após um signal, o processo despertado (c.signal) tem prioridade para entrar no Monitor antes de qualquer processo na Fila de Entrada.
4.  **Estrutura de Dados**: As filas de espera são implementadas como **filas FIFO** (First-In, First-Out) para garantir justiça na ordem de atendimento dos processos.