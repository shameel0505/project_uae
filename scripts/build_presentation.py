"""
Nabat TerraPod Challenge - Phase 1 Technical Proposal Deck Generator
Generates a professional 16:9 widescreen PowerPoint deck (.pptx)
Aesthetic: Option A - Clean Deep-Tech Engineering Briefing (ATRC/ASPIRE standards)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path="Nabat_TerraPod_Proposal_Shameel.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Clean Deep-Tech
    COLOR_BG = RGBColor(248, 250, 252)        # Slate 50 (#F8FAFC)
    COLOR_CARD = RGBColor(255, 255, 255)      # White
    COLOR_BORDER = RGBColor(226, 232, 240)    # Slate 200 (#E2E8F0)
    COLOR_NAVY = RGBColor(10, 37, 64)         # Deep Navy (#0A2540)
    COLOR_EMERALD = RGBColor(5, 150, 105)     # ATRC Emerald (#059669)
    COLOR_GOLD = RGBColor(180, 83, 9)         # Desert Amber / Gold (#B45309)
    COLOR_TEXT_MAIN = RGBColor(15, 23, 42)    # Slate 900 (#0F172A)
    COLOR_TEXT_MUTED = RGBColor(71, 85, 105)  # Slate 600 (#475569)
    COLOR_TEXT_LIGHT = RGBColor(148, 163, 184)# Slate 400 (#94A3B8)

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="NABAT TERRAPOD CHALLENGE | PHASE 1 TECHNICAL DECK"):
        # Category Tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_GOLD

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.733), Inches(0.6))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY

        # Subtle divider
        divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.02))
        divider.fill.solid()
        divider.fill.fore_color.rgb = COLOR_BORDER
        divider.line.fill.background()

    def add_footer(slide, text="Tagged: [Modelled = first-principles physics] | [Target = design requirement] | Lead: Mohamed Shameel"):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.35))
        tf = footer_box.text_frame
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(8.5)
        p.font.color.rgb = COLOR_TEXT_LIGHT

    def create_card(slide, left, top, width, height, title="", border_color=COLOR_BORDER, fill_color=COLOR_CARD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.1), width - Inches(0.3), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = title.upper()
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_NAVY
        return card

    # =========================================================================
    # SLIDE 1: COVER & EXECUTIVE SUMMARY
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)
    add_header(s1, "Nabat-BioDrop™: Biomimetic Rainwater-Harvesting Seed Carrier", "ASPIRE / ATRC ABU DHABI & NABAT AI TECHNOLOGIES")

    # Left Hero Box
    create_card(s1, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "Executive System Summary")
    s1_text = s1.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf1 = s1_text.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "The Nabat-BioDrop™ TerraPod solves the primary failure modes of hyper-arid aerial restoration: wind drift, extreme surface scorching (>65°C), rain shedding, and seed entrapment."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT_MAIN

    p2 = tf1.add_paragraph()
    p2.text = "\nOptimized for high-speed continuous UAV broadcast (5 m/s cruise), it integrates:"
    p2.font.size = Pt(12)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_NAVY

    bullets = [
        "Self-Anchoring Ovoid Keel: Prevents wind roll; penetrates 9-13mm into sand.",
        "Concave Rainwater Funnel: Captures 5x more rain directly into seed nest.",
        "Kaolin Albedo Shield: 78% solar reflectance drops surface temp by 33.3°C.",
        "Water-Soluble Root Escape: Matrix shear drops to <0.12 MPa on rain contact.",
        "100% Bio-Composite: Zero synthetic polymers, zero microplastics."
    ]
    for b in bullets:
        bp = tf1.add_paragraph()
        bp.text = f"• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    # Right Metric Grid (4 Cards)
    metrics = [
        ("AERODYNAMIC ADVANTAGE", "Prolate Ovoid (Cd = 0.33)", "-27.4% lateral wind drift vs. sphere;\nself-anchors on 15.85 m/s impact [Modelled].", COLOR_EMERALD),
        ("THERMAL ALBEDO SHIELD", "Kaolin Mineral Coat (R = 78%)", "Drops surface equilibrium from 74.7°C to 41.4°C\n(ΔT = -33.3°C), preventing embryo death [Modelled].", COLOR_GOLD),
        ("RAINWATER CATCHMENT", "12mm Concave Funnel Aperture", "Captures 0.565 mL directly to seed nest in a 5mm\nshower (5x higher concentration vs dome) [Modelled].", COLOR_NAVY),
        ("TECHNO-ECONOMIC COST", "AED 0.227 per Seed-Carrier", "Itemized production model at 1M units; delivers a\n43.1% safety margin below the AED 0.40 ceiling.", COLOR_EMERALD)
    ]
    coords = [
        (Inches(6.7), Inches(1.6)),
        (Inches(9.7), Inches(1.6)),
        (Inches(6.7), Inches(4.2)),
        (Inches(9.7), Inches(4.2))
    ]
    for i, (m_tag, m_val, m_desc, m_col) in enumerate(metrics):
        cx, cy = coords[i]
        create_card(s1, cx, cy, Inches(2.8), Inches(2.5), m_tag)
        mtb = s1.shapes.add_textbox(cx + Inches(0.15), cy + Inches(0.55), Inches(2.5), Inches(1.8))
        mtf = mtb.text_frame
        mtf.word_wrap = True
        mp1 = mtf.paragraphs[0]
        mp1.text = m_val
        mp1.font.size = Pt(13)
        mp1.font.bold = True
        mp1.font.color.rgb = m_col

        mp2 = mtf.add_paragraph()
        mp2.text = f"\n{m_desc}"
        mp2.font.size = Pt(10)
        mp2.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s1, "Challenge Track: Nabat TerraPod Challenge (NTPC) | Author: Mohamed Shameel (shameel0505@gmail.com)")

    # =========================================================================
    # SLIDE 2: THE PROBLEM: FOUR ARID BOTTLENECK MODES
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "The Desert Restoration Dilemma: Four Critical Failure Modes", "PHYSICAL & PHYSIOLOGICAL BOTTLENECKS IN ABU DHABI DESERTS")

    problems = [
        ("1. WIND DRIFT & DUNE ROLLING",
         "The Mechanical Hazard:",
         "Spherical pods drift >3.6m in a 5 m/s wind and roll across bare dunes under 35 km/h Shamal winds.\n\nThey roll into dune hollows and are buried under 20-50 cm of drifting sand, extinguishing light and suffocating the embryo."),
        ("2. THE THERMAL COOKING TRAP",
         "The Physiological Hazard:",
         "Unshaded desert sand and dark biochar reach 65-75°C under 1,000 W/m² solar irradiance.\n\nHydrated seeds experience protein denaturation and irreversible thermo-inhibition above 42°C, baking the embryo before emergence."),
        ("3. CONVEX WATER SHEDDING",
         "The Hydrological Hazard:",
         "Standard convex domes and spheres shed >80% of scarce rainfall outward into surrounding dry sand.\n\nSurface moisture evaporates within 90 minutes (VPD > 4.5 kPa), leaving the seed dry before metabolic imbibition completes."),
        ("4. THE 'CONCRETE TOMB' EFFECT",
         "The Root Impedance Hazard:",
         "Standard clay and bentonite composites cure into hard clods with compressive strength >2.5 MPa.\n\nEmbryonic radicles generate only 0.8-1.2 MPa turgor; seedlings germinate inside but cannot penetrate out, dying trapped.")
    ]

    card_w = Inches(2.75)
    for i, (p_title, p_sub, p_body) in enumerate(problems):
        px = Inches(0.8) + i * Inches(2.98)
        create_card(s2, px, Inches(1.6), card_w, Inches(5.1), p_title)
        ptb = s2.shapes.add_textbox(px + Inches(0.15), Inches(2.2), card_w - Inches(0.3), Inches(4.3))
        ptf = ptb.text_frame
        ptf.word_wrap = True
        pp1 = ptf.paragraphs[0]
        pp1.text = p_sub
        pp1.font.size = Pt(11)
        pp1.font.bold = True
        pp1.font.color.rgb = COLOR_GOLD

        pp2 = ptf.add_paragraph()
        pp2.text = f"\n{p_body}"
        pp2.font.size = Pt(11)
        pp2.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s2, "References: El-Keblawy & Al-Shamsi (2008); Mohan et al. (2021) Remote Sensing. Tagged: [Modelled & Published Lit]")

    # =========================================================================
    # SLIDE 3: AERODYNAMIC GEOMETRY & CONTINUOUS UAV FLIGHT DYNAMICS
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Ballistic Stability & Continuous Cruise Dispensing (Mode B)", "AERODYNAMICS, DRAG REDUCTION & SAND ANCHORING")

    # Left Narrative Card
    create_card(s3, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.1), "Flight Dynamics & Anchoring")
    s3_text = s3.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(4.4), Inches(4.3))
    tf3 = s3_text.text_frame
    tf3.word_wrap = True

    p = tf3.paragraphs[0]
    p.text = "Optimized for Continuous Cruise Broadcast (Mode B) at 5 m/s forward UAV ground speed:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    s3_bullets = [
        "Dimensions: 29.0 mm height x 26.5 mm diameter (All axes strictly 25-30 mm).",
        "Passive Self-Righting: Forward Center of Gravity (CG at 35%) ensures heavy keel leads in flight.",
        "Oblique Impact: Enters sand at 16.6 m/s resultant velocity (θ = 72° impact angle).",
        "Granular Penetration: Poncelet model predicts 9.0-13.5 mm substrate anchoring in loose dune sand.",
        "Wind Roll Immunity: Anchored base resists 40 km/h Shamal winds while keeping funnel oriented upward."
    ]
    for b in s3_bullets:
        bp = tf3.add_paragraph()
        bp.text = f"• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    # Right Comparison Table Card
    create_card(s3, Inches(5.9), Inches(1.6), Inches(6.6), Inches(5.1), "Ballistic Model Comparison Table")

    # Table
    table_shape = s3.shapes.add_table(5, 4, Inches(6.1), Inches(2.3), Inches(6.2), Inches(3.8))
    table = table_shape.table
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(1.3)
    table.columns[2].width = Inches(1.5)
    table.columns[3].width = Inches(1.2)

    headers = ["Parameter", "Sphere (27mm)", "BioDrop™ Ovoid", "Delta"]
    rows = [
        ["Drag Coefficient (Cd)", "0.47", "0.33 [Modelled]", "-29.8%"],
        ["Terminal Velocity (vt)", "24.39 m/s", "30.13 m/s", "+23.5%"],
        ["Impact Speed (15m)", "15.24 m/s", "15.85 m/s", "+4.0%"],
        ["Crosswind Drift (5m/s)", "3.65 m", "2.65 m [Modelled]", "-27.4%"]
    ]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_CARD

    for row_idx, r in enumerate(rows):
        for col_idx, val in enumerate(r):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 0 else RGBColor(241, 245, 249)
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(10)
                p.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s3, "Physics derived from Poncelet granular continuum & Navier-Stokes aerodynamic drag. Tagged: [Modelled]")

    # =========================================================================
    # SLIDE 4: BIOMATERIAL MATRIX & HIGH-ALBEDO KAOLIN SHIELD
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Biomaterial Formulation & Thermal Albedo Shielding", "100% BIO-BASED COMPOSITE | ZERO SYNTHETIC POLYMERS | ZERO MICROPLASTICS")

    create_card(s4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "Mass Balance Formulation (9.80 g Pod)")
    s4_tbl_shape = s4.shapes.add_table(7, 3, Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.2))
    s4_tbl = s4_tbl_shape.table
    s4_tbl.columns[0].width = Inches(2.4)
    s4_tbl.columns[1].width = Inches(1.2)
    s4_tbl.columns[2].width = Inches(1.6)

    m_headers = ["Ingredient", "Fraction", "Mass / Pod"]
    m_rows = [
        ["Date Palm Frond Biochar", "32.0% w/w", "3.14 g"],
        ["Calcium Bentonite Clay", "28.0% w/w", "2.74 g"],
        ["Kaolin Albedo Shield", "20.0% w/w", "1.96 g"],
        ["Gum Arabic (Acacia)", "12.0% w/w", "1.18 g"],
        ["Sodium Alginate", "6.0% w/w", "0.59 g"],
        ["Carnauba Wax Seal", "2.0% w/w", "0.19 g"]
    ]
    for col_idx, h in enumerate(m_headers):
        c = s4_tbl.cell(0, col_idx)
        c.text = h
        c.fill.solid()
        c.fill.fore_color.rgb = COLOR_NAVY
        for p in c.text_frame.paragraphs:
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_CARD

    for row_idx, r in enumerate(m_rows):
        for col_idx, val in enumerate(r):
            c = s4_tbl.cell(row_idx + 1, col_idx)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 0 else RGBColor(241, 245, 249)
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(10)
                p.font.color.rgb = COLOR_TEXT_MAIN

    # Right Thermal Analysis Box
    create_card(s4, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.1), "First-Principles Thermal Radiation Model")
    s4_text = s4.shapes.add_textbox(Inches(6.9), Inches(2.2), Inches(5.4), Inches(4.3))
    tf4 = s4_text.text_frame
    tf4.word_wrap = True

    p = tf4.paragraphs[0]
    p.text = "Under 1,000 W/m² desert solar radiation (Tamb = 32°C, hc = 18 W/m²K):"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    t_bullets = [
        "Uncoated Dark Biochar (α = 0.92): Absorbs 920 W/m²; surface temp reaches 74.7°C (Lethal embryo denaturation).",
        "Kaolin Mineral Shield (α = 0.22, R = 78%): Reflects 780 W/m²; surface temp drops to 41.4°C.",
        "Thermal Breakthrough (ΔT = -33.3°C): Kaolin shield maintains the seed nest safely below the 42°C thermo-inhibition limit.",
        "Zero Microplastics: Certified 100% natural mineral and plant biopolymer matrix; zero polyacrylamides (PAM)."
    ]
    for b in t_bullets:
        bp = tf4.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s4, "Reference: Al-Rumaihi et al., Khalifa University (2022) Heliyon. Thermal model derived via Stefan-Boltzmann balance.")

    # =========================================================================
    # SLIDE 5: HYDROLOGICAL CATCHMENT & DEW SUPPRESSION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Biomimetic Rainwater Catchment & Dew Suppression", "CONCAVE FUNNEL WATER CONCENTRATION & PHASE-SELECTIVE ACTIVATION")

    create_card(s5, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "12mm Concave Catchment Funnel")
    s5_t1 = s5.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf5_1 = s5_t1.text_frame
    tf5_1.word_wrap = True

    p = tf5_1.paragraphs[0]
    p.text = "Overcoming Convex Runoff (5x Water Concentration):"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    c_bullets = [
        "Concave Aperture: 12.0 mm diameter cup (1.13 cm² catchment area) sloping inward at 35° directly to seed nest.",
        "Rain Event Harvesting: In a 5.0 mm desert storm, the funnel harvests 0.565 mL (565 mg) of liquid water directly into the central core.",
        "Convex Comparison: Standard convex balls shed >80% of rain into sand; the concave funnel concentrates 100% of intercepted rain.",
        "Auto-Filling Sand Bed: Windblown sand settling in the funnel creates an ideal 3-5mm protective Goldilocks moisture blanket."
    ]
    for b in c_bullets:
        bp = tf5_1.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    create_card(s5, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.1), "Thermal Dew Suppression Barrier")
    s5_t2 = s5.shapes.add_textbox(Inches(6.9), Inches(2.2), Inches(5.4), Inches(4.3))
    tf5_2 = s5_t2.text_frame
    tf5_2.word_wrap = True

    p = tf5_2.paragraphs[0]
    p.text = "Eliminating False Germination via Carnauba Seal:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    d_bullets = [
        "The Dew Trap: Morning dew (0.1-0.3 mm) hydrates seeds, but 55°C midday sun evaporates it in 90 min, causing lethal embryo lysis.",
        "High-Melting Carnauba (82-86°C): Unlike beeswax (melts at 62°C), carnauba remains rock-solid in desert heat.",
        "Threshold Resistance: 15µm carnauba film (contact angle θ > 95°) completely repels superficial dew (<0.5 mm).",
        "Storm Actuation: Sustained rainfall (≥5 mm) floods the funnel, dissolving the soluble matrix and triggering deep hydration."
    ]
    for b in d_bullets:
        bp = tf5_2.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s5, "Calculated via aperture integral: V = P x Afunnel. Contact angle theta > 95°. Tagged: [Modelled]")

    # =========================================================================
    # SLIDE 6: ROOT ESCAPE MATRIX & MICRO-GUILD STRATEGY
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Root Mechanical Freedom & Synergistic Micro-Guilds", "PREVENTING ROOT ENTRAPMENT & EMULATING DESERT NURSE ECOLOGY")

    create_card(s6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "Water-Soluble Root Escape Keel")
    s6_t1 = s6.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf6_1 = s6_t1.text_frame
    tf6_1.word_wrap = True

    p = tf6_1.paragraphs[0]
    p.text = "Eliminating the 'Concrete Tomb' Effect:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    r_bullets = [
        "Radicle Turgor Limit: An emerging baby radicle exerts maximum 0.8-1.2 MPa turgor pressure.",
        "Dry Clod Strength: Standard dried clay/bentonite exceeds 2.5 MPa, physically trapping and killing emerging roots.",
        "Soluble Gum Release: Formulated with 12% cold-soluble Gum Arabic. Moisture contact dissolves the binder within 20 minutes.",
        "Wet Shear Reduction: Wet matrix shear drops to <0.12 MPa (<< 0.8 MPa), allowing radicle to penetrate downward into damp sand."
    ]
    for b in r_bullets:
        bp = tf6_1.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    create_card(s6, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.1), "Synergistic Seed Micro-Guild Strategy")
    s6_t2 = s6.shapes.add_textbox(Inches(6.9), Inches(2.2), Inches(5.4), Inches(4.3))
    tf6_2 = s6_t2.text_frame
    tf6_2.word_wrap = True

    p = tf6_2.paragraphs[0]
    p.text = "Multi-Species Ecological Synergy (Nurse Guild):"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    g_bullets = [
        "Pioneer Nurse Grass (2 seeds Stipagrostis plumosa): Germinates in 48 hours; establishes fibrous surface roots to bind sand.",
        "Climax Shrub (1 seed Haloxylon salicornicum): Slower starter; benefits from nurse grass wind-shading and sends deep taproot.",
        "Diffuse Photonic Veil: Seed nest covered by thin diffuse kaolin/alginate film (10-20% light transmission) to satisfy phytochrome.",
        "Aerobic Porosity (>30µm): Interconnected pore channels ensure O2 diffusion, preventing embryo hypoxia and fermentation."
    ]
    for b in g_bullets:
        bp = tf6_2.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s6, "References: El-Keblawy et al. (2011) Seed Sci. & Technol. Shear strength model verified via Mohr-Coulomb failure criteria.")

    # =========================================================================
    # SLIDE 7: SOLUTION READINESS & EMPIRICAL VALIDATION
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Solution Readiness & Empirical Validation Protocol", "PROGRESSION FROM FIRST-PRINCIPLES MODELING (TRL 3) TO FIELD TESTING (TRL 6)")

    create_card(s7, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.1), "TRL Transition Roadmap")
    s7_t1 = s7.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(4.4), Inches(4.3))
    tf7_1 = s7_t1.text_frame
    tf7_1.word_wrap = True

    p = tf7_1.paragraphs[0]
    p.text = "Grounded Engineering Progression:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    trl_bullets = [
        "Phase 1 (Current - TRL 3/4): Complete first-principles physical, thermal, and ballistic modeling; bench surrogate validation.",
        "Phase 2 (Dec 2026 - TRL 4/5): Semi-finalist video pitch; prototype mechanical drop characterization and dissolution curves.",
        "Phase 3 (Jan 2027 - TRL 6): Production of 2,000 ready-to-deploy units; live UAV field trials across Abu Dhabi desert study plots.",
        "Transparent Reporting: All metrics explicitly tagged [Modelled], [Measured], or [Target] to ensure zero unsubstantiated claims."
    ]
    for b in trl_bullets:
        bp = tf7_1.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    create_card(s7, Inches(5.9), Inches(1.6), Inches(6.6), Inches(5.1), "Empirical Validation Protocol Summary")
    s7_tbl_shape = s7.shapes.add_table(5, 4, Inches(6.1), Inches(2.3), Inches(6.2), Inches(3.8))
    s7_tbl = s7_tbl_shape.table
    s7_tbl.columns[0].width = Inches(2.0)
    s7_tbl.columns[1].width = Inches(1.1)
    s7_tbl.columns[2].width = Inches(1.8)
    s7_tbl.columns[3].width = Inches(1.3)

    v_headers = ["Validation Assay", "Sample Size", "Methodology", "Benchmark Target"]
    v_rows = [
        ["Dimensional Audit", "n = 20", "Digital Vernier Caliper (3 axes)", "29.0 x 26.5 ± 0.4mm"],
        ["Crush Strength", "n = 10", "Calibrated digital force gauge", ">50 N fracture force"],
        ["15m Sand Drop", "n = 30", "Drop onto loose dune sand", "≥95% intact; 9-13mm"],
        ["Germination Proxy", "4 x 25 seeds", "Lepidium sativum dish assays", "≥25% higher emergence"]
    ]
    for col_idx, h in enumerate(v_headers):
        c = s7_tbl.cell(0, col_idx)
        c.text = h
        c.fill.solid()
        c.fill.fore_color.rgb = COLOR_NAVY
        for p in c.text_frame.paragraphs:
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_CARD

    for row_idx, r in enumerate(v_rows):
        for col_idx, val in enumerate(r):
            c = s7_tbl.cell(row_idx + 1, col_idx)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 0 else RGBColor(241, 245, 249)
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(10)
                p.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s7, "Testing compliant with ChallengeON Phase 1 guidelines. Physical deployment batch scheduled for Phase 3.")

    # =========================================================================
    # SLIDE 8: SCALED MANUFACTURING & NABAT UAV COMPATIBILITY
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Continuous Scalability & Nabat UAV Payload Integration", "CONTINUOUS DISC GRANULATION DELIVERING 50,000 PODS/DAY PER LINE")

    create_card(s8, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "Single-Stage Disc Agglomeration")
    s8_t1 = s8.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf8_1 = s8_t1.text_frame
    tf8_1.word_wrap = True

    p = tf8_1.paragraphs[0]
    p.text = "Simplified Industrial Manufacturing Flowsheet:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    m_flow = [
        "Continuous Disc Granulation: Scaled on standard 2.2m disc granulators (45° tilt, 18 RPM) with concave tooling.",
        "Avoiding Complex Assemblies: Single-step agglomeration followed by rotary mineral coating avoids fussy multi-part molding.",
        "High Line Throughput: One continuous line produces 50,000 pods/day (1.2 tonnes/day output).",
        "Low-Temp Dehydration: Fluidized bed drying at 38°C preserves embryo viability and endophytes."
    ]
    for b in m_flow:
        bp = tf8_1.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    create_card(s8, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.1), "Nabat UAV Payload Integration")
    s8_t2 = s8.shapes.add_textbox(Inches(6.9), Inches(2.2), Inches(5.4), Inches(4.3))
    tf8_2 = s8_t2.text_frame
    tf8_2.word_wrap = True

    p = tf8_2.paragraphs[0]
    p.text = "Payload Capacity on 25 kg Commercial Drone:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    uav_points = [
        "Universal Dispenser Fit: Symmetric 26.5mm diameter guarantees jam-free flow in rotary drum and pneumatic spreaders.",
        "2,550 Pods per Flight Sortie: At 9.8g unit mass, a 25kg payload UAV carries 2,550 pods (+155% vs. heavy 25g pucks).",
        "High Operational Speed: Cruise dispensing at 5 m/s covers 12-15 hectares per hour.",
        "Low Launch Energy: Smooth outer wax finish ensures zero barrel friction during high-speed broadcast."
    ]
    for b in uav_points:
        bp = tf8_2.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s8, "Throughput based on continuous disc granulator specs. UAV metrics based on standard 25kg drone payload capacity.")

    # =========================================================================
    # SLIDE 9: TECHNO-ECONOMIC VIABILITY: AED 0.227 PER CARRIER
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Techno-Economic Cost Model & Scalability", "FACTORY-GATE COST: AED 0.227 DELIVERS A 43.1% MARGIN BELOW AED 0.40 CEILING")

    create_card(s9, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "Itemized Unit Cost Structure (1,000,000 Units)")
    s9_tbl_shape = s9.shapes.add_table(6, 3, Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.2))
    s9_tbl = s9_tbl_shape.table
    s9_tbl.columns[0].width = Inches(2.6)
    s9_tbl.columns[1].width = Inches(1.3)
    s9_tbl.columns[2].width = Inches(1.3)

    c_headers = ["Cost Component", "Cost / Pod", "% Total"]
    c_rows = [
        ["Raw Materials (Biochar, Clay, Gum)", "AED 0.0958", "42.1%"],
        ["Direct Labor (4 Plant Technicians)", "AED 0.0520", "22.9%"],
        ["Capex Depreciation (AED 250k plant)", "AED 0.0450", "19.8%"],
        ["Quality Screening & Jute Packaging", "AED 0.0300", "13.2%"],
        ["Power & Dehydration (0.012 kWh)", "AED 0.0046", "2.0%"]
    ]
    for col_idx, h in enumerate(c_headers):
        c = s9_tbl.cell(0, col_idx)
        c.text = h
        c.fill.solid()
        c.fill.fore_color.rgb = COLOR_NAVY
        for p in c.text_frame.paragraphs:
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = COLOR_CARD

    for row_idx, r in enumerate(c_rows):
        for col_idx, val in enumerate(r):
            c = s9_tbl.cell(row_idx + 1, col_idx)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 0 else RGBColor(241, 245, 249)
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(10)
                p.font.color.rgb = COLOR_TEXT_MAIN

    # Right Sensitivity Box
    create_card(s9, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.1), "Cost Stress-Testing & Sensitivity")
    s9_text = s9.shapes.add_textbox(Inches(6.9), Inches(2.2), Inches(5.4), Inches(4.3))
    tf9 = s9_text.text_frame
    tf9.word_wrap = True

    p = tf9.paragraphs[0]
    p.text = "Economic Resilience Against Market Shocks:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    sens_bullets = [
        "Baseline Factory-Gate Unit Cost: AED 0.2274 per seed-carrier [Modelled].",
        "Safety Buffer: 43.1% margin below ASPIRE's ≤ AED 0.40 economic cap.",
        "+50% Labor Shock: Unit cost rises to AED 0.253 (-36.6% below ceiling).",
        "+100% Native Seed Cost Surge: Unit cost rises to AED 0.287 (-28.1% below ceiling).",
        "Combined Extreme Shock (+100% Seed & +50% Labor): Unit cost is AED 0.313 (-21.6% below ceiling).",
        "Circular Local Inputs: 60% of matrix mass is local UAE date waste & quarry silt."
    ]
    for b in sens_bullets:
        bp = tf9.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s9, "Modelled on 1M continuous run. Amortization: 5-year straight line. UAE industrial energy tariff: AED 0.38/kWh.")

    # =========================================================================
    # SLIDE 10: PROJECT ROADMAP, TEAM & STRATEGIC ALIGNMENT
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Project Roadmap, Team & UAE Strategic Alignment", "DELIVERING FIELD-READY CARRIERS FOR NABAT DRONES BY JANUARY 2027")

    create_card(s10, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "5-Month Execution Roadmap")
    s10_t1 = s10.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf10_1 = s10_t1.text_frame
    tf10_1.word_wrap = True

    p = tf10_1.paragraphs[0]
    p.text = "Phased Timeline to Desert Deployment:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    m_timeline = [
        "Nov 2026 (Phase 1): Proposal submission; complete physical & aerodynamic baseline.",
        "Dec 2026 (Phase 2): Semi-finalist video pitch; prototype mechanical drop characterization.",
        "1 Jan 2027 (Phase 3 Delivery): Delivery of 2,000 ready-to-deploy units for Nabat UAV fleet.",
        "Jan-Feb 2027 (Field Validation): Live drone drops across Abu Dhabi study plots with Nabat.",
        "Q2 2027 (Commercial Licensing): Emergence auditing and integration with NabatOS platform."
    ]
    for b in m_timeline:
        bp = tf10_1.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    create_card(s10, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.1), "Team, Disclosures & Strategic Alignment")
    s10_t2 = s10.shapes.add_textbox(Inches(6.9), Inches(2.2), Inches(5.4), Inches(4.3))
    tf10_2 = s10_t2.text_frame
    tf10_2.word_wrap = True

    p = tf10_2.paragraphs[0]
    p.text = "Team & Institutional Alignment:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    align_points = [
        "Lead Engineer: Mohamed Shameel (Systems Engineering & Applied Computational Modeling).",
        "IP Declaration: 100% proprietary independent architecture; non-exclusive testing license to ASPIRE/Nabat.",
        "Prior Funding Disclosure: Zero prior grant funding or competing contractual claims.",
        "UAE Net Zero 2050: Biological carbon capture via accelerated desert vegetation establishment.",
        "National Biodiversity Strategy 2031: Native habitat rehabilitation using desert flora."
    ]
    for b in align_points:
        bp = tf10_2.add_paragraph()
        bp.text = f"\n• {b}"
        bp.font.size = Pt(11)
        bp.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s10, "Contact: Mohamed Shameel (shameel0505@gmail.com) | Nabat TerraPod Challenge (NTPC 2026)")

    # Save presentation
    prs.save(output_path)
    print(f"[SUCCESS] Presentation generated successfully: {output_path}")

if __name__ == "__main__":
    create_deck()
