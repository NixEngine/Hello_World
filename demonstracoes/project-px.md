# Seus arquivos, sua inspeção: Project Px

**Examine arquivos escolhidos por você e gere um resumo SHA-256 sem exibir o conteúdo por padrão.** A Zero Px Core está desenvolvendo ferramentas de inspeção local e evidências técnicas para equipes que precisam compreender o que foi analisado e conferir se bytes mudaram.

## O que demonstramos

- Um protótipo lê um arquivo selecionado em blocos e calcula SHA-256. Uma opção separada permite visualizar uma pequena amostra de bytes quando solicitada.
- No X9 Linux, o protótipo passou em **12 verificações com arquivos sintéticos**, incluindo comparação dos resumos com outra implementação.
- Em um ensaio separado, verificamos a assinatura e a integridade de uma fotografia sintética, rejeitamos alterações e mantivemos explícito um estado ainda incerto.
- Em outro ensaio, consultamos em leitura uma transação histórica da **testnet Stellar** e a relacionamos a um novo diário local. Foram aprovadas **11 verificações**, incluindo controles com dados alterados. A observação veio de um único servidor Horizon por HTTPS; a assinatura é local.

### Um exemplo pequeno

Para o arquivo sintético de três bytes que contém `abc`, o protótipo leu três bytes e calculou:

`SHA-256: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`

O resultado coincidiu com uma segunda implementação. A amostra de conteúdo não foi solicitada nessa execução.

## Onde podemos colaborar

- Inspeção local de arquivos e comparação com referências fornecidas pelo cliente.
- Provas de conceito para registrar evidências e estados pendentes em fluxos técnicos.
- Avaliação conjunta de integrações e critérios de aceite, começando com dados autorizados ou sintéticos.

**Vamos conversar sobre o seu caso.** Se sua equipe tem uma necessidade de inspeção ou evidência com prazo definido, abra uma [issue pública no repositório](https://github.com/NixEngine/Hello_World/issues) para propor uma demonstração e conversar sobre escopo, orçamento e condições. Não inclua dados confidenciais na issue. Nossa preferência comercial é por projetos a partir de **US$ 100 mil**, com possibilidade de pagamento em **USDC ou BTC**, sujeitos a negociação. Isso não representa uma oferta aceita.

## Limites e estágio

Os ensaios descritos são protótipos e testes pontuais, não uma auditoria, certificação ou sistema validado para produção. Um hash permite comparar os bytes lidos com uma referência confiável; sozinho, não prova autoria, origem ou autenticidade. O arquivo pode mudar durante a leitura; a opção de amostra, se ativada, pode revelar conteúdo. O programa não inicia conexões de rede, mas um arquivo situado em unidade de rede pode ser acessado pela própria infraestrutura de montagem.

No teste Stellar, o diário local foi criado depois da observação. Um único Horizon e uma assinatura local não comprovam consenso, finalidade independente ou vínculo ao corpo do pedido original. Nenhum resultado acima demonstra receita, venda ou pagamento em produção.

---

# Your files, your inspection: Project Px

**Inspect files you select and produce a streaming SHA-256 digest without displaying their contents by default.** Zero Px Core is developing local inspection and technical-evidence tools for teams that need to understand what was examined and check whether bytes have changed.

## What we demonstrated

- A prototype reads a selected file in chunks and calculates SHA-256. A separate option displays a small byte sample when explicitly requested.
- On X9 Linux, the prototype passed **12 checks using synthetic files**, including comparison with an independent digest implementation.
- In a separate experiment, we verified the signature and integrity of a synthetic snapshot, rejected changes and explicitly preserved an uncertain state.
- In another read-only experiment, we queried a historical **Stellar testnet** transaction and linked the observation to a newly created local journal. **Eleven checks passed**, including controls with modified data. The observation came from one Horizon server over HTTPS; the signature was local.

### A small example

For a synthetic three-byte file containing `abc`, the prototype read three bytes and calculated:

`SHA-256: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`

The result matched an independent implementation. No content sample was requested for that run.

## How we can work together

- Local file inspection and comparison with customer-provided references.
- Proofs of concept for preserving evidence and unresolved states in technical workflows.
- Joint evaluation of integration requirements and acceptance criteria, starting with authorized or synthetic data.

**Let's discuss your use case.** If your team has a time-sensitive inspection or evidence need, open a [public repository issue](https://github.com/NixEngine/Hello_World/issues) to request a demonstration and discuss scope, budget and terms. Do not include confidential information in the issue. Our commercial preference is projects from **US$100,000**, potentially payable in **USDC or BTC**, subject to negotiation. This is not an accepted offer.

## Scope and limitations

The experiments above are prototypes and point-in-time tests, not an audit, certification or a production-validated system. A hash supports comparison of the bytes read with a trusted reference; it does not establish authorship, origin or authenticity by itself. A file may change while it is being read; enabling the sample option may reveal content. The program does not initiate network connections, although a network-mounted file may be accessed through the mount infrastructure.

For the Stellar experiment, the local journal was created after the observation. One Horizon server and a local signature do not independently establish consensus, finality, or a binding to the original request body. None of these results demonstrates revenue, a sale or a production payment.
