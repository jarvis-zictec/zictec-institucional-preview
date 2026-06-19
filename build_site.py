from pathlib import Path
from textwrap import dedent
import re

ROOT = Path(__file__).parent

CSS = r'''
:root{
  --navy:#071831; --navy2:#0c2450; --blue:#154b9b; --purple:#5e2fb4; --orange:#ff7a1a; --orange2:#ff9f43;
  --ink:#0b1830; --muted:#52627a; --line:#dbe4f0; --soft:#f5f8fc; --card:#ffffff; --peach:#fff1e6; --cyan:#eaf6ff;
  --green:#17a36b; --red:#cc3a31; --shadow:0 24px 70px rgba(7,24,49,.16); --radius:26px; --max:1180px;
}
*{box-sizing:border-box} html{scroll-behavior:smooth} body{margin:0;font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif;background:#fff;color:var(--ink);line-height:1.58} a{color:inherit}.wrap{width:min(var(--max),calc(100% - 40px));margin:auto}.draft-ribbon{background:#fff8ed;border-bottom:1px solid #ffd7a8;color:#8f4300;font-weight:800;font-size:13px}.draft-ribbon .wrap{padding:9px 0;text-align:center}.topbar{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.9);backdrop-filter:blur(18px);border-bottom:1px solid rgba(219,228,240,.9)}.nav{height:76px;display:flex;align-items:center;justify-content:space-between;gap:24px}.brand{display:flex;align-items:center;gap:14px;text-decoration:none}.brand img{height:42px;max-width:150px;object-fit:contain}.brand-text{font-weight:900;letter-spacing:.08em;color:var(--navy)}.menu{display:flex;gap:4px;align-items:center;font-weight:800;font-size:14px;color:#263a5d}.menu>a,.drop>a{padding:11px 12px;border-radius:999px;text-decoration:none;display:inline-flex;gap:7px;align-items:center}.menu a:hover,.menu a.active{color:var(--orange);background:#fff3e8}.drop{position:relative}.drop-panel{position:absolute;top:44px;left:0;width:330px;background:#fff;border:1px solid var(--line);border-radius:20px;box-shadow:0 22px 60px rgba(7,24,49,.18);padding:10px;display:none}.drop:hover .drop-panel{display:grid}.drop-panel a{padding:12px 13px;text-decoration:none;border-radius:14px;color:#263a5d;display:block}.drop-panel a:hover{background:var(--soft);color:var(--orange)}.drop-panel small{display:block;color:var(--muted);font-weight:600;margin-top:2px}.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:13px 18px;border-radius:999px;border:1px solid transparent;text-decoration:none;font-weight:900;white-space:nowrap}.btn.primary{background:linear-gradient(135deg,var(--orange),#ff5c21);color:#fff;box-shadow:0 18px 34px rgba(255,122,26,.28)}.btn.secondary{background:#fff;color:var(--navy);border-color:rgba(255,255,255,.28)}.btn.ghost{border-color:var(--line);background:#fff;color:var(--navy)}.hero{position:relative;overflow:hidden;background:radial-gradient(circle at 88% 6%,rgba(255,122,26,.34),transparent 22%),radial-gradient(circle at 55% 18%,rgba(94,47,180,.42),transparent 35%),linear-gradient(135deg,#061429 0%,#102b62 52%,#171034 100%);color:#fff}.hero:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(to bottom,#000,transparent 76%)}.hero-grid{position:relative;display:grid;grid-template-columns:1.05fr .95fr;gap:52px;align-items:center;padding:78px 0 58px}.hero.slim .hero-grid{grid-template-columns:1fr;padding:62px 0 46px}.eyebrow{display:inline-flex;gap:9px;align-items:center;padding:8px 12px;border-radius:999px;background:rgba(255,255,255,.11);border:1px solid rgba(255,255,255,.14);font-size:13px;font-weight:900;color:#ffe8d4}.hero h1{font-size:clamp(38px,6vw,74px);line-height:.98;margin:22px 0 18px;letter-spacing:-.055em}.hero.slim h1{max-width:950px}.lead{font-size:clamp(18px,2.2vw,23px);color:#dbe8ff;max-width:790px;margin:0 0 30px}.hero-actions{display:flex;gap:14px;flex-wrap:wrap}.hero-proof{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:34px}.proof{padding:16px;border-radius:18px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.12)}.proof b{display:block;color:#fff;font-size:15px}.proof span{display:block;color:#bdd1ee;font-size:12px;margin-top:5px}.hero-card{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.16);box-shadow:var(--shadow);border-radius:34px;padding:26px;backdrop-filter:blur(10px)}.network{height:430px;border-radius:25px;background:linear-gradient(145deg,rgba(255,255,255,.13),rgba(255,255,255,.05));position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.14)}.node{position:absolute;border-radius:18px;background:#fff;color:var(--navy);padding:13px 15px;box-shadow:0 16px 40px rgba(0,0,0,.22);font-weight:900}.node small{display:block;font-weight:700;color:#697893;margin-top:2px}.n1{left:28px;top:34px}.n2{right:28px;top:72px}.n3{left:66px;bottom:82px}.n4{right:42px;bottom:44px;background:var(--peach)}.pulse{position:absolute;left:50%;top:50%;width:160px;height:160px;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,var(--orange) 0 20%,rgba(255,122,26,.2) 21% 46%,rgba(255,255,255,.08) 47%);box-shadow:0 0 0 22px rgba(255,122,26,.08)}.line{position:absolute;height:2px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.55),transparent);transform-origin:center}.l1{left:92px;right:88px;top:122px;transform:rotate(10deg)}.l2{left:126px;right:96px;top:255px;transform:rotate(-18deg)}.l3{left:126px;right:110px;top:314px;transform:rotate(14deg)}section{padding:78px 0}.soft{background:var(--soft)}.dark{background:linear-gradient(135deg,var(--navy),#102b62);color:#fff}.section-title{display:flex;align-items:end;justify-content:space-between;gap:28px;margin-bottom:34px}.section-title h2{font-size:clamp(30px,4.4vw,50px);line-height:1.04;margin:0;letter-spacing:-.04em;color:var(--navy)}.section-title p{max-width:560px;color:var(--muted);margin:0;font-size:17px}.dark .section-title h2,.dark h2,.dark h3{color:#fff}.dark .section-title p,.dark p{color:#c7d6ed}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:24px;box-shadow:0 18px 48px rgba(18,39,76,.07)}.dark .card{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.12);box-shadow:none}.card h3{margin:0 0 9px;font-size:20px;color:var(--navy)}.card p{margin:0;color:var(--muted)}.card ul{margin:14px 0 0;padding-left:18px;color:#334761}.dark .card ul{color:#c7d6ed}.icon{width:46px;height:46px;border-radius:16px;display:grid;place-items:center;background:linear-gradient(135deg,var(--peach),#fff);color:var(--orange);font-size:23px;margin-bottom:18px}.split{display:grid;grid-template-columns:.92fr 1.08fr;gap:34px;align-items:start}.panel{background:#fff;border:1px solid var(--line);border-radius:30px;padding:28px;box-shadow:0 18px 48px rgba(18,39,76,.07)}.list{display:grid;gap:13px;margin:0;padding:0;list-style:none}.list li{display:grid;grid-template-columns:28px 1fr;gap:10px;color:#334761}.list li:before{content:"✓";width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:#eaf9f3;color:var(--green);font-weight:900}.journey{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;counter-reset:step}.step{position:relative;padding:22px;border-radius:22px;background:#fff;border:1px solid var(--line)}.step:before{counter-increment:step;content:"0" counter(step);display:inline-flex;background:var(--navy);color:#fff;border-radius:999px;padding:5px 10px;font-size:12px;font-weight:900;margin-bottom:16px}.step h3{margin:0 0 8px;font-size:17px;color:var(--navy)}.step p{color:#334761}.dark .step h3{color:var(--navy)}.dark .step p{color:#334761}.page-list{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}.page-card{display:block;position:relative;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:22px;padding:20px 52px 20px 20px;box-shadow:0 14px 38px rgba(18,39,76,.06);transition:.18s ease}.page-card:after{content:"→";position:absolute;right:22px;top:22px;color:var(--orange);font-weight:900}.page-card:hover{transform:translateY(-2px);border-color:#ffc48b}.page-card b{display:block;color:var(--navy);font-size:18px}.page-card span{display:block;color:var(--muted);font-size:14px;margin-top:5px}.feature{display:grid;grid-template-columns:180px 1fr;gap:22px;padding:24px;border-radius:26px;border:1px solid var(--line);background:#fff;margin-bottom:16px}.feature b{color:var(--navy)}.tag{display:inline-flex;border:1px solid var(--line);border-radius:999px;padding:7px 10px;font-weight:800;font-size:12px;color:#29405f;background:#fff}.tags{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}.cta{display:grid;grid-template-columns:1.2fr auto;gap:28px;align-items:center;background:linear-gradient(135deg,var(--orange),#ff6a21);border-radius:34px;color:#fff;padding:38px;box-shadow:0 22px 70px rgba(255,122,26,.25)}.cta h2{font-size:clamp(28px,4vw,46px);line-height:1.04;margin:0 0 10px}.cta p{margin:0;color:#fff1e6;max-width:720px}.cta-actions{display:flex;flex-direction:column;gap:12px;min-width:330px}.footer{background:#061429;color:#c7d6ed;padding:34px 0}.footer .wrap{display:flex;justify-content:space-between;gap:22px}.breadcrumb{font-size:13px;font-weight:800;color:#d7e5ff;margin-bottom:16px}.breadcrumb a{text-decoration:none;color:#fff}.table{width:100%;border-collapse:collapse;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 14px 38px rgba(18,39,76,.07)}.table th,.table td{padding:16px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.table th{background:#edf4ff;color:var(--navy);font-size:13px;text-transform:uppercase;letter-spacing:.04em}.notice{border-left:5px solid var(--orange);background:#fff7ef;border-radius:18px;padding:18px;color:#5a2d00}.mobile-menu{display:none}
.article-body{max-width:880px;margin:auto}.article-body h2{font-size:32px;margin:42px 0 12px;color:var(--navy)}.article-body h3{font-size:22px;margin:28px 0 8px;color:var(--navy2)}.article-body p{font-size:18px;color:#273a56}.article-body li{margin:8px 0;font-size:17px}.article-meta{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0}.article-meta span{background:#eef4fb;border:1px solid var(--line);border-radius:999px;padding:8px 12px;font-weight:800;color:#31435f;font-size:13px}.blog-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}.blog-card{display:block;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:24px;padding:24px;box-shadow:0 14px 45px rgba(7,24,49,.08)}.blog-card:hover{transform:translateY(-2px);box-shadow:var(--shadow)}.blog-card .k{color:var(--orange);font-weight:900;font-size:13px;text-transform:uppercase;letter-spacing:.08em}.blog-card h3{font-size:26px;margin:10px 0;color:var(--navy)}.blog-card p{color:var(--muted)}.editorial-note{background:#fff8ed;border:1px solid #ffd7a8;border-radius:22px;padding:22px;color:#6d3900}.toc{background:#f6f9fd;border:1px solid var(--line);border-radius:24px;padding:22px}.toc a{display:block;color:var(--blue);font-weight:800;text-decoration:none;margin:8px 0}.article-figure{margin:28px 0 10px;border-radius:28px;overflow:hidden;border:1px solid rgba(219,228,240,.9);box-shadow:0 22px 60px rgba(7,24,49,.16);background:#071831}.article-figure img{display:block;width:100%;height:auto}.article-figure figcaption{background:#fff;padding:12px 18px;color:var(--muted);font-size:14px}.blog-card img{width:100%;border-radius:18px;margin-bottom:16px;border:1px solid var(--line);background:#071831}@media (max-width: 980px){.menu{display:none}.mobile-menu{display:inline-flex}.hero-grid,.split,.cta{grid-template-columns:1fr}.hero-card{order:-1}.cards{grid-template-columns:1fr 1fr}.journey{grid-template-columns:1fr 1fr}.page-list{grid-template-columns:1fr}.hero-proof{grid-template-columns:1fr}.cta-actions{min-width:0}.footer .wrap{flex-direction:column}.feature{grid-template-columns:1fr}}
@media (max-width: 620px){.blog-grid{grid-template-columns:1fr}.wrap{width:min(100% - 28px,var(--max))}.cards,.journey{grid-template-columns:1fr}.section-title{display:block}.hero-grid{padding:54px 0 42px}.network{height:330px}.node{font-size:12px;padding:10px}.section-title p{margin-top:14px}.cta{padding:28px}.draft-ribbon .wrap{font-size:12px}.table{display:block;overflow-x:auto}.hero h1{font-size:38px}}
'''

NAV = [
    ("Home", "index.html"),
    ("Quem somos", "quem-somos.html"),
    ("Soluções", "solucoes.html"),
    ("Segmentos", "segmentos.html"),
    ("Blog", "blog.html"),
    ("Contato", "contato.html"),
]
SOL = [
    ("Origem Verificada / STIR-SHAKEN", "chamada-verificada.html", "Autenticação, identificação e jornada comercial"),
    ("STFC Tools", "stfc-tools.html", "APIs, evidências, relatórios e rotinas"),
    ("SBC / ProSBC", "sbc-prosbc.html", "Borda SIP, interconexão e segurança"),
    ("Regulatório Anatel", "regulatorio-anatel.html", "Obrigações, DETRAF, QEML e evidências"),
    ("Suporte técnico", "suporte.html", "Banco de horas, RCA e sustentação"),
]

def header(active):
    nav = []
    for label, href in NAV:
        cls = ' class="active"' if active == href else ''
        if label == 'Soluções':
            items = ''.join(f'<a href="{h}">{l}<small>{s}</small></a>' for l,h,s in SOL)
            nav.append(f'<div class="drop"><a{cls} href="{href}">Soluções ▾</a><div class="drop-panel">{items}</div></div>')
        else:
            nav.append(f'<a{cls} href="{href}">{label}</a>')
    return f'''
  <header class="topbar"><nav class="nav wrap">
    <a class="brand" href="index.html" aria-label="ZICTEC"><img src="assets/zictec-logo.png" alt="ZICTEC"></a>
    <div class="menu">{''.join(nav)}</div>
    <a class="btn ghost" href="contato.html">Falar com especialista</a>
  </nav></header>'''

def layout(title, desc, active, body):
    return f'''<!doctype html><html lang="pt-BR"><head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title><meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css?v=20260619-public">
</head><body>{header(active)}<main>{body}</main>{footer()}</body></html>'''

def footer():
    return '''<footer class="footer"><div class="wrap"><div><b>ZICTEC</b><br>Consultoria técnica e regulatória para operações de voz, STFC, SIP/SBC e Origem Verificada.</div><div>suporte@zictec.com.br • +55 47 3230-0435</div></div></footer>'''

def hero(kicker, title, lead, actions='', slim=False):
    cls = 'hero slim' if slim else 'hero'
    side = '' if slim else '''<aside class="hero-card"><div class="network"><div class="pulse"></div><div class="line l1"></div><div class="line l2"></div><div class="line l3"></div><div class="node n1">Operadora<small>STFC • VoIP • SIP</small></div><div class="node n2">Borda SBC<small>ProSBC • Telcobridges</small></div><div class="node n3">Regulatório<small>Anatel • DETRAF • QEML</small></div><div class="node n4">Confiança<small>STIR/SHAKEN • Origem</small></div></div></aside>'''
    return f'''<section class="{cls}"><div class="hero-grid wrap"><div><span class="eyebrow">{kicker}</span><h1>{title}</h1><p class="lead">{lead}</p>{actions}</div>{side}</div></section>'''

def cta(title='Vamos avaliar sua operação de voz?', text='A próxima conversa pode começar por diagnóstico técnico, priorização regulatória ou uma frente específica como Origem Verificada, STFC Tools ou SBC.', primary='Agendar diagnóstico'):
    return f'''<section><div class="wrap"><div class="cta"><div><h2>{title}</h2><p>{text}</p></div><div class="cta-actions"><a class="btn secondary" href="https://www.calendly.com/zictec/reuniao" target="_blank" rel="noopener">{primary}</a><a class="btn secondary" href="https://wa.me/554732300435" target="_blank" rel="noopener">Falar com especialista</a><a class="btn secondary" href="https://shop.zictec.com.br/" target="_blank" rel="noopener">Loja ZICTEC</a></div></div></div></section>'''

PAGES = {}

PAGES['index.html'] = layout('ZICTEC — Consultoria técnica e regulatória para operadoras', 'Consultoria técnica e regulatória para operadoras, provedores e empresas que dependem de voz, STFC, SIP, SBC e Origem Verificada.', 'index.html', hero('ZICTEC Telecom','Consultoria técnica e regulatória para operações de voz mais seguras, estáveis e conformes.','Consultoria, implantação e suporte especializado para operadoras de telecom que precisam tratar voz, interconexão, STFC, SIP, SBC, STIR/SHAKEN, Origem Verificada e obrigações Anatel com previsibilidade.', '<div class="hero-actions"><a class="btn primary" href="solucoes.html">Conhecer soluções</a><a class="btn secondary" href="contato.html">Falar com especialista</a></div><div class="hero-proof"><div class="proof"><b>Voz e STFC</b><span>operação, interconexão, rotas e evidências</span></div><div class="proof"><b>Regulatório Anatel</b><span>obrigações, QEML, DETRAF e processos</span></div><div class="proof"><b>Autenticação</b><span>STIR/SHAKEN e Origem Verificada sem promessas indevidas</span></div></div>') + dedent('''
<section><div class="wrap"><div class="section-title"><h2>Operar redes de voz exige mais do que infraestrutura.</h2><p>O novo site deixa claro onde a ZICTEC atua: na interseção entre engenharia, regulação e operação assistida.</p></div><div class="cards">
<article class="card"><div class="icon">§</div><h3>Exigências regulatórias complexas</h3><p>Regras, prazos, relatórios, evidências e atualizações exigem acompanhamento constante para evitar retrabalho e risco operacional.</p></article>
<article class="card"><div class="icon">⇄</div><h3>Interconexão e tráfego de voz</h3><p>Rotas, DETRAF, qualidade, bilhetagem, portabilidade e divergências técnicas precisam de leitura operacional e documentação.</p></article>
<article class="card"><div class="icon">◈</div><h3>SIP, SBC e estabilidade</h3><p>Falhas de borda, SDP, NAT, codecs, segurança e roteamento impactam diretamente atendimento, faturamento e reputação.</p></article>
</div></div></section>
<section class="soft"><div class="wrap"><div class="section-title"><h2>Soluções com páginas próprias.</h2><p>Conheça as principais frentes de atuação da ZICTEC em operação de voz, regulação, interconexão e autenticação de chamadas.</p></div><div class="page-list">
''') + ''.join(f'<a class="page-card" href="{h}"><b>{l}</b><span>{s}</span></a>' for l,h,s in SOL) + dedent('''
</div></div></section>
<section class="dark"><div class="wrap"><div class="section-title"><h2>Método de atuação</h2><p>Diagnóstico primeiro, escopo claro, implantação com validação e sustentação quando fizer sentido.</p></div><div class="journey"><div class="step"><h3>Diagnóstico</h3><p>Leitura da operação, rotas, SBC, obrigações e riscos.</p></div><div class="step"><h3>Projeto</h3><p>Arquitetura, entregáveis, pré-requisitos e fases.</p></div><div class="step"><h3>Implantação</h3><p>Configuração, integração, testes e evidências.</p></div><div class="step"><h3>Operação assistida</h3><p>Acompanhamento das primeiras rotinas e ajustes.</p></div><div class="step"><h3>Suporte</h3><p>Banco de horas, troubleshooting e evolução.</p></div></div></div></section>
''') + cta())

PAGES['quem-somos.html'] = layout('Quem somos — ZICTEC', 'ZICTEC: integradora e consultoria técnica para operadoras.', 'quem-somos.html', hero('Quem somos','Especialistas em operação e gestão de redes de voz para operadoras.','A ZICTEC atua como integradora e parceira técnica de operadoras STFC, provedores com telefonia e empresas com voz crítica. O foco é assumir a complexidade técnica/regulatória para que a operação cresça com estabilidade.', slim=True) + dedent('''
<section><div class="wrap split"><div><div class="section-title" style="display:block"><h2>Atuação prática, não discurso genérico.</h2><p style="margin-top:16px">A base histórica da ZICTEC combina consultoria técnica, suporte operacional, implantação de soluções e apoio regulatório para o mercado telecom.</p></div></div><div class="panel"><ul class="list"><li>Público principal: operadoras autorizadas/concessionárias STFC e provedores SCM que oferecem telefonia.</li><li>Atuação em redes de voz, VoIP, SIP, SBC, softswitch, interconexão e operação assistida.</li><li>Apoio em obrigações regulatórias, evidências, relatórios, DETRAF, QEML e processos Anatel.</li><li>Integração entre projeto técnico, implantação, suporte e evolução operacional.</li></ul></div></div></section>
<section class="soft"><div class="wrap"><div class="cards"><article class="card"><h3>Integradora técnica</h3><p>Planejamento e implantação de soluções de voz, borda e operação com fornecedores e plataformas especializadas.</p></article><article class="card"><h3>Parceira operacional</h3><p>Suporte e acompanhamento contínuo para reduzir dependência de tentativa/erro em ambientes críticos.</p></article><article class="card"><h3>Leitura regulatória</h3><p>Tradução de exigências setoriais em rotinas, dados, relatórios, controles e documentação técnica.</p></article></div></div></section>
''') + cta('Quer entender onde a ZICTEC pode ajudar?', 'Comece com uma conversa objetiva sobre cenário atual, riscos e prioridade operacional.'))

PAGES['solucoes.html'] = layout('Soluções — ZICTEC', 'Hub de soluções ZICTEC para operadoras.', 'solucoes.html', hero('Hub de soluções','Soluções técnicas e regulatórias para a operação de voz da operadora.','Páginas separadas para cada frente comercial: Origem Verificada, STFC Tools, SBC/ProSBC, regulatório Anatel e suporte técnico especializado.', '<div class="hero-actions"><a class="btn primary" href="contato.html">Solicitar diagnóstico</a><a class="btn secondary" href="segmentos.html">Ver segmentos</a></div>', slim=True) + '<section><div class="wrap"><div class="page-list">' + ''.join(f'<a class="page-card" href="{h}"><b>{l}</b><span>{s}</span></a>' for l,h,s in SOL) + '</div></div></section>' + dedent('''
<section class="soft"><div class="wrap"><div class="section-title"><h2>Como escolher o caminho certo</h2><p>Nem toda necessidade começa por produto. Muitas começam por diagnóstico e organização técnica.</p></div><table class="table"><thead><tr><th>Situação</th><th>Caminho recomendado</th></tr></thead><tbody><tr><td>Problemas de rotas, SIP, mídia ou interconexão</td><td>SBC / ProSBC + Suporte técnico</td></tr><tr><td>Necessidade de autenticar chamadas e preparar Origem Verificada</td><td>Origem Verificada / STIR-SHAKEN</td></tr><tr><td>Dificuldade com relatórios, evidências e rotinas STFC</td><td>STFC Tools + Regulatório Anatel</td></tr><tr><td>Backlog de obrigações, DETRAF, QEML ou processos</td><td>Regulatório Anatel + operação assistida</td></tr></tbody></table></div></section>
''') + cta())

PAGES['chamada-verificada.html'] = layout('Origem Verificada / STIR-SHAKEN — ZICTEC', 'Autenticação de chamadas e Origem Verificada com leitura técnica correta.', 'solucoes.html', hero('Origem Verificada / STIR-SHAKEN','Autenticação de chamadas como base para confiança, reputação e identificação futura.', 'A ZICTEC apoia operadoras na implantação da camada de autenticação STIR/SHAKEN e na preparação operacional para a iniciativa brasileira de Origem Verificada, separando corretamente protocolo, autenticação e identificação de marca.', '<div class="hero-actions"><a class="btn primary" href="https://www.chamadaverificada.com.br/" target="_blank" rel="noopener">Ver landing dedicada</a><a class="btn secondary" href="https://shop.zictec.com.br/" target="_blank" rel="noopener">Ver pacotes na loja</a></div>', slim=True) + dedent('''
<section><div class="wrap"><div class="notice"><b>Distinção essencial:</b> STIR/SHAKEN é a camada/protocolo; autenticação é a base operacional; Origem Verificada/Branded Call é a identificação de marca/campanha posterior e depende de validação técnica, credenciais, rotas, homologação e aceite.</div><div style="height:28px"></div><div class="cards"><article class="card"><h3>Diagnóstico técnico</h3><p>Leitura de rotas, SBC/softswitch, interconexão, cenário ABR Telecom e dependências para autenticação.</p></article><article class="card"><h3>Implantação assistida</h3><p>Configuração, testes e validação de caminho técnico conforme arquitetura escolhida: REST, ProSBC Client, ISBC ou modelo híbrido.</p></article><article class="card"><h3>Operação e evidências</h3><p>Apoio em homologação, documentação, troubleshooting, logs e evolução para etapas de identificação quando aplicável.</p></article></div></div></section>
<section class="soft"><div class="wrap"><div class="section-title"><h2>Caminhos comerciais</h2><p>A melhor jornada conduz para diagnóstico ou para pacotes assistidos quando o cenário já estiver claro.</p></div><div class="feature"><b>SaaS / Out-of-band</b><span>Reduz alterações profundas de rota quando aplicável, mas depende de validação do cenário real da operadora.</span></div><div class="feature"><b>Client ProSBC / STI-AS</b><span>Para ambientes que usam ProSBC e precisam integrar autenticação à borda de voz com suporte técnico.</span></div><div class="feature"><b>API REST / ZICTEC Tools</b><span>Para cenários com integração sistêmica, automação e controle mais direto via plataforma própria.</span></div></div></section>
''') + cta('Vamos mapear seu cenário de autenticação?', 'A escolha correta depende de arquitetura, rotas, SBC, status ABR e objetivo comercial.'))

PAGES['stfc-tools.html'] = layout('STFC Tools — ZICTEC', 'Ferramentas STFC Tools para operação, relatórios e evidências.', 'solucoes.html', hero('STFC Tools','APIs, relatórios e rotinas para reduzir esforço manual na operação STFC.', 'A plataforma STFC Tools concentra funcionalidades para apoiar validações, evidências, dados operacionais e exigências regulatórias geradas pela operação de telefonia.', '<div class="hero-actions"><a class="btn primary" href="contato.html">Quero avaliar STFC Tools</a></div>', slim=True) + dedent('''
<section><div class="wrap"><div class="cards"><article class="card"><h3>APIs modernas</h3><p>Integrações para automatizar consultas, validações e processos repetitivos da operação.</p></article><article class="card"><h3>Evidências e relatórios</h3><p>Organização de dados e saídas para reduzir esforço manual e melhorar rastreabilidade.</p></article><article class="card"><h3>Operação centralizada</h3><p>Plataforma em nuvem para apoiar times técnicos e administrativos na rotina STFC.</p></article></div></div></section>
<section class="soft"><div class="wrap split"><div><h2>Casos típicos</h2><p>STFC Tools é uma frente operacional concreta para reduzir fragilidade em rotinas, dados e evidências.</p></div><div class="panel"><ul class="list"><li>Atendimento a exigências regulatórias e organização de dados operacionais.</li><li>Rotinas de validação de chamadas, numeração, tráfego e evidências.</li><li>Redução de planilhas soltas e processos manuais frágeis.</li><li>Base para automações futuras conectadas à operação de voz.</li></ul></div></div></section>
''') + cta('STFC Tools pode reduzir rotina manual?', 'Vamos avaliar onde a operação perde tempo hoje e quais processos podem ser automatizados.'))

PAGES['sbc-prosbc.html'] = layout('SBC / ProSBC / Telcobridges — ZICTEC', 'Projeto, implantação e suporte SBC/ProSBC para operadoras.', 'solucoes.html', hero('SBC / ProSBC / Telcobridges','Borda SIP, interconexão e segurança para tráfego de voz crítico.', 'A ZICTEC atua no planejamento, implantação e sustentação de SBCs, com experiência em ProSBC/Telcobridges e leitura prática de problemas de SIP, mídia, roteamento e interconexão.', '<div class="hero-actions"><a class="btn primary" href="contato.html">Avaliar borda de voz</a></div>', slim=True) + dedent('''
<section><div class="wrap"><div class="cards"><article class="card"><h3>Planejamento de arquitetura</h3><p>Definição de topologia, rotas, segurança, interconexões, alta disponibilidade e requisitos de sessão.</p></article><article class="card"><h3>Implantação e migração</h3><p>Configuração, testes, cutover assistido, validação de mídia, codecs, NAT, SDP e sinalização.</p></article><article class="card"><h3>Suporte e troubleshooting</h3><p>Análise de logs, SIP traces, RCA curto com evidências e correções orientadas por teste.</p></article></div></div></section>
<section class="soft"><div class="wrap"><div class="section-title"><h2>Por que destacar SBC em página própria?</h2><p>SBC costuma aparecer quando já existe problema real ou projeto em andamento: interconexão, mídia, segurança, roteamento ou escala.</p></div><div class="tags"><span class="tag">ProSBC</span><span class="tag">Telcobridges</span><span class="tag">SIP</span><span class="tag">SDP/RTP</span><span class="tag">Interconexão</span><span class="tag">Segurança de borda</span><span class="tag">Alta disponibilidade</span></div></div></section>
''') + cta('Sua borda SIP precisa de diagnóstico?', 'Podemos começar por uma análise objetiva de rotas, sinalização, mídia e riscos.'))

PAGES['regulatorio-anatel.html'] = layout('Gestão regulatória Anatel — ZICTEC', 'Apoio técnico-regulatório para operadoras.', 'solucoes.html', hero('Gestão regulatória Anatel','Obrigações, evidências e rotinas regulatórias tratadas com visão técnica.', 'A ZICTEC apoia operadoras na organização de dados, processos e evidências ligados a obrigações setoriais, QEML, DETRAF, relatórios, numeração, STFC/SCM e demandas técnicas relacionadas à Anatel.', '<div class="hero-actions"><a class="btn primary" href="contato.html">Priorizar obrigações</a></div>', slim=True) + dedent('''
<section><div class="wrap"><div class="cards"><article class="card"><h3>Obrigações e prazos</h3><p>Mapeamento de entregas, dados necessários, riscos e responsáveis para reduzir surpresas operacionais.</p></article><article class="card"><h3>QEML e relatórios</h3><p>Apoio na coleta, consistência, validação e documentação dos indicadores e relatórios aplicáveis.</p></article><article class="card"><h3>DETRAF e interconexão</h3><p>Tratamento técnico/comercial de tráfego, divergências, rotas e documentação entre partes.</p></article></div></div></section>
<section class="soft"><div class="wrap split"><div><h2>Regulatório com engenharia junto.</h2><p>O diferencial aqui é não separar o documento da operação: muitos problemas regulatórios nascem de arquitetura, rota, bilhetagem, cadastro, evidência ou integração mal resolvida.</p></div><div class="panel"><ul class="list"><li>STFC/SCM e obrigações setoriais.</li><li>Chamadas abusivas, autenticação e reputação de chamadas.</li><li>Numeração, portabilidade/BDO/ABR Telecom e dados operacionais.</li><li>Organização de evidências para suporte a respostas e auditorias.</li></ul></div></div></section>
''') + cta('Quer organizar a frente regulatória?', 'Podemos começar por um mapa curto de obrigações, riscos e pendências técnicas.'))

PAGES['suporte.html'] = layout('Suporte técnico especializado — ZICTEC', 'Banco de horas e suporte para operação de voz.', 'solucoes.html', hero('Suporte técnico especializado','Sustentação para operações de voz que precisam de resposta técnica, evidência e continuidade.', 'Suporte por banco de horas, troubleshooting, análise de logs, RCA curto, acompanhamento de ambiente e evolução de operação SIP/STFC/SBC.', '<div class="hero-actions"><a class="btn primary" href="contato.html">Falar sobre suporte</a></div>', slim=True) + dedent('''
<section><div class="wrap"><div class="cards"><article class="card"><h3>Banco de horas</h3><p>Modelo flexível para demandas técnicas recorrentes, incidentes, ajustes e evolução da operação.</p></article><article class="card"><h3>RCA com evidência</h3><p>Análise orientada por logs, testes e reprodução, evitando diagnóstico genérico sem prova técnica.</p></article><article class="card"><h3>Operação assistida</h3><p>Apoio na estabilização após implantação, alterações de rota, mudanças de fornecedor ou expansão.</p></article></div></div></section>
<section class="soft"><div class="wrap"><div class="section-title"><h2>Escopo típico de suporte</h2><p>O suporte precisa deixar claro o tipo de atuação entregue pela ZICTEC em ambientes críticos.</p></div><table class="table"><thead><tr><th>Frente</th><th>Exemplos</th></tr></thead><tbody><tr><td>SIP/SBC</td><td>INVITE/SDP/RTP, codecs, NAT, roteamento, falhas de mídia, interconexão.</td></tr><tr><td>STFC e regulatório</td><td>Relatórios, evidências, tráfego, DETRAF, QEML e dados operacionais.</td></tr><tr><td>Plataformas</td><td>Softswitch, ProSBC, integrações, APIs e rotinas de apoio.</td></tr></tbody></table></div></section>
''') + cta('Precisa de suporte técnico recorrente?', 'Vamos estruturar um modelo de atendimento compatível com a criticidade da sua operação.'))

PAGES['segmentos.html'] = layout('Segmentos — ZICTEC', 'Perfis de operadoras e empresas atendidas pela ZICTEC.', 'segmentos.html', hero('Segmentos','Atuação ao lado de operadoras que precisam de estrutura, segurança e conformidade.', 'A ZICTEC adapta diagnóstico, implantação e suporte à realidade de cada operação: provedores que adicionam voz, operadoras STFC/VoIP, empresas com voz crítica e times que precisam organizar a frente regulatória.', slim=True) + dedent('''
<section><div class="wrap"><div class="cards"><article class="card"><h3>Provedores de Internet com telefonia</h3><p>Estruturação técnica e regulatória para ISP/SCM que opera ou pretende operar serviços de voz.</p></article><article class="card"><h3>Operadoras STFC e VoIP</h3><p>Apoio em interconexão, operação, relatórios, SBC, autenticação de chamadas e sustentação técnica.</p></article><article class="card"><h3>Empresas com voz crítica</h3><p>Ambientes que dependem de estabilidade, roteamento, gravação, segurança e integração com plataformas de atendimento.</p></article></div></div></section>
<section class="soft"><div class="wrap split"><div><h2>Mesmo tema, prioridades diferentes.</h2><p>Um provedor em expansão precisa de implantação e organização; uma operadora madura pode precisar de otimização, evidência e sustentação; um call center pode priorizar estabilidade e reputação.</p></div><div class="panel"><ul class="list"><li>Diagnóstico por estágio de maturidade.</li><li>Priorização por risco operacional e regulatório.</li><li>Plano técnico/comercial com próximos passos claros.</li></ul></div></div></section>
''') + cta())

PAGES['contato.html'] = layout('Contato — ZICTEC', 'Fale com a ZICTEC para diagnóstico técnico.', 'contato.html', hero('Contato','Vamos começar pelo problema certo.', 'Para evitar proposta genérica, a ZICTEC deve conduzir o primeiro contato por diagnóstico técnico: operação atual, dores, fornecedores, obrigações, rotas, prazos e objetivo comercial.', '<div class="hero-actions"><a class="btn primary" href="https://www.calendly.com/zictec/reuniao" target="_blank" rel="noopener">Agendar reunião</a><a class="btn secondary" href="mailto:suporte@zictec.com.br">suporte@zictec.com.br</a></div>', slim=True) + dedent('''
<section><div class="wrap"><div class="cards"><article class="card"><h3>Agendar diagnóstico</h3><p>Use o Calendly para uma conversa inicial com foco técnico/comercial.</p><p style="margin-top:14px"><a class="btn ghost" href="https://www.calendly.com/zictec/reuniao" target="_blank" rel="noopener">Abrir Calendly</a></p></article><article class="card"><h3>Email</h3><p>Envie cenário, urgência e contatos técnicos para agilizar triagem.</p><p style="margin-top:14px"><a class="btn ghost" href="mailto:suporte@zictec.com.br">suporte@zictec.com.br</a></p></article><article class="card"><h3>WhatsApp e loja</h3><p>Para falar com especialista, use o WhatsApp da ZICTEC; quando o cenário já estiver claro, consulte também os pacotes da loja.</p><p style="margin-top:14px"><a class="btn ghost" href="https://wa.me/554732300435" target="_blank" rel="noopener">Falar com especialista</a></p><p style="margin-top:10px"><a class="btn ghost" href="https://shop.zictec.com.br/" target="_blank" rel="noopener">shop.zictec.com.br</a></p></article></div></div></section>
<section class="soft"><div class="wrap"><div class="section-title"><h2>Informações úteis para a primeira conversa</h2><p>Esses dados ajudam a transformar a conversa em diagnóstico real.</p></div><div class="panel"><ul class="list"><li>Tipo de operação: STFC, VoIP, ISP com telefonia, call center ou ambiente corporativo.</li><li>Plataformas envolvidas: SBC, softswitch, ProSBC, ISBC, gateways, fornecedores e rotas.</li><li>Dor principal: estabilidade, mídia, interconexão, regulatório, DETRAF/QEML, autenticação, suporte ou expansão.</li><li>Urgência, evidências disponíveis, logs, prints e histórico de incidentes.</li></ul></div></div></section>
'''))


BLOG_ARTICLES = [
    {
        "slug": "isp-stfc-vale-a-pena.html",
        "category": "STFC para ISPs",
        "title": "ISP e STFC: quando faz sentido entrar em telefonia fixa?",
        "desc": "Um guia prático para provedores avaliarem telefonia fixa como produto, operação e responsabilidade regulatória.",
        "tags": ["STFC", "ISP", "Telefonia", "Anatel"],
        "body": """
<h2>Telefonia pode ser uma nova receita, mas não deve ser tratada como anexo da internet.</h2>
<p>Para muitos provedores regionais, adicionar telefonia fixa parece uma extensão natural da base de clientes. A oportunidade existe: o ISP já tem relacionamento, cobrança, atendimento e presença local. O risco aparece quando a voz é vendida sem operação preparada.</p>
<p>STFC envolve autorização, numeração, interconexão, portabilidade, bilhetagem, qualidade, suporte, relatórios e evidências. Não é apenas ativar um tronco SIP e criar planos comerciais.</p>
<h2>Quando faz sentido avançar</h2>
<ul><li>Quando existe base empresarial pedindo telefone fixo, PABX, canais de atendimento ou portabilidade.</li><li>Quando o provedor quer aumentar ARPU sem depender só de banda larga.</li><li>Quando há capacidade de organizar suporte técnico, faturamento e rotina regulatória.</li><li>Quando a operação aceita implantar controles antes de escalar vendas.</li></ul>
<h2>Quando é melhor segurar</h2>
<ul><li>Se a empresa não sabe quem responderá por incidentes de voz.</li><li>Se não há clareza sobre interconexão, numeração, portabilidade e DETRAF.</li><li>Se a telefonia será vendida por preço, sem estratégia comercial.</li><li>Se o suporte atual ainda não está preparado para diagnosticar SIP, mídia, rota e equipamento do cliente.</li></ul>
<h2>Checklist mínimo antes de vender</h2>
<ul><li>Modelo de autorização e escopo do serviço.</li><li>Arquitetura de softswitch/SBC/interconexão.</li><li>Processo de portabilidade e cadastro.</li><li>Bilhetagem, tarifação e conciliação de tráfego.</li><li>Rotina de suporte e análise de logs.</li><li>Responsáveis por obrigações Anatel e evidências.</li></ul>
<h2>Como a ZICTEC ajuda</h2>
<p>A ZICTEC pode apoiar desde o diagnóstico de viabilidade até a arquitetura, operação assistida, automação com STFC Tools, interconexão, SBC e rotinas regulatórias. O objetivo é transformar telefonia em produto sustentável — não em fonte recorrente de retrabalho.</p>
"""
    },
    {
        "slug": "detraf-na-pratica.html",
        "category": "DETRAF e interconexão",
        "title": "DETRAF na prática: onde operadoras perdem dinheiro sem perceber",
        "desc": "Por que divergências de tráfego, bilhetagem e interconexão podem virar prejuízo recorrente para operadoras de voz.",
        "tags": ["DETRAF", "Interconexão", "STFC", "Bilhetagem"],
        "body": """
<h2>DETRAF não é só um relatório: é uma rotina de controle financeiro e operacional.</h2>
<p>O Detalhamento de Tráfego entre operadoras afeta valores a pagar e a receber, conciliação de rotas e leitura de interconexão. Quando a operação não tem controle, pequenas divergências viram perda recorrente.</p>
<h2>Onde surgem as divergências</h2>
<ul><li>Rotas configuradas de forma diferente entre as partes.</li><li>Classificação incorreta de tráfego local, longa distância ou móvel.</li><li>Bilhetagem inconsistente entre softswitch, SBC e sistema financeiro.</li><li>Eventos de portabilidade não refletidos corretamente na rota.</li><li>Ausência de histórico organizado para contestação.</li></ul>
<h2>Sinais de alerta</h2>
<ul><li>Conciliação feita manualmente em planilhas isoladas.</li><li>Valores aceitos sem conferência técnica.</li><li>Diferença recorrente entre CDRs internos e cobrança recebida.</li><li>Dependência de uma pessoa específica para explicar tráfego.</li></ul>
<h2>O que uma rotina madura precisa ter</h2>
<ul><li>CDRs íntegros e rastreáveis.</li><li>Critérios claros de classificação de chamadas.</li><li>Comparação recorrente entre tráfego interno e externo.</li><li>Documentação de divergências e evidências.</li><li>Integração entre engenharia, regulatório e financeiro.</li></ul>
<h2>Como a ZICTEC posiciona essa frente</h2>
<p>A ZICTEC pode ajudar a revisar arquitetura, bilhetagem, interconexão, dados e automações para que o DETRAF deixe de ser apenas obrigação e vire instrumento de controle operacional.</p>
"""
    },
    {
        "slug": "sipi-sbc-interconexao.html",
        "category": "SIP-I / SBC",
        "title": "SIP-I, SBC e interconexão: a arquitetura mínima para operar voz com segurança",
        "desc": "Uma leitura técnica e comercial sobre borda SIP, migração de interconexão, segurança e estabilidade em operações de voz.",
        "tags": ["SIP-I", "SBC", "Interconexão", "ProSBC"],
        "body": """
<h2>Interconexão de voz precisa de controle de borda.</h2>
<p>Em uma operação de voz, o SBC não deve ser visto apenas como equipamento. Ele é ponto de controle para sinalização, mídia, segurança, normalização, roteamento, proteção e visibilidade técnica.</p>
<h2>Por que SIP-I exige atenção</h2>
<p>SIP-I transporta informações de sinalização legadas em ambiente IP. Isso cria uma ponte entre mundos diferentes: rede tradicional, requisitos de interconexão e infraestrutura moderna. Uma implantação mal planejada pode gerar falhas de completamento, problemas de mídia, divergência de sinalização e dificuldade de troubleshooting.</p>
<h2>Funções críticas do SBC</h2>
<ul><li>Controle de borda entre redes e fornecedores.</li><li>Normalização de SIP/SDP e tratamento de interoperabilidade.</li><li>Proteção contra tráfego indevido e abuso.</li><li>Roteamento, failover e política de chamadas.</li><li>Visibilidade para análise de logs, SIP traces e RCA.</li><li>Base para autenticação de chamadas e futuras integrações.</li></ul>
<h2>Checklist de arquitetura</h2>
<ul><li>Quais interconexões existem hoje?</li><li>Há separação clara entre cliente, fornecedor e interconexão?</li><li>Os CDRs batem com a rota e com o faturamento?</li><li>Existe alta disponibilidade ou contingência documentada?</li><li>O time consegue capturar e interpretar SIP traces?</li></ul>
<h2>Como a ZICTEC ajuda</h2>
<p>A ZICTEC atua em diagnóstico, projeto, implantação e sustentação de ambientes SIP/SBC, incluindo ProSBC/Telcobridges, rotas, interconexão, troubleshooting e evolução operacional.</p>
"""
    },
    {
        "slug": "stir-shaken-origem-verificada.html",
        "category": "Chamada Verificada",
        "title": "STIR/SHAKEN e Origem Verificada: o caminho para chamadas com mais confiança",
        "desc": "Entenda a diferença entre protocolo, autenticação de chamadas e identificação de marca/campanha no contexto brasileiro.",
        "tags": ["STIR/SHAKEN", "Origem Verificada", "Chamada Verificada", "Reputação"],
        "body": """
<h2>Confiança na chamada virou tema de infraestrutura, regulação e negócio.</h2>
<p>Empresas que dependem do telefone enfrentam um problema crescente: o usuário desconfia da chamada antes mesmo de atender. Spoofing, chamadas abusivas e baixa reputação afetam atendimento, cobrança, vendas e relacionamento.</p>
<h2>Três camadas que não devem ser confundidas</h2>
<ul><li><b>STIR/SHAKEN:</b> camada técnica/protocolo para autenticação da origem da chamada.</li><li><b>Autenticação:</b> operação que permite trafegar chamadas com validação conforme regras e ecossistema aplicáveis.</li><li><b>Origem Verificada / Branded Call:</b> camada posterior de identificação de marca/campanha, sujeita a validação, credenciais, rotas, homologação e aceite.</li></ul>
<h2>O que isso muda para operadoras</h2>
<ul><li>Exige revisão de rotas, SBC, interconexão e sistemas.</li><li>Cria demanda por logs, evidências e troubleshooting.</li><li>Conecta engenharia de voz com área comercial e reputação.</li><li>Abre espaço para serviços de preparação, implantação e operação assistida.</li></ul>
<h2>O que não devemos prometer</h2>
<p>Não se deve prometer logo na tela apenas porque existe STIR/SHAKEN. Identificação de marca depende de etapa específica, governança, homologação e regras da iniciativa aplicável.</p>
<h2>Como a ZICTEC ajuda</h2>
<p>A ZICTEC apoia diagnóstico, escolha de arquitetura, implantação assistida, testes, evidências, operação e preparação para evolução rumo à Origem Verificada quando o cenário técnico e comercial permitir.</p>
"""
    },
]

def blog_index():
    cards = ''
    for a in BLOG_ARTICLES:
        tags = ''.join(f'<span>{t}</span>' for t in a['tags'])
        thumb = f'<img src="{a.get("image", "")}" alt="Ilustração do artigo {a["title"]}">' if a.get('image') else ''
        cards += f"""<a class="blog-card" href="{a['slug']}">{thumb}<span class="k">{a['category']}</span><h3>{a['title']}</h3><p>{a['desc']}</p><div class="article-meta">{tags}</div></a>"""
    return layout('Blog ZICTEC — Conteúdo técnico para operadoras', 'Central de conteúdo ZICTEC sobre STFC, SIP, SBC, DETRAF, Origem Verificada e operação de voz.', 'blog.html', hero('Blog ZICTEC', 'Conteúdo técnico-comercial para quem opera voz, STFC e telecom com responsabilidade.', 'Guias práticos, checklists e análises para transformar regulação, interconexão, SIP/SBC e autenticação de chamadas em decisões operacionais melhores.', '<div class="hero-actions"><a class="btn primary" href="contato.html">Sugerir pauta / diagnóstico</a><a class="btn secondary" href="solucoes.html">Ver soluções</a></div>', slim=True) + f"""<section><div class="wrap"><div class="editorial-note"><b>Modo editorial:</b> esta seção é rascunho versionado para aprovação. Ela não altera o site principal publicado; serve para validar pauta, tom, SEO e estrutura antes de qualquer migração para WordPress/domínio oficial.</div><div style="height:28px"></div><div class="blog-grid">{cards}</div></div></section>""" + cta('Quer transformar uma dor da operação em conteúdo?', 'Podemos priorizar pautas por demanda comercial: STFC, DETRAF, SBC, Origem Verificada, suporte ou regulatório.'))

def article_page(a):
    meta = ''.join(f'<span>{t}</span>' for t in a['tags'])
    body = a['body']
    toc_links = []
    for idx, heading in enumerate(re.findall(r'<h2>(.*?)</h2>', body), start=1):
        anchor = f'sec-{idx}'
        body = body.replace(f'<h2>{heading}</h2>', f'<h2 id="{anchor}">{heading}</h2>', 1)
        label = re.sub(r'<[^>]+>', '', heading)
        toc_links.append(f'<a href="#{anchor}">{label}</a>')
    toc = '<div class="toc"><b>Neste artigo</b>' + ''.join(toc_links) + '<a href="#contato">Como a ZICTEC pode ajudar</a><a href="blog.html">← Voltar para o blog</a></div>'
    fig = ''
    if a.get('image'):
        fig = f'<figure class="article-figure"><img src="{a["image"]}" alt="Ilustração premium: {a["title"]}"><figcaption>Ilustração conceitual ZICTEC para apoiar a leitura técnica do tema.</figcaption></figure>'
    return layout(a['title'] + ' — Blog ZICTEC', a['desc'], 'blog.html', hero(a['category'], a['title'], a['desc'], '<div class="hero-actions"><a class="btn primary" href="contato.html">Falar com especialista</a><a class="btn secondary" href="blog.html">Voltar ao blog</a></div>', slim=True) + f"""<section><div class="wrap article-body"><div class="article-meta">{meta}</div>{fig}{toc}{body}<div id="contato"></div></div></section>""" + cta('Vamos aplicar isso na sua operação?', 'A ZICTEC pode transformar o tema em diagnóstico, plano técnico e próximos passos com escopo claro.'))


DEEP_BLOG_UPDATES = {
    "isp-stfc-vale-a-pena.html": {
        "image": "assets/blog/isp-stfc-voice-ops.svg",
        "desc": "Como avaliar telefonia fixa como produto, operação, margem e responsabilidade regulatória — sem transformar voz em custo invisível.",
        "body": """
<h2>Telefonia pode aumentar margem — ou virar uma fonte silenciosa de custo.</h2>
<p>Para o ISP regional, telefonia fixa costuma parecer uma oportunidade natural: a empresa já tem cliente, cobrança, suporte, infraestrutura IP e presença local. Mas voz não é apenas mais um serviço no combo. É uma operação com responsabilidades próprias: autorização, numeração, interconexão, portabilidade, bilhetagem, atendimento, disponibilidade e obrigações regulatórias.</p>
<p>O ponto central não é “ter ou não ter STFC”. É saber se a operação está preparada para vender, entregar, medir e sustentar telefonia sem depender de improviso.</p>
<h2>Quando a telefonia faz sentido para um provedor</h2>
<ul><li><b>Base empresarial ativa:</b> clientes B2B pedem telefone fixo, PABX, portabilidade, ramais, atendimento e continuidade.</li><li><b>Necessidade de aumentar ARPU:</b> voz pode complementar conectividade, especialmente em contas corporativas.</li><li><b>Capacidade de operação:</b> existe time ou parceiro para tratar SIP, CDR, rotas, portabilidade, incidentes e relatórios.</li><li><b>Estratégia comercial clara:</b> telefonia é vendida como solução, não como “mais um item barato”.</li></ul>
<h2>Onde muitos provedores erram</h2>
<p>O erro mais comum é tratar telefonia como revenda simples. A venda acontece, mas depois surgem chamados sobre áudio unilateral, chamadas que não completam, portabilidade parada, divergência de cobrança, falhas de PABX, problemas de rota e dúvidas regulatórias. Sem processo, isso consome margem.</p>
<h2>Checklist mínimo antes de escalar vendas</h2>
<ul><li>Modelo de autorização e escopo de serviço.</li><li>Arquitetura de softswitch, SBC, rotas e interconexões.</li><li>Processo de portabilidade e cadastro de numeração.</li><li>Bilhetagem confiável e conciliação de tráfego.</li><li>Rotina de suporte com logs, testes e responsáveis.</li><li>Controle de obrigações Anatel, QEML, DETRAF e evidências quando aplicável.</li></ul>
<h2>O gancho comercial correto</h2>
<p>Antes de investir em campanha de telefonia, o provedor deveria fazer um diagnóstico curto: onde está a margem, onde está o risco e quais rotinas precisam existir para a operação não vender prejuízo. A ZICTEC pode apoiar essa leitura e estruturar o caminho técnico, regulatório e operacional.</p>
"""
    },
    "detraf-na-pratica.html": {
        "image": "assets/blog/detraf-conciliacao-operadora.svg",
        "desc": "Por que prestadoras menores muitas vezes pagam DETRAF cegamente, deixam de apresentar cobranças devidas e perdem margem sem perceber.",
        "body": """
<h2>O problema real: muitas prestadoras sequer apresentam DETRAF.</h2>
<p>Em operações de menor porte, é comum o DETRAF ser tratado como uma cobrança recebida — não como uma rotina ativa de conciliação. A prestadora recebe demonstrativos de outra operadora, paga o que foi cobrado e raramente confere tecnicamente se aquele valor está correto.</p>
<p>O prejuízo aparece em duas frentes: a empresa pode <b>pagar a mais</b> por divergência de classificação, tráfego ou rota; e também pode <b>deixar de receber</b> valores que teria direito a cobrar, simplesmente porque não apresenta seu próprio DETRAF ou não sustenta a conciliação com evidências.</p>
<h2>DETRAF não é só burocracia: é margem operacional.</h2>
<p>O Detalhamento de Tráfego entre operadoras conecta engenharia, faturamento e backoffice. Quando ele não existe, ou quando é feito de forma frágil, a operação deixa dinheiro na mesa. Em telecom, uma diferença pequena repetida todos os meses vira custo estrutural invisível.</p>
<h2>Onde o dinheiro escapa</h2>
<ul><li><b>Pagamento cego:</b> aceitar a cobrança de outra operadora sem confrontar com CDRs próprios.</li><li><b>Ausência de apresentação:</b> não cobrar tráfego que deveria ser cobrado da outra parte.</li><li><b>Classificação incorreta:</b> chamadas locais, longa distância, móvel/fixo ou rotas tratadas de forma diferente entre as partes.</li><li><b>Portabilidade e BDO:</b> eventos de portabilidade não refletidos corretamente na rota e no cálculo.</li><li><b>Falta de evidência:</b> sem dados consistentes, a contestação perde força.</li></ul>
<h2>Por que isso acontece nas pequenas e médias</h2>
<p>Muitas prestadoras cresceram com foco em rede e cliente final, não em backoffice de telefonia. O conhecimento de DETRAF fica concentrado em uma pessoa, em planilhas ou em rotinas manuais. Quando há troca de equipe, mudança de fornecedor ou aumento de tráfego, a fragilidade aparece.</p>
<h2>Como uma rotina madura deveria funcionar</h2>
<ul><li>Geração recorrente de DETRAF com CDRs íntegros.</li><li>Conciliação entre tráfego próprio, cobrança recebida e valores a apresentar.</li><li>Critérios claros de cálculo, classificação e contestação.</li><li>Backoffice documentado para envio, acompanhamento e negociação.</li><li>Histórico de evidências para auditoria, divergência e revisão.</li></ul>
<h2>O papel da tecnologia e do backoffice</h2>
<p>A ZICTEC possui solução para DETRAF em plataformas já homologadas, com possibilidade de customização conforme o cenário da prestadora. Além da parte técnica, também é possível apoiar a rotina burocrática/backoffice: apresentação, conferência, conciliação, organização de evidências e acompanhamento do ciclo.</p>
<h2>Gancho comercial</h2>
<p>Se a prestadora hoje apenas paga o que recebe, sem conferir e sem apresentar seus próprios valores, o primeiro passo não é uma landing page: é um diagnóstico. Mapear tráfego, fontes de CDR, cobranças recebidas e valores não apresentados pode revelar economia e receita recorrente antes invisíveis.</p>
"""
    },
    "sipi-sbc-interconexao.html": {
        "image": "assets/blog/sipi-bgp-sbc-redundancia.svg",
        "desc": "SIP-I não é SIP comum: entenda ISUP, legado SS7, perfil brasileiro, links dedicados, BGP e redundância com pares de SBCs.",
        "body": """
<h2>SIP-I não é “SIP normal com outro nome”.</h2>
<p>Uma interconexão SIP comum costuma tratar sinalização VoIP entre plataformas IP. SIP-I é diferente: ele carrega informações ISUP dentro de mensagens SIP, preservando elementos importantes da sinalização tradicional usada nas redes legadas. Na prática, é uma ponte entre o mundo IP e o legado SS7/ISUP.</p>
<p>Por isso, uma interconexão SIP-I exige atenção a perfil, parâmetros, interoperabilidade e homologação. Não basta “abrir um trunk SIP”.</p>
<h2>ISUP, SS7 e a evolução para SIP-I</h2>
<p>Historicamente, redes de telefonia usaram SS7 como arquitetura de sinalização, com ISUP para controle de chamadas. Com a migração para IP, surgiu a necessidade de transportar essa lógica em redes SIP sem perder informações relevantes para interconexão entre operadoras.</p>
<p>O SIP-I encapsula conteúdo ISUP em SIP, permitindo que redes modernas IP conversem com requisitos e semântica herdados do ambiente de telefonia tradicional.</p>
<h2>Versões e perfil adotado no Brasil</h2>
<p>Existem variações e perfis de implementação. Para funcionar em uma interconexão real no Brasil, a operadora precisa seguir o perfil específico aceito pelas partes e adotado no ecossistema nacional. Diferenças aparentemente pequenas em ISUP, cabeçalhos, parâmetros, timers ou tratamento de causas podem impedir completamento, afetar tarifação ou dificultar portabilidade e roteamento.</p>
<h2>Novas interconexões e o movimento para SIP-I</h2>
<p>Na prática de mercado, novas interconexões vêm sendo estruturadas em SIP-I, substituindo gradualmente modelos TDM/legados. Isso reduz dependência de infraestrutura tradicional, mas aumenta a exigência sobre SBC, roteamento IP, segurança, observabilidade e homologação técnica.</p>
<h2>Internet pública ou link dedicado?</h2>
<p>Algumas modalidades podem usar conectividade sobre internet pública, especialmente em cenários específicos ou menores. Porém, grandes operadoras normalmente trabalham com links dedicados de interconexão, com endereçamento, roteamento e políticas próprias.</p>
<p>Nesses ambientes, é comum existir desenho com redundância, BGP, rotas controladas e conexões cruzadas entre pares de SBCs. A ideia é evitar ponto único de falha e garantir continuidade mesmo durante falha de link, equipamento ou caminho.</p>
<h2>Arquitetura típica de alta disponibilidade</h2>
<ul><li>Dois SBCs de um lado e dois SBCs do outro.</li><li>Links dedicados redundantes, frequentemente cruzados.</li><li>Roteamento BGP para preferência, contingência e failover.</li><li>Políticas de segurança, ACLs, NAT/control-plane e proteção de sinalização.</li><li>Captura de SIP traces, CDRs e métricas para diagnóstico.</li></ul>
<h2>Onde projetos falham</h2>
<ul><li>Tratar SIP-I como SIP comum.</li><li>Ignorar o perfil ISUP esperado pela outra operadora.</li><li>Não validar causas, timers, codecs, SDP e roteamento antes do tráfego real.</li><li>Não documentar topologia, BGP, redundância e janelas de teste.</li><li>Não ter SBC preparado para troubleshooting.</li></ul>
<h2>Gancho comercial</h2>
<p>A ZICTEC pode apoiar diagnóstico, desenho, implantação e sustentação de interconexões SIP-I, incluindo SBC/ProSBC, roteamento, testes, homologação, análise de traces e documentação técnica para operação.</p>
"""
    },
    "stir-shaken-origem-verificada.html": {
        "image": "assets/blog/stir-shaken-historico-origem.svg",
        "desc": "Histórico, evolução internacional, adoção no Brasil e tendências de autenticação, reputação e identificação de chamadas.",
        "body": """
<h2>STIR/SHAKEN nasceu como resposta a um problema de confiança.</h2>
<p>Durante anos, redes telefônicas permitiram que a identificação de origem da chamada fosse manipulada com relativa facilidade. Isso abriu espaço para spoofing, robocalls, golpes, chamadas abusivas e degradação da confiança do usuário no telefone.</p>
<p>Nos Estados Unidos e Canadá, o volume de chamadas fraudulentas acelerou a adoção de mecanismos técnicos e regulatórios para autenticar a origem das chamadas. É nesse contexto que surgem STIR e SHAKEN.</p>
<h2>STIR e SHAKEN: de onde vêm os nomes</h2>
<p><b>STIR</b> vem de Secure Telephone Identity Revisited, um conjunto de especificações ligado ao IETF para identidade segura em chamadas. <b>SHAKEN</b> é o framework operacional usado principalmente em redes IP de operadoras, com governança, certificados e procedimentos para aplicar a autenticação em escala.</p>
<p>Em termos simples: STIR/SHAKEN permite assinar e verificar informações de origem da chamada, ajudando a indicar se aquele tráfego veio de uma fonte autorizada ou confiável.</p>
<h2>Evolução internacional</h2>
<p>Nos EUA, a FCC pressionou operadoras a adotarem autenticação de chamadas como parte do combate a robocalls. No Canadá, a adoção também avançou com regulação e governança setorial. A tecnologia não eliminou fraude sozinha, mas criou uma camada essencial de rastreabilidade e confiança.</p>
<p>Com o tempo, o tema deixou de ser apenas técnico. Passou a envolver reputação de chamadas, analytics, políticas de bloqueio, identificação de marca e experiência do usuário na tela do telefone.</p>
<h2>Adoção no Brasil</h2>
<p>No Brasil, o tema evolui conectado ao combate a chamadas abusivas, à identificação de chamadas e ao ecossistema operacional envolvendo Anatel, operadoras e entidades setoriais. A iniciativa de Origem Verificada amplia a conversa: não basta autenticar tecnicamente; empresas querem que o usuário reconheça quem está chamando.</p>
<p>Mas é fundamental separar as camadas. Autenticação e identificação de marca não são a mesma entrega.</p>
<h2>Três camadas que não devem ser confundidas</h2>
<ul><li><b>STIR/SHAKEN:</b> protocolo/camada técnica de autenticação.</li><li><b>Autenticação de chamadas:</b> operação que permite trafegar chamadas com validação conforme regras, certificados, rotas e arquitetura.</li><li><b>Origem Verificada / Branded Call:</b> identificação visual/comercial da marca ou campanha, dependente de critérios, governança, homologação, credenciais, rotas e aceite.</li></ul>
<h2>Tendências</h2>
<ul><li>Maior pressão contra spoofing e chamadas abusivas.</li><li>Integração entre autenticação, reputação e analytics.</li><li>Demanda de empresas por identificação confiável na tela do usuário.</li><li>Operadoras precisando preparar SBC, rotas, logs e evidências.</li><li>Separação comercial entre autenticar a chamada e exibir marca/campanha.</li></ul>
<h2>O que não devemos prometer</h2>
<p>Não se deve prometer logo na tela apenas porque existe STIR/SHAKEN. A exibição de marca depende de uma etapa própria e de aceite operacional/comercial. O papel correto é preparar a base técnica, autenticar quando aplicável e evoluir para Origem Verificada conforme regras e viabilidade.</p>
<h2>Gancho comercial</h2>
<p>A ZICTEC pode apoiar operadoras em diagnóstico, escolha de arquitetura, integração com SBC/ProSBC ou API, testes, evidências, operação assistida e preparação para a jornada de Origem Verificada sem misturar promessa técnica com promessa comercial.</p>
"""
    }
}

for _article in BLOG_ARTICLES:
    _article.update(DEEP_BLOG_UPDATES.get(_article["slug"], {}))

PAGES['blog.html'] = blog_index()
for _article in BLOG_ARTICLES:
    PAGES[_article['slug']] = article_page(_article)

(ROOT / 'styles.css').write_text(CSS, encoding='utf-8')
for name, html in PAGES.items():
    (ROOT / name).write_text(html, encoding='utf-8')
print('wrote', len(PAGES), 'pages + styles.css')
