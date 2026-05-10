"""Visual styling for the NextCure Intelligence System."""

from __future__ import annotations

import streamlit as st


def inject_global_styles() -> None:
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: radial-gradient(circle at top left, rgba(124, 58, 237, 0.25), transparent 28%),
                        radial-gradient(circle at top right, rgba(14, 165, 233, 0.15), transparent 26%),
                        linear-gradient(135deg, #080B18 0%, #111827 44%, #1E1B4B 100%);
            color: #F8FAFC;
        }
        [data-testid="stHeader"] { background: rgba(8, 11, 24, 0); }
        [data-testid="stToolbar"] { display: none; }
        .block-container { max-width: 1220px; padding-top: 2.4rem; }
        .hero {
            padding: 2.2rem 2.4rem;
            border: 1px solid rgba(255,255,255,.12);
            background: rgba(15, 23, 42, .74);
            border-radius: 28px;
            box-shadow: 0 28px 80px rgba(0,0,0,.35);
            backdrop-filter: blur(18px);
        }
        .eyebrow { color: #A78BFA; font-size: .78rem; letter-spacing: .18em; text-transform: uppercase; font-weight: 700; }
        .hero h1 { font-size: 3.1rem; line-height: 1.02; margin: .55rem 0; color: #FFFFFF; }
        .hero p { color: #CBD5E1; font-size: 1.05rem; max-width: 760px; }
        .status-pill, .detail-pill {
            display: inline-flex; align-items: center; gap: .45rem; padding: .42rem .72rem;
            border-radius: 999px; border: 1px solid rgba(167,139,250,.35);
            color: #EDE9FE; background: rgba(124,58,237,.12); font-size: .78rem; font-weight: 650;
        }
        .detail-pill { margin-top: .75rem; border-color: rgba(14,165,233,.35); background: rgba(14,165,233,.10); color: #BAE6FD; }
        .card {
            padding: 1.15rem 1.2rem; border: 1px solid rgba(255,255,255,.10);
            background: rgba(15, 23, 42, .68); border-radius: 22px;
            box-shadow: 0 18px 50px rgba(0,0,0,.22); height: 100%;
        }
        .metric-label { color: #94A3B8; font-size: .82rem; }
        .metric-value { color: #FFFFFF; font-size: 1.45rem; font-weight: 800; margin-top: .25rem; overflow-wrap:anywhere; line-height:1.14; }
        .card-caption { font-size:.80rem; margin-top:.45rem; line-height:1.35; }
        .section-title { font-size: 1.25rem; font-weight: 800; color: #FFFFFF; margin: 1rem 0 .4rem; }
        .muted { color: #94A3B8; }
        .insight {
            padding: 1rem 1.1rem; margin-bottom: .75rem; border-radius: 18px;
            background: rgba(124,58,237,.12); border: 1px solid rgba(167,139,250,.18); color: #E2E8F0;
        }
        .executive-grid, .snapshot-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 1rem;
            margin: .75rem 0 1.1rem;
        }
        .snapshot-card {
            min-height: 150px;
            padding: 1rem 1.05rem;
            border: 1px solid rgba(255,255,255,.10);
            background: linear-gradient(180deg, rgba(15,23,42,.78), rgba(15,23,42,.52));
            border-radius: 22px;
            box-shadow: 0 18px 50px rgba(0,0,0,.20);
        }
        .snapshot-card .metric-value {
            color: #FFFFFF;
            font-size: 1.05rem;
            font-weight: 850;
            line-height: 1.24;
            margin-top: .35rem;
            overflow-wrap: break-word;
            word-break: normal;
            hyphens: auto;
        }
        .summary-card, .executive-narrative, .synthesis-card {
            padding: 1.15rem 1.2rem;
            border-radius: 22px;
            background: rgba(15, 23, 42, .70);
            border: 1px solid rgba(255,255,255,.10);
            box-shadow: 0 18px 50px rgba(0,0,0,.22);
            margin-bottom: .85rem;
        }
        .executive-narrative {
            background: linear-gradient(135deg, rgba(14,165,233,.14), rgba(124,58,237,.12));
            border-color: rgba(14,165,233,.24);
        }
        .synthesis-card {
            background: linear-gradient(180deg, rgba(15,23,42,.82), rgba(30,27,75,.44));
            border-color: rgba(167,139,250,.22);
            min-height: 245px;
        }
        .summary-title { color:#FFFFFF; font-weight: 850; font-size: 1rem; margin-bottom: .35rem; }
        .summary-body { color:#CBD5E1; line-height:1.5; }
        .ticker-card {
            padding: .95rem 1rem; border: 1px solid rgba(255,255,255,.10);
            background: rgba(15, 23, 42, .58); border-radius: 18px; text-align: center;
        }
        .ticker-symbol { color: #FFFFFF; font-size: 1.1rem; font-weight: 800; }
        .ticker-read { color: #94A3B8; font-size: .80rem; margin-top: .25rem; }
        div.stButton > button:first-child {
            width: auto;
            min-height: 2.35rem;
            border-radius: 999px;
            border: 1px solid rgba(14,165,233,.32);
            background: rgba(14,165,233,.10);
            color: #E0F2FE;
            font-weight: 800;
            letter-spacing: 0;
            font-size: .84rem;
            padding: .45rem .95rem;
            box-shadow: none;
        }
        div.stButton > button:first-child:hover {
            transform: translateY(-1px);
            filter: brightness(1.08);
            border-color: rgba(125,211,252,.55);
            color: #FFFFFF;
        }
        div.stButton > button[kind="primary"] {
            width: 100%;
            min-height: 3.3rem;
            border-radius: 18px;
            border: 0;
            background: linear-gradient(135deg, #7C3AED, #2563EB);
            color: white;
            font-weight: 850;
            letter-spacing: .04em;
            box-shadow: 0 18px 45px rgba(37, 99, 235, .28);
        }
        .nav-title { color:#94A3B8; font-size:.78rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase; margin:.25rem 0 .35rem; }
        .nav-shell { margin: .4rem 0 1rem; }
        div[data-testid="stHorizontalBlock"] div.stButton > button:first-child {
            white-space: nowrap;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: .45rem;
            flex-wrap: wrap;
            overflow: visible !important;
        }
        .stTabs [data-baseweb="tab-border"] { display: none; }
        .stTabs [data-baseweb="tab-highlight"] { background: #FB7185; }
        .stTabs [data-baseweb="tab"] {
            border-radius: 999px; padding: .55rem 1rem; background: rgba(255,255,255,.06);
            color: #CBD5E1; min-width: auto;
        }
        .stTabs [aria-selected="true"] { background: rgba(124,58,237,.30); color: #FFFFFF; }
        .stTabs button[aria-label*="scroll"], .stTabs button[title*="scroll"], .stTabs button[kind="secondary"] {
            background: rgba(15,23,42,.85) !important;
            color: #CBD5E1 !important;
            border: 1px solid rgba(255,255,255,.12) !important;
            border-radius: 999px !important;
            box-shadow: none !important;
        }
        [data-testid="stExpander"] {
            border: 1px solid rgba(255,255,255,.10);
            border-radius: 18px;
            background: rgba(15,23,42,.48);
        }

        .exec-data-note {
            display: inline-flex;
            align-items: center;
            margin: .1rem 0 1rem;
            padding: .48rem .78rem;
            border-radius: 999px;
            font-size: .78rem;
            font-weight: 750;
            letter-spacing: .01em;
            border: 1px solid rgba(255,255,255,.10);
        }
        .exec-data-note.good { color:#BBF7D0; background: rgba(22,163,74,.12); border-color: rgba(34,197,94,.26); }
        .exec-data-note.warn { color:#FDE68A; background: rgba(245,158,11,.12); border-color: rgba(245,158,11,.28); }
        .exec-brief-shell {
            position: relative;
            overflow: hidden;
            padding: 2rem 2.15rem;
            border-radius: 30px;
            border: 1px solid rgba(255,255,255,.14);
            background:
                radial-gradient(circle at 16% 0%, rgba(250,204,21,.17), transparent 24%),
                radial-gradient(circle at 88% 5%, rgba(124,58,237,.22), transparent 28%),
                linear-gradient(135deg, rgba(15,23,42,.92), rgba(30,27,75,.70));
            box-shadow: 0 28px 95px rgba(0,0,0,.38);
            margin-bottom: 1rem;
        }
        .exec-brief-shell:after {
            content:"";
            position:absolute;
            inset:0;
            pointer-events:none;
            background: linear-gradient(120deg, transparent 0%, rgba(255,255,255,.055) 45%, transparent 72%);
        }
        .exec-kicker {
            position: relative;
            color: #FACC15;
            text-transform: uppercase;
            letter-spacing: .18em;
            font-weight: 900;
            font-size: .74rem;
            margin-bottom: .7rem;
        }
        .exec-hero-line {
            position: relative;
            color: #FFFFFF;
            font-size: 1.85rem;
            line-height: 1.12;
            font-weight: 900;
            max-width: 980px;
        }
        .exec-subline {
            position: relative;
            margin-top: .8rem;
            color: #CBD5E1;
            font-size: .98rem;
            max-width: 760px;
            line-height: 1.45;
        }
        .exec-stat {
            padding: 1rem 1.05rem;
            border-radius: 22px;
            background: rgba(15,23,42,.62);
            border: 1px solid rgba(255,255,255,.10);
            box-shadow: 0 16px 40px rgba(0,0,0,.20);
            margin-bottom: 1rem;
        }
        .exec-stat.positive { border-color: rgba(34,197,94,.24); background: linear-gradient(180deg, rgba(22,163,74,.14), rgba(15,23,42,.62)); }
        .exec-stat.negative { border-color: rgba(248,113,113,.24); background: linear-gradient(180deg, rgba(239,68,68,.12), rgba(15,23,42,.62)); }
        .exec-stat.neutral { border-color: rgba(148,163,184,.20); }
        .exec-stat-label { color:#94A3B8; font-size:.76rem; font-weight:800; letter-spacing:.06em; text-transform:uppercase; }
        .exec-stat-value { color:#FFFFFF; font-size:1.55rem; font-weight:900; line-height:1.05; margin-top:.45rem; }
        .exec-stat-caption { color:#94A3B8; font-size:.78rem; margin-top:.35rem; }
        .exec-section-label {
            color:#FFFFFF;
            font-size:1.12rem;
            font-weight:900;
            margin: .75rem 0 .75rem;
            letter-spacing: -.01em;
        }
        .exec-accordion-shell {
            display: flex;
            flex-direction: column;
            gap: .72rem;
            margin: .4rem 0 1rem;
        }
        .exec-answer-strip {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            padding: .35rem .15rem .25rem;
        }
        .exec-strip-number {
            flex: 0 0 auto;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 2.45rem;
            height: 2.45rem;
            border-radius: 999px;
            color: #111827;
            background: linear-gradient(135deg, #FACC15, #F59E0B);
            font-size: .86rem;
            font-weight: 950;
            box-shadow: 0 12px 30px rgba(250,204,21,.20);
        }
        .exec-strip-content { flex: 1; min-width: 0; }
        .exec-strip-title { color:#FFFFFF; font-weight:950; font-size:1.05rem; letter-spacing:-.01em; }
        .exec-card-caption { color:#94A3B8; font-size:.82rem; margin:.38rem 0 .75rem; line-height:1.4; }
        .exec-card-body { display:flex; flex-direction:column; gap:.55rem; }
        .exec-answer-details {
            border: 1px solid rgba(255,255,255,.12);
            border-radius: 22px;
            background: linear-gradient(135deg, rgba(15,23,42,.78), rgba(30,27,75,.38));
            box-shadow: 0 18px 54px rgba(0,0,0,.24);
            overflow: hidden;
            margin-bottom: .72rem;
        }
        .exec-answer-details summary {
            min-height: 4.15rem;
            padding: 1.05rem 1.2rem;
            color: #FFFFFF;
            font-weight: 900;
            letter-spacing: -.01em;
            cursor: pointer;
            list-style: none;
            display: flex;
            align-items: center;
            gap: .9rem;
            background:
                radial-gradient(circle at 7% 50%, rgba(250,204,21,.13), transparent 22%),
                linear-gradient(90deg, rgba(255,255,255,.055), rgba(255,255,255,.018));
        }
        .exec-answer-details summary::-webkit-details-marker { display: none; }
        .exec-answer-details summary:hover {
            background:
                radial-gradient(circle at 7% 50%, rgba(250,204,21,.20), transparent 24%),
                linear-gradient(90deg, rgba(255,255,255,.075), rgba(255,255,255,.025));
        }
        .exec-summary-number {
            flex: 0 0 auto;
            display: inline-flex; align-items:center; justify-content:center;
            width: 2rem; height: 2rem; border-radius:999px;
            color:#111827; background: linear-gradient(135deg, #FACC15, #F59E0B);
            font-size:.78rem; font-weight:950;
            box-shadow: 0 10px 26px rgba(250,204,21,.18);
        }
        .exec-summary-title { flex: 1; min-width: 0; font-size: 1rem; }
        .exec-summary-hint {
            color:#94A3B8;
            font-size:.72rem;
            font-weight:800;
            text-transform:uppercase;
            letter-spacing:.08em;
        }
        .exec-answer-details[open] .exec-summary-hint { color:#FACC15; }
        .exec-answer-details[open] summary { border-bottom: 1px solid rgba(255,255,255,.09); }
        .exec-answer-details .exec-answer-strip { padding: 1rem 1.15rem 1.15rem; }
        .exec-bullet {
            position: relative;
            padding: .78rem .85rem .78rem 1rem;
            border-radius: 16px;
            color:#E2E8F0;
            background: rgba(255,255,255,.045);
            border: 1px solid rgba(255,255,255,.07);
            line-height: 1.42;
            font-size: .9rem;
        }
        .exec-bullet:before {
            content:"";
            display:inline-block;
            width:.42rem; height:.42rem;
            border-radius:999px;
            background:#FACC15;
            margin-right:.55rem;
            transform: translateY(-.08rem);
            box-shadow: 0 0 18px rgba(250,204,21,.42);
        }
        .exec-empty { color:#94A3B8; font-size:.88rem; padding:.8rem; border:1px dashed rgba(255,255,255,.12); border-radius:16px; }
        .exec-focus-panel {
            padding: 1.35rem 1.35rem;
            border-radius: 26px;
            border: 1px solid rgba(250,204,21,.18);
            background: linear-gradient(135deg, rgba(250,204,21,.10), rgba(15,23,42,.72));
            box-shadow: 0 22px 62px rgba(0,0,0,.24);
            margin-top: .3rem;
            margin-bottom: 1rem;
        }
        .exec-focus-panel.secondary {
            border-color: rgba(14,165,233,.20);
            background: linear-gradient(135deg, rgba(14,165,233,.11), rgba(15,23,42,.72));
        }
        .exec-panel-title { color:#FFFFFF; font-size:1rem; font-weight:900; margin-bottom:.75rem; }
        .exec-panel-copy { display:flex; flex-direction:column; gap:.58rem; }

        @media (max-width: 900px) {
            .hero h1 { font-size: 2.2rem; }
            .snapshot-grid, .executive-grid { grid-template-columns: 1fr; }
            .exec-answer-strip { gap: .75rem; }
            .exec-strip-number { width: 2.05rem; height: 2.05rem; font-size: .76rem; }
            .exec-hero-line { font-size: 1.45rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
