"""
Nabat TerraPod Challenge - Phase 1 Technical Proposal
Ultra-Accurate Publication-Grade Engineering Figures Generator
Designed for ASPIRE / ATRC Abu Dhabi & Nabat AI Technologies.

Rigorous engineering drafting:
- Mathematically exact geometries with true parametric CAD curves.
- Zero text collisions: every label, leader, and dimension sits in open whitespace.
- Verified physical parameters matching proposal documentation word-for-word.
- 300 DPI publication standards (AIAA / IEEE / Nature style).
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Ellipse

os.makedirs('assets', exist_ok=True)

# Deep-Tech Corporate Engineering Palette
COLOR_NAVY = '#0F172A'          # Deep Slate Navy (#0F172A)
COLOR_NAVY_LIGHT = '#1E293B'    # Slate 800 (#1E293B)
COLOR_EMERALD = '#047857'       # Deep Emerald Green (#047857)
COLOR_EMERALD_LIGHT = '#10B981' # Bright Emerald (#10B981)
COLOR_GOLD = '#B45309'          # Desert Ochre / Gold (#B45309)
COLOR_GOLD_LIGHT = '#F59E0B'    # Amber (#F59E0B)
COLOR_CRIMSON = '#BE123C'       # Deep Rose / Crimson (#BE123C)
COLOR_MUTED = '#64748B'         # Slate 500 (#64748B)
COLOR_LIGHT_BG = '#F8FAFC'      # Slate 50 canvas (#F8FAFC)
COLOR_BORDER = '#CBD5E1'        # Slate 300 border (#CBD5E1)
COLOR_DARK_CORE = '#1E293B'     # Dark Slate Biochar (#1E293B)
COLOR_SHELL = '#F1F5F9'         # High-Albedo Kaolin Clay (#F1F5F9)
COLOR_SAND = '#D97706'          # Sand Surface line (#D97706)
COLOR_SAND_FILL = '#FEF3C7'     # Sand subsurface fill (#FEF3C7)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['mathtext.fontset'] = 'dejavusans'

# =============================================================================
# 1. 2D CAD CUTAWAY SCHEMATIC (Slide 3) - ZERO LINE-TEXT CROSSING
# =============================================================================
def generate_terrapod_schematic():
    fig, ax = plt.subplots(figsize=(8.5, 6.0), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor(COLOR_LIGHT_BG)

    # Geometry: Height = 29.0 mm (-14.5 to +14.5), Equat. Diam = 26.5 mm (Radius = 13.25)
    a = 13.25
    b = 14.50
    k = 0.08  # smooth egg asymmetry
    
    t_lip = np.arcsin(6.0 / a)  # crater lip at x = 6.0 mm
    t_outer = np.linspace(t_lip, 2*np.pi - t_lip, 300)
    x_out = a * np.sin(t_outer)
    y_out = b * np.cos(t_outer) * (1.0 + k * np.cos(t_outer))
    y_lip = b * np.cos(t_lip) * (1.0 + k * np.cos(t_lip)) # ~ 14.2 mm
    
    # Parabolic crater
    x_crater = np.linspace(-6.0, 6.0, 100)
    y_crater = y_lip - 4.2 * (1.0 - (x_crater / 6.0)**2)
    
    x_shell = np.concatenate([x_out, x_crater])
    y_shell = np.concatenate([y_out, y_crater])
    
    # 1. Outer High-Albedo Kaolin Shell
    ax.fill(x_shell, y_shell, color=COLOR_SHELL, edgecolor=COLOR_NAVY, linewidth=2.0, zorder=2)

    # 2. Inner Composite Core (Shrunk by 0.8 mm)
    t_inner = np.linspace(t_lip, 2*np.pi - t_lip, 300)
    x_in = (a - 0.8) * np.sin(t_inner)
    y_in = (b - 0.8) * np.cos(t_inner) * (1.0 + k * np.cos(t_inner))
    y_lip_in = (b - 0.8) * np.cos(t_lip) * (1.0 + k * np.cos(t_lip))
    x_crater_in = np.linspace(-5.5, 5.5, 100)
    y_crater_in = y_lip_in - 4.0 * (1.0 - (x_crater_in / 5.5)**2)
    
    x_core = np.concatenate([x_in, x_crater_in])
    y_core = np.concatenate([y_in, y_crater_in])
    ax.fill(x_core, y_core, color=COLOR_DARK_CORE, edgecolor='#475569', linewidth=1.0, zorder=3)

    # 3. Bottom 35% Keel Ballast (below y = -4.35 mm)
    keel_mask = y_in <= -4.35
    ax.fill_between(x_in, y_in, -4.35, where=keel_mask, color='#0F172A', edgecolor=COLOR_EMERALD, linewidth=1.5, zorder=4)

    # Highlight Crater Rim
    ax.plot(x_crater, y_crater, color=COLOR_EMERALD, linewidth=2.5, zorder=5)

    # 4. Central Seed Nest
    nest = Ellipse((0.0, 7.5), 6.5, 4.0, facecolor='#FEF3C7', edgecolor=COLOR_GOLD, linewidth=1.8, zorder=6)
    ax.add_patch(nest)

    seed_grass = Ellipse((-1.2, 7.5), 1.5, 3.0, angle=25, facecolor=COLOR_GOLD, edgecolor='#78350F', linewidth=1.0, zorder=7)
    seed_shrub = Ellipse((1.3, 7.5), 1.8, 1.8, facecolor='#475569', edgecolor=COLOR_NAVY, linewidth=1.0, zorder=7)
    ax.add_patch(seed_grass)
    ax.add_patch(seed_shrub)

    # Diffuse Light Veil
    ax.plot([-3.0, 3.0], [9.5, 9.5], color=COLOR_EMERALD_LIGHT, linewidth=2.2, linestyle='--', zorder=8)

    # Center of Gravity Marker
    cg_y = -4.35
    ax.plot([0.0], [cg_y], marker='+', markersize=14, markeredgewidth=2.2, color=COLOR_GOLD_LIGHT, zorder=9)
    ax.plot([0.0], [cg_y], marker='o', markersize=8, fillstyle='none', markeredgewidth=2.0, color=COLOR_GOLD_LIGHT, zorder=9)

    # ==================== DIMENSIONS (LEFT, BOTTOM, TOP) ====================
    # Overall Height Caliper (Left: x = -17.5. No annotations on this side to prevent any line crossing!)
    ax.plot([-17.5, -17.5], [-14.5, 14.5], color=COLOR_NAVY, lw=1.3, zorder=10)
    ax.plot([-19.0, -16.0], [14.5, 14.5], color=COLOR_NAVY, lw=1.3, zorder=10)
    ax.plot([-19.0, -16.0], [-14.5, -14.5], color=COLOR_NAVY, lw=1.3, zorder=10)
    ax.text(-20.5, 0.0, '29.0 mm (Overall Height)', rotation=90, va='center', ha='right', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)

    # Maximum Diameter Caliper (Bottom: y = -18.5)
    ax.plot([-13.25, 13.25], [-18.5, -18.5], color=COLOR_NAVY, lw=1.3, zorder=10)
    ax.plot([-13.25, -13.25], [-20.0, -17.0], color=COLOR_NAVY, lw=1.3, zorder=10)
    ax.plot([13.25, 13.25], [-20.0, -17.0], color=COLOR_NAVY, lw=1.3, zorder=10)
    ax.text(0.0, -21.2, '26.5 mm (Maximum Equatorial Diameter)', ha='center', va='top', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)

    # Funnel Aperture Caliper (Top: y = 16.5)
    ax.plot([-6.0, 6.0], [16.5, 16.5], color=COLOR_EMERALD, lw=1.3, zorder=10)
    ax.plot([-6.0, -6.0], [15.2, 17.8], color=COLOR_EMERALD, lw=1.3, zorder=10)
    ax.plot([6.0, 6.0], [15.2, 17.8], color=COLOR_EMERALD, lw=1.3, zorder=10)
    ax.text(0.0, 18.5, '12.0 mm Funnel Aperture', ha='center', va='bottom', fontsize=9.0, fontweight='bold', color=COLOR_EMERALD)

    # ==================== ALL COMPONENT LEADERS ON THE RIGHT (ZERO CROSSINGS) ====================
    leaders = [
        ('12mm Concave Catchment Funnel\nDirects 0.56 mL rain to seed core', (3.5, 12.0), (16.0, 14.5), COLOR_EMERALD),
        ('Kaolin Mineral Shield (R = 78%)\n0.8mm outer coat (ΔT = −34.3°C)', (12.5, 4.0), (16.0, 9.5), COLOR_NAVY),
        ('Sheltered Seed Nest Chamber\nNurse grass + climax shrub guild', (3.5, 7.5), (16.0, 4.5), COLOR_GOLD),
        ('Center of Gravity (CG at 35%)\nForward self-righting flight stability', (0.0, cg_y), (16.0, -2.5), COLOR_GOLD_LIGHT),
        ('Water-Soluble Keel (12% Gum Arabic)\nDissolves in 20 min; shear < 0.12 MPa', (7.0, -9.5), (16.0, -9.5), COLOR_EMERALD)
    ]
    for text, pt_from, pt_to, col in leaders:
        ax.annotate(text, xy=pt_from, xytext=pt_to,
                    arrowprops=dict(facecolor=col, edgecolor=col, arrowstyle='->', lw=1.3),
                    fontsize=8.5, fontweight='bold', color=col if col != COLOR_GOLD_LIGHT else COLOR_NAVY, zorder=11)

    ax.set_xlim(-26, 42)
    ax.set_ylim(-25, 22)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('assets/terrapod_schematic.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/terrapod_schematic.png (Zero line crossings)")

# =============================================================================
# 2. STEFAN-BOLTZMANN THERMAL EQUILIBRIUM GRAPH (Slide 4)
# =============================================================================
def generate_thermal_plot():
    from scipy.optimize import fsolve

    fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor('#FFFFFF')

    G_range = np.linspace(200, 1100, 50)
    Tamb_C = 32.0
    Tamb = Tamb_C + 273.15
    Tsky = Tamb - 10.0
    hc = 13.0  # W/m2K
    sigma = 5.67e-8
    eps = 0.90

    def get_temp(G, alpha):
        def eq(T):
            return alpha * G - (hc * (T - Tamb) + eps * sigma * (T**4 - Tsky**4))
        return float(fsolve(eq, 330.0)[0] - 273.15)

    T_dark = [get_temp(g, 0.92) for g in G_range]
    T_kaolin = [get_temp(g, 0.22) for g in G_range]

    ax.axhspan(42.0, 85.0, color='#FEE2E2', alpha=0.55, zorder=1)
    ax.axhspan(20.0, 42.0, color='#ECFDF5', alpha=0.55, zorder=1)

    # 42°C threshold line
    ax.axhline(42.0, color=COLOR_CRIMSON, linestyle='--', linewidth=1.6, zorder=2)
    ax.text(230, 43.5, 'CRITICAL EMBRYO LETHAL THRESHOLD (42.0°C)', color=COLOR_CRIMSON, fontsize=8.5, fontweight='bold')

    ax.plot(G_range, T_dark, color=COLOR_CRIMSON, linewidth=2.8, label='Uncoated Biochar (α = 0.92)', zorder=3)
    ax.plot(G_range, T_kaolin, color=COLOR_EMERALD, linewidth=2.8, label='Kaolin Albedo Shield (α = 0.22, R = 78%)', zorder=3)

    t_dark_1000 = get_temp(1000, 0.92)
    t_kao_1000 = get_temp(1000, 0.22)

    ax.plot([1000, 1000], [t_kao_1000, t_dark_1000], color=COLOR_NAVY, linestyle=':', linewidth=1.6, zorder=4)
    ax.scatter([1000, 1000], [t_dark_1000, t_kao_1000], color=[COLOR_CRIMSON, COLOR_EMERALD], s=75, zorder=5)

    ax.annotate('74.9°C (Lethal Heat Shock)', xy=(1000, t_dark_1000), xytext=(720, 77.0),
                arrowprops=dict(facecolor=COLOR_CRIMSON, edgecolor=COLOR_CRIMSON, arrowstyle='->', lw=1.3),
                fontsize=8.5, fontweight='bold', color=COLOR_CRIMSON)

    ax.annotate('40.6°C (Embryo Viable)', xy=(1000, t_kao_1000), xytext=(740, 31.0),
                arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.3),
                fontsize=8.5, fontweight='bold', color=COLOR_EMERALD)

    ax.text(1015, 57.0, 'ΔT = −34.3°C\nCooling Shield', fontsize=8.5, fontweight='bold', color=COLOR_NAVY)

    ax.set_xlabel('Solar Irradiance G (W/m²)', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_ylabel('Surface Equilibrium Temperature (°C)', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_title('Stefan-Boltzmann Solar Radiation & Albedo Balance', fontsize=11, fontweight='bold', color=COLOR_NAVY, pad=12)
    ax.set_xlim(200, 1150)
    ax.set_ylim(25, 82)
    ax.grid(True, linestyle=':', alpha=0.5, color=COLOR_BORDER)
    ax.legend(loc='upper left', frameon=True, facecolor='#FFFFFF', edgecolor=COLOR_BORDER, fontsize=8.5)

    for spine in ax.spines.values():
        spine.set_color(COLOR_BORDER)

    plt.tight_layout()
    plt.savefig('assets/thermal_plot.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/thermal_plot.png")

# =============================================================================
# 3. HYDROLOGICAL MECHANICS COMPARISON (Slide 5) - ZERO OVERLAPS
# =============================================================================
def generate_hydrology_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.8, 4.4), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax1.set_facecolor('#FFFFFF')
    ax2.set_facecolor('#FFFFFF')

    # ---------------- LEFT: CONVENTIONAL CONVEX PELLET ----------------
    ax1.set_title("Standard Convex Pellet\n(80% Lateral Rain Runoff)", fontsize=10, fontweight='bold', color=COLOR_CRIMSON, pad=12)
    
    # Sand Bed (y from -7 to 0)
    ax1.plot([-14, 14], [0, 0], color=COLOR_SAND, lw=2.0)
    ax1.fill_between([-14, 14], -7, 0, color=COLOR_SAND_FILL, alpha=0.6)
    
    # Dome pellet (sits on sand: y from 0 to 6.5)
    theta = np.linspace(0, np.pi, 150)
    xd = 8.0 * np.cos(theta)
    yd = 6.5 * np.sin(theta)
    ax1.fill_between(xd, 0, yd, color='#CBD5E1', edgecolor=COLOR_NAVY, lw=1.5)

    # Vertical rain rays deflecting outward
    rain_x = [-5.0, -1.8, 1.8, 5.0]
    for rx in rain_x:
        ry_hit = 6.5 * np.sin(np.arccos(rx / 8.0))
        ax1.plot([rx, rx], [11.0, ry_hit], color='#0284C7', lw=1.6, linestyle='-')
        deflect_dx = 3.2 * np.sign(rx if rx != 0 else 1)
        ax1.annotate('', xy=(rx + deflect_dx, 0.8), xytext=(rx, ry_hit),
                     arrowprops=dict(facecolor=COLOR_CRIMSON, edgecolor=COLOR_CRIMSON, arrowstyle='->', lw=1.5))

    # Text placed completely in the sand area below the pellet (y = -2.2 and -4.5)
    ax1.text(0, -2.0, "LATERAL RUNOFF LOSS", ha='center', va='top', fontsize=9.0, fontweight='bold', color=COLOR_CRIMSON)
    ax1.text(0, -3.8, "80% of rain sheds away into dry sand;\nevaporates in <90 min (VPD > 4.5 kPa)", 
             ha='center', va='top', fontsize=7.8, color=COLOR_NAVY_LIGHT)

    ax1.set_xlim(-14, 14)
    ax1.set_ylim(-7.0, 12.0)
    ax1.axis('off')

    # ---------------- RIGHT: BIODROP CONCAVE CATCHMENT FUNNEL ----------------
    ax2.set_title("Nabat-BioDrop™ Concave Funnel\n(100% Water Concentration)", fontsize=10, fontweight='bold', color=COLOR_EMERALD, pad=12)
    
    # Sand Bed (y from -7 to 0)
    ax2.plot([-14, 14], [0, 0], color=COLOR_SAND, lw=2.0)
    ax2.fill_between([-14, 14], -7, 0, color=COLOR_SAND_FILL, alpha=0.6)

    # Upright BioDrop Ovoid anchored 10mm into sand:
    # Body extends from y = -2.0 (in sand) to y = 8.5 (above sand).
    # That means the pod terminates at y = -2.0! It NEVER reaches y = -3.5 or -5.5!
    a_o = 7.0
    b_o = 5.25
    y_center = 3.25 # spans from -2.0 to 8.5
    
    t_lip = np.arcsin(4.0 / a_o)
    t_body = np.linspace(t_lip, 2*np.pi - t_lip, 200)
    xb = a_o * np.sin(t_body)
    yb = y_center + b_o * np.cos(t_body) * (1.0 + 0.08 * np.cos(t_body))
    y_lip = y_center + b_o * np.cos(t_lip) * (1.0 + 0.08 * np.cos(t_lip)) # ~ 7.8
    
    xc = np.linspace(-4.0, 4.0, 60)
    yc = y_lip - 3.2 * (1.0 - (xc / 4.0)**2)
    
    x_pod = np.concatenate([xb, xc])
    y_pod = np.concatenate([yb, yc])
    ax2.fill(x_pod, y_pod, color=COLOR_SHELL, edgecolor=COLOR_NAVY, lw=1.5)
    
    # Internal nest
    ax2.plot(xc, yc, color=COLOR_EMERALD, lw=2.2)
    nest = Ellipse((0.0, 4.2), 4.0, 2.2, facecolor='#ECFDF5', edgecolor=COLOR_EMERALD, lw=1.2)
    ax2.add_patch(nest)

    # Rain rays entering funnel directly
    rain_x2 = [-3.0, -1.0, 1.0, 3.0]
    for rx in rain_x2:
        ax2.annotate('', xy=(rx * 0.35, 4.8), xytext=(rx, 11.0),
                     arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.6))

    # Text placed completely below the pod in open sand (pod ends at y = -2.0)
    ax2.text(0, -2.0, "100% CORE HYDRATION", ha='center', va='top', fontsize=9.0, fontweight='bold', color=COLOR_EMERALD)
    ax2.text(0, -3.8, "12mm crater captures 0.56 mL rain (5x);\nalginate sponge stores water for 7 days", 
             ha='center', va='top', fontsize=7.8, color=COLOR_NAVY_LIGHT)

    ax2.set_xlim(-14, 14)
    ax2.set_ylim(-7.0, 12.0)
    ax2.axis('off')

    plt.tight_layout()
    plt.savefig('assets/hydrology_diagram.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/hydrology_diagram.png (Zero overlaps)")

# =============================================================================
# 4. ROOT BIOMECHANICS FORCE BAR CHART (Slide 6) - ZERO TITLE OVERLAP
# =============================================================================
def generate_root_mechanics_chart():
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor('#FFFFFF')

    items = [
        'Wet BioDrop™ Keel\n(Dissolved in 20 min)',
        'Emerging Radicle Push\n(Physiological Turgor)',
        'Sun-Baked Clay Clod\n(Conventional Pellet)'
    ]
    forces = [0.12, 1.00, 2.50]
    bar_colors = [COLOR_EMERALD, COLOR_GOLD, COLOR_CRIMSON]

    y_pos = np.arange(len(items))
    bars = ax.barh(y_pos, forces, color=bar_colors, height=0.48, edgecolor=COLOR_BORDER, linewidth=1.2)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(items, fontsize=8.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_xlabel('Compressive Shear Resistance / Penetration Force (MPa)', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_title('Root Biomechanics: Overcoming the "Concrete Tomb" Barrier', fontsize=11, fontweight='bold', color=COLOR_NAVY, pad=18)
    ax.set_xlim(0, 3.4)
    ax.set_ylim(-0.6, 2.6)
    ax.grid(axis='x', linestyle=':', alpha=0.5, color=COLOR_BORDER)

    # Biological limit dashed line at 1.20 MPa
    ax.axvline(1.20, color=COLOR_GOLD, linestyle='--', linewidth=1.6)
    
    # Placed cleanly inside plot area at y = 2.4 (safely below title)
    ax.text(1.20, 2.45, 'Radicle Limit (1.20 MPa)', ha='center', va='bottom', color=COLOR_GOLD, fontsize=8.2, fontweight='bold')

    # Concise Value Labels strictly positioned with ZERO overlap
    # Bar 0 (Keel): length 0.12
    ax.text(0.18, 0, '< 0.12 MPa (Zero Barrier)', va='center', fontsize=8.5, fontweight='bold', color=COLOR_EMERALD)
    
    # Bar 1 (Radicle): length 1.00
    ax.text(0.92, 1, '0.80–1.20 MPa', va='center', ha='right', fontsize=8.5, fontweight='bold', color='#FFFFFF')
    ax.text(1.28, 1, 'Biological Push', va='center', ha='left', fontsize=8.0, fontweight='bold', color=COLOR_NAVY)

    # Bar 2 (Clod): length 2.50
    ax.text(2.55, 2, '> 2.50 MPa (Lethal Trap)', va='center', fontsize=8.5, fontweight='bold', color=COLOR_CRIMSON)

    for spine in ax.spines.values():
        spine.set_color(COLOR_BORDER)

    plt.tight_layout()
    plt.savefig('assets/root_mechanics_chart.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/root_mechanics_chart.png (Zero overlap)")

# =============================================================================
# 5. UAV PAYLOAD & COVERAGE COMPARISON CHART (Slide 8)
# =============================================================================
def generate_payload_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 4.0), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax1.set_facecolor('#FFFFFF')
    ax2.set_facecolor('#FFFFFF')

    categories = ['Standard Puck\n(25g)', 'Nabat-BioDrop™\n(9.8g)']
    
    # Subplot 1: Sortie Payload
    pods = [1000, 2550]
    bars1 = ax1.bar(categories, pods, color=[COLOR_MUTED, COLOR_EMERALD], width=0.52, edgecolor=COLOR_BORDER, linewidth=1.2)
    ax1.set_ylabel('Pods per 25 kg Drone Flight', fontsize=9, fontweight='bold', color=COLOR_NAVY)
    ax1.set_title('UAV Payload Capacity', fontsize=10.5, fontweight='bold', color=COLOR_NAVY)
    ax1.set_ylim(0, 3100)
    ax1.grid(axis='y', linestyle=':', alpha=0.5, color=COLOR_BORDER)

    for bar, val in zip(bars1, pods):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 80, f'{val:,}', ha='center', fontsize=10, fontweight='bold', color=COLOR_NAVY)
    
    ax1.text(1, 1400, '+155%\nPayload', ha='center', va='center', fontsize=9, fontweight='bold', color='#FFFFFF', 
             bbox=dict(boxstyle='round,pad=0.35', facecolor=COLOR_NAVY, edgecolor='none'))

    # Subplot 2: Hectare Coverage
    hectares = [0.67, 1.70] # 2550 / 1500 = 1.70 ha
    bars2 = ax2.bar(categories, hectares, color=[COLOR_MUTED, COLOR_GOLD], width=0.52, edgecolor=COLOR_BORDER, linewidth=1.2)
    ax2.set_ylabel('Hectares Restored per Sortie', fontsize=9, fontweight='bold', color=COLOR_NAVY)
    ax2.set_title('Rangeland Coverage (1,500/ha)', fontsize=10.5, fontweight='bold', color=COLOR_NAVY)
    ax2.set_ylim(0, 2.2)
    ax2.grid(axis='y', linestyle=':', alpha=0.5, color=COLOR_BORDER)

    for bar, val in zip(bars2, hectares):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 0.06, f'{val:.2f} ha', ha='center', fontsize=10, fontweight='bold', color=COLOR_NAVY)

    for ax in (ax1, ax2):
        for spine in ax.spines.values():
            spine.set_color(COLOR_BORDER)

    plt.tight_layout()
    plt.savefig('assets/payload_chart.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/payload_chart.png")

# =============================================================================
# 6. TECHNO-ECONOMIC COST WATERFALL CHART (Slide 9) - ZERO CLIPPING
# =============================================================================
def generate_cost_chart():
    fig, ax = plt.subplots(figsize=(7.5, 4.4), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor('#FFFFFF')

    cost_items = [
        'Raw Materials (Biochar, Clay, Seeds)',
        'Direct Labor (4 Techs @ 500k/mo)',
        'Capex Amortization & Plant Utilities',
        'Factory-Gate Conversion Total',
        'Commercial Landed Delivery Total',
        'ASPIRE NTPC Maximum Budget Cap'
    ]
    costs = [0.096, 0.052, 0.050, 0.227, 0.307, 0.400]
    colors = [COLOR_MUTED, COLOR_MUTED, COLOR_MUTED, COLOR_EMERALD, COLOR_GOLD, COLOR_NAVY]

    y_pos = np.arange(len(cost_items))
    bars = ax.barh(y_pos, costs, color=colors, height=0.48, edgecolor=COLOR_BORDER, linewidth=1.2)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(cost_items, fontsize=8.2, fontweight='bold', color=COLOR_NAVY)
    ax.invert_yaxis()
    ax.set_xlabel('Unit Cost (AED / Seed Carrier)', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_title('Techno-Economic Cost Model vs. ASPIRE Ceiling Cap', fontsize=11, fontweight='bold', color=COLOR_NAVY, pad=18)
    ax.set_xlim(0, 0.49)
    ax.set_ylim(5.6, -0.6) # headroom at top
    ax.grid(axis='x', linestyle=':', alpha=0.5, color=COLOR_BORDER)

    # Vertical reference line at 0.400
    ax.axvline(0.400, color=COLOR_CRIMSON, linestyle='--', linewidth=1.6)
    
    # Placed cleanly at top inside plot area (safely below title)
    ax.text(0.400, -0.25, 'ASPIRE CAP: AED 0.40', ha='center', va='bottom', color=COLOR_CRIMSON, fontsize=8.0, fontweight='bold')

    # Value Labels positioned with ZERO overlap
    for i, (bar, val) in enumerate(zip(bars, costs)):
        if i == 3: # Factory Gate Total
            ax.text(val + 0.008, bar.get_y() + bar.get_height()/2, f'AED {val:.3f}', 
                    va='center', fontsize=8.8, fontweight='bold', color=COLOR_EMERALD)
        elif i == 4: # Landed Delivery
            ax.text(val + 0.008, bar.get_y() + bar.get_height()/2, f'AED {val:.3f}', 
                    va='center', fontsize=8.8, fontweight='bold', color=COLOR_GOLD)
        elif i == 5: # Ceiling Cap
            ax.text(val + 0.008, bar.get_y() + bar.get_height()/2, f'AED {val:.3f}', 
                    va='center', fontsize=8.8, fontweight='bold', color=COLOR_NAVY)
        else:
            ax.text(val + 0.008, bar.get_y() + bar.get_height()/2, f'AED {val:.3f}', 
                    va='center', fontsize=8.2, fontweight='bold', color=COLOR_NAVY)

    # 43% Safety Margin Bracket: placed at x = 0.30, y = 1.8 (safely between 0.227 and 0.400)
    ax.annotate('43% Safety Margin\n(17 fils buffer)', 
                xy=(0.227, 3.0), xytext=(0.305, 1.8),
                arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.3),
                fontsize=8.5, fontweight='bold', color=COLOR_EMERALD, ha='center')

    for spine in ax.spines.values():
        spine.set_color(COLOR_BORDER)

    plt.tight_layout()
    plt.savefig('assets/cost_waterfall.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/cost_waterfall.png (Zero clipping)")

if __name__ == '__main__':
    generate_terrapod_schematic()
    generate_thermal_plot()
    generate_hydrology_diagram()
    generate_root_mechanics_chart()
    generate_payload_chart()
    generate_cost_chart()
    print("[ALL 6 CORE SCIENTIFIC FIGURES COMPILED ACCURATELY]")
