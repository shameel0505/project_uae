"""
Nabat TerraPod Challenge - Phase 1 Technical Proposal Deck Generator
Executive Deep-Tech Presentation Deck (16:9 Widescreen)
Designed for ASPIRE / ATRC Abu Dhabi & Nabat AI Technologies.

Aesthetic Guidelines:
- Clean, authoritative deep-tech engineering styling.
- ZERO emojis. Clean alphanumeric tags and indices only (e.g. 01, 02, 03).
- Strict vertical space budgeting: NO overlapping text, NO collision between shapes.
- High visual hierarchy: Bold headers, comfortable line spacing, generous margins.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path="Nabat_TerraPod_Proposal_Shameel.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # --- Deep-Tech Executive Palette ---
    COLOR_BG = RGBColor(248, 250, 252)          # Light slate canvas (#F8FAFC)
    COLOR_CARD = RGBColor(255, 255, 255)        # Pure White card (#FFFFFF)
    COLOR_BORDER = RGBColor(226, 232, 240)      # Slate 200 border (#E2E8F0)
    COLOR_NAVY = RGBColor(15, 23, 42)           # Deep Slate Navy (#0F172A)
    COLOR_NAVY_LIGHT = RGBColor(30, 41, 59)     # Slate 800 (#1E293B)
    COLOR_EMERALD = RGBColor(4, 120, 87)        # Deep Emerald (#047857)
    COLOR_GOLD = RGBColor(180, 83, 9)           # Deep Amber/Gold (#B45309)
    COLOR_CRIMSON = RGBColor(190, 18, 60)       # Deep Rose/Crimson (#BE123C)
    COLOR_MUTED = RGBColor(71, 85, 105)         # Slate 600 (#475569)
    COLOR_LIGHT = RGBColor(148, 163, 184)       # Slate 400 (#94A3B8)
    COLOR_CARD_ALT = RGBColor(241, 245, 249)    # Slate 100 soft box (#F1F5F9)

    # --- Core Layout Helpers ---
    def set_canvas(slide):
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

    def create_card(slide, left, top, width, height, bg_color=COLOR_CARD, border_color=COLOR_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # =========================================================================
    # SLIDE 1: EXECUTIVE OVERVIEW & SYSTEM BREAKTHROUGHS
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_canvas(s1)
    add_header(s1, "Nabat-BioDrop: Biomimetic Rainwater-Harvesting Seed Carrier", "ASPIRE / ATRC ABU DHABI & NABAT AI TECHNOLOGIES")

    # Left Overview Card
    create_card(s1, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb_s1 = s1.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.7))
    tf1 = tb_s1.text_frame
    tf1.word_wrap = True

    p_tag = tf1.paragraphs[0]
    p_tag.text = "EXECUTIVE BRIEFING"
    p_tag.font.size = Pt(9.5)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_GOLD

    p_title = tf1.add_paragraph()
    p_title.text = "Autonomous UAV Desert Seed Carrier"
    p_title.font.size = Pt(15)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_NAVY
    p_title.space_before = Pt(3)

    p_desc = tf1.add_paragraph()
    p_desc.text = "Nabat-BioDrop solves the fundamental failure modes of aerial desert revegetation: wind drift, extreme surface heat (>65°C), convex rain shedding, and root entrapment. Engineered specifically for UAE dune environments using local biomaterials."
    p_desc.font.size = Pt(10.5)
    p_desc.font.color.rgb = COLOR_MUTED
    p_desc.space_before = Pt(6)

    p_break = tf1.add_paragraph()
    p_break.text = "Core Technical Pillars:"
    p_break.font.size = Pt(11)
    p_break.font.bold = True
    p_break.font.color.rgb = COLOR_NAVY
    p_break.space_before = Pt(8)

    pillars = [
        "Aerodynamic Ovoid: Self-anchoring weighted keel stops wind roll in Shamal winds.",
        "Concave Rain Funnel: Directs 100% of intercepted rain straight to the seed core.",
        "Kaolin Solar Shield: Reflects infrared radiation to keep seeds below lethal limits.",
        "Water-Soluble Keel: Softens on rain contact so baby roots penetrate sand effortlessly.",
        "100% Bio-Composite: Formulated from local date palm biochar and desert bentonite."
    ]
    for pil in pillars:
        bp = tf1.add_paragraph()
        bp.text = f"•  {pil}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(4)

    # Right Hero Stat Grid (4 Independent Fixed Cards)
    stat_data = [
        ("−33°C", "SOLAR PROTECTION", "White kaolin shield reflects desert sun, keeping the seed nest at 41°C.", COLOR_GOLD),
        ("5x", "RAINWATER HARVESTING", "Concave funnel directs 100% of intercepted rain straight to the embryo.", COLOR_EMERALD),
        ("2,550", "PODS / DRONE FLIGHT", "Ultralight 9.8g profile doubles 25kg drone flight coverage vs. heavy pucks.", COLOR_NAVY),
        ("AED 0.23", "UNIT FACTORY COST", "43% below ASPIRE's AED 0.40 ceiling, providing a robust safety margin.", COLOR_EMERALD)
    ]
    coords = [
        (Inches(6.7), Inches(1.55)),
        (Inches(9.7), Inches(1.55)),
        (Inches(6.7), Inches(4.25)),
        (Inches(9.7), Inches(4.25))
    ]
    for i, (b_num, b_lbl, b_txt, b_col) in enumerate(stat_data):
        cx, cy = coords[i]
        create_card(s1, cx, cy, Inches(2.8), Inches(2.5))
        tb = s1.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.2), Inches(2.4), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = b_num
        p1.font.size = Pt(32)
        p1.font.bold = True
        p1.font.color.rgb = b_col

        p2 = tf.add_paragraph()
        p2.text = b_lbl
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = b_txt
        p3.font.size = Pt(9)
        p3.font.color.rgb = COLOR_MUTED
        p3.space_before = Pt(4)

    add_footer(s1)

    # =========================================================================
    # SLIDE 2: THE 3 ARID RESTORATION FAILURE MODES (3 FULL COLUMNS)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_canvas(s2)
    add_header(s2, "The Arid Challenge: Why Conventional Aerial Seeding Fails", "FIELD FAILURE MECHANISMS IN HYPER-ARID SAND DUNES")

    traps = [
        ("01 / THERMAL HAZARD",
         "Midday Solar Scorching",
         "Surface sand exceeds 65°C under desert sun",
         [
             "Unshaded seeds and dark biochar absorb intense solar infrared radiation.",
             "Plant embryos suffer irreversible protein denaturation when sustained heat exceeds 42°C.",
             "Conventional dark seedballs bake and die before metabolic germination can initiate."
         ],
         "FAILURE: LETHAL EMBRYO HEAT SHOCK",
         COLOR_CRIMSON),
        ("02 / HYDROLOGICAL HAZARD",
         "Convex Rain Shedding",
         "Scarce rain runs off outward into dry sand",
         [
             "Standard spherical and dome pellets shed over 80% of scarce rain into surrounding sand.",
             "Surface moisture evaporates in under 90 minutes in dry air (VPD > 4.5 kPa).",
             "Seed core receives minimal hydration despite brief desert rainfall events."
         ],
         "FAILURE: DESICCATION BEFORE IMBIBITION",
         COLOR_GOLD),
        ("03 / MECHANICAL HAZARD",
         "The 'Concrete Tomb' Effect",
         "Sun-baked clay traps emerging radicles",
         [
             "Standard clay and bentonite binders dry into hard clods exceeding 2.5 MPa strength.",
             "Emerging plant radicles exert a maximum pushing force of only 0.8–1.2 MPa.",
             "Seedlings germinate inside the hardened crust but cannot penetrate out, dying trapped."
         ],
         "FAILURE: PHYSICAL ROOT ENTRAPMENT",
         COLOR_NAVY)
    ]

    col_w = Inches(3.7)
    for i, (tag, headline, sub, bullets, fail_lbl, acc_col) in enumerate(traps):
        cx = Inches(0.8) + i * Inches(4.0)
        create_card(s2, cx, Inches(1.55), col_w, Inches(5.2))

        tb = s2.shapes.add_textbox(cx + Inches(0.25), Inches(1.8), col_w - Inches(0.5), Inches(3.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = tag
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf.add_paragraph()
        p2.text = headline
        p2.font.size = Pt(13.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = sub
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = COLOR_MUTED
        p3.space_before = Pt(2)

        for b in bullets:
            bp = tf.add_paragraph()
            bp.text = f"•  {b}"
            bp.font.size = Pt(9.5)
            bp.font.color.rgb = COLOR_NAVY_LIGHT
            bp.space_before = Pt(6)

        # Bottom result box inside card
        create_card(s2, cx + Inches(0.25), Inches(5.95), col_w - Inches(0.5), Inches(0.6), bg_color=COLOR_CARD_ALT)
        tb_r = s2.shapes.add_textbox(cx + Inches(0.3), Inches(6.05), col_w - Inches(0.6), Inches(0.4))
        tf_r = tb_r.text_frame
        tf_r.word_wrap = True
        pr = tf_r.paragraphs[0]
        pr.text = fail_lbl
        pr.font.size = Pt(8.5)
        pr.font.bold = True
        pr.font.color.rgb = acc_col

    add_footer(s2)

    # =========================================================================
    # SLIDE 3: AERODYNAMIC GEOMETRY: DESIGNED FOR THE DRONE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_canvas(s3)
    add_header(s3, "Aerodynamic Geometry: Eliminating Wind Drift & Sand Rolling", "OPTIMIZED FOR HIGH-SPEED CONTINUOUS UAV BROADCAST")

    # Left Column: Conventional Sphere
    create_card(s3, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb_sp = s3.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(3.9))
    tf_sp = tb_sp.text_frame
    tf_sp.word_wrap = True

    p = tf_sp.paragraphs[0]
    p.text = "CONVENTIONAL DESIGN"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_CRIMSON

    p_sp_sub = tf_sp.add_paragraph()
    p_sp_sub.text = "Spherical Pellet Limitations"
    p_sp_sub.font.size = Pt(14)
    p_sp_sub.font.bold = True
    p_sp_sub.font.color.rgb = COLOR_NAVY
    p_sp_sub.space_before = Pt(2)

    p_sp_desc = tf_sp.add_paragraph()
    p_sp_desc.text = "Standard spherical balls behave poorly in desert aerial dispersion:"
    p_sp_desc.font.size = Pt(9.5)
    p_sp_desc.font.color.rgb = COLOR_MUTED
    p_sp_desc.space_before = Pt(3)

    sp_points = [
        "High Air Drag: Large aerodynamic drag area causes severe lateral drift in crosswinds (>3.6 m drift from 15 m release height).",
        "Endless Dune Rolling: Perfectly round profile rolls uncontrollably across sand under common 35 km/h Shamal winds.",
        "Swale Burial & Suffocation: Rolling pellets collect in dune hollows and get buried under 20–50 cm of sand, cutting off light and oxygen."
    ]
    for pt in sp_points:
        bp = tf_sp.add_paragraph()
        bp.text = f"✕  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(6)

    # Left Bottom Limitation Box
    create_card(s3, Inches(1.1), Inches(5.85), Inches(5.0), Inches(0.7), bg_color=COLOR_CARD_ALT)
    tb_l = s3.shapes.add_textbox(Inches(1.2), Inches(5.95), Inches(4.8), Inches(0.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    pl = tf_l.paragraphs[0]
    pl.text = "LIMITATION: High drift disperses seeds outside target areas; rolling leads to deep sand burial."
    pl.font.size = Pt(8.5)
    pl.font.color.rgb = COLOR_CRIMSON

    # Right Column: Nabat-BioDrop Ovoid
    create_card(s3, Inches(6.7), Inches(1.55), Inches(5.8), Inches(5.2))
    tb_ov = s3.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.2), Inches(3.9))
    tf_ov = tb_ov.text_frame
    tf_ov.word_wrap = True

    p = tf_ov.paragraphs[0]
    p.text = "ENGINEERED SOLUTION"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    p_ov_sub = tf_ov.add_paragraph()
    p_ov_sub.text = "Prolate Ovoid Geometry"
    p_ov_sub.font.size = Pt(14)
    p_ov_sub.font.bold = True
    p_ov_sub.font.color.rgb = COLOR_NAVY
    p_ov_sub.space_before = Pt(2)

    p_ov_desc = tf_ov.add_paragraph()
    p_ov_desc.text = "Purpose-engineered for high-speed continuous UAV broadcast (5 m/s):"
    p_ov_desc.font.size = Pt(9.5)
    p_ov_desc.font.color.rgb = COLOR_MUTED
    p_ov_desc.space_before = Pt(3)

    ov_points = [
        "Low Drag Profile: Streamlined ovoid shape cuts wind resistance, reducing lateral drift by 27% during continuous drone cruise.",
        "Passive Self-Righting: Forward center of gravity (CG at 35% from base) ensures the heavy keel leads in flight and lands first.",
        "Ground Self-Anchoring: Enters sand at 15.8 m/s, penetrating 10 mm deep on impact to lock upright and completely stop wind roll."
    ]
    for pt in ov_points:
        bp = tf_ov.add_paragraph()
        bp.text = f"✓  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(6)

    # Right Bottom Spec Badges (3 horizontal chips)
    badge_data = [
        ("29.0 × 26.5 mm", "ENVELOPE"),
        ("−27% DRIFT", "STABILITY"),
        ("10 mm ANCHOR", "ANTI-ROLL")
    ]
    bw = Inches(1.6)
    for bi, (b_val, b_tag) in enumerate(badge_data):
        bx = Inches(7.0) + bi * Inches(1.8)
        create_card(s3, bx, Inches(5.85), bw, Inches(0.7), bg_color=COLOR_CARD_ALT)
        tb_b = s3.shapes.add_textbox(bx + Inches(0.1), Inches(5.92), bw - Inches(0.2), Inches(0.55))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        pb1 = tf_b.paragraphs[0]
        pb1.text = b_val
        pb1.font.size = Pt(10.5)
        pb1.font.bold = True
        pb1.font.color.rgb = COLOR_EMERALD
        pb2 = tf_b.add_paragraph()
        pb2.text = b_tag
        pb2.font.size = Pt(8)
        pb2.font.bold = True
        pb2.font.color.rgb = COLOR_NAVY

    add_footer(s3)

    # =========================================================================
    # SLIDE 4: THERMAL ALBEDO SHIELD: SURVIVING MIDDAY HEAT
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_canvas(s4)
    add_header(s4, "Solar Defense: Reflecting Desert Heat to Save Embryos", "HIGH-ALBEDO KAOLIN MINERAL COATING REDUCES SURFACE TEMPERATURE BY 33°C")

    # Left Column: The Thermal Physics
    create_card(s4, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb_th = s4.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.7))
    tf_th = tb_th.text_frame
    tf_th.word_wrap = True

    p = tf_th.paragraphs[0]
    p.text = "PHYSICAL MECHANISM"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_GOLD

    p_sub = tf_th.add_paragraph()
    p_sub.text = "Thermal Equilibrium & Solar Defense"
    p_sub.font.size = Pt(14)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_NAVY
    p_sub.space_before = Pt(2)

    p_txt = tf_th.add_paragraph()
    p_txt.text = "Midday solar radiation (1,000 W/m²) heats unshaded sand and dark biochar to 75°C. Sustained exposure above 42°C causes irreversible embryo protein denaturation."
    p_txt.font.size = Pt(10)
    p_txt.font.color.rgb = COLOR_MUTED
    p_txt.space_before = Pt(4)

    th_points = [
        "Kaolin Mineral Shield: Formulated with a thin outer coat of high-purity natural Kaolin clay offering 78% solar reflectance.",
        "Equilibrium Cooling: Reduces surface equilibrium temperature from 74.7°C to 41.4°C (a 33.3°C thermal reduction).",
        "Safe Incubation Window: Maintains the inner seed chamber safely below the 42°C lethal threshold during peak summer sun.",
        "Zero Synthetic Polymers: Achieves complete thermal defense using 100% natural, non-toxic mineral albedo."
    ]
    for pt in th_points:
        bp = tf_th.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(5)

    # Right Top: Two Contrast Cards side-by-side
    create_card(s4, Inches(6.7), Inches(1.55), Inches(2.8), Inches(2.4))
    tb_c1 = s4.shapes.add_textbox(Inches(6.9), Inches(1.75), Inches(2.4), Inches(2.0))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    pc1_1 = tf_c1.paragraphs[0]
    pc1_1.text = "74.7°C"
    pc1_1.font.size = Pt(32)
    pc1_1.font.bold = True
    pc1_1.font.color.rgb = COLOR_CRIMSON
    pc1_2 = tf_c1.add_paragraph()
    pc1_2.text = "UNCOATED BIOCHAR"
    pc1_2.font.size = Pt(9.5)
    pc1_2.font.bold = True
    pc1_2.font.color.rgb = COLOR_NAVY
    pc1_2.space_before = Pt(2)
    pc1_3 = tf_c1.add_paragraph()
    pc1_3.text = "Absorbs 92% of solar heat; causes irreversible embryo denaturation."
    pc1_3.font.size = Pt(9)
    pc1_3.font.color.rgb = COLOR_MUTED
    pc1_3.space_before = Pt(4)

    create_card(s4, Inches(9.7), Inches(1.55), Inches(2.8), Inches(2.4))
    tb_c2 = s4.shapes.add_textbox(Inches(9.9), Inches(1.75), Inches(2.4), Inches(2.0))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    pc2_1 = tf_c2.paragraphs[0]
    pc2_1.text = "41.4°C"
    pc2_1.font.size = Pt(32)
    pc2_1.font.bold = True
    pc2_1.font.color.rgb = COLOR_EMERALD
    pc2_2 = tf_c2.add_paragraph()
    pc2_2.text = "KAOLIN SOLAR SHIELD"
    pc2_2.font.size = Pt(9.5)
    pc2_2.font.bold = True
    pc2_2.font.color.rgb = COLOR_NAVY
    pc2_2.space_before = Pt(2)
    pc2_3 = tf_c2.add_paragraph()
    pc2_3.text = "Reflects 78% of heat; maintains internal embryo viability."
    pc2_3.font.size = Pt(9)
    pc2_3.font.color.rgb = COLOR_MUTED
    pc2_3.space_before = Pt(4)

    # Right Bottom: Formulation Breakdown Card
    create_card(s4, Inches(6.7), Inches(4.15), Inches(5.8), Inches(2.6))
    tb_mat = s4.shapes.add_textbox(Inches(7.0), Inches(4.35), Inches(5.2), Inches(2.2))
    tf_mat = tb_mat.text_frame
    tf_mat.word_wrap = True

    p = tf_mat.paragraphs[0]
    p.text = "CIRCULAR BIO-COMPOSITE"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_m_sub = tf_mat.add_paragraph()
    p_m_sub.text = "100% Natural UAE Formulation (Zero Microplastics)"
    p_m_sub.font.size = Pt(13)
    p_m_sub.font.bold = True
    p_m_sub.font.color.rgb = COLOR_NAVY
    p_m_sub.space_before = Pt(2)

    mats = [
        "Date Palm Waste Biochar (32%): High carbon water retention and porous matrix.",
        "Calcium Bentonite Clay (28%): Moisture binding and structural cohesion.",
        "Kaolin Mineral Shield (20%): Outer high-albedo solar defense layer.",
        "Cold-Soluble Gum Arabic (12%): Rapid-release root escape binder."
    ]
    for m in mats:
        bp = tf_mat.add_paragraph()
        bp.text = f"•  {m}"
        bp.font.size = Pt(9)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(3)

    add_footer(s4)

    # =========================================================================
    # SLIDE 5: HYDROLOGICAL CATCHMENT & DEW SUPPRESSION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_canvas(s5)
    add_header(s5, "Hydrological Architecture: Harvesting Rain & Repelling Dew", "CONCAVE FUNNEL WATER CONCENTRATION & TIMED RAIN ACTIVATION")

    # Left Column: Concave Catchment Funnel
    create_card(s5, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb_f = s5.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(3.9))
    tf_f = tb_f.text_frame
    tf_f.word_wrap = True

    p = tf_f.paragraphs[0]
    p.text = "WATER CONCENTRATION"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    p_f_sub = tf_f.add_paragraph()
    p_f_sub.text = "12mm Concave Catchment Funnel"
    p_f_sub.font.size = Pt(14)
    p_f_sub.font.bold = True
    p_f_sub.font.color.rgb = COLOR_NAVY
    p_f_sub.space_before = Pt(2)

    p_f_desc = tf_f.add_paragraph()
    p_f_desc.text = "Directing 100% of intercepted precipitation straight into the seed core:"
    p_f_desc.font.size = Pt(9.5)
    p_f_desc.font.color.rgb = COLOR_MUTED
    p_f_desc.space_before = Pt(3)

    f_points = [
        "Inward Aperture: A 12 mm diameter crater channels rainwater downward directly into the central seed chamber.",
        "5x Concentration: In a typical 5 mm rain shower, the funnel catches 0.56 mL of liquid water right into the core.",
        "Zero Runoff Waste: Convex pellets shed water outward into dry sand; BioDrop captures and concentrates every drop.",
        "Natural Sand Mulch: Windblown sand gently settles in the funnel, creating a protective blanket that traps humidity."
    ]
    for pt in f_points:
        bp = tf_f.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(5)

    # Left Bottom Box
    create_card(s5, Inches(1.1), Inches(5.85), Inches(5.0), Inches(0.7), bg_color=COLOR_CARD_ALT)
    tb_fb = s5.shapes.add_textbox(Inches(1.2), Inches(5.95), Inches(4.8), Inches(0.5))
    tf_fb = tb_fb.text_frame
    tf_fb.word_wrap = True
    pfb = tf_fb.paragraphs[0]
    pfb.text = "HARVEST CAPACITY: 0.56 mL per pod in a 5 mm rain shower (5x vs convex pellets)."
    pfb.font.size = Pt(8.5)
    pfb.font.bold = True
    pfb.font.color.rgb = COLOR_EMERALD

    # Right Column: The Carnauba Wax Dew Barrier
    create_card(s5, Inches(6.7), Inches(1.55), Inches(5.8), Inches(5.2))
    tb_w = s5.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.2), Inches(3.9))
    tf_w = tb_w.text_frame
    tf_w.word_wrap = True

    p = tf_w.paragraphs[0]
    p.text = "PHASE ACTIVATION"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_GOLD

    p_w_sub = tf_w.add_paragraph()
    p_w_sub.text = "High-Melting Carnauba Dew Shield"
    p_w_sub.font.size = Pt(14)
    p_w_sub.font.bold = True
    p_w_sub.font.color.rgb = COLOR_NAVY
    p_w_sub.space_before = Pt(2)

    p_w_desc = tf_w.add_paragraph()
    p_w_desc.text = "Preventing lethal false germination from non-viable morning condensation:"
    p_w_desc.font.size = Pt(9.5)
    p_w_desc.font.color.rgb = COLOR_MUTED
    p_w_desc.space_before = Pt(3)

    w_points = [
        "The Morning Dew Trap: Light condensation (0.2 mm) evaporates in 90 minutes of sun, killing premature sprouts.",
        "High-Melting Carnauba (85°C): Unlike beeswax (which melts at 62°C in summer sand), carnauba remains rock-solid in desert heat.",
        "Threshold Protection: The hydrophobic seal repels light morning moisture, keeping seeds safely dormant during dry spells.",
        "Rainstorm Activation: A genuine rainfall (≥5 mm) overcomes the threshold, penetrating the core and triggering active growth."
    ]
    for pt in w_points:
        bp = tf_w.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(5)

    # Right Bottom Box
    create_card(s5, Inches(7.0), Inches(5.85), Inches(5.2), Inches(0.7), bg_color=COLOR_CARD_ALT)
    tb_wb = s5.shapes.add_textbox(Inches(7.1), Inches(5.95), Inches(5.0), Inches(0.5))
    tf_wb = tb_wb.text_frame
    tf_wb.word_wrap = True
    pwb = tf_wb.paragraphs[0]
    pwb.text = "ACTIVATION THRESHOLD: Repels dew (<0.5 mm); activates only when rain exceeds 5 mm."
    pwb.font.size = Pt(8.5)
    pwb.font.bold = True
    pwb.font.color.rgb = COLOR_GOLD

    add_footer(s5)

    # =========================================================================
    # SLIDE 6: ROOT MECHANICAL FREEDOM & NURSE GUILD ECOLOGY
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_canvas(s6)
    add_header(s6, "Biological Emergence: Fast-Dissolving Keel & Nurse Ecology", "PREVENTING ROOT ENTRAPMENT & ACCELERATING NATIVE ESTABLISHMENT")

    # Left Column: Water-Soluble Keel
    create_card(s6, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb_k = s6.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(3.9))
    tf_k = tb_k.text_frame
    tf_k.word_wrap = True

    p = tf_k.paragraphs[0]
    p.text = "MECHANICAL FREEDOM"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    p_k_sub = tf_k.add_paragraph()
    p_k_sub.text = "Water-Soluble Root Escape Keel"
    p_k_sub.font.size = Pt(14)
    p_k_sub.font.bold = True
    p_k_sub.font.color.rgb = COLOR_NAVY
    p_k_sub.space_before = Pt(2)

    p_k_desc = tf_k.add_paragraph()
    p_k_desc.text = "Eliminating the 'Concrete Tomb' failure mode:"
    p_k_desc.font.size = Pt(9.5)
    p_k_desc.font.color.rgb = COLOR_MUTED
    p_k_desc.space_before = Pt(3)

    k_points = [
        "Turgor Limit: An emerging plant radicle exerts a maximum pushing force of only 0.8–1.2 MPa.",
        "The Hard Shell Trap: Standard dried clay shells exceed 2.5 MPa, physically trapping emerging roots inside.",
        "Fast-Dissolve Gum Arabic: Formulated with 12% cold-soluble plant gum that dissolves within 20 minutes in water.",
        "Effortless Exit: Matrix shear drops to <0.12 MPa (10x below root limit), letting roots push downward into moist sand."
    ]
    for pt in k_points:
        bp = tf_k.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(5)

    # Left Integrated Metric Box
    create_card(s6, Inches(1.1), Inches(5.75), Inches(5.0), Inches(0.8), bg_color=COLOR_CARD_ALT)
    tb_kb = s6.shapes.add_textbox(Inches(1.2), Inches(5.82), Inches(4.8), Inches(0.65))
    tf_kb = tb_kb.text_frame
    tf_kb.word_wrap = True
    pkb1 = tf_kb.paragraphs[0]
    pkb1.text = "20 MINS  |  < 0.12 MPa WET SHEAR"
    pkb1.font.size = Pt(11)
    pkb1.font.bold = True
    pkb1.font.color.rgb = COLOR_EMERALD
    pkb2 = tf_kb.add_paragraph()
    pkb2.text = "Keel dissolves rapidly; matrix resistance drops 10x below baby root turgor limit."
    pkb2.font.size = Pt(8.5)
    pkb2.font.color.rgb = COLOR_MUTED

    # Right Column: Native Nurse Guild Ecology
    create_card(s6, Inches(6.7), Inches(1.55), Inches(5.8), Inches(5.2))
    tb_ng = s6.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.2), Inches(3.9))
    tf_ng = tb_ng.text_frame
    tf_ng.word_wrap = True

    p = tf_ng.paragraphs[0]
    p.text = "ECOLOGICAL SYNERGY"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_GOLD

    p_ng_sub = tf_ng.add_paragraph()
    p_ng_sub.text = "Native Nurse Guild Ecology"
    p_ng_sub.font.size = Pt(14)
    p_ng_sub.font.bold = True
    p_ng_sub.font.color.rgb = COLOR_NAVY
    p_ng_sub.space_before = Pt(2)

    p_ng_desc = tf_ng.add_paragraph()
    p_ng_desc.text = "Two-stage plant succession engineered for UAE arid dynamics:"
    p_ng_desc.font.size = Pt(9.5)
    p_ng_desc.font.color.rgb = COLOR_MUTED
    p_ng_desc.space_before = Pt(3)

    ng_points = [
        "Pioneer Nurse Grass (Stipagrostis plumosa): Germinates in 48 hours to create surface root nets that lock shifting sand.",
        "Climax Shrub (Haloxylon salicornicum): Slower starter; takes shelter in grass shade and grows deep perennial roots.",
        "Diffuse Light Veil: Semi-translucent mineral cover filters 10–20% of sunlight—activating growth without scorching.",
        "Aerated Porosity: Open pore channels guarantee oxygen supply, preventing seed suffocation during wet spells."
    ]
    for pt in ng_points:
        bp = tf_ng.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(5)

    # Right Integrated Metric Box
    create_card(s6, Inches(7.0), Inches(5.75), Inches(5.2), Inches(0.8), bg_color=COLOR_CARD_ALT)
    tb_ngb = s6.shapes.add_textbox(Inches(7.1), Inches(5.82), Inches(5.0), Inches(0.65))
    tf_ngb = tb_ngb.text_frame
    tf_ngb.word_wrap = True
    png1 = tf_ngb.paragraphs[0]
    png1.text = "2-STAGE GUILD  |  SYNERGISTIC SUCCESSION"
    png1.font.size = Pt(11)
    png1.font.bold = True
    png1.font.color.rgb = COLOR_GOLD
    png2 = tf_ngb.add_paragraph()
    png2.text = "Pioneer nurse grass stabilizes moving sand, enabling long-term climax shrub establishment."
    png2.font.size = Pt(8.5)
    png2.font.color.rgb = COLOR_MUTED

    add_footer(s6)

    # =========================================================================
    # SLIDE 7: EMPIRICAL VALIDATION PROTOCOL (3 COLUMNS)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_canvas(s7)
    add_header(s7, "Solution Readiness: Empirical Validation Protocol", "PROGRESSION FROM FIRST-PRINCIPLES MODELING TO ABU DHABI FIELD TRIALS")

    stages = [
        ("STAGE 1 / BENCH AUDIT",
         "Physical & Mechanical",
         "Dimensional and impact integrity",
         [
             "Dimensional Audit (n=20): Digital caliper check ensuring compliance with 25–30 mm envelope.",
             "Compressive Strength (n=10): Digital force gauge benchmark targeting >50 N fracture force.",
             "15m Sand Drop Test (n=30): Validating ≥95% survival and 10 mm sand anchoring."
         ],
         "BENCHMARK: >50 N FRACTURE FORCE",
         COLOR_NAVY),
        ("STAGE 2 / LAB PROXY",
         "Germination & Moisture",
         "Rapid biological benchmarking",
         [
             "Fast Arid Proxy (Lepidium sativum): 24-hour emergence benchmark for rapid testing.",
             "Comparative Assays (4x25 seeds): Encapsulated pods vs. bare controls under stress.",
             "Dissolution Auditing: Confirming keel softens within 20 minutes in water."
         ],
         "BENCHMARK: 24-HOUR EMERGENCE PROXY",
         COLOR_GOLD),
        ("STAGE 3 / FIELD TRIALS",
         "Operational Flight Trials",
         "Phase 3 deployment in Abu Dhabi",
         [
             "Pilot Compounding: Compounding 2,000 ready-to-deploy units for Nabat drone fleet.",
             "High-Speed Broadcast: Dispensing at 5 m/s cruise across designated restoration plots.",
             "Emergence Monitoring: Auditing plant establishment and dune stabilization."
         ],
         "TARGET: 2,000 FLIGHT-READY UNITS",
         COLOR_EMERALD)
    ]

    for i, (stag, s_title, s_sub, s_bullets, s_bench, acc_col) in enumerate(stages):
        cx = Inches(0.8) + i * Inches(4.0)
        create_card(s7, cx, Inches(1.55), col_w, Inches(5.2))

        tb = s7.shapes.add_textbox(cx + Inches(0.25), Inches(1.8), col_w - Inches(0.5), Inches(3.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = stag
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = acc_col

        p2 = tf.add_paragraph()
        p2.text = s_title
        p2.font.size = Pt(13.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = s_sub
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = COLOR_MUTED
        p3.space_before = Pt(2)

        for b in s_bullets:
            bp = tf.add_paragraph()
            bp.text = f"•  {b}"
            bp.font.size = Pt(9.5)
            bp.font.color.rgb = COLOR_NAVY_LIGHT
            bp.space_before = Pt(6)

        create_card(s7, cx + Inches(0.25), Inches(5.95), col_w - Inches(0.5), Inches(0.6), bg_color=COLOR_CARD_ALT)
        tb_r = s7.shapes.add_textbox(cx + Inches(0.3), Inches(6.05), col_w - Inches(0.6), Inches(0.4))
        tf_r = tb_r.text_frame
        tf_r.word_wrap = True
        pr = tf_r.paragraphs[0]
        pr.text = s_bench
        pr.font.size = Pt(8.5)
        pr.font.bold = True
        pr.font.color.rgb = acc_col

    add_footer(s7)

    # =========================================================================
    # SLIDE 8: INDUSTRIAL SCALABILITY & NABAT UAV COMPATIBILITY
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_canvas(s8)
    add_header(s8, "Industrial Scalability: 50,000 Pods / Day & High Drone Coverage", "CONTINUOUS DISC AGGLOMERATION & EAD ABU DHABI DENSITY INTEGRATION")

    # Left Column: Production Flow
    create_card(s8, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb_m = s8.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(3.9))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    p = tf_m.paragraphs[0]
    p.text = "MANUFACTURING SCALABILITY"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_m_sub = tf_m.add_paragraph()
    p_m_sub.text = "High-Volume Disc Granulation"
    p_m_sub.font.size = Pt(14)
    p_m_sub.font.bold = True
    p_m_sub.font.color.rgb = COLOR_NAVY
    p_m_sub.space_before = Pt(2)

    p_m_desc = tf_m.add_paragraph()
    p_m_desc.text = "Continuous single-stage industrial agglomeration:"
    p_m_desc.font.size = Pt(9.5)
    p_m_desc.font.color.rgb = COLOR_MUTED
    p_m_desc.space_before = Pt(3)

    flow_pts = [
        "Continuous Disc Granulation: Scaled on standard 2.2 m agricultural disc granulators (45° tilt, 18 RPM) with concave tooling.",
        "Single-Step Forming: Continuous pan agglomeration followed by rotary mineral coating avoids multi-part molds or manual assembly.",
        "Embryo-Safe Dehydration: Fluidized bed drying at 38°C preserves seed embryo viability and mycorrhizal spores.",
        "High Line Throughput: One continuous line yields 50,000 pods per day (1.2 tonnes/day), meeting large-scale restoration goals."
    ]
    for pt in flow_pts:
        bp = tf_m.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(5)

    create_card(s8, Inches(1.1), Inches(5.75), Inches(5.0), Inches(0.8), bg_color=COLOR_CARD_ALT)
    tb_mb = s8.shapes.add_textbox(Inches(1.2), Inches(5.82), Inches(4.8), Inches(0.65))
    tf_mb = tb_mb.text_frame
    tf_mb.word_wrap = True
    pm1 = tf_mb.paragraphs[0]
    pm1.text = "50,000 PODS / DAY / LINE"
    pm1.font.size = Pt(11)
    pm1.font.bold = True
    pm1.font.color.rgb = COLOR_NAVY
    pm2 = tf_mb.add_paragraph()
    pm2.text = "Standard continuous industrial granulator output (1.2 tonnes/day)."
    pm2.font.size = Pt(8.5)
    pm2.font.color.rgb = COLOR_MUTED

    # Right Column: Drone Payload & Hectare Impact
    create_card(s8, Inches(6.7), Inches(1.55), Inches(5.8), Inches(5.2))
    tb_d = s8.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.2), Inches(3.9))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True

    p = tf_d.paragraphs[0]
    p.text = "DRONE INTEGRATION"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    p_d_sub = tf_d.add_paragraph()
    p_d_sub.text = "Drone Payload & Field Coverage"
    p_d_sub.font.size = Pt(14)
    p_d_sub.font.bold = True
    p_d_sub.font.color.rgb = COLOR_NAVY
    p_d_sub.space_before = Pt(2)

    p_d_desc = tf_d.add_paragraph()
    p_d_desc.text = "Operational metrics grounded in EAD Abu Dhabi restoration trials:"
    p_d_desc.font.size = Pt(9.5)
    p_d_desc.font.color.rgb = COLOR_MUTED
    p_d_desc.space_before = Pt(3)

    d_pts = [
        "2,550 Pods per Flight: Ultralight 9.8g mass enables 2,550 pods on a standard 25 kg UAV (+155% vs. heavy 25g pellets).",
        "Rangeland Restoration: 1,500 pods/ha achieves 300–500 mature shrubs/ha at a low carrier cost of AED 340.50 / hectare.",
        "Dune Stabilization: 4,500 pods/ha locks moving sand at AED 1,021.50 / hectare (matching EAD 6.5M seed trial).",
        "Sortie Coverage: A single drone flight restores up to 1.7 hectares of rangeland or 0.6 hectares of critical sand dunes."
    ]
    for pt in d_pts:
        bp = tf_d.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(5)

    create_card(s8, Inches(7.0), Inches(5.75), Inches(5.2), Inches(0.8), bg_color=COLOR_CARD_ALT)
    tb_db = s8.shapes.add_textbox(Inches(7.1), Inches(5.82), Inches(5.0), Inches(0.65))
    tf_db = tb_db.text_frame
    tf_db.word_wrap = True
    pd1 = tf_db.paragraphs[0]
    pd1.text = "2,550 PODS / FLIGHT  |  1.7 HECTARES"
    pd1.font.size = Pt(11)
    pd1.font.bold = True
    pd1.font.color.rgb = COLOR_EMERALD
    pd2 = tf_db.add_paragraph()
    pd2.text = "+155% payload capacity vs. heavy pellets; high aerial restoration throughput."
    pd2.font.size = Pt(8.5)
    pd2.font.color.rgb = COLOR_MUTED

    add_footer(s8)

    # =========================================================================
    # SLIDE 9: TECHNO-ECONOMIC VIABILITY: AED 0.23 PER CARRIER
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_canvas(s9)
    add_header(s9, "Techno-Economic Viability: AED 0.23 per Carrier", "43% SAFETY MARGIN BELOW THE ASPIRE AED 0.40 CEILING")

    # Left Column: Cost Breakdown
    create_card(s9, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb_c = s9.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.7))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True

    p = tf_c.paragraphs[0]
    p.text = "UNIT ECONOMICS"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    p_sub = tf_c.add_paragraph()
    p_sub.text = "Factory-Gate Unit Cost Breakdown"
    p_sub.font.size = Pt(14)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_NAVY
    p_sub.space_before = Pt(2)

    p_desc = tf_c.add_paragraph()
    p_desc.text = "Upcycling local date palm agricultural waste and domestic bentonite clay minimizes bill-of-materials cost while maintaining industrial consistency:"
    p_desc.font.size = Pt(9.5)
    p_desc.font.color.rgb = COLOR_MUTED
    p_desc.space_before = Pt(3)

    c_bars = [
        ("Raw Materials", "AED 0.10", "Date palm biochar, bentonite, kaolin, gum, and native seeds"),
        ("Labor & Conversion", "AED 0.05", "Automated continuous disc granulation and fluidized bed drying"),
        ("Capex & Packaging", "AED 0.08", "Plant depreciation over 5M units and bulk biodegradable packaging")
    ]
    for b_title, b_val, b_desc in c_bars:
        bp1 = tf_c.add_paragraph()
        bp1.text = f"•  {b_title}: {b_val}"
        bp1.font.size = Pt(10.5)
        bp1.font.bold = True
        bp1.font.color.rgb = COLOR_NAVY
        bp1.space_before = Pt(6)

        bp2 = tf_c.add_paragraph()
        bp2.text = f"   {b_desc}"
        bp2.font.size = Pt(9)
        bp2.font.color.rgb = COLOR_MUTED

    p_sum = tf_c.add_paragraph()
    p_sum.text = "Total factory-gate cost is AED 0.227 per pod, providing a 43.1% safety margin (17 fils buffer) below ASPIRE's AED 0.40 ceiling."
    p_sum.font.size = Pt(9.5)
    p_sum.font.bold = True
    p_sum.font.color.rgb = COLOR_EMERALD
    p_sum.space_before = Pt(8)

    # Right Top: Two Contrast Cards
    create_card(s9, Inches(6.7), Inches(1.55), Inches(2.8), Inches(2.3))
    tb_cs1 = s9.shapes.add_textbox(Inches(6.9), Inches(1.75), Inches(2.4), Inches(1.9))
    tf_cs1 = tb_cs1.text_frame
    tf_cs1.word_wrap = True
    pcs1_1 = tf_cs1.paragraphs[0]
    pcs1_1.text = "AED 0.23"
    pcs1_1.font.size = Pt(30)
    pcs1_1.font.bold = True
    pcs1_1.font.color.rgb = COLOR_EMERALD
    pcs1_2 = tf_cs1.add_paragraph()
    pcs1_2.text = "NABAT-BIODROP COST"
    pcs1_2.font.size = Pt(9.5)
    pcs1_2.font.bold = True
    pcs1_2.font.color.rgb = COLOR_NAVY
    pcs1_2.space_before = Pt(2)
    pcs1_3 = tf_cs1.add_paragraph()
    pcs1_3.text = "Itemized factory-gate cost at 1M unit scale."
    pcs1_3.font.size = Pt(9)
    pcs1_3.font.color.rgb = COLOR_MUTED
    pcs1_3.space_before = Pt(4)

    create_card(s9, Inches(9.7), Inches(1.55), Inches(2.8), Inches(2.3))
    tb_cs2 = s9.shapes.add_textbox(Inches(9.9), Inches(1.75), Inches(2.4), Inches(1.9))
    tf_cs2 = tb_cs2.text_frame
    tf_cs2.word_wrap = True
    pcs2_1 = tf_cs2.paragraphs[0]
    pcs2_1.text = "AED 0.40"
    pcs2_1.font.size = Pt(30)
    pcs2_1.font.bold = True
    pcs2_1.font.color.rgb = COLOR_NAVY
    pcs2_2 = tf_cs2.add_paragraph()
    pcs2_2.text = "ASPIRE CEILING CAP"
    pcs2_2.font.size = Pt(9.5)
    pcs2_2.font.bold = True
    pcs2_2.font.color.rgb = COLOR_NAVY
    pcs2_2.space_before = Pt(2)
    pcs2_3 = tf_cs2.add_paragraph()
    pcs2_3.text = "Challenge economic ceiling threshold."
    pcs2_3.font.size = Pt(9)
    pcs2_3.font.color.rgb = COLOR_MUTED
    pcs2_3.space_before = Pt(4)

    # Right Bottom: Sensitivity Card
    create_card(s9, Inches(6.7), Inches(4.05), Inches(5.8), Inches(2.7))
    tb_res = s9.shapes.add_textbox(Inches(7.0), Inches(4.25), Inches(5.2), Inches(2.3))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True

    p = tf_res.paragraphs[0]
    p.text = "STRESS RESILIENCE"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_GOLD

    p_r_sub = tf_res.add_paragraph()
    p_r_sub.text = "Financial Sensitivity & Shock Resistance"
    p_r_sub.font.size = Pt(13)
    p_r_sub.font.bold = True
    p_r_sub.font.color.rgb = COLOR_NAVY
    p_r_sub.space_before = Pt(2)

    shocks = [
        "+50% Labor Spike: Unit cost rises to AED 0.25 (Still −36% below ceiling).",
        "+100% Seed Price Shock: Unit cost rises to AED 0.29 (Still −28% below ceiling).",
        "Extreme Combined Shock: Model survives up to +150% native seed price surges while remaining fully under budget."
    ]
    for sh in shocks:
        bp = tf_res.add_paragraph()
        bp.text = f"•  {sh}"
        bp.font.size = Pt(9)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(4)

    add_footer(s9)

    # =========================================================================
    # SLIDE 10: EXECUTION ROADMAP, TEAM & UAE ALIGNMENT
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_canvas(s10)
    add_header(s10, "Project Execution: Roadmap, Team & National Alignment", "DELIVERING 2,000 FIELD-READY SEED CARRIERS BY JANUARY 2027")

    # Top: 4-Milestone Schedule Flow
    m_boxes = [
        ("PHASE 1: PROPOSAL", "Nov 2026", "First-principles modeling, supplier mapping, baseline specs.", COLOR_NAVY),
        ("PHASE 2: LAB PROTOTYPE", "Dec 2026", "Semi-finalist pitch, drop assays, proxy germination.", COLOR_GOLD),
        ("PHASE 3: PILOT BATCH", "1 Jan 2027", "Delivery of 2,000 ready-to-deploy units to Nabat drone fleet.", COLOR_EMERALD),
        ("DESERT VALIDATION", "Q1 2027", "Live UAV drop trials and vegetation emergence auditing in Abu Dhabi.", COLOR_NAVY)
    ]

    mw = Inches(2.75)
    for i, (m_tag, m_date, m_desc, acc_col) in enumerate(m_boxes):
        mx = Inches(0.8) + i * Inches(2.98)
        create_card(s10, mx, Inches(1.55), mw, Inches(2.0))

        tb = s10.shapes.add_textbox(mx + Inches(0.15), Inches(1.7), mw - Inches(0.3), Inches(1.7))
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
        p3.space_before = Pt(4)

    # Bottom Left: Team Profile
    create_card(s10, Inches(0.8), Inches(3.75), Inches(5.6), Inches(3.0))
    tb_tm = s10.shapes.add_textbox(Inches(1.1), Inches(3.95), Inches(5.0), Inches(2.6))
    tf_tm = tb_tm.text_frame
    tf_tm.word_wrap = True

    p = tf_tm.paragraphs[0]
    p.text = "LEADERSHIP & IP"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p_t_sub = tf_tm.add_paragraph()
    p_t_sub.text = "Lead Innovator Profile"
    p_t_sub.font.size = Pt(13.5)
    p_t_sub.font.bold = True
    p_t_sub.font.color.rgb = COLOR_NAVY
    p_t_sub.space_before = Pt(2)

    t_pts = [
        "Mohamed Shameel: Independent Applied Engineering & Computational Modeling. Grassroots self-directed research with zero corporate overhead.",
        "Agile Execution: Rapid prototyping capability with direct access to domestic UAE material suppliers across Abu Dhabi, Dubai, and Sharjah.",
        "100% Clean IP: Proprietary independent architecture; non-exclusive testing license granted to ASPIRE and Nabat AI Technologies.",
        "Zero Prior Encumbrance: Completely unencumbered solution with no competing grant or corporate restrictions."
    ]
    for pt in t_pts:
        bp = tf_tm.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(3)

    # Bottom Right: National Strategic Alignment
    create_card(s10, Inches(6.7), Inches(3.75), Inches(5.8), Inches(3.0))
    tb_al = s10.shapes.add_textbox(Inches(7.0), Inches(3.95), Inches(5.2), Inches(2.6))
    tf_al = tb_al.text_frame
    tf_al.word_wrap = True

    p = tf_al.paragraphs[0]
    p.text = "NATIONAL STRATEGY"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    p_a_sub = tf_al.add_paragraph()
    p_a_sub.text = "Strategic Alignment to UAE Vision"
    p_a_sub.font.size = Pt(13.5)
    p_a_sub.font.bold = True
    p_a_sub.font.color.rgb = COLOR_NAVY
    p_a_sub.space_before = Pt(2)

    al_pts = [
        "UAE Net Zero 2050: Accelerated biological carbon sequestration through scalable dryland revegetation.",
        "National Biodiversity Strategy 2031: Large-scale habitat rehabilitation utilizing indigenous desert flora.",
        "Circular Bioeconomy: Upcycling date palm agricultural waste into high-tech ecological restoration carriers.",
        "Drone-First Restoration: Seamless integration with Nabat's autonomous UAV fleet for cost-effective national impact."
    ]
    for pt in al_pts:
        bp = tf_al.add_paragraph()
        bp.text = f"•  {pt}"
        bp.font.size = Pt(9)
        bp.font.color.rgb = COLOR_NAVY_LIGHT
        bp.space_before = Pt(3)

    add_footer(s10)

    # Save presentation
    prs.save(output_path)
    print(f"[SUCCESS] Deep-tech presentation generated successfully: {output_path}")

if __name__ == "__main__":
    create_deck()
