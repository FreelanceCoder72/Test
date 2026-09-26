"""
DineIQ Analytics – Premium Home Page
Totally redesigned UI with glassmorphism, animations, and modern aesthetics
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DineIQ",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from analytics.data_loader import data_available, load_orders, load_menu_items, load_customers, load_restaurants, load_order_items
from utils.ui_helpers import inject_global_styles, inject_fa, sidebar_nav, COLORS, CHART_TEMPLATE
from config.settings import DATA_DIR, PROCESSED_DIR

# ── Inject Premium Styles ───────────────────────────────────────────────────
inject_fa()
inject_global_styles()
sidebar_nav()

# ── Custom CSS for Home Page ─────────────────────────────────────────────────
st.markdown("""
<style>
/* Home specific */
.dineiq-stat-card {
    background: linear-gradient(135deg, rgba(25, 34, 53, 0.75) 0%, rgba(15, 22, 36, 0.85) 100%);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.25rem 1.4rem;
    margin-bottom: 1rem;
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
    position: relative;
    overflow: hidden;
    animation: dineiqFadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.dineiq-stat-card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5), 0 0 22px rgba(255, 107, 53, 0.25);
    border-color: rgba(255, 107, 53, 0.45);
}
.dineiq-feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 1.1rem;
    margin-top: 1rem;
}
.dineiq-pipeline-card {
    background: linear-gradient(135deg, rgba(21,26,45,0.85) 0%, rgba(15,18,32,0.9) 100%);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 8px 28px rgba(0,0,0,0.3);
    animation: dineiqFadeInUp 0.6s ease both;
    position: relative;
    overflow: hidden;
}
.dineiq-pipeline-card::before {
    content: '';
    position: absolute;
    top:0; left:0; right:0; height:2px;
    background: linear-gradient(90deg, #FF6B35, #00F2FE);
    opacity:0.8;
}
</style>
""", unsafe_allow_html=True)

# ── Hero Section ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="dineiq-hero">
    <div class="dineiq-hero-orb dineiq-hero-orb-1"></div>
    <div class="dineiq-hero-orb dineiq-hero-orb-2"></div>
    <div class="dineiq-hero-orb dineiq-hero-orb-3"></div>
    <div style="position: relative; z-index: 2; text-align: center;">
        <div style="
            width: 84px; height: 84px; margin: 0 auto 1.3rem;
            border-radius: 22px;
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.3), rgba(233, 69, 96, 0.4));
            border: 1px solid rgba(255, 107, 53, 0.6);
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 12px 35px rgba(255, 107, 53, 0.4), 0 0 25px rgba(233, 69, 96, 0.3);
            animation: dineiqFloat 4s ease-in-out infinite;
        ">
            <i class="fa-solid fa-utensils" style="font-size: 2.5rem; color: #FFFFFF;"></i>
        </div>
        <div style="
            display: inline-flex; align-items: center; gap: 0.6rem;
            background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 6px 18px; border-radius: 30px; margin-bottom: 1rem;
            backdrop-filter: blur(10px);
        ">
            <span style="
                display: inline-block; width: 8px; height: 8px;
                border-radius: 50%; background: #06D6A0;
                animation: livePulseDot 2s infinite;
            "></span>
            <span style="color: #06D6A0; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;">
                Enterprise Dining Intelligence Platform • Data Science Arena
            </span>
        </div>
        <h1 style="
            color: #FFFFFF; margin: 0; font-size: 3.6rem; font-weight: 900;
            letter-spacing: -0.04em; line-height: 1.1;
            font-family: 'Outfit', sans-serif;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        ">
            Dine<span style="background: linear-gradient(135deg, #FF6B35, #E94560); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">IQ</span> Analytics
        </h1>
        <p style="
            color: rgba(255, 255, 255, 0.82); font-size: 1.18rem; margin: 0.8rem auto 1.5rem;
            max-width: 780px; font-weight: 400; line-height: 1.6;
        ">
            End-to-End Predictive Analytics, Menu Optimization, Churn Forecasting & Dual-Pipeline Distributed Machine Learning.
            <br><span style="color: rgba(255,255,255,0.5); font-size:0.95rem;">Crafted with premium glassmorphism & motion design • 12 AI modules • Real-time telemetry</span>
        </p>
        <div style="display: flex; justify-content: center; gap: 0.8rem; flex-wrap: wrap;">
            <span style="background: rgba(255, 107, 53, 0.15); border: 1px solid rgba(255, 107, 53, 0.35); color: #FF8C42; font-size: 0.75rem; font-weight: 700; padding: 5px 14px; border-radius: 20px; letter-spacing: 0.05em;">
                <i class="fa-solid fa-bolt" style="margin-right: 4px;"></i> APACHE SPARK
            </span>
            <span style="background: rgba(0, 242, 254, 0.15); border: 1px solid rgba(0, 242, 254, 0.35); color: #00F2FE; font-size: 0.75rem; font-weight: 700; padding: 5px 14px; border-radius: 20px; letter-spacing: 0.05em;">
                <i class="fa-solid fa-brain" style="margin-right: 4px;"></i> ML PIPELINES
            </span>
            <span style="background: rgba(6, 214, 160, 0.15); border: 1px solid rgba(6, 214, 160, 0.35); color: #06D6A0; font-size: 0.75rem; font-weight: 700; padding: 5px 14px; border-radius: 20px; letter-spacing: 0.05em;">
                <i class="fa-solid fa-chart-line" style="margin-right: 4px;"></i> PREDICTIVE ANALYTICS
            </span>
            <span style="background: rgba(255, 209, 102, 0.15); border: 1px solid rgba(255, 209, 102, 0.35); color: #FFD166; font-size: 0.75rem; font-weight: 700; padding: 5px 14px; border-radius: 20px; letter-spacing: 0.05em;">
                <i class="fa-solid fa-cubes" style="margin-right: 4px;"></i> 548K+ RECORDS
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Live Status Banner ────────────────────────────────────────────────────────
if data_available():
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(6, 214, 160, 0.12) 0%, rgba(19, 26, 42, 0.85) 100%);
        border: 1px solid rgba(6, 214, 160, 0.35);
        border-left: 4px solid #06D6A0;
        border-radius: 16px;
        padding: 1rem 1.5rem;
        margin-bottom: 1.8rem;
        color: #06D6A0;
        font-weight: 600;
        display: flex; align-items: center; justify-content: space-between;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25), 0 0 20px rgba(6, 214, 160, 0.12);
        animation: dineiqFadeInUp 0.5s ease both;
        backdrop-filter: blur(12px);
    ">
        <div style="display: flex; align-items: center; gap: 0.8rem;">
            <div style="width:36px; height:36px; border-radius:10px; background:rgba(6,214,160,0.15); border:1px solid rgba(6,214,160,0.3); display:flex; align-items:center; justify-content:center;">
                <i class="fa-solid fa-circle-check" style="font-size: 1.1rem;"></i>
            </div>
            <div>
                <div style="color:#FFFFFF; font-weight:700; font-size:0.95rem; font-family:'Outfit', sans-serif;">Enterprise Dataset Connected &bull; All 12 AI Analytics Modules Active</div>
                <div style="color:rgba(255,255,255,0.6); font-size:0.8rem; font-weight:400;">Live cluster synced • Real-time telemetry • Ready for deep analysis</div>
            </div>
        </div>
        <span style="
            background: rgba(6, 214, 160, 0.2); border: 1px solid rgba(6, 214, 160, 0.5);
            padding: 5px 14px; border-radius: 20px; font-size: 0.78rem; font-weight: 800; letter-spacing: 0.06em;
            color:#06D6A0; display:flex; align-items:center; gap:6px;
        ">
            <span style="width:6px; height:6px; background:#06D6A0; border-radius:50%; animation: livePulseDot 2s infinite; display:inline-block;"></span>
            LIVE CLUSTER
        </span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(255,209,102,0.12) 0%, rgba(19, 26, 42, 0.85) 100%);
        border: 1px solid rgba(255,209,102,0.35); border-left: 4px solid #FFD166;
        border-radius: 16px; padding: 1rem 1.5rem; margin-bottom: 1.8rem;
        backdrop-filter: blur(12px); animation: dineiqFadeInUp 0.5s ease both;
        box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    ">
        <div style="display:flex; align-items:center; gap:0.8rem;">
            <div style="width:36px; height:36px; border-radius:10px; background:rgba(255,209,102,0.15); border:1px solid rgba(255,209,102,0.3); display:flex; align-items:center; justify-content:center;">
                <i class="fa-solid fa-triangle-exclamation" style="color:#FFD166;"></i>
            </div>
            <div>
                <div style="color:#FFFFFF; font-weight:700; font-size:0.95rem; font-family:'Outfit', sans-serif;">Dataset Not Found • Generate to Unlock All Modules</div>
                <div style="color:rgba(255,255,255,0.6); font-size:0.8rem;">Click "Initialize & Generate Dataset" in sidebar to create 548K+ realistic records</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── KPIs ──────────────────────────────────────────────────────────────────────
def kpi(label, value, color, icon, delay=0):
    st.markdown(f"""
    <div class="dineiq-stat-card" style="animation-delay: {delay}s; border-top: 2px solid {color}66;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.8rem;">
            <div style="width:40px; height:40px; background:{color}18; border:1px solid {color}35; border-radius:12px; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 15px {color}25;">
                <i class="fa-solid {icon}" style="color:{color}; font-size:1rem;"></i>
            </div>
            <div style="width:7px; height:7px; background:{color}; border-radius:50%; box-shadow:0 0 10px {color}; animation: livePulseDot 2s infinite;"></div>
        </div>
        <div style="color:rgba(255,255,255,0.55); font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:3px; font-family:'Space Grotesk', sans-serif;">{label}</div>
        <div style="color:#FFFFFF; font-size:1.5rem; font-weight:800; font-family:'Outfit', sans-serif; letter-spacing:-0.02em;">{value}</div>
    </div>
    """, unsafe_allow_html=True)

if data_available():
    try:
        orders = load_orders()
        oi = load_order_items()
        customers = load_customers()
        items = load_menu_items()
        total_rev = oi["total_price"].sum() if not oi.empty else 0
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1: kpi("Total Orders", f"{len(orders):,}", "#FF6B35", "fa-receipt", 0.1)
        with c2: kpi("Order Lines", f"{len(oi):,}", "#00F2FE", "fa-list-check", 0.18)
        with c3: kpi("Customers", f"{len(customers):,}", "#06D6A0", "fa-users", 0.26)
        with c4: kpi("Menu Items", f"{len(items):,}", "#FFD166", "fa-bowl-food", 0.34)
        with c5: kpi("Total Revenue", f"${total_rev/1000:.1f}K", "#E94560", "fa-dollar-sign", 0.42)
    except Exception as e:
        st.caption(f"KPI load error: {e}")
else:
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: kpi("Total Orders", "—", "#FF6B35", "fa-receipt", 0.1)
    with c2: kpi("Order Lines", "—", "#00F2FE", "fa-list-check", 0.18)
    with c3: kpi("Customers", "—", "#06D6A0", "fa-users", 0.26)
    with c4: kpi("Menu Items", "—", "#FFD166", "fa-bowl-food", 0.34)
    with c5: kpi("Total Revenue", "—", "#E94560", "fa-dollar-sign", 0.42)

# ── Main Layout: Nav Cards + Pipeline ────────────────────────────────────────
col_main, col_side = st.columns([2.2, 1])

with col_main:
    st.markdown("""
    <div style="margin: 1.5rem 0 0.8rem 0;">
        <div style="display:flex; align-items:center; gap:0.8rem;">
            <div style="width:4px; height:22px; border-radius:2px; background: linear-gradient(180deg, #FF6B35, #00F2FE); box-shadow:0 0 10px rgba(255,107,53,0.5);"></div>
            <h3 style="color:#FFFFFF; font-family:'Outfit', sans-serif; font-weight:800; font-size:1.4rem; margin:0; letter-spacing:-0.02em;">Intelligence Modules</h3>
            <span style="background:rgba(255,107,53,0.15); border:1px solid rgba(255,107,53,0.3); color:#FF8C42; font-size:0.68rem; font-weight:700; padding:3px 10px; border-radius:20px; letter-spacing:0.06em;">12 ACTIVE</span>
        </div>
        <div style="width:40px; height:3px; background: linear-gradient(90deg, #FF6B35, #00F2FE); border-radius:2px; margin-top:0.6rem;"></div>
        <div style="color:rgba(255,255,255,0.5); font-size:0.85rem; margin-top:0.4rem;">Select any module from sidebar to dive deep • Each card is interactive with live data</div>
    </div>
    """, unsafe_allow_html=True)

    modules = [
        ("fa-trophy", "Executive Dashboard", "Revenue, profit, AOV, channel mix & executive KPIs with heatmaps", "#FF6B35", 1, "Revenue • Profit • Orders"),
        ("fa-utensils", "Menu Intelligence", "Multi-dimensional classification: Profit Drivers, Hidden Opportunities", "#06D6A0", 2, "155 items • 4 classes"),
        ("fa-users", "Customer Intelligence", "RFM analysis, KMeans segmentation & churn risk detection", "#00F2FE", 3, "5 segments • Churn ML"),
        ("fa-recycle", "Wastage Dashboard", "Food wastage cost, risk prediction & location-wise analysis", "#E94560", 4, "Wastage ML • Cost Impact"),
        ("fa-chart-line", "Forecast Dashboard", "Time-series demand forecasting with Ridge & confidence bands", "#FFD166", 5, "30-90d Forecast • MAE/RMSE"),
        ("fa-code-branch", "Dual Pipeline", "Spark MLlib vs Python Scikit-learn independent verification", "#118AB2", 6, "Agreement Rate • Confusion Matrix"),
        ("fa-cart-shopping", "Market Basket", "Association rules, lift, confidence & bundle recommendations", "#FF6B35", 7, "Apriori • Bundles"),
        ("fa-location-dot", "Location Intelligence", "Restaurant performance by city, area & capacity analysis", "#06D6A0", 8, "20 Locations • Geo"),
        ("fa-lightbulb", "Recommendations", "AI-driven menu, pricing & operational recommendations", "#00F2FE", 9, "Actionable Insights"),
        ("fa-flask", "What-If Analysis", "Simulate pricing, demand & promotion changes with waterfall", "#FFD166", 10, "Scenario Modeling"),
        ("fa-triangle-exclamation", "Anomaly Detection", "Sales spikes, rating anomalies & duplicate transactions", "#E94560", 11, "Z-Score • IQR"),
        ("fa-tags", "Promotions & Pricing", "Promotion effectiveness, elasticity & pricing history", "#118AB2", 12, "15 Promos • Elasticity"),
    ]

    # Render in 2 columns grid
    for i in range(0, len(modules), 2):
        c1, c2 = st.columns(2)
        for col, mod in zip([c1, c2], modules[i:i+2]):
            with col:
                icon, title, desc, accent, num, stats = mod
                st.markdown(f"""
                <div class="dineiq-nav-card" style="--card-accent:{accent}; border-top: 2px solid {accent}55; animation-delay:{num*0.07}s;">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.7rem;">
                        <div style="display:flex; align-items:center; gap:0.85rem;">
                            <div style="width:42px; height:42px; background:{accent}18; border:1px solid {accent}40; border-radius:12px; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 15px {accent}25; flex-shrink:0;">
                                <i class="fa-solid {icon}" style="color:{accent}; font-size:1.1rem;"></i>
                            </div>
                            <div>
                                <div style="font-size:1.02rem; font-weight:800; color:#FFFFFF; font-family:'Outfit', sans-serif; line-height:1.2;">{title}</div>
                                <div style="font-size:0.70rem; color:{accent}; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; margin-top:2px;">Module {num:02d} • Ready</div>
                            </div>
                        </div>
                        <div style="width:28px; height:28px; border-radius:50%; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.08); display:flex; align-items:center; justify-content:center;">
                            <i class="fa-solid fa-arrow-right" style="color:rgba(255,255,255,0.4); font-size:0.7rem;"></i>
                        </div>
                    </div>
                    <div style="font-size:0.84rem; color:rgba(255,255,255,0.6); line-height:1.5; min-height:2.6rem;">{desc}</div>
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-top:0.9rem; padding-top:0.7rem; border-top:1px solid rgba(255,255,255,0.06);">
                        <span style="font-size:0.70rem; color:{accent}; font-weight:600; background:{accent}15; border:1px solid {accent}30; padding:3px 10px; border-radius:20px;">{stats}</span>
                        <span style="font-size:0.70rem; color:rgba(255,255,255,0.35);">Select in sidebar →</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

with col_side:
    st.markdown("""
    <div style="margin: 1.5rem 0 0.8rem 0;">
        <div style="display:flex; align-items:center; gap:0.8rem;">
            <div style="width:4px; height:22px; border-radius:2px; background: linear-gradient(180deg, #00F2FE, #06D6A0); box-shadow:0 0 10px rgba(0,242,254,0.5);"></div>
            <h3 style="color:#FFFFFF; font-family:'Outfit', sans-serif; font-weight:800; font-size:1.25rem; margin:0;">Platform Pipelines</h3>
        </div>
        <div style="width:40px; height:3px; background: linear-gradient(90deg, #00F2FE, #06D6A0); border-radius:2px; margin-top:0.6rem;"></div>
    </div>
    """, unsafe_allow_html=True)

    # Pipeline Cards
    st.markdown("""
    <div class="dineiq-pipeline-card" style="animation-delay:0.2s;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.9rem;">
            <div style="width:36px; height:36px; border-radius:11px; background:rgba(255,107,53,0.15); border:1px solid rgba(255,107,53,0.35); display:flex; align-items:center; justify-content:center;">
                <i class="fa-solid fa-bolt" style="color:#FF6B35;"></i>
            </div>
            <span style="color:#FFFFFF; font-weight:800; font-size:1rem; font-family:'Outfit', sans-serif;">Big Data Engine</span>
        </div>
        <ul style="margin:0; padding-left:0; list-style:none; color:rgba(255,255,255,0.65); font-size:0.85rem; line-height:1.8;">
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>Apache Spark Quality Checks</li>
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>Distributed Processing (Sim)</li>
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>548K+ Records Validation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dineiq-pipeline-card" style="animation-delay:0.3s;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.9rem;">
            <div style="width:36px; height:36px; border-radius:11px; background:rgba(0,242,254,0.15); border:1px solid rgba(0,242,254,0.35); display:flex; align-items:center; justify-content:center;">
                <i class="fa-solid fa-brain" style="color:#00F2FE;"></i>
            </div>
            <span style="color:#FFFFFF; font-weight:800; font-size:1rem; font-family:'Outfit', sans-serif;">Machine Learning</span>
        </div>
        <ul style="margin:0; padding-left:0; list-style:none; color:rgba(255,255,255,0.65); font-size:0.85rem; line-height:1.8;">
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>Menu Performance Classifier</li>
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>Random Forest (100 trees)</li>
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>Wastage Risk Prediction</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dineiq-pipeline-card" style="animation-delay:0.4s;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.9rem;">
            <div style="width:36px; height:36px; border-radius:11px; background:rgba(6,214,160,0.15); border:1px solid rgba(6,214,160,0.35); display:flex; align-items:center; justify-content:center;">
                <i class="fa-solid fa-server" style="color:#06D6A0;"></i>
            </div>
            <span style="color:#FFFFFF; font-weight:800; font-size:1rem; font-family:'Outfit', sans-serif;">Analytical Core</span>
        </div>
        <ul style="margin:0; padding-left:0; list-style:none; color:rgba(255,255,255,0.65); font-size:0.85rem; line-height:1.8;">
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>12 Specialized Modules</li>
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>RFM + KMeans Clustering</li>
            <li><i class="fa-solid fa-check" style="color:#06D6A0; margin-right:8px; font-size:0.75rem;"></i>Market Basket + Forecasting</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Telemetry
    st.markdown("""
    <div style="height:1px; width:100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); margin:1.4rem 0;"></div>
    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.9rem;">
        <span style="width:7px; height:7px; border-radius:50%; background:#06D6A0; animation: livePulseDot 2s infinite; display:inline-block;"></span>
        <span style="color:#FFFFFF; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; font-family:'Space Grotesk', sans-serif;">Live Telemetry</span>
    </div>
    """, unsafe_allow_html=True)

    if data_available():
        try:
            cust = load_customers()
            items = load_menu_items()
            rests = load_restaurants()
            st.markdown(f"""
            <div style="background:rgba(21,26,45,0.6); border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:1rem 1.2rem; backdrop-filter:blur(10px);">
                <div style="display:flex; justify-content:space-between; margin-bottom:0.7rem;">
                    <span style="color:rgba(255,255,255,0.5); font-size:0.8rem;">Customer Base</span>
                    <span style="color:#FFFFFF; font-weight:700; font-size:0.85rem;">{len(cust):,} users</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:0.7rem;">
                    <span style="color:rgba(255,255,255,0.5); font-size:0.8rem;">Menu Catalog</span>
                    <span style="color:#FFFFFF; font-weight:700; font-size:0.85rem;">{len(items)} items</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:rgba(255,255,255,0.5); font-size:0.8rem;">Store Branches</span>
                    <span style="color:#FFFFFF; font-weight:700; font-size:0.85rem;">{len(rests)} locations</span>
                </div>
                <div style="margin-top:0.9rem; padding-top:0.8rem; border-top:1px solid rgba(255,255,255,0.06);">
                    <div style="display:flex; align-items:center; gap:6px; color:#06D6A0; font-size:0.75rem; font-weight:600;">
                        <i class="fa-solid fa-signal"></i> All systems operational
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.caption("Telemetry loading...")
    else:
        st.markdown("""
        <div style="background:rgba(21,26,45,0.6); border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:1rem 1.2rem; text-align:center;">
            <i class="fa-solid fa-satellite-dish" style="color:rgba(255,255,255,0.3); font-size:1.5rem; margin-bottom:0.6rem;"></i>
            <div style="color:rgba(255,255,255,0.5); font-size:0.85rem;">Telemetry offline: no dataset loaded</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="height:1px; width:100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); margin:1.4rem 0;"></div>
    <div style="text-align:center; color:rgba(255,255,255,0.4); font-size:0.72rem; line-height:1.5;">
        DineIQ Analytics v3.0 Premium<br>
        <span style="color:rgba(255,255,255,0.25);">Data Science Intelligence Arena • Redesigned UI</span><br>
        <div style="margin-top:0.6rem; display:flex; justify-content:center; gap:0.8rem;">
            <i class="fa-solid fa-sparkles" style="color:#FF6B35;"></i>
            <span style="color:#FF8C42; font-weight:600;">Glassmorphism • Animations • Modern</span>
            <i class="fa-solid fa-sparkles" style="color:#00F2FE;"></i>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:1rem 0 1.2rem 0; border-bottom:1px solid rgba(255,255,255,0.06); margin-bottom:1rem;">
        <div style="width:56px; height:56px; margin:0 auto 0.8rem; border-radius:16px; background: linear-gradient(135deg, rgba(255,107,53,0.25), rgba(233,69,96,0.35)); border:1px solid rgba(255,107,53,0.5); display:flex; align-items:center; justify-content:center; box-shadow:0 8px 20px rgba(255,107,53,0.3);">
            <i class="fa-solid fa-utensils" style="font-size:1.5rem; color:#FFFFFF;"></i>
        </div>
        <div style="color:#FFFFFF; font-weight:800; font-size:1.15rem; font-family:'Outfit', sans-serif; letter-spacing:-0.02em;">DineIQ Analytics</div>
        <div style="color:rgba(255,255,255,0.5); font-size:0.72rem; font-weight:600; letter-spacing:0.08em; text-transform:uppercase; margin-top:2px;">Enterprise Platform</div>
        <div style="margin-top:0.6rem; display:inline-flex; align-items:center; gap:5px; background:rgba(6,214,160,0.12); border:1px solid rgba(6,214,160,0.25); padding:3px 10px; border-radius:20px; color:#06D6A0; font-size:0.68rem; font-weight:700;">
            <span style="width:5px; height:5px; background:#06D6A0; border-radius:50%; animation: livePulseDot 2s infinite; display:inline-block;"></span>
            v3.0 Premium UI
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🛠️ Platform Controls")

    # Generate Dataset
    if st.button("🚀 Initialize & Generate Dataset", use_container_width=True, type="primary"):
        with st.spinner("Generating 548K+ realistic records..."):
            try:
                from data_generator.generate_dataset import main as gen_main
                import io, contextlib
                f = io.StringIO()
                with contextlib.redirect_stdout(f):
                    gen_main()
                st.success("✅ Dataset generated successfully!")
                st.code(f.getvalue()[-1000:], language="bash")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
                st.caption("Run: `python data_generator/generate_dataset.py`")

    st.caption("Generates ~548K+ realistic dining orders, inventory, customers, and ratings")

    # Train ML
    if st.button("🧠 Train ML Models", use_container_width=True):
        with st.spinner("Training scikit-learn models..."):
            try:
                from python_pipeline.ml_pipeline import train_menu_classifier
                result = train_menu_classifier()
                if result["status"] == "success":
                    st.success(f"✅ Models trained! Accuracy: {result['accuracy']}%")
                else:
                    st.error(f"Failed: {result['message']}")
            except Exception as e:
                st.error(f"Error: {e}")

    # Spark
    if st.button("⚡ Run Spark Engine", use_container_width=True):
        with st.spinner("Executing Spark jobs..."):
            try:
                from spark_pipeline.spark_jobs import run_spark_pipeline
                result = run_spark_pipeline()
                st.success("✅ Spark pipeline completed!")
                st.json(result.get("summary", {}))
            except Exception as e:
                st.error(f"Spark error: {e}")

    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    if data_available():
        try:
            orders = load_orders()
            st.metric("Orders", f"{len(orders):,}")
            if not orders.empty and "total_amount" in orders.columns:
                st.metric("Revenue", f"${orders['total_amount'].sum():,.0f}")
        except:
            st.caption("Stats unavailable")
    else:
        st.info("No dataset. Generate first.")

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; padding:0.8rem; background:rgba(255,107,53,0.08); border:1px solid rgba(255,107,53,0.15); border-radius:12px;">
        <div style="color:#FF8C42; font-weight:700; font-size:0.85rem; font-family:'Outfit', sans-serif;">💡 Premium UI Active</div>
        <div style="color:rgba(255,255,255,0.5); font-size:0.72rem; margin-top:3px;">Glassmorphism • Animations • Motion Design</div>
    </div>
    """, unsafe_allow_html=True)
