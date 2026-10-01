from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
CSS_VERSION = "20260930-prosbc-ecosystem-v1"

SOLUTIONS = [
    ("Origem Verificada / STIR-SHAKEN", "chamada-verificada.html", "Autenticação, identificação e jornada comercial"),
    ("SBC / ProSBC", "sbc-prosbc.html", "Borda SIP, interconexão e segurança"),
    ("Ecossistema ProSBC gerenciado", "prosbc-ecossistema-zictec.html", "Licenças, IaaS, operação, monitoramento e integrações"),
    ("Automação e STIR/SHAKEN", "prosbc-automacao-stir-shaken.html", "Scripts proprietários, provisionamento, identidade e políticas"),
    ("STFC Tools", "stfc-tools.html", "APIs, evidências, relatórios e rotinas"),
    ("Regulatório Anatel", "regulatorio-anatel.html", "Obrigações, DETRAF, QEML e evidências"),
    ("Suporte técnico", "suporte.html", "Banco de horas, RCA e sustentação"),
]


def talk_url(context: str) -> str:
    text = f"Olá, vim pelo site da ZICTEC e quero falar com um especialista sobre {context}."
    return "https://wa.me/554732300435?text=" + quote(text)


def header(context: str) -> str:
    items = "".join(f'<a href="{href}">{label}<small>{summary}</small></a>' for label, href, summary in SOLUTIONS)
    return f'''<header class="topbar"><nav class="nav wrap">
<a class="brand" href="index.html" aria-label="ZICTEC"><img src="assets/zictec-logo.png" alt="ZICTEC"></a>
<div class="menu"><a href="index.html">Home</a><a href="quem-somos.html">Quem somos</a><div class="drop"><a class="active" href="solucoes.html">Soluções ▾</a><div class="drop-panel">{items}</div></div><a href="segmentos.html">Segmentos</a><a href="blog.html">Blog</a><a href="contato.html">Contato</a></div>
<details class="mobile-nav"><summary aria-label="Abrir ou fechar menu"><span class="menu-open-label">☰ Menu</span><span class="menu-close-label">× Fechar</span></summary><div class="mobile-nav-panel"><a href="index.html">Home</a><a href="quem-somos.html">Quem somos</a><a href="solucoes.html">Todas as soluções</a><a href="sbc-prosbc.html">SBC / ProSBC</a><a href="prosbc-ecossistema-zictec.html">Ecossistema ProSBC gerenciado</a><a href="prosbc-automacao-stir-shaken.html">Automação e STIR/SHAKEN</a><a href="chamada-verificada.html">Origem Verificada</a><a href="blog.html">Blog</a><a href="contato.html">Contato</a></div></details>
<a class="btn ghost" href="{talk_url(context)}" target="_blank" rel="noopener">Falar com especialista</a>
</nav></header>'''


def footer() -> str:
    return '''<footer class="footer"><div class="wrap"><div><b>ZICTEC</b><br>Consultoria técnica e regulatória para operações de voz, STFC, SIP/SBC e Origem Verificada.</div><div>suporte@zictec.com.br • +55 47 3230-0435</div></div></footer>'''


def layout(title: str, description: str, context: str, body: str) -> str:
    return f'''<!doctype html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={CSS_VERSION}">
</head><body><div class="draft-ribbon"><div class="wrap">PRÉ-VISUALIZAÇÃO PARA VALIDAÇÃO • conteúdo ainda não publicado no site principal</div></div>{header(context)}<main>{body}</main>{footer()}</body></html>'''


def cta(title: str, text: str) -> str:
    return f'''<section><div class="wrap"><div class="cta"><div><h2>{title}</h2><p>{text}</p></div><div class="cta-actions"><a class="btn cta-primary" href="https://www.calendly.com/zictec/reuniao" target="_blank" rel="noopener">Agendar diagnóstico</a><a class="btn secondary" href="{talk_url(title)}" target="_blank" rel="noopener">Falar com especialista</a><a class="cta-tertiary" href="https://shop.zictec.com.br/" target="_blank" rel="noopener">Visitar Loja ZICTEC →</a></div></div></div></section>'''


sbc_body = '''
<section class="hero slim"><div class="hero-grid wrap"><div><span class="eyebrow">ProSBC com serviços ZICTEC</span><h1>Da licença à operação: uma borda SIP preparada para crescer com controle.</h1><p class="lead">A ZICTEC estrutura ambientes ProSBC com dimensionamento, arquitetura, implantação, migração, suporte especializado, hospedagem e integrações para operações de voz críticas.</p><div class="hero-actions"><a class="btn primary" href="prosbc-ecossistema-zictec.html">Conhecer o ecossistema</a><a class="btn secondary" href="prosbc-automacao-stir-shaken.html">Ver automação e STIR/SHAKEN</a></div></div></div></section>
<section><div class="wrap"><div class="section-title"><h2>ProSBC como plataforma, não como componente isolado.</h2><p>Licença, infraestrutura, rotas, mídia, observabilidade e operação precisam ser desenhadas em conjunto.</p></div><div class="cards"><article class="card"><div class="icon">01</div><h3>Licenciamento e arquitetura</h3><p>Levantamento de sessões, CPS, codecs, transcodificação, alta disponibilidade, interfaces e perfil de tráfego para definir a composição adequada.</p></article><article class="card"><div class="icon">02</div><h3>Implantação e migração</h3><p>Topologia, configuração, testes, homologação, cutover assistido, validação de SIP/SDP/RTP e estratégia de rollback.</p></article><article class="card"><div class="icon">03</div><h3>Suporte e operação</h3><p>Diagnóstico por traces e logs, ajustes controlados, acompanhamento técnico, monitoramento e evolução conforme o nível contratado.</p></article></div></div></section>
<section class="soft"><div class="wrap"><div class="section-title"><h2>Duas camadas complementares</h2><p>O ambiente base pode ser expandido com operação gerenciada e componentes próprios da ZICTEC.</p></div><div class="page-list"><a class="page-card featured" href="prosbc-ecossistema-zictec.html"><b>Ecossistema ProSBC gerenciado</b><span>Licenças, IaaS, sustentação, monitoramento, softswitch, CDR, billing e DETRAF.</span></a><a class="page-card" href="prosbc-automacao-stir-shaken.html"><b>Automação, políticas e identidade</b><span>Scripts proprietários, provisionamento controlado, STIR/SHAKEN, reputação e validação de origem.</span></a></div></div></section>
<section class="dark"><div class="wrap"><div class="section-title"><h2>O que analisamos antes de implantar</h2><p>A disponibilidade final depende da arquitetura completa, não apenas do SBC.</p></div><div class="journey"><div class="step"><h3>Tráfego</h3><p>Sessões, CPS, picos, codecs e mídia.</p></div><div class="step"><h3>Interconexões</h3><p>Operadoras, clientes, SIP/SIP-I e rotas.</p></div><div class="step"><h3>Infraestrutura</h3><p>On-premises, virtualização, nuvem e HA.</p></div><div class="step"><h3>Integrações</h3><p>Softswitch, CDR, billing, APIs e dados.</p></div><div class="step"><h3>Operação</h3><p>Monitoramento, suporte, mudanças e rollback.</p></div></div></div></section>
<section><div class="wrap"><div class="notice"><b>Escopo e marcas:</b> capacidades, recursos e integrações dependem da versão, licenciamento, arquitetura, interoperabilidade e proposta vigente. ProSBC e TelcoBridges são marcas de seus respectivos titulares. Componentes próprios da ZICTEC não devem ser interpretados como módulos nativos ou mantidos pelo fabricante, salvo declaração expressa.</div></div></section>
'''
sbc_page = layout("ProSBC com implantação e suporte ZICTEC", "Licenciamento, arquitetura, implantação, IaaS, suporte e integrações para ambientes ProSBC.", "ProSBC", sbc_body + cta("Quer avaliar seu ambiente ProSBC?", "Começamos pelo tráfego, topologia, interconexões, riscos e objetivos de operação."))


ecosystem_body = '''
<section class="hero slim prosbc-hero"><div class="hero-grid wrap"><div><span class="eyebrow">Ecossistema ProSBC gerenciado</span><h1>Licença, infraestrutura e operação em uma jornada única.</h1><p class="lead">A ZICTEC reúne serviços profissionais, infraestrutura hospedada e integração operacional para que o ProSBC seja implantado com escopo, evidências e responsabilidades claras.</p><div class="hero-actions"><a class="btn primary" href="#camadas">Ver as camadas</a><a class="btn secondary" href="prosbc-automacao-stir-shaken.html">Automação proprietária</a></div></div></div></section>
<section id="camadas"><div class="wrap"><div class="section-title"><h2>Do projeto à sustentação</h2><p>Camadas combináveis conforme o estágio, a arquitetura e as responsabilidades de cada operação.</p></div><div class="cards"><article class="card"><div class="icon">01</div><h3>Licenciamento e expansão</h3><p>Fornecimento e apoio no dimensionamento de licenças, recursos e evolução de capacidade conforme a edição, versão e proposta comercial vigentes.</p></article><article class="card"><div class="icon">02</div><h3>Arquitetura e implantação</h3><p>Desenho de topologia, instalação, configuração, políticas SIP, interoperabilidade, homologação e documentação de aceite.</p></article><article class="card"><div class="icon">03</div><h3>Migração assistida</h3><p>Plano de testes, janela de mudança, virada assistida e rollback. Migração sem impacto não é presumida.</p></article><article class="card"><div class="icon">04</div><h3>ProSBC hospedado / IaaS</h3><p>Infraestrutura para execução do ProSBC com opções de implantação, monitoramento e gestão ZICTEC conforme contrato e responsabilidades definidas.</p></article><article class="card"><div class="icon">05</div><h3>Suporte especializado</h3><p>Banco de horas, sustentação ou operação gerenciada, com cobertura, SLA, canais e responsabilidades definidos na contratação.</p></article><article class="card"><div class="icon">06</div><h3>Observabilidade</h3><p>Sessões, causas SIP, CDRs, traces, alarmes e indicadores disponíveis conforme licenciamento, configuração, ancoragem e pontos de coleta.</p></article></div></div></section>
<section class="soft"><div class="wrap split"><div><span class="eyebrow">IaaS e operação</span><h2>Hospedagem não precisa significar perda de controle.</h2><p>A oferta pode separar claramente infraestrutura, licença, configuração, conectividade, backup, atualização, segurança e gestão operacional. Assim, a operadora sabe o que está incluído e quem responde por cada camada.</p><div class="tags"><span class="tag">Ambiente dedicado</span><span class="tag">Alta disponibilidade</span><span class="tag">Backup e rollback</span><span class="tag">Monitoramento</span><span class="tag">Gestão de mudanças</span></div></div><div class="panel"><h3>Responsabilidades definidas em proposta</h3><ul class="list"><li>Infraestrutura e capacidade contratada.</li><li>Licenciamento e recursos habilitados.</li><li>Conectividade, rotas e interconexões.</li><li>Atualizações, manutenção e contingência.</li><li>SLA, suporte e escalonamento.</li></ul></div></div></section>
<section><div class="wrap"><div class="section-title"><h2>Integrações ao redor da borda SIP</h2><p>O ProSBC participa do fluxo operacional, mas não substitui sozinho as plataformas de negócio.</p></div><p class="diagram-label"><b>Mapa conceitual:</b> estas integrações podem operar em paralelo e trocar sinalização, eventos ou dados conforme cada arquitetura.</p><div class="ecosystem-flow"><div class="ecosystem-node"><b>Softswitch</b><span>assinantes, serviços e roteamento central</span></div><div class="ecosystem-node core"><b>ProSBC</b><span>borda, políticas SIP, segurança e interconexão</span></div><div class="ecosystem-node"><b>CDR e billing</b><span>exportação, enriquecimento, tarifação e conciliação</span></div><div class="ecosystem-node"><b>DETRAF</b><span>dados, regras, conferência e backoffice</span></div><div class="ecosystem-node"><b>APIs e automação</b><span>políticas, validações, auditoria e evidências</span></div></div><div class="notice"><b>Importante:</b> a geração ou exportação de eventos pelo SBC não substitui um sistema completo de billing ou DETRAF. Tarifação, conciliação e apuração dependem de regras de negócio, qualidade dos CDRs e integrações de backoffice.</div></div></section>
<section class="dark"><div class="wrap"><div class="section-title"><h2>Uma implantação orientada por evidências</h2><p>Cada etapa produz critérios de aceite e condições claras para avanço.</p></div><div class="journey"><div class="step"><h3>Diagnóstico</h3><p>Inventário, tráfego, riscos e dependências.</p></div><div class="step"><h3>Desenho</h3><p>Topologia, capacidade e responsabilidades.</p></div><div class="step"><h3>Laboratório</h3><p>Configuração, integração e testes negativos.</p></div><div class="step"><h3>Cutover</h3><p>Janela, validação e rollback preparado.</p></div><div class="step"><h3>Operação</h3><p>Monitoramento, suporte e melhoria contínua.</p></div></div></div></section>
'''
ecosystem_page = layout("Ecossistema ProSBC gerenciado — ZICTEC", "Licenciamento, implantação, IaaS, suporte, monitoramento e integrações para ProSBC.", "ecossistema ProSBC gerenciado", ecosystem_body + cta("Quer desenhar a composição correta?", "A ZICTEC pode separar licença, infraestrutura, serviços profissionais e operação recorrente em um escopo verificável."))


automation_body = '''
<section class="hero slim prosbc-hero"><div class="hero-grid wrap"><div><span class="eyebrow">Automação ZICTEC integrada ao ProSBC</span><h1>Políticas de voz evoluídas com componentes proprietários e provisionamento controlado.</h1><p class="lead">A ZICTEC desenvolve lógicas e scripts próprios para complementar ambientes ProSBC por mecanismos suportados no projeto, com controle de versão, implantação, evidência e rollback.</p><div class="hero-actions"><a class="btn primary" href="#capacidades">Conhecer capacidades</a><a class="btn secondary" href="chamada-verificada.html">Entender a jornada de autenticação</a></div></div></div></section>
<section><div class="wrap"><div class="notice"><b>Limite técnico:</b> os componentes proprietários são fornecidos e mantidos como parte da solução integrada ZICTEC. Eles não são apresentados como módulos nativos, certificados ou mantidos pela TelcoBridges, salvo declaração expressa.</div><div style="height:28px"></div><div class="cards"><article class="card"><div class="icon">V</div><h3>Versionamento</h3><p>Identificação de releases, integridade do componente e histórico do que foi aprovado para cada ambiente.</p></article><article class="card"><div class="icon">P</div><h3>Provisionamento</h3><p>Distribuição controlada por ambiente, com critérios de ativação, evidência de carga e separação entre desenvolvimento e produção.</p></article><article class="card"><div class="icon">R</div><h3>Rollback</h3><p>Retorno à versão anterior e comportamento de contingência definidos antes de cada mudança.</p></article></div></div></section>
<section id="capacidades" class="soft"><div class="wrap"><div class="section-title"><h2>Capacidades que podem compor a solução</h2><p>Cada recurso depende de arquitetura, fonte de dados, licenciamento, homologação e política operacional.</p></div><div class="cards"><article class="card"><h3>Roteamento e normalização SIP</h3><p>Políticas de rota, manipulação controlada de sinalização, interoperabilidade, failover e consulta a fontes externas.</p></article><article class="card"><h3>STIR/SHAKEN e SIP Identity</h3><p>Integração com funções autorizadas de assinatura ou validação, respeitando limites de confiança, campos protegidos e o ponto correto de assinatura por requisição.</p></article><article class="card"><h3>Blacklist e anti-spam</h3><p>Consulta a listas internas ou externas e aplicação de políticas de permitir, bloquear, desviar ou analisar, sujeita à qualidade dos dados e a falsos positivos ou negativos.</p></article><article class="card"><h3>Reputação de números</h3><p>Uso de sinais de reputação e histórico operacional como insumo de política, sem prometer legitimidade absoluta ou ausência de fraude.</p></article><article class="card"><h3>Validação de origem</h3><p>Controles inspirados em conceitos de Do Not Originate, adaptados às regras e fontes disponíveis no Brasil, sem alegar equivalência ou homologação regulatória.</p></article><article class="card"><h3>Auditoria e estatísticas</h3><p>Registros de decisão, sucesso, falha, volume e causas para troubleshooting, relatórios e evolução das políticas.</p></article></div></div></section>
<section><div class="wrap split"><div><span class="eyebrow">STIR/SHAKEN com precisão</span><h2>Autenticar não é o mesmo que identificar a marca.</h2><p>STIR/SHAKEN permite assinar e verificar informações de identidade telefônica transportadas na sinalização SIP. A validação confirma a integridade da assinatura e a atestação declarada no fluxo aplicável.</p><p>Isso não comprova isoladamente a identidade pessoal do chamador, a legitimidade do conteúdo ou a ausência de fraude. Nome, marca, motivo e logotipo pertencem à jornada de Origem Verificada e dependem de regras, cadastro, governança, rotas participantes e terminais compatíveis.</p></div><div class="panel"><h3>Modelos de integração</h3><ul class="list"><li>Componente protegido no ambiente ProSBC.</li><li>API ZICTEC e orquestração com serviços autorizados.</li><li>Integração SIP e políticas condicionadas ao comportamento da origem.</li><li>Arquitetura híbrida, conforme volume e governança.</li></ul><a class="btn ghost" href="chamada-verificada.html">Ver página de Origem Verificada</a></div></div></section>
<section class="dark"><div class="wrap"><div class="section-title"><h2>Ciclo de mudança seguro</h2><p>Automação em borda de voz exige mais do que copiar um script.</p></div><div class="journey"><div class="step"><h3>Especificar</h3><p>Regra, dados, exceções e falhas esperadas.</p></div><div class="step"><h3>Testar</h3><p>Casos positivos, negativos e contingência.</p></div><div class="step"><h3>Homologar</h3><p>Aceite funcional e de interoperabilidade.</p></div><div class="step"><h3>Provisionar</h3><p>Versão aprovada no ambiente correto.</p></div><div class="step"><h3>Observar</h3><p>Logs, métricas, alertas e rollback.</p></div></div></div></section>
'''
automation_page = layout("Automação e STIR/SHAKEN no ProSBC — ZICTEC", "Scripts proprietários, provisionamento controlado, STIR/SHAKEN, reputação e políticas integradas ao ProSBC.", "automação e STIR/SHAKEN no ProSBC", automation_body + cta("Quer validar uma política no seu ProSBC?", "Podemos começar por uma PoC com critérios de aceite, dados necessários e rollback definido."))


solutions_cards = "".join(f'<a class="page-card" href="{href}"><b>{label}</b><span>{summary}</span></a>' for label, href, summary in SOLUTIONS)
solutions_body = f'''
<section class="hero slim"><div class="hero-grid wrap"><div><span class="eyebrow">Hub de soluções</span><h1>Engenharia, automação e operação para redes de voz.</h1><p class="lead">Da borda ProSBC à autenticação de chamadas, a ZICTEC integra infraestrutura, software, suporte e processos regulatórios para operadoras.</p><div class="hero-actions"><a class="btn primary" href="prosbc-ecossistema-zictec.html">Explorar ecossistema ProSBC</a><a class="btn secondary" href="contato.html">Solicitar diagnóstico</a></div></div></div></section>
<section><div class="wrap"><div class="page-list">{solutions_cards}</div></div></section>
<section class="soft"><div class="wrap"><div class="section-title"><h2>Como escolher o caminho certo</h2><p>Nem toda necessidade começa por produto. Muitas começam por diagnóstico, capacidade e responsabilidades.</p></div><table class="table"><thead><tr><th>Situação</th><th>Caminho recomendado</th></tr></thead><tbody><tr><td>Licença, implantação, migração, IaaS ou operação recorrente</td><td>Ecossistema ProSBC gerenciado</td></tr><tr><td>Políticas próprias, reputação, blacklist ou provisionamento</td><td>Automação e STIR/SHAKEN no ProSBC</td></tr><tr><td>Problemas de rotas, SIP, mídia ou interconexão</td><td>SBC / ProSBC + suporte técnico</td></tr><tr><td>Autenticação e preparação para Origem Verificada</td><td>Origem Verificada / STIR-SHAKEN</td></tr><tr><td>Relatórios, CDR, DETRAF, evidências ou obrigações</td><td>STFC Tools + Regulatório Anatel</td></tr></tbody></table></div></section>
'''
solutions_page = layout("Soluções de voz e ProSBC — ZICTEC", "Soluções ZICTEC para ProSBC, STIR/SHAKEN, STFC, automação, suporte e regulatório.", "soluções de voz e ProSBC", solutions_body + cta("Vamos definir o primeiro passo?", "A conversa pode começar por arquitetura ProSBC, automação, autenticação, suporte ou uma obrigação operacional específica."))


chamada_body = '''
<section class="hero slim"><div class="hero-grid wrap"><div><span class="eyebrow">Origem Verificada / STIR-SHAKEN</span><h1>Autenticação de chamadas como base para confiança e identificação.</h1><p class="lead">A ZICTEC apoia operadoras na integração de STIR/SHAKEN e na preparação para Origem Verificada, separando protocolo, operação de autenticação e apresentação de marca.</p><div class="hero-actions"><a class="btn primary" href="https://www.chamadaverificada.com.br/" target="_blank" rel="noopener">Ver landing dedicada</a><a class="btn secondary" href="prosbc-automacao-stir-shaken.html">Integração com ProSBC</a></div></div></div></section>
<section><div class="wrap"><div class="notice"><b>Distinção essencial:</b> STIR/SHAKEN assina e verifica informações de identidade telefônica na sinalização SIP. Origem Verificada é a camada de identificação apresentada ao usuário. A autenticação não garante, por si só, exibição de nome, marca, motivo ou logotipo.</div><div style="height:28px"></div><div class="cards"><article class="card"><h3>Diagnóstico técnico</h3><p>Rotas, SBC/softswitch, interconexões, governança aplicável e dependências para assinatura ou validação.</p></article><article class="card"><h3>Arquitetura e implantação</h3><p>Integração por componente ProSBC, API, SIP ou composição híbrida, conforme volume, responsabilidade e homologação.</p></article><article class="card"><h3>Operação e evidências</h3><p>Testes, registros, troubleshooting, métricas de sucesso e falha, auditoria e evolução controlada.</p></article></div></div></section>
<section class="soft"><div class="wrap split"><div><h2>Autenticação técnica</h2><p>A validação confirma integridade da assinatura e atestação declarada no fluxo aplicável. Não comprova isoladamente identidade pessoal, legitimidade do conteúdo ou ausência de fraude.</p><div class="tags"><span class="tag">SIP Identity</span><span class="tag">PASSporT</span><span class="tag">Assinatura</span><span class="tag">Validação</span><span class="tag">Evidências</span></div></div><div class="panel"><h3>Identificação e marca</h3><p>Nome, marca, campanha, motivo e logotipo dependem de cadastro, validação, regras vigentes, rotas participantes, governança e terminais compatíveis.</p><a class="btn ghost" href="prosbc-automacao-stir-shaken.html">Ver automação integrada</a></div></div></section>
'''
chamada_page = layout("Origem Verificada e STIR/SHAKEN — ZICTEC", "Autenticação de chamadas, SIP Identity e preparação para Origem Verificada.", "Origem Verificada e STIR/SHAKEN", chamada_body + cta("Vamos mapear seu cenário de autenticação?", "A escolha depende de arquitetura, rotas, SBC, governança, volume e objetivo comercial."))


extra_css = r'''

/* ProSBC ecosystem preview — 2026-09-30 */
.draft-ribbon{background:#ffe1c6;border-bottom-color:#ffbb7d;color:#713500}
.prosbc-hero{background:radial-gradient(circle at 88% 18%,rgba(255,122,26,.28),transparent 30%),linear-gradient(135deg,#071831 0%,#0c2450 100%)}
.prosbc-hero .hero-grid{grid-template-columns:minmax(0,950px)}
.hero .btn.primary{color:#071831}
.mobile-nav{display:none;position:relative}.mobile-nav summary{position:relative;z-index:92;cursor:pointer;list-style:none;padding:10px 14px;border:1px solid var(--line);border-radius:12px;background:#fff;color:var(--navy);font-weight:800}.mobile-nav summary::-webkit-details-marker{display:none}.menu-close-label{display:none}.mobile-nav[open] .menu-open-label{display:none}.mobile-nav[open] .menu-close-label{display:inline}.mobile-nav[open]::before{content:"";position:fixed;inset:0;z-index:80;background:rgba(7,24,49,.36)}.mobile-nav-panel{position:absolute;right:0;top:48px;z-index:91;width:min(330px,calc(100vw - 32px));padding:12px 12px 16px;border:1px solid var(--line);border-radius:18px;background:#fff;box-shadow:0 20px 55px rgba(7,24,49,.25)}.mobile-nav-panel a{display:block;padding:11px 12px;border-radius:10px;color:var(--navy);font-weight:700}.mobile-nav-panel a:hover{background:#f4f7fb}.mobile-nav-panel a:nth-child(n+4):nth-child(-n+7){padding-left:24px;color:var(--muted);font-size:14px}
.soft .eyebrow,.split .eyebrow{color:#a84400;background:#ffe8d4;border-color:#ffc896}
.cta-actions .cta-primary{background:var(--navy);border:1px solid var(--navy);color:#fff}.cta-actions .cta-primary:hover{background:var(--navy2)}
.cta-tertiary{color:#fff;font-weight:800;text-decoration:underline;text-underline-offset:4px;white-space:nowrap}
.page-card.featured{outline:2px solid rgba(255,122,26,.42);background:linear-gradient(135deg,#fff8ed,#fff)}
.ecosystem-flow{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:stretch;margin:28px 0}
.ecosystem-node{position:relative;display:flex;flex-direction:column;gap:8px;min-height:150px;padding:22px;border:1px solid var(--line);border-radius:22px;background:#fff;box-shadow:0 14px 38px rgba(7,24,49,.08)}
.ecosystem-node b{font-size:18px;color:var(--navy)}.ecosystem-node span{color:var(--muted);font-size:14px}.ecosystem-node.core{background:linear-gradient(145deg,var(--navy),var(--navy2));border-color:transparent}.ecosystem-node.core b{color:#fff}.ecosystem-node.core span{color:#d7e4f7}
.diagram-label{margin:0 0 18px;padding:14px 18px;border-left:4px solid var(--orange);background:#f7f9fc;color:var(--muted);border-radius:0 14px 14px 0}
@media (max-width:980px){.ecosystem-flow{grid-template-columns:1fr 1fr}}
@media (max-width:980px){.mobile-nav{display:block}}
@media (max-width:620px){.ecosystem-flow{grid-template-columns:1fr}.prosbc-hero .hero-actions .btn{width:100%;white-space:normal;text-align:center}.nav>.btn.ghost{display:none}.mobile-nav{margin-left:auto}.prosbc-hero h1{font-size:clamp(38px,11vw,54px)}}
'''

outputs = {
    "sbc-prosbc.html": sbc_page,
    "prosbc-ecossistema-zictec.html": ecosystem_page,
    "prosbc-automacao-stir-shaken.html": automation_page,
    "solucoes.html": solutions_page,
    "chamada-verificada.html": chamada_page,
}
for name, content in outputs.items():
    (ROOT / name).write_text(content, encoding="utf-8")

css_path = ROOT / "styles.css"
css = css_path.read_text(encoding="utf-8")
marker = "/* ProSBC ecosystem preview — 2026-09-30 */"
if marker in css:
    css = css.split(marker)[0].rstrip() + "\n"
css_path.write_text(css + extra_css, encoding="utf-8")
print(f"wrote {len(outputs)} pages and updated styles.css")
