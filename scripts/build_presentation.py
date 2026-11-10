"""
Nabat TerraPod Challenge - Phase 1 Technical Proposal Deck Generator
Executive Deep-Tech Presentation Deck (16:9 Widescreen)
Designed for ASPIRE / ATRC Abu Dhabi & Nabat AI Technologies.
Clean, modern, human-readable executive presentation: high visual impact, clear storytelling, zero number clutter.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path="Nabat_TerraPod_Proposal_Shameel.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # --- Modern Executive Color Palette ---
    COLOR_BG = RGBColor(248, 250, 252)          # Ultra-light slate (#F8FAFC)
    COLOR_WHITE = RGBColor(255, 255, 255)       # Pure White
    COLOR_BORDER = RGBColor(226, 232, 240)      # Slate 200 border (#E2E8F0)
    COLOR_NAVY = RGBColor(15, 23, 42)           # Deep slate navy (#0F172A)
    COLOR_NAVY_LIGHT = RGBColor(30, 41, 59)     # Slate 800 (#1E293B)
    COLOR_EMERALD = RGBColor(5, 150, 105)       # Emerald (#059669)
    COLOR_GOLD = RGBColor(217, 119, 6)          # Amber / Desert Gold (#D97706)
    COLOR_RED = RGBColor(225, 29, 72)           # Warning Rose (#E11D48)
    COLOR_MUTED = RGBColor(100, 116, 139)       # Slate 500 (#64748B)
    COLOR_LIGHT = RGBColor(148, 163, 184)       # Slate 400 (#94A3B8)

    # --- Helper Layout Functions ---
    def set_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category="NABAT TERRAPOD CHALLENGE | ASPIRE & ATRC"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.28))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_GOLD

        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.733), Inches(0.55))
        tf = t_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(21)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.015))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BORDER
        line.line.fill.background()

    def add_footer(slide, text="Lead Innovator: Mohamed Shameel (shameel0505@gmail.com) | ChallengeON Track: NTPC 2026"):
        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.3))
        tf = f_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(8.5)
        p.font.color.rgb = COLOR_LIGHT

    def create_card(slide, left, top, width, height, bg_color=COLOR_WHITE, border_color=COLOR_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    def add_hero_stat(slide, left, top, width, height, big_num, label, desc="", accent_col=COLOR_EMERALD):
        create_card(slide, left, top, width, height, bg_color=COLOR_WHITE)
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = big_num
        p1.font.size = Pt(34)
        p1.font.bold = True
        p1.font.color.rgb = accent_col

        p2 = tf.add_paragraph()
        p2.text = label.upper()
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY
        p2.space_before = Pt(3)

        if desc:
            p3 = tf.add_paragraph()
            p3.text = desc
            p3.font.size = Pt(9.5)
            p3.font.color.rgb = COLOR_MUTED
            p3.space_before = Pt(4)

    def add_bottom_stat(slide, left, top, width, height, stat_value, stat_label, description, accent_col=COLOR_EMERALD):
        create_card(slide, left, top, width, height, bg_color=COLOR_WHITE)
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.12), width - Inches(0.4), height - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = stat_value
        p1.font.size = Pt(19)
        p1.font.bold = True
        p1.font.color.rgb = accent_col

        p2 = tf.add_paragraph()
        p2.text = stat_label.upper()
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = description
        p3.font.size = Pt(8.5)
        p3.font.color.rgb = COLOR_MUTED
        p3.space_before = Pt(2)

    # =========================================================================
    # SLIDE 1: COVER & EXECUTIVE SUMMARY
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)
    add_header(s1, "Nabat-BioDrop™: Biomimetic Rainwater-Harvesting Seed Carrier", "ASPIRE / ATRC ABU DHABI & NABAT AI TECHNOLOGIES")

    # Left Overview Card
    create_card(s1, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.35))
    tb_s1 = s1.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(4.75))
    tf1 = tb_s1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "High-Performance Carrier for Autonomous UAV Seeding"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p2 = tf1.add_paragraph()
    p2.text = "\nNabat-BioDrop™ solves the fundamental bottlenecks of desert aerial restoration. Engineered specifically for UAE dune environments, it transforms bare sand into a protective micro-incubator using biomimetic geometry and natural local minerals."
    p2.font.size = Pt(11)
    p2.font.color.rgb = COLOR_MUTED

    p3 = tf1.add_paragraph()
    p3.text = "\nCore Engineering Breakthroughs:"
    p3.font.size = Pt(11.5)
    p3.font.bold = True
    p3.font.color.rgb = COLOR_NAVY

    pillars = [
        "Self-Anchoring Ovoid: Stops wind roll and sand burial in Shamal winds.",
        "Concave Rain Funnel: Concentrates scarce rainfall directly into the seed nest.",
        "Kaolin Solar Shield: Reflects desert heat to keep embryos safe from scorching.",
        "Water-Soluble Keel: Softens on wetting so baby roots easily penetrate sand.",
        "100% Bio-Composite: Made from local date palm biochar and natural clay."
    ]
    for pil in pillars:
        bp = tf1.add_paragraph()
        bp.text = f"•  {pil}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(4)

    # Right Hero Stat Grid (4 Big Stat Cards)
    add_hero_stat(s1, Inches(6.7), Inches(1.55), Inches(2.8), Inches(2.55), "−33°C", "Solar Protection", "White kaolin shield reflects desert sun, keeping the seed nest at 41°C.", COLOR_GOLD)
    add_hero_stat(s1, Inches(9.7), Inches(1.55), Inches(2.8), Inches(2.55), "5x", "Rainwater Harvesting", "Concave funnel directs 100% of intercepted rain straight to the embryo.", COLOR_EMERALD)
    add_hero_stat(s1, Inches(6.7), Inches(4.35), Inches(2.8), Inches(2.55), "2,550", "Pods / Drone Flight", "Ultralight 9.8g profile doubles 25kg drone flight coverage vs. heavy pucks.", COLOR_NAVY)
    add_hero_stat(s1, Inches(9.7), Inches(4.35), Inches(2.8), Inches(2.55), "AED 0.23", "Unit Cost", "43% below ASPIRE's AED 0.40 ceiling, providing a strong safety budget margin.", COLOR_EMERALD)

    add_footer(s1)

    # =========================================================================
    # SLIDE 2: THE ARID RESTORATION CHALLENGE (3 CORE FAILURE MODES)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_header(s2, "The Arid Challenge: Why Conventional Aerial Seeding Fails", "FIELD FAILURE MECHANISMS IN HYPER-ARID DESERTS")

    traps = [
        ("☀️  MIDDAY HEAT SCORCHING",
         "Surface Heat Exceeds 65°C",
         "Naked seeds and dark biochar pellets absorb intense solar radiation. Above 42°C, plant embryos suffer irreversible protein denaturation, killing the seed before it can sprout.",
         COLOR_RED),
        ("💧  CONVEX WATER SHEDDING",
         "Scarce Rain Is Diverted Away",
         "Standard spherical and dome pellets shed over 80% of scarce rain into the surrounding sand. The water quickly evaporates in dry desert air, leaving the seed completely dehydrated.",
         COLOR_GOLD),
        ("🪨  THE 'CONCRETE TOMB'",
         "Hardened Clay Traps Emerging Roots",
         "Standard clay pellets dry into rock-hard clods (>2.5 MPa). Baby radicles exert only 0.8–1.2 MPa of turgor pressure—meaning seeds germinate inside but are trapped and perish.",
         COLOR_NAVY)
    ]

    card_w = Inches(3.7)
    for i, (tag, headline, desc, acc_col) in enumerate(traps):
        cx = Inches(0.8) + i * Inches(4.0)
        create_card(s2, cx, Inches(1.55), card_w, Inches(4.0))

        tb = s2.shapes.add_textbox(cx + Inches(0.25), Inches(1.85), card_w - Inches(0.5), Inches(3.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = tag
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf.add_paragraph()
        p2.text = f"\n{headline}"
        p2.font.size = Pt(13.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY

        p3 = tf.add_paragraph()
        p3.text = f"\n{desc}"
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = COLOR_MUTED

    # Bottom Takeaway Card
    create_card(s2, Inches(0.8), Inches(5.75), Inches(11.733), Inches(1.15))
    tb_b = s2.shapes.add_textbox(Inches(1.1), Inches(5.88), Inches(11.1), Inches(0.85))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p_b1 = tf_b.paragraphs[0]
    p_b1.text = "THE ENGINEERING IMPERATIVE:"
    p_b1.font.size = Pt(10)
    p_b1.font.bold = True
    p_b1.font.color.rgb = COLOR_GOLD

    p_b2 = tf_b.add_paragraph()
    p_b2.text = "Conventional seed balls fail because they treat the desert like farmland. A winning carrier must actively reflect midday solar radiation, concentrate rare raindrops, and guarantee an easy root exit into damp sand."
    p_b2.font.size = Pt(10.5)
    p_b2.font.color.rgb = COLOR_NAVY
    p_b2.space_before = Pt(2)

    add_footer(s2)

    # =========================================================================
    # SLIDE 3: AERODYNAMIC FORM FACTOR: DESIGNED FOR THE DRONE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_header(s3, "Aerodynamic Form Factor: Eliminating Wind Drift & Sand Rolling", "OPTIMIZED FOR HIGH-SPEED CONTINUOUS UAV BROADCAST")

    # Left: Conventional Sphere
    create_card(s3, Inches(0.8), Inches(1.55), Inches(5.6), Inches(4.0))
    tb_sp = s3.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(3.4))
    tf_sp = tb_sp.text_frame
    tf_sp.word_wrap = True

    p = tf_sp.paragraphs[0]
    p.text = "CONVENTIONAL SPHERE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_RED

    p_sp_sub = tf_sp.add_paragraph()
    p_sp_sub.text = "High Wind Drift & Uncontrolled Rolling"
    p_sp_sub.font.size = Pt(14)
    p_sp_sub.font.bold = True
    p_sp_sub.font.color.rgb = COLOR_NAVY

    sp_points = [
        "High Air Drag: Spherical profile gets blown off-course by crosswinds, spreading seeds unpredictably away from target restoration zones.",
        "Endless Dune Rolling: Round balls roll continuously across loose sand under common 35 km/h Shamal winds.",
        "Deep Burial & Suffocation: Rolling pods settle into dune hollows and get buried under 20–50 cm of sand, permanently cutting off light and air."
    ]
    for pt in sp_points:
        bp = tf_sp.add_paragraph()
        bp.text = f"\n✕  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Right: Nabat-BioDrop Ovoid
    create_card(s3, Inches(6.7), Inches(1.55), Inches(5.8), Inches(4.0))
    tb_ov = s3.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.2), Inches(3.4))
    tf_ov = tb_ov.text_frame
    tf_ov.word_wrap = True

    p = tf_ov.paragraphs[0]
    p.text = "NABAT-BIODROP™ OVOID"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    p_ov_sub = tf_ov.add_paragraph()
    p_ov_sub.text = "Streamlined Stability & Upright Sand Anchoring"
    p_ov_sub.font.size = Pt(14)
    p_ov_sub.font.bold = True
    p_ov_sub.font.color.rgb = COLOR_NAVY

    ov_points = [
        "Low Aerodynamic Drag: Streamlined ovoid shape cuts through desert crosswinds, reducing lateral flight drift by 27% during 5 m/s drone broadcast.",
        "Passive Self-Righting: Weighted lower keel (center of gravity at 35%) ensures the heavy base leads during flight and hits the ground first.",
        "Self-Anchoring Impact: Drops into loose sand and penetrates 10 mm on impact, locking the pod upright and completely stopping wind roll."
    ]
    for pt in ov_points:
        bp = tf_ov.add_paragraph()
        bp.text = f"\n✓  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_NAVY_LIGHT

    # Bottom Stat Row
    add_bottom_stat(s3, Inches(0.8), Inches(5.75), Inches(3.7), Inches(1.15), "29.0 × 26.5 mm", "Challenge Envelope", "Strictly compliant with ASPIRE 25–30 mm limit.", COLOR_NAVY)
    add_bottom_stat(s3, Inches(4.8), Inches(5.75), Inches(3.7), Inches(1.15), "−27% Drift", "Tighter Dispersion", "Concentrates seed drop along target drone flight lines.", COLOR_EMERALD)
    add_bottom_stat(s3, Inches(8.8), Inches(5.75), Inches(3.7), Inches(1.15), "10 mm Anchor", "Wind Roll Immunity", "Locks upright into dune sand; resists Shamal winds.", COLOR_EMERALD)

    add_footer(s3)

    # =========================================================================
    # SLIDE 4: THERMAL ALBEDO SHIELD: SURVIVING MIDDAY HEAT
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_header(s4, "Solar Defense: Reflecting Desert Heat to Save Embryos", "HIGH-ALBEDO KAOLIN MINERAL COATING REDUCES SURFACE TEMPERATURE BY 33°C")

    # Left: Explanation Card
    create_card(s4, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.35))
    tb_th = s4.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(4.75))
    tf_th = tb_th.text_frame
    tf_th.word_wrap = True

    p = tf_th.paragraphs[0]
    p.text = "The Overheating Trap vs. The Solar Shield"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_th2 = tf_th.add_paragraph()
    p_th2.text = "\nUnshaded desert sand and dark biochar absorb over 90% of solar radiation. Under UAE midday sun (1,000 W/m²), surface temperatures soar to 75°C."
    p_th2.font.size = Pt(10.5)
    p_th2.font.color.rgb = COLOR_MUTED

    p_th3 = tf_th.add_paragraph()
    p_th3.text = "\nLethal Biological Threshold: Seed embryos suffer permanent heat damage and denaturation when sustained temperatures cross 42°C."
    p_th3.font.size = Pt(10.5)
    p_th3.font.bold = True
    p_th3.font.color.rgb = COLOR_RED

    p_th4 = tf_th.add_paragraph()
    p_th4.text = "\nThe Solution: Nabat-BioDrop™ is coated with a reflective outer layer of high-purity Kaolin clay (78% solar reflectance). By reflecting infrared heat, surface temperature drops to 41.4°C—keeping seeds safely alive in their natural comfort zone."
    p_th4.font.size = Pt(10.5)
    p_th4.font.color.rgb = COLOR_NAVY_LIGHT

    # Right: Hero Stat Contrast (2 Cards)
    add_hero_stat(s4, Inches(6.7), Inches(1.55), Inches(2.8), Inches(2.55), "74.7°C", "Uncoated Biochar", "Absorbs solar heat; lethal to delicate seed embryos.", COLOR_RED)
    add_hero_stat(s4, Inches(9.7), Inches(1.55), Inches(2.8), Inches(2.55), "41.4°C", "Kaolin Solar Shield", "Reflects 78% of heat; embryo stays safe and viable.", COLOR_EMERALD)

    # Bottom Right: 100% Bio-Composite Card
    create_card(s4, Inches(6.7), Inches(4.35), Inches(5.8), Inches(2.55))
    tb_mat = s4.shapes.add_textbox(Inches(7.0), Inches(4.55), Inches(5.2), Inches(2.15))
    tf_mat = tb_mat.text_frame
    tf_mat.word_wrap = True

    p = tf_mat.paragraphs[0]
    p.text = "100% Natural UAE Formulation (Zero Microplastics)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    mats = [
        "Date Palm Waste Biochar (32%): High carbon water retention and porous matrix.",
        "Calcium Bentonite Clay (28%): Natural mineral binder providing core stability.",
        "Kaolin Mineral Shield (20%): Outer white reflective layer for heat defense.",
        "Cold-Soluble Gum Arabic (12%): Rapid-dissolving natural plant binder.",
        "Carnauba Wax Seal (2%): Pure plant lipid barrier repelling morning dew."
    ]
    for m in mats:
        bp = tf_mat.add_paragraph()
        bp.text = f"•  {m}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(2)

    add_footer(s4)

    # =========================================================================
    # SLIDE 5: HYDROLOGICAL CATCHMENT & DEW SUPPRESSION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_header(s5, "Hydrological Architecture: Harvesting Rain & Repelling Dew", "CONCAVE FUNNEL WATER CONCENTRATION & TIMED RAIN ACTIVATION")

    # Left: The 12mm Concave Funnel
    create_card(s5, Inches(0.8), Inches(1.55), Inches(5.6), Inches(4.0))
    tb_f = s5.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(3.4))
    tf_f = tb_f.text_frame
    tf_f.word_wrap = True

    p = tf_f.paragraphs[0]
    p.text = "12mm Concave Rainwater Funnel"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_sub = tf_f.add_paragraph()
    p_sub.text = "Concentrating Rain Directly into the Seed Nest"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_EMERALD

    f_points = [
        "Concave Aperture: A 12 mm inward-sloping crater designed to catch and funnel rainwater straight down to the seed embryo.",
        "5x Water Concentration: In a typical 5 mm desert rain shower, the funnel gathers 0.56 mL of liquid water right into the core.",
        "Zero Runoff Waste: Convex pellets shed water outwards into dry sand; BioDrop™ channels 100% of intercepted rain inward.",
        "Natural Sand Mulch: Windblown sand gently fills the funnel, forming a protective blanket that traps humidity and blocks evaporation."
    ]
    for pt in f_points:
        bp = tf_f.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Right: The Carnauba Wax Dew Barrier
    create_card(s5, Inches(6.7), Inches(1.55), Inches(5.8), Inches(4.0))
    tb_w = s5.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.2), Inches(3.4))
    tf_w = tb_w.text_frame
    tf_w.word_wrap = True

    p = tf_w.paragraphs[0]
    p.text = "Smart Dew Shield (Timed Activation)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_w_sub = tf_w.add_paragraph()
    p_w_sub.text = "Preventing Fatal False Germination"
    p_w_sub.font.size = Pt(11)
    p_w_sub.font.bold = True
    p_w_sub.font.color.rgb = COLOR_GOLD

    w_points = [
        "The Morning Dew Trap: Light morning dew (0.2 mm) hydrates seeds, but vanishes in 90 minutes of desert sun—baking sprouted embryos.",
        "High-Melting Carnauba (85°C): Unlike beeswax (which melts at 62°C in summer sand), carnauba stays solid in extreme desert heat.",
        "Threshold Protection: The hydrophobic seal repels light morning moisture, keeping seeds safely dormant during dry spells.",
        "Rainstorm Activation: A genuine rainfall (≥ 5 mm) overcomes the threshold, penetrating the core and triggering active germination."
    ]
    for pt in w_points:
        bp = tf_w.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Bottom Stat Row
    add_bottom_stat(s5, Inches(0.8), Inches(5.75), Inches(3.7), Inches(1.15), "0.56 mL", "Rain Harvested / Pod", "Gathered directly into the seed nest in a 5mm rain.", COLOR_EMERALD)
    add_bottom_stat(s5, Inches(4.8), Inches(5.75), Inches(3.7), Inches(1.15), "82–86°C", "Wax Melting Point", "Pure Carnauba resists intense summer sand heat.", COLOR_NAVY)
    add_bottom_stat(s5, Inches(8.8), Inches(5.75), Inches(3.7), Inches(1.15), "≥ 5 mm", "Rain Activation", "Sprouts only when real soil moisture is sufficient.", COLOR_GOLD)

    add_footer(s5)

    # =========================================================================
    # SLIDE 6: ROOT MECHANICAL FREEDOM & NURSE GUILD ECOLOGY
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_header(s6, "Biological Emergence: Fast-Dissolving Keel & Nurse Ecology", "PREVENTING ROOT ENTRAPMENT & ACCELERATING NATIVE ESTABLISHMENT")

    # Left: Water-Soluble Keel
    create_card(s6, Inches(0.8), Inches(1.55), Inches(5.6), Inches(4.0))
    tb_k = s6.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(3.4))
    tf_k = tb_k.text_frame
    tf_k.word_wrap = True

    p = tf_k.paragraphs[0]
    p.text = "Water-Soluble Root Escape Keel"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_k_sub = tf_k.add_paragraph()
    p_k_sub.text = "Eliminating the 'Concrete Tomb' Problem"
    p_k_sub.font.size = Pt(11)
    p_k_sub.font.bold = True
    p_k_sub.font.color.rgb = COLOR_EMERALD

    k_points = [
        "Fragile Baby Roots: An emerging radicle exerts a maximum pushing force of only 0.8–1.2 MPa.",
        "The Hard Shell Trap: Standard dried clay shells exceed 2.5 MPa, physically trapping and killing emerging roots inside.",
        "Fast-Dissolve Gum Arabic: Formulated with 12% cold-soluble plant gum. Rainwater dissolves the binder within 20 minutes.",
        "Effortless Exit: Matrix resistance drops to near zero (<0.12 MPa), letting the baby root push straight down into moist sand."
    ]
    for pt in k_points:
        bp = tf_k.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Right: Synergistic Nurse Guild
    create_card(s6, Inches(6.7), Inches(1.55), Inches(5.8), Inches(4.0))
    tb_ng = s6.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.2), Inches(3.4))
    tf_ng = tb_ng.text_frame
    tf_ng.word_wrap = True

    p = tf_ng.paragraphs[0]
    p.text = "Native Nurse Guild Ecology"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_ng_sub = tf_ng.add_paragraph()
    p_ng_sub.text = "Two-Stage Plant Succession for UAE Deserts"
    p_ng_sub.font.size = Pt(11)
    p_ng_sub.font.bold = True
    p_ng_sub.font.color.rgb = COLOR_GOLD

    ng_points = [
        "Pioneer Nurse Grass (Stipagrostis plumosa): Fast starter; germinates in 48 hours to create surface root nets that lock shifting sand.",
        "Climax Shrub (Haloxylon salicornicum): Slower starter; takes shelter in the grass's microclimate and grows deep perennial roots.",
        "Diffuse Light Veil: A semi-translucent mineral cover filters 10–20% of sunlight—activating seed growth without scorching.",
        "Aerated Porosity: Open pore channels guarantee oxygen supply, preventing seed suffocation during wet spells."
    ]
    for pt in ng_points:
        bp = tf_ng.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Bottom Stat Row
    add_bottom_stat(s6, Inches(0.8), Inches(5.75), Inches(3.7), Inches(1.15), "20 Mins", "Keel Dissolution Speed", "Rapid softening upon contact with rainwater.", COLOR_EMERALD)
    add_bottom_stat(s6, Inches(4.8), Inches(5.75), Inches(3.7), Inches(1.15), "< 0.12 MPa", "Wet Shear Resistance", "Far below root strength; zero barrier to exit.", COLOR_NAVY)
    add_bottom_stat(s6, Inches(8.8), Inches(5.75), Inches(3.7), Inches(1.15), "2-Stage Guild", "Ecological Succession", "Pioneer grass stabilizes sand for climax shrubs.", COLOR_GOLD)

    add_footer(s6)

    # =========================================================================
    # SLIDE 7: EMPIRICAL VALIDATION PROTOCOL
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7)
    add_header(s7, "Solution Readiness: Empirical Validation Protocol", "PROGRESSION FROM FIRST-PRINCIPLES MODELING TO ABU DHABI FIELD TRIALS")

    stages = [
        ("STAGE 1: BENCH CHARACTERIZATION",
         "Physical & Mechanical Auditing",
         [
             "Dimensional Audit (n=20): Caliper check ensuring all axes fit 25–30 mm limit.",
             "Compressive Strength (n=10): Digital force gauge benchmark targeting >50 N strength.",
             "15m Sand Drop Test (n=30): Validating ≥95% survival and 10 mm self-anchoring."
         ],
         COLOR_NAVY),
        ("STAGE 2: LABORATORY PROXY ASSAYS",
         "Germination & Moisture Verification",
         [
             "Fast Arid Proxy (Lepidium sativum): 24-hour emergence benchmark for rapid testing.",
             "Comparative Assays (4×25 seeds): Pod-encapsulated vs. bare seeds under stress.",
             "Dissolution Auditing: Confirming keel softens within 20 minutes in water."
         ],
         COLOR_GOLD),
        ("STAGE 3: PHASE 3 UAV FIELD TRIALS",
         "Operational Desert Revegetation",
         [
             "Pilot Production: Compounding 2,000 ready-to-deploy units for Nabat drone fleet.",
             "Abu Dhabi Flight Validation: Dispensing at 5 m/s cruise across restoration plots.",
             "Long-Term Monitoring: Tracking seedling emergence and dune stabilization."
         ],
         COLOR_EMERALD)
    ]

    card_w = Inches(3.7)
    for i, (stage_tag, stage_title, bullets, acc_col) in enumerate(stages):
        cx = Inches(0.8) + i * Inches(4.0)
        create_card(s7, cx, Inches(1.55), card_w, Inches(4.0))

        tb = s7.shapes.add_textbox(cx + Inches(0.25), Inches(1.85), card_w - Inches(0.5), Inches(3.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = stage_tag
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf.add_paragraph()
        p2.text = f"\n{stage_title}"
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY

        for b in bullets:
            bp = tf.add_paragraph()
            bp.text = f"\n•  {b}"
            bp.font.size = Pt(10)
            bp.font.color.rgb = COLOR_MUTED

    # Bottom Protocol Summary
    create_card(s7, Inches(0.8), Inches(5.75), Inches(11.733), Inches(1.15))
    tb_b7 = s7.shapes.add_textbox(Inches(1.1), Inches(5.88), Inches(11.1), Inches(0.85))
    tf_b7 = tb_b7.text_frame
    tf_b7.word_wrap = True
    p_b7_1 = tf_b7.paragraphs[0]
    p_b7_1.text = "PHASE 1 SCIENTIFIC COMPLIANCE:"
    p_b7_1.font.size = Pt(10)
    p_b7_1.font.bold = True
    p_b7_1.font.color.rgb = COLOR_EMERALD

    p_b7_2 = tf_b7.add_paragraph()
    p_b7_2.text = "In full accordance with Phase 1 proposal guidelines, all baseline calculations are grounded in peer-reviewed UAE desert ecology and physics. Physical bench validation begins immediately upon Phase 2 selection."
    p_b7_2.font.size = Pt(10.5)
    p_b7_2.font.color.rgb = COLOR_NAVY
    p_b7_2.space_before = Pt(2)

    add_footer(s7)

    # =========================================================================
    # SLIDE 8: INDUSTRIAL SCALABILITY & NABAT UAV COMPATIBILITY
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8)
    add_header(s8, "Industrial Scalability: 50,000 Pods / Day & High Drone Coverage", "CONTINUOUS DISC AGGLOMERATION & EAD ABU DHABI DENSITY INTEGRATION")

    # Left: Scalable Manufacturing Flow
    create_card(s8, Inches(0.8), Inches(1.55), Inches(5.6), Inches(4.0))
    tb_m = s8.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(3.4))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    p = tf_m.paragraphs[0]
    p.text = "High-Volume Production Flow"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_m_sub = tf_m.add_paragraph()
    p_m_sub.text = "Continuous Industrial Disc Granulation"
    p_m_sub.font.size = Pt(11)
    p_m_sub.font.bold = True
    p_m_sub.font.color.rgb = COLOR_EMERALD

    flow_pts = [
        "Continuous Disc Granulation: Scaled on standard 2.2 m industrial disc granulators (45° tilt, 18 RPM) fitted with concave forming tooling.",
        "Single-Step Forming: Continuous pan agglomeration followed by rotary mineral coating avoids expensive molds or manual multi-part assembly.",
        "High Line Throughput: One continuous line produces 50,000 pods per day (1.2 tonnes/day), easily meeting regional restoration demands.",
        "Embryo-Safe Dehydration: Fluidized bed drying at 38°C preserves seed embryo viability and beneficial mycorrhizal spores."
    ]
    for pt in flow_pts:
        bp = tf_m.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Right: Drone Payload & Hectare Impact
    create_card(s8, Inches(6.7), Inches(1.55), Inches(5.8), Inches(4.0))
    tb_d = s8.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.2), Inches(3.4))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True

    p = tf_d.paragraphs[0]
    p.text = "Drone Payload & Hectare Coverage"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_d_sub = tf_d.add_paragraph()
    p_d_sub.text = "Grounded in EAD Abu Dhabi Field Trials"
    p_d_sub.font.size = Pt(11)
    p_d_sub.font.bold = True
    p_d_sub.font.color.rgb = COLOR_GOLD

    d_pts = [
        "2,550 Pods per Flight: At 9.8 g unit mass, a standard 25 kg payload UAV carries 2,550 pods (+155% more than heavy 25 g pucks).",
        "Rangeland Restoration: 1,500 pods/ha achieves 300–500 mature shrubs/ha at a low carrier cost of AED 340.50/ha.",
        "Dune Stabilization: 4,500 pods/ha locks moving sand at AED 1,021.50/ha (matching EAD's 6.5M seed trial in Abu Dhabi).",
        "Sortie Coverage: A single drone flight restores 1.7 hectares of rangeland or 0.6 hectares of critical sand dunes."
    ]
    for pt in d_pts:
        bp = tf_d.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Bottom Stat Row
    add_bottom_stat(s8, Inches(0.8), Inches(5.75), Inches(3.7), Inches(1.15), "50,000", "Pods / Day / Line", "Continuous industrial granulator throughput.", COLOR_NAVY)
    add_bottom_stat(s8, Inches(4.8), Inches(5.75), Inches(3.7), Inches(1.15), "2,550", "Pods per 25kg UAV", "+155% payload capacity vs. heavy 25g pellets.", COLOR_EMERALD)
    add_bottom_stat(s8, Inches(8.8), Inches(5.75), Inches(3.7), Inches(1.15), "1.7 ha", "Coverage per Flight", "In rangeland restoration (1,500 pods/ha).", COLOR_GOLD)

    add_footer(s8)

    # =========================================================================
    # SLIDE 9: TECHNO-ECONOMIC VIABILITY: AED 0.23 PER CARRIER
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9)
    add_header(s9, "Techno-Economic Viability: AED 0.23 per Carrier", "43% SAFETY MARGIN BELOW THE ASPIRE AED 0.40 CEILING")

    # Left: Big Cost Callout & Summary
    create_card(s9, Inches(0.8), Inches(1.55), Inches(5.6), Inches(4.0))
    tb_c = s9.shapes.add_textbox(Inches(1.1), Inches(1.85), Inches(5.0), Inches(3.4))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True

    p = tf_c.paragraphs[0]
    p.text = "Unit Cost Breakdown (At 1,000,000 Units)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_c2 = tf_c.add_paragraph()
    p_c2.text = "\nBy upcycling local date palm agricultural waste and domestic bentonite clay, the factory-gate manufacturing cost is just AED 0.23 per seed carrier."
    p_c2.font.size = Pt(10.5)
    p_c2.font.color.rgb = COLOR_MUTED

    p_c3 = tf_c.add_paragraph()
    p_c3.text = "\nThis delivers a massive 43% safety margin below ASPIRE's AED 0.40 ceiling—ensuring economic feasibility even under future raw material price spikes."
    p_c3.font.size = Pt(10.5)
    p_c3.font.bold = True
    p_c3.font.color.rgb = COLOR_EMERALD

    p_c4 = tf_c.add_paragraph()
    p_c4.text = "\n•  Raw Materials: AED 0.10 (Biochar, clay, kaolin, gum, and seeds)\n•  Labor & Conversion: AED 0.05 (Automated continuous production)\n•  Capex & Packaging: AED 0.08 (Plant depreciation & bulk jute bagging)"
    p_c4.font.size = Pt(10)
    p_c4.font.color.rgb = COLOR_NAVY_LIGHT

    # Right Top: Hero Cost Comparison Cards
    add_hero_stat(s9, Inches(6.7), Inches(1.55), Inches(2.8), Inches(2.1), "AED 0.23", "Nabat-BioDrop™ Cost", "Fully itemized factory-gate production cost.", COLOR_EMERALD)
    add_hero_stat(s9, Inches(9.7), Inches(1.55), Inches(2.8), Inches(2.1), "AED 0.40", "ASPIRE Ceiling Cap", "Maximum allowed cost ceiling in challenge brief.", COLOR_NAVY)

    # Right Bottom: Resilience Card
    create_card(s9, Inches(6.7), Inches(3.85), Inches(5.8), Inches(1.7))
    tb_res = s9.shapes.add_textbox(Inches(7.0), Inches(4.0), Inches(5.2), Inches(1.4))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True

    p = tf_res.paragraphs[0]
    p.text = "Financial Sensitivity & Shock Resistance"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    shocks = [
        "+50% Labor Spike: Unit cost rises to AED 0.25 (Still −36% below ceiling).",
        "+100% Seed Price Shock: Unit cost rises to AED 0.29 (Still −28% below ceiling).",
        "Extreme Combined Shock: Model survives up to +150% native seed price surges."
    ]
    for sh in shocks:
        bp = tf_res.add_paragraph()
        bp.text = f"•  {sh}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(2)

    # Bottom Stat Row
    add_bottom_stat(s9, Inches(0.8), Inches(5.75), Inches(3.7), Inches(1.15), "−43%", "Budget Margin", "17 fils buffer per carrier below ASPIRE cap.", COLOR_EMERALD)
    add_bottom_stat(s9, Inches(4.8), Inches(5.75), Inches(3.7), Inches(1.15), "AED 340 / ha", "Rangeland Cost", "At 1,500 pods/ha operational seeding density.", COLOR_NAVY)
    add_bottom_stat(s9, Inches(8.8), Inches(5.75), Inches(3.7), Inches(1.15), "+150%", "Seed Shock Resilience", "Remains fully compliant under extreme price surges.", COLOR_GOLD)

    add_footer(s9)

    # =========================================================================
    # SLIDE 10: EXECUTION ROADMAP, TEAM & UAE ALIGNMENT
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10)
    add_header(s10, "Project Execution: Roadmap, Team & National Alignment", "DELIVERING 2,000 FIELD-READY SEED CARRIERS BY JANUARY 2027")

    # Top: 4-Step Milestone Flow Across the Slide
    m_boxes = [
        ("PHASE 1: PROPOSAL", "Nov 2026", "First-principles modeling, supplier mapping, and baseline design.", COLOR_NAVY),
        ("PHASE 2: LAB PROTOTYPE", "Dec 2026", "Semi-finalist video pitch, mechanical drop assays, and proxy tests.", COLOR_GOLD),
        ("PHASE 3: PILOT BATCH", "1 Jan 2027", "Delivery of 2,000 ready-to-deploy units to Nabat drone fleet.", COLOR_EMERALD),
        ("DESERT VALIDATION", "Q1 2027", "Live UAV drop trials and vegetation emergence auditing in Abu Dhabi.", COLOR_NAVY)
    ]

    mw = Inches(2.75)
    for i, (m_tag, m_date, m_desc, acc_col) in enumerate(m_boxes):
        mx = Inches(0.8) + i * Inches(2.98)
        create_card(s10, mx, Inches(1.55), mw, Inches(1.8))

        tb = s10.shapes.add_textbox(mx + Inches(0.15), Inches(1.7), mw - Inches(0.3), Inches(1.5))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = m_date
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf.add_paragraph()
        p2.text = m_tag
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = m_desc
        p3.font.size = Pt(9)
        p3.font.color.rgb = COLOR_MUTED
        p3.space_before = Pt(3)

    # Bottom Left: Team Profile
    create_card(s10, Inches(0.8), Inches(3.6), Inches(5.6), Inches(3.3))
    tb_tm = s10.shapes.add_textbox(Inches(1.1), Inches(3.85), Inches(5.0), Inches(2.8))
    tf_tm = tb_tm.text_frame
    tf_tm.word_wrap = True

    p = tf_tm.paragraphs[0]
    p.text = "Lead Innovator & Execution Model"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    t_pts = [
        "Lead Innovator: Mohamed Shameel (Independent Applied Engineering & Computational Modeling). Grassroots self-directed research with zero corporate overhead.",
        "Agile Execution: Rapid prototyping capability with direct access to domestic UAE material suppliers across Abu Dhabi, Dubai, and Sharjah.",
        "100% Clean IP: Proprietary independent architecture; non-exclusive testing rights granted to ASPIRE and Nabat AI Technologies.",
        "Zero Prior Encumbrance: Completely unencumbered solution with no competing grant or corporate restrictions."
    ]
    for pt in t_pts:
        bp = tf_tm.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    # Bottom Right: National Strategic Alignment
    create_card(s10, Inches(6.7), Inches(3.6), Inches(5.8), Inches(3.3))
    tb_al = s10.shapes.add_textbox(Inches(7.0), Inches(3.85), Inches(5.2), Inches(2.8))
    tf_al = tb_al.text_frame
    tf_al.word_wrap = True

    p = tf_al.paragraphs[0]
    p.text = "Strategic Alignment to UAE Vision"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    al_pts = [
        "UAE Net Zero 2050: Accelerated biological carbon sequestration through scalable dryland revegetation.",
        "National Biodiversity Strategy 2031: Large-scale habitat rehabilitation utilizing indigenous desert flora.",
        "Circular Bioeconomy: Upcycling date palm agricultural waste into high-tech ecological restoration carriers.",
        "Drone-First Restoration: Seamless integration with Nabat's autonomous UAV fleet for cost-effective national impact."
    ]
    for pt in al_pts:
        bp = tf_al.add_paragraph()
        bp.text = f"\n•  {pt}"
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_MUTED

    add_footer(s10, "Author: Mohamed Shameel (shameel0505@gmail.com) | NTPC 2026 Submission")

    # Save presentation
    prs.save(output_path)
    print(f"[SUCCESS] Modern executive presentation generated successfully: {output_path}")

if __name__ == "__main__":
    create_deck()
