#!/usr/bin/env python3
"""
Fix index5.html as per requirements.
"""
content = open('/home/user/ExcelinDigital/index5.html').read()

# Helper: the literal backslash-u escape sequences used in the JS bundle
# em-dash:
EM = '\\u2014'       # 6 chars: —
RQ = '\\u2019'       # right single quote: ’
CDOT = '\\u00b7'     # middle dot: ·
SLASH = '\\u002F'    # forward slash: /
QUOT = '\\"'         # escaped double quote inside JS string

# ── A) Fix "How an Engagement Runs" step descriptions ─────────────────────────

# Step 1
old1 = (
    'We open by stress-testing the challenge itself. Our expert uses bespoke AI agents to scan '
    'organisational data, benchmark against sector patterns, and surface blind spots faster than '
    f'traditional diagnostics allow {EM} confirming whether the problem is worth solving at this '
    'level of investment before anything else moves.'
)
new1 = (
    f'Stress-testing the challenge. Our experts dive into organizational data, and interview your '
    f'team to build a deep understanding of challenges and objectives benchmark against sector '
    f'patterns, and surface blind spots {EM}.'
)
assert old1 in content, f"Step 1 old text NOT found! Sample: {repr(old1[:80])}"
content = content.replace(old1, new1, 1)
assert new1 in content, "Step 1 replacement failed"
print("✓ Step 1")

# Step 2
old2 = (
    f'With the baseline locked, we go deep. AI-assisted analysis accelerates option modelling, '
    f'scenario testing, and benchmarking {EM} giving our expert the processing headroom to focus on '
    f'judgment, not data gathering. The output is a ranked, decision-ready recommendation set with '
    f'the rigour of a strategy house and none of the lag.'
)
new2 = (
    f'With the baseline locked, we go deep. AI-assisted analysis accelerates targeted benchmarking, '
    f'option modelling, and scenario testing {EM} giving our expert the processing headroom to focus '
    f'on judgment, not data gathering, with the rigor of a tier-1 strategy house toolkits and '
    f'deliverables.'
)
assert old2 in content, f"Step 2 old text NOT found!"
content = content.replace(old2, new2, 1)
assert new2 in content, "Step 2 replacement failed"
print("✓ Step 2")

# Step 3
old3 = (
    f'As the analysis unfolds, your leaders learn the domain alongside it. Sessions are tailored '
    f'and AI-augmented {EM} your team isn{RQ}t just taught concepts, they practise applying AI '
    f'tools to the actual decisions in front of them. Fluency is built in context, not in a classroom.'
)
new3 = (
    f'As the analysis unfolds, your leaders learn the domain alongside it. Learning sessions are '
    f'tailored and AI-augmented {EM} your team isn{RQ}t just exploring concepts, they practice '
    f'applying AI tools to the actual decisions in front of them. Fluency is built in context.'
)
assert old3 in content, f"Step 3 old text NOT found!"
content = content.replace(old3, new3, 1)
assert new3 in content, "Step 3 replacement failed"
print("✓ Step 3")

# Step 4
old4 = (
    f'The agents, tools, and trained skills built and used by our expert during the engagement '
    f'don{RQ}t leave with us. They are documented, transferred, and walked through with your team '
    f'{EM} purpose-built for your workflows, ready to run without us in the room.'
)
new4 = (
    f'The purpose-built agents, tools, and trained skills used by our expert during the engagement '
    f'are handed. They represent the key for ongoing expertise at the fingertips of your team.'
)
assert old4 in content, f"Step 4 old text NOT found!"
content = content.replace(old4, new4, 1)
assert new4 in content, "Step 4 replacement failed"
print("✓ Step 4")

# Step 5
old5 = (
    f'We close with a structured handoff {EM} a KPI framework, a governance model, and a clear '
    f'next-decision brief. You leave with the answer, the capability, and the tools. '
    f'We leave with nothing to come back for.'
)
new5 = (
    f'We close with a structured handoff {EM} a KPI framework, a governance model, and a clear '
    f'next-decision brief. You leave with the answer, the capability, and the tools.'
)
assert old5 in content, f"Step 5 old text NOT found!"
content = content.replace(old5, new5, 1)
assert new5 in content, "Step 5 replacement failed"
print("✓ Step 5")

# ── B) CSS alignment is already fixed (grid-template-rows: auto auto 1fr auto) ─
# (Applied in previous run)
new_grid_count = content.count('grid-template-rows: auto auto 1fr auto')
old_grid_count = content.count('grid-template-rows: auto auto auto 1fr')
print(f"✓ CSS grid: {new_grid_count} fixed, {old_grid_count} remaining (expected 2 = themes.theme)")

# ── C) Remove London from footer ──────────────────────────────────────────────
old_london = f'Dubai {CDOT} London'
new_london = 'Dubai'
if old_london in content:
    content = content.replace(old_london, new_london, 1)
    print("✓ London footer removed")
elif 'London' not in content:
    print("✓ London already removed")
else:
    print(f"! London still in content, looking for: {repr(old_london)}")
    import re
    for m in re.finditer('London', content):
        print('  Found at:', m.start(), repr(content[m.start()-80:m.start()+80]))

# ── D) Replace 50 years with trend reversal image ─────────────────────────────
old_50 = (
    f'50<em style={QUOT}font-size:0.55em;letter-spacing:0;{QUOT}> yrs<{SLASH}em><{SLASH}div>'
    f'<div class={QUOT}l{QUOT}>Multinational delivery across Amazon, Visa, Google, '
    f'Strategy&amp; and Booz Allen.<{SLASH}div>'
    f'<div class={QUOT}s{QUOT}>Leaders<{SLASH}div>'
)

if old_50 in content:
    # Build the SVG trend chart - using escaped quotes inside JS string
    # Forward slashes in closing SVG tags are OK since they're literal in this JS context
    svg = (
        f'<svg viewBox={QUOT}0 0 200 88{QUOT} xmlns={QUOT}http://www.w3.org/2000/svg{QUOT} '
        f'style={QUOT}width:200px;height:88px;display:block;{QUOT}>'
        # Subtle baseline
        f'<line x1={QUOT}10{QUOT} y1={QUOT}72{QUOT} x2={QUOT}190{QUOT} y2={QUOT}72{QUOT} '
        f'stroke={QUOT}rgba(0,46,95,0.15){QUOT} stroke-width={QUOT}1{QUOT}/>'
        # Declining trend line (blue)
        f'<polyline points={QUOT}18,28 98,62{QUOT} stroke={QUOT}#002E5F{QUOT} '
        f'stroke-width={QUOT}2.5{QUOT} fill={QUOT}none{QUOT} stroke-linecap={QUOT}round{QUOT}/>'
        # Rising trend line (amber)
        f'<polyline points={QUOT}98,62 182,22{QUOT} stroke={QUOT}#C96A20{QUOT} '
        f'stroke-width={QUOT}2.5{QUOT} fill={QUOT}none{QUOT} stroke-linecap={QUOT}round{QUOT}/>'
        # Arrow at end
        f'<polygon points={QUOT}182,22 174,26 176,18{QUOT} fill={QUOT}#C96A20{QUOT}/>'
        # Turning point
        f'<circle cx={QUOT}98{QUOT} cy={QUOT}62{QUOT} r={QUOT}5{QUOT} fill={QUOT}#C96A20{QUOT}/>'
        f'<circle cx={QUOT}98{QUOT} cy={QUOT}62{QUOT} r={QUOT}2.5{QUOT} fill={QUOT}#fff{QUOT}/>'
        # Start dot
        f'<circle cx={QUOT}18{QUOT} cy={QUOT}28{QUOT} r={QUOT}3{QUOT} fill={QUOT}#002E5F{QUOT}/>'
        # Labels
        f'<text x={QUOT}10{QUOT} y={QUOT}16{QUOT} '
        f'font-family={QUOT}-apple-system,sans-serif{QUOT} font-size={QUOT}12{QUOT} '
        f'font-weight={QUOT}700{QUOT} fill={QUOT}#002E5F{QUOT}>-7%</text>'
        f'<text x={QUOT}145{QUOT} y={QUOT}16{QUOT} '
        f'font-family={QUOT}-apple-system,sans-serif{QUOT} font-size={QUOT}12{QUOT} '
        f'font-weight={QUOT}700{QUOT} fill={QUOT}#C96A20{QUOT}>+5%</text>'
        f'<{SLASH}svg>'
    )

    new_50 = (
        f'<div style={QUOT}line-height:0;margin-bottom:4px;{QUOT}>{svg}<{SLASH}div><{SLASH}div>'
        f'<div class={QUOT}l{QUOT}>Reversed a declining -7% declining revenue trend to +5% '
        f'growth via digital transformation.<{SLASH}div>'
        f'<div class={QUOT}s{QUOT}>Ref {CDOT} MENA<{SLASH}div>'
    )

    content = content.replace(old_50, new_50, 1)
    assert 'declining revenue trend to +5%' in content, "D) SVG replace failed"
    print("✓ Receipts: 50 years replaced with trend SVG")
else:
    print("! Receipts old_50 not found, checking nearby content...")
    import re
    pos = content.find('50<em')
    if pos >= 0:
        print("  Found '50<em' at", pos, ":", repr(content[pos-20:pos+200]))

# ── Final verification ─────────────────────────────────────────────────────────
print("\n── Final Verification ─────────────────────────────────────────────────")
checks = [
    ('Stress-testing the challenge. Our experts', 'Step 1'),
    ('targeted benchmarking, option modelling', 'Step 2'),
    ('Learning sessions are tailored', 'Step 3'),
    ('are handed. They represent the key', 'Step 4'),
    ('the tools.', 'Step 5 end'),
    ('We leave with nothing', False, 'Step 5 old sentence absent'),
    ('London', False, 'London removed'),
    ('grid-template-rows: auto auto 1fr auto', 'CSS grid fix'),
    ('declining revenue trend to +5%', 'Receipts trend'),
    (f'Ref {CDOT} MENA', 'Receipts Ref MENA'),
]
all_ok = True
for check in checks:
    if len(check) == 2:
        s, label = check
        found = s in content
        ok = found
    else:
        s, found_expected, label = check
        found = s in content
        ok = (found == found_expected) if isinstance(found_expected, bool) else found
    status = '✓' if ok else '✗'
    print(f"  {status} {label}")
    if not ok:
        all_ok = False

if all_ok:
    open('/home/user/ExcelinDigital/index5.html', 'w').write(content)
    print("\n✓ All checks passed. File saved.")
else:
    print("\n✗ Some checks failed. NOT saving (review above).")
