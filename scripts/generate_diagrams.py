"""
Generate high-resolution deep-tech diagrams for Nabat TerraPod Presentation
Generates:
1. assets/terrapod_schematic.png - 2D CAD-style cutaway of the Ovoid TerraPod
2. assets/thermal_plot.png - Stefan-Boltzmann surface equilibrium temperature curves
3. assets/payload_chart.png - Drone sortie capacity & coverage comparison
4. assets/cost_waterfall.png - Unit cost breakdown vs ASPIRE ceiling
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Arc, Wedge
import numpy as np

os.makedirs('assets', exist_ok=True)

# Styling Constants
COLOR_NAVY = '#0F172A'
COLOR_EMERALD = '#047857'
COLOR_EMERALD_LIGHT = '#10B981'
COLOR_GOLD = '#B45309'
COLOR_CRIMSON = '#BE123C'
COLOR_MUTED = '#64748B'
COLOR_LIGHT_BG = '#F8FAFC'
COLOR_BORDER = '#CBD5E1'

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# =============================================================================
# 1. TERRAPOD CAD-STYLE CUTAWAY SCHEMATIC
# =============================================================================
def generate_terrapod_schematic():
    fig, ax = plt.subplots(figsize=(7, 5.5), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor(COLOR_LIGHT_BG)

    # Coordinates: Center at (0, 0)
    # Height = 29mm (-14.5 to +14.5), Width = 26.5mm (-13.25 to +13.25)
    
    # Outer Ovoid Boundary (Egg profile: wider at bottom, slightly tapered at top)
    # Parametric egg shape
    t = np.linspace(0, 2*np.pi, 300)
    # egg distortion
    a = 13.25  # semi-major equatorial radius
    b = 14.5   # semi-major height
    # Prolate egg parametric equation
    x_egg = a * np.sin(t)
    # taper slightly toward the top
    y_egg = b * np.cos(t) * (1.0 + 0.12 * np.cos(t))

    # Outer White Kaolin Shield Layer
    ax.fill(x_egg, y_egg, color='#E2E8F0', edgecolor=COLOR_NAVY, linewidth=2, zorder=2)
    
    # Inner Composite Body (Shrunk by 0.8mm)
    x_inner = (a - 0.9) * np.sin(t)
    y_inner = (b - 0.9) * np.cos(t) * (1.0 + 0.12 * np.cos(t))
    ax.fill(x_inner, y_inner, color='#334155', zorder=3) # Dark biochar core

    # Weighted Keel (Bottom half from y = -14.5 to y = -2)
    keel_mask = y_inner < -1.0
    ax.fill_between(x_inner, y_inner, -1.0, where=keel_mask, color='#1E293B', zorder=4)

    # Upper Concave Funnel (12mm diameter = -6 to +6 at top, depth = 4.2mm)
    # Cutout crater at top: from x = -6 to +6, curving down to y = 10.3
    x_funnel = np.linspace(-6.0, 6.0, 100)
    y_funnel_curve = 14.0 - 4.5 * (1.0 - (x_funnel / 6.0)**2)
    # Top edge of egg between -6 and +6
    top_mask = (x_egg >= -6.0) & (y_egg > 8.0)
    ax.fill_between(x_funnel, y_funnel_curve, 15.5, color=COLOR_LIGHT_BG, zorder=5)
    ax.plot(x_funnel, y_funnel_curve, color=COLOR_EMERALD, linewidth=2.5, zorder=6)

    # Seed Nest Chamber (Directly below funnel: x from -3.5 to 3.5, y from 6.0 to 9.5)
    seed_chamber = patches.Ellipse((0, 7.8), 7.0, 4.0, facecolor='#FEF3C7', edgecolor=COLOR_GOLD, linewidth=1.5, zorder=6)
    ax.add_patch(seed_chamber)

    # Seeds inside chamber
    seed1 = patches.Ellipse((-1.5, 7.8), 2.0, 1.2, angle=25, facecolor=COLOR_GOLD, zorder=7)
    seed2 = patches.Ellipse((1.5, 7.8), 1.6, 2.2, angle=-15, facecolor=COLOR_NAVY, zorder=7)
    ax.add_patch(seed1)
    ax.add_patch(seed2)

    # Diffuse Light Veil (Thin translucent layer on top of seed chamber)
    ax.plot([-3.5, 3.5], [9.8, 9.8], color=COLOR_EMERALD_LIGHT, linewidth=2.5, linestyle='--', zorder=8)

    # Center of Gravity Indicator (at 35% from bottom: -14.5 + 29*0.35 = -4.35)
    ax.plot([0], [-4.35], marker='+', markersize=14, markeredgewidth=2.5, color=COLOR_GOLD, zorder=9)
    ax.plot([0], [-4.35], marker='o', markersize=8, fillstyle='none', markeredgewidth=2, color=COLOR_GOLD, zorder=9)

    # Technical Annotations & Leaders
    # 1. Concave Funnel
    ax.annotate('12mm Concave Catchment Funnel\n(Harvests 0.56 mL rain)', 
                xy=(0, 10.5), xytext=(9.0, 14.0),
                arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.5),
                fontsize=8.5, fontweight='bold', color=COLOR_NAVY, zorder=10)

    # 2. Kaolin Albedo Shield
    ax.annotate('Kaolin Mineral Shield (R = 78%)\n(Reflects infrared heat; ΔT = -33°C)', 
                xy=(-12.5, 2.0), xytext=(-22.0, 8.0),
                arrowprops=dict(facecolor=COLOR_NAVY, edgecolor=COLOR_NAVY, arrowstyle='->', lw=1.5),
                fontsize=8.5, fontweight='bold', color=COLOR_NAVY, zorder=10)

    # 3. Seed Nest & Guild
    ax.annotate('Synergistic Seed Nest\n(Nurse grass + climax shrub)', 
                xy=(3.5, 7.8), xytext=(12.0, 6.0),
                arrowprops=dict(facecolor=COLOR_GOLD, edgecolor=COLOR_GOLD, arrowstyle='->', lw=1.5),
                fontsize=8.5, fontweight='bold', color=COLOR_GOLD, zorder=10)

    # 4. Center of Gravity (CG at 35%)
    ax.annotate('Forward Center of Gravity (CG at 35%)\n(Passive self-righting flight & impact)', 
                xy=(0, -4.35), xytext=(10.0, -4.5),
                arrowprops=dict(facecolor=COLOR_GOLD, edgecolor=COLOR_GOLD, arrowstyle='->', lw=1.5),
                fontsize=8.5, fontweight='bold', color=COLOR_NAVY, zorder=10)

    # 5. Fast-Dissolving Keel
    ax.annotate('Water-Soluble Keel (12% Gum Arabic)\n(Dissolves in 20 min; wet shear < 0.12 MPa)', 
                xy=(-6.0, -11.0), xytext=(-22.0, -11.0),
                arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.5),
                fontsize=8.5, fontweight='bold', color=COLOR_EMERALD, zorder=10)

    # Dimension Calipers
    # Height dimension (left)
    ax.plot([-17, -17], [-14.5, 14.5], color=COLOR_MUTED, lw=1.2)
    ax.plot([-18.5, -15.5], [14.5, 14.5], color=COLOR_MUTED, lw=1.2)
    ax.plot([-18.5, -15.5], [-14.5, -14.5], color=COLOR_MUTED, lw=1.2)
    ax.text(-19.5, 0, '29.0 mm', rotation=90, verticalalignment='center', horizontalalignment='right', 
            fontsize=9, fontweight='bold', color=COLOR_NAVY)

    # Width dimension (bottom)
    ax.plot([-13.25, 13.25], [-18, -18], color=COLOR_MUTED, lw=1.2)
    ax.plot([-13.25, -13.25], [-19.5, -16.5], color=COLOR_MUTED, lw=1.2)
    ax.plot([13.25, 13.25], [-19.5, -16.5], color=COLOR_MUTED, lw=1.2)
    ax.text(0, -20.5, '26.5 mm Diameter', horizontalalignment='center', 
            fontsize=9, fontweight='bold', color=COLOR_NAVY)

    ax.set_xlim(-24, 24)
    ax.set_ylim(-23, 18)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('assets/terrapod_schematic.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/terrapod_schematic.png")

# =============================================================================
# 2. STEFAN-BOLTZMANN THERMAL EQUILIBRIUM GRAPH
# =============================================================================
def generate_thermal_plot():
    from scipy.optimize import fsolve

    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor('#FFFFFF')

    # Solar Irradiance range (W/m2)
    G_range = np.linspace(200, 1100, 50)
    Tamb_C = 32.0
    Tamb = Tamb_C + 273.15
    Tsky = Tamb - 10.0
    hc = 13.0  # boundary layer convection
    sigma = 5.67e-8
    eps = 0.90

    def get_temp(G, alpha):
        def eq(T):
            return alpha * G - (hc * (T - Tamb) + eps * sigma * (T**4 - Tsky**4))
        return fsolve(eq, 330.0)[0] - 273.15

    T_dark = [get_temp(g, 0.92) for g in G_range]
    T_kaolin = [get_temp(g, 0.22) for g in G_range]

    # Plot Lethal Zone (> 42 deg C)
    ax.axhspan(42.0, 85.0, color='#FEE2E2', alpha=0.6, zorder=1)
    ax.axhspan(20.0, 42.0, color='#ECFDF5', alpha=0.6, zorder=1)
    ax.axhline(42.0, color=COLOR_CRIMSON, linestyle='--', linewidth=1.5, zorder=2)
    ax.text(220, 43.0, 'CRITICAL EMBRYO LETHAL THRESHOLD (42°C)', color=COLOR_CRIMSON, fontsize=8.5, fontweight='bold')

    # Plot Curves
    ax.plot(G_range, T_dark, color=COLOR_CRIMSON, linewidth=2.8, label='Uncoated Biochar (α = 0.92)', zorder=3)
    ax.plot(G_range, T_kaolin, color=COLOR_EMERALD, linewidth=2.8, label='Kaolin Albedo Shield (α = 0.22, R = 78%)', zorder=3)

    # 1,000 W/m2 Reference Points
    t_dark_1000 = get_temp(1000, 0.92)
    t_kao_1000 = get_temp(1000, 0.22)

    ax.plot([1000, 1000], [t_kao_1000, t_dark_1000], color=COLOR_NAVY, linestyle=':', linewidth=1.5, zorder=4)
    ax.scatter([1000, 1000], [t_dark_1000, t_kao_1000], color=[COLOR_CRIMSON, COLOR_EMERALD], s=70, zorder=5)

    ax.annotate(f'74.9°C (Lethal Heat Shock)', xy=(1000, t_dark_1000), xytext=(720, 77.0),
                arrowprops=dict(facecolor=COLOR_CRIMSON, edgecolor=COLOR_CRIMSON, arrowstyle='->', lw=1.2),
                fontsize=8.5, fontweight='bold', color=COLOR_CRIMSON)

    ax.annotate(f'40.6°C (Embryo Viable)', xy=(1000, t_kao_1000), xytext=(740, 32.0),
                arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.2),
                fontsize=8.5, fontweight='bold', color=COLOR_EMERALD)

    ax.annotate('ΔT = −34.3°C\nCooling Shield', xy=(1000, 56), xytext=(1020, 54),
                fontsize=8.5, fontweight='bold', color=COLOR_NAVY)

    ax.set_xlabel('Solar Irradiance G (W/m²)', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_ylabel('Surface Equilibrium Temperature (°C)', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_title('First-Principles Solar Radiation & Thermal Albedo Balance', fontsize=11, fontweight='bold', color=COLOR_NAVY, pad=12)
    ax.set_xlim(200, 1150)
    ax.set_ylim(25, 82)
    ax.grid(True, linestyle=':', alpha=0.5, color=COLOR_BORDER)
    ax.legend(loc='upper left', frameon=True, facecolor='#FFFFFF', edgecolor=COLOR_BORDER, fontsize=8.5)

    # Clean borders
    for spine in ax.spines.values():
        spine.set_color(COLOR_BORDER)

    plt.tight_layout()
    plt.savefig('assets/thermal_plot.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/thermal_plot.png")

# =============================================================================
# 3. DRONE PAYLOAD & COVERAGE COMPARISON CHART
# =============================================================================
def generate_payload_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.8), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax1.set_facecolor('#FFFFFF')
    ax2.set_facecolor('#FFFFFF')

    # Chart 1: Pods per 25kg UAV Sortie
    categories = ['Standard Puck\n(25g)', 'Nabat-BioDrop™\n(9.8g)']
    pods = [1000, 2550]
    colors1 = [COLOR_MUTED, COLOR_EMERALD]

    bars1 = ax1.bar(categories, pods, color=colors1, width=0.55, edgecolor=COLOR_BORDER, linewidth=1)
    ax1.set_ylabel('Pods per 25 kg Drone Flight', fontsize=9, fontweight='bold', color=COLOR_NAVY)
    ax1.set_title('UAV Payload Capacity', fontsize=10.5, fontweight='bold', color=COLOR_NAVY)
    ax1.set_ylim(0, 3000)
    ax1.grid(axis='y', linestyle=':', alpha=0.5, color=COLOR_BORDER)

    for bar, val in zip(bars1, pods):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 80, f'{val:,}', ha='center', fontsize=10, fontweight='bold', color=COLOR_NAVY)
    ax1.text(1, 1400, '+155%\nPayload', ha='center', fontsize=9.5, fontweight='bold', color='#FFFFFF', 
             bbox=dict(boxstyle='round,pad=0.3', facecolor=COLOR_NAVY, edgecolor='none'))

    # Chart 2: Hectare Coverage per Flight Sortie
    hectares = [0.66, 1.70] # at 1500 pods/ha
    bars2 = ax2.bar(categories, hectares, color=[COLOR_MUTED, COLOR_GOLD], width=0.55, edgecolor=COLOR_BORDER, linewidth=1)
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
# 4. TECHNO-ECONOMIC COST WATERFALL CHART
# =============================================================================
def generate_cost_chart():
    fig, ax = plt.subplots(figsize=(6.8, 3.8), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor('#FFFFFF')

    cost_items = [
        'Raw Materials\n(Biochar, Clay, Seeds)',
        'Direct Labor\n(4 Techs @ 500k/mo)',
        'Capex & Plant\n(Amortization over 5M)',
        'Factory-Gate Total\n(Conversion Cost)',
        'Landed Delivery\n(Freight & 35% Margin)',
        'ASPIRE Ceiling Cap\n(Maximum Allowed)'
    ]
    costs = [0.096, 0.052, 0.079, 0.227, 0.307, 0.400]
    colors = [COLOR_MUTED, COLOR_MUTED, COLOR_MUTED, COLOR_EMERALD, COLOR_GOLD, COLOR_NAVY]

    y_pos = np.arange(len(cost_items))
    bars = ax.barh(y_pos, costs, color=colors, height=0.55, edgecolor=COLOR_BORDER, linewidth=1)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(cost_items, fontsize=8.5, fontweight='bold', color=COLOR_NAVY)
    ax.invert_yaxis()
    ax.set_xlabel('Unit Cost (AED / Seed Carrier)', fontsize=9.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_title('Techno-Economic Cost Model vs. ASPIRE Ceiling Cap', fontsize=11, fontweight='bold', color=COLOR_NAVY, pad=12)
    ax.set_xlim(0, 0.46)
    ax.grid(axis='x', linestyle=':', alpha=0.5, color=COLOR_BORDER)

    # Vertical reference line at 0.40
    ax.axvline(0.400, color=COLOR_CRIMSON, linestyle='--', linewidth=1.5)
    ax.text(0.402, 5.3, 'CEILING: AED 0.40', color=COLOR_CRIMSON, fontsize=8, fontweight='bold')

    for bar, val in zip(bars, costs):
        ax.text(val + 0.008, bar.get_y() + bar.get_height()/2, f'AED {val:.3f}', 
                va='center', fontsize=9, fontweight='bold', color=COLOR_NAVY)

    # 43% safety buffer bracket annotation
    ax.annotate('43% Safety Margin (17 fils)', xy=(0.227, 3), xytext=(0.28, 2.3),
                arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.2),
                fontsize=8.5, fontweight='bold', color=COLOR_EMERALD)

    for spine in ax.spines.values():
        spine.set_color(COLOR_BORDER)

    plt.tight_layout()
    plt.savefig('assets/cost_waterfall.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/cost_waterfall.png")

# =============================================================================
# 5. HYDROLOGY COMPARISON DIAGRAM
# =============================================================================
def generate_hydrology_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.8), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax1.set_facecolor('#FFFFFF')
    ax2.set_facecolor('#FFFFFF')

    # Left: Conventional Convex Pellet
    ax1.set_title("Standard Convex Pellet\n(80% Rain Shedding Runoff)", fontsize=9.5, fontweight='bold', color=COLOR_CRIMSON)
    theta = np.linspace(0, np.pi, 100)
    x_dome = 10 * np.cos(theta)
    y_dome = 8 * np.sin(theta)
    ax1.fill_between(x_dome, 0, y_dome, color='#CBD5E1', edgecolor=COLOR_NAVY, lw=1.5)
    ax1.plot([-14, 14], [0, 0], color='#D97706', lw=2) # Sand surface
    for rx in [-6, -2, 2, 6]:
        ax1.annotate('', xy=(rx*1.5, 3), xytext=(rx, 11),
                     arrowprops=dict(facecolor=COLOR_CRIMSON, edgecolor=COLOR_CRIMSON, arrowstyle='->', lw=1.5))
    ax1.text(0, -2.5, "Lateral Runoff: Water sheds outward\ninto hot sand; desiccation in <90 min", ha='center', fontsize=7.5, color=COLOR_CRIMSON, fontweight='bold')
    ax1.set_xlim(-16, 16)
    ax1.set_ylim(-5, 14)
    ax1.axis('off')

    # Right: BioDrop Concave Catchment Funnel
    ax2.set_title("Nabat-BioDrop™ Concave Funnel\n(100% Water Concentration)", fontsize=9.5, fontweight='bold', color=COLOR_EMERALD)
    t = np.linspace(-np.pi, 0, 100)
    x_body = 10 * np.cos(t)
    y_body = 12 * np.sin(t)
    ax2.plot([-14, 14], [-6, -6], color='#D97706', lw=2) # Sand surface
    ax2.fill_between(x_body, -6, y_body, color='#E2E8F0', edgecolor=COLOR_NAVY, lw=1.5)
    xf = np.linspace(-6, 6, 50)
    yf = - 3.5 * (1.0 - (xf/6)**2)
    ax2.fill_between(xf, -6, yf, color='#ECFDF5', edgecolor=COLOR_EMERALD, lw=2)
    for rx in [-4, -1.5, 1.5, 4]:
        ax2.annotate('', xy=(rx*0.4, -2.5), xytext=(rx, 8),
                     arrowprops=dict(facecolor=COLOR_EMERALD, edgecolor=COLOR_EMERALD, arrowstyle='->', lw=1.5))
    ax2.text(0, -4.5, "0.56 mL Captured\nDirect into Core", ha='center', fontsize=7.5, color=COLOR_EMERALD, fontweight='bold')
    ax2.text(0, -9.5, "100% Catchment: Inward 12mm crater\ndeposits rain directly onto embryo", ha='center', fontsize=7.5, color=COLOR_NAVY, fontweight='bold')
    ax2.set_xlim(-16, 16)
    ax2.set_ylim(-12, 11)
    ax2.axis('off')

    plt.tight_layout()
    plt.savefig('assets/hydrology_diagram.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/hydrology_diagram.png")

# =============================================================================
# 6. ROOT BIOMECHANICS FORCE BAR CHART
# =============================================================================
def generate_root_mechanics_chart():
    fig, ax = plt.subplots(figsize=(6.8, 3.8), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor('#FFFFFF')

    bars = ['Wet BioDrop™ Keel\n(Dissolved in 20 min)', 'Emerging Radicle\n(Turgor Pressure Limit)', 'Sun-Baked Clay Clod\n(Standard Pellet Shell)']
    forces = [0.12, 1.0, 2.5]
    bar_colors = [COLOR_EMERALD, COLOR_GOLD, COLOR_CRIMSON]

    b = ax.barh(bars, forces, color=bar_colors, height=0.52, edgecolor=COLOR_BORDER)
    ax.set_xlabel('Compressive Shear Resistance / Penetration Force (MPa)', fontsize=9, fontweight='bold', color=COLOR_NAVY)
    ax.set_title('Root Biomechanics: Overcoming the "Concrete Tomb"', fontsize=10.5, fontweight='bold', color=COLOR_NAVY)
    ax.set_xlim(0, 3.2)
    ax.grid(axis='x', linestyle=':', alpha=0.5, color=COLOR_BORDER)

    ax.axvline(1.2, color=COLOR_GOLD, linestyle='--', lw=1.5)
    ax.text(1.25, 1.25, 'Radicle Limit (1.2 MPa)', color=COLOR_GOLD, fontsize=8, fontweight='bold')

    ax.text(0.18, 0, '< 0.12 MPa (Zero Barrier - Sprout Free)', va='center', fontsize=8, fontweight='bold', color=COLOR_EMERALD)
    ax.text(1.05, 1, '0.8–1.2 MPa (Biological Push)', va='center', fontsize=8, fontweight='bold', color=COLOR_NAVY)
    ax.text(2.55, 2, '> 2.5 MPa (Fatal Trap)', va='center', fontsize=8, fontweight='bold', color=COLOR_CRIMSON)

    for spine in ax.spines.values():
        spine.set_color(COLOR_BORDER)

    plt.tight_layout()
    plt.savefig('assets/root_mechanics_chart.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/root_mechanics_chart.png")

# =============================================================================
# 7. MANUFACTURING PROCESS PIPELINE
# =============================================================================
def generate_manufacturing_flow():
    fig, ax = plt.subplots(figsize=(6.8, 3.8), dpi=300)
    fig.patch.set_facecolor(COLOR_LIGHT_BG)
    ax.set_facecolor(COLOR_LIGHT_BG)

    steps = [
        ('STAGE 1: FEEDSTOCK', 'Biochar & Clay Blending', 'Date palm biochar (32%)\nCalcium bentonite (28%)\nNative desert seed guild', COLOR_NAVY),
        ('STAGE 2: GRANULATION', 'Disc Pan Agglomeration', '2.2 m pan granulator @ 18 RPM\n45° tilt, continuous feed\n50,000 units / day / line', COLOR_GOLD),
        ('STAGE 3: TOOLING', 'Soluble Keel Compression', 'Cold-soluble gum arabic base\nCenter of gravity weighted to 35%\nUpper 12 mm concave tooling', COLOR_NAVY),
        ('STAGE 4: COATING', 'Fluidized Bed Albedo Coat', '20% Kaolin albedo spray (R=78%)\n2% Carnauba wax dew seal (85°C)\nGentle dehydration at 38°C', COLOR_EMERALD)
    ]

    for idx, (stg, tit, sub, col) in enumerate(steps):
        by = 3.0 - idx * 0.95
        rect = patches.FancyBboxPatch((0.1, by), 6.6, 0.82, boxstyle='round,pad=0.08', facecolor='#FFFFFF', edgecolor=col, lw=1.5)
        ax.add_patch(rect)
        # Left tag bar
        tag_bar = patches.Rectangle((0.1, by), 1.9, 0.82, facecolor=col)
        ax.add_patch(tag_bar)
        ax.text(1.05, by + 0.41, stg, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')
        # Title and details
        ax.text(2.15, by + 0.55, tit, ha='left', va='center', fontsize=8.5, fontweight='bold', color=COLOR_NAVY)
        ax.text(2.15, by + 0.23, sub.replace('\n', '  |  '), ha='left', va='center', fontsize=7, color=COLOR_MUTED)

    ax.set_xlim(0, 6.8)
    ax.set_ylim(0, 3.9)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('assets/manufacturing_flow.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[SUCCESS] Generated assets/manufacturing_flow.png")

if __name__ == '__main__':
    generate_terrapod_schematic()
    generate_thermal_plot()
    generate_payload_chart()
    generate_cost_chart()
    generate_hydrology_diagram()
    generate_root_mechanics_chart()
    generate_manufacturing_flow()
    print("[ALL 7 ASSETS GENERATED SUCCESSFULLY]")
